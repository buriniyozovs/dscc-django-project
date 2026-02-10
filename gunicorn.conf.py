# gunicorn.conf.py - Gunicorn configuration file
import multiprocessing
# Bind to all interfaces on port 8000
bind = "0.0.0.0:8000"
# Worker configuration
# Rule of thumb: (2 x CPU cores) + 1
workers = multiprocessing.cpu_count() * 2 + 1
# Worker class - sync is default, consider gevent for I/O-bound apps
worker_class = "sync"
# Timeout for worker processes (seconds)
timeout = 30
# Graceful timeout for workers to finish requests
graceful_timeout = 30
# Maximum requests per worker before restart (prevents memory leaks)
max_requests = 1000
max_requests_jitter = 50
# Logging
accesslog = "-" # stdout
errorlog = "-" # stderr
loglevel = "info"
# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
# Process naming
proc_name = "django_app"
# Preload application for faster worker spawning
preload_app = True
