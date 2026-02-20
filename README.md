<h1 align="left">Módulo de Restaurante en Odoo</h1>


<h2 align="left">Integrantes</h2>
<ul>
    <li>Paula Cardenas</li>
    <li>Soledad Moral</li>
    <li>Rubén Llanes</li>
    <li>Gabriel Méndez</li>
</ul>


<h2 align="left">Sobre el proyecto</h2>

<p align="left">Este proyecto simula un ERP de un Restaurante, con diferentes módulos para que los clientes y los trabajadores puedan guiarse claramente a través de ésta.<br><br>Los módulos implementados hasta la fecha son Platos, Reservas, Categorías y el equipo de desarrollo</p>

<br clear="both">

<h2 align="left">Módulo Platos</h2>

<p align="left">En este módulo el cliente puede ver todos los platos en la carta, y cada plato viene con sus detalles como:</p>

<ul>
    <li>Nombre</li>
    <li>Una descripción breve</li>
    <li>Disponibilidad</li>
    <li>Imagen del plato (opcional)</li>
    <li>Mas informacion que quisiéramos añadir en un futuro</li>
</ul>

<p align="left">En el backend de Odoo, podemos añadir la informacion de los platos para, posteriormente, mostrarsela a los clientes en la web</p>

<hr>

<h2 align="left">Módulo Reservas</h2>

<p align="left">Modulo el cual se encarga de crear y mostrar las reservas del restaurante, tiene estos valores:</p>

<ul>
    <li>Nombre de la persona que reserva la mesa</li>
    <li>Fecha y hora de la reserva</li>
    <li>Numero de comensales</li>
    <li>Descripción o añadido voluntario sobre algun aspecto de necesidad extra</li>
</ul>

<p align="left">A la hora de crear una nueva reserva se piden 4 datos de los cuales tres de ellos son obligatorios: Nombre, fecha y hora y numero de comensales.</p>

<p align="left">Otra función a destacar es el “Datetime” el cual te permite mediante un calendario escoger fecha, permitiendo elegir hasta mes o año, y una hora en formato de 24h.</p>

<hr>

<h2 align="left">Módulo Categorias</h2>

<p align="left">Este módulo permite crear y gestionar las distintas categorías del restaurnate desde el ERP de Odoo.</p>

<p align="left">Cada categoría contiene los siguientes campos:</p>
<ul>
  <li>Nombre (campo obligarotio)</li>
  <li>Descripción</li>
  <li>Activo (booleano para activar o desactivar categoría)</li>
</ul>


<p align="left">En esta página se muestran únicamente las categorías activas del restaurante.<br>La información se presenta en formato tarjeta, mostrando:</p>

<ul>
    <li>Nombre de la categoría</li>
    <li>Descripción</li>
</ul>

<p align="left">Los datos que aparecen en la web son los mismos creados previamente desde el backend del ERP.</p>

<hr> 

<h2 align="left">Módulo Equipo</h2>

<p align="left">Su función principal es mostrar la información de cada miembro tanto en el backend del ERP como en la web pública, simulando una sección real de presentación de equipo en una empresa.</p>


<br clear="both">
<div>
  <img style="100%" src="https://capsule-render.vercel.app/api?type=waving&height=100&section=header&reversal=false&fontSize=70&fontColor=FFFFFF&fontAlign=50&fontAlignY=50&stroke=-&descSize=20&descAlign=50&descAlignY=50&textBg=false&theme=cobalt"  />
</div>

<h2>Manual de arranque</h2>
<p>Antes de comenzar, asegúrate de tener instalado:</p>

<ul>
  <li>Docker</li>
  <li>El archivo <strong>docker-compose.yml</strong></li>
  <li>El módulo ubicado dentro de la carpeta '/addons'</li>
</ul>

<hr>

<h3>1. Arrancar el entorno con Docker</h3>

<h4>Levantar los contenedores</h4>

<p>Si es la primera vez o el entorno está apagado:</p>

<pre><code class="language-bash">
docker compose up -d
</code></pre>

<p>Este comando iniciará los servicios definidos (Odoo y la base de datos) en segundo plano.</p>

<h3>2. Acceder al ERP y crear la base de datos</h3>

<p>Abrir en el navegador:</p>

<pre><code>
http://localhost:8069/web
</code></pre>

<p>Si es la primera vez que entramos, crear una base de datos con los siguientes datos:</p>

<ul>
  <li><strong>Nombre de la base de datos:</strong> odoo_restaurante</li>
  <li><strong>Email:</strong> admin@odoo.local</li>
  <li><strong>Password:</strong> admin</li>
</ul>

<p>Una vez creada la base de datos:</p>

<ol>
  <li>Activar el <strong>Modo Desarrollador</strong>.</li>
  <li>Ir a <strong>Aplicaciones</strong>.</li>
  <li>Instalar el módulo <strong>Website</strong>.</li>
</ol>

<p>Al instalar Website, la web pública quedará disponible en:</p>

<pre><code>
http://localhost:8069/
</code></pre>

<hr>

<h3>3. Instalar o actualizar el módulo</h3>

<p>Después de añadir o modificar código en el módulo:</p>

<h4>Reiniciar el servicio en Docker</h4>

<pre><code class="language-bash">
docker compose restart odoo
</code></pre>

<h4>Actualizar desde Odoo</h4>

<ol>
  <li>Ir a <strong>Aplicaciones</strong>.</li>
  <li>Pulsar <strong>Actualizar lista de aplicaciones</strong>.</li>
  <li>Buscar el módulo.</li>
  <li>Pulsar <strong>Instalar</strong> o <strong>Actualizar</strong>.</li>
</ol>

<hr>

<h3>4. Verificación final</h3>

<ul>
  <li>Odoo arranca sin errores</li>
  <li>El módulo aparece en la lista de aplicaciones.</li>
  <li>La web carga correctamente en <strong>http://localhost:8069/</strong>.</li>
  <li>Las rutas públicas funcionan sin necesidad de login.</li>
  <li>Los datos creados en el backend se visualizan correctamente en la web.</li>
  <li>El archivo <strong>manifest.py</strong> incluye la dependencia <strong>website</strong>.</li>
  <li>El módulo se actualiza sin errores.</li>
</ul>
<br clear="both">
<div>
  <img style="100%" src="https://capsule-render.vercel.app/api?type=waving&height=100&section=header&reversal=false&fontSize=70&fontColor=FFFFFF&fontAlign=50&fontAlignY=50&stroke=-&descSize=20&descAlign=50&descAlignY=50&textBg=false&theme=cobalt"  />
</div>