import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JComponent;
import javax.swing.Timer;

/**
 * This component displays a rectangle field with a frog and a car. 
 */
public class FroggerComponent extends JComponent{

	private static final long serialVersionUID = 1L;
	private static final int FIELD_X = 0;  // the X coordinate of the field
	private static final int FIELD_Y = 0;  // the Y coordinate of the field
	private static final int FIELD_HEIGHT = 300;  // the height of the field
	private static final int FIELD_WIDTH = 1000;  // the width of the field
	
	private int carX;   // the X coordinate of the car
	private int carY;   // the Y coordinate of the car
	private int frogX;  // the X coordinate of the frog
	private int frogY;  // the Y coordinate of the frog
	private boolean enabled; // an event watcher. Becomes true when user wins or loses
	
	/**
	 * construct an initial state of the game.
	 * car starts from the left middle lane
	 * frog stays in middle bottom lane
	 */
	public FroggerComponent(){
		this.carX = 0;
		this.carY = 100;
		this.frogX = 450;
		this.frogY = 200;
		this.enabled = false;
	}
	
	/**
	 * draw on the component
	 * @param g the graphics context
	 */
	public void paintComponent(Graphics g){
		
		Graphics2D g2 = (Graphics2D) g;
		
		// draw the field 
		g2.drawRect(FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT);
		g2.setColor(Color.green);
		g2.fillRect(FIELD_X, FIELD_Y, FIELD_WIDTH, FIELD_HEIGHT);
		g2.setColor(Color.gray);
		g2.fillRect(FIELD_X, FIELD_HEIGHT/3 , FIELD_WIDTH, FIELD_HEIGHT/3);
		
		//import the image of car and frog
		BufferedImage imgCar = null;
		BufferedImage imgFrog = null;
		try{
			imgFrog = ImageIO.read(new File("froggreen.png"));
			imgCar = ImageIO.read(new File("simplecar.png"));	
		}
		catch(IOException e){System.out.println("Could not open input file");}	
		
		// draw the car and frog
		g2.drawImage(imgCar, carX, carY, FIELD_WIDTH / 5, FIELD_HEIGHT / 3, null);
		g2.drawImage(imgFrog, frogX, frogY, FIELD_WIDTH / 10, FIELD_HEIGHT / 3, null);	
		
		//set the format of the message showed when user loses or wins
		final int frontSize = 100;          
		final int StringBasePointX = 300;   
		final int StringBasePointY = 80;   
		
		// when frog arrives to the top, game stops and show "You win!"
		if ( frogY == 0 ){
			
			g2.setColor(Color.RED);
			g2.setFont(new Font("Arial", Font.BOLD, frontSize));
			g2.drawString("You win!", StringBasePointX, StringBasePointY);
			enabled = true;
		}
		
		//when frog and car crash, game stops and show "You lose!"
		if( frogY == carY && ((frogX <= carX && (carX - frogX) < 100) || ( frogX > carX && (frogX - carX) < 200))){
			g2.setColor(Color.RED);
			g2.setFont(new Font("Arial", Font.BOLD, frontSize));
			g2.drawString("You lose!", StringBasePointX, StringBasePointY);
			enabled = true;
		}
	}
	
	
	
	/**
	 * adjust location of the frog according to the user keyboard input 
	 * @param e key board event
	 */
	public void moveFrogLocation(KeyEvent e){
		
		if (enabled){return;} // when crash or win happen, stop the KeyListener
		int keyPressed = e.getKeyCode();
		if (keyPressed == KeyEvent.VK_UP) {
			frogY = frogY - 100;
			repaint();
			
		}
		
		

	}
	
	
	/**
	 * move the car and frog according to time and user input.
	 * 
	 */
	public void Move(){
		
		if (enabled){return;} //when crash or win happen, time listener stops
		
		//update car location by 1/4 of its lenght
		carX = carX+100;
		repaint();
	}}

