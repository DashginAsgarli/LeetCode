-- Write a solution to find the employees who earn more than their managers.

-- Return the result table in any order.


select e.name as Employee
from Employee e
join Employee m
on e.managerId = m.id
where e.salary > m.salary;