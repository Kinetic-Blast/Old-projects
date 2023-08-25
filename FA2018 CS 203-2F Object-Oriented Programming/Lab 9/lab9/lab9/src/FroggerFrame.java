import javax.swing.JFrame;
import javax.swing.Timer;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

/**
 * the frame contains a frogger game.
 */
public class FroggerFrame extends JFrame{
	
	private FroggerComponent component;
	
	/**
	 * construct the frame		
	 */
	public FroggerFrame() {
		
		component = new FroggerComponent();
		add(component);
		
		
		// set timer event
		int Time = 500;
		new Timer (Time , e -> {
			component.Move();
		}).start();
		
		
		//add key listener to component 
		component.addKeyListener(new KeyListener () {

			@Override
			public void keyPressed(KeyEvent arg0) {
				component.moveFrogLocation(arg0);}

			@Override
			public void keyReleased(KeyEvent arg0) {
				// TODO Auto-generated method stub
				
			}

			@Override
			public void keyTyped(KeyEvent arg0) {
				// TODO Auto-generated method stub
				
			}
			
		});
		
		
		
		component.setFocusable(true);
		component.requestFocus();
	}	
}

