# Try out my blog webpage this way:


* main page

> > python manage.py runserver

* other pages (from the Browser)

    * To see Detail about content database of id or primary of integer 1
    > http://127.0.0.1:8000/posts/1/

    * To see Detail about content database of id or primary of integer 2
    > http://127.0.0.1:8000/posts/2/

*  To run the tests:

> >python manage.py test

## Explanations to The Code of Exercises: Tasks 1 - 4 --> 

Explanation of Test Methods
test_post_content:

Verifies that the content of the created Post object matches the expected string.
test_post_title:

Verifies that the title of the created Post object matches the expected string.
test_post_list_view:

Sends a GET request to the post_list view.
Asserts the following:
HTTP status code is 200.
Response contains the title of the created post.
The correct template (post_list.html) is used.
test_post_detail_view:

Sends a GET request to the post_detail view with the ID of the created post.
Asserts the following:
HTTP status code is 200.
Response contains the content of the created post.
The correct template (post_detail.html) is used.
test_post_list_template:

Specifically tests whether the post_list view uses the correct template (post_list.html).
test_post_detail_template:

Specifically tests whether the post_detail view uses the correct template (post_detail.html).

## Bonus Task

Explanation of Each Test
setUpTestData:

Creates three Post objects with unique titles and content to use in all test cases.
test_post_content:

Checks if the content of the first Post matches the expected string.
test_post_title:

Checks if the title of the second Post matches the expected string.
test_post_list_view:

Sends a GET request to the post_list URL.
Verifies the HTTP status code is 200.
Ensures the response contains the titles of all three posts.
test_post_detail_view:

Sends a GET request to the post_detail URL for the third post.
Verifies the HTTP status code is 200.
Ensures the response contains the content of the third post.
test_post_list_template:

Checks that the post_list.html template is used when accessing the post list view.
test_post_detail_template:

Checks that the post_detail.html template is used when accessing the post detail view.
Running the Tests
Run the tests with:

bash
Copy
Edit
python manage.py test
