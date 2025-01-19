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

    