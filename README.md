# Projeto-Integrador-II-2024

### README.md

# Sistema de Gestão Psicopedagógica

Este repositório contém o código-fonte de um **Sistema de Gestão Psicopedagógica** desenvolvido para auxiliar profissionais na administração eficiente de seus atendimentos. O sistema oferece funcionalidades para o gerenciamento de pacientes, agendamentos, finanças, e mais, através de uma interface web simples e moderna.

## Funcionalidades

- **Cadastro de Pacientes**: Registre, edite e exclua informações detalhadas dos pacientes, como nome, data de nascimento e contato.
- **Gestão de Responsáveis e Escolas**: Adicione e gerencie responsáveis e instituições educacionais associadas aos pacientes.
- **Agendamento de Atendimentos**: Marque e acompanhe consultas psicopedagógicas com opções para editar e apagar agendamentos.
- **Controle Financeiro**: Registre receitas e despesas, edite e exclua registros financeiros.
- **Visualização de Dados**: Exiba todos os registros em tabelas organizadas com ações para edição e exclusão.
- **Estilização Responsiva**: Interface moderna com cores suaves, adaptável a diferentes tamanhos de tela.
- **Rodapé Informativo**: Inclui detalhes do projeto, destacando "Projeto Integrador 2 - Univesp - 2º semestre de 2024".

## Tecnologias Utilizadas

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Banco de Dados**: SQLite
- **Hospedagem Local**: Flask Development Server

## Estrutura do Projeto


psicopedagogia/
│
├── static/
│   ├── css/
│   │   └── styles.css  # Estilos do frontend
│   └── img/            # Imagens utilizadas no projeto
│
├── templates/
│   ├── base.html               # Template base
│   ├── index.html              # Página inicial
│   ├── dados_registrados.html  # Página para exibir pacientes
│   ├── dados_agendamentos.html # Página para exibir agendamentos
│   ├── dados_financeiros.html  # Página para exibir dados financeiros
│   ├── editar_paciente.html    # Formulário para editar paciente
│   ├── editar_agendamento.html # Formulário para editar agendamento
│   └── editar_financeiro.html  # Formulário para editar financeiro
│
├── app.py    # Código principal do aplicativo Flask
└── psicopedagogia.db # Banco de dados SQLite



## Como Executar o Projeto

### Pré-requisitos

- **Python 3.8+**
- **Virtualenv** (opcional, mas recomendado)

### Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/SeuUsuario/psicopedagogia.git
   cd psicopedagogia
   ```

2. Crie e ative um ambiente virtual (opcional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install Flask
   ```

4. Inicie o servidor Flask:
   ```bash
   python app.py
   ```

5. Acesse o sistema no navegador:
   ```
   http://127.0.0.1:5000
   ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e novas funcionalidades.

## Licença

Este projeto é desenvolvido como parte de um **Projeto Integrador 2 - Univesp - 2º semestre de 2024** e está disponível sob a [Licença MIT](LICENSE).

---

Desenvolvido como parte do **Projeto Integrador 2** do curso da **Univesp**.
```


 
