{{ config(materialized='table') }}

WITH base_transactions AS (
    SELECT
        player_id,
        CAST(timestamp AS DATE) AS transaction_date,
        type,
        amount
    FROM
        {{ source('your_source_schema', 'transactions') }}
)

SELECT
    player_id,
    transaction_date,
    SUM(CASE WHEN type = 'Deposit' THEN amount ELSE 0 END) AS total_deposits,
    -- Withdrawals should be negative as per instructions
    SUM(CASE WHEN type = 'Withdraw' THEN -amount ELSE 0 END) AS total_withdrawals
FROM
    base_transactions
GROUP BY
    1, 2
ORDER BY
    1, 2