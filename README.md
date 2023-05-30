# RAID4UdeAServer

Haciendo uso del conocimiento que se tiene de los RAID's configuramos una maquina que tiene instalado ubuntu server, a su board se conecta una tarjeta RAID que conecta 8 discos de 1Tb, probaremos configuraciones RAID y realizaremos un diseño experimental para verificar su rendimiento

## Primer acercamiento: configuración física

El día jueves 11-05-23, Kai y Miguel, junto con Danny, realizan la configuración física de la maquina.
La configuración de ubuntu server estuvo completa, se verificó que se pudiera acceder a ella desde los computadores del LIS

## Segundo acercamiento: estado inicial de la maquina y los discos

El día viernes 12-05-23, Carlos solicita VPN para poder acceder al servidor desde fuera de UdeA. Se gestiona el permiso Con Hernando Silva, el a su vez da instrucción a un monitor para que nos de acceso. El acceso es enviado a los contactos del equipo. Kai verifica que se puede acceder desde afuera.

Desde el LIS, Carlos realiza el chequeo del estado inicial de la maquina, hace instalaciones y planea la forma de realizar el arreglo RAID o los arreglos RAID. Una cuestión que se considera importante es el chequeo de temperatura, se hace la instalación pertinente para chequearla mediante el comando: sensors
Siguiente cuestión previa a realizar cualquier RAID es conocer cuales son las propiedades del equipo, del software y de cada uno de los discos.
Se instalan varios programas para hacer benchmark: fio no funcionó, el otro era básico y finalmente se instaló con el cual realizaremos pruebas.
Se instala python para poder crear un script que ejecute el diseño eperimental.
Se hace benchmark a un disco y funciona.
Se crea un script para realizar 4 pruebas de benchmark y no funciona. Estamos escribiendo el script.
El día 16 de mayo se crea por Miguel el Benchmark Bonnie++, para registrar el rendimiento de cada disco de manera automatizada.

Requisitos del script para realizar el benchmark:
Debido a que estamos generando una automatización y el script corre pero no se conoce el estado de la prueba, es importante mostrar en pantalla el porcentaje de avance o el estado de la prueba, de modo que el script creado dirá en qué prueba va del total de pruebas.
El equipo comunicará a sus pares cuando alguno esté utilizando el servidor para evitar generar ruidos en la prueba.
Antes de cada prueba se tomará la temperatura y se registrará en un archivo csv o xls.
Considerando datos a recopilar según el benchmark seleccionado.
  
