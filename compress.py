import os
import zipfile

folderNames = []
print()
print("====================================================")
print("============== O que deseja fazer? =================")
print("====================================================")
print("Para criar CBR de todas as pastas digite: 1")
print("Para criar CBR de uma única pasta digite: 2")
print("Para sair digite........................: 0")
inputPergunta = input()
print()

if inputPergunta == "1":
    inputNomeDiretorio = input("Digite o nome do diretório onde estão as pasdas dos capítulos. Ex.: C:\\Shingeki_no_Kyojin : ")
    inputFileNamePrefix = input("Digite o prefixo do nome dos arquivos. Ex.: Shingeki_No_Kyojin_ : ")

    # directories = [x[0] for x in os.walk(os.getcwd())]
    directories = [x[0] for x in os.walk(inputNomeDiretorio)]
    directories.pop(0)

    for directory in directories:
        if (directory == 'env'): continue
        folderNames.append(directory.split('\\')[-1])

    def zipdir(path, ziph):
        length = len(path)

        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            folder = root[length:] # path without "parent"
            for file in files:
                ziph.write(os.path.join(root, file), os.path.join(folder, file))

    for folderName in folderNames:
        print(inputFileNamePrefix + folderName + '.cbr')
        if __name__ == '__main__':
            zipf = zipfile.ZipFile(inputFileNamePrefix + folderName + '.cbr', 'w', zipfile.ZIP_DEFLATED)
            zipdir(inputNomeDiretorio + '\\' + folderName, zipf)
            zipf.close()
    
    print("Finalizado!")
elif inputPergunta == "2":
    inputNomeDiretorio = input("Digite o nome do diretório onde estão os arquivos de imagem. Ex.: C:\\Shingeki_no_Kyojin\\118 ")
    inputFileNamePrefix = input("Digite o prefixo do nome dos arquivos. Ex.: Shingeki_No_Kyojin_118 : ")

    def zipdir(path, ziph):
        length = len(path)

        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            folder = root[length:] # path without "parent"
            for file in files:
                ziph.write(os.path.join(root, file), os.path.join(folder, file))

    if __name__ == '__main__':
        zipf = zipfile.ZipFile(inputFileNamePrefix + '.cbr', 'w', zipfile.ZIP_DEFLATED)
        zipdir(inputNomeDiretorio, zipf)
        zipf.close()

    print("Finalizado!")
else:
    print("Finalizado!")
