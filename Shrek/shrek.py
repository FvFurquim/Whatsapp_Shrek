from selenium import webdriver

f = open("shrek.txt", "r")

lines = f.readlines()

driver = webdriver.Chrome('D:/Program Files/webdrivers/chromedriver')
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of the victim: ')

input('Press anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//div[@class = "_2S1VP copyable-text selectable-text"]')

for i in lines:
	msg_box.send_keys(i)
