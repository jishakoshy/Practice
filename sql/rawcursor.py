# # - CONCAT: full name

# - join: first name and department name

# select concat(first_name, depart_name) as name from worker;
                    #   or

# select e1.first_name, e2.depart_name from employees e1 join employees e2
#  on e1.id = e2.id;


# - EXTRACT: projects that started in 2023
# select distinct projects where year = 2023


# project with highest budget
# select max(budget) from budget   or 
# SELECT * FROM projects WHERE budget = (SELECT MAX(budget) FROM projects);


# - full name of all employees
# select concat(first_name, ' ', last_name) form employees

# - delete employees with salary higher than average
# select 

# sum of hgt 
# select sum(height) from student

# having grp by query

# second largest marks from student
# select * from student order by marks desc limit  1 offset 1

# add a column with a default value
# alter table student 

# the foreign key concept needs clarity
# create table student(id int primary key,name varchar(30), foreign key(id) 
# references employee(emp_id))

# query to find the name of lowest salaried employee in IT department,
# select name from student where department = 'IT' order by salary desc limit 1;

# query to add a new user and grant read only permission,
 
# custom procedure to find odd or even, 

# increase salaries of employees by 20% if salary < 50000 else 10%.
 
# Practice DCL, TCL queries, sub queries, if-else, case etc.

# Project with highest budget

# Full name of all employees

# Delete employees with salary higher than average
# delete from employees where salary > (select avg(salary) from employees)

