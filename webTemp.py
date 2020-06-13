from microWebSrv import MicroWebSrv
import esp32

@MicroWebSrv.route('/temperature')
def _httpHandlerTempGet(httpClient, httpResponse):
    temp = (esp32.raw_temperature() -32) * 5.0/9.0
    
    httpResponse.WriteResponseOk( headers        = ({'Cache-Control': 'no-cache'}),
                                  contentType    = 'text/html',
                                  contentCharset = 'UTF-8',
                                  content        = "Temperatur = {}".format(temp))
    
srv = MicroWebSrv(webPath='www/')
srv.WebSocketThreaded       = False
srv.Start()