# Mangá Scraper e Criador de CBR

Sistema para baixar mangás do unionmangas.top e depois criar CBR. Foi criado com intuito educacional, para aprender sobre a biblioteca BeautifulSoup4. 

## Instalação

É necessário ter o Python instalado.
Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar o BeautifulSoup4. 

```bash
pip install beautifulsoup4
```

## Modo de Usar

Ao executar o comando abaixo será apresentado um prompt com as opções de utilização do programa. É possível baixar todos os capítulos de um anime (colocando a URL da lista de capítulos, quando for solicitado), ou baixar um capítulo específico (colocando a URL de leitura do capítulo). Será então criada uma pasta o nome do anime, e dentro dela uma pasta com o número do capítulo e em seu interior as imagens do mangá.
```python
python scrape.py
```
É possível também criar o CBR (comic book reader) do mangá baixado, para tando execute o comando abaixo e siga as instruções.
```python
python compress.py
```

## Contribuição e Implementações Futuras
Sinta-se livre para fork e implementar novas funcionalidades com intuito de estudar BeautifulSoup4 e Python em geral.

Tenho intenção de modificar esses arquivos para OOP, e de criar uma API com 3 endpoints, que traga as informações de mangás, capítulos, e páginas.

## License
[MIT](https://choosealicense.com/licenses/mit/)