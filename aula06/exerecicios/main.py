import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil
from back import GerenciadorPessoas, converter_para_documento, converter_para_formulario

class PersonControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Pessoas")
        self.root.geometry("900x600")  # Aumentei a largura para acomodar a imagem

        # Inicializa o gerenciador de pessoas
        self.gerenciador = GerenciadorPessoas()

        # Diretório para salvar as imagens de perfil
        self.perfil_dir = "perfil"
        if not os.path.exists(self.perfil_dir):
            os.makedirs(self.perfil_dir)

        self.imagem_path = None  # Armazena o caminho da imagem selecionada

        # Define Labels and Inputs
        self.create_label_and_input("ID:", 0, 0)
        self.id_entry = self.create_entry(0, 1, width=20)
        self.id_entry.config(state='readonly')  # Torna o campo ID somente leitura
        
        self.create_label_and_input("Nome:", 0, 2)
        self.name_entry = self.create_entry(0, 3, width=20)
        
        self.create_label_and_input("Idade:", 0, 5)
        self.age_entry = self.create_entry(0, 6, width=5)
        
        self.create_label_and_input("Altura:", 1, 0)
        self.height_entry = self.create_entry(1, 1, width=10)
        
        self.create_label_and_input("Peso:", 1, 2)
        self.weight_entry = self.create_entry(1, 3, width=10)
        
        self.create_label_and_input("Cidade:", 1, 4)
        self.city_combo = ttk.Combobox(self.root, values=["Registro", "Outra"], width=10)
        self.city_combo.grid(row=1, column=5, pady=5, padx=10)

        self.create_label_and_input("Data Nascimento:", 2, 0)
        self.birth_entry = self.create_entry(2, 1, width=12)
        
        self.create_label_and_input("Data Cadastro:", 2, 2)
        self.registration_entry = self.create_entry(2, 3, width=12)
        
        self.create_label_and_input("Data Atualização:", 2, 4)
        self.update_entry = self.create_entry(2, 5, width=12)

        # Description Field
        self.create_label_and_input("Descrição:", 3, 0)
        self.desc_entry = self.create_entry(3, 1, width=40, colspan=4)

        # Create Buttons
        self.create_buttons()
        
        # Criar tabela
        self.create_table()
        
        # Adiciona um evento de seleção na tabela
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)
    
    def create_label_and_input(self, text, row, column):
        """Helper to create labels with default settings"""
        label = ttk.Label(self.root, text=text)
        label.grid(row=row, column=column, pady=5, padx=10, sticky=tk.E)

    def create_entry(self, row, column, width=10, colspan=1):
        """Helper to create entry widgets with default settings"""
        entry = ttk.Entry(self.root, width=width)
        entry.grid(row=row, column=column, pady=5, padx=10, sticky=tk.W, columnspan=colspan)
        return entry

    def create_buttons(self):
        """Create action buttons: Save, Delete, Update, Consult"""
        button_texts = ["Salvar", "Excluir", "Alterar", "Consultar", "Escolher Imagem"]
        button_commands = [self.save_data, self.delete_data, self.update_data, self.consult_data, self.select_image]

        for i, (text, command) in enumerate(zip(button_texts, button_commands)):
            button = ttk.Button(self.root, text=text, command=command)
            button.grid(row=5, column=i, pady=15, padx=5)
        
        # Exit button
        exit_button = ttk.Button(self.root, text="Sair", command=self.root.quit)
        exit_button.grid(row=6, column=4, pady=10)

    def create_table(self):
        """Cria a tabela para exibir os clientes"""
        columns = ('ID', 'Nome', 'Idade', 'Cidade')
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')

        # Define cabeçalhos para as colunas
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.grid(row=7, column=0, columnspan=6, padx=10, pady=10, sticky='nsew')

        # Adiciona scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=7, column=6, sticky='ns')

    def select_image(self):
        """Abre o diálogo para selecionar uma imagem e exibe"""
        file_path = filedialog.askopenfilename(title="Escolher imagem", filetypes=[("Imagens", "*.png *.jpg *.jpeg")])
        if file_path:
            self.imagem_path = file_path
            self.load_image(file_path, 0, 7, 5)  # Mudei a coluna para 7

    def load_image(self, path, row, column, rowspan):
        """Carrega e exibe uma imagem"""
        try:
            img = Image.open(path)
            img = img.resize((100, 100), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            if hasattr(self, 'image_label'):
                self.image_label.configure(image=self.photo)
                self.image_label.image = self.photo
            else:
                self.image_label = ttk.Label(self.root, image=self.photo)
                self.image_label.grid(row=row, column=column, rowspan=rowspan, pady=5, padx=10)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")

    def get_form_data(self):
        """Coleta os dados do formulário"""
        return {
            'nome': self.name_entry.get(),
            'idade': self.age_entry.get(),
            'altura': self.height_entry.get(),
            'peso': self.weight_entry.get(),
            'cidade': self.city_combo.get(),
            'data_nascimento': self.birth_entry.get(),
            'descricao': self.desc_entry.get(),
            'imagem_path': self.imagem_path
        }

    def save_data(self):
        """Salva os dados no banco de dados"""
        dados = self.get_form_data()
        try:
            documento = converter_para_documento(dados)
            pessoa_id = self.gerenciador.inserir_pessoa(documento)
            
            # Salva a imagem no diretório de perfil
            if self.imagem_path:
                ext = os.path.splitext(self.imagem_path)[1]
                new_image_path = os.path.join(self.perfil_dir, f"{pessoa_id}{ext}")
                shutil.copy(self.imagem_path, new_image_path)
                self.gerenciador.atualizar_imagem_pessoa(pessoa_id, new_image_path)

            self.id_entry.config(state='normal')
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, pessoa_id)
            self.id_entry.config(state='readonly')
            messagebox.showinfo("Salvar", f"Dados salvos com sucesso! ID: {pessoa_id}")
            self.consult_data()  # Atualiza a tabela após salvar
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado ao salvar dados: {str(e)}")
        
    def delete_data(self):
        """Exclui os dados do banco de dados"""
        pessoa_id = self.id_entry.get()
        if not pessoa_id:
            messagebox.showerror("Erro", "Por favor, selecione um registro para excluir.")
            return
        try:
            if self.gerenciador.excluir_pessoa(pessoa_id):
                messagebox.showinfo("Excluir", "Dados excluídos com sucesso!")
                self.clear_form()
                self.consult_data()  # Atualiza a tabela após excluir
            else:
                messagebox.showinfo("Excluir", "Nenhum registro encontrado para excluir.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir dados: {e}")
        
    def update_data(self):
        """Atualiza os dados no banco de dados"""
        pessoa_id = self.id_entry.get()
        if not pessoa_id:
            messagebox.showerror("Erro", "Por favor, selecione um registro para atualizar.")
            return
        dados = self.get_form_data()
        documento = converter_para_documento(dados)
        try:
            if self.gerenciador.atualizar_pessoa(pessoa_id, documento):
                messagebox.showinfo("Alterar", "Dados atualizados com sucesso!")
                self.consult_data()  # Atualiza a tabela após atualizar
            else:
                messagebox.showinfo("Alterar", "Nenhum registro encontrado para atualizar.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar dados: {e}")
        
    def consult_data(self):
        """Consulta os dados no banco de dados e exibe na tabela"""
        try:
            pessoas = self.gerenciador.listar_pessoas()
            self.tree.delete(*self.tree.get_children())  # Limpa a tabela
            for pessoa in pessoas:
                self.tree.insert('', 'end', values=(
                    pessoa['_id'],
                    pessoa['nome'],
                    pessoa['idade'] if pessoa['idade'] is not None else '',
                    pessoa['cidade']
                ))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar dados: {str(e)}")

    def on_tree_select(self, event):
        """Preenche o formulário quando um item é selecionado na tabela"""
        selected_item = self.tree.selection()
        if selected_item:
            pessoa_id = self.tree.item(selected_item)['values'][0]
            pessoa = self.gerenciador.consultar_pessoa(pessoa_id)
            if pessoa:
                self.preencher_formulario(converter_para_formulario(pessoa))

    def clear_form(self):
        """Limpa todos os campos do formulário"""
        self.id_entry.config(state='normal')
        self.id_entry.delete(0, tk.END)
        self.id_entry.config(state='readonly')
        for entry in [self.name_entry, self.age_entry, self.height_entry,
                      self.weight_entry, self.birth_entry, self.registration_entry,
                      self.update_entry, self.desc_entry]:
            entry.delete(0, tk.END)
        self.city_combo.set('')

        # Limpa a imagem
        if hasattr(self, 'image_label'):
            self.image_label.configure(image='')
        self.imagem_path = None

    def preencher_formulario(self, dados):
        """Preenche o formulário com os dados consultados"""
        self.id_entry.config(state='normal')
        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, dados['_id'])
        self.id_entry.config(state='readonly')
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, dados['nome'])
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, dados['idade'])
        self.height_entry.delete(0, tk.END)
        self.height_entry.insert(0, dados['altura'])
        self.weight_entry.delete(0, tk.END)
        self.weight_entry.insert(0, dados['peso'])
        self.city_combo.set(dados['cidade'])
        self.birth_entry.delete(0, tk.END)
        self.birth_entry.insert(0, dados['data_nascimento'])
        self.registration_entry.delete(0, tk.END)
        self.registration_entry.insert(0, dados['data_cadastro'])
        self.update_entry.delete(0, tk.END)
        self.update_entry.insert(0, dados['data_atualizacao'])
        self.desc_entry.delete(0, tk.END)
        self.desc_entry.insert(0, dados['descricao'])

        # Carrega a imagem se existir
        if 'imagem_path' in dados and dados['imagem_path']:
            self.imagem_path = dados['imagem_path']
            self.load_image(dados['imagem_path'], 0, 7, 5)  # Mudei a coluna para 7
        else:
            # Limpa a imagem se não houver
            if hasattr(self, 'image_label'):
                self.image_label.configure(image='')
            self.imagem_path = None

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonControlApp(root)
    root.mainloop()