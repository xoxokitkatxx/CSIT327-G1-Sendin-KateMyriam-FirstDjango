from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser


class BootstrapFormMixin:
    """Applies Bootstrap 5 classes and placeholders to all form fields."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            widget = field.widget
            base_class = "form-select" if isinstance(widget, forms.Select) else "form-control"
            if self.is_bound and name in self.errors:
                base_class = f"{base_class} is-invalid"
            widget.attrs["class"] = base_class
            widget.attrs.setdefault("placeholder", field.label)


class CustomAuthenticationForm(BootstrapFormMixin, AuthenticationForm):
    """Login form with Bootstrap 5 widget styling."""
    pass


class CustomUserCreationForm(BootstrapFormMixin, UserCreationForm):
    """Sign-up form for creating a CustomUser with Bootstrap 5 widget styling."""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")


class ProfileUpdateForm(BootstrapFormMixin, forms.ModelForm):
    """Form for logged-in users to edit their own profile fields safely."""

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "course")