
## Get Started

1. fork the repo at https://github.com/rflynn/interview-questions
2. clone the repo locally. Do all subsequent work there.
3. complete as many of the following problems as you can in 30 minutes in any order. commit work locally as it is done.

## Write Python

Create the following files in `python/`. As you create them, commit them to your git repository.

file         | spec
-------------|--------------
fizzbuzz.py  | write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
primes100.py | print the primes between 1-100
checkstr.py  | a string may contain alphanumeric characters. it may also contain dashes, but not begin or end with them or contain 2 or sequentially. write a function that checks for this format.
randomtuples.py | write a function to generate a list of length 0-3 of the following tuple: (an integer between 0-3, a float between -0.5 and 0.5, a random alphanumeric string of length 0-5 which may also be None)
inherit.py   | write a class Foo and a class Bar that inherits from Foo. when a Foo object is created it prints "foo". when a Bar object is created it prints "foo" using inheritance and "bar".
perm2.py     | permutations of size 2 of a given list

## Run/Read/Debug Python

Given the file `python/get.py`

0. summarize what the file does
1. get it to run. use any tools/references you want.
2. get it to pass all tests
3. add an additional meaningful test
4. if an operation fails, return a non-zero exit code to the shell
5. add the capability to fetch multiple urls in one invocation
6. what additional improvements can you make?

## Write SQL

`cd interview-questions/sql`

1. install sqlite3 from http://sqlite.org/download.html
2. briefly review the schema and data in `sql/employees.sql`
3. load data `sqlite3 employees.sqlite3 < sql/employees.sql`
4. write queries to the following files
 1. `sql/employees-all.sql` display all employees
 2. `sql/employees-total.sql` display the total number of employees
 3. `sql/employees-salary-total.sql` display the total salary paid to all employees
 4. `sql/employees-lowest-paid.sql` display the name of the lowest-paid employee
 5. `sql/employees-managed-by-bob.sql` display all employees under manager 'Bob'
 6. `sql/employees-managers.sql` display a list of managers
 7. `sql/employees-brian.sql` display all employees with first name 'Brian'
5. be ready to discuss
 1. how well would these queries hold up against large datasets?
 2. how could we speed up queries?
 3. what are some problems with this schema? how can they be improved?
6. `sql/employees.sql`: rewrite this schema

