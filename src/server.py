from flask import Flask
import controllers

app = Flask(__name__)

app.add_url_rule('/', view_func=controllers.index)
app.add_url_rule('/registros', view_func=controllers.registros)
app.add_url_rule('/registros/query', view_func=controllers.query)
app.add_url_rule('/registros/formulario', view_func=controllers.formulario, methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True, port=80)