from flask import Flask
app = Flask(__name__)

@app.route('/curriculo')
def iniciar():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>

        <h1>Currículo</h1>
        <h2>Informações Pessoais</h2>
        <ul>
        <li>Nome: Analice Carvalho Fernandes</li>
        <li>Email: 12400572@aluno.cotemig.com.br</li>
        <li>Telefone: (31) 7146-9693</li></ul>


        
        <h2>Experiência Profissional</h2>
        <ul>
        <li>Empresa: COTEMIG</li>
        <li>Cargo: Aluno</li>
        <li>Período: Terceiro ano 2026</li></ul>

    </body>
    </html>


'''


if __name__ == '__main__':
    app.run(debug=True)