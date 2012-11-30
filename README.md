Gluebox
===

requirements: django 1.4

Enable edit mode for an user
---
add user to the group EDITORS to activate the inline content editing.

django 1.3 users
---
Inside templates,REquestContext provide a user instrance isntead of request.user.
cfr https://docs.djangoproject.com/en/dev/topics/auth/#id8

SQlite3 users
---
Make sure Apache can also write to the parent directory of the database. SQLite needs to be able to write to this directory.
