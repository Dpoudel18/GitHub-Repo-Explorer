DROP TABLE if exists contributors;

CREATE TABLE contributors (
    id int primary key,
    login varchar(25),
    contributions int
);

\copy contributors(id, login, contributions) FROM 'unit21/contributors.csv' DELIMITER ',' CSV HEADER;