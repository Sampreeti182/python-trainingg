### **Different Data Formats**





#### **Parquet**

Parquet is a columnar storage format that PySpark uses extensively for saving and reading DataFrames. Unlike row-based formats like CSV or JSON, Parquet stores data by columns, which is ideal for analytical workloads where you often select a subset of columns or run aggregations. Because the schema is embedded in the files, Spark can infer types and structure directly, making Parquet both efficient and convenient.

Columnar layout allows Spark to do column pruning—reading only the columns you request—and predicate pushdown, which lets Spark skip entire chunks of data that don’t match your filters. Together with built-in compression (commonly Snappy), Parquet reduces I/O and storage, which speeds up queries and lowers compute and storage costs. This is especially helpful at scale—for example, when scanning large datasets in data lakes (S3, ADLS, HDFS).

Strategy matters When you write Parquet datasets, you can partition them by logical keys like date or region. Partitioning creates subfolders (e.g., year=2025/month=12) and lets Spark prune partitions when your query filters on those keys, avoiding unnecessary reads. The key is choosing low‑ to medium‑cardinality columns you frequently filter on; over‑partitioning (too many small partitions) leads to lots of tiny files and slower performance.

Parquet supports nested structures (arrays, structs) well, and Spark can read them naturally. Over time, datasets often evolve: new columns get added or types change. The safest practice is to stabilize a target schema and align data before writing, so files remain consistent. While Spark can merge schemas at read time, doing so can be expensive; it’s better to manage schema evolution deliberately to avoid surprises and slow scans.



###### **Why Parquet is used?**

Parquet is widely used in PySpark (and big data systems in general) because it solves several key challenges in data storage and processing:



1\. **Columnar Storage for Analytics**

Parquet stores data in a column-oriented format rather than row-oriented. This is ideal for analytical queries where you often need only a few columns from a large dataset. Spark can read just the required columns instead of scanning entire rows, which significantly reduces I/O and speeds up queries.

2\. **Efficient Compression and Encoding**

Columnar storage allows better compression because values in the same column tend to be similar. Parquet uses efficient encoding techniques and supports compression algorithms like Snappy, Gzip, and Zstd. This reduces storage costs and improves read performance.

3\. **Schema Awareness and Self-Describing Files**

Parquet files embed the schema with the data, so Spark can infer the structure automatically without needing external metadata. This makes it easier to manage complex data types like nested structures and arrays.

4\. **Predicate Pushdown and Column Pruning**

Parquet works well with Spark’s optimizations. Filters (predicates) can be pushed down to the file level, so Spark reads only relevant chunks of data. Similarly, column pruning ensures only necessary columns are loaded into memory, saving time and resources.

5\. **Interoperability Across Tools**

Parquet is an open standard supported by many systems—Spark, Hive, Presto, Trino, Pandas, and even cloud warehouses like Snowflake and BigQuery. This makes it perfect for data lakes where multiple tools need to access the same data efficiently.

6\. **Handles Large-Scale Data**

Parquet is designed for distributed environments like Hadoop and Spark. It can store terabytes or petabytes of data in a structured, optimized way, making it a go-to choice for big data pipelines.



###### **Some real time uses**



Data Lakes and ETL Pipelines

Organizations store raw and processed data in data lakes (like AWS S3, Azure Data Lake, or HDFS). PySpark writes data in Parquet format because:



* It’s space-efficient (compressed columnar format).
* It supports schema evolution for changing data structures.
* It’s compatible with multiple tools (Spark, Hive, Presto, Pandas).



Example: A retail company ingests daily sales data from multiple sources, transforms it in Spark, and writes it as partitioned Parquet files by year/month/day for fast querying.



2\. Big Data Analytics

Parquet is used for interactive analytics on large datasets because Spark can:



* Read only required columns (column pruning).
* Skip irrelevant partitions (partition pruning).
* This makes queries on billions of rows feasible in seconds.



Example: A telecom company analyzing call records for fraud detection uses Parquet to store billions of rows efficiently and run Spark SQL queries quickly.



3\. Machine Learning Pipelines

ML workflows often require feature engineering on large datasets. Parquet helps because:



* It handles nested structures (arrays, structs) well.
* It’s fast to read/write during iterative transformations.

Example: A recommendation system pipeline stores user-item interaction data in Parquet for training models in Spark MLlib.





4\. Streaming + Batch Integration

* In real-time streaming pipelines (using Spark Structured Streaming), data from Kafka or event hubs is processed and written to Parquet for downstream batch analytics.

Example: A fintech app streams transaction data, writes it as Parquet in S3, and later runs batch jobs for compliance and fraud analysis.



5\. Cross-Platform Interoperability

Parquet is widely supported, so data written by Spark can be read by:



* Pandas for data science.
* Presto/Trino for ad-hoc SQL queries.
* Snowflake or BigQuery for BI dashboards.

Example: A marketing team uses Spark to preprocess campaign data and stores it in Parquet so analysts can query it in BI tools without extra conversions.







#### 

#### **Orc**



ORC is another columnar storage format like Parquet, designed for high-performance analytics on large datasets. It was originally developed for the Hadoop ecosystem and is widely used with Hive. ORC stores data in a column-oriented way, enabling efficient compression and fast reads for analytical queries. It also embeds rich metadata and statistics, which Spark can leverage for query optimization.



##### **Why ORC is used**



ORC is chosen for similar reasons as Parquet:



* Columnar layout for fast analytical queries.
* High compression ratio (often better than Parquet for certain data types).
* Predicate pushdown and column pruning for efficient filtering and projection.
* Built-in indexes and statistics for each stripe (block), which help Spark skip unnecessary data during scans.
* Schema evolution support, making it suitable for changing datasets.



ORC is especially popular in Hadoop + Hive environments because it integrates deeply with Hive’s ACID transactions and optimizations.



##### **Real-Time Use Cases of ORC**



1\. Hive Tables in Data Warehouses

ORC is the default format for Hive tables in many Hadoop-based data warehouses. It’s used for storing large fact tables and dimension tables because of its compression and indexing features.

2\. ETL Pipelines in Big Data

Data engineers often convert raw data (CSV/JSON) into ORC during ETL for better performance in downstream queries. ORC files are partitioned by date or region for efficient scans.

3\. Batch Analytics on Hadoop/Spark

ORC works well for batch jobs that aggregate or join large datasets. Its internal indexes allow Spark to skip entire stripes when filters don’t match, reducing I/O.

4\. Machine Learning Feature Stores

ORC can store structured feature sets for ML pipelines, especially when integrated with Hive Metastore for schema management.

5\. Regulatory and Compliance Data

Because ORC supports ACID transactions in Hive, it’s often used for financial or compliance datasets where updates and deletes are required.





#### **Avro**

Avro is a row-based storage format designed for efficient serialization of data. Unlike Parquet and ORC, which are columnar, Avro stores data in rows, making it ideal for write-heavy or streaming scenarios where data is frequently appended. Avro is schema-based and uses a compact binary format, which makes it fast for serialization and deserialization. It’s widely used in big data pipelines, especially for data interchange between **s**ystems.



##### **Why Avro is used**



Avro is chosen for several reasons:



* **Schema evolution support**: Avro handles changes in schema gracefully, which is critical for long-running pipelines.
* **Compact binary format:** Smaller size compared to JSON or CSV, reducing storage and network transfer costs.
* **Interoperability:** Works well with Kafka, Hadoop, Spark, and many other systems for data exchange.
* **Row-oriented design:** Best suited for transactional or streaming data where entire rows are processed together.
* **Self-describing files:** Schema is embedded in the file, so readers know how to interpret the data.





##### **Real-Time Use Cases of Avro**



1\. Kafka Message Serialization

Avro is a popular choice for serializing messages in Apache Kafka because it’s compact and supports schema evolution. This ensures producers and consumers can evolve independently without breaking compatibility.

2\. Streaming Pipelines

In Spark Structured Streaming, Avro is often used for ingesting and writing event data because it’s efficient for row-based operations and integrates well with Kafka and other streaming sources.

3\. Data Interchange Between Systems

Avro acts as a common format for exchanging data between heterogeneous systems (e.g., Spark → Hadoop → Flink) because it’s language-neutral and schema-driven.

4\. Archiving Raw Event Data

Companies store raw logs or clickstream data in Avro because it’s lightweight and preserves schema information, making it easy to replay or reprocess later.

5\. Machine Learning Feature Storage

Avro can store row-based feature sets for ML pipelines, especially when features are consumed in streaming or transactional contexts.











