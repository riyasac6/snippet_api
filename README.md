# snippet_api
Develop a text saving and retrieval web app using Django. The app should be able to save short text snippets with a title, timestamp and created user. The snippet should also contain a relation to a Tag model (simple model with only title field). Tag title should be unique. Implement JWT authentication for getting user.

Authentication API:
----------
	1. Login API
	2. Refresh API

CRUD APIs:
----------
	1. Overview API (total count, listing)
		Total number of snippet and list all available snippets with a hyperlink to respective detail APIs.
	2. Create API
		API to collect the snippet information and save the data to DB.
	3. Detail API
		API should display the snippet title, content, and timestamp information.
	4. Update API
		API to update individual items. Update API should return item detail response.
	5. Delete API
		API to delete selected items and return the list of items as response.
	6. Tag list API
		API to list tags
	7. Tag Detail API
		API to return snippets linked to the selected tag.


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

