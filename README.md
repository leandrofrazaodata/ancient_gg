# Data Engineer - Ancient gg

This repository contains the solution for the Data Engineer Technical Assessment. The project involves data cleaning, synthetic data generation, data transformation using dbt, and orchestration with Airflow[cite: 1, 2, 29].

## Project Structure

|-- data_generator/
|   |-- generate_data.py         
|
|-- dbt_project/
|   |-- models/
|   |   |-- core/
|   |   |   |-- daily_player_transactions.sql
|   |   |   |-- agg_discord_deposits_by_country.sql
|   |   |   |-- player_top_three_deposits.sql
|   |-- dbt_project.yml       
|   |-- profiles.yml          
|
|-- airflow_dag/
|   |-- dbt_dag.py               
|
|-- README.md                    



### **Part 1: Data Generation**

The `data_generator/generate_data.py` script extends the sample data to 1000 rows while adhering to the business rules outlined in the assessment[cite: 14, 22].

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
    This will create three CSV files in the directory: `transactions.csv`, `players.csv`, and `affiliates.csv`[cite: 10].

---

### **Part 2: dbt Models**

The dbt models transform the raw data to fulfill specific analytical requirements[cite: 24].

**Models:**
* `daily_player_transactions`: Creates one row per player daily, showing total deposits and withdrawals (with withdrawals as negative values)[cite: 25, 26].
* `agg_discord_deposits_by_country`: Calculates the sum and count of deposits by country for KYC-approved players from the 'Discord' affiliate origin[cite: 27].
* `player_top_three_deposits`: Shows one row per player with their three largest deposit amounts in separate columns[cite: 28].

**Setup & Execution:**
1.  **Install dbt:** You will need `dbt-core` and the specific adapter for your data warehouse (e.g., `dbt-postgres`, `dbt-snowflake`, `dbt-redshift`).
    ```bash
    pip install dbt-core dbt-<your-adapter>
    ```
2.  **Configure Profile:** Create a `profiles.yml` file in your `~/.dbt/` directory. This file contains the connection details for your data warehouse. Refer to the official dbt documentation for instructions specific to your adapter. The profile name should be `gaming_analytics_profile` to match the `dbt_project.yml` file.

3.  **Load Data:** Upload the three CSVs generated in Part 1 to your data warehouse. Ensure these tables are configured as sources for your dbt project.

4.  **Run Models:** Navigate to the `dbt_project` directory and run the models:
    ```bash
    # This command compiles and runs all models in the project
    dbt run
    ```
5.  **Test Models (Recommended):**
    ```bash
    # This command runs any tests defined in your project
    dbt test
    ```

---

### **Part 3: Airflow Orchestration (Bonus)**

The `airflow_dag/dbt_dag.py` file provides a simple Airflow DAG to orchestrate the dbt pipeline for daily refreshes.
