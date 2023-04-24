from settrade_v2 import Investor
from settrade_v2.errors import SettradeError


class INVESTOR_EQUITY:

    def account_info(investor,account_no):
        try:
            deri = investor.Equity(account_no=account_no)
            account_info = deri.get_account_info()
            #0
            accountType = account_info.get('accountType')
            actualCashBalance = account_info.get('actualCashBalance')
            actualMarginLoan = account_info.get('actualMarginLoan')
            asset = account_info.get('asset')
            availableCashBalance = account_info.get('availableCashBalance')
            availableMarginLoan = account_info.get('availableMarginLoan')
            buyMr = account_info.get('buyMr')
            callAmount = account_info.get('callAmount')
            callMargin = account_info.get('callMargin')
            canBuy = account_info.get('canBuy')
            canSell = account_info.get('canSell')
            cashBalance = account_info.get('cashBalance')
            clientType = account_info.get('clientType')
            cmAdjust = account_info.get('cmAdjust')
            collateral = account_info.get('collateral')
            creditBalance = account_info.get('creditBalance')
            creditLimit = account_info.get('creditLimit')
            crossingKey = account_info.get('crossingKey')
            customerType = account_info.get('customerType')
            equityBalance = account_info.get('equityBalance')
            excessEquity = account_info.get('excessEquity')
            fmAdjust = account_info.get('fmAdjust')
            forceAmount = account_info.get('forceAmount')
            forceMargin = account_info.get('forceMargin')
            imAdjust = account_info.get('imAdjust')
            liabilities = account_info.get('liabilities')
            lineAvail50 = account_info.get('lineAvail50')
            lineAvail60 = account_info.get('lineAvail60')
            lineAvail70 = account_info.get('lineAvail70')
            lineAvail80 = account_info.get('lineAvail80')
            lineAvailable = account_info.get('lineAvailable')
            longMarketValue = account_info.get('longMarketValue')
            marginCM = account_info.get('marginCM')
            marginFM = account_info.get('marginFM')
            marginIM = account_info.get('marginIM')
            mr = account_info.get('mr')
            mtmRealtime = account_info.get('mtmRealtime')
            percentMM = account_info.get('percentMM')
            purchasingPower = account_info.get('purchasingPower')
            valueForceSale = account_info.get('valueForceSale')


            return f'1,{accountType},{actualCashBalance},{actualMarginLoan},{asset},{availableCashBalance},{availableMarginLoan},{buyMr},{callAmount},{callMargin},{canBuy},{canSell},{cashBalance},{clientType},{cmAdjust},{collateral},{creditBalance},{creditLimit},{crossingKey},{customerType},{equityBalance},{excessEquity},{fmAdjust},{forceAmount},{forceMargin},{imAdjust},{liabilities},{lineAvail50},{lineAvail60},{lineAvail70},{lineAvail80},{lineAvailable},{longMarketValue},{marginCM},{marginFM},{marginIM},{mr},{mtmRealtime},{percentMM},{purchasingPower},{valueForceSale}'
        except SettradeError as e:
            return f'0,{e.code},{e}'
        
    
    def get_order(investor,account_no,order_no):
        try:
            deri = investor.Equity(account_no=account_no)
            order_info = deri.get_order(order_no=order_no)

            #0
            accountNo = order_info.get('accountNo')
            balance = order_info.get('balance')
            canCancel = order_info.get('canCancel')
            canChangeAccount = order_info.get('canChangeAccount')
            canChangePriceVol = order_info.get('canChangePriceVol')
            canChangeTrusteeId = order_info.get('canChangeTrusteeId')
            cancelId = order_info.get('cancelId')
            cancelTime = order_info.get('cancelTime')
            cancelled = order_info.get('cancelled')
            counterPartyMember = order_info.get('counterPartyMember')
            enterId = order_info.get('enterId')
            entryTime = order_info.get('entryTime')
            icebergVol = order_info.get('icebergVol')
            matched = order_info.get('matched')
            nvdrFlag = order_info.get('nvdrFlag')
            orderNo = order_info.get('orderNo')
            orderType = order_info.get('orderType')
            price = order_info.get('price')
            priceType = order_info.get('priceType')
            rejectCode = order_info.get('rejectCode')
            rejectReason = order_info.get('rejectReason')
            setOrderNo = order_info.get('setOrderNo')
            showOrderStatus = order_info.get('showOrderStatus')
            showOrderStatusMeaning = order_info.get('showOrderStatusMeaning')
            side = order_info.get('side')
            status = order_info.get('status')
            symbol = order_info.get('symbol')
            terminalType = order_info.get('terminalType')
            tradeDate = order_info.get('tradeDate')
            tradeReport = order_info.get('tradeReport')
            tradeReportType = order_info.get('tradeReportType')
            tradeTime = order_info.get('tradeTime')
            validTillDate = order_info.get('validTillDate')
            validity = order_info.get('validity')
            version = order_info.get('version')
            vol = order_info.get('vol')

            return f'1,{accountNo},{balance},{canCancel},{canChangeAccount},{canChangePriceVol},{canChangeTrusteeId},{cancelId},{cancelTime},{cancelled},{counterPartyMember},{enterId},{entryTime},{icebergVol},{matched},{nvdrFlag},{orderNo},{orderType},{price},{priceType},{rejectCode},{rejectReason},{setOrderNo},{showOrderStatus},{showOrderStatusMeaning},{side},{status},{symbol},{terminalType},{tradeDate},{tradeReport},{tradeReportType},{tradeTime},{validTillDate},{validity},{version},{vol}'
        except SettradeError as e:
            return f'0,{e.code},{e}'


    def get_orders(investor,account_no):
        try:
            deri = investor.Equity(account_no=account_no)
            order_list = deri.get_orders()
            print('order_list',order_list)
            orderNo = ''
            for i in range(len(order_list)):

                #0
                if(i==0):
                   if(order_list[i].get('orderNo') is not None):
                        orderNo = str(order_list[i].get('orderNo')) #1
                   else:
                       break
                
                else:
                   orderNo += ',' +str(order_list[i].get('orderNo')) #1     

                
            return f'1,{orderNo}'
        except SettradeError as e:
            return f'0,{e.code},{e}'


    def palce_order(investor,account_no,pin,symbol,side,price_type,price,volume):
        try:
            deri = investor.Equity(account_no=account_no)
            place_order = deri.place_order(
                pin=pin,
                symbol = symbol,
                side = side,
                price_type = price_type,
                price = price,
                volume = volume,
            )
            print('place_order',place_order)
            enterId = place_order.get("enterId")
            accountNo = place_order.get("accountNo")
            orderNo = place_order.get("orderNo")
            setOrderNo = place_order.get("setOrderNo")
            symbol = place_order.get("symbol")
            tradeDate = place_order.get("tradeDate")
            tradeTime = place_order.get("tradeTime")
            entryTime = place_order.get("entryTime")
            side = place_order.get("side")
            priceType = place_order.get("priceType")
            price = place_order.get("price")
            vol = place_order.get("vol")
            icebergVol = place_order.get("icebergVol")
            validity = place_order.get("validity")
            orderType = place_order.get("orderType")
            matched = place_order.get("matched")
            balance = place_order.get("balance")
            cancelled = place_order.get("cancelled")
            status = place_order.get("status")
            showOrderStatus = place_order.get("showOrderStatus")
            showOrderStatusMeaning = place_order.get("showOrderStatusMeaning")
            rejectCode = place_order.get("rejectCode")
            rejectReason = place_order.get("rejectReason")
            cancelId = place_order.get("cancelId")
            cancelTime = place_order.get("cancelTime")
            version = place_order.get("version")
            nvdrFlag = place_order.get("nvdrFlag")
            canChangeAccount = place_order.get("canChangeAccount")
            canChangeTrusteeId = place_order.get("canChangeTrusteeId")
            canChangePriceVol = place_order.get("canChangePriceVol")
            canCancel = place_order.get("canCancel")
            counterPartyMember = place_order.get("counterPartyMember")
            tradeReportType = place_order.get("tradeReportType")
            tradeReport = place_order.get("tradeReport")
            terminalType = place_order.get("terminalType")
            validTillDate = place_order.get("validTillDate")

            return f'1,{enterId},{accountNo},{orderNo},{setOrderNo},{symbol},{tradeDate},{tradeTime},{entryTime},{side},{priceType},{price},{vol},{icebergVol},{validity},{orderType},{matched},{balance},{cancelled},{status},{showOrderStatus},{showOrderStatusMeaning},{rejectCode},{rejectReason},{cancelId},{cancelTime},{version},{nvdrFlag},{canChangeAccount},{canChangeTrusteeId},{canChangePriceVol},{canCancel},{counterPartyMember},{tradeReportType},{tradeReport},{terminalType},{validTillDate}'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
        

    def change_order(investor,account_no,pin,order_no,new_price,new_volume):
        try:
            order_no = order_no
            deri = investor.Equity(account_no=account_no)
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

    def cancel_order(investor,account_no,pin,order_no):
        try:
            deri = investor.Equity(account_no=account_no)
            #convert order_no (str) to (int)
            order_no = order_no
            cancel_order = deri.cancel_order(order_no=order_no, pin=pin)
            return f'1'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
            
    def cancel_orders(investor,account_no,pin,order_no):
        try:
            deri = investor.Equity(account_no=account_no)
            #convert order_no (str) to (int)
            for i in range(len(order_no)):
                order_no[i] = order_no[i]
            cancel_orders = deri.cancel_orders(order_no=order_no, pin=pin)
            return f'1'
        except  SettradeError as e:
            return f'0,{e.code},{e}'
    
    