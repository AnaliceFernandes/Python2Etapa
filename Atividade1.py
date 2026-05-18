from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def explicar():
    return '''
    <h1> O que é um decorator em Python </h1> 
    Decorator é uma ferramenta Python (iniciada por @) que envolve uma função, permitindo modificar ou estender seu comportamento sem alterar o código original.

    <h1> Para que ele serve</h1> 
    Servem principalmente para mapear URLs a funções de visualização (views), além de modificar comportamentos de funções sem alterar seu código original.

    <h1> Como ele é utilizado no Flask</h1>
    São usados principalmente para associar URLs a funções de visualização (rotas) e estender comportamentos, como autenticação e logging, de forma modular e reutilizável, sem alterar o código original da função.
'''


if __name__ == '__main__':
    app.run(debug=True)