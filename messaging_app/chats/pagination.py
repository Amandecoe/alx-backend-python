from rest_framework.pagination import PageNumberPagination
import math
class MessageFilter( PageNumberPagination):
  page= 20 # number of messages per page
  def paginated_response(self):           
      page_size_query_param = 'page_size'  # optional, let client override
      max_page_size = 100       # prevent abuse
      total_items = self.page.paginator.count    # total messages in queryset
      current_page = self.page.number            # current page number
      page_size = self.get_page_size(self.request)