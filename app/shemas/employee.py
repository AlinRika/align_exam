from pydantic import BaseModel, ConfigDict


class EmployeeAdd(BaseModel):
    name_and_surname: str
    age: int
    position: str
    remote: bool


class EmployeeGet(EmployeeAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class EmployeeFilter(BaseModel):
    name_and_surname: str | None = None
    position: str | None = None
    remote: bool | None = None
