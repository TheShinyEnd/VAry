from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium.common.exceptions
import math
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import os
# to build:
#  pyinstaller --onefile --add-data "chromedriver.exe;." .\maniuplate_chromeATyoutube.py


def playYTvidinbackground(video_url, starttime=None, endingtime=None):
    def get_youtube_video_duration(video_url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Send a request to the video page
        response = requests.get(video_url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to load page: {response.status_code}")

        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the script tag that contains the duration
        scripts = soup.find_all('script')

        # Search for the duration in the script tags
        for script in scripts:
            if 'ytInitialPlayerResponse' in script.string if script.string else '':
                script_content = script.string
                break
        else:
            raise Exception("Couldn't find ytInitialPlayerResponse in the page")

        # Extract the duration using a regular expression
        duration_match = re.search(r'"approxDurationMs":"(\d+)"', script_content)
        if not duration_match:
            raise Exception("Couldn't find video duration in the page")

        # Convert duration from milliseconds to seconds
        duration_ms = int(duration_match.group(1))
        duration_seconds = duration_ms / 1000

        return duration_seconds

    # Get the YouTube video URL from the user

    vid_length = math.floor(get_youtube_video_duration(video_url))

    print(f'Specified video length is: {vid_length}')

    if endingtime is not None:
        if endingtime > vid_length:
            print("ending time is more than the vid time, idk. error. don't act.. idfk")
            return False, "endingtime>vidlength"
    
    if starttime is not None:
        if starttime > vid_length:
            print("starting time is more than the vid time, idk. error. don't act.. idfk")
            return False, "starttime>vidlength"


    def tryandretryuntilwork(*args):
        def run():
            return driver.execute_script(*args)
        while True:
            try:
                return run()
            except Exception as e:
                print(e)
                time.sleep(0.5)
                continue

    def skipadbutton():
        skip_button_exists = len(driver.find_elements(By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]')) > 0

        print(f'Does the skip button exist? {skip_button_exists}')
        if skip_button_exists:
            skip_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]'))
            )
            skip_button.click()

    def getcurrentYTtime():
        return tryandretryuntilwork("return arguments[0].currentTime", video)
        # document.getElementsByTagName('video')[0].currentTime

    def play():
        tryandretryuntilwork("arguments[0].play()", video)
        print("playing...")
        # document.getElementsByTagName('video')[0].play()
    def pause():
        tryandretryuntilwork("arguments[0].pause()", video)
        print("pausing...")
        # document.getElementsByTagName('video')[0].pause()
    def detectifpause():
        return tryandretryuntilwork("return arguments[0].paused", video)
        # document.getElementsByTagName('video')[0].paused
    def detectifmuted():
        return tryandretryuntilwork("return arguments[0].muted", video)
        # document.getElementsByTagName('video')[0].muted
    def mute():
        tryandretryuntilwork("arguments[0].muted = true", video)
        print("muting...")
        # document.getElementsByTagName('video')[0].muted = true
    def unmute():
        tryandretryuntilwork("arguments[0].muted = false", video)
        print("unmuting...")
        # document.getElementsByTagName('video')[0].muted = false
        
    def setytvolume(volume): # is a one to 0
        # so if more than 100, assume wrong
        
        # this volume seems to not work, like overall, does not seem to take effect
        
        
        if volume > 1:
            volume = volume / 100
        tryandretryuntilwork("arguments[0].volume = arguments[1]", video, volume)
        print("Changing volume...")
        # document.getElementsByTagName('video')[0].volume = volume

    # Create a new instance of the Chrome driver
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # driver = webdriver.Chrome(options=options)
    webdriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')
    print(f'Webdriver location: {webdriver_path}')
    # Create a new instance of the Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    # Navigate to the YouTube video
    driver.get(video_url)

    # Wait until the video element is present on the page
    wait = WebDriverWait(driver, 15)
    video = wait.until(EC.presence_of_element_located((By.TAG_NAME, "video")))
    if not detectifmuted():
        mute()


    def setYTtime(time):
        tryandretryuntilwork("arguments[0].currentTime = arguments[1]", video, time)
        print("Changing playback time...")
        # document.getElementsByTagName('video')[0].currentTime = time

    # Simulate multiple types of user interactions
    def simulate_user_interaction():
        actions = ActionChains(driver)
        
        # Click on the body
        actions.move_to_element(driver.find_element(By.TAG_NAME, 'body')).click().perform()
        time.sleep(1)
        
        # Click on the video element
        actions.move_to_element(video).click().perform()
        time.sleep(1)
        
        # Send a key press event
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(1)

    if not detectifmuted():
        mute()
    # Perform user interaction to enable autoplay
    simulate_user_interaction()
    if not detectifmuted():
        mute()
    wait3sec = time.time() + 3

    while True:
        try:
            video = driver.find_element(By.TAG_NAME, "video")
            skipadbutton()
            if not detectifmuted(): # aka if not muted
                mute()
                
            end_time = math.floor(tryandretryuntilwork("return arguments[0].duration", video))
            print("End time:", end_time)
            
            if detectifpause():
                play()
            
            if end_time != vid_length:
                wait3sec = time.time() + 3
                tryandretryuntilwork("arguments[0].currentTime = arguments[0].duration - 0.2", video)
                print("ad detected, skipping...")
            elif time.time() > wait3sec:
                print("no ad detected, continuing...")
                tryandretryuntilwork("arguments[0].currentTime = 0", video)
                break
        except selenium.common.exceptions.StaleElementReferenceException:
            print("Stale element reference exception occurred. Trying to find the video element again.")
            continue
        
        time.sleep(1)

    while detectifpause():
        play()
        time.sleep(0.8)

    setytvolume(1) 
    print('skipped all ads, or there were just no ads.. ')
    if detectifmuted(): # aka, it detects if it is muted, if it is, it's a True. otherwise false, so you unmute
        unmute()

    if starttime is not None:
        setYTtime(starttime)
    else:
        setYTtime(0)
    
    if endingtime is not None:
        while getcurrentYTtime() < endingtime:
            time.sleep(0.1)
            print(getcurrentYTtime())
    
    if endingtime is None:
        # wait until vid reaches the end
        while getcurrentYTtime() < end_time - 2.5: # -0.5 to account for the slight delay in the video ending
            time.sleep(1)
        
    
    driver.quit() # since it cleans up, it'll take a little bit until it returns back to the callable
    
    

viduri = input("Enter the YouTube video URL:\n")
import threading

threading.Thread(target=playYTvidinbackground, args=(viduri,)).start()
# playYTvidinbackground(viduri)

while True: pass # just so i can view the error msg


exit()

    
# reset back to where it was previously at the selected / given time

exit()

# Close the browser
driver.quit()


exit() # the bellow is so cool, it instantly interacts with the correct elements, and actually in the search lists finds the correct video CLICKS on it.. amazing!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Initialize the WebDriver
driver = webdriver.Chrome()
# Open YouTube
driver.get('https://www.youtube.com/')

# Wait until the search bar is available and search for a video
search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'search_query'))
)
search_bar.send_keys('Markiplier INFINITE SNAILS!! Content Warning - Part 3')
search_bar.send_keys(Keys.RETURN)

# Wait for the video to appear and click on it
video = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@id="video-title"]'))
)
video.click()


# Wait for the "Skip" button to appear and click it
try:
    skip_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "ytp-ad-skip-button")]'))
    )
    skip_button.click()
except:
    print("Skip button not found or no ad present")

# Close the browser
time.sleep(5)
driver.quit()