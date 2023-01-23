from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'Warning': 'Put after the link /user= here, put your Instagram username'})

@app.route('/user=<string:parameter>')
def get_value(parameter):
    url = f"https://www.instagram.com/{parameter}/?__a=1&__d=dis"
    head = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'gzip,deflate,br',
        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
        'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
        'user-agent': 'Instagram 9.4.0 Android (30/11; 480dpi; 1080x2158; OPPO; CPH2069; OP4C7BL1; qcom; en_US; 276028020)'#generate_user_agent(),
        }
    information = requests.get(url,headers=head).json()

    id = (information['graphql']['user']['id'])
    name = (information['graphql']['user']['full_name'])
    Bio = (information['graphql']['user']['biography'])
    Followers = (information['graphql']['user']['edge_followed_by']['count'])
    Following = (information['graphql']['user']['edge_follow']['count'])
    url = (information['graphql']['user']['external_url'])
    private = (information['graphql']['user']['is_private'])
    business = (information['graphql']['user']['is_business_account'])
    posts = str(information['graphql']['user']["edge_owner_to_timeline_media"]["count"])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}",headers=head)
    ree = re.json()
    dat = ree['date']
    
    data = {'id': f'{id}', 'name': f'{name}', 'bio': f'{Bio}', 'followers': f'{Followers}', 'following': f'{Following}', 'link': f'{url}', 'private': f'{private}', 'business': f'{business}', 'posts': f'{posts}', 'date': f'{dat}'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=1337)
