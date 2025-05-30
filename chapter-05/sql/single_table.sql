
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


INSERT INTO users(name, email, password) VALUES (
    'John',
    'john@john.de',
    '12345'
);

INSERT INTO users(name, email, password) VALUES (
    'Jane',
    'jane@jane.de',
    '12345'
);

INSERT INTO users(name, email, password) VALUES (
    'Karl',
    'Karl@Karl.de',
    '12345'
);

INSERT INTO users(name, email, password) VALUES (
    'Karla',
    'Karla@Karla.de',
    '12345'
);

INSERT INTO users(name, email, password) VALUES (
    'Hans',
    'Hans@Hans.de',
    '12345'
);

INSERT INTO users(name, email, password) VALUES (
    'Hannah',
    'Hannah@Hannah.de',
    '12345'
);

INSERT INTO users(name, email, password) VALUES (
    'Ben',
    'Ben@Ben.de',
    '12345'
);


INSERT INTO users(name, email, password) VALUES (
    'Betty'
    'Betty@Betty.de',
    '12345'
);


INSERT INTO users(name, email, password) VALUES (
    'Tim'
    'Tim@Tim.de',
    '12345'
);

INSERT INTO users(name, email, password) VALUES (
    'Tina'
    'Tina@Tina.de',
    '12345'
);


SELECT * FROM users;

SELECT name, email
FROM users
WHERE id = 1;

UPDATE users
SET name ='Steve'
WHERE id = 1
RETURNING *;


DELETE FROM users
WHERE id = 1;