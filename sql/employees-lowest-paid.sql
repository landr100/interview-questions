select employee from (select employee, min(salary) from employees);
