# user_routes.py

from flask import Blueprint
import requests

insert_key = '4c5a667a4c6d733237376973724350'
url = f'http://openapi.seoul.go.kr:8088/{insert_key}/xml/landActualPriceInfo/1/5/'
res = requests.get(url)
data = res.json()

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/')
def index():
    return data
