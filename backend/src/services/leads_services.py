from fastapi import HTTPException, Query
from models import Lead
from database import SESSION_LOCAL

db = SESSION_LOCAL()

def create_lead_service(payload: dict):
    try:
        lead = Lead(**payload)
        db.add(lead)
        db.commit()
        return {"message": "Lead created", "data": payload}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
    
def create_lead_batch_service(payload: list[dict]):
    try:
        leads = [Lead(**item) for item in payload]
        db.add_all(leads)
        db.commit()
        return {"message": "Leads created", "data": payload}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

def list_leads_service(
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
    try:
        query = db.query(Lead)
        
        if page < 1:
            raise HTTPException(status_code=400, detail="Page number must be greater than 0")
        if search:
            query = query.filter(Lead.company_name.ilike(f"%{search}%"))
        if company_name:
            query = query.filter(Lead.company_name == company_name)
        if status:
            query = query.filter(Lead.current_status == status)
        if priority:
            query = query.filter(Lead.priority == priority)
        if country:
            query = query.filter(Lead.country == country)
        if industry:
            query = query.filter(Lead.industry == industry)
        
        if order.lower() == "desc":
            query = query.order_by(getattr(Lead, sort_by).desc())
        else:
            query = query.order_by(getattr(Lead, sort_by).asc())
        
        list_of_items = query.offset((page-1)*page_size).limit(page_size).all()
        print(f"list_of_items: {list_of_items}")
        
        return {
            "page": page,
            "page_size": page_size,
            "filters": {
                "search": search,
                "status": status,
                "priority": priority,
                "country": country,
                "industry": industry,
                "sort_by": sort_by,
                "order": order
            },
            "items": [
                {
                    "id": a.id,
                    "website": a.website,
                    "country": a.country,
                    "company_size": a.company_size,
                    "primary_service": a.primary_service,
                    "current_status": a.current_status,
                    "created_at": a.created_at,
                    "industry": a.industry,
                    "company_name": a.company_name,
                    "linkedin": a.linkedin,
                    "city": a.city,
                    "lead_source": a.lead_source,
                    "priority": a.priority,
                    "notes": a.notes,
                    "updated_at": a.updated_at,
                } for a in list_of_items
            ]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


def get_lead_service(lead_id:int):
    try:
        lead = db.query(Lead).filter(Lead.id==lead_id).first()
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")
        return lead
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

def update_lead_service(lead_id:int, payload:dict):
    try:
        lead = db.query(Lead).filter(Lead.id==lead_id).first()
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")
        for key, value in payload.items():
            setattr(lead, key, value)
        db.commit()
        return {"message": "Lead updated", "id": lead_id, "data": payload}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


def update_status_service(lead_id:int, payload:dict):
    try:
        lead = db.query(Lead).filter(Lead.id==lead_id).first()
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")
        lead.current_status = payload["status"]
        db.commit()
        return {"message": "Status updated", "id": lead_id, "status": payload["status"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

def delete_lead_service(lead_id:int):
    try:
        lead = db.query(Lead).filter(Lead.id==lead_id).first()
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")
        db.delete(lead)
        db.commit()
        return {"message": "Lead deleted", "id": lead_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

def add_activity_service(lead_id:int, payload:dict):
    try:
        lead = db.query(Lead).filter(Lead.id==lead_id).first()
        if not lead:
            raise HTTPException(status_code=404, detail="Lead not found")
        return {"message": "Activity added", "lead_id": lead_id, "activity": payload}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
