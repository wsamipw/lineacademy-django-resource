from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='article/',
                              default='default.jpg', blank=True, null=True)
    date = models.DateTimeField()
    content = models.TextField()
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Hero(models.Model):
    image = models.ImageField(upload_to='hero/', default='default.jpg')
    caption = models.CharField(max_length=250)
    sub_heading = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.caption


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None)
    photographer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story/', default='default.jpg')
    date = models.DateTimeField()
    content = models.TextField()
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

   def get_absolute_url(self):
    #    return "story/%s"%(self.slug)
       return reverse("home:storyDetail", kwargs={"slug": self.slug})
    


    class Meta:
        ordering = ["-date"]
        verbose_name = "My Story"
        verbose_name_plural = "My Stories"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug

    qs = Story.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    instance.slug = create_slug(instance)
    # do other stuffs here


pre_save.connect(pre_save_post_receiver, sender=Story)
