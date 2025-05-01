from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return "ระบบเชื่อมต่อฐานข้อมูลสำเร็จ!"

@app.route('/products')
def show_products():
    rows = [
        {'PN': 1, 'ProductCode': 'P001', 'Name': 'เหล็กแผ่น', 'Price1': 55.00, 'SUnit': 'แผ่น'},
        {'PN': 2, 'ProductCode': 'P002', 'Name': 'เมทัลชีท', 'Price1': 65.50, 'SUnit': 'แผ่น'},
    ]
    return render_template("products.html", rows=rows)

@app.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        return redirect('/products')
    return render_template("add_product.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
