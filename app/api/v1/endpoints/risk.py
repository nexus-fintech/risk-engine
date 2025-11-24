from fastapi import APIRouter, HTTPException, status
from app.schemas.credit_request import CreditRequest
from app.schemas.credit_score import CreditScore
from app.services.risk_evaluator import RiskEvaluatorService

router = APIRouter()
risk_service = RiskEvaluatorService()

@router.post(
    "/evaluate-risk",
    response_model=CreditScore,
    status_code=status.HTTP_200_OK,
    summary="Evaluate Credit Risk",
    description="Analyzes a client's financial profile and determines their eligibility for a loan."
)
def evaluate_risk(request: CreditRequest):
    """
    Main endpoint for the risk engine.
    Receives client data (Income, Debt, Age) and returns a CreditScore.
    """
    try:
        result = risk_service.evaluate(request)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing risk evaluation: {str(e)}"
        )
