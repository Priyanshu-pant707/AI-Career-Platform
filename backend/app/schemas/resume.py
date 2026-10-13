
# from pydantic import BaseModel, Field
# from typing import Optional


# class EducationItem(BaseModel):
#     institution: Optional[str] = None
#     degree: Optional[str] = None
#     graduation_year: Optional[str] = None


# class ProjectItem(BaseModel):
#     name: str
#     description: Optional[str] = None
#     technologies: list[str] = Field(default_factory=list)


# class ExperienceItem(BaseModel):
#     company: Optional[str] = None
#     role: Optional[str] = None
#     description: Optional[str] = None


# class ResumeSchema(BaseModel):
#     name: Optional[str] = None
#     email: Optional[str] = None
#     phone: Optional[str] = None

#     skills: list[str] = Field(default_factory=list)
#     education: list[EducationItem] = Field(default_factory=list)
#     projects: list[ProjectItem] = Field(default_factory=list)
#     experience: list[ExperienceItem] = Field(default_factory=list)
#     certifications: list[str] = Field(default_factory=list)





from pydantic import BaseModel, Field
from typing import Optional


class EducationItem(BaseModel):
    institution: Optional[str] = None
    degree: Optional[str] = None
    graduation_year: Optional[str] = None


class ProjectItem(BaseModel):
    name: str
    description: Optional[str] = None
    technologies: list[str] = Field(default_factory=list)


class ExperienceItem(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    description: Optional[str] = None


class ResumeSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    skills: list[str] = Field(default_factory=list)
    education: list[EducationItem] = Field(default_factory=list)
    projects: list[ProjectItem] = Field(default_factory=list)
    experience: list[ExperienceItem] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)
