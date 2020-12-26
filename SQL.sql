DROP TABLE data.Highschooler;
CREATE TABLE data.Highschooler (
	id int,
    name varchar(255),
    grade int
    );
    
    
INSERT INTO data.Highschooler(id, name, grade)
VALUES 
	(1510, 'Jordan', 9),
	(1689, 'Gabriel', 9);
    
SELECT * FROM data.highschooler;

-- Talbe Friend
DROP TABLE data.Friend;
CREATE TABLE data.Friend (
	id1 int,
    id2 int
);

INSERT INTO data.Friend(id1, id2)
VALUES
	(1510, 1381),
	(1510, 1689);
    
SELECT * FROM Friend
