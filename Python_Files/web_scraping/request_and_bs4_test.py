from bs4 import BeautifulSoup
import requests
#retrieves data from the given url
response = requests.get('https://www.goat.com/login')

print(response.status_code)    #status of request.get on certain url
                                #the boolean value is true between 200 and 400 and false eitherwise
src = response.content  

soup = BeautifulSoup(src,"html.parser") #creates a beaufiful soup object
s = soup.prettify() #pretty html format
with open('goat.html', 'w') as f:
    f.write(str(s))

#links = soup.find_all('a')
#for link in links:
#    print(link.attrs)