
# DMart Data Architecture and Analytics Workflow

## 1. Introduction
DMart operates through a combination of **offline stores** and **online platforms**, generating large volumes of transactional and operational data daily. To manage, process, and analyze this data efficiently, a robust data pipeline leveraging **Azure services** is implemented. This document explains the entire workflow in detail.

---

## 2. Data Sources
DMart collects data from multiple sources:

- **Offline Stores**
  - Store managers maintain **Excel sheets** for inventory and sales.
- **Online Stores**
  - Website transactions stored in **RDBMS** or **NoSQL** databases.
  - Data formats include **blob storage** and **files**.
- **Point of Sale (POS)**
  - Transaction data captured in **CSV files**.
- **Cash on Delivery (COD)**
  - Data stored in a separate path.

**End of Day (EOD)** data consolidation occurs at **12 AM nightly**, ensuring all transactions and updates are captured.

---

## 3. Azure Data Factory (ADF)
**Purpose**: Data ingestion and movement.

- **Key Functions**:
  - **Copy Data**: Extract data from multiple sources (Excel, CSV, databases).
  - **Move Data Regularly**: Automate data transfer using **pipelines**.
- **Why ADF?**
  - Handles large-scale data integration.
  - Supports scheduled and event-driven workflows.

---

## 4. Azure Data Lake
**Purpose**: Centralized storage for raw data.

- **Features**:
  - **Massive Storage**: Cost-effective solution for storing large datasets.
  - **Data Types**:
    - **Structured**: RDBMS tables.
    - **Semi-Structured**: CSV, JSON files.
    - **Unstructured**: NoSQL databases like MongoDB, Cosmos DB.
- **Benefits**:
  - Scalability for growing data.
  - Separation of raw and processed data for better governance.

---

## 5. Azure Databricks
**Purpose**: Data processing and transformation.

- **Tools & Capabilities**:
  - **Notebook Interface**: Combines code blocks and text blocks for collaborative work.
  - **Processing Engine**: Uses **PySpark** for distributed data processing.
  - **Integration**: Similar to Google Colab for interactive coding.
- **Use Cases**:
  - Cleaning and transforming raw data.
  - Applying business logic for analytics.

---

## 6. Azure Synapse Analytics
**Purpose**: Data analysis and reporting.

- **Functions**:
  - **Prepare Reports**: Summarize processed data for stakeholders.
  - **Dashboards**: Visualize KPIs and trends.
  - **BI Tools**: Enable advanced analytics and decision-making.
- **Advantages**:
  - High-performance querying.
  - Seamless integration with Power BI.

---

## 7. End-to-End Workflow
1. **Data Collection**: From offline stores, online stores, POS, and COD.
2. **Data Ingestion**: Using **Azure Data Factory** pipelines.
3. **Data Storage**: In **Azure Data Lake** for raw data.
4. **Data Processing**: With **Azure Databricks** using PySpark.
5. **Data Analysis & Reporting**: Through **Azure Synapse Analytics**.

---

## 8. Benefits of This Architecture
- **Scalability**: Handles growing data volumes.
- **Cost Efficiency**: Optimized storage and compute resources.
- **Automation**: Reduces manual intervention.
- **Actionable Insights**: Enables data-driven decision-making.
