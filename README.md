<h1>Raspagem de dados de todas OFERTAS do site https://mercadolivre.com.br/</h1>

<h2>Tá, mas o que é raspagem de dados?</h2>
<p>Raspagem de dados(ou Data Scraping) é uma técnica computacional na qual um programa extrai dados de saída legível somente para humanos, proveniente de um serviço ou aplicativo.</p>

<h2>Quais pacotes/módulos foram usado nesse projeto?</h2>
<ul>
  <li>Requests_HTML -> Esta biblioteca torna a análise de HTML (por exemplo, raspagem da web) o mais simples e intuitiva possível.
    <a href='https://pypi.org/project/requests-html/'>Documentação PyPi</a>.
  </li>
  <li>Beautiful Soup -> Beautiful Soup é uma biblioteca Python de extração de dados de arquivos HTML e XML.
  <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/'>Documentação</a>.
  </li>
  <li>OS -> Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes de sistema operacional.
  <a href='https://docs.python.org/pt-br/3/library/os.html'>Documentação</a>.
  </li>
  <li>Datetime -> O módulo datetime fornece as classeh3s para manipulação de datas e horas.
  <a href='https://docs.python.org/pt-br/3/library/datetime.html?highlight=datetime#module-datetime'>Documentação</a>.
  </li>
  <li>Pathlib -> Usei para criar arquivos .txt, porém é bastante usado para manipulação de caminho de baixo nível em strings.
  <a href='https://docs.python.org/pt-br/3/library/pathlib.html?highlight=pathlib#module-pathlib'>Documentação</a>.
  </li>
</ul>

<h2>Entendi, mas qual seria a ultilidade desse programa?</h2>
<p>Nessa primeira versão, ele lista todos os produtos que estão em promoção, seja qualquer porcentagem de desconto, de 1% até 99% de desconto, e passar para um documento .txt. Nas proximas versões, ele irá listar os produtos de acordo com o seu gosto, exemplo: Celular, Eletrodomésticos e computadores. Para em seguida pegar todos que estão em promoção.</p>
<br>
<p>Versão 1.1 | 28/02/2022</p>
<p>Versão 1.2 | 30/04/2022</p>
<h3>Coisas para arrumar na versão 1.3:</h3>
<ul>
  <li>Um sistema onde você pesquisa o nome do produto e ele mostra o produto e suas repectivas promoções.</li>
  <li>Um banco de dados, ao invés de um código de texto.</li>
</ul>
