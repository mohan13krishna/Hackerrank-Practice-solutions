
public static int B,H;
private static boolean flag = false;

static
{
    Scanner sc = new Scanner(System.in);
     B = sc.nextInt();
     H = sc.nextInt();
    if(B>0 && H>0)
    {
        flag = true;
    }
    else
    {
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}



