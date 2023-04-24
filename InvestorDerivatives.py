from settrade_v2 import Investor
from settrade_v2.errors import SettradeError


class INVESTOR_DERIVATIVES:

    def account_info(investor,account_no):
        try:
            deri = investor.Derivatives(account_no=account_no)
            account_info = deri.get_account_info()
            #0
            callForceFlag = account_info.get('callForceFlag') #1
            callForceMargin = account_info.get('callForceMargin') #2
            callForceMarginMM = account_info.get('callForceMarginMM') #3
            cashBalance = account_info.get('cashBalance') #4
            closingMethod = account_info.get('closingMethod') #5
            creditLine = account_info.get('creditLine') #6
            depositWithdrawal = account_info.get('depositWithdrawal') #7
            equity = account_info.get('equity') #8
            excessEquity = account_info.get('excessEquity') #9
            initialMargin = account_info.get('initialMargin') #10
            liquidationValue = account_info.get('liquidationValue') #11
            totalFM = account_info.get('totalFM') #12
            totalMM = account_info.get('totalMM') #13
            totalMR = account_info.get('totalMR') #14

            return f'1,{callForceFlag},{callForceMargin},{callForceMarginMM},{cashBalance},{closingMethod},{creditLine},{depositWithdrawal},{equity},{excessEquity},{initialMargin},{liquidationValue},{totalFM},{totalMM},{totalMR}'
        except SettradeError as e:
            return f'0,{e.code},{e}'
        
    
    def get_order(investor,account_no,order_no):
        try:
            deri = investor.Derivatives(account_no=account_no)
            order_info = deri.get_order(order_no=order_no)

            #0
            accountNo = order_info.get('accountNo') #1
            balanceQty = order_info.get('balanceQty') #2
            canCancel = order_info.get('canCancel') #3
            canChange = order_info.get('canChange') #4
            cancelId = order_info.get('cancelId') #5
            cancelQty = order_info.get('cancelQty') #6
            cancelTime = order_info.get('cancelTime') #7
            cpm = order_info.get('cpm') #8
            entryId = order_info.get('entryId') #9
            entryTime = order_info.get('entryTime') #10
            icebergVol = order_info.get('icebergVol') #11
            isStopOrderNotActivate = order_info.get('isStopOrderNotActivate') #12
            matchQty = order_info.get('matchQty') #13
            orderNo = order_info.get('orderNo') #14
            position = order_info.get('position') #15
            price = order_info.get('price') #16
            priceDigit = order_info.get('priceDigit') #17
            priceType = order_info.get('priceType') #18
            qty = order_info.get('qty') #19
            rejectCode = order_info.get('rejectCode') #20
            rejectReason = order_info.get('rejectReason') #21
            showStatus = order_info.get('showStatus') #22
            side = order_info.get('side') #23
            status = order_info.get('status') #24
            statusMeaning = order_info.get('statusMeaning') #25
            symbol = order_info.get('symbol') #26
            terminalType = order_info.get('terminalType') #27
            tfxOrderNo = order_info.get('tfxOrderNo') #28
            trType = order_info.get('trType') #29
            tradeDate = order_info.get('tradeDate') #30
            transactionTime = order_info.get('transactionTime') #31
            triggerCondition = order_info.get('triggerCondition') #32
            triggerPrice = order_info.get('triggerPrice') #33
            triggerSession = order_info.get('triggerSession') #34
            triggerSymbol = order_info.get('triggerSymbol') #35
            validToDate = order_info.get('validToDate') #36
            validity = order_info.get('validity') #37
            version = order_info.get('version') #38

            return f'1,{accountNo},{balanceQty},{canCancel},{canChange},{cancelId},{cancelQty},{cancelTime},{cpm},{entryId},{entryTime},{icebergVol},{isStopOrderNotActivate},{matchQty},{orderNo},{position},{price},{priceDigit},{priceType},{qty},{rejectCode},{rejectReason},{showStatus},{side},{status},{statusMeaning},{symbol},{terminalType},{tfxOrderNo},{trType},{tradeDate},{transactionTime},{triggerCondition},{triggerPrice},{triggerSession},{triggerSymbol},{validToDate},{validity},{version}'
        except SettradeError as e:
            return f'0,{e.code},{e}'


    def get_orders(investor,account_no):
        try:
            deri = investor.Derivatives(account_no=account_no)
            order_list = deri.get_orders()
            orderNo = ''
            for i in range(len(order_list)):

                #0
                if(i==0):
                   orderNo = str(order_list[i].get('orderNo')) #1     
                
                else:
                   orderNo += ',' +str(order_list[i].get('orderNo')) #1   

            return f'1,{orderNo}'
        except SettradeError as e:
            return f'0,{e.code},{e}'


    def palce_order(investor,account_no,pin,symbol,side,position,price_type,price,volume):
        try:
            deri = investor.Derivatives(account_no=account_no)
            place_order = deri.place_order(
                pin=pin,
                symbol = symbol,
                side = side,
                position = position,
                price_type = price_type,
                price = price,
                volume = volume,
            )

            accountNo = place_order.get('accountNo')
            balanceQty = place_order.get('balanceQty')
            canCancel = place_order.get('canCancel')
            canChange = place_order.get('canChange')
            cancelId = place_order.get('cancelId')
            cancelQty = place_order.get('cancelQty')
            cancelTime = place_order.get('cancelTime')
            cpm = place_order.get('cpm')
            entryId = place_order.get('entryId')
            entryTime = place_order.get('entryTime')
            icebergVol = place_order.get('icebergVol')
            isStopOrderNotActivate = place_order.get('isStopOrderNotActivate')
            matchQty = place_order.get('matchQty')
            orderNo = place_order.get('orderNo')
            Position = place_order.get('position')
            Price = place_order.get('price')
            priceDigit = place_order.get('priceDigit')
            priceType = place_order.get('priceType')
            qty = place_order.get('qty')
            rejectCode = place_order.get('rejectCode')
            rejectReason = place_order.get('rejectReason')
            showStatus = place_order.get('showStatus')
            Side = place_order.get('side')
            status = place_order.get('status')
            statusMeaning = place_order.get('statusMeaning')
            Symbol = place_order.get('symbol')
            terminalType = place_order.get('terminalType')
            tfxOrderNo = place_order.get('tfxOrderNo')
            trType = place_order.get('trType')
            tradeDate = place_order.get('tradeDate')
            transactionTime = place_order.get('transactionTime')
            triggerCondition = place_order.get('triggerCondition')
            triggerPrice = place_order.get('triggerPrice')
            triggerSession = place_order.get('triggerSession')
            triggerSymbol = place_order.get('triggerSymbol')
            validToDate = place_order.get('validToDate')
            validity = place_order.get('validity')
            version = place_order.get('version')
            return f'1,{accountNo},{balanceQty},{canCancel},{canChange},{cancelId},{cancelQty},{cancelTime},{cpm},{entryId},{entryTime},{icebergVol},{isStopOrderNotActivate},{matchQty},{orderNo},{Position},{Price},{priceDigit},{priceType},{qty},{rejectCode},{rejectReason},{showStatus},{Side},{status},{statusMeaning},{Symbol},{terminalType},{tfxOrderNo},{trType},{tradeDate},{transactionTime},{triggerCondition},{triggerPrice},{triggerSession},{triggerSymbol},{validToDate},{validity},{version}'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
        

    def change_order(investor,account_no,pin,order_no,new_price,new_volume):
        try:
            order_no = int(order_no)
            deri = investor.Derivatives(account_no=account_no)
            change_order = deri.change_order(
            pin=pin,
            order_no=order_no,
            new_price=new_price,
            new_volume=new_volume,
            bypass_warning=True,
            )
            return f'1'
        except  SettradeError as e:
            return f'0,{e.code},{e}'

    def cancel_order(investor,account_no,order_no,pin):
        try:
            deri = investor.Derivatives(account_no=account_no)
            #convert order_no (str) to (int)
            order_no = int(order_no)
            cancel_order = deri.cancel_order(order_no=order_no, pin=pin)
            return f'1'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
            
    def cancel_orders(investor,account_no,order_no,pin):
        try:
            deri = investor.Derivatives(account_no=account_no)
            #convert order_no (str) to (int)
            for i in range(len(order_no)):
                order_no[i] = int(order_no[i])
            cancel_orders = deri.cancel_orders(order_no=order_no, pin=pin)
            return f'1'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
