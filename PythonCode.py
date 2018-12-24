'''
--> A project to Scrap The Product Names and their Links  from live websites
    using beautiful soup
'''

#importing the important libraries
from xlsxwriter import Workbook
import xlrd
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


# URL of the web page
url = "http://www.consumerreports.org/cro/a-to-z-index/products/index.htm"
file_name = 'product_reports.txt'


# Creating the object of the user agent
ua = UserAgent()


#creating the header of fake user agent
header = {'user-agent':ua.chrome}


# server return an object on sending the request for the web page
page = requests.get(url, headers = header)


# HTML code of the page writing to a file using page.content
with open(file_name,'w') as file:
    file.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)
    
    
# A function to extract the content of file
def read_file():
    file = open(file_name)
    data = file.read()
    file.close()
    return data
    

# Beautiful Soup return an object, it is the parser which parse the 
#HTML data
soup = BeautifulSoup(read_file(),'lxml')


'''
Since all product have the common class attribute crux-body-copy
so we have to find all of these divs 
'''

#Finding all div which has the class 'crux-body-copy'
all_divs = soup.find_all('div', class_ = 'crux-body-copy')


for div in all_divs:
    print(div.a.string)
    
    
# div has a child tag <a> and a has a navigating string 
products = [div.a.string for div in all_divs]


# Removing all new line and white space characters from the retrieved string
prod = []
for product in products:
    product = product.replace('\n','')
    product = product.replace(" ", "")
    prod.append(product)
    
print(prod)


'''
div has a child tag <a> which has href attribute 
so we have to find the href of tag <a>
'''

# finding href from tag <a>
links = [div.a['href'] for div in all_divs]
print(links)

print(len(links))


# creating a workbook with a worksheet
workbook = Workbook('Product_details.xlsx')
worksheet = workbook.add_worksheet()


# Initializing the first columns of all rows of worksheet
worksheet.write(0,0,'S.No',)
worksheet.write(0,1,'Product Name')
worksheet.write(0,2,'product Link')


# Filling the worksheet from product and their links
for row in range(len(links)):
    worksheet.write(row+1,0,row+1)
    worksheet.write(row+1,1,prod[row])
    worksheet.write(row+1,2,links[row])

workbook.close()


    
    
    
    


