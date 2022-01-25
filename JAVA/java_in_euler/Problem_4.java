import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Collections;

public class Problem_4{

  public static void main(String[] args){
    ArrayList<Integer> Result = new ArrayList<>();
    for(int i=100; i<1000; i++)
    {
      for(int j=100; j<1000; j++)
      {
        ArrayList<String> Rundown = new ArrayList<>();
        String mul = Integer.toString(i*j);
        for(int k=0;k<mul.length(); k++)
        {
          Rundown.add(mul.substring(k,k+1));
        }
        if(mul.length()%2==0)
        {
          int count = 0;
          for(int n=0;n<mul.length()/2;n++)
            {
            if(Integer.parseInt(Rundown.get(n))==Integer.parseInt(Rundown.get(Rundown.size()-1-n)))
              {
              count+=2;
              }
            }
          if(count==Rundown.size())
          {
            Result.add(i*j);
          }
        }
        if(mul.length()%2==1)
        {
          int count = 0;
          for(int n=0;n<mul.length()/2;n++)
            {
            if(Integer.parseInt(Rundown.get(n))==Integer.parseInt(Rundown.get(Rundown.size()-1-n)))
              {
              count+=2;
              }
            }
          if(count==Rundown.size()-1)
          {
            Result.add(i*j);

          }
        }

    }

  }
  Collections.sort(Result);
  System.out.println(Result);
  }
}
