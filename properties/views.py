# Import necessary modules
from django.http import JsonResponse
from .utils import get_all_properties
from django.views.decorators.cache import cache_page

# Cache the page for 15 minutes (60 seconds * 15 minutes)
@cache_page(60 * 15)
def property_list(request):
    # Retrieve all properties
    properties = get_all_properties()
    # Return properties as a JSON response
    return JsonResponse({
        "data": properties
    })
