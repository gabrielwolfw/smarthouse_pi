# smarthouse_pi

## Creación Carpeta meta-toolchain
Paso 1:
```
source oe-init-build-env rpi4
```

Paso 2:
```
cd ..
```

Paso 3:
```
bitbake-layers create-layer meta-toolchain
```



## Toolchain
Ejecutar script para configuración de ambiente de compilación, utilizando el toolchain
instalado:

```
. /opt/poky/5.0.9/environment-setup-cortexa7t2hf-neon-vfpv4-poky-linux-gnueabi
```

Comprobar el ambiente:
```
echo $CC
```

Luego se debe hacer un a ejecución:
```
make
```

