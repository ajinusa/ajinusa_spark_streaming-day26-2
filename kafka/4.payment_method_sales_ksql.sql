CREATE TABLE payment_method_sales_ksql AS
SELECT
    payment_method,
    SUM(total_price) AS total_price
FROM apotek_dibimbing_ajinusa_stream
GROUP BY payment_method
EMIT CHANGES;