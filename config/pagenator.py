from rest_framework.pagination import PageNumberPagination


class MyPagenator(PageNumberPagination):
    page_size = 25