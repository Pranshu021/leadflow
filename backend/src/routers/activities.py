from fastapi import APIRouter
from services.activitiy_services import list_activities_service, get_activity_service, update_activity_service, delete_activity_service
from database import SESSION_LOCAL
db = SESSION_LOCAL()

router=APIRouter()

@router.get("")
def list_activities(
    page:int=1,
    page_size:int=20,
    lead_id:int|None=None,
    status:str|None=None,
    meeting_type:str|None=None,
    created_by:str|None=None,
):
    return list_activities_service(page, page_size, lead_id, status, meeting_type, created_by)
    

@router.get("/{activity_id}")
def get_activity(activity_id:int):
    return get_activity_service(activity_id)

@router.put("/{activity_id}")
def update_activity(activity_id:int, payload:dict):
    return update_activity_service(activity_id, payload)

@router.delete("/{activity_id}")
def delete_activity(activity_id:int):
    return delete_activity_service(activity_id)