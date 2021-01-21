from rest_framework.pagination import PageNumberPagination

from core import settings


class DefaultPagination(PageNumberPagination):
    page_size = settings.DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = settings.MAX_PAGE_SIZE
