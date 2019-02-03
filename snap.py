from selenium import webdriver
from datetime import datetime
import csv

urls = [{'centos70': 'http://mirrors.aliyun.com/centos/7.0.1406/'},
        {'centos71': 'http://mirrors.aliyun.com/centos/7.1.1503/'},
        {'centos72': 'http://mirrors.aliyun.com/centos/7.2.1511/'},
        {'centos7': 'http://pub.mirrors.aliyun.com/centos/7/'}
        ]

DRIVER = 'chromedriver'

FILENAME = 'urls.csv'


def get_snap(browser, urlname, url):
    now = datetime.now().strftime('%Y%m%d%H%M%S%f')
    browser.get(url)
    screenshot = browser.save_screenshot(urlname + '-' + now + '.png')


def get_urls():
    urls = []
    with open(FILENAME, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            urls.append({row['name']: row['url']})

    return urls


def main():
    browser = webdriver.Chrome(DRIVER)
    for url in get_urls():
        for key in url:
            get_snap(browser, key, url[key])
    browser.quit()


if __name__ == "__main__":
    # print(get_urls())
    main()
