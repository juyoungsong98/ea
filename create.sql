create TABLE short (
	title VARCHAR NOT NULL,
	description VARCHAR NOT NULL,
	type VARCHAR NOT NULL,
	link VARCHAR NOT NULL,
	id INTEGER NOT NULL
);

create TABLE long (
	title VARCHAR NOT NULL,
	description VARCHAR NOT NULL,
	type VARCHAR NOT NULL,
	link VARCHAR NOT NULL,
	id INTEGER NOT NULL
);

create TABLE users (
	username VARCHAR NOT NULL PRIMARY KEY,
	password VARCHAR NOT NULL
	history INTEGERLIST
);