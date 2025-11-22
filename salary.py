import sys

if len(sys.argv) != 2:
    print("Usage: python employee_bonus.py <salary>")
    sys.exit(1)

salary = float(sys.argv[1])


bonus = 0.10 * salary


total_salary = salary + bonus


print("\n--- Salary Details ---")
print("Base Salary:", salary)
print("Bonus (10%):", bonus)
print("Total Salary after Bonus:", total_salary)
