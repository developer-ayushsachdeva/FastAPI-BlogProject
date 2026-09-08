from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    body: str

class BlogResponse(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str