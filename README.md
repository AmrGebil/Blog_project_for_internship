# Blog project for internship
This project is a blog API built using Django Rest Framework.

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the server using `python manage.py runserver`.

## Usage

The API provides the following endpoints:

- `/`: Returns user information.
- `/register/`:  Creates a user account.
- `/login/`: Allows users to log in and returns an authentication token.
- `/logout/`: Logs the user out.
- `/profile/`:Returns, edits, and deletes user profiles.
- `/post/`: Creates posts and returns a list of all posts.
- `/post/<id>/`:Returns a specific post and allows editing or deletion.

- `/post/Tags/`: Returns a list of tags

- `/post/<id>/comment`: Returns a list of comments for a specific post and allows comment creation.
- `/post/<id>/comment/<id>`: Returns a specific comment and allows editing or deletion.
  
- `/post/<id>/like_dislike/`: Allows users to like or dislike a specific post.
-  `/post/<id>/like_dislike/<id>`: Returns a user's like or dislike status for a post and allows editing, changing, or deletion.
   
 - `/post/bookmarks/create/`: Creates bookmarks for a specific post.
- `/post/bookmarks/list/`: Returns a list of bookmarks.
- `/post/bookmarks/<id>/`: Deletes a specific bookmark.

