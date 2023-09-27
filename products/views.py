from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Product


def product_list(request):
    products = Product.active.all()[:6]

    template = "products.html"
    context = {
        "products": products,
    }
    return render(request, template, context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(
        category=product.category, available=True
    ).exclude(id=product.id)[:4]
    cart_product_form = CartAddProductForm()

    template = "products/detail.html"
    context = {
        "product": product,
        "related_products": related_products,
        "cart_product_form": cart_product_form,
    }

    return render(request, template, context)


# def product_detail(request, slug):
#     if request.user.is_authenticated:
#         if request.user.is_vendor:
#             product = get_object_or_404(Product, slug=slug)
#         else:
#             product = get_object_or_404(Product, slug=slug, is_approved=True)
#     else:
#         product = get_object_or_404(Product, slug=slug, is_approved=True)
#     cart_product_form = CartAddProductForm()
#     reviews = product.reviews.filter(is_visible=True)

# Check if the user has ordered for this item before
# so that only users who have ordered item can post review
# if request.user.is_authenticated:
#     try:
#         user_ordered_item = OrderItem.objects.filter(
#             user=request.user, product_id=product.id).exists()
#     except OrderItem.DoesNotExist:
#         user_ordered_item = None
# else:
#     user_ordered_item = None

# Get the review of the currently logged in user
# if request.user.is_authenticated:
#     try:
#         user_review = Review.objects.get(
#             user__id=request.user.id, product__slug=product.slug
#         )
#     except Review.DoesNotExist:
#         user_review = None
# else:
#     user_review = None

# if request.method == "POST":
#     review_form = ReviewForm(request.POST)
#     if review_form.is_valid():
#         review = review_form.save(commit=False)
#         review.user = request.user
#         review.product = product
#         review.ip = request.META.get("REMOTE_ADDR")
#         review.user_agent_data = request.META.get("HTTP_USER_AGENT")
#         review.save()
#         messages.success(request, "Thanks! Your review was submitted successfully.")
#         return redirect("products:detail", product.slug)
#     else:
#         messages.warning(
#             request, "An error occured while submitting your form, check below"
#         )
# else:
#     review_form = ReviewForm()

# similar_products = list(
#     product.category.products.filter(is_approved=True).exclude(id=product.id)
# )

# if len(similar_products) >= 4:
#     similar_products = random.sample(similar_products, 4)

# template_name = "products/detail.html"
# context = {
#     "product": product,
#     "cart_product_form": cart_product_form,
#     "reviews": reviews,
#     "user_review": user_review,
#     "review_form": review_form,
#     "similar_products": similar_products,
# }

# return render(request, template_name, context)
