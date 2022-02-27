from django import template

from app.core.models import NavigationSettings

register = template.Library()


@register.inclusion_tag("tags/navbar.html", takes_context=True)
def navbar(context, current_page):
    request = context.get("request")
    navigation = [
        {
            "title": item.value.title,
            "url": item.value.url,
            "is_current": "active" if not item.value.url == request.path else "",
            "link_class": "color-contrast-high"
            if item.value.url == request.path
            else "",
        }
        for item in NavigationSettings.for_request(request).menu_items
    ]
    return {
        "request": request,
        "navigation": navigation,
        "current_page_id": current_page.id if current_page else None,
    }
