from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.http import HttpResponseRedirect
from django import forms

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

# Create your models here.
class Article(Page):
    body = RichTextField()
    date = models.DateField("Post date")
    author = models.CharField(max_length=255, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('author'),
        FieldPanel('feed_image'),
    ]

    def get_context_data(self, request, *args, **kwargs):
            data = super().get_context_data(request, *args, **kwargs)
            comments_connected = ArticleComment.objects.filter(
                article_connected=self.get_object()
            )
            data["comments"] = comments_connected
            data["comment_form"] = NewCommentForm(instance=self.request.user)
            return data

    def post(self, request, *args, **kwargs):
        """
        There we receive comment from user and save it
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        new_comment = ArticleComment(
            content=request.POST.get("content"),
            author=request.POST.get("author"),
            author_email=request.POST.get("author_email"),
            article_connected=self.get_object(),
        )
        new_comment.save()
        return HttpResponseRedirect(self.request.path_info)

class BlogView(Page):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        # Add extra variables and return the updated context
        context['all_blogs'] = Article.objects.all()
        context['blog_entries'] = Article.objects.all()[:1]
        context['secondary'] = Article.objects.all()[1:3]
        context["triple_main"] = Article.objects.all()[3:4]
        context["triple_secondary"] = Article.objects.all()[4:6]
        context["bottom_two"] = Article.objects.all()[6:8]
        return context

class ArticleComment(models.Model):
    article_connected = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )
    author = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content", "author", "author_email"]
        widgets = {
            "content": forms.Textarea(
                attrs={"placeholder": "Добавить комментарии..."}
            ),
            "author": forms.TextInput(
                attrs={"placeholder": "Имя"}
            ),
            "author_email": forms.TextInput(
                attrs={"placeholder": "E-mail"}
            ),
        }