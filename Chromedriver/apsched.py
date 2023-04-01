from aiogram import Bot
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.headless = True

async def send_message_interval(bot: Bot):
    url = "https://uz-appointment.visametric.com/uz/appointment-form"
    driver = webdriver.Chrome(executable_path='E:\Programming\EPAM\ProjectVisa\Chromedriver\chromedriver.exe', options=options)
    driver.maximize_window()
    users = [1807668339, 1941579270]
    try:
        driver.get(url=url)
        driver.find_element("xpath", "//select[@name='country']/option[text()='Schengen Visa']").click()
        driver.find_element("xpath", "//select[@name='visitingcountry']/option[text()='Germany']").click()
        driver.find_element("xpath", "//select[@name='city']/option[text()='Tashkent']").click()
        driver.find_element("xpath", "//select[@name='office']/option[text()='Tashkent']").click()
        driver.find_element("xpath", "//select[@name='officetype']/option[text()='NORMAL']").click()
        sel = Select(driver.find_element("xpath", "//select[@name='totalPerson']"))
        sel.select_by_visible_text("2 arizachi")
        info = driver.find_element(By.ID, "availableDayInfo")
        if info.text == "Sana mavjud emas":
            for user in users:
                await bot.send_message(chat_id=user, text="sana topilmadi")
        else:
            for user in users:
                await bot.send_message(chat_id=user, text="Ariza topshirish uchun sana mavjud")
        time.sleep(10)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
