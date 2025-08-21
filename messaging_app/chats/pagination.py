from rest_framework import PageNumberPagination
import math
class MessageFilter(PageNumberPagination):
  page= 20            # number of messages per page
  page_size_query_param = 'page_size'  # optional, let client override
  max_page_size = 100       # prevent abuse
  page = page.paginator.count(20)