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

class FahrenheitConversionHandler(web.RequestHandler):
    def get(self,temperature):
        K = Converters.ConvertFahrenheitToKelvin(temperature)
        C = Converters.ConvertKelvinToCelcius(K)
        R = Converters.ConvertKelvinToRankine(K)

        self.write(json.dumps({"kelvin":K,"celsius":C,"rankine":R}))

class CelciusConversionHandler(web.RequestHandler):
    def get(self,temperature):
        K = Converters.ConvertCelciusToKelvin(temperature)
        F = Converters.ConvertKelvinToFahrenheit(K)
        R = Converters.ConvertKelvinToRankine(K)

        self.write(json.dumps({"fahrenheit":F,"kelvin":K,"rankine":R}))

class RankineConversionHandler(web.RequestHandler):
    def get(self,temperature):
        K = Converters.ConvertRankineToKelvin(temperature)
        F = Converters.ConvertKelvinToFahrenheit(K)
        C = Converters.ConvertKelvinToCelcius(K)
	
        self.write(json.dumps({"fahrenheit":F,"kelvin":K,"celsius":C}))

def make_app():
    return web.Application([
        (r"/convert/kelvin/(\d+)/",       KelvinConversionHandler),
        (r"/convert/fahrenheit/(\d+)/",   FahrenheitConversionHandler),
        (r"/convert/rankine/(\d+)/",      RankineConversionHandler),
        (r"/convert/celsius/(\d+)/",      CelciusConversionHandler)
        ])

if __name__ == '__main__':
	app = make_app()
	app.listen(5000)
	ioloop.IOLoop.current().start()
