public class Main  {
    public static void main(String[] args) {
        String name = "Seemakurthi Rohith Kishan";
        String[] education = {
            "Narayana Concept School (2016)",
            "Narayana Junior College (2018)",
            "Presidency University (2022)"
        };
        String[] hobbies = {
            "watching movies",
            "playing badminton",
            "editing videos",
            "reading novels"
        };
        String email = "seemakurthiKishan@gmail.com";
        String contactNumber = "+91 7794879128";
        String instagramId = "Rohith rama";
        String facebookId = "Rohith Seemakurthi";

        System.out.println("=====================================");
        System.out.println("             RESUME                  ");
        System.out.println("=====================================");
        System.out.println("Name: " + name);
        System.out.println("\nEducational Background:");
        for (String edu : education) {
            System.out.println("- " + edu);
        }
        System.out.println("\nHobbies:");
        for (String hobby : hobbies) {
            System.out.println("- " + hobby);
        }
        System.out.println("\nContact Details:");
        System.out.println("- Mail Id: " + email);
        System.out.println("- Contact Number: " + contactNumber);
        System.out.println("\nSocial Media:");
        System.out.println("- Instagram ID: " + instagramId);
        System.out.println("- Facebook ID: " + facebookId);
        System.out.println("=====================================");
    }
}
