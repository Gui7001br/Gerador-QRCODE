import tkinter as tk
from pyqrcode import create

def generate_qr_code():
    """Função para gerar o QR Code com base no texto inserido pelo usuário"""
    qr_code = create(text.get())
    qr_code.png('qr_code.png', scale=10)

    image = tk.PhotoImage(file='qr_code.png')
    label_image.config(image=image)
    label_image.image = image

# Inicialização da aplicação
app = tk.Tk()
app.title("Gerador de QR Code")

# Criação do frame principal
frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

# Criação da variável de texto para armazenar o texto inserido pelo usuário
text = tk.StringVar()

# Criação da label e entry para inserir o texto
label_text = tk.Label(frame, text="Digite o texto para gerar o QR Code:")
label_text.pack()

entry_text = tk.Entry(frame, textvariable=text)
entry_text.pack()

# Criação do botão para gerar o QR Code
button_generate = tk.Button(frame, text="Gerar QR Code", command=generate_qr_code)
button_generate.pack()

# Criação da label para exibir o QR Code gerado
label_image = tk.Label(frame)
label_image.pack()

# Início do loop principal da aplicação
app.mainloop()