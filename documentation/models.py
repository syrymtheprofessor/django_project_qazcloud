from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.http import HttpResponseRedirect
from django import forms

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

class DocumentationView(Page): 
    content_panels = Page.content_panels + [
        InlinePanel('document', label='Документы'),
    ]
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        docs = Document.objects.all()        

        for doc in docs:
            doc.filetype = str(doc.file).split('.')[-1][:3]
        
        context['docs'] = docs
        return context

class Document(Orderable):
    parent = ParentalKey(DocumentationView, related_name='document', on_delete=models.CASCADE, null=True, blank=False)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="documentation")
    date = models.DateTimeField(default=timezone.now)

    panels = [
        FieldPanel('name'),
        FieldPanel('date'),
        FieldPanel('file'),
    ]