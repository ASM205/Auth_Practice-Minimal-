package PSET1;
INCOMPLETE
public class GreatCircle
{

    public static void main(String args[])
    {
        double x1, x2, y1, y2, r = 6371.0, distance, s2_for_x, s2_for_y;
        
       
        x1 = Math.toRadians(Double.parseDouble(args[0]));
        x2 = Math.toRadians(Double.parseDouble(args[1]));
        y1 = Math.toRadians(Double.parseDouble(args[2]));
        y2 = Math.toRadians(Double.parseDouble(args[3]));

        s2_for_x = Math.pow(Math.sin((x2 - x1)/2), 2);
        s2_for_y = Math.pow(Math.sin((y2 - y1)/2), 2);
        
        distance = 2*r * Math.asin(Math.sqrt(s2_for_x + Math.cos(x1)*Math.cos(x2)*s2_for_y));


        System.out.println(distance + " kilometers");


    }
}