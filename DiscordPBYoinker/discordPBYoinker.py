from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getUrl(discord_Id):
    url = 'https://discord.id/'
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument("disable-gpu")

    driver = webdriver.Chrome(executable_path=r'DiscordPBYoinker/chromedriver.exe', chrome_options=chrome_options)
    #driver.set_window_position(50, 50)
    #driver.set_window_size(800, 600)
    driver.implicitly_wait(10) # seconds
    driver.get(url)
    
    inputId = driver.find_element_by_id('inputid')
    inputId.clear()
    inputId.send_keys(discord_Id)
    
    button_lookup = driver.find_element_by_tag_name('button')
    button_lookup.click()
    
    button_antiboot = driver.find_element_by_class_name('frc-button')
    button_antiboot.click()
    
    resulths = driver.find_elements_by_class_name('resulth')
    resultTwoSpan = resulths[1].find_element_by_tag_name('span')
    username = resultTwoSpan.text
    
    discord_PB = driver.find_element_by_class_name('avyimg')
    src_PB = discord_PB.get_attribute('src')
    
    driver.close()
    
    return src_PB, username
