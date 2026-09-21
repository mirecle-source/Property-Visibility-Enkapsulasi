class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} - Rp{self.salary:,.0f}"


class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []

    def add_employee(self, employee):
        """Menambahkan employee ke perusahaan."""
        if not isinstance(employee, Employee):
            raise TypeError(
                "Objek yang ditambahkan harus merupakan Employee."
            )

        self.__employees.append(employee)

    def show_employees(self):
        """Menampilkan seluruh karyawan."""
        print(f"\n=== Karyawan {self.name} ===")

        if not self.__employees:
            print("Belum ada karyawan.")
            return

        for employee in self.__employees:
            print(employee)

    def __calculate_payroll(self):
        """Menghitung total seluruh gaji karyawan."""
        return sum(employee.salary for employee in self.__employees)

    def show_payroll(self):
        """Menampilkan total payroll perusahaan."""
        total = self.__calculate_payroll()

        print("\n=== Payroll ===")
        print(f"Total gaji: Rp{total:,.0f}")


# ==============================
# TEST PROGRAM
# ==============================

company = Company("PT Teknologi Manado")

company.add_employee(Employee("Ben", 4_700_000))
company.add_employee(Employee("Adi", 7_300_000))
company.add_employee(Employee("Rara", 6_500_000))

company.show_employees()
company.show_payroll()