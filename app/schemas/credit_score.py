from pydantic import BaseModel, Field
from enum import Enum

class RiskLevel(str, Enum):
    LOW = "LOW"         # Low risk (Ideal client)
    MEDIUM = "MEDIUM"   # Medium risk (Requires review or higher rate)
    HIGH = "HIGH"       # High risk (Likely rejection)

class CreditScore(BaseModel):
    """
    Output DTO.
    Result of the risk analysis returned to the Java backend.
    """
    score: int = Field(..., ge=300, le=850, description="Calculated credit score (simulated FICO)")
    risk_level: RiskLevel
    is_approved: bool = Field(..., description="Suggested final decision")
    suggested_interest_rate: float = Field(..., description="Suggested interest rate based on risk")
    max_approved_amount: float = Field(..., description="Maximum amount we are willing to lend")
