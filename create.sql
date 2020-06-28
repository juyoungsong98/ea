create TABLE resources (
	date VARCHAR NOT NULL,
	title VARCHAR NOT NULL,
	description VARCHAR,
	type VARCHAR NOT NULL,
	length VARCHAR NOT NULL, 
	link VARCHAR
);

create TABLE users (
	username VARCHAR NOT NULL PRIMARY KEY,
	password VARCHAR NOT NULL
);