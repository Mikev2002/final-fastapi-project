from pydantic import BaseModel, EmailStr, ConfigDict

# -------------------------
# Create User Request Schema
# -------------------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# -------------------------
# Update User Profile Schema
# -------------------------
class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None


# -------------------------
# Change Password Schema
# -------------------------
class UserPasswordChange(BaseModel):
    old_password: str
    new_password: str


# -------------------------
# User Response Schema
# -------------------------
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    # Pydantic V2: replaces "class Config: orm_mode = True"
    model_config = ConfigDict(from_attributes=True)
