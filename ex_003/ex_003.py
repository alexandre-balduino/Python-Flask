
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="soares98",
        database="cadastro"
    )

@app.route("/", methods=["GET"])
def main():
    try:
        db = connect_db()
        cursor = db.cursor()
        comando = '''
SELECT id, nome, profissao
FROM gafanhotos
        '''
        cursor.execute(comando)
        dados = cursor.fetchall()
        cursor.close()
        db.close()
        return render_template("index.html", lista=dados)
    except Exception as e:
        return f"Erro ao conectar: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
