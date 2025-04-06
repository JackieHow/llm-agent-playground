from internal.router.router import Router
from internal.server import Http
from injector import Injector
from config import Config

import dotenv

dotenv.load_dotenv()
conf = Config()

injector = Injector()
app = Http(__name__, conf=conf, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
