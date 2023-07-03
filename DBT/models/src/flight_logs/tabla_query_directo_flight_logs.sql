{{ config(materialized='table', sort='flight_number', dist='id') }}

SELECT id,
		flight_number, 
		airline, 
		departure_airport,
		departure_city, 
		departure_country
FROM dbt.flight_logs
ORDER BY flight_number