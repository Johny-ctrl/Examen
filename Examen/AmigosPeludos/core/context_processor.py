def total_venta(request):
    total = 0
    request.user.is_authenticated and 'cart' in request.session
    if "cart" in request.session.keys():
        for key, value in request.session["cart"].items():
            total += value["precio"]
    return {"total_venta": total}

    