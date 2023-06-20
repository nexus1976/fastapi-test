import uuid
from typing import List
from domain.entities.widget import Widget

class WidgetService():
    async def get_widgets(self) -> List[Widget]:
        widgets = list()
        widget1 = Widget()
        widget1.id = uuid.uuid4()
        widget1.name = 'widget1'
        widgets.append(widget1)
        widget2 = Widget()
        widget2.id = uuid.uuid4()
        widget2.name = 'widget2'
        widgets.append(widget2)
        widget3 = Widget()
        widget3.id = uuid.uuid4()
        widget3.name = 'widget3'
        widgets.append(widget3)
        return widgets    