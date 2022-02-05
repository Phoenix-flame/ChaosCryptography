let x = 0.01;
let y = 0;
let z = 0;

let x1 = 0.01;
let y1 = 0;
let z1 = 0;




let sigma = 10;
let rho = 28;
let beta = 8.0 / 3.0;

let points = new Array();
let points1 = new Array();


function setup() {
  createCanvas(800, 600, WEBGL);
  
}

function draw() {
  background(0);
  let dt = 0.01;
  let dx = sigma * (y - x) * dt;
  let dy = (x * (rho - z) - y) * dt;
  let dz = (x * y - beta * z) * dt;
  x = x + dx;
  y = y + dy;
  z = z + dz;
  
  let dx1 = (sigma + 0.001) * (y1 - x1) * dt;
  let dy1 = (x1 * (rho - z1) - y1) * dt;
  let dz1 = (x1 * y1 - beta * z1) * dt;
  x1 = x1 + dx1;
  y1 = y1 + dy1;
  z1 = z1 + dz1;


  points.push(new p5.Vector(x, y, z));
  points1.push(new p5.Vector(x1, y1, z1));

  translate(0, 0, -80);
  scale(5);
  stroke(255);
  noFill();
  beginShape();
  for (let v of points) {
    stroke(10, 255, 10);
    vertex(v.x, v.y, v.z);
  }
  endShape();
  

  noFill();
  beginShape();
  for (let v of points1) {
    stroke(255, 10, 10);
    vertex(v.x, v.y, v.z);
  }
  endShape();

}
