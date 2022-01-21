# vagas-cadmus

Projeto com a finalidade de extrair os dados das vagas do portal da CADMUS e enviar um e-mail automático com os dados em um arquivo do tipo excel.

# Tecnologia


- [Python 3.9.10](https://www.python.org/downloads/release/python-3910/)


## Bibliotecas

- [selenium](https://selenium-python.readthedocs.io/)
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [email](https://docs.python.org/3/library/email.html)
- [os](https://docs.python.org/3/library/os.html)
- [pyderman](https://pypi.org/project/pyderman/)
- [time](https://docs.python.org/3/library/time.html)

## Executar localmente

Utilizando Git Bash


```bash
git clone https://github.com/Carlosykaa/vagas-cadmus.git
```
Acessar pasta do projeto
```bash
cd vagas-cadmus
```

Instalar as dependências
```bash
pip install -r requirements.txt
```
Inserir e-mail de origem e destinatário no arquivo run.py
```python
msg['From'] = 'email_origem_example@gmail.com'
msg['To'] = 'email_destino_example@gmail.com'
```

Inserir a senha do e-mail de origem no arquivo run.py
```python
pwd = 'SENHA_AQUI'
```

Executar o programa
```bash
python.exe run.py
```

## Autor

- [@Carlosykaa](https://github.com/Carlosykaa)