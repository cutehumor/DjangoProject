from django.db.models import Manager

class MyManager(Manager):
    def create_one(self, name, price):
        model = self.model()  # 实例化与对象管理器关联的对象
        model.name = name
        model.price = price
        model.save()
        return model

    def get_all(self):
        return super().all()
