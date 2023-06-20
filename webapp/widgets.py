from typing import List
from fastapi import APIRouter, Depends, status, Response, Request
from dependency_injector.wiring import inject, Provide
from webapp.ioc_container import Container
from domain.services.widgets_service import WidgetService, Widget

widgets_router = APIRouter(prefix='/api/widgets', tags=['widgets'])

@widgets_router.get('/', response_model=List[Widget] | None,
                    status_code=status.HTTP_200_OK | status.HTTP_500_INTERNAL_SERVER_ERROR)
@inject
async def get_all_widgets(request: Request, response: Response,
                          widgetsService: WidgetService = Depends(Provide[Container.WidgetServiceFactory])):
    try:
        results = await widgetsService.get_widgets()
    except Exception as e:
        ex = f'widgets_router:get_all_widgets: {str(e)}'
        print(ex)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return None
    else:
        response.status_code = status.HTTP_200_OK
        return results