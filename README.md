# Data Engineer - Ancient gg

This repository contains the solution for the Data Engineer Technical Assessment. The project involves data cleaning, synthetic data generation, data transformation using dbt, and orchestration with Airflow.
                  
### **Part 1: Data Generation**

The `data_generator/generate_data.py` script extends the sample data to 1000 rows while adhering to the business rules outlined in the assessment.

**To run the script:**
1.  Navigate to the `data_generator` directory.
2.  Install the required Python packages:
    ```bash
    pip install pandas Faker
    ```
3.  Execute the script:
    ```bash
    python generate_data.py
    ```
    This will create three CSV files in the directory: `transactions.csv`, `players.csv`, and `affiliates.csv`.

---

### **Part 2: dbt Models**

The dbt models transform the raw data to fulfill specific analytical requirements.

**Models:**
* `daily_player_transactions`: Creates one row per player daily, showing total deposits and withdrawals (with withdrawals as negative values).
* `agg_discord_deposits_by_country`: Calculates the sum and count of deposits by country for KYC-approved players from the 'Discord' affiliate origin.
* `player_top_three_deposits`: Shows one row per player with their three largest deposit amounts in separate columns.

**Setup & Execution:**
1.  **Install dbt:** You will need `dbt-core` and the specific adapter for the data warehouse (e.g., `dbt-postgres`, `dbt-snowflake`, `dbt-redshift`).
    ```bash
    pip install dbt-core dbt-<adapter>
    ```
2.  **Configure Profile:** Create a `profiles.yml` file in `~/.dbt/` directory. This file contains the connection details for data warehouse. Refer to the official dbt documentation for instructions specific to the adapter. The profile name should be `gaming_analytics_profile` to match the `dbt_project.yml` file.

3.  **Load Data:** Upload the three CSVs generated in Part 1 to data warehouse. Ensure these tables are configured as sources for dbt project.

4.  **Run Models:** Navigate to the `dbt_project` directory and run the models:
    ```bash
    # This command compiles and runs all models in the project
    dbt run
    ```
5.  **Test Models (Recommended):**
    ```bash
    # This command runs any tests defined in the project
    dbt test
    ```

---

### **Part 3: Airflow Orchestration (Bonus)**

The `airflow_dag/dbt_dag.py` file provides a simple Airflow DAG to orchestrate the dbt pipeline for daily refreshes.



