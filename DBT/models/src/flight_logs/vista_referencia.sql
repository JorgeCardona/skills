
-- Use the `ref` function to select from other models

SELECT t1.*
FROM {{ source('tabla_referencia','clientes_alias') }} AS t1
JOIN {{ source('vista_referencia','vista_query_con_with_flight_logs') }} AS t2
  ON t1.flight_number = t2.flight_number
WHERE t1.id > 1500 AND t1.id < 1800
