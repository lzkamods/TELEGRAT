import asyncio
import logging

from aiogram import Bot, Dispatcher
from colorama import Fore, Back, Style
from app import config as conf

from aiogram.types import Message, CallbackQuery, FSInputFile, InputMediaPhoto
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import pathlib
from pathlib import Path

from subprocess import call
import webbrowser
from tkinter import *
import pyscreenshot
import pyautogui
import os
import cv2

import app.keyboards as kb
import app.config as conf


from app.main import router
from app.handlers.os_control.scrnsht import s_router
from app.handlers.files import f_router
from app.handlers.os_control.csht import c_router
from app.handlers.os_control.SGGV import sggv_router
from app.handlers.os_control.scrntxt import t_router
from app.handlers.os_control.kptmgr import k_router
from app.handlers.www import w_router
from app.handlers.apps import a_router