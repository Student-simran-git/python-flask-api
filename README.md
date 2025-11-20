Project: Simple Flask REST API (User management)
Objective: Implement CRUD endpoints and demonstrate tests via terminal (curl).

Files:
- app.py : Flask application with GET/POST/PUT/DELETE for /users

How to run:
1. python app.py
2. Open a new terminal and use curl commands.

Commands used (PowerShell):
1) GET before:
   curl http://127.0.0.1:5000/users

2) POST (add user):
   curl -Method POST "http://127.0.0.1:5000/users" -Headers @{ "Content-Type"="application/json" } -Body '{"name":"Simran","email":"sim@gmail.com"}'

3) GET after:
   curl http://127.0.0.1:5000/users

4) PUT (update) or DELETE:
   curl -Method PUT "http://127.0.0.1:5000/users/1" -Headers @{ "Content-Type"="application/json" } -Body '{"email":"updated@gmail.com"}'
   OR
   curl -Method DELETE "http://127.0.0.1:5000/users/1"

Screenshots included:
- 01_get_before.png
- 02_post_add.png
- 03_get_after.png
- 04_put_update.png (or 04_delete.png)

Conclusion:
API works correctly. CRUD operations demonstrated using terminal (curl). Server run: http://127.0.0.1:5000
