

difference() {
//image visual
scale([1, 1, 1])
  surface(file = "destination.png", center = true, invert = true);

//bottom part for remove
translate([0,0,-80]) 
 cube([1500,1500,80],center=true);

}