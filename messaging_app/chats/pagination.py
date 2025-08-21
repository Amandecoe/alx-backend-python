from rest_framework import PageNumberPagination

class MessageFilter(PageNumberPagination):
  page_size = 20            # number of messages per page
  page_size_query_param = 'page_size'  # optional, let client override
  max_page_size = 100       # prevent abuse