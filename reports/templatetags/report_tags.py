from django import template

register = template.Library()


@register.filter('clean', needs_autoescape=True)
@register.simple_tag
def clean(group_list):
    group_list = "".join(group_list)
    new_group_list = group_list[:-1].split(",")
    groups = []
    for string in new_group_list:
        groups.append(string[3:-1])
    return groups
