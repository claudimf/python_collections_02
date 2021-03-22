# Python Collections parte 2: Conjuntos e dicionários

👋 Olá, Seja Bem-vindo(a) ao 'Python Collections parte 2: Conjuntos e dicionários'.

# Projeto ['Python Collections parte 2: Conjuntos e dicionários'](https://cursos.alura.com.br/course/python-collections-conjuntos-e-dicionarios):

### Aulas

<details>
    <summary>Conjuntos</summary>
    <ul>
        <li>Introdução</li>
        <li>Trabalhando com conjuntos, os sets</li>
        <li>Mais operações de conjuntos</li>
        <li>Verificando dados</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Operações</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Outro tipo de conjunto e conjuntos de outros tipos</li>
        <li>Lidando com conjunto</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Dicionários</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Dicionários</li>
        <li>Mais operações de dicionários</li>
        <li>Filtrando valores</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Variações de dicionários</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Default dict</li>
        <li>Counter</li>
        <li>Contando valores</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Praticando</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Colocando tudo em prática</li>
        <li>Conclusão</li>
        <li>Faça como eu fiz na aula</li>
        <li>Única escolha sobre o conteúdo da aula</li>
        <li>Projeto final</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python aulas/01.py
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Data Structures](https://docs.python.org/3/tutorial/datastructures.html)