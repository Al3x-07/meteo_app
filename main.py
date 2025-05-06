from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang import Builder
import requests

Builder.load_file("meteo_layout.kv")

class MeteoApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.get_meteo, 1)

    def get_meteo(self, dt):
        # Coordinate fisse: Cuneo (o altra località desiderata)
        lat = 44.3907
        lon = 7.5483

        url = (
            "https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,"
            "sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max,precipitation_probability_max"
            "&timezone=Europe%2FBerlin"
        )

        try:
            response = requests.get(url)
            data = response.json()
            daily = data["daily"]

            # Prende il primo giorno disponibile
            self.ids.temp_max.text = str(daily["temperature_2m_max"][0]) + " °C"
            self.ids.temp_min.text = str(daily["temperature_2m_min"][0]) + " °C"
            self.ids.sunrise.text = daily["sunrise"][0].split("T")[1]
            self.ids.sunset.text = daily["sunset"][0].split("T")[1]
            self.ids.daylight.text = self.seconds_to_hms(daily["daylight_duration"][0])
            self.ids.sunshine.text = self.seconds_to_hms(daily["sunshine_duration"][0])
            self.ids.uv_index.text = str(daily["uv_index_max"][0])
            self.ids.precipitation.text = str(daily["precipitation_probability_max"][0]) + " %"

            self.ids.status.text = "Dati meteo aggiornati"
        except Exception as e:
            self.ids.status.text = f"Errore nel caricamento: {e}"

    def seconds_to_hms(self, seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        return f"{h}h {m}m"

class MeteoAppMain(App):
    def build(self):
        return MeteoApp()

if __name__ == "__main__":
    MeteoAppMain().run()
