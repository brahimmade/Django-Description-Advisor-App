# from django_filters.rest_framework import filters
# from ...models import JobTitle


# class MyFilterBackend(filters.DjangoFilterBackend):
#     def get_filterset_kwargs(self, request, queryset, view):
#         kwargs = super().get_filterset_kwargs(request, queryset, view)

#         # merge filterset kwargs provided by view class
#         if hasattr(view, 'get_filterset_kwargs'):
#             kwargs.update(view.get_filterset_kwargs())

#         return kwargs


# class BookFilter(filters.FilterSet):
#     def __init__(self, *args, author=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         # do something w/ author

    
    