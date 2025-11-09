from flask import Flask, render_template, request  # ✅ Incluído 'request'
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return render_template('index.html')

# Listagem de alunos
@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.lista()
    return render_template('aluno/listar.html', lista=lista)

# Saudação via query string
@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

# Saudação via parâmetro de rota
@app.route('/saudacao/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

# Listagem de professores
@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.lista()
    return render_template('professor/listar.html', lista=lista)

# Listagem de cursos
@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.lista()
    return render_template('curso/listar.html', lista=lista)

# Login via formulário POST
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    email = request.form['email']
    senha = request.form['senha']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

# Cadastro via GET e POST
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    dados = ""
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        cpf = request.form['cpf']
        nome_mae = request.form['nome_mae']
        dados = (
            f"Cadastro Recebido:\n\n"
            f"Nome: {nome},\n"
            f"Nasc: {data_nascimento},\n"
            f"CPF: {cpf},\n"
            f"Mãe: {nome_mae}"
        )
    return render_template('cadastro/cadastro.html', valor_recebido=dados)

# Execução do app
if __name__ == '__main__':
    app.run(debug=True)
