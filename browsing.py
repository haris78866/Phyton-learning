import webbrowser

def open_google_maps(location):
    base_url = "https://www.google.com/maps/place/"
    url = base_url + location.replace(" ", "+")
    webbrowser.open(url)

if __name__ == "__main__":
    location = input("Enter the location for Google Maps: ")
    open_google_maps(location)
