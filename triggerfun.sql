create or replace function Insertsync()
returns trigger as $test$
	BEGIN
		insert into test2(ID,NAME,AGE,CARD,PWD) values(new.ID,new.NAME,new.PIN,new.CARD,new.PWD);
		return NEW;
	END
$test$ LANGUAGE plpgsql;