from django import template

register=template.Library()

@register.filter(name='tags')
def tags(list_data,tags_size):
    tag=[]
    i=0
    for data in list_data:
        tag.append(data)
        i=i+1
        if i==tags_size:
            i=0
            yield tag
            tag=[]
    if tag:
        yield tag
