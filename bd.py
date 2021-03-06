from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Setores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_setor = db.Column(db.String(80))
    def __init__(self, nome_setor):
        self.nome_setor = nome_setor

class Lojas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_loja = db.Column(db.String(80))
    nome_setor = db.Column(db.String(80))
    def __init__(self, nome_loja, nome_setor):
        self.nome_loja = nome_loja
        self.nome_setor = nome_setor

class Funcionarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String(80))
    nome_loja = db.Column(db.String(80))
    tipo_funcionario = db.Column(db.String(80))
    cpf = db.Column(db.String(80))
    status = db.Column(db.String(80))
    telefone = db.Column(db.String(80))
    def __init__(self, nome_funcionario, nome_loja, tipo_funcionario, cpf, status, telefone):
        self.nome_funcionario = nome_funcionario
        self.nome_loja = nome_loja
        self.tipo_funcionario = tipo_funcionario
        self.cpf = cpf
        self.status = status
        self.telefone = telefone

class RequisicoesDeCadastros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String(80))
    data_requisicao = db.Column(db.String(80))
    nome_loja = db.Column(db.String(80))
    def __init__(self, nome_funcionario, data_requisicao, nome_loja):
        self.nome_funcionario = nome_funcionario
        self.data_requisicao = data_requisicao
        self.nome_loja = nome_loja

class RequisicoesDePromocoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_funcionario = db.Column(db.String(80))
    data_requisicao = db.Column(db.String(80))
    nome_loja = db.Column(db.String(80))
    status = db.Column(db.String(80))
    corpo = db.Column(db.String(80))
    def __init__(self, nome_funcionario, data_requisicao, nome_loja, status, corpo):
        self.nome_funcionario = nome_funcionario
        self.data_requisicao = data_requisicao
        self.nome_loja = nome_loja
        self.status = status
        self.corpo = corpo


######################### CRUDE OPERATIONS #############################
def SearchLeader(requester):
    print(requester.loja)
    leaderFound = Funcionarios.query.filter_by(nome_loja=requester.loja, tipo_funcionario='Líder').all()
    if(len(leaderFound)==0):
        print("Not Found")
        return(['',''])
    else:
        leader = [leaderFound.telefone, leaderFound.nome_funcionario]
        return(leader)

def searchByUsername(usernName):
    data_user = Funcionarios.query.filter_by(nome_funcionario=usernName).all()
    if(len(data_user)==0):
        return False
    else:
        return True

def checkIfUserExists(tempUser):
    data_user = Funcionarios.query.filter_by(telefone=tempUser.telefone).all()
    if(len(data_user)==0):
        tempUser.passo = "B1"
        print("número não existe no banco, realizando pré cadastro")
        return tempUser
    else:
        tempUser.passo = "A1"
        tempUser.telefone = data_user[0].telefone
        tempUser.nome_funcionario = data_user[0].nome_funcionario
        tempUser.loja = data_user[0].nome_loja
        print("número existe no banco, realizando perguntas")
        return tempUser

def insertFuncionario():
    data = Funcionarios(input('Digite o nome do funcionario: '), input('Digite o nome da loja: '), input('Digite o cargo: '), 
    input('Digite o CPF do funcionario: '), 'Ativo', input('Digite o telefone do funcionario: '))
    db.session.add(data)
    db.session.commit()

def SelectRequests():
    requisicoes = RequisicoesDePromocoes.query.all()
    setores = ""
    for num, r in enumerate(requisicoes, start=1):
        setores += "\\n" + str(num) + str(r.corpo) + "\\n"
    return(setores)

def SelectSetores():
    data_setores = Setores.query.all()
    setores = ""
    for num, d in enumerate(data_setores, start=1):
        setores += "\\n selecione " + str(num) + " para " + str(d.nome_setor)
    return(setores)
def SelectSetores_Unique(indexToCheck):
    data_setor = Lojas.query.filter_by(id=indexToCheck).first()
    setores = data_setor.nome_setor
    return(str(setores))

def SelectLojas(sectorToCheck):
    print(sectorToCheck)
    data_lojas = Lojas.query.filter_by(nome_setor=sectorToCheck).all()
    lojas = ""
    for num, d in enumerate(data_lojas, start=1):
        lojas += "\\n selecione " + str(d.id) + " para " + str(d.nome_loja)
    return(lojas)
def SelectLojas_Unique(indexToCheck):
    data_setor = Setores.query.filter_by(id=indexToCheck).first()
    setores = data_setor.nome_setor
    return(str(setores))