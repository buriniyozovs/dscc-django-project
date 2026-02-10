# views.py - Add this to your existing views file
from django.http import JsonResponse
from django.db import connection
import time
def health_check(request):
 """
 Health check endpoint for monitoring.
 Returns the status of the application and database connection.
 """
 health = {
 "status": "healthy",
 "timestamp": time.time(),
 "checks": {}
 }
 # Check database connectivity
 try:
 with connection.cursor() as cursor:
 cursor.execute("SELECT 1")
 health["checks"]["database"] = "connected"
 except Exception as e:
 health["status"] = "unhealthy"
 health["checks"]["database"] = str(e)
 status_code = 200 if health["status"] == "healthy" else 503
 return JsonResponse(health, status=status_code)