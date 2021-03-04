from flask import Flask, render_template
from flask import jsonify
app = Flask(__name__)
import pandas as pd



@app.route("/scrape")
def scrape():
    print('LOADING...')
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    driver.get(url)
    title_elements = driver.find_elements_by_css_selector('h3')
    title_list = [title.text for title in title_elements]
    img_list = []
    for i, title in enumerate(title_list):
        driver.get(url)
        driver.find_elements_by_css_selector('h3')[i].click()
        img_list.append(
            driver.find_element_by_class_name('downloads').find_element_by_css_selector('a').get_attribute('href'))

    driver.quit()
    hemisphere_image_urls = []
    title_picture_list = list(zip(title_list, img_list))
    for title, img in title_picture_list:
        hemisphere_image_urls.append({'title': title, 'img': img})
    print('COMPLETED')

    return jsonify(hemisphere_image_urls)

@app.route("/")
def index():
    print('LOADING...')
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    driver.get(url)
    title_elements = driver.find_elements_by_css_selector('h3')
    title_list = [title.text for title in title_elements]
    img_list = []
    for i, title in enumerate(title_list):
        driver.get(url)
        driver.find_elements_by_css_selector('h3')[i].click()
        img_list.append(
            driver.find_element_by_class_name('downloads').find_element_by_css_selector('a').get_attribute('href'))

    driver.quit()
    hemisphere_image_urls = []
    title_picture_list = list(zip(title_list, img_list))
    for title, img in title_picture_list:
        hemisphere_image_urls.append({'title': title, 'img': img})
    print('COMPLETED')
    return pd.DataFrame(hemisphere_image_urls).to_html()


if __name__ == '__main__':
    app.debug = False
    app.run()

### **** I spent about 3 hours trying to install homebrew and mongodb for my new M1 mac chip. I was able to sucessfully install brew on my machine using a custom script someone wrote, but after a lot of trial and error of installing mongo, I figured out that it is not supported by the M1 chip. Source: https://developer.mongodb.com/community/forums/t/support-for-apple-m1-silicon/12442 ***###