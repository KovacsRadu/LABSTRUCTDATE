class Masina:
    def __init__(self, marca: str, model: str, token: str, pretAchizitie: int, pretVanzare: int):
        self._marca = marca
        self._model = model
        self._token = token
        self._pretAchizitie = pretAchizitie
        self._pretVanzare = pretVanzare

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, new: str):
        self._marca = new

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new: str):
        self._model = new

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, new: str):
        self._token = new

    @property
    def pretAchizitie(self):
        return self._pretAchizitie

    @pretAchizitie.setter
    def pretAchizitie(self, new: int):
        if not isinstance(new, int):
            raise ValueError("pretAchizitie must be an integer")
        self._pretAchizitie = new

    @property
    def pretVanzare(self):
        return self._pretVanzare

    @pretVanzare.setter
    def pretVanzare(self, new: int):
        if not isinstance(new, int):
            raise ValueError("pretVanzare must be an integer")
        self._pretVanzare = new

    def __str__(self):
        return f"{self._marca} {self._model} {self._token} {self._pretAchizitie} {self._pretVanzare}"







