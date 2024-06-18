from fastapi import HTTPException, status


class NotFoundProductException(HTTPException):
    def __init__(self, detail="Not Found Product"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
        self.detail = detail
