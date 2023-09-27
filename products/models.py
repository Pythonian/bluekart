from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.conf import settings

# User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    icon = models.FileField(
        upload_to="icons", validators=[FileExtensionValidator(["svg"])]
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category", args=[self.slug])


class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.PROTECT
    )
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=300, unique=True, db_index=True)
    image = models.ImageField(
        upload_to="products/%Y/%m/%d", default="products/default.jpg"
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    available = models.BooleanField(default=True)
    sku = models.CharField(max_length=10, unique=True)
    commission = models.PositiveIntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    objects = models.Manager()
    active = ProductManager()

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", args=[self.slug])


# class Review(models.Model):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name="reviews"
#     )
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
#     subject = models.CharField(max_length=100)
#     content = models.TextField(max_length=500)
#     rating = models.FloatField()
#     ip = models.GenericIPAddressField(blank=True, null=True)
#     user_agent_data = models.CharField(max_length=255, blank=True, null=True)
#     thumbsup = models.IntegerField(default="0")
#     thumbsdown = models.IntegerField(default="0")
#     thumbs = models.ManyToManyField(
#         User, related_name="thumbs", default=None, blank=True
#     )
#     is_visible = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ["-created"]

#     def __str__(self):
#         return self.subject


# class ReviewVote(models.Model):
#     review = models.ForeignKey(
#         Review,
#         related_name="reviewid",
#         on_delete=models.CASCADE,
#         default=None,
#         blank=True,
#     )
#     user = models.ForeignKey(
#         User, related_name="userid", on_delete=models.CASCADE, default=None, blank=True
#     )
#     vote = models.BooleanField(default=True)
