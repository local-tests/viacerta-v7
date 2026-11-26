# Maquetes 3D dos serviços

As imagens `casa-3d`, `empresa-3d` e `evento-3d` da versão 02 são modeladas aqui, em Three.js, e renderizadas no navegador.

1. Rode o servidor (ele também salva as imagens):

   ```bash
   python servidor.py 5510
   ```

2. Abra http://localhost:5510 e espere aparecer "pronto". Os PNGs (2400 × 1600, fundo transparente) ficam em `saida/`.
   Para refazer só uma cena: http://localhost:5510/?cenas=casa

3. Converta para WebP (1200 e 600 px) e copie para `versão-02/assets/img/`:

   ```bash
   python -c "from PIL import Image; [Image.open(f'saida/{n}.png').resize((w, w*2//3), Image.LANCZOS).save(f'../../versão-02/assets/img/{n}-3d{s}.webp', 'WEBP', quality=82, method=6) for n in ('casa','empresa','evento') for w, s in ((1200,''),(600,'-600'))]"
   ```

Cores, materiais e posições ficam em `index.html`: funções `cenaCasa`, `cenaEmpresa` e `cenaEvento`. O vermelho da marca é o material `led` (faixas de luz) e `vermelho` (toldo e letreiro).
