from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Agent(models.Model):
    slug = models.SlugField(
        default='',
        editable=False,
    )
    agent_name = models.CharField(max_length=250)
    agent_phonenumber = models.CharField(max_length=15)
    agent_email = models.EmailField()
    agent_location = models.CharField(max_length=50)

    def __str__(self):
        return self.agent_name

    def get_agent_url(self):
        return reverse('agent_edit', kwargs={'pk': self.pk, 'slug': self.slug})


    def save(self, *args, **kwargs):
        agent_slug = self.agent_name
        self.slug = slugify(agent_slug, allow_unicode=True)
        super().save(*args, **kwargs)

