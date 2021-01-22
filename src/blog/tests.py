from django.test import TestCase
from blog.models import Writer, Article
from django.contrib.auth.models import User

# Create your tests here.


class WriterTestCase(TestCase):

    def test_user_creation(self):

        username = "Shakespeare"
        password = "booksToday"
        User.objects.create(username=username, password=password)
        user = User.objects.get(username=username)
        self.assertEqual(user.username, username)

    def test_writer_creation(self):
        username = "Shakespeare"
        password = "booksToday"
        test_user = User.objects.create(username=username, password=password)

        name = "Shakespeare"
        is_editor = True

        shakespeare = Writer.objects.create(
            user=test_user,
            name=name,
            is_editor=is_editor
        )
        self.assertEqual(shakespeare.name, name)
        self.assertEqual(shakespeare.is_editor, is_editor)


class ArticleTestCase(TestCase):

    def test_article_creation(self):

        username = "Shakespeare"
        password = "booksToday"
        test_user = User.objects.create(username=username, password=password)

        name = "Shakespeare"
        is_editor = True

        article_name = "Hamlet"
        content = """
        The Tragedy of Hamlet, Prince of Denmark, often shortened to Hamlet \
        , is a tragedy written by William Shakespeare sometime between 1599 \
        and 1601. It is Shakespeare's longest play, with 30,557 words. Set \
        in Denmark, the play depicts Prince Hamlet and his revenge \
        against his uncle, Claudius, who has murdered Hamlet's father \
        in order to seize his throne and marry Hamlet's mother.
        """

        shakespeare = Writer.objects.create(
            user=test_user,
            name=name,
            is_editor=is_editor
        )
        article = Article(
            title=article_name,
            content=content,
            written_by=shakespeare,
            edited_by=shakespeare
        )

        self.assertEqual(article.title, article_name)
        self.assertEqual(article.content, content)
