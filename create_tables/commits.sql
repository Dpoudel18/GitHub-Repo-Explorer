DROP TABLE if exists commits;

CREATE TABLE commits (
    sha varchar(45) primary key,
    author_id bigint,
    committer_id bigint,
    message_label varchar(100),
    parents_sha varchar(45),
    commit_date date
);

\copy commits(sha, author_id, committer_id, message_label, parents_sha, commit_date) FROM 'unit21/commits.csv' DELIMITER ',' CSV HEADER;