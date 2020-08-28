# https://www.cnblogs.com/mazhiyong/p/13225738.html
from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    id: Optional[int] = None
    username: str

    class Config:
        orm_mode = True