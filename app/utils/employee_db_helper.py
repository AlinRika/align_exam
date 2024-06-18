from sqlalchemy import select

from app.database import EmployeeOrm, new_session
from app.logging_setup import logger
from app.shemas.employee import EmployeeAdd, EmployeeGet, EmployeeFilter
from app.utils.exceptions import NotFoundProductException


class EmployeeDBHelper:
    @classmethod
    async def add_employee(cls, employee: EmployeeAdd) -> int:
        """Add new employee to database"""
        async with new_session() as session:
            data = employee.model_dump()
            new_employee = EmployeeOrm(**data)
            session.add(new_employee)
            await session.flush()
            await session.commit()
            logger.info(f"New employee ID: {new_employee.id}")
            return new_employee.id

    @classmethod
    # async def get_employees(cls, name: str, position: str, remote: bool) -> list[EmployeeGet]:
    async def get_employees(cls, employee: EmployeeFilter) -> list[EmployeeGet]:
        """Get all employees from database"""
        async with new_session() as session:
            query = select(EmployeeOrm)
            if employee.name_and_surname:
                query = query.where(EmployeeOrm.name_and_surname == employee.name_and_surname)
                logger.info("Use filter by name")
            if employee.position:
                query = query.where(EmployeeOrm.position == employee.position)
                logger.info("Use filter by position")
            if employee.remote:
                query = query.where(EmployeeOrm.remote == employee.remote)
                logger.info("Use filter by remote")
            result = await session.execute(query)
            logger.info("Find all employees in the database")
            employee_models = result.scalars().all()
            employees = [EmployeeGet.model_validate(employee_model) for employee_model in employee_models]
            return employees

    @classmethod
    async def get_one_employee(cls, employee_id) -> EmployeeGet:
        """Get one employee from database by ID"""
        async with new_session() as session:
            employee_model = await session.get(EmployeeOrm, employee_id)

            if not employee_model:
                logger.error(f"Product with ID: {employee_id} not found in the database.\n"
                             f"\tException: {NotFoundProductException}\n")
                raise NotFoundProductException(detail=f"Product with ID:{employee_id} not found")

            logger.info(f"Find product with ID: {employee_id} in the database")
            employee = EmployeeGet.model_validate(employee_model)
            return employee

