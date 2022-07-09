#Definir variable cart



class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart
        #creacion del producto en el carro
        def add(self, producto):
            if str(producto.id) not in self.cart.keys():
                self.cart[producto.id] = {
                    "producto_id": producto.id,
                    "nombre": producto.name,
                    "cantidad": 1,
                    "precio": str(producto.precio),
                    "imagen":producto.imagen.url  
                    }    
            #Si el producto ya existe
            else:
                for key , value in  self.cart.items():
                  if key == str(producto.id) :
                    value["quantity"] = value["quantity"] + 1
                    self.save()     
                    break
                  