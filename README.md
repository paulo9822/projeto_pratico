### API de Dados

* A API de Dados é um mini servidor backend em Python para fornecimento de informações a partir de uma base de dados csv de alunos com rotas para endpoints de filtragem de registros.

* O servidor é construido com Flask.

#### Pré-requisitos

* Flask ([Documentação](https://flask.palletsprojects.com/en/2.3.x/))

    > `pip install Flask`

* Pandas ([Documentação](https://pandas.pydata.org/))

    > `pip install pandas`

#### Rotas

* /
    * Rota que renderiza a página principal

* /registros
    * Rota que renderiza as informações de todos os registros

* /registros/query
    * Rota para pesquisas personalizadas com variáveis passadas por GET.


#### URL com arquivo csv. para pesquisa

https://drive.google.com/file/d/1_g6fYGFLb4evK3MLV_tBr4BldN6V1g5E/view
