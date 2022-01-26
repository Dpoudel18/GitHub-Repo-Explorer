DROP TABLE if exists milestones;

CREATE TABLE milestones (
    number bigint primary key,
    title varchar(100),
    creator_id bigint,
    created_at date,
    updated_at date,
    due_on date,
    closed_at date,
    open_issues int,
    closed_issues int,
    state varchar(7)
);

\copy milestones(number, title, creator, created_at, updated_at, due_on, closed_at, open_issues, closed_issues, state) FROM 'unit21/milestones.csv' DELIMITER ',' CSV HEADER;