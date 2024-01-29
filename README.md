# ¿Qué es la Locust?
    - Locust es una herramienta de prueba de carga/rendimiento de código abierto para HTTP y otros protocolos. Su enfoque amigable para los desarrolladores le permite definir sus pruebas en código Python normal.

    - Las pruebas de Locust se pueden ejecutar desde la línea de comandos o mediante su interfaz de usuario basada en web. El rendimiento, los tiempos de respuesta y los errores se pueden ver en tiempo real y/o exportar para su posterior análisis.

    - Puede importar bibliotecas Python normales a sus pruebas y, con la arquitectura conectable de Locust, es infinitamente ampliable. A diferencia de cuando se utiliza la mayoría de las otras herramientas, el diseño de su prueba nunca estará limitado por una GUI o un lenguaje específico de dominio.

# Instalación
    1. Instale Python (3.8 o posterior)
    2. pip3 install locust
        2.1. Valida tu instalación
             locust -V

# Ejecutar pruebaß
    - locust -f test/test_2.py --host https://reqres.in --users 50 --spawn-rate 25
# Ver reportes
    - Abrir http://localhost:8089


