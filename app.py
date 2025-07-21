from flask import Flask, render_template, request, redirect, url_for
from models.cola import ColaBoletos
from models.pila import HistorialVentas

app = Flask(__name__)
cola_boletos = ColaBoletos()
historial_ventas = HistorialVentas()

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/cola', methods=['GET', 'POST'])
def gestionar_cola():
    if request.method == 'POST':
        cliente = request.form.get('cliente')
        asientos = request.form.get('asientos')
        funcion = request.form.get('funcion')

        if cliente and asientos and funcion:
            reserva = f"{cliente} - {asientos} asientos - Función: {funcion}"
            cola_boletos.encolar(reserva)

        if request.form.get('accion') == 'procesar' and not cola_boletos.esta_vacia():
            reserva = cola_boletos.desencolar()
            historial_ventas.empilar(reserva)

        return redirect(url_for('gestionar_cola'))

    return render_template('cola.html', reservas=cola_boletos.obtener())

@app.route('/pila', methods=['GET', 'POST'])
def gestionar_historial():
    if request.method == 'POST':
        venta = request.form.get('venta')
        if venta:
            historial_ventas.empilar(venta)

        if request.form.get('accion') == 'deshacer' and not historial_ventas.esta_vacia():
            historial_ventas.desempilar()

        return redirect(url_for('gestionar_historial'))

    return render_template('pila.html', ventas=historial_ventas.obtener())

if __name__ == '__main__':
    app.run(debug=True)
