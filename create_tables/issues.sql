DROP TABLE if exists issues;

CREATE TABLE issues (
    number bigint primary key,
    user_id bigint,
    created_at date,
    updated_at date,
    closed_at date,
    milestone_number int,
    state varchar(7)
);
    
\copy issues(number, user_id, created_at, updated_at, closed_at, milestone_number, state) FROM 'unit21/issues.csv' DELIMITER ',' CSV HEADER;