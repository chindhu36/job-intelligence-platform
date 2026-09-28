from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CVProfile:
    candidate_name: Optional[str] = None

    summary: Optional[str] = None

    technical_skills: List[str] = field(default_factory=list)

    programming_languages: List[str] = field(default_factory=list)

    cloud_platforms: List[str] = field(default_factory=list)

    data_platforms: List[str] = field(default_factory=list)

    databases: List[str] = field(default_factory=list)

    bi_tools: List[str] = field(default_factory=list)

    frameworks: List[str] = field(default_factory=list)

    engineering_practices: List[str] = field(default_factory=list)

    work_experience: List[str] = field(default_factory=list)

    qualifications: List[str] = field(default_factory=list)

    certifications: List[str] = field(default_factory=list)