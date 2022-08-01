
# ✨ Project Test Challenge on Django Framework

Web App for SED band rock

## 📋 Tecnologies
 - `Django framework`
## 📋 Pre-requisitos
 - `python 3.9.0` o superior
 - `mysql` data bases
 ```
   create databases hotel_django;
 ```
## 🔭 Copy repository and installation
_Copia del repositorio **GITLAB** del proyecto en funcionamiento en tu máquina local._
 - `Clone the repo`
 ```
   git clone https://github.com/alexanderJPV/djangoTestChallenge
  ```
 - `project path`
 ```
    cd /project
 ```
 - `Install python packages`
 ```
    pip install -r requirements.txt
 ```
## 🔧 Runing
- `Comand to run serve`
```
python manage.py runserver
```
- `Comand to migrate data fake`
```
python manage.py loaddata datafake.json
```
## 🔧 Authentication
```
- user: test
- password: test
```
Runs the app in the development mode.

- Mode admin Open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/admin/) to view it in the browser.

- Mode development Open [http://127.0.0.1:8000/api/{model}/](http://127.0.0.1:8000/api/) to view it in the browser.

## Resources folder tree

```
/djangoTestChallenge
   /testChallenge
        /api
            /migrations
            admin.py
            models.py
            serializers.py
            urls.py
            views.py
        /testChallenge
            asgi.py
            setting.py
            urls.py
            wsgi.py
        datafake.py
        manage.py
    README.md
    requirements.txt
```
## Activities Diagram and flowchart
Explains all entyties, flows and activities
* Entity cliente(client)
* Entity reserva(reserve)
* Entity habitacion(room)
* Entity pago(payment)
* Entity factura
## End-points
<ol>
   <li>
      <p>End-poinds cliente(client).</p>
      <h4>CRUD: En el analisis y diseño "Cliente" es el actor principal su funcion es el solicitante de una reserva. Los end-points siguientes hacen posible que el backend segun la arquitecura API RESTFULL.<br>
      Content-Type: application/json
      </h4>
      <blockquote>
         <span>Allow: GET, POST</span>
         <p> http://127.0.0.1:8000/api/clients/</p>
         <span>Allow: GETONE, PUT, DELETE</span>
         <p> http://localhost:3000/api/clients/{id}</p>
      </blockquote>
   </li>
   <li>
      <p>End-poinds Habitacion(room).</p>
      <h4>CRUD: En el analisis y diseño "Habitacion" es otro actor principal su funcion representar las caracteristicas y estados de una habitacion de hotel. Los end-points siguientes hacen posible que el backend segun la arquitecura API RESTFULL.<br>
      Content-Type: application/json
      </h4>
      <blockquote>
         <span>Allow: GET, POST</span>
         <p> http://127.0.0.1:8000/api/rooms/</p>
         <span>Allow: GETONE, PUT, DELETE</span>
         <p> http://127.0.0.1:8000/api/rooms/{id}</p>
      </blockquote>
   </li>
   <li>
      <p>End-poinds Reserve(reserva).</p>
      <h4>CRUD: En el analisis y diseño "Reserva" es la relacion de una cliente con habitacion. Los end-points siguientes hacen posible que el backend segun la arquitecura API RESTFULL.<br>
      Content-Type: application/json
      </h4>
      <blockquote>
         <span>Allow: GET, POST</span>
         <p> http://127.0.0.1:8000/api/reserves/</p>
         <span>Allow: GETONE, PUT, DELETE</span>
         <p> http://127.0.0.1:8000/api/reserves/{id}</p>
      </blockquote>
   </li>
   <li>
      <p>End-poinds Payment(pago).</p>
      <h4>CRUD: En el analisis y diseño "Pago" tiene la funcion de registrar el monto y tipo de pago y mentiene una relacion direca con reserva. Los end-points siguientes hacen posible que el backend segun la arquitecura API RESTFULL.<br>
      Content-Type: application/json
      </h4>
      <blockquote>
        <span>Allow: GET, POST</span>
        <p> http://127.0.0.1:8000/api/payments/</p>
        <span>Allow: GETONE, PUT, DELETE</span>
        <p> http://127.0.0.1:8000/api/payments/{id}</p>
      </blockquote>
      <h4>OTHERS: Adiciones funciones extras a CRUD.<br>
          Facturar: Recibe el id=X de una factura y hace una consulta para reunir los datos necesarios para un comprobante de factura.
      </h4>
      <blockquote>
        <span>Allow: GET IMPRIMIR-FACTURA</span>
        <p> http://localhost:8000/api/payments/?paymentId={id}</p>
      </blockquote>
   </li>
   <li>
      <p>End-poinds Factura.</p>
      <h4>CRUD: En el analisis y diseño "Factura" tiene la funcion de registrar el numero de factura nit y datelles para le emicion de un comprobante. Los end-points siguientes hacen posible que el backend segun la arquitecura API RESTFULL.<br>
      </h4>
      <blockquote>
        <span>Allow: GET, POST</span>
        <p> http://127.0.0.1:8000/api/facturas/</p>
        <span>Allow: GETONE, PUT, DELETE</span>
        <p> http://127.0.0.1:8000/api/facturas/{id}</p>
      </blockquote>
   </li>
</ol>

## 🛠️ Construido con

* [django](https://django.com/) - El framework usado
## ✒️ Autores

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Alexander Perez** - *Trabajo Inicial and Documentación* - [fulanitodetal](#fulanito-de-tal)
