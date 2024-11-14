import pygame
import pygame.camera

def capture_image(filename='capture.jpg', camera_name='Cam Link 4K'):
    pygame.camera.init()
    cameras = pygame.camera.list_cameras()
    
    # Print available cameras for debugging
    print("Available cameras:", cameras)
    
    camera_index = -1
    if camera_name in cameras:
        camera_index = cameras.index(camera_name)

    if camera_index > -1:
        try:
            cam = pygame.camera.Camera(camera_index)
            cam.start()
            pygame.time.wait(500)
            img = cam.get_image()
            pygame.image.save(img, filename)
            cam.stop()
            print(f"Image captured from {camera_name} and saved to {filename}")
            return True
        except Exception as e:
           print(f"Error capturing from {camera_name}: {e}")
           return False
    else:
        print(f"Camera '{camera_name}' not found. Available cameras: {cameras}")
        return False

# Example usage
if __name__ == "__main__":

    # file name, camera name
    capture_image('capture.jpg', 'Cam Link 4K')
    