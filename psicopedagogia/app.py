from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        data_nascimento TEXT,
                        contato TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS responsaveis (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        paciente_id INTEGER,
                        FOREIGN KEY(paciente_id) REFERENCES pacientes(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS agendamentos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        paciente_id INTEGER,
                        data TEXT,
                        hora TEXT,
                        FOREIGN KEY(paciente_id) REFERENCES pacientes(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS financeiro (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        descricao TEXT,
                        valor REAL,
                        tipo TEXT,
                        data TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro_paciente', methods=['GET', 'POST'])
def cadastro_paciente():
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        contato = request.form['contato']
        conn = sqlite3.connect('psicopedagogia.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pacientes (nome, data_nascimento, contato) VALUES (?, ?, ?)", 
                       (nome, data_nascimento, contato))
        conn.commit()
        conn.close()
        return redirect(url_for('cadastro_paciente'))
    return render_template('cadastro_paciente.html')

@app.route('/cadastro_responsavel', methods=['GET', 'POST'])
def cadastro_responsavel():
    if request.method == 'POST':
        nome = request.form['nome']
        paciente_id = request.form['paciente_id']
        conn = sqlite3.connect('psicopedagogia.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO responsaveis (nome, paciente_id) VALUES (?, ?)", 
                       (nome, paciente_id))
        conn.commit()
        conn.close()
        return redirect(url_for('cadastro_responsavel'))
    return render_template('cadastro_responsavel.html')

@app.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        data = request.form['data']
        hora = request.form['hora']
        conn = sqlite3.connect('psicopedagogia.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO agendamentos (paciente_id, data, hora) VALUES (?, ?, ?)", 
                       (paciente_id, data, hora))
        conn.commit()
        conn.close()
        return redirect(url_for('agendamento'))
    return render_template('agendamento.html')

@app.route('/financeiro', methods=['GET', 'POST'])
def financeiro():
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        tipo = request.form['tipo']
        data = request.form['data']
        conn = sqlite3.connect('psicopedagogia.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO financeiro (descricao, valor, tipo, data) VALUES (?, ?, ?, ?)", 
                       (descricao, valor, tipo, data))
        conn.commit()
        conn.close()
        return redirect(url_for('financeiro'))
    return render_template('financeiro.html')

# Página de dados registrados
@app.route('/dados_registrados')
def dados_registrados():
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    conn.close()
    return render_template('dados_registrados.html', pacientes=pacientes)

# Página para apagar paciente
@app.route('/apagar_paciente/<int:id>')
def apagar_paciente(id):
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dados_registrados'))

# Página de dados de agendamentos
@app.route('/dados_agendamentos')
def dados_agendamentos():
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agendamentos")
    agendamentos = cursor.fetchall()
    conn.close()
    return render_template('dados_agendamentos.html', agendamentos=agendamentos)

# Página para apagar agendamento
@app.route('/apagar_agendamento/<int:id>')
def apagar_agendamento(id):
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM agendamentos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dados_agendamentos'))

# Página de dados financeiros
@app.route('/dados_financeiros')
def dados_financeiros():
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM financeiro")
    financeiro = cursor.fetchall()
    conn.close()
    return render_template('dados_financeiros.html', financeiro=financeiro)

# Página para apagar financeiro
@app.route('/apagar_financeiro/<int:id>')
def apagar_financeiro(id):
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM financeiro WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dados_financeiros'))

# Rota para editar paciente
@app.route('/editar_paciente/<int:id>', methods=['GET', 'POST'])
def editar_paciente(id):
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        nome = request.form['nome']
        data_nascimento = request.form['data_nascimento']
        contato = request.form['contato']
        cursor.execute("""
            UPDATE pacientes 
            SET nome = ?, data_nascimento = ?, contato = ?
            WHERE id = ?
        """, (nome, data_nascimento, contato, id))
        conn.commit()
        conn.close()
        return redirect(url_for('dados_registrados'))
    else:
        cursor.execute("SELECT * FROM pacientes WHERE id = ?", (id,))
        paciente = cursor.fetchone()
        conn.close()
        return render_template('editar_paciente.html', paciente=paciente)

@app.route('/editar_agendamento/<int:id>', methods=['GET', 'POST'])
def editar_agendamento(id):
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        paciente_id = request.form['paciente_id']
        data = request.form['data']
        hora = request.form['hora']
        cursor.execute("""
            UPDATE agendamentos 
            SET paciente_id = ?, data = ?, hora = ?
            WHERE id = ?
        """, (paciente_id, data, hora, id))
        conn.commit()
        conn.close()
        return redirect(url_for('dados_agendamentos'))
    else:
        cursor.execute("SELECT * FROM agendamentos WHERE id = ?", (id,))
        agendamento = cursor.fetchone()
        conn.close()
        return render_template('editar_agendamento.html', agendamento=agendamento)

@app.route('/editar_financeiro/<int:id>', methods=['GET', 'POST'])
def editar_financeiro(id):
    conn = sqlite3.connect('psicopedagogia.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        tipo = request.form['tipo']
        data = request.form['data']
        cursor.execute("""
            UPDATE financeiro 
            SET descricao = ?, valor = ?, tipo = ?, data = ?
            WHERE id = ?
        """, (descricao, valor, tipo, data, id))
        conn.commit()
        conn.close()
        return redirect(url_for('dados_financeiros'))
    else:
        cursor.execute("SELECT * FROM financeiro WHERE id = ?", (id,))
        financeiro = cursor.fetchone()
        conn.close()
        return render_template('editar_financeiro.html', financeiro=financeiro)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
