from __future__ import print_function
import time
import locationiq
from locationiq.rest import ApiException
from pprint import pprint

import logging
from functools import wraps

logging.basicConfig()
logger = logging.getLogger("my-logger")
logger.setLevel(logging.DEBUG)

API_KEY = 'pk.bc7ccb19ed88617f050998f1b303b2a1'

def timed(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug("{} ran in {}s".format(func.__name__, round(end - start, 2)))
        return result

    return wrapper

@timed
def geoloc(address,API_KEY,max_results=10):
    configuration = locationiq.Configuration()
    # Configure API key authorization: key
    configuration.api_key['key'] = API_KEY
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['key'] = 'Bearer'

    # Defining host is optional and default to https://eu1.locationiq.com/v1
    configuration.host = "https://eu1.locationiq.com/v1"
    # Enter a context with an instance of the API client
    with locationiq.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = locationiq.AutocompleteApi(api_client)
    # address = '1 Embarcadero street San Francisco' # str | Address to geocode
    normalizecity = 1 # int | For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs.
    limit = max_results # int | Limit the number of returned results. Default is 10. (optional) (default to 10)
    viewbox = '-132.84908,47.69382,-70.44674,30.82531' # str | The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - `max_lon,max_lat,min_lon,min_lat` or `min_lon,min_lat,max_lon,max_lat` - are accepted in any order as long as they span a real box.  (optional)
    bounded = 1 # int | Restrict the results to only items contained with the viewbox (optional)
    countrycodes = 'us' # str | Limit search to a list of countries. (optional)
    accept_language = 'en' # str | Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native (optional)
    tag = 'place' # str | Restricts the autocomplete search results to elements of specific OSM class and type.  Example - To restrict results to only class place and type city: tag=place:city, To restrict the results to all of OSM class place: tag=place (optional)

    try:
        api_response = api_instance.autocomplete(address, normalizecity, limit=limit, viewbox=viewbox, bounded=bounded, countrycodes=countrycodes, accept_language=accept_language, tag=tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AutocompleteApi->autocomplete: %s\n" % e)

if __name__=="__main__":
    address = '1 Embarcadero street San Francisco'
    geoloc(address,API_KEY,1)