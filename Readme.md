# listdir
lista, compara e copia diretórios

# listfile
lista, compara e copia arquivos

# DboxListFile
Verifica e faz download do Dropbox para o dispositivo de backup
Usa arquivo "config.py":
```python
    photo_root_folder = '/MeusDocs/Photos'  
    dbox_dev_token = 'YOUR_TOKEN_HERE'
```

Uso:
#### python listdir.py pathOrigen pathBackup \[onlyNotFound\] \[copyMissingDir\]

#### python listfile.py pathOrigen pathBackup \[onlyNotFound\] \[copyMissingFiles\]


Exemplos:

#### `python listdir.py c:\temp g:\temp onlyNotFound`
##### mostra os diretórios abaixo de c:\temp que não foram encontrados abaixo de g:\temp

#### `pyhton listdir.py c:\temp g:\temp onlyNotFound copyMissingDir`
##### mostra os diretórios abaixo de c:\temp que não foram encontratods abaixo de g:\temp e copia para g:\temp

#### `python listfile.py c:\temp g:\temp onlyNotFound`
##### mostra os arquivos que não foram encontrados nos diretórios abaixo de g:\temp

#### `python listfile.py c:\temp g:\temp onlyNotFound copyMissingFiles`
##### copia os arquivos dos subdiretórios abaixo de c:\temp que não foram encontrados nos subdiretórios abaixo de g:\temp


Observação: Tanto _listdir_ quanto _listfile_ verificam apenas um nível de diretórios abaixo do diretório informado.


Executado a última vez com python 3.8.5
