DROP TABLE if exists commits cascade;
DROP TABLE if exists contributors cascade;
DROP TABLE if exists issues cascade;
DROP TABLE if exists pulls cascade;
DROP TABLE if exists milestones cascade;
DROP TABLE if exists issues_label cascade;
DROP TABLE if exists pulls_label cascade;


CREATE TABLE contributors (
    id int primary key,
    login varchar(25),
    contributions int
);

CREATE TABLE commits (
    sha varchar(45) primary key,
    author_id bigint,
    committer_id bigint,
    message_label varchar(100),
    parents_sha varchar(45),
    commit_date date,
    FOREIGN KEY (committer_id) REFERENCES contributors(id)
);

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
    state varchar(7),
    FOREIGN KEY (creator_id) REFERENCES contributors(id)
);

CREATE TABLE issues (
    number bigint primary key,
    user_id bigint,
    created_at date,
    updated_at date,
    closed_at date,
    milestone_number int,
    state varchar(7),
    FOREIGN KEY (user_id) REFERENCES contributors(id),
    FOREIGN KEY (milestone_number) REFERENCES milestones(number),
    FOREIGN KEY (number) REFERENCES issues_label(issue_number)
);

CREATE TABLE pulls (
    number int primary key,
    user_id bigint,
    created_at date,
    updated_at date,
    closed_at date,
    state varchar(7),
    merged_at date,
    FOREIGN KEY (user_id) REFERENCES contributors(id)
);


CREATE TABLE issues_label (
    label_id bigint primary key,
    issue_number bigint,
    label_name varchar(30),
    FOREIGN KEY (issue_number) REFERENCES issues(number)
);

CREATE TABLE pulls_label (
    label_id bigint primary key,
    pulls_number bigint,
    label_name varchar(30),
    FOREIGN KEY (pulls_number) REFERENCES pulls(number)
);
