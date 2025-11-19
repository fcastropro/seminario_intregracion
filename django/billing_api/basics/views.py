from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def area_triangulo(request):
    try:
        base = float(request.data.get('base',0))
        altura = float(request.data.get('altura',0))
    except (TypeError, ValueError):
        return Response({"error": "Parámetros Inválidos"}, status=status.HTTP_400_BAD_REQUEST)
    area = (base * altura)/2
    return Response({
        "base": base,
        "altura": altura,
        "area": area
    })

@api_view(['GET'])
def tabla_multiplicar(request):
    try:
        numero = int(request.query_params.get('numero', 0))
    except (TypeError, ValueError):
        return Response(
            {"error": "Número Inválido"},
            status=status.HTTP_400_BAD_REQUEST
        )
    tabla = [f"{numero} x {i} = {numero * i}" for i in range(1, 13)]
    return Response({
        "numero": numero,
        "tabla": tabla
    })

@api_view(['POST'])
def contar_mayores(request):
    try:
        numeros = request.data.get('numeros',[])
        limite = request.data.get('limite',0)
    except (TypeError, ValueError):
        return Response({"error": "Parámetros Invalidos"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        limite=float(limite)
        lista_numeros = [float(n) for n in numeros]
    except(TypeError, ValueError):
        return Response({"error":"Valores numéricos Inválidos"},
                        status=status.HTTP_400_BAD_REQUEST)
    contador = 0
    for n in lista_numeros:
        if n> limite:
            contador+=1
    return Response({
        "numeros":lista_numeros,
        "limite":limite,
        "mayores":contador
    })

@api_view(['POST'])
def sumar_numeros(request):
    try:
        numero = int(request.data.get('numero', 0))
    except (TypeError, ValueError):
        return Response(
            {"error": "Número Inválido"},
            status=status.HTTP_400_BAD_REQUEST
        )
    if numero < 1:
        return Response(
            {"error": "El número debe ser mayor o igual a 1"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    numeros = list(range(1, numero + 1))
    resultado = sum(numeros)
    expresion = " + ".join(str(x) for x in numeros)

    return Response({
        "numero": numero,
        "expresion": expresion,      # "1 + 2 + 3 + ... + n"
        "resultado": resultado       # suma total
    })

@api_view(['POST'])
def promedio(request):
    try:
        numeros = request.data.get('numeros',[])
    except (TypeError, ValueError):
        return Response({"error": "Parámetros Invalidos"},
                        status=status.HTTP_400_BAD_REQUEST)
 
    promedio= sum(numeros) / len(numeros)
    return Response({
        "promedio":promedio
    })

@api_view(['POST'])
def potencia(request):
    try:
        base = request.data.get('base',0)
    except (TypeError, ValueError):
        return Response({"error": "Parámetros Invalidos"},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        potencia = request.data.get('potencia',0)
    except (TypeError, ValueError):
        return Response({"error": "Parámetros Invalidos"},
                        status=status.HTTP_400_BAD_REQUEST)
 
    resultado= base ** potencia
    return Response({
        "resultado":resultado
    })