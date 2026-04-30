from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_sqlite_data():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except sqlite3.Error:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    data = []
    error_message = None

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                data = json.load(f)
        except Exception:
            data = []
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
        except Exception:
            data = []
    elif source == 'sql':
        data = get_sqlite_data()
        if data is None:
            return render_template('product_display.html', error_message="Database error")
    else:
        return render_template('product_display.html', error_message="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            data = [item for item in data if item['id'] == product_id]
            if not data:
                error_message = "Product not found"
        except ValueError:
            error_message = "Product not found"

    return render_template('product_display.html', products=data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
