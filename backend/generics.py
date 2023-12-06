from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.generics import ListAPIView as BaseListAPIView


class ListViewPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results_count": self.page.paginator.count,
                "pages_count": self.page.paginator.num_pages,
                "results": data,
            }
        )


class ListAPIView(BaseListAPIView):
    def get(self, request, *args, **kwargs):
        if request.query_params.get("pagination"):
            self.pagination_class = ListViewPagination
        return super().get(request, *args, **kwargs)


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance
