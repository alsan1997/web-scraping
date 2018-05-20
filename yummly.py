import requests
import json

header = {
 "Content-Type": "application/json",
 "X-Yummly-App-ID": "5edc9616", #FillIn your own ID
 "X-Yummly-App-Key": "8c3a2a8a3d72cd5a68d97d92b84dc8cc", #FillIn your own Appkey
 "Access-Control-Allow-Origin": 'true'
}


#datas
recipeName = []
minutes = []
rating = []
ingredients = []
cuisines = ["cuisine^cuisine-spanish","cuisine^cuisine-american", "cuisine^cuisine-italian", "cuisine^cuisine-mexican","cuisine^cuisine-thai",
            "cuisine^cuisine-japanese", "cuisine^cuisine-indian", "cuisine^cuisine-greek", "cuisine^cuisine-hawaiin", "cuisine^cuisine-french",
            "cuisine^cuisine-german", "cuisine^cuisine-swedish", "cuisine^cuisine-barbecue", "cuisine^cuisine-irish", "cuisine^cuisine-mediterranean"]

for j in cuisines:
    idx = 0
    param = {"allowedCuisine[]": j}
    url='https://api.yummly.com/v1/api/recipes'
    response = requests.get(url, headers=header, params=param)
    yummly = response.json()
    matches = yummly['matches']        
    for i in yummly['matches']:
        data = matches[idx]
        recipeName.append(data['recipeName'])
        minutes.append(data['totalTimeInSeconds']/60)
        rating.append(data['rating'])
        ingredients.append(data['ingredients'])
        idx = idx + 1
    print(idx, "got 10")