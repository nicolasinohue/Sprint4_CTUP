from sqlalchemy import Column, Integer, Numeric, String, Date, Float, ForeignKey, Sequence
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base()

class ClientePF(Base):
    __tablename__ = 'clientePf'
    id = Column(Numeric, primary_key=True)
    cpf = Column(String(14), unique=True, nullable=False)
    data_nasc = Column(Date)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), unique=True, nullable=False)
    cliente = relationship("Cliente", back_populates="clientes_pf")
    senhas = relationship("Senhas", back_populates="cliente_pf", cascade='all, delete-orphan', uselist=False)

class ClientePJ(Base):
    __tablename__ = 'clientePj'
    id = Column(Numeric, primary_key=True)
    cnpj = Column(String(18), unique=True, nullable=False)
    data_fund = Column(Date)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), unique=True, nullable=False)
    cliente = relationship("Cliente", back_populates="clientes_pj")
    senhas = relationship("Senhas", back_populates="cliente_pj", cascade='all, delete-orphan', uselist=False)

class Senhas(Base):
    __tablename__ = 'senha'
    id = Column(Integer, primary_key=True)
    senha = Column(String(40))
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    cliente = relationship('Cliente', back_populates='senhas')
    cliente_pf_id = Column(Numeric, ForeignKey('clientePf.id'), nullable=False)
    cliente_pf = relationship("ClientePF", back_populates="senhas")
    cliente_pj_id = Column(Numeric, ForeignKey('clientePj.id'), nullable=False)
    cliente_pj = relationship("ClientePJ", back_populates="senhas")

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cep = Column(String(10), nullable=False)
    email = Column(String(100), nullable=False)
    clientes_pf = relationship("ClientePF", back_populates="cliente")
    clientes_pj = relationship("ClientePJ", back_populates="cliente")
    apolices = relationship("Apolice", back_populates="cliente")
    pagamentos = relationship("Pagamento", back_populates="cliente")
    bikes = relationship("Bike", back_populates="cliente")
    senhas = relationship('Senhas', back_populates='cliente', cascade='all, delete-orphan')

class Apolice(Base):
    __tablename__ = 'apolice'
    id = Column(Numeric, primary_key=True)
    titular = Column(String(30))
    info_bike = Column(String(30))
    valor_assegurado = Column(Float)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), unique=True, nullable=False)
    cliente = relationship("Cliente", back_populates="apolices")
    plano = relationship("Plano", back_populates="apolice")

class Pagamento(Base):
    __tablename__ = 'pagamento'
    id = Column(Numeric, primary_key=True)
    valor = Column(Float)
    parcelas = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), unique=True, nullable=False)
    cliente = relationship("Cliente", back_populates="pagamentos")
    cartao = relationship("Cartao", uselist=False, back_populates="pagamento")
    boleto = relationship("Boleto", back_populates="pagamento")

class Cartao(Base):
    __tablename__ = 'cartao'
    num_cartao = Column(Integer, primary_key=True)
    titular = Column(String(100))
    data_val = Column(Date)
    cvv = Column(Integer)
    modalidade = Column(String(8))
    pagamento_id = Column(Integer, ForeignKey('pagamento.id'), unique=True, nullable=False)
    pagamento = relationship("Pagamento", back_populates="cartao")

class Boleto(Base):
    __tablename__ = 'boleto'
    id = Column(Numeric, primary_key=True)
    titular = Column(String(100))
    remetente = Column(String(100))
    venc_boleto = Column(Date)
    cod_bol = Column(String(50))
    agencia = Column(String(50))
    pagamento_id = Column(Integer, ForeignKey('pagamento.id'), unique=True, nullable=False)
    pagamento = relationship("Pagamento", back_populates="boleto")

class Bike(Base):
    __tablename__ = 'bike'
    id = Column(Numeric, Sequence('sequencia_id'), primary_key=True)
    n_serie = Column(String(40))
    nick = Column(String(40))
    tipo_quadro = Column(String(15))
    quantmarcha = Column(Integer)
    tiposuspensao = Column(String(20))
    tipofreio = Column(String(14))
    modalidade = Column(String(14))
    ano_fab = Column(Date)
    marca = Column(String(20))
    modelo = Column(String(15))
    valor = Column(Float)
    num_serie = Column(String(20))
    acessorio = Column(String(20))
    tipopneu = Column(String(12))
    tamanho_pneu = Column(Numeric(2))
    observacoes = Column(String(100))
    nf = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    cliente = relationship("Cliente", back_populates="bikes")
    vistorias = relationship("Vistoria", back_populates="bike")

class Vistoria(Base):
    __tablename__ = 'vistoria'
    id = Column(Numeric, primary_key=True)
    data_vistoria = Column(Date)
    etapa = Column(String(50))
    bike_id = Column(Integer, ForeignKey('bike.id'), unique=True, nullable=False)
    bike = relationship("Bike", back_populates="vistorias")

class Plano(Base):
    __tablename__ = 'plano'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30))
    valor = Column(Float)
    cobertura = Column(String(200))
    apolice_id = Column(Integer, ForeignKey('apolice.id'), unique=True, nullable=False)
    apolice = relationship("Apolice", back_populates="planos")