# Controle de Pessoas

## Descrição

O **Controle de Pessoas** é uma aplicação de desktop desenvolvida em Python que permite gerenciar informações de indivíduos de forma eficiente. Utilizando uma interface gráfica amigável criada com Tkinter, a aplicação fornece funcionalidades completas de CRUD (Criar, Ler, Atualizar, Excluir) para adicionar, consultar, atualizar e remover registros de pessoas. Os dados são armazenados em um banco de dados MongoDB, garantindo persistência e facilidade de acesso. Além disso, a aplicação suporta o upload de imagens de perfil para cada pessoa cadastrada.

## Funcionalidades

- **Adicionar Pessoa**: Insira informações detalhadas como nome, idade, altura, peso, cidade, datas de nascimento, cadastro e atualização, descrição e uma imagem de perfil.
- **Consultar Pessoa**: Busque registros específicos utilizando o ID único de cada pessoa.
- **Atualizar Pessoa**: Modifique informações existentes de qualquer registro.
- **Excluir Pessoa**: Remova registros conforme necessário.
- **Upload de Imagem**: Associe uma imagem de perfil a cada registro de pessoa.
- **Interface Intuitiva**: Navegue facilmente através de uma interface gráfica construída com Tkinter.
- **Listagem de Pessoas**: Visualize todos os registros em uma tabela interativa com funcionalidades de busca.

## Tecnologias Utilizadas

- **Python 3.12**: Linguagem de programação principal.
- **Tkinter**: Biblioteca para desenvolvimento da interface gráfica.
- **MongoDB**: Banco de dados NoSQL para armazenamento de informações.
- **PyMongo**: Biblioteca Python para interação com o MongoDB.
- **Pillow (PIL)**: Biblioteca para manipulação e exibição de imagens.
- **Shutil**: Módulo Python para operações de alto nível em arquivos e coleções de arquivos.

## Estrutura do Projeto

```
seu-projeto/
├── aula06/
│   ├── exercicios/
│   │   ├── __pycache__/
│   │   ├── icones/
│   │   │   ├── acesso.png
│   │   │   ├── alterar.png
│   │   │   ├── consultar.png
│   │   │   ├── excluir.png
│   │   │   ├── icone.ico
│   │   │   ├── logo_servicos.png
│   │   │   ├── logo_usuarios.png
│   │   │   ├── logout.png
│   │   │   ├── sair.png
│   │   │   └── salvar.png
│   │   ├── back.py
│   │   └── main.py
│   └── perfil/
│       └── [Imagens de Perfil]
├── .git/
├── README.md
└── requirements.txt
```

## Instalação

### Pré-requisitos

- **Python 3.12**: [Download Python](https://www.python.org/downloads/)
- **MongoDB**: [Download MongoDB Community Server](https://www.mongodb.com/try/download/community)

### Passos de Instalação

1. **Clone o Repositório**

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie e Ative um Ambiente Virtual (Opcional, mas Recomendado)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. **Instale as Dependências**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure o MongoDB**

    - Certifique-se de que o serviço do MongoDB está rodando.
    - A aplicação está configurada para conectar ao MongoDB na URI `mongodb://localhost:27017/`. Se necessário, ajuste a URI no arquivo `back.py`.

## Uso

1. **Inicie a Aplicação**

    ```bash
    python main.py
    ```

2. **Interface do Usuário**

    - **Adicionar Pessoa**: Preencha os campos com as informações da pessoa e clique em "Salvar".
    - **Consultar Pessoa**: Insira o ID da pessoa e clique em "Consultar" para visualizar os detalhes.
    - **Atualizar Pessoa**: Após consultar uma pessoa, edite as informações desejadas e clique em "Alterar".
    - **Excluir Pessoa**: Selecione uma pessoa da tabela e clique em "Excluir" para remover o registro.
    - **Escolher Imagem**: Clique em "Escolher Imagem" para adicionar ou alterar a imagem de perfil da pessoa.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. **Fork este Repositório**
2. **Crie uma Branch para sua Feature**

    ```bash
    git checkout -b feature/nova-feature
    ```

3. **Commit suas Alterações**

    ```bash
    git commit -m 'Adiciona nova funcionalidade'
    ```

4. **Push para a Branch**

    ```bash
    git push origin feature/nova-feature
    ```

5. **Abra um Pull Request**

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

- **Autor**: Marcelo Augusto
- **Email**: Marceloaugustocge@gmail.com
- **GitHub**: [Marcelo](https://github.com/marcelitos1v9)

