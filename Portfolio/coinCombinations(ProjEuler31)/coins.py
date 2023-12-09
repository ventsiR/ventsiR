import os
import math

#input function with hardcoded newline tab on line end and r as reset
def myInput(displayText):
    userIn = input(displayText + "\n\t>")
    if userIn == "r":
        return main()
    else:
        return userIn

def main():
    #get user inputs
    os.system('cls' if os.name == 'nt' else 'clear')
    userIn = myInput("--------------------------------------\nIn the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:\n\n\t1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).\n\nIt is possible to make £2 in the following way:\n\n\t1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p\n\nHow many different ways can £2 be made using any number of coins?\n--------------------------------------\n\n\n--------------------------------------\nThis program answers this question for any target and collection of coins of unique value you input.\n--------------------------------------\n\n\n--------------------------------------\nFirst, enter the target value you want your coins to sum to as an integer in the unit of money such that the value of your least valuable coin in the same unit is also an integer.\nFor the above example, I would enter '200'. If I wanted to also consider a coin worth 0.2p, then I could enter 2000 for my target, in which case I would enter 2 for my 0.2p coin, 10 for a 1p coin and so on.")
    userInIsInt = userIn.isdigit()
    while userInIsInt == False:
        userIn = myInput("\nYour target must be a positive whole number. E.g. '200'.\n")
        userInIsInt = userIn.isdigit()
    target = int(userIn)
    print("\nEnter your coins' values in the same unit as that used for your target.\n")
    userIn = ""
    coins = []
    i = 1
    while userIn != "f":
        print("\nYour target value: " + str(target) + "\nYour coin values: " + str(coins) + "\n")
        userIn = myInput("Enter " + (str(i)+"st" if str(i)[-1] == "1" else str(i)+"nd" if str(i)[-1] == "2" else str(i)+"rd" if str(i)[-1] == "3" else str(i)+"th") + " coin. Enter 'f' after you've finished entering your coins. Enter 'r' to start from the beginning.")
        userInIsInt = userIn.isdigit()
        if userInIsInt:
            userInIsUnique = (int(userIn) not in coins)
            userInIsInt = int(userIn) != 0 and int(userIn) <= target
        while (not userInIsInt or not userInIsUnique) and not userIn == 'f':
            if not userInIsInt:
                userIn = myInput("\nYour coin must be a positive whole number, less than or equal to your target. E.g. '1'.")
            elif not userInIsUnique:
                userIn = myInput("\nYou already entered this value.")
            userInIsInt = userIn.isdigit() and userIn != 0
            if userInIsInt:
                userInIsUnique = (int(userIn) not in coins)
                userInIsInt = int(userIn) != 0 and int(userIn) <= target
        if userIn == 'f':
            break
        coins.append(int(userIn))
        coins.sort()
        i += 1
    # target = 200
    # coins = [1,2,5,10,20,50,100,200]
    
    #logic
    # The idea: 
    # 1. We sort coins from highest to lowest value.
    # 2. We consider a vector - coinsTry - of integer values representing the number of each denomination of coins to use.
    # 3. We increment the nth entry of coinsTry until we meet/exceed target. If meet, increment count.
    # 4. Then we treat the sub-array of coinsTry from the 0th to the (n-1)th entry as a single number, that we increment in a fasion similar to binary counting, i.e. ...0000, ...0001, ......0010, ...0011, ...0100, ...0101, and so on... but here, instead of using base 2 or base 10 to know when to start incrementing the next digit, we check if the sub-array of coinsTry seldom sums to over 200.
    # 5. Repeat 3. and 4. until we have gone through all combinations of digits for the 0th to (n-1)th entry of coinsTry.
    # 6. Increase n by 1 - meaning the next slot in the array coinsTry.
    # 7. Repeat 3., 4., 5. and 6. until there is no next slot to try in 6..
    coins.sort(reverse=True)
    end = False #control variable for main loop
    coinsTry = [0]*len(coins) #vector indicating how many of each coin we are trying
    trySlot = 0 #the slot we are currently incrementing
    count = 0 #counter for combinations of coins summing to 200
    sum = 0 #variable to calculate sum of current coinsTry
    slotIncrement = True #variable controlling whether we change the slot to increment

    while end == False:
        while True: #loop to increment tryslot and check if sum == target
            sum = 0
            for i in range(0,len(coins)):
                sum += coins[i]*coinsTry[i]
            if sum > target:
                coinsTry[trySlot] = 0
                break
            elif sum == target:
                coinsTry[trySlot] = 0
                count += 1
                break
            else:
                coinsTry[trySlot] += math.ceil((target - sum)/coins[trySlot])
        for i in range(1, trySlot + 1): #loop to increment the slots before tryslot in a fashion similar to binary counting i.e. 0000, 0001, 0010, 0011, 0100, 0101,... 
            slotIncrement = True
            sum = 0
            for j in range(0,len(coins)):
                sum += coins[j]*coinsTry[j]
            if sum < target:
                coinsTry[trySlot-i] += 1
                coinsTry[trySlot] = 1 #note: trySlot set to 1 to avoid recouting - if it was 0, we would count coinsTry = [1, 0, 0, 0, 0, 0, 0, 0] many times over.
                slotIncrement = False
                break
            else:
                coinsTry[trySlot-i] = 0
        if slotIncrement == True: #loop to change our trySlot and control when to end the program
            trySlot += 1
            if trySlot >= len(coins):
                end = True
            else:
                coinsTry[trySlot] = 1 #note: trySlot set to 1 to avoid recouting - if it was 0, we would count coinsTry = [1, 0, 0, 0, 0, 0, 0, 0] many times over.
    myInput("There are " + str(count) + " unique ways to make up the value " + str(target) + " using the set of coins with value " + str(coins) + ".\n\nTo restart enter r.")

main()