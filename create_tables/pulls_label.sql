DROP TABLE if exists pulls_label;

CREATE TABLE pulls_label (
    label_id bigint primary key,
    pulls_number varchar(25),
    label_name varchar(30)
);

\copy pulls_label(label_id, pulls_number, label_name) FROM 'unit21/pulls_label.csv' DELIMITER ',' CSV HEADER;