from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # signals.py 내의 신호 처리기를 임포트
        import accounts.signals
