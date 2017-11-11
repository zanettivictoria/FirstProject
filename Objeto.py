from blog.models import Post
from django.contrib.auth.models import User

Post.objects.all()
Post.objectscreate(author=me, tittle='Titulo Simples', text= "Test")
User.objects.all()
me=User.objects.get(username='Vic)

