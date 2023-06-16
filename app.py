import sqlite3
from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_pedido():
    if  request.method == 'POST':
        pedido_id = request.form['pedido_id']
        conn = sqlite3.connect('./happyburger.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Pedido WHERE pedido = ?', (pedido_id,))
        pedido = cursor.fetchone()
        conn.close()
        if pedido:
            return render_template('detalle_pedido.html', pedido=pedido)
        else:
            mensaje = "Pedido no encontrado"
            return render_template('buscar_pedido.html', mensaje=mensaje)
    else:
        return render_template('buscar_pedido.html')




if __name__== "__main__":
    app.run(debug=True, port=5001)