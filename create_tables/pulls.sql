DROP TABLE if exists pulls;

CREATE TABLE pulls (
    number bigint primary key,
    user_id bigint,
    created_at date,
    updated_at date,
    closed_at date,
    state varchar(7),
    merged_at date
);
    
\copy pulls(number, user_id, created_at, updated_at, closed_at, state, merged_at) FROM 'unit21/pulls.csv' DELIMITER ',' CSV HEADER;
\copy contributors(id, login, contributions) FROM 'unit21/contributors.csv' DELIMITER ',' CSV HEADER;
\copy issues_label(label_id, issue_number, label_name) FROM 'unit21/issues_label.csv' DELIMITER ',' CSV HEADER;