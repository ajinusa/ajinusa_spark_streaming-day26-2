
CREATE TABLE apotek_dibimbing_ajinusa_ksql AS
SELECT transaction_id,
       LATEST_BY_OFFSET(buyer_name) AS buyer_name,
       LATEST_BY_OFFSET(medication_name) AS medication_name,
       LATEST_BY_OFFSET(quantity) AS quantity,
       LATEST_BY_OFFSET(unit_price) AS unit_price,
       LATEST_BY_OFFSET(total_price) AS total_price,
       LATEST_BY_OFFSET(payment_method) AS payment_method,
       LATEST_BY_OFFSET(transaction_date) AS transaction_date,
       LATEST_BY_OFFSET(transaction_time) AS transaction_time
FROM apotek_dibimbing_ajinusa_stream
GROUP BY transaction_id;
