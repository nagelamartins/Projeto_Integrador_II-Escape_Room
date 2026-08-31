from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import random

mensagens_erro = [
    "Acesso negado. Mas gostei da confiança.",
    "Hmm... não.",
    "Você está indo por um bom caminho, pena que não é o certo.",
    "Quase. Ou talvez bem longe. Vamos descobrir.",
    "Essa resposta tem personalidade. Pena que está errada.",
    "Interessante escolha. Incorreta, mas interessante.",
    "Eu poderia fingir que estava certo. Mas você descobriria.",
    "O sistema diz que não. Eu concordo com o sistema.",
    "Essa porta continua trancada. Ela parece ter opiniões fortes.",
    "Não abriu. Aparentemente, portas não funcionam com esperança.",
    "Tenho boas e más notícias. A boa: você tentou. A má: estava errado.",
    "Não. Mas admiro sua ousadia.",
    "404: resposta correta não encontrada.",
    "Não quero criar um clima ruim, mas... não."
]

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///escaperoom.db"
app.secret_key = "uma_frase_qualquer_dificil_de_adivinhar"

db = SQLAlchemy(app)


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

class Desempenho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    sala = db.Column(db.Integer, nullable=False)
    acertou_de_primeira = db.Column(db.Boolean, nullable=False)


@app.route("/", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        nome_usuario = request.form["usuario"]
        senha = request.form["senha"]

        usuario = Usuario.query.filter_by(nome_usuario=nome_usuario).first()

        if usuario and check_password_hash(usuario.senha, senha):
            session["usuario_id"] = usuario.id
            return redirect(url_for("home"))
        else:
            erro = "Usuário ou senha incorretos."

    return render_template("login.html", erro=erro)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome_usuario = request.form["usuario"]
        senha = request.form["senha"]

        senha_criptografada = generate_password_hash(senha)

        novo_usuario = Usuario(nome_usuario=nome_usuario, senha=senha_criptografada)
        db.session.add(novo_usuario)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("cadastro.html")


@app.route("/home")
def home():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    return render_template("inicio.html")

@app.route("/sala1", methods=["GET", "POST"])
def sala1():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "16":
            acertou_de_primeira = not session.get("errou_sala1", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=1,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala1", None)

            return redirect(url_for("sala2"))
        else:
            session["errou_sala1"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala1.html", erro=erro)

@app.route("/sala2", methods=["GET", "POST"])
def sala2():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "YOP":
            acertou_de_primeira = not session.get("errou_sala2", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=2,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala2", None)

            return redirect(url_for("sala3"))
        else:
            session["errou_sala2"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala2.html", erro=erro)    

@app.route("/sala3", methods=["GET", "POST"])
def sala3():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "AZUL":
            acertou_de_primeira = not session.get("errou_sala3", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=3,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala3", None)

            return redirect(url_for("sala4"))
        else:
            session["errou_sala3"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala3.html", erro=erro)    

@app.route("/sala4", methods=["GET", "POST"])
def sala4():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "15":
            acertou_de_primeira = not session.get("errou_sala4", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=4,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala4", None)

            return redirect(url_for("sala5"))
        else:
            session["errou_sala4"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala4.html", erro=erro)  

@app.route("/sala5", methods=["GET", "POST"])
def sala5():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "113":
            acertou_de_primeira = not session.get("errou_sala5", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=5,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala5", None)

            return redirect(url_for("sala6"))
        else:
            session["errou_sala5"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala5.html", erro=erro)  

@app.route("/sala6", methods=["GET", "POST"])
def sala6():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "30":
            acertou_de_primeira = not session.get("errou_sala6", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=6,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala6", None)

            return redirect(url_for("sala7"))
        else:
            session["errou_sala6"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala6.html", erro=erro) 

@app.route("/sala7", methods=["GET", "POST"])
def sala7():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "19":
            acertou_de_primeira = not session.get("errou_sala7", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=7,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala7", None)

            return redirect(url_for("sala8"))
        else:
            session["errou_sala7"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala7.html", erro=erro) 

@app.route("/sala8", methods=["GET", "POST"])
def sala8():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "18":
            acertou_de_primeira = not session.get("errou_sala8", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=8,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala8", None)

            return redirect(url_for("sala9"))
        else:
            session["errou_sala8"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala8.html", erro=erro) 

@app.route("/sala9", methods=["GET", "POST"])
def sala9():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "21":
            acertou_de_primeira = not session.get("errou_sala9", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=9,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala9", None)

            return redirect(url_for("sala10"))
        else:
            session["errou_sala9"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala9.html", erro=erro) 

@app.route("/sala10", methods=["GET", "POST"])
def sala10():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    erro = None

    if request.method == "POST":
        resposta = request.form["resposta"]

        if resposta == "51":
            acertou_de_primeira = not session.get("errou_sala10", False)

            registro = Desempenho(
                usuario_id=session["usuario_id"],
                sala=10,
                acertou_de_primeira=acertou_de_primeira
            )
            db.session.add(registro)
            db.session.commit()

            session.pop("errou_sala10", None)

            return redirect(url_for("fim"))
        else:
            session["errou_sala10"] = True
            erro = random.choice(mensagens_erro)

    return render_template("sala10.html", erro=erro) 

@app.route("/fim")
def fim():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    return render_template("fim.html")

if __name__ == "__main__":
    app.run(debug=True)