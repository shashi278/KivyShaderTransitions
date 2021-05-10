from kivy.properties import StringProperty, ColorProperty, OptionProperty
from kivy.uix.screenmanager import ShaderTransition
from kivy.event import EventDispatcher
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.app import MDApp

import glob
from random import shuffle

kv = '''
ScreenManager:
	id: screens
	
	MyScreen:
		#md_bg_color: 1,.6,.4,1
		label_text:"Screen 1"
		name: "screen0"
		source: "busan.jpg"
	
	MyScreen:
		#md_bg_color: .1,.6,1,1
		label_text:"Screen 2"
		name: "screen1"
		source:"lion.jpg"
	
	MyScreen:
		#md_bg_color: .1,.3,.7,1
		label_text:"Screen 3"
		name: "screen2"
		source: "iris.jpg"

<MyScreen@Screen>:
	label_text: 'Hello'
	md_bg_color: 1,1,1,1
	source: ''
	canvas:
		Color:
			rgba: root.md_bg_color if not root.source else [1,1,1,1]
		Rectangle:
			source: root.source
			pos: self.pos
			size: self.size

	BoxLayout:
		MDIconButton:
			pos_hint:{'center_x':0.5,'center_y':0.5}
			icon: "chevron-left"
			on_release: app.switch_prev()

		MDLabel:
			text: root.label_text
			#halign: "center"
			font_size: sp(54)
			theme_text_color: "Custom"
			text_color: 1,1,1,.8
			bold: True
			pos_hint:{'center_x':0.9,'center_y':0.9}

		MDIconButton:
			pos_hint:{'center_x':0.5,'center_y':0.5}
			icon: "chevron-right"
			on_release: app.switch_next()
'''


class CustomTransition(ShaderTransition):
	direction = OptionProperty("lr", options=["lr", "rl"])

	glsl_file = StringProperty("transitions/angular.glsl")

	clearcolor = ColorProperty([0, 0, 0, 0])
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		with open("header.glsl") as header, open(self.glsl_file) as glsl, open("footer.glsl") as footer:
			self.fs = (
				header.read() +
				glsl.read()
				+ footer.read() 
				)

	def add_screen(self, screen):
		super().add_screen(screen)
		self.render_ctx["resolution"] = list(map(float, screen.size))

		aspect_ratio = screen.size[0]/screen.size[1]
		
		if aspect_ratio >= 1:
			self.render_ctx["aspect"] = 1.0

		else:
			self.render_ctx["aspect"] = 2.0

		if self.direction == "lr":
			self.render_ctx["direction"] = 1.0
		
		else:
			self.render_ctx["direction"] = 2.0


class DemoApp(MDApp):

	current_screen = 0
	current_shader = 0
	shader_length = 0

	def switch_next(self):
		glsl_file = self.shader_list[self.current_shader]
		ct = CustomTransition(duration=2, direction="rl", glsl_file=glsl_file)
		self.current_shader = (self.current_shader+1)% self.shader_length

		self.kv.transition = ct
		c = (self.current_screen+1)%3
		self.current_screen = c
		self.kv.current = "screen"+str(c)
	
	def switch_prev(self):
		self.kv.transition = CustomTransition(duration=2, direction="lr", glsl_file="transitions/pageCurl.glsl")
		c = (self.current_screen-1)%3
		self.current_screen = c
		self.kv.current = "screen"+str(c)

	def on_start(self):
		self.shader_list = glob.glob("transitions/*.glsl")
		shuffle(self.shader_list)
		self.shader_length = len(self.shader_list)

		Clock.schedule_interval(self._perform_anim, 2.3)
	
	def _perform_anim(self, *args):
		self.switch_next()

	def build(self):
		self.kv = Builder.load_string(kv)
		return self.kv

DemoApp().run()
