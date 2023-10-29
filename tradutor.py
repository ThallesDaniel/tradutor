import tkinter as tk
from tkinter import filedialog
from googletrans import Translator

# Função para traduzir o texto do arquivo
def traduzir_arquivo():
    arquivo_origem = filedialog.askopenfilename(filetypes=[("Arquivos de Texto", "*.txt")])

    if arquivo_origem:
        arquivo_destino = arquivo_origem.replace('.txt', '_traduzido.txt')
        translator = Translator()
        try:
            with open(arquivo_origem, 'r', encoding='utf-8') as f_origem, open(arquivo_destino, 'w', encoding='utf-8') as f_destino:
                texto_origem = f_origem.read()
                texto_traduzido = translator.translate(texto_origem, src='auto', dest='pt').text
                f_destino.write(texto_traduzido)
            resultado.config(text=f'Arquivo traduzido e salvo em {arquivo_destino}')
        except Exception as e:
            resultado.config(text=f'Erro: {str(e)}')

# Configuração da janela principal
root = tk.Tk()
root.title("Tradutor de Texto")

# Botão para escolher um arquivo
selecionar_arquivo_btn = tk.Button(root, text="Selecionar Arquivo", command=traduzir_arquivo)
selecionar_arquivo_btn.pack()

# Label para exibir o resultado
resultado = tk.Label(root, text="", wraplength=300)
resultado.pack()

# Iniciar a interface gráfica
root.mainloop()
