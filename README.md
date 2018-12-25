# Scraping-Product-Details-from-live-website
Web scraping is a technique to exrtract large amount of data from websites whereby the data is extracted and saved to a local file of computer or to a database. In this repository we are scraping the product name and their link from a live website using web scraping using beautiful soup.


# Basic steps for web scraping:
1. Load the document from which you want to scrap the data.
2. Parse or to interpret the document to make the searching possible.
3. Simply extract the data from the web pages.
4. Transform the data into useful format.

# Process to access the html code of live site

user ---> Request ---> Server -----> Response ----->Html code

Beautiful soup is a  python library which is used to puling the data from the html pages $ xml files. It provides efficient searching and modification techniques.

HTML code is like a Tree of tags and Beautiful soup is used to parse the tree for extracting the data from these tags.

                                               <html>
                                               
                                 <head>                          <body>
                                 
                      <meta>                <title>      <p>                 <p>
                      
                      
                      
 # Required packages:
 
 1. requests                     (pip install requests)
 2. Beautiul Soup                (pip install beautifulsoup4)
 3. UserAgent                    (pip install fake-useragent)
 4. xlsxwriter                   (pip install xlsxwriter)
 5. xlrd                         (pip install xlrd)
 
 # References:
 
 Below is the link of website which is used to scrap the data:
 
  http://www.consumerreports.org/cro/a-to-z-index/products/index.htm
 
                      
