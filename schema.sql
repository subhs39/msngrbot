drop table if exists subscribers;
create table subscribers(

	id serial primary key,
	Name VARCHAR(40) not null,
	phone_number numeric(10)

);