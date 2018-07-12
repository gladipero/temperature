import json
from tornado import web
from tornado import ioloop


class Converters:
    def ConvertKelvinToFahrenheit(temperature):
        return float(((9.0/5.0)*(float(temperature)-273.15))+32.0)

    def ConvertKelvinToCelcius(temperature):
        return float(float(temperature) - 273.15)

    def ConvertKelvinToRankine(temperature):
        return float(float(temperature)*1.8)

    def ConvertRankineToKelvin(temperature):
        return float(float(temperature)/1.8)

    def ConvertFahrenheitToKelvin(temperature):
        return float((float(temperature) + 459.67)*(5.0/9.0))

    def ConvertCelciusToKelvin(temperature):
        return float(float(temperature) + 273.15)


class KelvinConversionHandler(web.RequestHandler):
    def get(self,temperature):
        F = Converters.ConvertKelvinToFahrenheit(temperature)
        C = Converters.ConvertKelvinToCelcius(temperature)
        R = Converters.ConvertKelvinToRankine(temperature)
        
        self.write(json.dumps({"fahrenheit":F,"celsius":C,"rankine":R}))
        '''if float(temperature) > 0:
            self.write(json.dumps({"fahrenheit":F,"celsius":C,"rankine":R}))
        else:
            self.write((json.dumps({"fahrenheit":"Absolute Zero","celsius":"Absolute Zero","rankine":"Absolute Zero"})))'''

class FahrenheitConversionHandler(web.RequestHandler):
    def get(self,temperature):
        K = Converters.ConvertFahrenheitToKelvin(temperature)
        C = Converters.ConvertKelvinToCelcius(K)
        R = Converters.ConvertKelvinToRankine(K)
        self.write(json.dumps({"kelvin":K,"celsius":C,"rankine":R}))
        '''
        if K > 0:
            self.write(json.dumps({"kelvin":K,"celsius":C,"rankine":R}))
        else:
            self.write((json.dumps({"kelvin":"Absolute Zero","celsius":"Absolute Zero","rankine":"Absolute Zero"})))
        '''
        
class CelciusConversionHandler(web.RequestHandler):
    def get(self,temperature):
        temperature = float(temperature)
        K = Converters.ConvertCelciusToKelvin(temperature)
        F = Converters.ConvertKelvinToFahrenheit(K)
        R = Converters.ConvertKelvinToRankine(K)

        self.write(json.dumps({"kelvin":K,"fahrenheit":F,"rankine":R}))
        '''
        if K > 0:
            self.write(json.dumps({"kelvin":K,"fahrenheit":F,"rankine":R}))
        else:
            self.write((json.dumps({"kelvin":"Absolute Zero","fahrenheit":"Absolute Zero","rankine":"Absolute Zero"})))
'''
        
class RankineConversionHandler(web.RequestHandler):
    def get(self,temperature):
        K = Converters.ConvertRankineToKelvin(temperature)
        F = Converters.ConvertKelvinToFahrenheit(K)
        C = Converters.ConvertKelvinToCelcius(K)

        self.write(json.dumps({"kelvin":K,"celsius":C,"fahrenheit":F}))
        '''        
        if K > 0:
            self.write(json.dumps({"kelvin":K,"celsius":C,"fahrenheit":F}))
        else:
            self.write((json.dumps({"kelvin":"Absolute Zero","celsius":"Absolute Zero","fahrenheit":"Absolute Zero"})))'''

def make_app():
    return web.Application([
        (r"/convert/kelvin/([+-]?\d*\.?\d+?)/",       KelvinConversionHandler),
        (r"/convert/fahrenheit/([+-]?\d*\.?\d+?)/",   FahrenheitConversionHandler),
        (r"/convert/rankine/([+-]?\d*\.?\d+?)/",      RankineConversionHandler),
        (r"/convert/celsius/([+-]?\d*\.?\d+?)/",      CelciusConversionHandler)
        ])

if __name__ == '__main__':
        app = make_app()
        app.listen(5000)
        ioloop.IOLoop.current().start()
