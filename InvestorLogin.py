from settrade_v2 import Investor
from settrade_v2.errors import SettradeError


class INVESTOR_LOGIN:
    def login(app_id,app_secret,broker_id,app_code):
        try:
            investor = Investor(
                            app_id=app_id,                                 
                            app_secret=app_secret, 
                            broker_id=broker_id,
                            app_code=app_code,
                            is_auto_queue = False)
            
            print("---- login Success ----")
            return {
                'status_code':1,
                'code':investor,
                'message':'Success'
                    }
        except SettradeError as e:
            print("---- error login  ----")
            print("---- check your config.txt ----")
            print(e)
            return {
                'status_code':e.status_code,
                'code':e.code,
                'message':e
                    }