from rest_framework.throttling import UserRateThrottle

class MyThrottleClass(UserRateThrottle):
    scope = 'my_throttle_class'