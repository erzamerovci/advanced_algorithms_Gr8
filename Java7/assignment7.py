from typing import List, Optional, Dict

class Employee:
    def __init__(self, id: int, name: str, position: str, salary: float, supervisor_id: Optional[int]):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.supervisor_id = supervisor_id


def get_employee_depth(employees: List[Employee], employee_id: int) -> int:
    """
    Calculate the depth of an employee in the organizational hierarchy.
    CEO = depth 0.
    Returns -1 if employee not found or if a circular reference is detected.
    """

    emp_dict: Dict[int, Employee] = {emp.id: emp for emp in employees}

    if employee_id not in emp_dict:
        return -1 

    visited = set()  

    def find_depth(emp: Employee) -> int:
        if emp.supervisor_id is None:
            return 0  
        if emp.id in visited:
            return -1  
        visited.add(emp.id)

        supervisor = emp_dict.get(emp.supervisor_id)
        if not supervisor:
            return -1  

        supervisor_depth = find_depth(supervisor)
        if supervisor_depth == -1:
            return -1

        return supervisor_depth + 1

    return find_depth(emp_dict[employee_id])


employees = [
    Employee(1, "Alice Johnson", "CEO", 250000, None),
    Employee(2, "Bob Smith", "CTO", 180000, 1),
    Employee(3, "Carol White", "CFO", 175000, 1),
    Employee(4, "David Brown", "Engineering Manager", 140000, 2),
    Employee(5, "Eve Davis", "QA Manager", 130000, 2),
    Employee(6, "Frank Wilson", "Senior Accountant", 95000, 3),
    Employee(7, "Grace Lee", "Senior Developer", 120000, 4),
    Employee(8, "Henry Martinez", "Junior Developer", 85000, 4),
    Employee(9, "Ivy Chen", "QA Engineer", 90000, 5),
    Employee(10, "Jack Thompson", "DevOps Engineer", 110000, 4),
    Employee(11, "Kelly Anderson", "Junior Accountant", 65000, 6),
    Employee(12, "Liam Garcia", "Intern Developer", 50000, 7)
]

print(get_employee_depth(employees, 1))   # 0 (Alice - CEO)
print(get_employee_depth(employees, 2))   # 1 (Bob - CTO)
print(get_employee_depth(employees, 7))   # 3 (Grace - Senior Developer)
print(get_employee_depth(employees, 12))  # 4 (Liam - Intern)
print(get_employee_depth(employees, 999)) # -1 (Not found)
