# Como actualizaré el CV de forma automatica

```mermaid
graph TD
    A[Inicio] --> B{¿Se hace un Push en algún archivo .csv?}
    B -->|Sí| C[Ejecutamos Script Python]
    B -->|No| E[Fin]
    C --> E[Fin]