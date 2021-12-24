create database testdb
CREATE TABLE IF NOT EXISTS testdb.tarantool_table(Day int, TickTime double, Speed double) ENGINE=MergeTree() order by (Day, TickTime, Speed)
select * from testdb.tarantool_table where Day = 1 and Speed > 5748404;
