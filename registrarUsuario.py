from cargarUsuarios import cargarUsuarios

def registrarUsuario(nombreUsuario, contraseñaUsuario, archivoUsuarios):
    usuarios_dict = cargarUsuarios(archivoUsuarios)
    if (nombreUsuario in usuarios_dict):
        mensaje = "Este usuario ya se encuentra registrado."
    else:
        with open(archivoUsuarios, 'a') as f:
            f.write(f"{nombreUsuario};{contraseñaUsuario}\n")
        mensaje = "Usuario añadido correctamente."
    return mensaje

