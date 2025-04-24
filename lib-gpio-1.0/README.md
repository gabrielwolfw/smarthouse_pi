# Grupo X Yocto 2

**Integrantes:**  
- Kevin Lobo Juarez (2020087823)
- Gustavo Zamora Espinoza (2017137089)
- Eder Vega Suazo (2021067844)

## Estructura
- `build/`: Construcción de la libería y el bin
- `include/`: Encabezados de la biblioteca
- `src/`: Código fuente de la biblioteca y app de prueba
- `Makefile`: Para compilar
- `README.md`: Este documento

## Respuestas a preguntas

**1. ¿Qué pasos debe seguir antes de escribir o leer de un puerto de entrada/salida general (GPIO)?**  
*R:*  
- Exportar el pin GPIO (`echo <n> > /sys/class/gpio/export`) considerar offset 512
- Configurar la dirección del pin (`echo in|out > /sys/class/gpio/gpio<n>/direction`)
- Leer o escribir el valor según corresponda

**2. ¿Qué comando podría utilizar, bajo Linux, para escribir a un GPIO específico?**  
*R:*  
```bash
echo 1 > /sys/class/gpio/gpio<n>/value
```

## Cómo compilar y usar

### 1. Prepara el ambiente de cross-compilación Yocto:
```bash
source /opt/poky/5.0.3/environment-setup-cortexa7t2hf-neon-vfpv4-poky-linux-gnueabi
```

### 2. Compila todo:
```bash
mkdir build && cd build
cmake ..
make
```

### 3. Copia los archivos a la Raspberry Pi:
Copia `lib/libgpio.so` y `bin/app_test_gpio` a la Raspberry (por red o SD).

### 4. En la Raspberry:
```bash
export LD_LIBRARY_PATH=.
chmod +x app_test_gpio
./app_test_gpio
```

## Notas
- Cambia los números de pin GPIO en `app_test_gpio.c` según tu conexión.