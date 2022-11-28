SELECT r.name as room, DATE_TRUNC('day', AVG(AGE(s.birthday))) AS average_age
FROM task_1.students s
JOIN task_1.rooms r
ON s.room = r.id
GROUP BY r.name
ORDER BY average_age
LIMIT 5
