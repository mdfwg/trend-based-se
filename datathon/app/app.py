import streamlit as st
import requests
import os
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import streamlit as st
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
class ScoredPoint:
    def __init__(self, id, version, score, payload, vector, shard_key, order_value):
        self.id = id
        self.version = version
        self.score = score
        self.payload = payload
        self.vector = vector
        self.shard_key = shard_key
        self.order_value = order_value


def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    SERVICE_ACCOUNT_FILE = 'service_account.json'  # Update with your service account file path

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    return service
def fetch_file_ids(service, folder_id, names):
    file_ids = {}
    for name in names:
        results = service.files().list(
            q=f"'{folder_id}' in parents and name='{name}'",
            pageSize=1,
            fields="files(id, name)").execute()
        items = results.get('files', [])
        if items:
            file_ids[name] = items[0]['id']
    return file_ids
def show_image(image_id):
    image_url = f'https://drive.google.com/uc?id={image_id}'
    img = requests.get(image_url)
    return img.content

def response_to_imageNames(response):
    image_names = []
    for item in response:
        image_names.append(str(item.id)+'.webp')
    return image_names
def main():
    st.title('Stack Overflow')
    x=st.text_input('search:')
    response=[ScoredPoint(id=13881018908259734424, version=0, score=0.0, payload={'title': 'Genuine Sheepskin Earmuffs With Gift Box - Chocolate'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=6741082963333937131, version=0, score=0.0, payload={'title': "Prettylittlething Women's Cream Soft Faux Fur Ear Muffs"}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=15970458072186916174, version=0, score=0.0, payload={'title': "Shein 1pc Women's Foldable Plush Ear Muffs Ear Warmers for Winter Outdoor ..."}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=12796632817562111605, version=0, score=0.0, payload={'title': 'Gelante Plain Blank Baseball Caps Adjustable Back Strap Wholesale Lot 6 Pack'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=4899234377105272946, version=0, score=0.0, payload={'title': "New Era Men's Basic 59FIFTY Fitted Hat"}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=11925973543532142928, version=0, score=0.0, payload={'title': 'FRR Rabbit Fur Earmuffs with Velvet Band'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=7206407142812522904, version=0, score=0.0, payload={'title': "Buy Alpine Beanie Online - Men's Alpine Beanie | Slyk Shades"}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=817338107446175204, version=0, score=0.0, payload={'title': '32 Degrees Unisex Waffle Sherpa-Lined Beanie Cement / One Size'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=9793819018988895423, version=0, score=0.0, payload={'title': 'Tsalei Y2K Beanie Spider Beanie Double-Layer Knitted Hat Streetwear Headwear ...'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=3459600580643463954, version=0, score=0.0, payload={'title': 'Stylish Fedora Hats - Trendy Headwear for Every Occasion'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=17638024535505005986, version=0, score=0.0, payload={'title': 'Varsity Headwear - Soft Front Cashmere Cap Large / Flint Grey'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=1125364535336170582, version=0, score=0.0, payload={'title': "Aviator Hat, Women's, Size: One size, Plaid"}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=1452451141248393208, version=0, score=0.0, payload={'title': 'Holzlrgus Soft Beanies for Women with Brim Berets for Women Bonnet Bucket Hat ...'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=13751410419774281823, version=0, score=0.0, payload={'title': 'Falari 2 Pcs Set Men Women Knitted Beanie Hat Ski Skully Cap Plain Solid Color ...'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=3527736290902828119, version=0, score=0.0, payload={'title': 'Hig Ear Warmer Unisex Classic Fleece Earmuffs Winter Accessory Outdoor'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=11069447016055400402, version=0, score=0.0, payload={'title': "Sam's Rock Headwear Womens Fuzzy Fedora w/ Band - Black - Small/Medium, Women's ..."}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=3650951150364856806, version=0, score=0.0, payload={'title': 'Vintage Plaid Wool French Beret Cap for Women - Elegant Autumn/Winter Hat with ...'}, vector=None, shard_key=None, order_value=None),
    ScoredPoint(id=5780736666559986230, version=0, score=0.0, payload={'title': '180s - Lush Ear Warmer - Dusty Rose'}, vector=None, shard_key=None, order_value=None)]
    image=response_to_imageNames(response)
    folderid='1-5XfGoRKzGBMSD__O1kn8STJ2B2IaIlq'
    service=authenticate()

    file_ids = fetch_file_ids(service, folderid, image)

    st.write(f"Found {file_ids} results")
  
    left_column, mid, right_column = st.columns(3)

    for index, item in enumerate(response):
        if index % 3 == 0:
            left_container = left_column.container(border=True)
            left_container.markdown(f"<div style='text-align: left; font-size: small;'>{index}</div>", unsafe_allow_html=True)
            left_container.write(item.payload['title'])
            left_container.image(show_image(file_ids[image[index]]))
        elif index % 3 == 1:
            mid_container = mid.container(border=True)
            mid_container.markdown(f"<div style='text-align: left; font-size: small;'>{index}</div>", unsafe_allow_html=True)
            mid_container.write(item.payload['title'])
            mid_container.image(show_image(file_ids[image[index]]))
        else:
            right_container = right_column.container(border=True)
            right_container.markdown(f"<div style='text-align: left; font-size: small;'>{index}</div>", unsafe_allow_html=True)
            right_container.write(item.payload['title'])
            right_container.image(show_image(file_ids[image[index]]))
if __name__=='__main__':
    main()