from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests, random
app = Flask(__name__)
@app.route('/')
def index():
    return "Error"
@app.route('/img=<string:imgs>')
def get_value(imgs):
 mod_1 = ['01','02','03','04','05','06','07','08','09','10','11','12']
 mod_2 = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
 running = True
 while running:
   mod_4 = str(''.join((random.choice(mod_1) for i in range(1))))
   mod_5 = str(''.join((random.choice(mod_2) for i in range(1))))
   dateimg = (mod_4+'-'+mod_5)
   url = f'https://telegra.ph/{imgs}-{dateimg}'
   response = requests.get(url)
   soup = BeautifulSoup(response.content, 'html.parser')
   img_tags = soup.find_all('img')
   urls = [img['src'] for img in img_tags]
   for link in urls:
    if ('/file/') in link:
     running = False
     img = ('https://telegra.ph/'+link)
     data = {'image': f'{img}'}
     return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=1337)
