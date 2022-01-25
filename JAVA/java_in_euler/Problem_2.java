public class Problem_2{
  public static void main(String[] args){
    int num1 = 1;
    int num2 = 1;
    int num3 = 0;
    int result = 0;
    for(int i=1; i<=100; i++){
      if(i<=100 && num1<4000000){
      num3= num2;
      num2= num1;
      num1= num1+num3;
      if(num1%2==0){
        result += num1;
        }
      }
    }
    System.out.println(result);
  }
}
