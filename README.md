# Simulador de Ruleta con IA

Este proyecto es una API creada con FastAPI que simula apuestas de ruleta usando IA y estrategias como Martingala.

## Endpoints

- `GET /`: Verifica si el servidor está activo.
- `POST /simular`: Ejecuta la simulación.

### Ejemplo de llamada POST:

```json
{
  "capital": 100,
  "rondas": 200
}
```
