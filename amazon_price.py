import bs4
import requests


def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select(
        '#newOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    return elems[0].text.strip()


price = getAmazonPrice(
    'http://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print('The price is ' + price)
