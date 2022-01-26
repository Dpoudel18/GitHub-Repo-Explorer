DROP TABLE if exists issues_label;

CREATE TABLE issues_label (
    label_id bigint primary key,
    issue_number varchar(25),
    label_name varchar(30)
);

\copy issues_label(label_id, issue_number, label_name) FROM 'unit21/issues_label.csv' DELIMITER ',' CSV HEADER;