# Collection of Web Scraping Programs Written in 2017
 

## Introduction

For reference purposes, this repository holds a collection of some web scraping programs I wrote in 2017, when I just started learning programming. In [web sraping](https://en.wikipedia.org/wiki/Web_scraping) you basically take up the role of a browser: you write programs to make HTTP requests to the websites, obtain HTML files, parse the files and extract the data you want. Popular Python libraries include [`requests`](https://requests.readthedocs.io/en/master/) for sending HTTP requests, [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for parsing HTML files, [selenium](https://www.selenium.dev/) for simulating a web browser, as well as the [scrapy](https://scrapy.org/) framework. The [requests-html](https://requests.readthedocs.io/projects/requests-html/en/latest/) library is more convenient for personal use.

## Directories

Here are the programs/scripts.

* [gter-admission-economics.py](gter-admission-economics.py) 

Scrape graduate school admission data from the [gter forum](http://bbs.gter.net/) for better decision making during graduate school application.

* [douyu.py](douyu.py)

Scrape the [DouYu](https://en.wikipedia.org/wiki/DouYu) live streaming website. Program requested by a friend.

* [quantnet.py](quantnet.py)

Gather graduate school admission data posted on [quantnet](https://quantnet.com/tracker/) for better decision making.

* [douban movie top250](douban)

Scrape movie list on [https://movie.douban.com/top250](https://movie.douban.com/top250). A beginner's project for familiarizing with the scrapy framework.

* [bocconi](bocconi)

Gather Bocconi faculty information from Bocconi's website.

* [xpath syntax](xpath-syntax.md)

A collection of examples that illustrates basic [Xpath](https://en.wikipedia.org/wiki/XPath) syntax. XPath (XML Path Language) is a query language for selecting nodes from an XML document.
