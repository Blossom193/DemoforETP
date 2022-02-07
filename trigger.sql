create trigger INSET after insert on test5
for each row execute procedure Insertsync();