CREATE STREAM apotek_dibimbing_ajinusa_stream (
    transaction_id VARCHAR,
    buyer_name VARCHAR,
    medication_name VARCHAR,
    quantity INT,
    unit_price INT,
    total_price INT,
    payment_method VARCHAR,
    transaction_date VARCHAR,
    transaction_time VARCHAR
) WITH (
    KAFKA_TOPIC = 'apotek-dibimbing-ajinusa',   -- Gantilah 'your_kafka_topic' dengan topik Kafka yang sesuai
    KEY_FORMAT='KAFKA', 
    PARTITIONS=5,
    VALUE_FORMAT = 'JSON'
);

