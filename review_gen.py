from bs4 import BeautifulSoup
import json
import requests
import re
import string
import review_functions as rf
import os

os.chdir(r'C:\Users\Turcanhydgoongod\Documents\Jupyter\BeerReviewer')

with open('english_dict.json','r') as file:
    english_dict = json.loads(file.read())

url = input("Input a BeerAdvocate.com URL:\n")
print("Fetching reviews")
source = requests.get(url).text
soup = BeautifulSoup(source,'lxml')
name = soup.title.string.split('|')[0]
n_ratings = soup.find("span",{"class":"ba-ratings Tooltip"}).get_text()
n_reviews = soup.find("span",{"class":"ba-reviews Tooltip"}).get_text()
print("There are: " + n_ratings + " ratings for "+name+"."+"\n"+
     "There are: " + n_reviews + " reviews for "+name+".")
if n_reviews == '0':
    print("No reviews to alter!")
    exit()

mess = soup.find("div", {"id": "rating_fullview"}).get_text()
mess = mess.split("overall:")[1::2]
review_list = [review.partition("\xa0")[0] for review in mess]

letters = string.ascii_uppercase[0:27]+string.ascii_lowercase[0:27]
for index, review in enumerate(review_list):
    i = 0
    for letter in review:
        if (letter not in letters) and (review[i+1] in letters):
            review = review[i+1:]
            review_list[index] = review
            break
        else:
            i += 1

altered_review_list = []
for review in review_list:
    altered_review_list.append(
        rf.review_changer(''.join(review.split('\n\n'))))

with open(name+".txt",'w') as file:
    file.write("\n\n\n".join(altered_review_list))

print("\n----------------------------------\n".join(
    [review for review in altered_review_list]
))




