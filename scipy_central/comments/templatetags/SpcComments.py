from django import template
from django.contrib.comments.models import CommentFlag
from django.core.exceptions import ObjectDoesNotExist
from scipy_central.comments.forms import SpcCommentEditForm

register = template.Library()

@register.filter
def is_flagged(comment_obj, request):
    """
    Returns `True` if signed-in user flagged comment previously
    or else `False`
    """
    try:
        # if user is not authenticated
        if not request.user.is_authenticated():
            return False
        # if object present, return True
        CommentFlag.objects.get(comment=comment_obj, user=request.user)
        return True
    except (ObjectDoesNotExist):
        return False

@register.inclusion_tag('comments/edit-form.html')
def comment_edit_form(comment_object):
    """
    renders comment's edit form
    """
    form = SpcCommentEditForm(comment_object)
    context = {
        'form': form,
    }
    return context
