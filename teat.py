import requests
from bs4 import BeautifulSoup
import lxml

g = requests.get('https://www.flipkart.com/clothing-and-accessories/topwear/pr?sid=clo,ash&p[]=facets.ideal_for%255B%255D%3DMen&p[]=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_c8c79dda-c902-4e1b-8607-c627f81ee3fe_2_372UD5BXDFYS_MC.6XNZG1FYFBZT&otracker=hp_rich_navigation_1_2.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BTop%2BWear_6XNZG1FYFBZT&cid=6XNZG1FYFBZT').text

# soup = BeautifulSoup(g, 'lxml')
# abc = soup.article
# link = soup.find('iframe', class_="youtube-player")
print(g)
