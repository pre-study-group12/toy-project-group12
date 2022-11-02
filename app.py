from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.mapsk1p.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dailyfit


@app.route('/')
def home():
    return render_template('main_page.html')


@app.route('/list/')
def border_list():
    return render_template('border_list.html')


@app.route('/sign_in/')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign_up/')
def sign_up():
    return render_template('sign_up.html')


@app.route('/posting/')
def posting_page():
    return render_template('posting_page.html')


@app.route('/read/')
def read_post():
    return render_template('read_post.html')

# user_id 조회를 통해 중복확인
@app.route('/sign_up/id_check', methods=['POST'])
def check_id():
    status = 0
    id_receive = request.form['id_give']
    users = list(db.users.find({}, {'_id': False}))
    for user in users:
        user_id = user['user_id']
        if user_id == id_receive:
            status = 0
            break
        else:
            status = 1
    return jsonify({'result': 'success', 'status': status})


# 회원가입 정보 DB 저장
@app.route('/sign_up/create', methods=['POST'])
def create_user():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    doc = {
        'user_id': id_receive,
        'user_pw': pw_receive
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '회원가입이 완료되었습니다.'})


# @app.route("/list", methods=["GET"])
# def border_list_get():
#     return jsonify({'msg': 'GET 연결 완료!'})
#
#
# @app.route("/mars", methods=["POST"])
# def web_mars_post():
#     sample_receive = request.form['sample_give']
#     print(sample_receive)
#     return jsonify({'msg': 'POST 연결 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
