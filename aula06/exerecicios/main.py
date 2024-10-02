import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil
from back import GerenciadorPessoas, converter_para_documento, converter_para_formulario
import threading

class PersonControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Pessoas")
        self.root.geometry("1200x650")  # Aumentei a largura para acomodar mais elementos

        # Configuração do tema
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")
        self.style.configure("TEntry", padding=5)
        self.style.configure("TLabel", padding=5)
        self.style.configure("Treeview", rowheight=25)
        self.style.map("TButton", background=[("active", "#ddd")])

        # Inicializa o gerenciador de pessoas
        self.gerenciador = GerenciadorPessoas()

        # Diretório para salvar as imagens de perfil
        self.perfil_dir = "perfil"
        if not os.path.exists(self.perfil_dir):
            os.makedirs(self.perfil_dir)

        self.imagem_path = None  # Armazena o caminho da imagem selecionada

        # Carregue os ícones
        self.load_icons()

        # Define Labels and Inputs
        self.create_label_and_input("ID:", 0, 0)
        self.id_entry = self.create_entry(0, 1, width=20)
        self.id_entry.config(state='readonly')  # Torna o campo ID somente leitura

        self.create_label_and_input("Nome:", 0, 2)
        self.name_entry = self.create_entry(0, 3, width=20)

        self.create_label_and_input("Idade:", 0, 4)
        self.age_entry = self.create_entry(0, 5, width=5)

        self.create_label_and_input("Cidade:", 0, 6)
        self.city_combo = ttk.Combobox(self.root, values=["Registro","Iguape","Cananeia","Pariquera","Cajati","Outra"], width=10)
        self.city_combo.grid(row=0, column=7, pady=5, padx=10)

        self.create_label_and_input("Altura:", 1, 0)
        self.height_entry = self.create_entry(1, 1, width=10)

        self.create_label_and_input("Peso:", 1, 2)
        self.weight_entry = self.create_entry(1, 3, width=10)

        # Adicionar campo de gênero
        self.create_label_and_input("Gênero:", 1, 4)
        self.gender_var = tk.StringVar(value="Masculino")
        self.gender_frame = ttk.Frame(self.root)
        self.gender_frame.grid(row=1, column=5, columnspan=2, pady=5, padx=10, sticky=tk.W)
        self.gender_male = ttk.Radiobutton(self.gender_frame, text="Masculino", variable=self.gender_var, value="Masculino", state='disabled')
        self.gender_male.pack(side=tk.LEFT)
        self.gender_female = ttk.Radiobutton(self.gender_frame, text="Feminino", variable=self.gender_var, value="Feminino", state='disabled')
        self.gender_female.pack(side=tk.LEFT)

        # Adicionar checkbox para habilitar/desabilitar o campo de gênero
        self.gender_enabled = tk.BooleanVar(value=False)
        self.gender_checkbox = ttk.Checkbutton(self.gender_frame, text="Editar", variable=self.gender_enabled, command=self.toggle_gender_field)
        self.gender_checkbox.pack(side=tk.LEFT)

        self.create_label_and_input("Data Nascimento:", 2, 0)
        self.birth_entry = self.create_entry(2, 1, width=12)

        self.create_label_and_input("Data Cadastro:", 2, 2)
        self.registration_entry = self.create_entry(2, 3, width=12)

        self.create_label_and_input("Data Atualização:", 2, 4)
        self.update_entry = self.create_entry(2, 5, width=12)

        # Description Field
        self.create_label_and_input("Descrição:", 3, 0)
        self.desc_entry = self.create_entry(3, 1, width=40, colspan=4)

        # Botão para selecionar imagem
        self.select_image_button = ttk.Button(self.root, text="Selecionar Imagem", command=self.select_image)
        self.select_image_button.grid(row=3, column=5, pady=5, padx=10)

        # Create Buttons
        self.create_buttons()

        # Criar tabela
        self.create_table()

        # Adiciona um evento de seleção na tabela
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        # Campo de busca
        self.create_search_field()

        # Carrega os dados inicialmente
        self.consult_data()

        # Carregar imagens
        self.load_images()

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
        """Cria os botões da interface"""
        button_frame = ttk.Frame(self.root)
        button_frame.grid(row=4, column=0, columnspan=8, pady=10)

        ttk.Button(
            button_frame, 
            text="Adicionar", 
            image=self.add_icon, 
            compound=tk.LEFT, 
            command=self.save_data
        ).grid(row=0, column=0, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Buscar", 
            image=self.consultar_icon,  # Corrigido para usar o ícone de consulta
            compound=tk.LEFT, 
            command=self.search_data
        ).grid(row=0, column=1, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Atualizar", 
            image=self.update_icon, 
            compound=tk.LEFT, 
            command=self.update_data
        ).grid(row=0, column=2, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Excluir", 
            image=self.delete_icon, 
            compound=tk.LEFT, 
            command=self.delete_data
        ).grid(row=0, column=3, padx=5)
        
        ttk.Button(
            button_frame, 
            text="Limpar", 
            image=self.clear_icon, 
            compound=tk.LEFT, 
            command=self.clear_form
        ).grid(row=0, column=4, padx=5)

        # Exit button
        exit_button = ttk.Button(self.root, text="Sair", command=self.root.quit)
        exit_button.grid(row=6, column=7, pady=10, padx=10, sticky=tk.E)

    def create_table(self):
        """Cria a tabela para exibir os clientes"""
        columns = ('ID', 'Nome', 'Idade', 'Cidade', 'Gênero')  # Adicionado 'Gênero'
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings')

        # Define cabeçalhos para as colunas
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        self.tree.grid(row=7, column=0, columnspan=8, padx=10, pady=10, sticky='nsew')

        # Adiciona scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=7, column=8, sticky='ns')

        # Configura redimensionamento da tabela
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(7, weight=1)

    def create_search_field(self):
        """Cria campo de busca para filtrar pessoas por nome"""
        search_frame = ttk.Frame(self.root)
        search_frame.grid(row=5, column=0, columnspan=8, pady=10)

        search_label = ttk.Label(search_frame, text="Buscar por Nome:")
        search_label.grid(row=0, column=0, padx=5)

        self.search_entry = ttk.Entry(search_frame, width=20)
        self.search_entry.grid(row=0, column=1, padx=5)

        search_button = ttk.Button(search_frame, text="Buscar", command=self.search_data_thread)
        search_button.grid(row=0, column=2, padx=5)

        reset_button = ttk.Button(search_frame, text="Resetar Busca", command=self.consult_data_thread)
        reset_button.grid(row=0, column=3, padx=5)

    def save_data_thread(self):
        """Inicia a thread para salvar dados"""
        threading.Thread(target=self.save_data).start()

    def delete_data_thread(self):
        """Inicia a thread para deletar dados"""
        threading.Thread(target=self.delete_data).start()

    def update_data_thread(self):
        """Inicia a thread para atualizar dados"""
        threading.Thread(target=self.update_data).start()

    def consult_data_thread(self):
        """Inicia a thread para consultar dados"""
        threading.Thread(target=self.consult_data).start()

    def search_data_thread(self):
        """Inicia a thread para buscar dados"""
        threading.Thread(target=self.search_data).start()

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
        dados = {
            'nome': self.name_entry.get(),
            'idade': self.age_entry.get(),
            'altura': self.height_entry.get(),
            'peso': self.weight_entry.get(),
            'cidade': self.city_combo.get(),
            'data_nascimento': self.birth_entry.get(),
            'descricao': self.desc_entry.get(),
            'imagem_path': self.imagem_path
        }
        if self.gender_enabled.get():
            dados['genero'] = self.gender_var.get()
        return dados

    def save_data(self):
        """Salva os dados no banco de dados"""
        self.toggle_buttons_state('disabled')
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
            self.consult_data()
        except ValueError as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {str(e)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado ao salvar dados: {str(e)}")
        finally:
            self.toggle_buttons_state('normal')

    def delete_data(self):
        """Exclui os dados do banco de dados"""
        self.toggle_buttons_state('disabled')
        pessoa_id = self.id_entry.get()
        if not pessoa_id:
            messagebox.showerror("Erro", "Por favor, selecione um registro para excluir.")
            self.toggle_buttons_state('normal')
            return
        try:
            if self.gerenciador.excluir_pessoa(pessoa_id):
                # Remove a imagem associada
                imagem_path = os.path.join(self.perfil_dir, f"{pessoa_id}.png")  # Assumindo extensão .png
                if os.path.exists(imagem_path):
                    os.remove(imagem_path)

                messagebox.showinfo("Excluir", "Dados excluídos com sucesso!")
                self.clear_form()
                self.consult_data()
            else:
                messagebox.showinfo("Excluir", "Nenhum registro encontrado para excluir.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir dados: {e}")
        finally:
            self.toggle_buttons_state('normal')

    def update_data(self):
        """Atualiza os dados no banco de dados"""
        self.toggle_buttons_state('disabled')
        pessoa_id = self.id_entry.get()
        if not pessoa_id:
            messagebox.showerror("Erro", "Por favor, selecione um registro para atualizar.")
            self.toggle_buttons_state('normal')
            return
        dados = self.get_form_data()
        documento = converter_para_documento(dados)
        try:
            if self.gerenciador.atualizar_pessoa(pessoa_id, documento):
                # Atualiza a imagem se houver nova
                if self.imagem_path:
                    ext = os.path.splitext(self.imagem_path)[1]
                    new_image_path = os.path.join(self.perfil_dir, f"{pessoa_id}{ext}")
                    if os.path.exists(new_image_path):
                        os.remove(new_image_path)  # Remove a imagem antiga
                    shutil.copy(self.imagem_path, new_image_path)
                    self.gerenciador.atualizar_imagem_pessoa(pessoa_id, new_image_path)

                messagebox.showinfo("Alterar", "Dados atualizados com sucesso!")
                self.consult_data()
            else:
                messagebox.showinfo("Alterar", "Nenhum registro encontrado para atualizar.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar dados: {e}")
        finally:
            self.toggle_buttons_state('normal')

    def consult_data(self):
        """Consulta os dados no banco de dados e exibe na tabela"""
        self.toggle_buttons_state('disabled')
        try:
            pessoas = self.gerenciador.listar_pessoas()
            self.tree.delete(*self.tree.get_children())  # Limpa a tabela
            for pessoa in pessoas:
                self.tree.insert('', 'end', values=(
                    pessoa['_id'],
                    pessoa['nome'],
                    pessoa['idade'] if pessoa['idade'] is not None else '',
                    pessoa['cidade'],
                    pessoa['genero']  # Adicionado gênero
                ))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar dados: {str(e)}")
        finally:
            self.toggle_buttons_state('normal')

    def search_data(self):
        """Busca os dados no banco de dados pelo nome e exibe na tabela"""
        self.toggle_buttons_state('disabled')
        nome_busca = self.search_entry.get().strip()
        try:
            pessoas = self.gerenciador.buscar_pessoas_por_nome(nome_busca)
            self.tree.delete(*self.tree.get_children())  # Limpa a tabela
            for pessoa in pessoas:
                self.tree.insert('', 'end', values=(
                    pessoa['_id'],
                    pessoa['nome'],
                    pessoa['idade'] if pessoa['idade'] is not None else '',
                    pessoa['cidade'],
                    pessoa['genero']  # Adicionado gênero
                ))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar dados: {str(e)}")
        finally:
            self.toggle_buttons_state('normal')

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
        self.search_entry.delete(0, tk.END)

        # Limpa a imagem
        if hasattr(self, 'image_label'):
            self.image_label.configure(image='')
        self.imagem_path = None

        self.gender_var.set('Masculino')
        self.gender_enabled.set(False)
        self.toggle_gender_field()

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
        self.gender_var.set(dados.get('genero', 'Masculino'))
        self.gender_enabled.set(False)
        self.toggle_gender_field()

        # Carrega a imagem se existir
        if 'imagem_path' in dados and dados['imagem_path']:
            self.imagem_path = dados['imagem_path']
            self.load_image(dados['imagem_path'], 0, 7, 5)  # Mudei a coluna para 7
        else:
            # Limpa a imagem se não houver
            if hasattr(self, 'image_label'):
                self.image_label.configure(image='')
            self.imagem_path = None

    def toggle_buttons_state(self, state):
        """Habilita ou desabilita os botões para evitar múltiplas ações simultâneas"""
        for child in self.root.winfo_children():
            if isinstance(child, ttk.Button):
                child.config(state=state)

    def toggle_gender_field(self):
        """Habilita ou desabilita o campo de gênero"""
        state = 'normal' if self.gender_enabled.get() else 'disabled'
        self.gender_male.config(state=state)
        self.gender_female.config(state=state)

    def load_icons(self):
        """Carrega os ícones para os botões"""
        icon_size = (20, 20)
        icons_dir = os.path.join(os.path.dirname(__file__), 'icones')

        self.add_icon = self.load_and_resize_image(os.path.join(icons_dir, 'acesso.png'), icon_size)
        self.search_icon = self.load_and_resize_image(os.path.join(icons_dir, 'logo_usuarios.png'), icon_size)
        self.update_icon = self.load_and_resize_image(os.path.join(icons_dir, 'alterar.png'), icon_size)
        self.delete_icon = self.load_and_resize_image(os.path.join(icons_dir, 'excluir.png'), icon_size)
        self.clear_icon = self.load_and_resize_image(os.path.join(icons_dir, 'limpar.png'), icon_size)
        self.consultar_icon = self.load_and_resize_image(os.path.join(icons_dir, 'consultar.png'), icon_size)

    def load_and_resize_image(self, path, size):
        """Carrega e redimensiona uma imagem"""
        try:
            img = Image.open(path)
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Erro ao carregar a imagem {path}: {e}")
            return None

    def add_data(self):
        # Implementação do método adicionar dados
        pass

    def load_images(self):
        # Implementação do método load_images
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonControlApp(root)
    root.mainloop()