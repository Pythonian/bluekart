from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["quantity"].widget.attrs.update(
        #     {"class": "form-select d-inline w-25"}
        # )

    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=""
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
