# Documentation of Sketch

The original sketch was a simple p5 sketch which consisted of a setup function in which the canvas was created along with a pizza base. The draw function then drew these shapes on the canvas. Lastly there was some user interface in the shape of a mousePressed function which drew a piece of pepperoni where the mouse was clicked. 

There is a link to the license for the initial code in my example page at the top on the left. 

## What changes have I made?
 - There are now three different sizes of pizzas available as well as six toppings of varying shape, size and colour. 
 -  There is a modal containing instructions. 
 -  The text on the button of the currently selected topping goes red when clicked. 
 -  If you click on the canvas but miss the pizza, an alert box comes up to inform you of this. 
 -  There is also a cost calculator which calculates the cost of your pizza depending on the size of base chosen and the number of each topping added.

## Explanation of code
I start by defining the global variables including the different toppings and base sizes. E.G.

```javascript
var BaseEnum = { "Small": 1, "Medium": 2, "Large": 3 };
Object.freeze(BaseEnum);
```
I also define the current topping and base selected along with the their initial values.
```javascript
var topping;
var base;
var mouseX;
var mouseY;
topping = ToppingsEnum.Pepperoni;
base = BaseEnum.Small;
```
There is a handy variable called DEBUG which when set to true forces the console to log certain information. E.G.
```javascript
if (DEBUG == true) {
      console.log("draw_base", this._d, z);
    }
```
This was particularly useful when debugging my code as it allowed me to see where I was going wrong so I could find a solution.

I created a class for the pizza base which changes based on what size you select. This utilises get and set methods to change the size and cost of the base.
```javascript
class pizza_base {
  constructor(d, cost) {
    this._d = d;
    this._cost = cost; //cost of pizza base
  }
  get d() {
    return this._d;
  }
  set d(newd) {
    this._d = newd;
  }

  get cost() {
    return this._cost;
  }
  set cost(new_cost) {
    this._cost = new_cost;
  }
```
In this method the x and y coordinates of the mouse click are recorded and used to calculate the 'size' of the mouse to find out if the click is on the pizza or not. If it is then the topping is drawn. However if the 'size' of the mouse implies that the click missed the pizza but hit the canvas then an alert box comes up saying "You missed the pizza!" Obviously whether or not the mouse hits the pizza depends on the size of base chosen so the condition includes `this._d` (The size of the base chosen). 
```javascript
All_Tests(mouseX, mouseY) {

    var mouseSize = Math.sqrt((Math.pow((mouseX - this._d), 2) + Math.pow((mouseY - this._d), 2)));

    if (mouseSize <= this._d * 0.88) {
      draw_topping(mouseX, mouseY, topping);
    }

    if ((mouseSize >= this._d) && (mouseSize <= this._d * 1.4)
      && (mouseY >= 0) && (mouseY <= this._d * 2) && (mouseX >= 0)
      && (mouseX <= this._d * 2)) {
      alert("You missed the pizza!");
    }
  }
  ```
Next is the draw method which draws the pizza based on which size is selected.

I then created a toppings class which records the number of each topping(n) along with the setable location(x), location(y), Cost(cost) and Radius(r)
```javascript
class pizza_topping {
  constructor(x, y, r, n, cost) {
    this._x = x;
    this._y = y;
    this.radius = r;
    this._n = n
    this._cost = cost;
  }
  get x() {
    return this._x;
  }
  set x(newX) {
    this._x = newX;
  }
  get y() {
    return this._y;
  }
  set y(newY) {
    this._y = newY;
  }
  get n() {
    return this._n;
  }
  set n(newN) {
    this._n = newN;
  }
  get cost() {
    return this._cost;
  }

  addOnetoN() {
    this._n += 1;
  }
```

It also contains the draw method for each topping such as 
```javascript
draw_pepperoni() {
    stroke(90, 20, 60);
    strokeWeight(2);
    fill(124, 29, 29);
    ellipse(this.x, this.y, this.radius);
  }
  ```
  The `addOnetoN()` method increases the number n of each type of topping when one is added to the pizza. This helps to calculate the cost of the pizza later on.
  
  Next the bases and toppings are instantiated  `let SmallPizza = new pizza_base(250, 300);`  (Radius, Cost(Pence)). `let sausage = new pizza_topping(30, 30, 50, 0, 8);` (default_x, default_y, Size, Number_of topping_on Pizza, Cost of topping (pence)
  
  We now move onto the main functions. These set the default base and topping and draw the canvas. 
  Event Function mousePressed changes the base when you click on a different size and in doing so resets the canvas.
  ```javascript
  function mousePressed() {
 
  switch (base) {
    case 1:
      // Pizza_base_small, test conditions
      SmallPizza.All_Tests(mouseX, mouseY);
      break;
    case 2:
      // Pizza_base_medium, test conditions
      MediumPizza.All_Tests(mouseX, mouseY);
      break;
    case 3:
      // Pizza_base_large, test conditions
      LargePizza.All_Tests(mouseX, mouseY);
      break;
    default:
      SmallPizza.All_Tests(mouseX, mouseY);//default is small pizza
  }

  if (DEBUG == true) {
    console.log("mousePressed", mouseX, 
    mouseY);
  }
}
  ```
  The function `draw_topping(mouseX, mouseY, topping)` switches between toppings when you click on each button. I included the `addOnetoN()` method to keep track of the number of each topping. 
  
  Event Function such as `js_Pepperoni()` use the function `SetRed()` to make sure that when you click on a topping the text on the button turns red so that the user knows which topping is selected. 
  ```javascript
  function js_Pepperoni() {
  SetRed("jsPepperoni");
  topping = ToppingsEnum.Pepperoni;
  if (DEBUG == true) {
    console.log("Pep_buttonPressed", topping);
  }
}
```
```javascript
function SetRed(type1) {
  if (DEBUG == true) {
    console.log("Button Font SetRed", type1);
  }
  document.getElementById("jsPepperoni").style.color = "black";
  document.getElementById("jsPineapple").style.color = "black";
  document.getElementById("jsMushroom").style.color = "black";
  document.getElementById("jsSausage").style.color = "black";
  document.getElementById("jsPepper").style.color = "black";
  document.getElementById("jsChilli").style.color = "black";
  document.getElementById(type1).style.color = "red";
}
```
The function `pizza_cost()` calculates the total cost of the pizza by adding up the `total_cost` variable (The cost of the pizza base) and the cost of each topping times the number n of each topping.
```javascript
function pizza_cost() {

  var total_cost;
  switch (base) {
    case 1:
      // Pizza_base_small, test conditions
      total_cost = SmallPizza.cost;
      break;
    case 2:
      // Pizza_base_medium, test conditions
      total_cost = MediumPizza.cost;
      break;
    case 3:
      // Pizza_base_large, test conditions
      total_cost = LargePizza.cost;
      break;
    default:
      total_cost = SmallPizza.cost;//default is pepperoni
  }

  total_cost = total_cost + ((pepperoni.n * pepperoni.cost) + (pineapple.n * pineapple.cost));
  total_cost = total_cost + ((mushroom.n * mushroom.cost) + (pepper.n * pepper.cost));
  total_cost = (total_cost + ((sausage.n * sausage.cost) + (chilli.n * chilli.cost))) / 100;

  if (DEBUG == true) {
    console.log("Pizza_cost", total_cost);
  }

  document.getElementById('Cost_of_pizza').value = total_cost;
  return;
}
```
The total cost is then displayed on the page.

The `handleClick(myRadio)` Event function makes sure that when you click on a button to change the size of the pizza, the old pizza is cleared. It makes use of the `pizza_cost_reset()` function to reset the total cost of the pizza and record the price of the new pizza base.

My HTML page contains links to the p5 addon files as well as my javascript file. Its here that I included the license. 

I implemented a modal in my HTML page. This is a window that pops up over the page and in it I wrote some instructions.   
```javascript
<button id="myBtn">Instructions</button>
  <div id="myModal" class="modal">
    <div class="modal-content">
      <span class="close">&times;</span>
```

I include my buttons in this file with references to functions in my javascript files such as `handleClick(this)` and `js_Pepperoni()`. This is also where I put the `Cost_of_pizza` label. 
