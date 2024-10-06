from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Notion(models.Model):
    title = models.CharField("Заметка", max_length=255)
    description = models.TextField(null=True, blank=True)
    when_to_note = models.DateTimeField()
    created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(to='Tag')
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        ordering = ['created']
        db_table = "notions"
        unique_together = (("title", "description", "when_to_note", "is_active"), )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField("Тег", max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        db_table = "tags"

    def __str__(self):
        return self.name
