from fastapi import APIRouter, Depends, status

from app.logging_setup import logger
from app.shemas.employee import EmployeeAdd, EmployeeGet, EmployeeFilter
from app.utils.employee_db_helper import EmployeeDBHelper

router = APIRouter()


@router.post(
    path="/employees/new",
    summary="Add a new employee",
    response_model=EmployeeGet,
    status_code=status.HTTP_201_CREATED,
)
async def post_employee(employee: EmployeeAdd = Depends()) -> EmployeeGet:
    logger.info("post_employee start")
    new_employee_id = await EmployeeDBHelper.add_employee(employee)
    logger.info(f"Product with ID: {new_employee_id} create")
    new_employee = await EmployeeDBHelper.get_one_employee(new_employee_id)
    logger.info("post_employee finish\n")
    return new_employee


@router.get(
    path="/employees/list",
    summary="Get all employees",
    response_model=list[EmployeeGet] | str,
)
async def get_employees(employee: EmployeeFilter = Depends()) -> list[EmployeeGet] | str:
    logger.info("get_employees start")
    products = await EmployeeDBHelper.get_employees(employee)
    if products:
        logger.info(f"Get all employees")
        logger.info("get_employees finish\n")
        return products
    logger.info(f"Database is empty")
    logger.info("get_employees finish\n")
    return 'Database is empty'


@router.get(
    path="/employees/{id}",
    summary="Get a employee by ID",
    response_model=EmployeeGet,
)
async def get_one_employee(id: int) -> EmployeeGet:
    logger.info("get_one_employee start")
    product = await EmployeeDBHelper.get_one_employee(id)
    logger.info(f"Get employee by ID: {id}")
    logger.info("get_one_employee finish\n")
    return product
