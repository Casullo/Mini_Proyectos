def escribir_centrado(texto):
    longitud= len(texto)
    espacios = 40 - longitud // 2
    print ("  " * espacios, texto)
    # print (" " * espacios, "=" * longitud)

escribir_centrado ("hola, mundo!")
escribir_centrado ("hola, Dani!")
escribir_centrado ("hola, Rami!")
escribir_centrado ("hola, sea!")
escribir_centrado ("hola, matea!")