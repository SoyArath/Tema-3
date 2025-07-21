# Escritura del README.md actualizado a archivo para descarga
content = '''# Sistema de Venta de Boletos de Cine - Superman

![Pantalla del sistema de boletos](Superman_Cinema_System/static/Interfaz.png)

**Nombre del alumno:** Arath Yahir Lopez Guzman  
**Materia:** Estructura de Datos

---

## Descripción del sistema

Esta aplicación web está desarrollada en Python con Flask y permite gestionar la **venta de boletos para la película Superman** mediante estructuras de datos abstractas:

### Características principales:

- **Cola de reservas (FIFO):** Los clientes agregan sus reservas y esperan su turno para ser atendidos.
- **Pila de historial de ventas (LIFO):** Cada vez que se procesa una reserva, se registra en el historial; se puede cancelar la última venta.
- **Abstracción implementada:** Se utilizan clases abstractas para definir las interfaces de Cola y Pila.

### Funcionalidades del sistema:
- **Encolar** una nueva reserva de boletos
- **Procesar** (desencolar) la siguiente reserva y convertirla en venta
- **Registrar** manualmente una venta directa
- **Cancelar** (desempilar) la última venta registrada

La interfaz utiliza Bootstrap con un tema visual inspirado en Superman.

---

## Estructura del proyecto

```
Superman_Cinema_System/
├── app.py
├── models/
│   ├── __init__.py
│   ├── cola.py
│   └── pila.py
├── templates/
│   ├── Interfaz.png
│   ├── cola.html
│   ├── menu.html
│   ├── pila.html
│   └── readme.md
├── static/
│   └── css/
│       └── custom.css
└── venv/
    ├── .gitignore
    ├── pyvenv.cfg
    ├── Include/
    ├── Lib/
    └── Scripts/
```

## Instalación

1. **Clona o descarga** este repositorio en tu máquina local.  
2. Abre una terminal y sitúate en la carpeta raíz del proyecto:  
   ```bash
   cd Superman_Cinema_System
   ```

3. (Opcional) Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   .\venv\Scripts\activate     # Windows
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para arrancar el servidor Flask, ejecuta:

```bash
python app.py
```

Luego abre tu navegador en:

```
http://127.0.0.1:5000/
```

## Ejemplo de uso

### Ver menú principal:
- Navega a `/` para acceder al menú principal con tema de Superman

### Agregar una reserva:
1. Ve a "Reservas de Boletos (Cola)"
2. Escribe "Juan Pérez - 2 boletos VIP" y haz clic en "Agregar Reserva"
3. Verás tu reserva listada como número 1 en la cola

### Procesar reserva (venta):
1. Haz clic en "Procesar Siguiente Reserva (Vender Boleto)"
2. La reserva desaparece de la cola y se añade al historial de ventas

### Gestionar ventas:
1. Ve a "Historial de Ventas (Pila)"
2. Añade ventas manuales o cancela la última venta registrada

## Conceptos aplicados

- **Abstracción**: Uso de clases abstractas para definir interfaces comunes
- **FIFO (First In, First Out)**: Cola para reservas de boletos  
- **LIFO (Last In, First Out)**: Pila para historial de ventas
- **Herencia**: Las clases concretas heredan de las abstractas
- **Polimorfismo**: Métodos implementados de manera específica en cada clase''' 

# Guardar el archivo
output_path = '/mnt/data/README.md'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"README actualizado guardado en: {output_path}")
