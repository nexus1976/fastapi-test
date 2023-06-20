"""ioc_container module."""
from dependency_injector import containers, providers
from domain.services.widgets_service import WidgetService

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=['webapp.widgets'])
    config = providers.Configuration()

    WidgetServiceFactory = providers.Factory(WidgetService)