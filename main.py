from flask import Flask
from flask import request
from flask import jsonify
import json
import requests


app = Flask(__name__)


URL = 'https://api.telegram.org/bot1520761661:AAH270x1WwkSz5rJjXbmy22wv71whJWvBTY/'


def write_json(data, filename = 'answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent = 2, ensure_ascii = False)


def mess(string):
    try:

        s = string
        lst_3 = s.split()
        lst = lst_3[1].split('/')
        list_0 = [lst_3[0], lst[0], lst[1]]
        list = [int(x) for x in list_0]
        return list
    except Exception as ex:
        return None


def send_message(chat_id, text):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json = answer)
    return r.json()


# def chek_id():
#     file = open('user_id.txt', 'r')
#     data = file.read().split(',')
#     print(data)
#     print(type(data))






@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        messange = mess(r['message']['text'])
        write_json(r)
        # chek_id()
        try:
            tud = 'TUD:'+str(messange[0])
            port = 'Port:'+str(messange[1])
            map = 'Card:'+str(messange[2])
            messange_to_send = [tud, port, map]
        except Exception as ex:
            messange_to_send = 'Пожалуйста, напишите по шаблону'

        send_message(chat_id, messange_to_send)
        # print(request)
        return jsonify(r)

    return '<h1>HeLLLLO</h1>'

def main():
    r = requests.get(URL + 'getMe')
    write_json(r)
    print(r)
    pass





if __name__ == '__main__':
    # main()
    app.run()
    # app.run(debug=True)
