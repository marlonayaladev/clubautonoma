async function buscarDNI(dni) {
    const url = "https://apiperu.dev/api/dni"; // URL de la API
    const token = "f1c6e14c1c16427ac5fb9e700a6f5f1b2be5687f62a897a22ac3ac7b80365029"; // Reemplaza con tu token de API

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`,
            },
            body: JSON.stringify({ dni: dni }), // Enviar el DNI como JSON
        });

        const data = await response.json();
        if (response.ok) {
            console.log("Datos del DNI:", data);
            return data;
        } else {
            console.error("Error en la consulta:", data);
            return null;
        }
    } catch (error) {
        console.error("Error al realizar la consulta:", error);
        return null;
    }
}

// Ejemplo de uso:
buscarDNI("12345678").then((data) => {
    if (data) {
        console.log("Nombre completo:", data.nombre_completo);
    } else {
        console.log("No se encontró información.");
    }
});

// el mismo codigo XD
// Si
// mierda la base de datos