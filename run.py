from xlsxwriter import Workbook
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from cadmus.cadmus import Cadmus

obj = Cadmus()
obj.access_site()
obj.move_to_element()
obj.get_name_local()
obj.get_desc()
obj.driver_quit()


diretorio_arquivos = os.getcwd()+'\\arquivos'
os.makedirs(diretorio_arquivos, exist_ok=True)
wb = Workbook(diretorio_arquivos+r'\vagas.xlsx')
ws = wb.add_worksheet('CADMUS')
bold = wb.add_format({'bold': 1})
ws.write('A1', 'Nome', bold)
ws.write('B1', 'Local', bold)
ws.write('C1', 'Descrição', bold)
row = 1
col = 0
for val in obj.gen_data:
    ws.write_string(row, col, val['name'])
    ws.write_string(row, col+1, val['local'])
    ws.write_string(row, col+2, val['desc'])
    row += 1
wb.close()


msg = MIMEMultipart()
msg['From'] = 'email_origem_example@gmail.com'
msg['To'] = 'email_destino_example@gmail.com'
msg['Subject'] = 'E-mail automático Vagas'
pwd = 'SENHA_AQUI'
body = """
E-mail automático.

Em anexo, arquivo em exel contendo as vagas disponíveis no portal https://cadmus.com.br/vagas-tecnologia/!"""

msg.attach(MIMEText(body,'plain'))
server = smtplib.SMTP('smtp.gmail.com', '587')
server.starttls()

server.login(msg['From'], pwd)
file = open(diretorio_arquivos+'\\vagas.xlsx', 'rb')
app = MIMEApplication(file.read(), 'xlsx')
app.add_header('Content-Disposition', 'attachment; filename=Vagas_Cadmus.xlsx')
msg.attach(app)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

