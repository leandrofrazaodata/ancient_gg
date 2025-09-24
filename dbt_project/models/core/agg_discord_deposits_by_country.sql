{{ config(materialized='table') }}

SELECT
    p.country_code,
    COUNT(t.id) AS number_of_deposits,
    SUM(t.amount) AS total_deposit_amount
FROM
    {{ source('discord', 'transactions') }} t
JOIN
    {{ source('discord', 'players') }} p
    ON t.player_id = p.id
JOIN
    {{ source('discord', 'affiliates') }} a
    ON p.affiliate_id = a.id
WHERE
    t.type = 'Deposit'
    AND p.is_kyc_approved = TRUE
    AND a.origin = 'Discord'
GROUP BY
    1
ORDER BY

    3 DESC
