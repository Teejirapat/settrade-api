from settrade_v2 import Investor
from settrade_v2.errors import SettradeError


class INVESTOR_DERIVATIVES:

    def account_info(investor,account_no):
        try:
            deri = investor.Derivatives(account_no=account_no)
            account_info = deri.get_account_info()
            #0
            callForceFlag = account_info['callForceFlag'] #1
            callForceMargin = account_info['callForceMargin'] #2
            callForceMarginMM = account_info['callForceMarginMM'] #3
            cashBalance = account_info['cashBalance'] #4
            closingMethod = account_info['closingMethod'] #5
            creditLine = account_info['creditLine'] #6
            depositWithdrawal = account_info['depositWithdrawal'] #7
            equity = account_info['equity'] #8
            excessEquity = account_info['excessEquity'] #9
            initialMargin = account_info['initialMargin'] #10
            liquidationValue = account_info['liquidationValue'] #11
            totalFM = account_info['totalFM'] #12
            totalMM = account_info['totalMM'] #13
            totalMR = account_info['totalMR'] #14

            return f'1,{callForceFlag},{callForceMargin},{callForceMarginMM},{cashBalance},{closingMethod},{creditLine},{depositWithdrawal},{equity},{excessEquity},{initialMargin},{liquidationValue},{totalFM},{totalMM},{totalMR}'
        except SettradeError as e:
            return f'0,{e.code},{e}'
        
    
    def get_order(investor,account_no,order_no):
        try:
            deri = investor.Derivatives(account_no=account_no)
            order_info = deri.get_order(order_no=order_no)

            #0
            accountNo = order_info['accountNo'] #1
            balanceQty = order_info['balanceQty'] #2
            canCancel = order_info['canCancel'] #3
            canChange = order_info['canChange'] #4
            cancelId = order_info['cancelId'] #5
            cancelQty = order_info['cancelQty'] #6
            cancelTime = order_info['cancelTime'] #7
            cpm = order_info['cpm'] #8
            entryId = order_info['entryId'] #9
            entryTime = order_info['entryTime'] #10
            icebergVol = order_info['icebergVol'] #11
            isStopOrderNotActivate = order_info['isStopOrderNotActivate'] #12
            matchQty = order_info['matchQty'] #13
            orderNo = order_info['orderNo'] #14
            position = order_info['position'] #15
            price = order_info['price'] #16
            priceDigit = order_info['priceDigit'] #17
            priceType = order_info['priceType'] #18
            qty = order_info['qty'] #19
            rejectCode = order_info['rejectCode'] #20
            rejectReason = order_info['rejectReason'] #21
            showStatus = order_info['showStatus'] #22
            side = order_info['side'] #23
            status = order_info['status'] #24
            statusMeaning = order_info['statusMeaning'] #25
            symbol = order_info['symbol'] #26
            terminalType = order_info['terminalType'] #27
            tfxOrderNo = order_info['tfxOrderNo'] #28
            trType = order_info['trType'] #29
            tradeDate = order_info['tradeDate'] #30
            transactionTime = order_info['transactionTime'] #31
            triggerCondition = order_info['triggerCondition'] #32
            triggerPrice = order_info['triggerPrice'] #33
            triggerSession = order_info['triggerSession'] #34
            triggerSymbol = order_info['triggerSymbol'] #35
            validToDate = order_info['validToDate'] #36
            validity = order_info['validity'] #37
            version = order_info['version'] #38

            return f'1,{accountNo},{balanceQty},{canCancel},{canChange},{cancelId},{cancelQty},{cancelTime},{cpm},{entryId},{entryTime},{icebergVol},{isStopOrderNotActivate},{matchQty},{orderNo},{position},{price},{priceDigit},{priceType},{qty},{rejectCode},{rejectReason},{showStatus},{side},{status},{statusMeaning},{symbol},{terminalType},{tfxOrderNo},{trType},{tradeDate},{transactionTime},{triggerCondition},{triggerPrice},{triggerSession},{triggerSymbol},{validToDate},{validity},{version}'
        except SettradeError as e:
            return f'0,{e.code},{e}'


    def get_orders(investor,account_no):
        try:
            deri = investor.Derivatives(account_no=account_no)
            order_list = deri.get_orders()

            accountNo = ''
            balanceQty = ''
            canCancel = ''
            canChange = ''
            cancelId = ''
            cancelQty = ''
            cancelTime = ''
            cpm = ''
            entryId = ''
            entryTime = ''
            icebergVol = ''
            isStopOrderNotActivate = ''
            matchQty = ''
            orderNo = ''
            position = ''
            price = ''
            priceDigit = ''
            priceType = ''
            qty = ''
            rejectCode = ''
            rejectReason = ''
            showStatus = ''
            side = ''
            status = ''
            statusMeaning = ''
            symbol = ''
            terminalType = ''
            tfxOrderNo = ''
            trType = ''
            tradeDate = ''
            transactionTime = ''
            triggerCondition = ''
            triggerPrice = ''
            triggerSession = ''
            triggerSymbol = ''
            validToDate = ''
            validity = ''
            version = ''
            for i in range(len(order_list)):

                #0
                accountNo += ',' +str(order_list[i]['accountNo']) #1
                balanceQty = order_list[i]['balanceQty'] #2
                canCancel = order_list[i]['canCancel'] #3
                canChange = order_list[i]['canChange'] #4
                cancelId = order_list[i]['cancelId'] #5
                cancelQty = order_list[i]['cancelQty'] #6
                cancelTime = order_list[i]['cancelTime'] #7
                cpm = order_list[i]['cpm'] #8
                entryId = order_list[i]['entryId'] #9
                entryTime = order_list[i]['entryTime'] #10
                icebergVol = order_list[i]['icebergVol'] #11
                isStopOrderNotActivate = order_list[i]['isStopOrderNotActivate'] #12
                matchQty = order_list[i]['matchQty'] #13
                orderNo = order_list[i]['orderNo'] #14
                position = order_list[i]['position'] #15
                price = order_list[i]['price'] #16
                priceDigit = order_list[i]['priceDigit'] #17
                priceType = order_list[i]['priceType'] #18
                qty = order_list[i]['qty'] #19
                rejectCode = order_list[i]['rejectCode'] #20
                rejectReason = order_list[i]['rejectReason'] #21
                showStatus = order_list[i]['showStatus'] #22
                side = order_list[i]['side'] #23
                status = order_list[i]['status'] #24
                statusMeaning = order_list[i]['statusMeaning'] #25
                symbol = order_list[i]['symbol'] #26
                terminalType = order_list[i]['terminalType'] #27
                tfxOrderNo = order_list[i]['tfxOrderNo'] #28
                trType = order_list[i]['trType'] #29
                tradeDate = order_list[i]['tradeDate'] #30
                transactionTime = order_list[i]['transactionTime'] #31
                triggerCondition = order_list[i]['triggerCondition'] #32
                triggerPrice = order_list[i]['triggerPrice'] #33
                triggerSession = order_list[i]['triggerSession'] #34
                triggerSymbol = order_list[i]['triggerSymbol'] #35
                validToDate = order_list[i]['validToDate'] #36
                validity = order_list[i]['validity'] #37
                version = order_list[i]['version'] #38

            return f'1,{accountNo},{balanceQty},{canCancel},{canChange},{cancelId},{cancelQty},{cancelTime},{cpm},{entryId},{entryTime},{icebergVol},{isStopOrderNotActivate},{matchQty},{orderNo},{position},{price},{priceDigit},{priceType},{qty},{rejectCode},{rejectReason},{showStatus},{side},{status},{statusMeaning},{symbol},{terminalType},{tfxOrderNo},{trType},{tradeDate},{transactionTime},{triggerCondition},{triggerPrice},{triggerSession},{triggerSymbol},{validToDate},{validity},{version}'
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

            accountNo = place_order['accountNo']
            balanceQty = place_order['balanceQty']
            canCancel = place_order['canCancel']
            canChange = place_order['canChange']
            cancelId = place_order['cancelId']
            cancelQty = place_order['cancelQty']
            cancelTime = place_order['cancelTime']
            cpm = place_order['cpm']
            entryId = place_order['entryId']
            entryTime = place_order['entryTime']
            icebergVol = place_order['icebergVol']
            isStopOrderNotActivate = place_order['isStopOrderNotActivate']
            matchQty = place_order['matchQty']
            orderNo = place_order['orderNo']
            Position = place_order['position']
            Price = place_order['price']
            priceDigit = place_order['priceDigit']
            priceType = place_order['priceType']
            qty = place_order['qty']
            rejectCode = place_order['rejectCode']
            rejectReason = place_order['rejectReason']
            showStatus = place_order['showStatus']
            Side = place_order['side']
            status = place_order['status']
            statusMeaning = place_order['statusMeaning']
            Symbol = place_order['symbol']
            terminalType = place_order['terminalType']
            tfxOrderNo = place_order['tfxOrderNo']
            trType = place_order['trType']
            tradeDate = place_order['tradeDate']
            transactionTime = place_order['transactionTime']
            triggerCondition = place_order['triggerCondition']
            triggerPrice = place_order['triggerPrice']
            triggerSession = place_order['triggerSession']
            triggerSymbol = place_order['triggerSymbol']
            validToDate = place_order['validToDate']
            validity = place_order['validity']
            version = place_order['version']
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
