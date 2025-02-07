import requests
from bs4 import BeautifulSoup
from selenium import webdriver


#driver = webdriver.Firefox()
#link = "https://myanimelist.net/profile/Retro8bit/reviews"
#driver.get(link)#"http://www.python.org")
#exit()

#driver.page_source




      

def malUpdate(uName):
      x = requests.get('https://myanimelist.net/profile/'+uName+'/reviews')
      html = x.text
      soup = BeautifulSoup(html, 'html.parser')
      reviews = soup.find_all("div", {"class": "review-element"})

      out="""<html>
		<head>
			<title>MyAnimeList Mirror</title>
			<meta charset="utf-8"/>
			   <meta name="viewport" content="initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no, target-densitydpi=device-dpi" />
	    <meta name="apple-mobile-web-app-capable" content="yes" />
	    <meta name="apple-mobile-web-app-status-bar-style" content="black" />
	    <meta name="HandheldFriendly" content="true" />

	 <link rel="stylesheet" href="style.css" />
			<style>
	                      img{max-width:4em;transition-duration: 4s;}
	                      img:hover{max-width:20em;}
				
			</style>
		</head>
		<body>
	<center>
	<div class="top">
		<h1>MyAnimeList Archive</h1>
	</div>"""
      
      for r in reviews:
            out +='<div class="review">'
            date= r.find_all("div",{"class":"update_at"})[0]
            title= r.find_all("div",{"class":"titleblock"})[0].find_all('a')[0]
            text = r.find_all("div", {"class": "text"})[0]


            out +="<h3>"+title.text+"</h3>"
            out +="<p>"+text.text.replace('\n','<br>')+"</p>"
            out +="<sub>Date published: "+date.text + " " + date['title']+"</sub>"
            out +="</div>"

      out+="""<div class="bottom">
		<a href="index.html"><h1>Other Mirrors</h1></a>
	</div></center>
		</body>
	</html>"""
      out = out.encode("utf8")
      fyle = open("myAnimeList.html", "wb")
      fyle.write(out)
      fyle.close()
      print("myAnimeList update complete")

