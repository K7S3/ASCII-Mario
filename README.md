# supermario

TITLE:
 - To create Super Mario Game in Python3 using OOP on terminal

SCORING:
 - 100 for killing an enemy

FEATURES: 
   
    CODING:
            - PEP 8 Guidelines followed mostly everywhere
            - Commented code
            - Well planned and documented code
            
    GAMEPLAY:
            - Dynamic and relative movement of player and the frame meaning both the player and frame moves giving a realistic feel
            - Gravity feature 
            - 2 player game    
            - Added extra 'down' and 'bullet' controls
    
    LEVEL:
            - Multiple levels are implemented  
            - Time between two levels is 5 secs
            - Difficulty varies as the distance needed to complete the level
    SCENERY:        
            - Water and pits on floor are randomly generated
            - Obstacles on ground are generated with different shapes and sizes at random places
            - Floating bricks are randomly generated
            - Presence of clouds
    ENEMY:
            - Randomly moves on ground
            - Worth 100 points
            - If collided player loses life
    PLAYER:
            - Can shoot bullets
            - Has a life
    CONTROLS:
    
        MARIO:
            - A: left
	        - S: down
	        - D: right
	        - W: up
	        - X: shoot
	        - Q: quit
	    LUIGI:
	        - 4: left
	        - 5: down
	        - 6: right
	        - 8: up
	        - 2: shoot
	        - 7: quit
	BONUS:
	        - 2 player game
	        - Multiple level
	        - Has Sound
	        - Has Colour
	OOPs:
	        - Inheritance: Multilevel Inheritance involving the base class sprite and classes bullet, character, brick being inherited from them
	            -Sprite
	                - Character
	                    - Mario
	                    - Luigi
	                    - Enemy
	                - Brick
	                    - Floor
	                - Bullet
	                - Cloud
	        - Polymorphism: Calling same methods for different objects using the same abstraction or method
                    - Having multiple types of bricks but using same add_bricks() function
                    - Having same collision detection function for all characters.
            - Abstraction :- Hide inner details from user
                    - In floor.py add_all function calls three private functions for adding floor, pits and water
                    - In character check_obstacle function need not be accessed by class instances.
            - Encapsulation: Class and object based approach for all the functionality implemented.
            - Modularity - Code is modular and separated in different files
            
            