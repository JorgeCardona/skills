## CREA LA TABLA
```sql
CREATE TABLE product (
    id SERIAL,
    date DATE NOT NULL,
    quantity INT,
    type VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2),
    description TEXT,
    supplier VARCHAR(100),
    location VARCHAR(100),
    status VARCHAR(50),
    category VARCHAR(50),
    name VARCHAR(100),
    PRIMARY KEY (id, date)
) PARTITION BY RANGE (date);
```

## CREA UN INDICE
```sql
CREATE INDEX idx_name ON product (name);
```

## CREA LAS PARTICIONES
```sql
CREATE TABLE product_p_before_2022 PARTITION OF product
    FOR VALUES FROM (MINVALUE) TO ('2022-01-01');

CREATE TABLE product_p_2022 PARTITION OF product FOR VALUES FROM (DATE '2022-01-01') TO (DATE '2023-01-01');
CREATE TABLE product_p_2023 PARTITION OF product FOR VALUES FROM (DATE '2023-01-01') TO (DATE '2024-01-01');
CREATE TABLE product_p_2024 PARTITION OF product FOR VALUES FROM (DATE '2024-01-01') TO (DATE '2025-01-01');

CREATE TABLE product_p_after_2024 PARTITION OF product
    FOR VALUES FROM (DATE '2025-01-01') TO (MAXVALUE);
```
   
## LISTA TODAS LAS PARTICIONES
```sql
SELECT
    *
FROM
    pg_inherits i
    JOIN pg_class c ON i.inhrelid = c.oid
    JOIN pg_class p ON i.inhparent = p.oid
WHERE
    inhparent = 'product'::regclass
ORDER BY
    p.relname,
    c.relname;
```	

## PARTICIONES CON ALIAS Y DE UNA TABLA ESPECIFICA
```sql
SELECT
    p.relname AS tabla,
    c.relname AS particion
FROM
    pg_inherits i
    JOIN pg_class c ON i.inhrelid = c.oid
    JOIN pg_class p ON i.inhparent = p.oid
WHERE
    inhparent = 'product'::regclass
ORDER BY
    p.relname,
    c.relname;
```
	
## Inserta datos para 2020
```sql
DO $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= 15 LOOP
        INSERT INTO product (date, quantity, type, price, description, supplier, location, status, category, name)
        VALUES ('2020-01-01'::DATE + (i - 1), 10 + i, 'Type ' || (i % 5 + 1), 100.50 + i, 'Description ' || (i % 5 + 1), 'Supplier ' || (i % 5 + 1), 'Location ' || (i % 5 + 1), 'Status ' || (i % 5 + 1), 'Category ' || (i % 5 + 1), 'Name ' || (i % 5 + 1));
        i := i + 1;
    END LOOP;
END $$;
```

## Inserta datos para 2021
```sql
DO $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= 15 LOOP
        INSERT INTO product (date, quantity, type, price, description, supplier, location, status, category, name)
        VALUES ('2021-01-01'::DATE + (i - 1), 10 + i, 'Type ' || (i % 5 + 1), 100.50 + i, 'Description ' || (i % 5 + 1), 'Supplier ' || (i % 5 + 1), 'Location ' || (i % 5 + 1), 'Status ' || (i % 5 + 1), 'Category ' || (i % 5 + 1), 'Name ' || (i % 5 + 1));
        i := i + 1;
    END LOOP;
END $$;
```

## Inserta datos para 2022
```sql
DO $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= 30 LOOP
        INSERT INTO product (date, quantity, type, price, description, supplier, location, status, category, name)
        VALUES ('2022-01-01'::DATE + (i - 1), 10 + i, 'Type ' || (i % 5 + 1), 100.50 + i, 'Description ' || (i % 5 + 1), 'Supplier ' || (i % 5 + 1), 'Location ' || (i % 5 + 1), 'Status ' || (i % 5 + 1), 'Category ' || (i % 5 + 1), 'Name ' || (i % 5 + 1));
        i := i + 1;
    END LOOP;
END $$;
```

## Inserta datos para 2023
```sql
DO $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= 30 LOOP
        INSERT INTO product (date, quantity, type, price, description, supplier, location, status, category, name)
        VALUES ('2023-01-01'::DATE + (i - 1), 10 + i, 'Type ' || (i % 5 + 1), 100.50 + i, 'Description ' || (i % 5 + 1), 'Supplier ' || (i % 5 + 1), 'Location ' || (i % 5 + 1), 'Status ' || (i % 5 + 1), 'Category ' || (i % 5 + 1), 'Name ' || (i % 5 + 1));
        i := i + 1;
    END LOOP;
END $$;
```

## Inserta datos para 2024
```sql
DO $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= 30 LOOP
        INSERT INTO product (date, quantity, type, price, description, supplier, location, status, category, name)
        VALUES ('2024-01-01'::DATE + (i - 1) * INTERVAL '1 day', 10 + i, 'Type ' || (i % 5 + 1), 100.50 + i, 'Description ' || (i % 5 + 1), 'Supplier ' || (i % 5 + 1), 'Location ' || (i % 5 + 1), 'Status ' || (i % 5 + 1), 'Category ' || (i % 5 + 1), 'Name ' || (i % 5 + 1));
        i := i + 1;
    END LOOP;
END $$;
```

## Inserta datos para 2025
```sql
DO $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= 15 LOOP
        INSERT INTO product (date, quantity, type, price, description, supplier, location, status, category, name)
        VALUES ('2025-01-01'::DATE + (i - 1) * INTERVAL '1 day', 10 + i, 'Type ' || (i % 5 + 1), 100.50 + i, 'Description ' || (i % 5 + 1), 'Supplier ' || (i % 5 + 1), 'Location ' || (i % 5 + 1), 'Status ' || (i % 5 + 1), 'Category ' || (i % 5 + 1), 'Name ' || (i % 5 + 1));
        i := i + 1;
    END LOOP;
END $$;
```

## Consultar datos de la partición product_p_before_2022
```sql
SELECT * FROM product WHERE date < '2022-01-01';
```

## Consultar datos de la partición product_p_before_2022
```sql
SELECT * FROM product_p_before_2022;
```

## Plan de ejecución para la partición product_p_before_2022
```sql
EXPLAIN (ANALYZE, VERBOSE, FORMAT JSON)
SELECT * FROM product WHERE date < '2022-01-01';
```

## Consultar datos de la partición product_p_2022
```sql
SELECT * FROM product WHERE date >= '2022-01-01' AND date < '2023-01-01';
```

## Consultar datos de la partición product_p_2022
```sql
SELECT * FROM product_p_2022;
```

## Plan de ejecución para la partición product_p_2022
```sql
EXPLAIN (ANALYZE, VERBOSE, FORMAT JSON)
SELECT * FROM product WHERE date >= '2022-01-01' AND date < '2023-01-01';
```

## Consultar datos de la partición product_p_2023
```sql
SELECT * FROM product WHERE date >= '2023-01-01' AND date < '2024-01-01';
```

## Consultar datos de la partición product_p_2023
```sql
SELECT * FROM product_p_2023;
```

## Plan de ejecución para la partición product_p_2023
```sql
EXPLAIN (ANALYZE, VERBOSE, FORMAT JSON)
SELECT * FROM product WHERE date >= '2023-01-01' AND date < '2024-01-01';
```

## Consultar datos de la partición product_p_2024
```sql
SELECT * FROM product WHERE date >= '2024-01-01' AND date < '2025-01-01';
```

## Consultar datos de la partición product_p_2024
```sql
SELECT * FROM product_p_2024;
```

## Plan de ejecución para la partición product_p_2024
```sql
EXPLAIN (ANALYZE, VERBOSE, FORMAT JSON)
SELECT * FROM product WHERE date >= '2024-01-01' AND date < '2025-01-01';
```

## Consultar datos de la partición product_p_after_2024
```sql
SELECT * FROM product WHERE date >= '2025-01-01';
```

## Consultar datos de la partición product_p_after_2024
```sql
SELECT * FROM product_p_after_2024;
```

## Plan de ejecución para la partición product_p_after_2024
```sql
EXPLAIN (ANALYZE, VERBOSE, FORMAT JSON)
SELECT * FROM product WHERE date >= '2025-01-01';
```

## consulta todos los datos
```sql
SELECT * FROM product;
```

## Plan de ejecución para todos los datos en la tabla product
```sql
EXPLAIN (ANALYZE, VERBOSE, FORMAT JSON)
SELECT * FROM product;
```
