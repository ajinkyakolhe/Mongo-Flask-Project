from flask import Flask,request, render_template
from flask_pymongo import PyMongo
import re

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test-database'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test-database'

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def get_all_stars():
    infoc = mongo.db.info
    output = []
    for s in infoc.find():
        output.append({'title': s['title']})
    return render_template('t_4.html')

@app.route("/echo")
def echo():
    pump = request.args.get('title')
    pump2 = request.args.get('year')
    pump3 = request.args.get('apidata')
    pump4 = request.args.get('rating')
    pump5 = request.args.get('ratingv')
    print(pump)
    infoc = mongo.db.info
    out = []
    for s in infoc.find():
        atr1,atr2,atr3 = s['title'],s['updated'], s['Tags']
        if bool(re.search(r'(.*)' + re.escape(pump) + '(.*)', atr1)) \
                and bool(re.search(r'(.*)' + re.escape(pump2) + '(.*)', atr2)) \
                and bool(re.search(r'(.*)' + re.escape(pump3) + '(.*)', atr3)) :
            if pump4 == "greater than":
                if s['rating'] > pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'category': s['category'],
                                'id': s['id'],'rating': s['rating']})
            elif pump4 == "gte":
                if s['rating'] >= pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'category': s['category'],
                                'id': s['id'], 'rating': s['rating']})
            elif pump4 == "less than":
                if (s(['rating'] < pump5) or (s['rating'] == '')):
                    out.append({'title': s['title'], 'description': s['description'], 'category': s['category'],
                                'id': s['id'], 'rating': s['rating']})
            elif pump4 == "le":
                if s['rating'] <= pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'category': s['category'],
                                'id': s['id'], 'rating': s['rating']})
            elif pump4 == "equal":
                if s['rating'] == pump5 or s['rating'] == '':
                    out.append({'title': s['title'], 'description': s['description'], 'category': s['category'],
                                'id': s['id'], 'rating': s['rating']})
            else:
                print("No output")
    return render_template('t_4.html', show=out)

if __name__ == '__main__':
    app.run(debug=True)