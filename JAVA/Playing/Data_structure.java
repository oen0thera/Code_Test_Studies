public class Data_structure{
  String name;

  public void setName(String name){
    this.name = name;
  }
  public static void main(String[] args){
    Data_structure pos = new Data_structure();
    pos.setName("Hello");
    System.out.println(pos.name);
  }
}
