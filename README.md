# Projeto Integrador 5 módulo "Python para negócios" UTFPR(Universidade Tecnológica Federal do Paraná).

## Requisitos das disciplinas ##

Descrição Geral. Neste projeto integrador deve-se criar um MVP em curto espaço de tempo. Seu MVP deve estar relacionado com pelo menos uma das disciplinas técnicas do Módulo 5.

### Disciplinas utilizadas:
- Computação Gráfica e Visão Computacional com Python
- Processamento de Dados Espaciais com Python

### Material para Entregar

Arquivo compactado. Deve-se preparar o arquivo compactado contendo todos os arquivos mencionados em cada requisito descrito anteriormente. Somente um membro do grupo faz a entrega deste arquivo compactado, entretanto, todos os membros do grupo devem entregar o vídeo de explicação (de 3 a 5 minutos, e mostrando um documento oficial para fins de identificação).

## Como utilizar? ##

**:warning: Warning:** É necessário ter o Docker instalado:
- 🐳 [Docker Engine Installation](https://docs.docker.com/engine/install/ubuntu/)  
- 🐳 [Docker Compose Installation](https://docs.docker.com/compose/install/)  
- **💡 Tip:** [For any doubts please use Docker documentation](https://docs.docker.com/)  

### Utilizando a aplicação

Após instalar o Docker e o Docker-compose, abar um terminal e execute:

```sh
docker-compose run --rm --service-ports app
```
Para acessar a aplicação, abra uma nova aba no seu terminal e execute:

```sh
docker-compose run --rm app bash
```

Para resetar a aplicação, execute:

```sh
docker-compose down && docker-compose up
```

### Mock
Gerar mock dos estados brasileiros, execute:

```sh
docker-compose run --rm app python3 utils/read_json.py
```

### Listar árvore de pacotes instalados 
Execute:

```sh
docker-compose run --rm app pipdeptree
```

### Permissões de arquivos ###
Quando se cria arquivos dentro de um contâiner Docker eles irão pertencer ao contâiner, para mudar a permissão rode o seguinte comando:

```sh
sudo chown -R $USER:$USER .
```

## Referências ##
[1° Flask + Docker](https://github.com/claudimf/flask_1)  
[2° Pytrends](https://pypi.org/project/pytrends/)  
[3° The Ultimate Guide to PyTrends: the Google Trends API (with Python code examples)](https://lazarinastoy.com/the-ultimate-guide-to-pytrends-google-trends-api-with-python/)  
