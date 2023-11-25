from django.db import models
from django.core.validators import MinLengthValidator
from .topic_model.mindmap import MindMap


class MindMapField(models.Field):
    description = 'A mind map structure to use to create the flow in the frontend'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_map(self, name, text):
        return MindMap(name, text)

class Project(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50)
    text = models.TextField(verbose_name='Text', validators=[MinLengthValidator(1000, 'Brainstorming is about generating as many ideas as possible. Add more to have a more productive mind map!')])
    mind_map = MindMapField()

    def save(self, *args, **kwargs):
        self.mind_map = MindMapField().create_map(self.name, self.text)
        super().save(*args, **kwargs)
    