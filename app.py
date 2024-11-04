from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = "helloWorld"

@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("loja.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    con.close()
    return render_template("index.html", datas=data)

@app.route("/add_product", methods=["POST", "GET"])
def add_product():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        quantidade = request.form["quantidade"]
        con = sql.connect("loja.db")
        cur = con.cursor()
        cur.execute("INSERT INTO products (NOME, PRECO, QUANTIDADE) VALUES (?, ?, ?)", (nome, preco, quantidade))
        con.commit()
        con.close()
        flash("Produto cadastrado com sucesso!", "success")
        return redirect(url_for("index"))
    return render_template("add_product.html")

@app.route("/edit_product/<int:id>", methods=["POST", "GET"])
def edit_product(id):
    if request.method == "POST":
        nome = request.form["nome"]
        preco = request.form["preco"]
        quantidade = request.form["quantidade"]
        con = sql.connect("loja.db")
        cur = con.cursor()
        cur.execute("UPDATE products SET NOME = ?, PRECO = ?, QUANTIDADE = ? WHERE ID = ?", (nome, preco, quantidade, id))
        con.commit()
        con.close()
        flash("Produto atualizado com sucesso!", "success")
        return redirect(url_for("index"))

    con = sql.connect("loja.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM products WHERE ID = ?", (id,))
    data = cur.fetchone()
    con.close()
    return render_template("edit_product.html", datas=data)

@app.route("/delete_product/<int:id>", methods=["GET"])
def delete_product(id):
    con = sql.connect("loja.db")
    cur = con.cursor()
    cur.execute("DELETE FROM products WHERE ID = ?", (id,))
    con.commit()
    con.close()
    flash("Produto deletado com sucesso!", "warning")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
