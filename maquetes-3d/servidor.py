# Servidor local para renderizar as cenas 3D no navegador e salvar os PNGs.
# GET serve esta pasta; POST /salvar?nome=arquivo.png grava o corpo em ./saida/
import os, sys, urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

BASE = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(BASE, 'saida')
os.makedirs(SAIDA, exist_ok=True)


class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=BASE, **k)

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def do_POST(self):
        url = urllib.parse.urlparse(self.path)
        if url.path != '/salvar':
            self.send_error(404); return
        nome = os.path.basename(urllib.parse.parse_qs(url.query).get('nome', ['saida.png'])[0])
        if not nome.endswith('.png'):
            self.send_error(400); return
        dados = self.rfile.read(int(self.headers.get('Content-Length', 0)))
        with open(os.path.join(SAIDA, nome), 'wb') as f:
            f.write(dados)
        self.send_response(200); self.end_headers(); self.wfile.write(b'ok')


porta = int(sys.argv[1]) if len(sys.argv) > 1 else 5510
ThreadingHTTPServer(('127.0.0.1', porta), H).serve_forever()
