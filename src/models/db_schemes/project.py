from pydantic import BaseModel, Field, field_validator 
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: str = Field(..., min_length=1)


    @field_validator('project_id')
    def validate_project_id(cls, value):
        if value is None:
            raise ValueError('project_id cannot be None')
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value
    
    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def get_indexes(cls):
        return [
            {
                "key": [("chunk_project_id", 1)],
                "name": "chunk_project_id_index_1",
                "unique": False
            }
        ]

