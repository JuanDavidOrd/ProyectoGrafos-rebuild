# ProyectoGrafos-rebuild

Requisitos
- Python 3.10+ con un entorno virtual (se asume `.venv` en la raíz).
- Dependencias en `requirements.txt` (PySide6, matplotlib, pandas, networkx, etc.).

Ejecutar la aplicación (Windows)

1. Crear y activar el entorno virtual con python 3.11:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```
2. Instalar dependencias 

```powershell
pip install -r requirements.txt
```

3. Ejecutar la aplicación:

```powershell
python run.py
```

Notas rápidas
- Al cargar un JSON de universo puedes usar los botones laterales para editar estrellas, gestionar vías y calcular rutas (Punto 2 / Punto 3).
- Punto 3 incluye estancia, consumo de pasto e investigación; si el "burro" muere, la UI intentará reproducir el sonido `assets/sounds/donkey_death.wav` y mostrará un reporte.
- Los reportes se exportan a la carpeta `reports/` en formato CSV/JSON.

Estructura básica del proyecto
- `run.py` – lanzador
- `ui/` – interfaz PySide6 (mapa, paneles, diálogos)
- `core/` – lógica de grafo, simulador, reglas y reportes
- `assets/sounds/` – sonidos (opcional)
- `data/` – datos de ejemplo (JSON)


