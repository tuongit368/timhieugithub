"""This module is the main entry for the Py-Climber game"""

import src.game_functions as gf
from src.image_resources import ImageResources
from src.settings import Settings
from src.tilemap import Tilemap
import random
import pygame

def run_game():
    """Main entry point for Py-Climber"""
    
    # Khởi động đối tượng pygame
    pygame.init()

    random.seed()

    # Tải đối tượng cài đặt và tài nguyên hình ảnh của chúng tôi, I/O đĩa có thể được thực hiện trước
    settings = Settings()
    image_res = ImageResources(settings)

    # Thêm vào bộ đệm để có thể truy cập được khi cần
    settings.image_res = image_res
    
    # Tạo màn hình chính để hiển thị dựa trên cài đặt
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    
    # Tạo sơ đồ ô 2D - thao tác này lấy danh sách các chỉ mục và danh sách hình ảnh để tạo ra bề mặt lát gạch
    tile_map = Tilemap(settings, screen, settings.map_indicies, image_res.tile_images, 
        image_res.block_image, image_res.blob_exit_images, image_res.player_sprite_images, image_res.enemy_blob_images)

    # Ghi đè các chỉ mục mặc định bằng bản đồ được tạo
    tile_map.generate_basic_map(settings.map_number_floors , settings.map_number_subfloors)

    #Đặt lại trò chơi
    gf.reset_game(tile_map)

    # Sử dụng quản lý vòng lặp đơn giản của pygame để có 30 FPS cố định
    clock = pygame.time.Clock()
    while True:
        # Nên đảm bảo mỗi khung hình dành ít nhất 1/30 giây trong vòng lặp này
        # nhược điểm là lãng phí giấc ngủ trên phần cứng nhanh và phần cứng chậm sẽ bị lag
        # nhưng phần cứng chậm sẽ luôn bị trễ và triển khai dựa trên đồng bằng thời gian
        # vòng lặp cho trò chơi đơn giản này là IMHO quá mức cần thiết.
        clock.tick(30)

        # Xử lý các sự kiện hệ thống (nhấn phím, cần điều khiển, v.v.)
        gf.check_events(settings, screen, tile_map)
        # Cập nhật trò chơi (điều này sẽ cập nhật tất cả đối tượng phụ và hiển thị chúng trên màn hình)
        gf.update_screen(settings, screen, tile_map)
    
# Gọi hàm trên khi script chạy
run_game()
