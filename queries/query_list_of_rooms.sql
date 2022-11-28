SELECT r.name as room, COUNT(*) as number_of_students
FROM task_1.rooms r
JOIN task_1.students s ON r.id = s.room
GROUP BY r.name
ORDER BY number_of_students DESC
