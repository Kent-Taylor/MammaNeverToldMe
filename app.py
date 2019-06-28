from flask import Flask, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)



class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

@app.route('/guide', methods=["POST"])
def add_guide():
    title = request.json['postTitle']
    content = request.json['postContent']

    new_guide = Guide(title, content)

    db.session.add(new_guide)
    db.session.commit()

    guide = db.session.query(Guide.id, Guide.title, Guide.content).filter(Guide.title == title).all()

    return jsonify(guide)

@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    guide = Guide.query.get(id)
    title = request.json['postTitle']
    content = request.json['postContent']

    guide.title = title
    guide.content = content

    db.session.commit()
    return jsonify(guide)

@app.route("/guide/<id>", methods=["DELETE"])
def guide_delete(id):
    guide = Guide.query.get(id)
    db.session.delete(guide)
    db.session.commit()

    return "Post was succesfully deleted"


@app.route('/guide', methods=["GET"])
def postedposts():
    guides = db.session.query(Guide.id, Guide.title, Guide.content).all()

    return jsonify(guides)

    

if __name__== '__main__':
    app.run(debug=True)