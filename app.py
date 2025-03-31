from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopping_list.db'
db = SQLAlchemy(app)

# Model bazy danych
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Tworzenie bazy danych (tylko raz)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route("/add", methods=["POST"])
def add_item():
    data = request.get_json()
    item_name = data.get("name")
    if item_name:
        new_item = Item(name=item_name)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"success": True, "item": {"id": new_item.id, "name": new_item.name}})
    return jsonify({"success": False})

@app.route("/delete/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return "", 204  # Kod 204 = "No Content" (sukces, ale bez odpowiedzi)
    return "", 404  # Jeśli element nie istnieje


@app.route("/edit/<int:item_id>", methods=["POST"])
def edit_item(item_id):
    data = request.get_json()
    new_name = data.get("new_name")

    item = Item.query.get(item_id)
    if item:
        item.name = new_name
        db.session.commit()
        return jsonify({"success": True, "new_name": new_name})

    return jsonify({"success": False}), 400


if __name__ == '__main__':
    app.run(debug=True)
