


        //Write your code here

for(int i=0;i<n;i++)
{
    //inserting string values to bigdecimal
    BigDecimal First=new BigDecimal(s[i]);
    int index=i;
    for(int j=i+1;j<n;j++)
    {
        //second BigDecimal to compare the first Bigdecimal
        BigDecimal Second=new BigDecimal(s[j]);

        //comparing if First element is greater that second element
        //if the First element is greater than Second element than compareTo() returns 1

        if(Second.compareTo(First)==1){
            First=Second;
            index=j;
        }
    }

    //temporary variable to store s[i] value

        String temp=s[i];
        s[i]=s[index];
        s[index]=temp;
}
      
 
