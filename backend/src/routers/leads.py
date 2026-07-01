from fastapi import APIRouter, HTTPException, Query
from database import SESSION_LOCAL
from services.leads_services import list_leads_service, get_lead_service, update_lead_service, delete_lead_service, create_lead_service, create_lead_batch_service, update_status_service, add_activity_service

router = APIRouter()
db = SESSION_LOCAL()

@router.post("")
def create_lead(payload: dict):
    try:
        return create_lead_service(payload)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
    
@router.post("/batch")
def create_lead_batch(payload: list[dict]):
    try:
        return create_lead_batch_service(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.get("")
def list_leads(
    page:int=1,
    page_size:int=20,
    search:str|None=None,
    status:str|None=Query(default=None),
    company_name:str|None=None,
    priority:str|None=None,
    country:str|None=None,
    industry:str|None=None,
    sort_by:str="updated_at",
    order:str="desc"
):

    return list_leads_service(page, page_size, search, status, company_name, priority, country, industry, sort_by, order)


@router.get("/{lead_id}")
def get_lead(lead_id:int):
        return get_lead_service(lead_id)

@router.put("/{lead_id}")
def update_lead(lead_id:int, payload:dict):
    return update_lead_service(lead_id, payload)

@router.patch("/{lead_id}/status")
def update_status(lead_id:int, payload:dict):
    return update_status_service(lead_id, payload)


@router.delete("/{lead_id}")
def delete_lead(lead_id:int):
    return delete_lead_service(lead_id)

@router.post("/{lead_id}/activities")
def add_activity(lead_id:int, payload:dict):
    return add_activity_service(lead_id, payload)
