CREATE TABLE contents (
    id BIGSERIAL PRIMARY KEY NOT NULL,
    message_id INT,
    need_why VARCHAR(50) NOT NULL,
    texnologies VARCHAR(300) NOT NULL,
    location VARCHAR(100) NOT NULL, 
);

INSERT INTO contents (message_id, need_why, texnologies, location) values (28950, "xodim", "['cpp', 'git', 'java', 'kotlin', 'mongoDb', 'oracle', 'postgresql', 'spring']", "Xorazm");
