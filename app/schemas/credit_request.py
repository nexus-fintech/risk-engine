from pydantic import BaseModel, Field
from decimal import Decimal

class CreditRequest(BaseModel):
    """
    Input DTO.
    Represents the aggregated financial data sent by the Java backend
    to request a risk evaluation.
    """
    client_id: int = Field(..., gt=0, description="Unique client ID in the Core Banking system")
    age: int = Field(..., ge=18, le=100, description="Client's age")
    
    monthly_income: float = Field(..., gt=0, description="Declared monthly income")
    monthly_debt: float = Field(..., ge=0, description="Total current monthly debts")
    
    requested_amount: float = Field(..., gt=0, description="Requested loan amount")
    term_in_months: int = Field(..., gt=0, le=60, description="Term in months")

    @property
    def debt_to_income_ratio(self) -> float:
        """Calculated property: Debt-to-Income ratio"""
        if self.monthly_income == 0:
            return 0.0
        return self.monthly_debt / self.monthly_income
