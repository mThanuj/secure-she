from dotenv import load_dotenv
import geocoder
import os


load_dotenv(".env")

IP_KEY = os.getenv("IP_KEY")


class GetLocation:
    def __init__(self) -> None:
        self.location = None
        self.api_key = IP_KEY

    def get_location(self) -> None:
        g = geocoder.ip("me", key=self.api_key)

        if g.ok:
            self.location = g.json
            print("Geocoding request successful.", self.location)
        else:
            print("Geocoding request failed.")
            return None

    def return_location(self) -> str:
        self.get_location()

        if self.location:
            return self.create_google_maps_link(
                self.location["lat"], self.location["lng"]
            )

        return ""

    def create_google_maps_link(self, latitude, longitude):
        base_url = "https://www.google.com/maps/search/?api=1&query="
        return base_url + str(latitude) + "," + str(longitude)
