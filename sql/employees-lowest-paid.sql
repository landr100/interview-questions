select employee from employees where salary = (select min(salary) from employees);
