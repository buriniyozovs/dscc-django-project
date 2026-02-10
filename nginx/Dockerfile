FROM nginx:alpine
# Remove default config
RUN rm /etc/nginx/conf.d/default.conf
# Copy custom config
COPY nginx.conf /etc/nginx/conf.d/
# Health check
HEALTHCHECK --interval=30s --timeout=3s \
 CMD wget --quiet --tries=1 --spider http://localhost/health/ || exit 1