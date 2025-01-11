import __init__
from models.database import engine
from models.model import Subscription
from sqlmodel import Session, select
from datetime import date

class SubscriptionService:
    def __init__(self, engine):
        self.engine = engine

    def create(self, subscription: Subscription):
        with Session(self.engine) as session:
            session.add(subscription)
            session.commit()
            return subscription
        
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscription)
            result = session.exec(statement).all()
        return result             

        
ss = SubscriptionService(engine)
#subscription = Subscription(empresa='netflix', site='netflix.com.br', data_assinatura=date.today(), valor=25)
print(ss.list_all())