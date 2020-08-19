from sender import telegramSender
import os

fileName = os.path.basename(__file__)

telegramSender(fileName ,'message vk_message', '365913711', 'error')