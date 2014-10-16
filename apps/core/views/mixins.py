from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)
