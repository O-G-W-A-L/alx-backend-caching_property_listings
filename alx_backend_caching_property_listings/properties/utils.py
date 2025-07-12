import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Retrieves all properties, attempting to fetch from cache first.
    """
    properties = cache.get('all_properties')
    if not properties:
        properties = list(Property.objects.all())
        cache.set('all_properties', properties, 3600)  # Cache for 1 hour ehhh ahna
    return properties

def get_redis_cache_metrics():
    """
    Retrieves and analyzes Redis cache hit/miss metrics.
    """
    try:
        redis_conn = get_redis_connection("default")
        info = redis_conn.info('keyspace')
        
        keyspace_hits = info.get('keyspace_hits', 0)
        keyspace_misses = info.get('keyspace_misses', 0)
        
        total_requests = keyspace_hits + keyspace_misses
        hit_ratio = (keyspace_hits / total_requests) * 100 if total_requests > 0 else 0
        
        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'hit_ratio': round(hit_ratio, 2)
        }
        
        logger.info(f"Redis Cache Metrics: Hits={keyspace_hits}, Misses={keyspace_misses}, Hit Ratio={hit_ratio:.2f}%")
        return metrics
    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {"error": str(e)}
