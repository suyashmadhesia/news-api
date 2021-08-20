from rest_framework.pagination import CursorPagination
from rest_framework.response import Response

class FeedPaginator(CursorPagination):
    page = 1
    page_size = 5
    cursor_query_param = 'page_size'
    ordering = 'created_at'


    def get_paginated_response(self, data):
        next_link = self.get_next_link()
        if next_link is not None:
            next_link = next_link[next_link.index('?'):len(next_link)]
        return Response({
            'links' : {
                'next' : next_link,
                'previous' : self.get_next_link()
            },
            'posts' : data,
        })