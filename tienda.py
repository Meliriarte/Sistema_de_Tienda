tienda = { 
    "lista_productos" : [
        {"id": 1, "nombre": "Camiseta", "precio": 19.99, "stock": 50},
        {"id": 2, "nombre": "Zapatos", "precio": 59.99, "stock": 30},
        {"id": 3, "nombre": "Gorra", "precio": 14.99, "stock": 20}
    ],
    "lista_pedidos" : [
        {"id_pedido": 101, "cliente": "juan@gmail.com", "productos": [1, 2], "estado": "Pendiente"},
        {"id_pedido": 102, "cliente": "ana@gmail.com", "productos": [3], "estado": "En proceso"}
    ],
    "clientes_registrados" : [
        {"nombre": "Juan Pérez", "email": "juan@gmail.com", "direccion": "Calle 123"},
        {"nombre": "Ana Gómez", "email": "ana@gmail.com", "direccion": "Calle 456"}
    ], 
};

producto_nuevo = {"id": 4, "nombre": "Pantalon", "precio": 30.99, "stock":40};
tienda["lista_productos"].append(producto_nuevo);

print (tienda);