from fastmcp import FastMCP
from services.activitiy_services import list_activities_service
from services.leads_services import list_leads_service, update_lead_service

mcp = FastMCP("leadflow", instructions="Provide marketing lead data and the respective activities")

@mcp.tool()
def greet():
    """
    This is just a testing tool
    """
    return "Hello from leadflow"

@mcp.tool()
def list_leads(
    page:int=1,
    page_size:int=20,
    search:str|None=None,
    status:str|None=None,
    company_name:str|None=None,
    priority:str|None=None,
    country:str|None=None,
    industry:str|None=None,
    sort_by:str="updated_at",
    order:str="desc"
):
    """
    List all of the marketing leads with respect to the provided filters.
    """
    result = list_leads_service(
        page,
        page_size,
        search,
        status,
        company_name,
        priority,
        country,
        industry,
        sort_by,
        order
    )
    
    return result
    
@mcp.tool()
def list_activities(
    page: int = 1,
    page_size: int = 20,
    lead_id: int | None = None,
    status: str | None = None,
    meeting_type: str | None = None,
    created_by: str | None = None,
):
    """
    List all of the activities with respect to the provided filters.
    """
    
    result = list_activities_service(
        page,
        page_size,
        lead_id,
        status,
        meeting_type,
        created_by
    )
    
    return result
    
@mcp.tool()
def update_lead(lead_id:int, payload:dict):
    """
    Update the lead with the given lead_id according to the payload
    
    Parameters:
    - lead_id: Lead Id to update the fields in
    - payload: Dictionary that contains the fields to be updated
    """
    result = update_lead_service(
        lead_id, payload
    )
    
    return result

if __name__ == "__main__":
    mcp.run()
    
    