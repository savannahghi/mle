from .drf_common_views import FacilityViewSet, SystemViewSet, UserFacilityViewSet
from .vanilla_common_views import (
    AboutView,
    FacilityCreateView,
    FacilityDeleteView,
    FacilityUpdateView,
    FacilityView,
    HomeView,
    SystemCreateView,
    SystemDeleteView,
    SystemsView,
    SystemUpdateView,
    UserFacilityAllotmentCreateView,
    UserFacilityAllotmentDeleteView,
    UserFacilityAllotmentUpdateView,
    UserFacilityAllotmentView,
)

__all__ = [
    "AboutView",
    "FacilityCreateView",
    "FacilityDeleteView",
    "FacilityUpdateView",
    "FacilityView",
    "FacilityViewSet",
    "HomeView",
    "SystemCreateView",
    "SystemDeleteView",
    "SystemUpdateView",
    "SystemsView",
    "SystemViewSet",
    "UserFacilityAllotmentCreateView",
    "UserFacilityAllotmentDeleteView",
    "UserFacilityAllotmentUpdateView",
    "UserFacilityAllotmentView",
    "UserFacilityViewSet",
]