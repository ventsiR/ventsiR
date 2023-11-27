import os
# import re
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import Firefox, FirefoxOptions, FirefoxProfile
# from selenium.webdriver.common.action_chains import ActionChains

#----------------------------------------------selections

comps = [
    'England1'
    # , 'Spain1', 'France1', 'Germany1', 'Italy1', 'Netherlands1', 'Portugal1''Argentina1', 'Australia1', 'Austria1', 'Belgium1', 'Brazil1', 'China1', 'Columbia1', 'Croatia1', 'Denmark1', 'England1', 'England2', 'England3', 'France1', 'France2', 'Germany1', 'Germany2', 'Greece1', 'Italy1', 'Italy2', 'Japan1', 'Mexico1', 'Netherlands1', 'Norway1', 'Portugal1', 'Russia1', 'Saudi1', 'Scotland1', 'SKorea1', 'Spain1', 'Spain2', 'Sweden1', 'Switzerland1', 'Turkey1', 'Ukraine1', 'USA1'
    ]
seasons = [
        # '2019-20', '2020-21', '2021-22', '2022-23'
        #    , 
        '2023-24', '2022-23'
        ]
fbrefstats = ["stats","keepers","keepersadv","shooting","passing","passing_types","gca","defense","possession","playingtime","misc"]
lastXSeasons = 2

with open('compsDict.csv', mode='r', encoding='utf-8-sig') as compDict:
    reader = csv.DictReader(compDict)
    compData = list(reader)

with open('seasonsDict.csv', mode='r', encoding='utf-8-sig') as seasonsDict:
    reader = csv.DictReader(seasonsDict)
    seasonData = list(reader)

def compLookup(myid, col):
    for row in compData:
        if row["id"] == myid:
            return row[col]
    return None

def seasonLookup(id, col):
    for row in seasonData:
        if row['id'] == id:
            return row[col]
    return None

#----------------------------------------------

# ----------------------------------------------upcoming games via flashscore

for comp in comps:
    scrape = []
    url = 'https://www.flashscore.com/football/' + compLookup(comp,'flashscoreURL') + '/fixtures/'

    driver = webdriver.Firefox()
    driver.get(url)
    driver.minimize_window()

    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//button[contains(text(),'Reject All')]"))).click()
    driver.switch_to.default_content()

    games = driver.find_elements(By.XPATH, "//div[contains(@class, 'event__match')]")

    for game in games:
        gamedetails = game.find_elements(By.XPATH, ".//div[contains(@class,'event__time')] | .//div[contains(@class, 'event__participant')]")
        for detail in gamedetails:
            scrape.append(detail.text)

    if not os.path.exists('data/upcomingGames'):
        os.makedirs('data/upcomingGames')
    with open('data/upcomingGames/' + comp + '.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        row = []
        for idx, entry in enumerate(scrape, 1):
            row.append(entry)
            if idx % 3 == 0:
                writer.writerow(row)
                row = []
    driver.quit()
    print("flashscore " + comp + " done. \n")

# # ----------------------------------------------

# # ----------------------------------------------transfermarkt referee stats

for comp in comps:
    for season in seasons:
        driver = webdriver.Firefox()
        driver.get('https://www.transfermarkt.com/' + compLookup(comp,'transfermarktURL1') + '/schiedsrichter/wettbewerb/' + compLookup(comp,'transfermarktURL2') + '/plus/1?saison_id=' + seasonLookup(season,'transfermarktURL'))
        driver.minimize_window()

        wait = WebDriverWait(driver, 30)
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="sp_message_iframe_851946"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="REJECT ALL"]'))).click()
        driver.switch_to.default_content()
        # driver.find_element(By.XPATH, "//span[text()='Detailed']").click()

        table = driver.find_element(By.XPATH, "//div[contains(@class, 'responsive-table')]")
        scrape = []

        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            td_elements = row.find_elements(By.TAG_NAME, "td")
            th_elements = row.find_elements(By.TAG_NAME, "th")
            columns = td_elements + th_elements
            columns_data = [col.text for col in columns]
            scrape.append(columns_data)

        with open("data/transfermarktRefs/" + comp + season + " refs.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(scrape)

        driver.quit()
    print("transfermarkt " + comp + " done. \n")

# ----------------------------------------------

#----------------------------------------------fbref general stats



for comp in comps:
    url = 'https://fbref.com/en/comps/' + compLookup(comp, 'fbrefURL') + '/history'

    driver = webdriver.Firefox()
    driver.get(url)
    driver.minimize_window()
    wait = WebDriverWait(driver, 30)
    # rejectCookies = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//span[contains(text(), 'DISAGREE')]")))
    # driver.switch_to.default_content()

    seasonsTable = driver.find_element(By.XPATH, "//table[@id='seasons']")
    rows = seasonsTable.find_elements(By.XPATH, ".//tbody/tr[not(@class='header')]/th[@data-stat = 'year_id']/a")
    seasons = []
    for row in rows:
        seasons.append(row.text)
    seasons.sort(reverse=True)
    seasons = seasons[:lastXSeasons]
    
    driver.quit()

    for season in seasons:
        for stat in fbrefstats:
            url = 'https://fbref.com/en/comps/' + compLookup(comp, 'fbrefURL') + '/' + season + '/' + stat + '/' + season

            driver = webdriver.Firefox()
            driver.get(url)
            driver.minimize_window()
            wait = WebDriverWait(driver, 30)
            # rejectCookies = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//span[contains(text(), 'DISAGREE')]")))
            # driver.switch_to.default_content()
            tables = driver.find_elements(By.XPATH, "//table[contains(@id, 'stats_')]")

            # print(tables)

            for table in tables:
                scrape = []
                aggregation = table.get_attribute("id")
                rows = table.find_elements(By.TAG_NAME, "tr")
                for row in rows:
                    th_elements = row.find_elements(By.TAG_NAME, "th")
                    td_elements = row.find_elements(By.TAG_NAME, "td")
                    columns = th_elements + td_elements
                    columns_data = [col.text for col in columns]
                    scrape.append(columns_data)

                mypath = 'data/fbref/' + comp + '/' + stat + '/' + aggregation
                if not os.path.exists(mypath):
                    os.makedirs(mypath)
                with open(mypath + '/' + season + '.csv', "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(scrape)

            driver.quit()
        print(comp + " " + season + " done. \n")
    print("fbref " + comp + " done. \n")
    
#----------------------------------------------