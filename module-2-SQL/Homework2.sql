--1
INSERT INTO pupils
(name, birthday, gender)
VALUES('Petrenko Serhiy', '2005-11-10', "Male");

--2
INSERT INTO courses
(id, title, date_start, date_finish, group_name, is_children)
VALUES(4, 'Java', '2022-01-15', '2022-09-01', 'Java_UA_1', 0);

--3
UPDATE courses
SET is_children=1
WHERE id BETWEEN 1 AND 3;

--4
SELECT name, MAX(rating) AS max_rate
FROM pupils p, study s 
WHERE s.course_id = 1;

--5
SELECT title as course_title
FROM courses c, study s, pupils_address pa 
WHERE pa.id = s.pupil_id 
  AND s.course_id = c.id 
  AND address = "Lviv"
  ORDER BY course_title 


--6
SELECT title as course_title
FROM courses c, study s, pupils p
WHERE p.id = s.pupil_id 
  AND s.course_id = c.id 
  AND gender = "Female"
  ORDER BY course_title 
  
  
--7
DELETE FROM study
WHERE pupil_id IN (SELECT id FROM pupils p 
					WHERE name LIKE 'Ivanov%')





