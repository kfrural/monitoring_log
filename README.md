# **Real-Time Infrastructure Monitoring System with Kafka, Spark Streaming, and Elasticsearch**

This repository provides a **template** for a real-time infrastructure monitoring system. The system uses **Apache Kafka** for data ingestion, **Apache Spark Streaming** for real-time processing, and **Elasticsearch** for storing logs and metrics. Additionally, the system sends real-time alerts to **Slack**, **email**, or **PagerDuty** when anomalies are detected.

### **System Overview**

This template can be used as a base to build an infrastructure monitoring system for servers or any other infrastructure. It is modular, with different components for data ingestion, processing, storage, and visualization. The system monitors metrics such as **CPU usage**, **memory usage**, and **error logs**.

### **Technologies Used**
- **Apache Kafka**: For real-time data ingestion.
- **Apache Spark Streaming**: For real-time data processing and analysis.
- **Elasticsearch**: For storing logs and performing searches.
- **Grafana** and **Kibana**: For data visualization.
- **Slack**, **Email**, **PagerDuty**: For sending alerts.
- **InfluxDB**: For storing time-series metrics.

---

### **Prerequisites**

Before running the system, you need to set up a few tools and services:

1. **Apache Kafka**: For data ingestion.
   - Download and follow installation instructions [here](https://kafka.apache.org/downloads).
   
2. **Apache Spark**: For real-time processing.
   - Download and follow installation instructions [here](https://spark.apache.org/downloads.html).
   
3. **Elasticsearch**: For storing logs.
   - Download and follow installation instructions [here](https://www.elastic.co/downloads/elasticsearch).

4. **Grafana** and **Kibana**: For data visualization.
   - Download and follow installation instructions [here](https://grafana.com/get) and [here](https://www.elastic.co/downloads/kibana).

5. **Telegraf** or **Logstash**: For collecting metrics and logs.
   - Download and follow installation instructions for [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) or [Logstash](https://www.elastic.co/downloads/logstash).

---

### **Configuration and Customization Required**

After cloning the repository, there are several configurations you need to adjust to tailor the system to your environment:

#### **1. Kafka - Topic Configuration**
The system uses Kafka for data ingestion, but you'll need to ensure that the correct topics exist in your Kafka cluster. To do this:

- Open the Kafka console and create the necessary topics:
  ```bash
  kafka-topics.sh --create --topic cpu-usage --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  kafka-topics.sh --create --topic memory-usage --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  kafka-topics.sh --create --topic server-logs --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
  ```

#### **2. Spark - Streaming Configuration**
In the `streaming/spark-streaming/spark_streaming.py` file, you’ll find the Spark configuration to consume data from Kafka. Make sure the Kafka server address and topics are correct:

```python
kafka_stream = KafkaUtils.createStream(ssc, "localhost:2181", "spark-streaming", {
    "cpu-usage": 1, 
    "memory-usage": 1,
    "server-logs": 1
})
```

Adjust the **Zookeeper** address (`localhost:2181`) and the **Kafka topics** as needed.

#### **3. Elasticsearch - Index Creation**
Before collecting logs into Elasticsearch, you need to make sure the appropriate indexes are created. This is done by the script `storage/elasticsearch/init_es.py`.

Make sure the `index_creation.json` file is configured correctly (as mentioned earlier) and execute the script to create the indexes:

```bash
python storage/elasticsearch/init_es.py
```

#### **4. Alerts - Configuring Slack, Email, and PagerDuty**
The system sends alerts when anomalies are detected. You can configure these alerts in the following files:

- **Slack**: In the `alerts/slack/slack_alert.py` file, configure the Slack authentication token:
  
  ```python
  slack_token = "YOUR_SLACK_TOKEN"
  slack_channel = "#alerts"
  ```

- **Email**: In the `alerts/email/email_alert.py` file, configure the SMTP server and email credentials:
  
  ```python
  smtp_server = "smtp.yourdomain.com"
  smtp_port = 587
  smtp_user = "your_email@example.com"
  smtp_password = "your_email_password"
  ```

- **PagerDuty**: In the `alerts/pagerduty/pagerduty_alert.py` file, configure the PagerDuty API token:
  
  ```python
  pagerduty_api_key = "YOUR_API_KEY"
  pagerduty_service_id = "YOUR_SERVICE_ID"
  ```

#### **5. Grafana and Kibana Configuration**
To visualize the collected metrics and logs, you can set up **Grafana** and **Kibana**:

- **Grafana**: Create dashboards by connecting Grafana to InfluxDB and visualize metrics such as CPU usage, memory usage, etc.

- **Kibana**: Set up Kibana to visualize logs from Elasticsearch and create interactive charts.

#### **6. Telegraf or Logstash for Data Collection**
Depending on which tool you choose (Telegraf or Logstash), configure them to collect data from your servers. For example, if you're using Telegraf, configure the `telegraf.conf` file with the data sources and output destinations.

---

### **Running the System**

After configuring all the components, you can run the system as follows:

1. **Start Kafka**:
   - Start **Zookeeper**:
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     ```
   - Start **Kafka**:
     ```bash
     bin/kafka-server-start.sh config/server.properties
     ```

2. **Start Spark Streaming**:
   - Run the Spark Streaming script to consume data from Kafka and process it:
     ```bash
     spark-submit --master local[2] streaming/spark-streaming/spark_streaming.py
     ```

3. **Start Elasticsearch**:
   - Start Elasticsearch:
     ```bash
     ./bin/elasticsearch
     ```

4. **Start Telegraf or Logstash**:
   - Configure and start Telegraf or Logstash to collect data from your system.

---

### **Final Considerations**

This template serves as a starting point for a real-time infrastructure monitoring system. To use it in production, you'll need to adjust configurations according to your specific environment, such as servers, data volume, and alerting preferences. The system can be easily scaled to handle large volumes of data using Kafka, Spark, and Elasticsearch clusters.

If you need assistance or have any questions, feel free to open an issue in this repository.

---
