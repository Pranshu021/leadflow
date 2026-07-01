from fastapi import HTTPException
from database import SESSION_LOCAL
from models import Activity

db = SESSION_LOCAL()


def list_activities_service(
    page: int = 1,
    page_size: int = 20,
    lead_id: int | None = None,
    status: str | None = None,
    meeting_type: str | None = None,
    created_by: str | None = None,
):
    try:
        list_of_items = (
            db.query(Activity)
            .filter(
                Activity.lead_id == lead_id if lead_id else True,
                Activity.status == status if status else True,
                Activity.meeting_type == meeting_type if meeting_type else True,
                Activity.created_by == created_by if created_by else True,
            )
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return {
            "items": [
                {
                    "id": a.id,
                    "lead_id": a.lead_id,
                    "meeting_type": a.meeting_type.value,
                    "contact_person": a.contact_person,
                    "designation": a.designation,
                    "email": a.email,
                    "phone": a.phone,
                    "status": a.status.value,
                    "created_by": a.created_by,
                    "created_at": a.created_at.isoformat() if a.created_at else None,
                }
                for a in list_of_items
            ]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


def get_activity_service(activity_id: int):
    try:
        activity = db.query(Activity).filter(Activity.id == activity_id).first()
        if not activity:
            raise HTTPException(status_code=404, detail="Activity not found")
        return activity
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


def update_activity_service(activity_id: int, payload: dict):
    try:
        activity = db.query(Activity).filter(Activity.id == activity_id).first()
        if not activity:
            raise HTTPException(status_code=404, detail="Activity not found")
        for key, value in payload.items():
            setattr(activity, key, value)
        db.commit()
        return {"message": "Activity updated", "id": activity_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e


def delete_activity_service(activity_id: int):
    try:
        activity = db.query(Activity).filter(Activity.id == activity_id).first()
        if not activity:
            raise HTTPException(status_code=404, detail="Activity not found")
        db.delete(activity)
        db.commit()
        return {"message": "Activity deleted", "id": activity_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
