# Xpath Syntax

Here are some examples about how one can use xpath to select elements in HTML in scrapy.


##### Extract texts

```python
response.xpath("//div[@class='yw']/ul//li//a/text()").extract()
response.xpath("//div[@class='txt']//p//span/text()").extract()
response.xpath("//ul//li/div[@class='list_name']/a/text()").extract()
```

##### Extract links

```python
page_urls = response.xpath("//div[@class='yw']/ul//li//a/@href").extract()
response.xpath("//ul[@class='yw-list']/li/a/@href").extract()
response.xpath("//a[@target='_blank']").extract()
response.xpath("span[@class='arrow']")
response.xpath("//div[@class='pagination_index']")
```

##### Next page

```python
response.xpath("//a[text()='下一页']/@href").extract()
response.xpath("//table[@id='pager']//span/a[text()='下一页']/@href")
response.xpath("//table[@id='pager']/span/a[text()='下一页']/@href").extract_first()
```

##### Search by text

```python
response.xpath("//div[@class='content_c']//p[contains(text(), '出生')]/text()").extract()
```

##### Select the element that contains other elements:
```python
images = response.xpath("//td/a[.//img]").extract()

images[0].xpath("following-sibling::p[1]//text()").extract()

images[0].xpath("./a/img/@src").extract()
```

##### Select the element that contains some data in some sub tags:

```python
response.xpath(u"//td//*[contains(text(), '生')]//text()").extract()
```
Here’s another example, to find the “`id`” attribute of a `<div>` tag containing five `<a>` children:
```python
>>> response.xpath('//div[count(a)=$cnt]/@id', cnt=5).extract_first()
u'images'
```

A node converted to a string, however, puts together the text of itself plus of all its descendants:
```python
>>> sel.xpath("string(//a[1])").extract() # convert it to string
[u'Click here to go to the Next Page']
```