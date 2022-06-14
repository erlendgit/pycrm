from django.urls import reverse
from django.utils.translation import gettext as _
from core.utils import MenuItem

MENU = {
    "main": MenuItem(_("Main menu")).with_children([
        MenuItem(_("Home"), url=reverse("core:home")),
        MenuItem(_("Date convert"), url=reverse("core:date_convert")),
        MenuItem(_("Entities"), url=reverse("crm:index"), perm=lambda user: user.is_authenticated),
    ]),
    'user': MenuItem(_("User menu")).with_children([
        MenuItem(_("Login"), url=reverse("user:login"), perm=lambda user: user.is_anonymous),
        MenuItem(_("Site administration"), url=reverse("admin:index"), perm=lambda user: user.is_superuser),
        MenuItem(_("Logout"), url=reverse("user:logout"), perm=lambda user: user.is_authenticated),
    ])
}
