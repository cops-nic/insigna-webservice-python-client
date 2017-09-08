if __name__ == '__main__':
    from suds.client import Client,WebFault
    from ws.WsSecurity import WsSecurityHeader
    
    try:
        #URL del webservice
        url='https://beta.ws.insigna.mx/services?wsdl'
        #Se crea el proxy del Web service
        client=Client(url)
        #Se agrega el security header con el username y password para la autenticacion
        secureHeader=WsSecurityHeader().getSecurityHeader('usuario','password')
        client.set_options(soapheaders=secureHeader)
        #Se usan los metodos y objetos propios del Web service de INSIGNA
        wrapper=client.factory.create('cfdiInfoWrapper')
        wrapper.uuid='e08b6418-5f55-428a-b5eb-d469531ada1b'
        wrapper.transactionId='tr1'
        infoResult=client.factory.create('CfdiInfoResult')
        infoResult=client.service.getCfdiInfo(wrapper)
        print infoResult
    except WebFault as detail:
        error= detail.fault.detail.OperationFailed
        print error.errorCode+': '+error.errorDescription               
    pass