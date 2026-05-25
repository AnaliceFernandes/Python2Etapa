from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def questao1():
    nomep = "Analice"
    return render_template('questao1.html', nome=nomep)

@app.route('/questao2')
def questao2():
    nomep = "Analice"
    idadep = "17"
    return render_template('questao2.html', nome=nomep, idade=idadep)


@app.route('/questao3')
def questao3():
    nomep = "Analice"
    emailp = "12400572@aluno.cotemig.com.br"
    return render_template('questao3.html', nome=nomep, email=emailp)



@app.route('/questao4')
def questao4():
    lista_alunos = [
        {"nome": "Analice", "nota": 6},
        {"nome": "Isabela", "nota": 8},
        {"nome": "Hugo", "nota": 10}
    ]
    return render_template('questao4.html', alunos=lista_alunos)



@app.route('/questao5')
def questao5():
    lista_alunos = [
        {"nome": "Analice", "nota": 6},
        {"nome": "Isabela", "nota": 8},
        {"nome": "Hugo", "nota": 10}
    ]    

    return render_template('questao5.html', alunos=lista_alunos)



if __name__ == '__main__':
    app.run(debug=True)