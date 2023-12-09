# snippet_api
Develop a text saving and retrieval web app using Django. The app should be able to save short text snippets with a title, timestamp and created user. The snippet should also contain a relation to a Tag model (simple model with only title field). Tag title should be unique. Implement JWT authentication for getting user.

Clone Git
----------
git clone https://github.com/riyasac6/snippet_api.git

Run Docker 
----------
cd snippet_api/ && docker-compose -f docker-compose.yml up -d --build

Restore Database
---------
cd sql/ && cat snippet_db.sql | docker exec -i base-postgres psql -U postgres

Down and Up Docker
--------
cd ../ && docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d

Postman Collection
--------
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/18979185-d42cd73f-ba67-49a0-9438-d9f9d12eb6de?action=collection%2Ffork&collection-url=entityId%3D18979185-d42cd73f-ba67-49a0-9438-d9f9d12eb6de%26entityType%3Dcollection%26workspaceId%3D5d558899-993e-46ec-a937-f43f0f9e3a55)


Site Available URL: 
-------------------
http://127.0.0.1:8000/api-auth/login/

username : admin

password : As@1234

