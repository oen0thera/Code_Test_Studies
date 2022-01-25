import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;


public class Data{
  private String cat;
  private String dog;
  private String Berd;

  String[] animals_array={"Russian_blue","chihuahua",  "Parrot"};
  List<String> animals_list = new ArrayList<String>(Arrays.asList(animals_array));

  public void in_Animal(String cat, String dog, String Berd){
    if(animals_list.contains(cat)){
      System.out.println("cat:"+cat);
    }else{
      throw new IllegalArgumentException("Not in animals_list");
    }
    if(animals_list.contains(dog)){
      System.out.println("dog:"+dog);
    }else{
      throw new IllegalArgumentException("Not in animals_list");
    }
    if(animals_list.contains(Berd)){
      System.out.println("Berd:"+Berd);
    }else{
      throw new IllegalArgumentException("Not in animals_list");
    }

    this.cat = cat;
    this.dog = dog;
    this.Berd = Berd;

  }
}
