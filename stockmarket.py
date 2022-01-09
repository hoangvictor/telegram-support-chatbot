import requests
import os
from selenium import webdriver
from time import sleep


def test_sendIMG(update, context):
    update.message.reply_text('HI')
    filename = "stock_market_chart.jpg"
    driver = webdriver.Firefox()
    driver.get('https://ceilingstock.vn/chart.html?symbol=HNG')
    sleep(1)

    driver.get_screenshot_as_file(filename)

    update.message.bot.send_photo(
        update.message.chat.id, open(filename, "rb"))

    os.remove(filename)
