public class OverRiding {
    public static void main(String args[]) {
        Job job = new Job();
        job.name = "KMS";
        job.age = 24;
        job.job = "학생";
        job.info();
    }
}
    class Man {
        public String name;
        public int age;

        public void info() {
            System.out.println("이름 : " + name + ", 나이 : " + age);
        }
    }
    class Job extends Man {
        String job;

        public void info() {
            super.info();
            System.out.println("직업 : " + job);
        }
    }
