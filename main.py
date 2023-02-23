from sqlite3 import IntegrityError
from flask import Flask, render_template, request, url_for, flash, abort, redirect
from models.Bebida import Bebida
from models.Cliente import Cliente
from flask_login import LoginManager

from models.Endereco import Endereco
from models.Pizza import Borda, Sabor, Tamanho

app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)

piz_nome = "Pizzaria do seu Zé"
user = {}

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name, piz_nome=piz_nome)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/NovoUsuario', methods=["GET", "POST"])
def form_new_user():
    if request.method == "POST":
        try:
            cli = Cliente()
            cli.post(list(request.form.values()))
            return redirect(url_for("form_new_address"))
        except IntegrityError:
            return "<h2>Não foi posivel criar usuaria,\
                Email já cadastrato</h2>"
    return render_template('create/user_1.html', piz_nome=piz_nome)

@app.route('/NovoEndereco', methods=["GET", "POST"])
def form_new_address():
    if request.method == "POST":
        try:
            end = Endereco()
            print(end.post([
                1,
                request.form["numero"],
                request.form["rua"],
                request.form["cidade"],
                request.form["bairro"],
                ]))
            return redirect("/")
        except IntegrityError:
            return "<h2>Não foi posivel criar endereço</h2>"
    return render_template('create/end_1.html', piz_nome=piz_nome)

@app.route('/user/<id>')
def get_user(id=1):
    cli = Cliente()
    nome = cli.get(id)[2]
    return render_template('index.html', name=nome, piz_nome=piz_nome)

@app.route('/pedido', methods=["GET", "POST"])
def pedido(id=1):
    if request.method == 'POST':
        print(request.form)
    # cli = Cliente()
    # nome = cli.get(id)[2]
    sabores = Sabor().get_all()
    tam = Tamanho().get_all()
    bebidas = Bebida().get_all()
    bordas = Borda().get_all()
    return render_template('pedido.html', piz_nome=piz_nome, tam=tam, sabores=sabores, bordas=bordas, bebidas=bebidas)

if "__main__" == __name__:
    app.run(debug=True)
