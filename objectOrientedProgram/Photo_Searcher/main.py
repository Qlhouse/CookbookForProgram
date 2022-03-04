from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        print(query)

        # Get wikipedia page and the first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        print(image_link)
        return image_link

    def download_image(self):
        # Download the image
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}
        req = requests.get(self.get_image_link(), headers=headers)
        imagePath = "files/image.jpg"
        with open(imagePath, "wb") as file:
            file.write(req.content)

        return imagePath

    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
