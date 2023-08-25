import javax.swing.JFrame;


public class FroggerTester {
	public static void main(String[] arg){
		
		JFrame frame = new FroggerFrame();
		frame.setSize(1025, 360);
		frame.setTitle("Frogger");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
		
	}

}
