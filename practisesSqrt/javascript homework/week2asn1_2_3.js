/*
find largest number function without using math.max() -Updated 190628
*/

const max = (...numbers) => {
  const largest = numbers[0];
  
  for ( var i = 1; i < numbers.length; i++) {
    if (largest < numbers[i]) {
      largest = numbers[i];
    }
  }
  return largest
}

console.log(max(1, 2, 4, 5));
console.log(max(5, 2, 7, 1, 6));
console.log(max(500, 200, 900));


/*
function maxx(numbers) {
  var arr = numbers;
  var largest = arr[0];
  for (var i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    }
  }
  return largest;
}
console.log(maxx("1, 2, 3, 4"));
console.log(maxx("5, 2, 7, 1, 6"));
*/




/*
find 2 different methods to create a proper object as a parameter of the calculate function -updated 190628
*/

// new method 2


const foo2 = function(op, n1, n2) {
	
	this.op = op;
	this.n1 = n1;
	this.n2 = n2;
}

let args = new foo2("+", 1, 2)

//method 1

var foo1 = {
	op: "+",
	n1: 1,
	n2: 2
};


function calculate(args){
	let result;
	if (args.op==="+") {
		result = args.n1 + args.n2;
	}
	else if (args.op==="-") {
		result = args.n1 - args.n2;
	}
	else {
		result = "Not supported";
	}
	return result;
}

calculate(foo1);

//method 2 - cancelled
/*
var values2 = [2, 3];
values.calculates = function calculates(argss){
	let result;
	if(argss==="+"){
		result = values2[0]+values2[1];
	} else if (argss==="-"){
		result=values2[0]-values2[1];
	} else{
		result="Not supported";
	}
	return result;
}
console.log(argss="-");
*/


/*
calculate the average price of all the products - updated 20190628
*/

function avg(data) {
	const i = 0;
	data.products.forEach(function(element){
		i += element.price;
	});
	
	return i / data.size;
}

var avg = {
	"size":3,
	"products":[
	{
		name:"prod1",
		price:100
	},
	{
		name:"prod2",
		price:700
	},
	{
		name:"prod3",
		price:250
	}

	]
}

console.log();

/*- cancelled
var avg = {
	"size":3,
	"products":[
	{
		name:"prod1",
		price:100
	},
	{
		name:"prod2",
		price:700
	},
	{
		name:"prod3",
		price:250
	}
	]
};
//console.log(avg.products[0].price, avg.products[1].price, avg.products[2].price);
x = [avg.products[0].price, avg.products[1].price, avg.products[2].price];
function average(data) {
  var sum = 0;
  var count = data.length;
  for (var i = 0; i < count; i++) {
    sum = sum + data[i];
  }
  return sum / count;
}
console.log(average(x));
*/
