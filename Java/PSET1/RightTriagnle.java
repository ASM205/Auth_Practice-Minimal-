package PSET1;

public class RightTriagnle
{
    public static void main(String args[])
    {
        int a,b,c, a2,b2,c2;
        a = Integer.parseInt(args[0]);
        b = Integer.parseInt(args[1]);
        c = Integer.parseInt(args[2]);

        a2 = a*a;
        b2 = b*b;
        c2 = c*c;
        if ( a<0 || b<0 || c<0)
            System.out.println("false");

        if((a2+b2 == c2) || (b2+c2 == a2) || (a2 + c2 == b2))
            System.out.println("true");
        else
            System.out.println("false");
            
    }
}