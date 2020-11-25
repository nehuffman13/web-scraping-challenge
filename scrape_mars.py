from splinter import Browser
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd


def init_browser():
    executable_path = {"executable_path" : "/Users/MPatxot/.wdm/drivers/chromedriver/78.0.3904.97/mac64/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

mars_web = {}
hemisphere_image_urls = []

def scrape_news():
    
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)
    html = browser.html

    soup = bs(html, 'html.parser')
    latest_news_date = (soup.find_all('div', class_="list_date"))[0].get_text()
    latest_news_title = (soup.find_all('div', class_='content_title'))[0].get_text()
    latest_news_paragraph = (soup.find_all('div', class_='article_teaser_body'))[0].get_text()
    
    mars_web['latest_news_date'] = latest_news_date
    mars_web['latest_news_title'] = latest_news_title
    mars_web['latest_news_paragraph'] = latest_news_paragraph
   
    browser.quit()
    return mars_web
    
def scrape_marsImage():
    
    browser = init_browser()
    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    
    image = (soup.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href'))
    
    featured = 'https://www.jpl.nasa.gov'+ image
    
    mars_web['featured_image'] = featured
    
    browser.quit()
    return mars_web
    
def scrape_marsFacts():
    browser = init_browser()
    
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    tables_df = ((pd.read_html(url))[0]).rename(columns={0: "Attribute", 1: "Value"}).set_index(['Attribute'])
    html_table = (tables_df.to_html()).replace('\n', '')
    
    mars_web['mars_data'] = html_table
    browser.quit()
    return mars_web
        
def scrape_marsH1Cerberus():

    browser = init_browser()

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    cerberus_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    mars_web['hemisphere_urls'] = hemisphere_image_urls
    hemisphere_image_urls.append([{"title": "Cerberus Hemisphere", "img_url": cerberus_url}])
    
    browser.quit()
    return mars_web
    
def scrape_marsH2Schiaparelli():
 
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url}])

    browser.quit()
    return mars_web
    
def scrape_marsH3SyrtisMajor():        

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    syrtis_major_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_url}])

    browser.quit()
    return mars_web
        
def scrape_marsH4VallesMarineris():     

    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    valles_marineries_url= (soup.find_all('div', class_='downloads')[0].li.a.get('href'))
    hemisphere_image_urls.append([{"title": "Valles Marineris Hemisphere", "img_url": valles_marineries_url}])

    browser.quit()
    return mars_web