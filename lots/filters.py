import django_filters

from lots.models import Article

class ArticleFilter(django_filters.FilterSet):
	class Meta:
		model = Article
		fields = ('title','body','id', 'city',)
