
from bs4 import BeautifulSoup
import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

temp = ""
while 1:
    f = open('search.txt', 'r')

    it = f.read()
    item = it.split(' ')
    
    if it != temp and it != "":
        amazon_raw_link = "http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="
        amazon_gen_link = ""
        
        snapdeal_raw_link = "https://www.snapdeal.com/search?clickSrc=top_searches&keyword="
        snapdeal_gen_link = "";
        		
        for i in item:
                if i != item[len(item) - 1]:
                        amazon_gen_link = amazon_gen_link + i + '+'
                        snapdeal_gen_link = snapdeal_gen_link + i + '%20'
                else:
                        amazon_gen_link = amazon_gen_link + i
                        snapdeal_gen_link = snapdeal_gen_link + i 
                  
        amazon_item_link = amazon_raw_link + amazon_gen_link
        snapdeal_item_link = snapdeal_raw_link + snapdeal_gen_link


        response = opener.open(amazon_item_link)
        page = response.read()

        soup = BeautifulSoup(page, 'html.parser',from_encoding="iso-8859-1")
        
        amazon_price = soup.find("span", {"class": "currencyINR"}).next.next
        
        fo = open('/home/nkh371/Downloads/ShopBat/Final Extension/popup.js', 'a+');

        emb = "\nprice_amz = \"" + "Rs. " + amazon_price + "\";" + " " + "\nlink_amz = \"" + amazon_item_link + "\";" + "\n" + "iname_amz = \"" + it + "\";" + "\n"

        fo.write(emb);
        fo.close();
        
        ajvhjhvb = "4"
		
        response = opener.open(snapdeal_item_link)
        page = response.read()
		
        soup = BeautifulSoup(page, 'html.parser',from_encoding="iso-8859-1")
        
        snapdeal_price = soup.find("span", {"class": "lfloat product-price"}).next
        
        fo = open('/home/nkh371/Downloads/ShopBat/Final Extension/popup.js', 'a+');


        emb = "\nprice_snp = \"" + snapdeal_price + "\";" + " " + "\nlink_snp = \"" + snapdeal_item_link + "\";" + "\n" + "iname_snp = \"" + it + "\";" + "\n"
		
        fo.write(emb);
        fo.close();
    
        temp = it
