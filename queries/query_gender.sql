SELECT
  room
FROM
  task_1.students
GROUP BY
  room
HAVING
  MIN(sex) <> MAX(sex)
