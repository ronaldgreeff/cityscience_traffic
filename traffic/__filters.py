from django_filters import rest_framework as filters
from traffic.models import Record

class RecordFilter(filters.FilterSet):
	class Meta:
		model = Record
		fields = ['road']