from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from kosakata.models import Kosakata
from data_uji.models import DataUji
from django.db.models import Q

import functools
import operator

class KosakataDataTables(BaseDatatableView):
    # The model we're going to show
    model = Kosakata

    # define the columns that will be returned
    columns = ['id', 'kata', 'arti_kata']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['id', 'kata', 'arti_kata']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500


    def render_column(self, row, column):
        # # We want to render user as a custom column
        # if column == 'user':
        #     # escape HTML for security reasons
        #     return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
        # else:
        return super(KosakataDataTables, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        lookups = [
            'id__istartswith',
            'kata__istartswith',
            'arti_kata__istartswith',
        ]

        or_queries = [Q(**{lookup: search}) for lookup in lookups]


        if search:
            qs = qs.filter(functools.reduce(operator.or_, or_queries))

        # more advanced example using extra parameters
        # filter_customer = self.request.GET.get('customer', None)

        # if filter_customer:
        #     customer_parts = filter_customer.split(' ')
        #     qs_params = None
        #     for part in customer_parts:
        #         q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
        #         qs_params = qs_params | q if qs_params else q
        #     qs = qs.filter(qs_params)
        return qs



class DataUjiDataTables(BaseDatatableView):
    # The model we're going to show
    model = DataUji

    # define the columns that will be returned
    columns = ['id', 'raw_data', 'cleaned_data', 'stemmed_data']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns =  ['id', 'raw_data', 'cleaned_data', 'stemmed_data']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500


    def render_column(self, row, column):
        # # We want to render user as a custom column
        # if column == 'user':
        #     # escape HTML for security reasons
        #     return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
        # else:
        return super(DataUjiDataTables, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        lookups = [
            'id__istartswith',
            'raw_data__istartswith',
            'cleaned_data__istartswith',
            'stemmed_data__istartswith',
        ]

        or_queries = [Q(**{lookup: search}) for lookup in lookups]


        if search:
            qs = qs.filter(functools.reduce(operator.or_, or_queries))

        # more advanced example using extra parameters
        # filter_customer = self.request.GET.get('customer', None)

        # if filter_customer:
        #     customer_parts = filter_customer.split(' ')
        #     qs_params = None
        #     for part in customer_parts:
        #         q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
        #         qs_params = qs_params | q if qs_params else q
        #     qs = qs.filter(qs_params)
        return qs
