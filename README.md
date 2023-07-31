# ProFiler

<summary><strong>🧑‍💻 O que foi desenvolvido</strong></summary>

Aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.

Para executar a aplicação:

1. Siga os passos do tópico [**🏕️ Ambiente Virtual**]
2. Configure o auto-complete da aplicação com o comando `pro-filer --install-completion` e reinicie o terminal;
3. Execute o comando `pro-filer` seguido de um caminho (diretório ou arquivo) e uma ação. Por exemplo:

```bash
pro-filer . preview
```

![pro-filer preview](./images/pro-filer-preview.gif)

A aplicação já estava funcional, mas possuia dois problemas:

1. alguns bugs precisavam ser corrigidos;
2. mais testes precisavam ser implementados.

Foram corrigidos os bugs e implementados os testes para garantir que a aplicação funcionasse corretamente. Foi aplicado tudo o que aprendi sobre debugging e testes automatizados em Python!

</details>
  
<details>
  <summary><strong>:memo: Habilidades a serem trabalhadas </strong></summary>

Neste projeto, exercitei as habilidades de:

- Encontrar bugs no código de uma aplicação escrita em Python;
- Corrigir bugs no código de uma aplicação escrita em Python;
- Criar testes para uma aplicação escrita em Python;
- Utilizar o `pytest` para criar testes automatizados em uma aplicação escrita em Python.

<!-- 🤔 [HS] Escrevam as habilidade utilizando a Taxonomia de Bloom. -->

</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` instalará todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Se você desejar instalar uma nova dependência, basta adicioná-la no arquivo `dev-requirements.txt` e executar o comando `python3 -m pip install -r dev-requirements.txt` novamente.

  Se o VS Code não reconhecer as dependências instaladas no ambiente virtual criado, será necessário informar o caminho do interpretador Python. Para isso, abra o VS Code e pressione `Ctrl + Shift + P` (no Mac, `Cmd + Shift + P`) e digite `Python: Select Interpreter`. Selecione o interpretador que possui o caminho `./.venv/bin/python` no nome.
</details>
