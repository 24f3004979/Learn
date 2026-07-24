Core problem we solve with vue is to make good user experience, streamline development process along with make things into structured organized manner.

```js
<template>
	<h1>
	Application demo
	</h1>
	<component1/>
</template>

<script>
import component from './components/component1.vue'

export default {
	name: 'App',
	// Registering Name for the component
	components: {
		components
	},
	methods:
		function foo(){
			console.log('Functioning :)');
		},
	computed:
		function huu(){
			console.log("computed function");
		}
}
</script>
```

## Default Export usage
Dependency on option API, with wrap of core component with default export we expose this component to rest of the application to use with.
	Options API is traditional way to make components
	Vue internal defined options makes the parsing of an object and does its internal operations into it, giving set of core options for making component usable.
### Core Options
1. data : Function which returns plain JavaScript options, properties defined inside this becomes reactive state of your component.
2. methods : Event handlers, utility operations, mutate state and trigger DOM update.
3. computed : Used to get derived values, cached dataset, re-computes only when required with dependency options
4. watch : asynchronous operations with response to data change
5. props : array of objects used to receive data passed down form parent
6. Lifecycle Hoocks : built in functions , that run with moment in a component's lifecycle.