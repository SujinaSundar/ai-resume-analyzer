"""
Pydantic schemas for API requests.
"""
from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    """
    Request schema for ATS score analysis.
    """
    resume_text: str
    job_description: str
 