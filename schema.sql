drop table if exists posts;
	create table posts (
		id integer primary key autoincrement,
		user_name text not null,
		rating text not null,
		location text not null,
		busy text not null,
		address text not null,
		name text not null,
		content text not null
);
