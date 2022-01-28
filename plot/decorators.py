from functools import wraps
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden

def plot_permision_required(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if request.user.has_perm('plot.access_plot'):
             return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

  return wrap