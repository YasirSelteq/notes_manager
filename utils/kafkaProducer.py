from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['172.187.144.188:9092','172.187.144.188:9093','172.187.144.188:9094'], api_version=(0, 10))
