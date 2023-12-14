import os
import math
from time import perf_counter
from resources import *

def _myInput(displayText):
    # function to take user input with hardcoded 'r' to reset
    # and newline & tab on line end
    userIn = input(displayText + "\n\t>")
    if userIn == "r":
        return main()
    else:
        return userIn

def myStupidCoinCalc(target: int, *coinsTuple: int):
    """
    Given an integer target, and coins of integer value in the same
    unit of measurement as target, this function gives the number of
    distinct unordered combinations of coins to make up the target
    (with repetition).
    """
    # ---The logic---
    # In short:
        # we treat the entries of coinsTry as a single number and
        # increase that "number" in a fashion similar to how you'd
        # increase count through base N numbers;
        # e.g. base2: 0000, 0001, 0010, 0011, 0100, 0101, and so on...
    # In long: 
        # 1.We sort coins from highest to lowest value.
        # 2.We consider a vector - coinsTry - of integer values
        #   representing the number of each denomination of
        #   coins to use.
        # 3.We increment the nth entry of coinsTry until we meet/exceed
        #   target. If meet, increment count.
        # 4.Then we treat the sub-array of coinsTry from the 0th to the
        #   (n-1)th entry as a single number, that we increment in a
        #   fasion similar to binary counting,
        #   i.e. 0000, 0001, 0010, 0011, 0100, 0101, and so on... but
        #   here, instead of using base 2 or base 10 to know when to
        #   start incrementing the next digit, we check if the
        #   sub-array of coinsTry seldom sums to over 200.
        # 5.Repeat 3. and 4. until we have gone through all
        #   combinations of digits for the 0th to (n-1)th entry of
        #   coinsTry.
        # 6.Increase n by 1 - meaning the next slot in the array
        #   coinsTry.
        # 7.Repeat 3., 4., 5. and 6. until there is no next slot to
        #   try in 6..
    coins = list(coinsTuple)
    coins.sort(reverse=True)
    
    # control variable for main loop
    end = False
    
    # vector indicating how many of each coin we are trying
    coinsTry = [0]*len(coins)
    
    # the slot we are currently incrementing
    trySlot = 0
    
    # counter for combinations of coins summing to 200
    count = 0
    
    # variable to calculate sum of current coinsTry
    mySum = 0
    
    # variable controlling whether we change the slot to increment
    slotIncrement = True

    while end == False:
        while True:
            # loop to increment tryslot and check if sum == target
            mySum = sum(
                [coins[i]*coinsTry[i] for i in range(0,len(coins))]
                )
            if mySum > target:
                coinsTry[trySlot] = 0
                break
            elif mySum == target:
                coinsTry[trySlot] = 0
                count += 1
                break
            else:
                coinsTry[trySlot] += math.ceil(
                    (target-mySum)/coins[trySlot]
                    )
        for i in range(1, trySlot + 1): 
            # loop to increment the slots before tryslot in
            # a fashion similar to binary counting
            # i.e. 0000, 0001, 0010, 0011, 0100, 0101,... 
            slotIncrement = True
            mySum=sum(
                [coins[j]*coinsTry[j]for j in range(0, len(coins))]
                )
            if mySum < target:
                coinsTry[trySlot-i] += 1
                coinsTry[trySlot] = 1
                # note: trySlot set to 1 to avoid recounting
                # - if it was 0, we would count 
                # coinsTry = [1, 0, 0, 0, 0, 0, 0, 0]
                # many times over.
                slotIncrement = False
                break
            else:
                coinsTry[trySlot-i] = 0
        if slotIncrement == True:
            # loop to change our trySlot and 
            # control when to end the program
            trySlot += 1
            if trySlot >= len(coins):
                end = True
            else:
                # note: trySlot set to 1 to avoid recouting
                # - if it was 0, we would count coinsTry = 
                # [1, 0, 0, 0, 0, 0, 0, 0] many times over.
                coinsTry[trySlot] = 1
    return count

def aCleanCoinCalcSomeoneSmarterThanMeMade(target, *coinsTuple):
    coins = list(coinsTuple)
    ways = [0]*(target + 1)
    ways[0] = 1
    for x in coins:
        for i in range(x, target + 1):
            ways[i] += ways[i-x]
    return ways[target]

def main():
    # interact with user to get inputs and control program flow
    os.system('cls' if os.name == 'nt' else 'clear')
    userIn = _myInput(prompt_getTarget)
    userInIsInt = userIn.isdigit()
    while userInIsInt == False:
        userIn = _myInput(prompt_targetValueControl)
        userInIsInt = userIn.isdigit()
    target = int(userIn)
    print(prompt_enterCoins)
    userIn = ""
    coins = []
    i = 1
    while userIn != "f":
        print("\nYour target value: " + str(target) +
              "\nYour coin values: " + str(coins) + "\n")
        # display correct number suffix,
        # e.g. '1st', '2nd', '3rd', '4th', '11th',
        # '21st', '213th', '223rd', etc.
        iSuffix = "th"
        if len(str(i)) > 1:
            if str(i)[-2] != "1":
                # (separate ifs because
                # str(anyOneDigitNum)[-2] will give an error)
                pass
        else:
            if str(i)[-1] == "1":
                iSuffix = "st"
            elif str(i)[-1] == "2":
                iSuffix = "nd"
            elif str(i)[-1] == "3":
                iSuffix = "rd"
        print("Enter " + str(i)+iSuffix + " coin. ")
        userIn = _myInput(prompt_resetInstructions)
        userInIsInt = userIn.isdigit()
        if userInIsInt:
            userInIsUnique = (int(userIn) not in coins)
            userInIsInt = int(userIn) != 0 and int(userIn) <= target
        while (
            (not userInIsInt or not userInIsUnique)
            and not userIn == 'f'
            ):
            if not userInIsInt:
                userIn = _myInput(prompt_coinValueControl)
            elif not userInIsUnique:
                userIn = _myInput(prompt_coinNotUnique)
            userInIsInt = userIn.isdigit() and userIn != 0
            if userInIsInt:
                userInIsUnique = (int(userIn) not in coins)
                userInIsInt = int(userIn) > 0 and int(userIn) <= target
        if userIn == 'f':
            break
        coins.append(int(userIn))
        coins.sort()
        i += 1
    start = perf_counter()
    output = str(myStupidCoinCalc(target, *coins))
    end = perf_counter()
    print("My algorithm, which took " + str(end - start) + 
             " seconds:\n" + "There are " + output +
             " unique ways to make up the value " + str(target) +
             " using the set of coins with value " + str(coins) +
             ".\n\n")
    start = perf_counter()
    output = str(aCleanCoinCalcSomeoneSmarterThanMeMade(target, *coins))
    end = perf_counter()
    _myInput("A smarter, cleaner and faster algorithm that someone" + 
             " else made, which took " + str(end - start) + 
             " seconds:\n" + "There are " + output +
             " unique ways to make up the value " + str(target) +
             " using the set of coins with value " + str(coins) +
             ".\n\nTo restart enter r.")

if __name__ == '__main__':
    main()