# DinoGuard

## Descripción General

**DinoGuard** es un videojuego de plataformas 2D desarrollado en Python utilizando Pygame.  
El proyecto fue creado como una prueba técnica con el objetivo de demostrar familiarización con Python, programación orientada a objetos, manejo de estados y conceptos fundamentales de desarrollo de videojuegos.

El juego cuenta con tres niveles demo jugables en los que el jugador debe avanzar hasta el final evitando enemigos y obstáculos.

## Historia

En **DinoGuard**, un guardián prehistórico emprende una pequeña misión.

En el primer nivel, encuentra un huevo perdido en medio de un entorno lleno de peligros.  
En el segundo nivel, atraviesa nuevas amenazas para devolver el huevo a su madre, una diplodocus que lo espera al final del recorrido.  
Finalmente, en el tercer nivel, tras cumplir su misión, el guardián regresa a casa.

---

## Jugabilidad

El objetivo principal es llegar al final de cada nivel evitando enemigos y peligros del entorno.

### Mecánicas principales

- Movimiento horizontal y salto
- Física básica con gravedad
- Detección y resolución de colisiones con plataformas
- Sistema de cámara con seguimiento del jugador

### Controles

- **A** — Mover a la izquierda  
- **D** — Mover a la derecha  
- **SPACE** — Saltar  
- Click del mouse — Navegación en menús  

---

## Enemigos

El juego incluye dos tipos de enemigos:

- **Triceratops (T)**  
- **Velociraptor (R)**  

Ambos patrullan horizontalmente sobre plataformas y están afectados por gravedad.  
El Velociraptor tiene mayor velocidad de desplazamiento que el Triceratops.

Los enemigos no pueden ser eliminados.  
Cualquier colisión lateral con un enemigo provoca la muerte inmediata del jugador.

---

## Peligros

- **Agua (a)** — Caer en agua provoca la muerte del jugador.
- **Lava (a)** _ Caer en lava provoca la muerte del jugador.
- Al morir, el jugador regresa al menú principal.
- El progreso de niveles desbloqueados se mantiene guardado mediante un sistema de persistencia en JSON.

---

## Niveles

El juego incluye **3 niveles demo**.

Los niveles están definidos mediante arreglos tipo tilemap directamente en el código fuente.  
Cada carácter representa un elemento del juego:

- `.` — Espacio vacío  
- `P` — Plataforma  
- `s` — Relleno de terreno  
- `a` — Agua (mortal)  
- `T` — Triceratops  
- `R` — Velociraptor  

---

## Gestión de Estados

El proyecto implementa un **State Manager** para controlar la transición entre pantallas.

Estados incluidos:

- Main Menu  
- Level Selection  
- Gameplay  
- Game Over  
- Level Complete  
- Pantalla de Controles  

---

## Implementación Técnica

DinoGuard incluye:

- Física básica con gravedad
- Resolución de colisiones separada por ejes (horizontal y vertical)
- Sistema de cámara con seguimiento del jugador
- Estructura orientada a objetos para jugador y enemigos
- Sistema de guardado persistente utilizando archivos JSON

---

## Sistema de Persistencia

El progreso del jugador se almacena en un archivo JSON que registra:

- Nivel actual  
- Niveles desbloqueados  
- Estado de guardado  

Esto permite conservar el avance incluso después de regresar al menú principal.

---

## Requisitos

- Python 3.x  
- Pygame  

Instalación de dependencias:

```bash
pip install pygame
