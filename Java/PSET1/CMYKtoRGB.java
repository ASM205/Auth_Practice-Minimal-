package PSET1;

public class CMYKtoRGB
{
    public static void main(String args[])
    {
        int red,green ,blue;
        double cyan = Double.parseDouble(args[0]),
        magenta = Double.parseDouble(args[1]),
        yellow = Double.parseDouble(args[2]),
        black = Double.parseDouble(args[3]), white;



        white = 1-black;
        red = (int) (255 * white * (1-cyan));
        green = (int) (255 * white * (1 - magenta));
        blue = (int) (255 * white *(1-yellow));

        System.out.println("red = " + red + "\ngreen = "+ green+ "\nblue = "+ blue);


    }
}