import os

os.environ["DATABASE_URL"] = "postgresql:///blogly_test"

from unittest import TestCase

from app import app, db
from models import DEFAULT_IMAGE_URL, User

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client, add sample data."""

        # As you add more models later in the exercise, you'll want to delete
        # all of their records before each test just as we're doing with the
        # User model below.
        User.query.delete()

        self.client = app.test_client()

        test_user = User(
            first_name="test1_first",
            last_name="test1_last",
            image_url=None,
        )

        db.session.add(test_user)
        db.session.commit()
        # We can hold onto our test_user's id by attaching it to self (which is
        # accessible throughout this test class). This way, we'll be able to
        # rely on this user in our tests without needing to know the numeric
        # value of their id, since it will change each time our tests are run.
        self.user_id = test_user.id

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()

    def test_list_users(self):
        with self.client as c:
            resp = c.get("/users")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("test1_first", html)
            self.assertIn("test1_last", html)

    def test_homepage(self):
        """Test if homepage redirects to /users"""

        with self.client as client:
            response = client.get('/')

            # successfully redirects to /users
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location,'/users')

    def test_show_edit_user(self):
        """Test that edit form is shown on button click"""

        # test get request
        with self.client as client:
            response = client.get(f'/users/{self.user_id}/edit')
            html = response.get_data(as_text=True)

            # successfully redirects to /users
            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- Test: this is the edit user form -->', html)

    def test_edit_user(self):
        """Test that edit form is shown on button click"""

        # test get request
        with self.client as client:
            response = client.post(f'/users/{self.user_id}/edit')

            # TODO: test to see if info is successfully updated

            # successfully redirects to /users
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.location,'/users')

    def test_show_user(self):
        """Test that user info is shown on button click"""

        # test get request
        with self.client as client:
            response = client.get(f'/users/{self.user_id}')
            html = response.get_data(as_text=True)

            # successfully redirects to /users
            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- Test: this is the user page -->', html)


    def test_confirm_delete(self):
        """Test that delete confirmation page is shown on button click"""

        # test get request
        with self.client as client:
            response = client.get(f'/users/{self.user_id}/delete')
            html = response.get_data(as_text=True)

            # successfully redirects to /users
            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- Test: this is the delete confirmation page -->', html)