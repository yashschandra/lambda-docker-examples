import boto3
import io
from selenium import webdriver


def handler(event, context):
    print('got event ', event)
    s3 = boto3.client('s3')
    options = webdriver.ChromeOptions()
    options.binary_location = '/opt/chrome/chrome'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280x1696")
    options.add_argument("--single-process")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    print('driver opening')
    try:
        driver = webdriver.Chrome("/opt/chromedriver",
                                options=options)
        print('driver opened')
    except e:
        print('driver not open ', e)
    try:
        driver.get("data:text/html;charset=utf-8," + event['html_str'])
        print('driver got, upload...')
    except e:
        print('driver did not get ', e)
    try:
        with io.BytesIO(driver.get_screenshot_as_png()) as f:
            s3.upload_fileobj(f, 'bounty-public', 'posters/test/screenshot.png')
            print('uploaded')
    except e:
        print('not able to upload ', e)
    driver.close()
