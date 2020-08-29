from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\Sai Charan\\Downloads\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='email']").send_keys("yugeshthegreat@gmail.com")
driver.find_element_by_xpath("//*[@id='pass']").send_keys("9959873205")
driver.find_element_by_xpath("//*[@name='login']").click()
driver.close()