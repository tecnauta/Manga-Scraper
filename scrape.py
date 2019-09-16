from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import re
import os
import sys

urls = []
urlsImgs = []

print()
print("====================================================")
print("============== O que deseja fazer? =================")
print("====================================================")
print("Para baixar todos os capítulos de um anime digite: 1")
print("Para baixar um capítulo de um anime digite.......: 2")
print("Para sair digite.................................: 0")
inputPergunta = input()

def fnBaixarImagem(nomeImagem, enderecoImagem):
    print(".", end="", flush=True)

    try:
        with open(nomeImagem, 'wb') as handle:
            response = requests.get(enderecoImagem, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break
                
                handle.write(block)
    except:
        print()
        sys.exit("Sem acesso ao site")

if inputPergunta == "1":
    inputUrlAllChapters = input("Digite a URL completa da lista de capítulos que deseja baixar no Union Mangas. Ex.: https://unionmangas.top/manga/shingeki-no-kyojin : ")

    try:
        urlRoot = requests.get(inputUrlAllChapters)
    except:
        print()
        sys.exit("Sem acesso ao site")

    soupRoot = BeautifulSoup(urlRoot.content, features="lxml")

    folderPath = os.getcwd() + '\\' + inputUrlAllChapters.split('/')[-1]
    print(folderPath)
    # Criando diretório do mangá
    try:  
        os.mkdir(folderPath)
    except OSError:  
        print ("Criação do diretório %s falhou" % folderPath)

    # BeautifulSoup dos links da página mãe
    for text in soupRoot.find_all('div', class_='row lancamento-linha'):
        for links in text.find_all('a', href=re.compile('^https://unionleitor.top/leitor/')):
            urls.append(links.get('href'))

    urls.reverse()

    for url in urls:
        # fullPath = os.getcwd() + '\\' + url.split('/')[-2] + '\\' + url.split('/')[-1]
        fullPath = folderPath + '\\' + url.split('/')[-1]
        print(fullPath, end=" ", flush=True)

        # Criando diretórios das imagens
        try:  
            os.mkdir(fullPath)
        except OSError:
            print("O diretório %s já existe. Pulando para o próximo." % fullPath)
            continue

        # BeautifulSoup das imagens da página
        try:
            urlPage = requests.get(url)
        except:
            print()
            sys.exit("Sem acesso ao site")

        soupPage = BeautifulSoup(urlPage.content, features="lxml")

        for textPage in soupPage.find_all('img', class_='img-manga'):
            imageUrl = textPage.get('src')
            imageName = imageUrl.split('/')
            try:
                if (imageName[-1] == 'banner_scan.png'): continue
                fnBaixarImagem(fullPath + '\\' + imageName[-1], imageUrl)
            except IndexError:
                pass
        print()
    print("Finalizado!")

elif inputPergunta == "2":
    inputUrlOneChapters = input("Digite a URL da página do capítulo que deseja baixar no Union Mangas. Ex.: https://unionmangas.top/leitor/Shingeki_no_Kyojin/01 : ")

    folderPath = os.getcwd() + '\\' + inputUrlOneChapters.split('/')[-2]
    fullPath = os.getcwd() + '\\' + inputUrlOneChapters.split('/')[-2] + '\\' + inputUrlOneChapters.split('/')[-1]

    # Criando diretórios
    try:
        os.mkdir(folderPath)
    except OSError:  
        print("O diretório %s já existe. Pulando para o próximo." % fullPath)

    try:
        os.mkdir(fullPath)
    except OSError:
        print("O diretório %s já existe. Pulando para o próximo." % fullPath)

    # BeautifulSoup das imagens da página
    try:
        urlPage = requests.get(inputUrlOneChapters)
    except:
        print()
        sys.exit("Sem acesso ao site")
    
    soupPage = BeautifulSoup(urlPage.content, features="lxml")

    for textPage in soupPage.find_all('img', class_='img-manga'):
        imageUrl = textPage.get('src')
        imageName = imageUrl.split('/')
        try:
            if (imageName[-1] == 'banner_scan.png'): continue
            fnBaixarImagem(fullPath + '\\' + imageName[-1], imageUrl)
        except IndexError:
            pass

    print("Finalizado!")
else:
    print("Finalizado!")