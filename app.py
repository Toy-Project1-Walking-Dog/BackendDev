from flask import Flask,render_template, request, jsonify
import requests
from bs4 import BeautifulSoup

# URL and headers to crawl
# URL = "URL to crawl"
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# # Request
# data = requests.get(URL, headers=headers)

from pymongo import MongoClient
import certifi


app = Flask(__name__)

ca = certifi.where()


# <pssword> 지우고 '테스트' 하세요
client = MongoClient('mongodb+srv://sparta:<password>@cluster1.rnrelan.mongodb.net/?retryWrites=true&w=majority', tlsCAFILE=ca)
db = client.dbsparta
# db.userInfo.insert_one(doc)
# db.post.insert_one(doc)

@app.route('/')
def home():
   return render_template('main.html')

# 강다온
# 미세먼지 조회
@app.route('/', methods=["GET"])
def micro_dust():
   return jsonify({'msg':'whataever you want'})

# 정우용
# 회원가입
@app.route('/signup', methods=["POST"])
def signup():
   return jsonify({'msg':'whataever you want'})

# 정우용
# 로그인
@app.route('/login', methods=["POST"])
def login():
   return jsonify({'msg':'whataever you want'})

# 박나원
# 게시글 등록
@app.route('/post', methods=["POST"])
def post_create():
   return jsonify({'msg':'whataever you want'})

# 박나원
# 게시글 보기
@app.route('/post', methods=["GET"])
def post_list():
   return jsonify({'msg':'whataever you want'})

# 박나원
# 게시글 삭제
@app.route('/post/delete', methods=["POST"])
def post_delete():
   return jsonify({'msg':'whataever you want'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5001,debug=True)