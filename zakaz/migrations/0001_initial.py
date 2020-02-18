# Generated by Django 3.0.3 on 2020-02-12 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lots', '0004_article_favourite'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата публикации')),
                ('status', models.CharField(choices=[('draft', 'На рассмотрении'), ('win', 'Выигрыш'), ('sended', 'Заявка отправлено')], default='draft', max_length=10)),
                ('klyent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='klyent', to=settings.AUTH_USER_MODEL)),
                ('lot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lot', to='lots.Article')),
            ],
        ),
    ]
