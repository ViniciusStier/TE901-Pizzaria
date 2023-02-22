from flask import Flask, render_template, request
from database.Cliente import Cliente


app = Flask(__name__)

piz_nome = "Pizzaria do seu Zé"

@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name, piz_nome=piz_nome)

@app.route('/NovoUsuario', methods=["GET", "POST"])
def form_new_user():
    if request.method == "POST":
        cli = Cliente(**request.form)
        print(cli.post())
        cli.commit()
    return render_template('create/user_1.html', piz_nome=piz_nome)

@app.route('/user/<id>')
def get_user(id=1):
    cli = Cliente(id=id)
    print(cli)
    return render_template('index.html', name=cli.nome, piz_nome=piz_nome)

if "__main__" == __name__:
    app.run(debug=True)
