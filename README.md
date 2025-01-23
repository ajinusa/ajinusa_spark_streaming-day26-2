# Arifin Satria Ajinusa (Day24 - Kafka)
Dalam tugas ini disimulasikan embuat 1 producer, 3 consumer. Dengan melakukan 5 partisi, 1 replikasi, 1 jam retensi data, dan max 1 GB penyimpanan data di dalam cluster Kafka.
Selain itu juga disimulasikan menggunakan fitur KSQL DB untuk mengambil message dari cluster Kafka.
Untuk detail penjelasan hasil tugas ada di dalam file "Dokumentasi - Assignment Day 24 - Kafka (Ajinusa)"



# Dibimbing, Data Engineering Bootcamp

1. Clone This Repo.
2. Run `make docker-build` for x86 user, or `make docker-build-arm` for arm chip user.

---
```
## docker-build                 - Build Docker Images (amd64) including its inter-container network.
## docker-build-arm             - Build Docker Images (arm64) including its inter-container network.
## postgres                     - Run a Postgres container
## spark                        - Run a Spark cluster, rebuild the postgres container, then create the destination tables
## jupyter                      - Spinup jupyter notebook for testing and validation purposes.
## airflow                      - Spinup airflow scheduler and webserver.
## kafka                        - Spinup kafka cluster (Kafka+Zookeeper).
## datahub                      - Spinup datahub instances.
## metabase                     - Spinup metabase instance.
## clean                        - Cleanup all running containers related to the challenge.
```

---