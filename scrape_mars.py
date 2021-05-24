{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import datetime as dt\n",
    "import pymongo\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init_browser():\n",
    "    executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "    return Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    url = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url)\n",
    "    html = browser.html\n",
    "    soup = bs(html, 'lxml')\n",
    "    title = soup.find('div', class_=\"content_title\")\n",
    "    title_text = title.a.text\n",
    "    title_text = title_text.strip()\n",
    "    news_p = soup.find(\"div\", class_=\"rollover_description_inner\")\n",
    "    news_text = news_p.text\n",
    "    news_text = news_text.strip()\n",
    "     #Featured Photo\n",
    "    url2 = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "    browser.visit(url2)\n",
    "    html2 = browser.html\n",
    "    soup2 = bs(html2, 'html.parser')\n",
    "\n",
    "    results = soup2.find(\"ul\", class_=\"articles\")\n",
    "    href = results.find(\"a\",class_='fancybox')['data-fancybox-href']\n",
    "    featured_image_url = 'https://www.jpl.nasa.gov' + href\n",
    "\n",
    "    #Mars Weather\n",
    "    url3 = 'https://twitter.com/marswxreport?lang=en'\n",
    "    browser.visit(url3)\n",
    "    html3 = browser.html\n",
    "    soup3 = bs(html3, 'html.parser')\n",
    "\n",
    "    results2 = soup3.find('div', class_=\"js-tweet-text-container\")\n",
    "    tweet = results2.find(\"p\", class_=\"TweetTextSize TweetTextSize--normal js-tweet-text tweet-text\").text\n",
    "    tweet_split = tweet.rsplit(\"pic\")\n",
    "    mars_weather = tweet_split[0]\n",
    "\n",
    "    #Mars Facts\n",
    "    url4 = 'https://space-facts.com/mars/'\n",
    "    facts_table = pd.read_html(url4)\n",
    "    facts_df = facts_table[0]\n",
    "    facts_df.columns = [\"Description\", \"Value\"]\n",
    "    facts_df = facts_df.set_index(\"Description\")\n",
    "    facts_html = facts_df.to_html()\n",
    "\n",
    "    \n",
    "    url5 = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "    browser.visit(url5)\n",
    "    html4 = browser.html\n",
    "    soup4 = bs(html4, 'html.parser')\n",
    "\n",
    "    titles = soup4.find_all(\"h3\")\n",
    "    for title in titles:\n",
    "        browser.click_link_by_partial_text(\"Hemisphere\")\n",
    "\n",
    "    results4 = soup4.find_all(\"div\", class_=\"description\")\n",
    "    mars_dict={}\n",
    "    hemisphere_image_urls=[]\n",
    "    for result in results4:\n",
    "        link = result.find('a')\n",
    "        img_href = link['href']\n",
    "        title_img = link.find('h3').text\n",
    "        url6 = \"https://astrogeology.usgs.gov\" + img_href\n",
    "        browser.visit(url6)\n",
    "        html5 = browser.html\n",
    "        soup5 = bs(html5, 'html.parser')\n",
    "        pic = soup5.find(\"a\", target=\"_blank\")\n",
    "        pic_href = pic['href']\n",
    "        hemisphere_image_urls.append({\"title\":title_img,\"img_url\":pic_href})\n",
    "\n",
    "    \n",
    "    mars_info_dict = {\"news_title\":title_text,\"news_text\":news_text,\"featured_image\":featured_image_url,\n",
    "    \"mars_weather\":mars_weather,\"facts_table\":facts_html,\"hemisphere_img\":hemisphere_image_urls}\n",
    "\n",
    "    browser.quit()\n",
    "\n",
    "    return mars_info_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
