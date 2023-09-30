class Card:
    value = None
    img_path = None

    def __init__(self, value, img_path):
        self.value = value
        self.img_path = img_path

    def _public_set_value(self, value):
        self.value = value

    def _public_set_img_path(self, img_path):
        self.img_path = img_path

    def _public_get_value(self):
        return self.value

    def _public_get_img_path(self):
        return self.img_path


