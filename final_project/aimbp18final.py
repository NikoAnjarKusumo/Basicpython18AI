#modul yang digunakan
import smtplib, ssl 
import imghdr
from email.message import EmailMessage

#akun dan password
akun_email = "aimbptes005@gmail.com"
pass_email = "*****"

#akun penerima dalam file txt
penerima = open("emails.txt", "r")
data = penerima.read()
email_penerima = data.split("\n")
penerima.close()

#isi Email
subject = "Mengirim Email dengan Python Final Project"
body = """
Ini final project basic python AI For Indonesia
"""
#fungsi utama pengirim email
em = EmailMessage()
em['From'] = akun_email
em['To'] = email_penerima
em['Subject'] = subject
em.set_content(body)

#atach gambar
images_files =["gojo.png", "toji.png"]

for gambar in images_files:
    with open(gambar, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

        em.add_attachment(image_data, maintype = 'image', subtype = image_type, filename = image_name)

#atach pdf
pdf_files = ["Basic Python.pdf"]

for pdf in pdf_files:
    with open(pdf, 'rb') as f:
        pdf_data = f.read()
        pdf_name = f.name

        em.add_attachment(pdf_data, maintype = 'pdf', subtype = "octret-stream", filename = pdf_name)

#menangani login prot sssl pada gmail
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(akun_email, pass_email)
    smtp.sendmail(akun_email, email_penerima, em.as_string())
    print("Terkirim\n"+ data)