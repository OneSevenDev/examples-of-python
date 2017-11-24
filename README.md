# Lo aprendido del libro: **Learning Python design patterns *Segunda Edición*** proporcionado por [Packtpub](https://www.packtpub.com), [buy](https://www.packtpub.com/application-development/learning-python-design-patterns-second-edition) :credit_card:

## Capitulo 1

### Logrando comprender de manera teorica y ejemplificada lo siguiente:
* abstraccion
* composicion
* herencia
* polimorfismo

### Existen 3 grupo de patrones de diseño:
1. Patron creacional
2. Patron estructural
3. Patron de comportamiento

### Resumen:
> Cada patron de diseño es completamente util y funcional de acuerdo al contexto en el que se presente, como todo desarrollador debe analisar el contexto y aplicar el patron necesario. Recordar que al momento de crear una abstracción se debe considerar en que esta sea explicitamente para una funcionalidad, de considerar mas de una funcionalidad o añadido es recomendable dividirlo.

## Capitulo 2

### Recomendaciones
- El patron singleton se usa para poder instanciar unicamente una clase, para el caso de usar conexiones a base de datos, esto lo mantendria sincronizada.
- Este patron optimiza recursos al tener una unica instancia siendo llamada.
- Es un patron comprobado durante el tiempo para acceder globalmente a una instancia.

### Desventajas
- Al ser una variable global, esta puede ser modificada por error alterando a las demas llamadas.
- Se puede tener una clase que consume muchos recursos que terminan sin utilizarce.

### Resumen:
> Es recomendable usar singleton cuando se quiere una unica clase global que este sincronizada, se debe tener en cuenta que existen una variación en el patron sigleton, madiante la creación de distintas instancias con el mismo estado.