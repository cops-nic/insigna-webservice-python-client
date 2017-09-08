#importamos la clase Element de suds.wsse
from suds.wsse import  Element

class WsSecurityHeader(object):


    def __init__(self):
        #do nothing
        pass
        
        '''
        Metodo que crear el Security header necesario 
        para autenticar al cliente al Web service
        '''
    def getSecurityHeader(self,username,password): 
        #Define del namespace 
        wsns=('wsse','http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd')
        ##Crea el elemento Security
        security=Element('Security',ns=wsns)
        #Crea del usernametoken
        usernametoken=Element('UsernameToken',ns=wsns)
        username=Element('Username',ns=wsns).setText(username)
        password=Element('Password',ns=wsns).setText(password)
        password.set('Type', 'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText')
        #Agrega el username y el password al usernametoken
        usernametoken.insert(username)
        usernametoken.insert(password)
        #Agrega el usernametoken al Security
        security.insert(usernametoken)
        return security