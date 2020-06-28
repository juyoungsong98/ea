create TABLE resources (
	title VARCHAR NOT NULL,
	type VARCHAR NOT NULL,
	length VARCHAR NOT NULL,
	image VARCHAR NOT NULL, 
	link VARCHAR
);

create TABLE users (
	username VARCHAR NOT NULL PRIMARY KEY,
	password VARCHAR NOT NULL
);