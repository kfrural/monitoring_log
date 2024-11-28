# Setup Guide

Este guia irá ajudá-lo a configurar e executar o projeto em sua máquina local. Ele cobre a instalação das dependências, configuração dos serviços necessários e como executar os componentes do sistema.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- **Docker** (para rodar containers de banco de dados e serviços)
- **Docker Compose** (para orquestrar os containers)
- **Python 3.7 ou superior**
- **Java 8 ou superior** (caso utilize componentes Java)
- **Git** (para clonar o repositório)
- **Kafka** (se o projeto envolver streaming de dados)

Se você não tem o Docker instalado, siga as instruções [aqui](https://docs.docker.com/get-docker/).

Se você precisar do Docker Compose, siga as instruções [aqui](https://docs.docker.com/compose/install/).

---

## 1. Clonando o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

---

## 2. Instalando Dependências

### Para a parte Python do projeto:
Certifique-se de estar no diretório raiz do repositório, e crie um ambiente virtual para Python:

```bash
python3 -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```

Instale as dependências do Python:

```bash
pip install -r requirements.txt
```

### Para a parte Java do projeto:
Se o seu projeto envolve Java, verifique se o `Maven` está instalado. Caso não tenha, instale seguindo as instruções [aqui](https://maven.apache.org/install.html).

No diretório raiz do projeto, você pode instalar as dependências Java com:

```bash
mvn clean install
```

---

## 3. Configurando os Serviços

### 3.1 Configuração de Docker e Docker Compose

Este projeto utiliza o Docker para rodar alguns serviços, como o Elasticsearch, InfluxDB, Kafka, e Grafana. Para configurá-los, execute os seguintes comandos:

```bash
docker-compose up -d
```

Isso irá iniciar os containers para os seguintes serviços:

- **Elasticsearch**: para armazenamento e pesquisa de dados.
- **Kafka**: para streaming de dados em tempo real.
- **InfluxDB**: para armazenamento de métricas temporais.
- **Grafana**: para visualização dos dados.

### 3.2 Configuração do Telegraf

Se você estiver utilizando o **Telegraf** para coleta de métricas, configure o arquivo `telegraf.conf` com os detalhes do seu ambiente e coloque-o no diretório correto:

```bash
cp telegraf.conf /etc/telegraf/telegraf.conf
```

Em seguida, inicie o serviço do Telegraf:

```bash
docker-compose up -d telegraf
```

---

## 4. Configuração de Variáveis de Ambiente

Algumas variáveis de ambiente podem ser necessárias para rodar o projeto corretamente. Você pode configurar um arquivo `.env` na raiz do projeto para definir essas variáveis:

Exemplo de `.env`:

```env
DATABASE_URL=jdbc:postgresql://localhost:5432/seu-banco
KAFKA_BOOTSTRAP_SERVER=localhost:9092
INFLUXDB_URL=http://localhost:8086
```

---

## 5. Executando o Sistema

### 5.1 Executando o Kafka Spark Streaming

Se o seu projeto envolve Spark Streaming, você pode rodar o arquivo Python `kafka_spark_stream.py` para consumir dados do Kafka:

```bash
python kafka_spark_stream.py
```

### 5.2 Executando o Processamento de Anomalias

Caso o sistema envolva detecção de anomalias, rode o script `detection.py`:

```bash
python detection.py
```

### 5.3 Rodando o Sistema de Visualização

- **Grafana**: Acesse o Grafana em [http://localhost:3000](http://localhost:3000) e configure o datasource apontando para o InfluxDB ou Elasticsearch, conforme configurado.
  
- **Kibana**: Acesse o Kibana em [http://localhost:5601](http://localhost:5601) para visualizar logs armazenados no Elasticsearch.

---

## 6. Testes

### 6.1 Rodando os Testes de Unidade

Para rodar os testes de unidade Python, use:

```bash
pytest
```

Se estiver utilizando Java, rode os testes com Maven:

```bash
mvn test
```

---

## 7. Parando os Serviços

Para parar os containers do Docker, basta rodar:

```bash
docker-compose down
```

---

## 8. Problemas Conhecidos

Se você enfrentar algum problema ao configurar ou executar o projeto, verifique as seguintes soluções:

- **Erro ao iniciar os containers do Docker**: Certifique-se de que você tem permissões adequadas para rodar o Docker e que os serviços necessários estão configurados corretamente.
- **Kafka não consegue consumir dados**: Verifique se o Kafka está corretamente configurado e se o tópico está criado.
- **Grafana não está exibindo dados**: Certifique-se de que o InfluxDB ou Elasticsearch estão com dados corretamente sendo armazenados.

---

## 9. Contribuindo

Se você deseja contribuir para o projeto, faça um fork deste repositório e envie um Pull Request com suas alterações. Certifique-se de rodar os testes antes de enviar.

---

Esse guia cobre os passos principais, mas caso precise de mais informações, consulte a documentação de cada serviço (Kafka, Spark, Elasticsearch, etc.). Se encontrar algum erro ou tiver dúvidas, entre em contato com os mantenedores do projeto ou abra uma issue.

---