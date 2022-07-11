#Definir variable cart
class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart
    #creacion del producto en el carro
    def add(self, producto):
        id = str(producto.id)
        if id not in self.cart.keys():
            self.cart[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "Venta": producto.precio,
                "cantidad": 1,
            }
        else:
            self.cart[id]["cantidad"] += 1
            self.cart[id]["Venta"] += producto.precio
        self.save()  
    #definir guardar
    def save(self):
        self.session["cart"] = self.cart
        #actualiza sesion en carro
        self.session.modified = True

    #borrar un producto del carro
    def remove(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()

    #disminuir cantidad de productos

    def decrement(self, producto):
        id = str(producto.id)
        if id in self.cart.keys():
            self.cart[id]["cantidad"] -= 1
            self.cart[id]["Venta"] -= producto.precio
            if self.cart[id]["cantidad"] <=0: self.remove(producto)
            self.save()
            
    #limpiar
    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True