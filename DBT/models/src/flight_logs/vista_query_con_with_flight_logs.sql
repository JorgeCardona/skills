# alias de tabla a consultar
WITH SELECT_TEST AS(

SELECT * FROM dbt.flight_logs
)

# select que crea la vista
SELECT flight_number, 
		airline, 
		departure_airport,
		departure_city, 
		departure_country
FROM SELECT_TEST