from redis_client import (
      add_value_to_list,
      updated_specific_value,
      get_specific_value,
      get_list_values,
      remove_data_related_to_user,
        get_all_values,
          set_dict_value,
          clean_redis_database
)

"""2. Almacenamiento de datos de usuarios:
Crea y guarda los datos de usuarios en Redis. Por ejemplo:

Usuario 1: Nombre - "Alice", Edad - 30
Usuario 2: Nombre - "Bob", Edad - 25
"""
set_dict_value("usuario:1",{"nombre": "Alice", "edad": 30})
set_dict_value("usuario:2",{"nombre": "Bob", "edad": 25})


"""3. Almacenamiento de preferencias de usuarios:
Guarda las preferencias de los usuarios en Redis. Por ejemplo:

Preferencias de Alice: ["Música", "Viajes"]
Preferencias de Bob: ["Deportes", "Cine"]
"""
add_value_to_list("preferencias:1", "Música", "Viajes")
add_value_to_list("preferencias:2", "Deportes", "Cine")


"""4. Consultas en Redis:
Realiza consultas para recuperar información de usuarios y sus preferencias.

Recupera la edad de "Alice".
Recupera las preferencias de "Bob".
"""
edad_alice = get_specific_value("usuario:1", "edad")
preferencias_bob = get_list_values("preferencias:2")
print(f"La edad de Alice es: {edad_alice}")
print(f"Las preferencias de bob son: {preferencias_bob}")

"""5. Actualización de datos en Redis:
Actualiza la edad de "Bob" a 28 años y añade la preferencia "Lectura".
"""

updated_specific_value("usuario:2", "edad", 28)
add_value_to_list("preferencias:2", "Lectura")

"""6.Eliminación de datos en Redis:
Elimina las preferencias de "Alice" de la base de datos.
"""
remove_data_related_to_user("1")

"""7.Consulta después de las modificaciones:
Verifica que las actualizaciones y eliminaciones se hayan realizado correctamente.
"""
usuario_1_data = get_all_values("usuario:1")
print(f"Información del usuario 1(debe ser vacio): {usuario_1_data}")
usuario_2_data = get_all_values("usuario:2")
print(f"Información del usuario 2: {usuario_2_data}")

preferencias_usario_1 = get_list_values("preferencias:1")
print(f"Preferencias de Alice(debe ser vacio): {preferencias_usario_1}")
preferencias_usario_2 = get_list_values("preferencias:2")
print(f"Preferencias de bob: {preferencias_usario_2}")

clean_redis_database()
