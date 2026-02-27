
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    nome = None
    if request.method == "POST":
        nome = request.form.get("nome_usuario")
    return render_template("index.html", nome=nome)


if __name__ == "__main__":
    app.run(debug=True)
