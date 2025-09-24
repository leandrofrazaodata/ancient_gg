{{ config(materialized='table') }}

WITH ranked_deposits AS (
    SELECT
        player_id,
        amount,
        ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY amount DESC) as deposit_rank
    FROM
        {{ source('your_source_schema', 'transactions') }}
    WHERE
        type = 'Deposit'
)

SELECT
    player_id,
    MAX(CASE WHEN deposit_rank = 1 THEN amount END) AS first_largest_deposit,
    MAX(CASE WHEN deposit_rank = 2 THEN amount END) AS second_largest_deposit,
    MAX(CASE WHEN deposit_rank = 3 THEN amount END) AS third_largest_deposit
FROM
    ranked_deposits
WHERE
    deposit_rank <= 3
GROUP BY
    1
ORDER BY
    1