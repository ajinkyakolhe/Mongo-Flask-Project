from flask import Flask,request, render_template
from flask_pymongo import PyMongo
import re

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mashup_db'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mashup_db'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_stars():
    infoc = mongo.db.info
    output = []
    for s in infoc.find():
        output.append({'title': s['title']})
    return render_template('m_4.html')

@app.route("/echo")
def echo():
    pump = request.args.get('title')
    pump2 = request.args.get('year')
    pump3 = request.args.get('apidata')
    pump4 = request.args.get('rating')
    pump5 = request.args.get('ratingv')
    infoc = mongo.db.info
    out = []
    #print(pump, pump2, pump3, pump4, pump5)

    for s in infoc.find():
        atr1,atr2 = s['title'],s['updated']
        atr3 = s['Tags']
        str1 = ''.join(atr3)
        atr4 = s['rating']
        #print(atr3)
        if bool(re.search(r'(.*)' + re.escape(pump) + '(.*)', atr1)) \
                and bool(re.search(r'(.*)' + re.escape(pump2) + '(.*)', atr2)) \
                and bool(re.search(r'(.*)' + re.escape(pump3) + '(.*)', str1)) :
            if pump4 == "greater than":
                if s['rating'] > pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'APIs': s['APIs'],
                                'id': s['id'],'rating': s['rating'],'updated': s['updated']})
            elif pump4 == "gte":
                if s['rating'] >= pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'APIs': s['APIs'],
                                'id': s['id'], 'rating': s['rating'],'updated': s['updated']})
            elif pump4 == "less than":
                if (s(['rating'] < pump5) or (s['rating'] == '')):
                    out.append({'title': s['title'], 'description': s['description'], 'APIs': s['APIs'],
                                'id': s['id'], 'rating': s['rating'],'updated': s['updated']})
            elif pump4 == "le":
                if s['rating'] <= pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'APIs': s['APIs'],
                                'id': s['id'], 'rating': s['rating'],'updated': s['updated']})
            elif pump4 == "equal":
                if s['rating'] == pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'APIs': s['APIs'],
                                'id': s['id'], 'rating': s['rating'],'updated': s['updated']})
            else:
                print("No output")
    print(out)
    return render_template('m_4.html', show=out)

if __name__ == '__main__':
    app.run(debug=True)