from django.test import TestCase
from django.urls import reverse
from blog.models import Post  # blog is app name


# Create your tests here.

# Task 1. *Setting Up the Test Environment:*
#    - Create a new Django test case class named PostModelTests.
#    - Use the setUpTestData method to create a test Post object with the following data:
#      - title: "Test Post"
#      - content: "This is a test content."

class PostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a single test Post object
        cls.test_post = Post.objects.create(
            title="Test Post", content="This is a test content."
        )

    def test_post_creation(self):
        # Test that the Post object is created correctly
        self.assertEqual(self.test_post.title, "Test Post")
        self.assertEqual(self.test_post.content, "This is a test content.")

    # Task 2. *Writing Model Tests:*
    #    - Write a test method named test_post_content that checks if the content of the created Post object matches "This is a test content."
    #    - Write a test method named test_post_title that checks if the title of the created Post object matches "Test Post."

    def test_post_content(self):
        """Test if the Post content matches the expected value."""
        self.assertEqual(self.test_post.content, "This is a test content.")

    def test_post_title(self):
        """Test if the Post title matches the expected value."""
        self.assertEqual(self.test_post.title, "Test Post")

    # 3. *Testing the Views:*
    #    - Write a test method named test_post_list_view that checks if the URL for the post list view (e.g., /posts/) returns a 200 HTTP status code.
    #    - Write a test method named test_post_detail_view that checks if the URL for the post detail view (e.g., /posts/1/) returns a 200 HTTP status code and displays the correct content "This is a test content."

    def test_post_list_view(self):
        """Test if the post list view returns a 200 HTTP status code."""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")  # Ensures the title is displayed in the list

    def test_post_detail_view(self):
        """Test if the post detail view returns a 200 HTTP status code and displays correct content."""
        response = self.client.get(reverse('post_detail', args=[self.test_post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is a test content.")  # Verifies the content of the detail view

    # 4. *Testing the Templates:*
    #    - Write a test method named test_post_list_template that checks if the correct template is used for the post list view (post_list.html).
    #    - Write a test method named test_post_detail_template that checks if the correct template is used for the post detail view (post_detail.html).

    def test_post_list_template(self):
        """Test if the correct template is used for the post list view."""
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_list.html')  # Verify the correct template is used

    def test_post_detail_template(self):
        """Test if the correct template is used for the post detail view."""
        response = self.client.get(reverse('post_detail', args=[self.test_post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')  # Verify the correct template is used

# mmmmmmmmmmmmmmmmmmmmmmmm *Bonus Task:* mmmmmmmmmmmmmmmmmmmmmm
#
# mmmmmmmmmmmmmmmmmmmmm The Question  starts Here mmmmmmmmmmmmm
# - Modify your setUpTestData to create multiple Post objects and update your test methods to check for the presence of multiple posts in the post list view.
# 2:03
# *Sample Test Class (Skeleton):*
# python
# from django.test import TestCase
# from django.urls import reverse
# from .models import Post

# class PostModelTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Create test data here
#         cls.post = Post.objects.create(title="Test Post", content="This is a test content.")

#     def test_post_content(self):
#         # Test content here
#         pass

#     def test_post_title(self):
#         # Test title here
#         pass

#     def test_post_list_view(self):
#         # Test post list view here
#         pass

#     def test_post_detail_view(self):
#         # Test post detail view here
#         pass

#     def test_post_list_template(self):
#         # Test post list template here
#         pass

#     def test_post_detail_template(self):
#         # Test post detail template here
#         pass
# Complete this skeleton with your test logic, run the tests, and check if all of them pass!


# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm *Bonus Task:* The Question Ends Here mmmmmmmmmmmmmmmmmmmmmmmmmmmmm

class PostModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create multiple test Post objects
        cls.posts = [
            Post.objects.create(title="Test Post 1", content="Content for post 1."),
            Post.objects.create(title="Test Post 2", content="Content for post 2."),
            Post.objects.create(title="Test Post 3", content="Content for post 3."),
        ]

    def test_post_content(self):
        """Test if the content of the posts matches the expected content."""
        post = self.posts[0]
        self.assertEqual(post.content, "Content for post 1.")

    def test_post_title(self):
        """Test if the title of the posts matches the expected title."""
        post = self.posts[1]
        self.assertEqual(post.title, "Test Post 2")

    def test_post_list_view(self):
        """Test if the post list view displays all posts."""
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post 1")
        self.assertContains(response, "Test Post 2")
        self.assertContains(response, "Test Post 3")

    def test_post_detail_view(self):
        """Test if the post detail view displays the correct content for a specific post."""
        post = self.posts[2]  # Test the third post
        response = self.client.get(reverse("post_detail", args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Content for post 3.")

    def test_post_list_template(self):
        """Test if the correct template is used for the post list view."""
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")

    def test_post_detail_template(self):
        """Test if the correct template is used for the post detail view."""
        post = self.posts[0]
        response = self.client.get(reverse("post_detail", args=[post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
