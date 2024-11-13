import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Função para carregar todas as imagens de um diretório sem ordenação adicional
def load_images_from_directory(directory):
    images = []
    for filename in sorted(os.listdir(directory), key=lambda x: os.path.getctime(os.path.join(directory, x))):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):  # Formatos de imagem suportados
            img_path = os.path.join(directory, filename)
            images.append(img_path)
    return images  # Retorna apenas os caminhos das imagens

# Função para exibir o slide atual
def show_slide(index):
    global current_slide, slide_images, current_image

    current_slide = index % len(slide_images)
    img_path = slide_images[current_slide]

    if img_path.lower().endswith('.gif'):
        current_image = Image.open(img_path)
        update_gif()  # Inicia a animação do GIF
    else:
        current_image = Image.open(img_path)
        img = current_image.resize((root.winfo_width(), root.winfo_height()), Image.LANCZOS)  # Redimensiona para tela cheia
        img_tk = ImageTk.PhotoImage(img)
        slide_label.config(image=img_tk)
        slide_label.image = img_tk  # Manter referência para evitar garbage collection

# Função para atualizar a animação do GIF
def update_gif():
    global current_image
    img = current_image.copy()  # Faz uma cópia da imagem atual

    # Redimensiona o GIF para tela cheia
    img = img.resize((root.winfo_width(), root.winfo_height()), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    slide_label.config(image=img_tk)
    slide_label.image = img_tk  # Manter referência para evitar garbage collection

    try:
        current_image.seek(current_image.tell() + 1)  # Avança para o próximo frame do GIF
    except EOFError:
        current_image.seek(0)  # Volta ao primeiro frame se chegar ao final

    # Atualiza o GIF a cada 100 ms# Retorna apenas os caminhos das imagens

    root.after(100, update_gif)

# Funções para avançar e retroceder slides
def next_slide(event=None):
    show_slide(current_slide + 1)

def previous_slide(event=None):
    show_slide(current_slide - 1)

# Função para encerrar a apresentação
def exit_presentation(event=None):
    root.quit()

# Configuração da janela principal com tela cheia
root = tk.Tk()
root.title("Apresentação de Imagens")
root.attributes('-fullscreen', True)  # Modo tela cheia
root.bind('<Escape>', exit_presentation)  # Tecla Esc para sair do modo tela cheia

# Seleciona o diretório contendo as imagens
directory_path = filedialog.askdirectory(title="Selecione o diretório com imagens")

# Verifique se o diretório existe
if not directory_path:
    print("Nenhum diretório selecionado.")
else:
    # Carregar os caminhos das imagens do diretório especificado na ordem de criação
    slide_images = load_images_from_directory(directory_path)

    # Configuração da interface de exibição do slide
    slide_label = tk.Label(root)
    slide_label.pack(fill=tk.BOTH, expand=True)  # Preenche a tela

    # Botões de navegação
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=10)

    prev_button = tk.Button(button_frame, text="Anterior", command=previous_slide)
    prev_button.pack(side=tk.LEFT, padx=5)

    next_button = tk.Button(button_frame, text="Próximo", command=next_slide)
    next_button.pack(side=tk.RIGHT, padx=5)

    # Controles de navegação com as teclas
    root.bind('<Right>', next_slide)  # Avança ao pressionar a tecla 'Direita'
    root.bind('<Left>', previous_slide)  # Retrocede ao pressionar a tecla 'Esquerda'

    # Verifica se há imagens para apresentar
    if slide_images:
        # Inicia a apresentação com o primeiro slide
        current_slide = 0
        show_slide(current_slide)

        # Inicia o loop principal do Tkinter
        root.mainloop()
    else:
        print("Nenhuma imagem encontrada no diretório selecionado.")
