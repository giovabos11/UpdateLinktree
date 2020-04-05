from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import data

#driver = webdriver.Chrome(executable_path=data.driver_path)
driver = webdriver.Firefox(executable_path=data.driver_path)

url = 'https://linktr.ee/'

def update(link):
    print('\n [*] Setting new link ...')

    link_container_click = '//*[@id="link-list-group"]/div[1]/div[2]/div[2]/div[2]'
    link_container = '//*[@id="link-list-group"]/div[1]/div[2]/div[2]/div[2]/input'

    driver.find_element_by_xpath(link_container_click).click()
    driver.find_element_by_xpath(link_container).send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath(link_container).send_keys(Keys.DELETE)
    driver.find_element_by_xpath(link_container).send_keys(link)
    driver.find_element_by_xpath(link_container).send_keys(Keys.ENTER)

    print(' [!] Link setted successfully')

def help_menu():
    print('')
    print(' ============== UpdateLinktree ============== ')
    print('')
    print(' Script created by: papu_11                   ')
    print('')
    print('\thelp        -> Display this menu            ')
    print('\tdefault     -> Set default link             ')
    print('\tset [link]  -> Updates the link to the input')
    print('\tlogin       -> Retry the login              ')
    print('\texit        -> Quit the script              ')
    print('')
    print(' ============================================ ')

def login():
    print('\n [*] Loggin in ...')

    login = 'https://linktr.ee/login'

    driver.get(login)
        
    username_field = '//*[@id="username"]'
    driver.find_element_by_xpath(username_field).send_keys(data.username)

    password_field = '//*[@id="password"]'
    driver.find_element_by_xpath(password_field).send_keys(data.password)

    submit = '//*[@id="_submit"]'
    driver.find_element_by_xpath(submit).click()

    verify = '/html/body/div[1]/div[2]/section[3]/section/section/div/div[1]/div[1]/button'

    sleep(5)

    if driver.find_element_by_xpath(verify).text.strip() == 'Add New Link':
        print(' [!] Login successful!')
    else:
        print(' [X] Login error. Please try again')
    
def default():
    print('\n [*] Setting default link (' + data.default_link + ')')

    link_container_click = '//*[@id="link-list-group"]/div[1]/div[2]/div[2]/div[2]'
    link_container = '//*[@id="link-list-group"]/div[1]/div[2]/div[2]/div[2]/input'

    driver.find_element_by_xpath(link_container_click).click()
    driver.find_element_by_xpath(link_container).send_keys(Keys.CONTROL + "a")
    driver.find_element_by_xpath(link_container).send_keys(Keys.DELETE)
    driver.find_element_by_xpath(link_container).send_keys(data.default_link)
    driver.find_element_by_xpath(link_container).send_keys(Keys.ENTER)

    print(' [!] Default link setted successfully')

def error():
    print('\n [X] Unknown command')

def exit():
    print('\n [!] Exiting!\n')
    driver.close()
    quit()

help_menu()
print('\n [*] Starting ...')
login()
while True:
    option = input('\n Enter an option or type \'help\'> ')
    if option.strip().lower() == 'help':
        help_menu()
    elif option.strip().lower() == 'default':
        default()
    elif option.strip().lower() == 'login':
        login()
    elif option.strip().lower() == 'exit':
        exit()
    elif option.strip()[:4] == 'set ':
        update(option.strip().replace(" ", "")[3:])
    else:
       error()