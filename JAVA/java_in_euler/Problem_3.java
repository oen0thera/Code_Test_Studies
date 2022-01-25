import java.util.List;
import java.util.ArrayList;
import java.math.BigInteger;
//[1, 71, 839, 1471, 6857]

public class Problem_3{
  public static void main(String[] args){
    BigInteger number = new BigInteger("600851475143");
    List<Integer> number_list = new ArrayList<>();
    for(int i=2;i<100000;i++){
      BigInteger remain = number.mod(BigInteger.valueOf(i));
      if(remain==BigInteger.valueOf(0)){
        number = number.divide(BigInteger.valueOf(i));
        System.out.println(i);
        number_list.add(i);
        System.out.println(number);
      }
      if(i==99){
        
      }

    }
    System.out.println(number_list);
  }
}
