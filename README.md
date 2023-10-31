# Blog project for internship
This project is a blog API built using Django Rest Framework.

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the server using `python manage.py runserver`.

## Usage

The API provides the following endpoints:

- `http://127.0.0.1:8000/`: Returns  user info.
- `/register/`: create user account. 
- `/login/`: user login and return token.
- `/logout/`: user logout.
- `/profile/`: Returns,edit and delete user profile
- `/post/`: create and Returns a list of all posts.
- `/post/<id>/`: Returns a specific post and edite or delete it.

- `/post/Tags/`: Returns a list of tags

- `/post/<id>/comment`: Returns list and create comments for special post.
- `/post/<id>/comment/<id>`: Returns a specific comment and edite or delete it.
  
- `/post/<id>/like_dislike/`: create like or dislike for special post .
-  `/post/<id>/like_dislike/<id>`: return like or dislike of user and edit or change or delete it  .
   
 - `/post/bookmarks/create/`: create bookmarks for special post .
- `/post/bookmarks/list/`: Returns a list of bookmarks.
- `/post/bookmarks/<id>/`: delete special bookmark.

