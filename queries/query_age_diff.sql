SELECT
  s2.room,
  AGE(s2.max_date, s2.min_date) as age_diff
FROM
  (
    SELECT
      room,
      MAX(birthday) OVER(PARTITION BY room) as max_date,
      MIN(birthday) OVER(PARTITION BY room) as min_date
    FROM
      task_1.students
  ) s2
GROUP BY
  s2.room,
  AGE(s2.max_date, s2.min_date)
ORDER BY
  age_diff DESC
LIMIT
  5
