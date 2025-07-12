from django.core.cache import cache
from .models import Property

def get_all_properties():
    """
    Retrieves all properties, attempting to fetch from cache first.
    """
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour
    return properties
