from internal.router.router import Router
from internal.server import Http
from injector import Injector

import dotenv

dotenv.load_dotenv()

injector = Injector()
app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)
