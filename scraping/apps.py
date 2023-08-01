from django.apps import AppConfig


class ScrapingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scraping'
    verbose_name = "Приложения по сбору вакансии"
