
exit()
import sys
import random
import math
import colorsys
import ctypes
import threading
import pygame
import wave
import struct
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import (
    Qt, QTimer, QPoint, QPointF, QRect, QUrl
)
from PyQt5.QtGui import (
    QPainter, QColor, QFont, QPainterPath,
    QLinearGradient, QRadialGradient, QPen, QBrush
)
from PyQt5.QtMultimedia import QSoundEffect

#########################################################
#          Sound Generation for Rain + Lightning
#########################################################

def generate_lightning_sound(filename="lightning.wav"):
    """generates a short lightning-like crackle. lower amplitude so it's not so loud"""
    framerate = 44100
    duration = 0.2
    amplitude = 15000  # reduced amplitude from 32767 -> 15000
    n_samples = int(framerate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, framerate, n_samples, 'NONE', 'not compressed'))
        for i in range(n_samples):
            t = i / framerate
            val = int(amplitude * math.exp(-40 * t)) if i < framerate * duration else 0
            data = struct.pack('<h', val)
            wav_file.writeframesraw(data)

def generate_rain_sound(filename="rain.wav"):
    """generates simpler, quieter white noise for rain."""
    framerate = 44100
    duration = 2.0
    amplitude = 8000  # significantly reduced amplitude
    n_samples = int(framerate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, framerate, n_samples, 'NONE', 'not compressed'))
        for _ in range(n_samples):
            val = random.randint(-amplitude, amplitude)
            data = struct.pack('<h', val)
            wav_file.writeframesraw(data)

if not os.path.exists("lightning.wav"):
    generate_lightning_sound()
if not os.path.exists("rain.wav"):
    generate_rain_sound()

#########################################################
#                Block Blast Game (Thread)
#########################################################

class BlockBlastGameThread(threading.Thread):
    """Runs the block-blast game in a separate thread."""
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.running = False

    def run(self):
        self.running = True
        pygame.init()

        # simple 800x600 window
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Block Blast!")
        clock = pygame.time.Clock()

        font = pygame.font.Font(None,36)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            screen.fill((40,40,40))
            textsurf = font.render("Block Blast! Game Running...", True, (255,255,255))
            screen.blit(textsurf,(50,50))

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def stop(self):
        self.running = False

#########################################################
#        Reality Distortion Effects
#########################################################

class SonderEffectsSuite(QWidget):
    """Single overlay window that can do any effect: quantum, fractals, etc."""
    def __init__(self):
        super().__init__()

        # window config
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.set_click_through()

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_effect)
        self.timer.start(16)

        # Current effect
        self.current_effect = None
        self.game_thread = None

        # load quieted sounds
        self.sounds = {}
        self.sounds['lightning'] = QSoundEffect()
        self.sounds['lightning'].setSource(QUrl.fromLocalFile(os.path.abspath("lightning.wav")))
        self.sounds['lightning'].setVolume(0.3)  # quieter

        self.sounds['rain'] = QSoundEffect()
        self.sounds['rain'].setSource(QUrl.fromLocalFile(os.path.abspath("rain.wav")))
        self.sounds['rain'].setVolume(0.2)  # fairly quiet

        # store effect data
        self.energy_nodes = []
        self.quantum_particles = []
        self.void_portals = []
        self.fractures = []
        self.time_ripples = []
        self.dna_strands = []
        self.tears = []
        self.matrix_chars = []
        self.particles = []
        self.binary_streams = []
        self.lightning_points = []
        self.vortex_particles = []
        self.stars = []
        self.nebulas = []
        self.quantum_fields = []
        self.psychedelic_offset = 0
        self.rain_drops = []

        self.init_all_effect_data()

        self.show()

    def set_click_through(self):
        hwnd = self.winId().__int__()
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x80000
        WS_EX_TRANSPARENT = 0x20
        styles = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        new_styles = styles | WS_EX_LAYERED | WS_EX_TRANSPARENT
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_styles)

    ####################################################
    #  initialize data for each effect (avoid keyError)
    ####################################################

    def init_all_effect_data(self):
        """Initialize enough data to avoid KeyErrors for each effect"""
        # energy
        for _ in range(20):
            node = {
                'pos': QPointF(random.randint(0, self.width()), random.randint(0, self.height())),
                'velocity': QPointF(random.uniform(-2,2), random.uniform(-2,2)),
                'charge': random.choice([-1,1]),
                'energy': random.uniform(0.5,1.0),
            }
            self.energy_nodes.append(node)

        # quantum
        for _ in range(30):
            p = {
                'x': random.randint(0,self.width()),
                'y': random.randint(0,self.height()),
                'wave_phase': random.uniform(0,2*math.pi),
                'frequency': 0.03,
                'amplitude': random.uniform(10,30),
                'uncertainty': random.uniform(5,15),
                'color': QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                'entangled_partner': None
            }
            self.quantum_particles.append(p)
        # pair them
        for i in range(0,len(self.quantum_particles),2):
            if i+1<len(self.quantum_particles):
                self.quantum_particles[i]['entangled_partner'] = self.quantum_particles[i+1]
                self.quantum_particles[i+1]['entangled_partner'] = self.quantum_particles[i]

        # void portals
        for _ in range(2):
            portal = {
                'center': QPointF(random.randint(100,self.width()-100), random.randint(100,self.height()-100)),
                'radius': random.uniform(60,120),
                'rotation': 0,
                'spin_speed': random.uniform(0.01,0.03),
                'particles':[],
                'distortion':1.2
            }
            # add sub particles
            for _ in range(50):
                angle = random.uniform(0,2*math.pi)
                distance = random.uniform(0,portal['radius'])
                portal['particles'].append({
                    'angle': angle,
                    'distance': distance,
                    'speed': random.uniform(0.01,0.03),
                    'size': random.uniform(1,3)
                })
            self.void_portals.append(portal)

        # reality fractures
        for _ in range(3):
            f_points = []
            x = random.randint(0,self.width())
            y = random.randint(0,self.height())
            for _ in range(random.randint(5,8)):
                x+=random.randint(-80,80)
                y+=random.randint(-80,80)
                f_points.append(QPointF(x,y))
            frac = {
                'points': f_points,
                'width': random.uniform(2,4),
                'glow_intensity': random.uniform(0.5,1.0),
                'color': QColor(random.randint(150,255), random.randint(0,100), random.randint(100,255))
            }
            self.fractures.append(frac)

        # time ripples
        # for demo, just an empty list. no random data needed if we never show them
        self.time_ripples = []

        # dna helix
        # store some random strands
        for strand_i in range(2):
            dna_points = []
            for i in range(20):
                dna_points.append({
                    'base_y': i*25,
                    'phase': i*0.3 + strand_i*math.pi,
                    'nucleotide': random.choice(['A','T','G','C']),
                    'color': QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                })
            self.dna_strands.append(dna_points)

        # dimensional tears
        for _ in range(2):
            dt_points = [QPointF(random.randint(0,self.width()), random.randint(0,self.height()))]
            # just some random tears
            dt = {
                'start': dt_points[0],
                'points': dt_points,
                'growth_direction': QPointF(random.uniform(-1,1),random.uniform(-1,1)),
                'width': random.uniform(4,8),
                'color': QColor(random.randint(100,255), random.randint(100,255), random.randint(100,255))
            }
            self.tears.append(dt)

        # matrix
        columns = self.width() // 20
        for x in range(columns):
            self.matrix_chars.append({
                'x': x*20,
                'y': random.randint(-500, 0),
                'speed': random.uniform(3,7),
                'length': random.randint(5,15),
                'chars': [chr(random.randint(0x30A0,0x30FF)) for _ in range(20)]
            })

        # particles
        for _ in range(50):
            self.particles.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(0,self.height()),
                'dx': random.uniform(-1,1),
                'dy': random.uniform(-1,1),
                'size': random.randint(2,6),
                'color': QColor(random.randint(50,255), random.randint(50,255), random.randint(50,255), 150)
            })

        # binary
        columns = self.width() // 15
        for x in range(columns):
            self.binary_streams.append({
                'x': x*15,
                'y': random.randint(-500,0),
                'speed': random.uniform(2,5),
                'length': random.randint(8,15)
            })

        # lightning
        # store some random points
        for _ in range(5):
            self.lightning_points.append((
                random.randint(0,self.width()), 
                random.randint(0,self.height())
            ))

        # vortex
        for _ in range(300):
            angle = random.uniform(0,2*math.pi)
            radius = random.uniform(60, max(self.width(), self.height()))
            self.vortex_particles.append({
                'angle': angle,
                'radius': radius,
                'speed': random.uniform(0.01,0.03),
                'size': random.uniform(1,3),
                'color': QColor(random.randint(50,255), random.randint(50,255), random.randint(50,255))
            })

        # cosmic
        for _ in range(100):
            self.stars.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(0,self.height()),
                'size': random.uniform(0.5,3),
                'twinkle_speed': random.uniform(0.02,0.1)
            })
        for _ in range(3):
            self.nebulas.append({
                'x': random.randint(100,self.width()-100),
                'y': random.randint(100,self.height()-100),
                'size': random.randint(150,300),
                'color': QColor(random.randint(20,200), random.randint(20,200), random.randint(20,200), 80),
                'alpha': random.uniform(0.1,0.3)
            })

        # quantum fields
        for _ in range(2):
            self.quantum_fields.append({
                'offset': random.uniform(0, 2*math.pi),
                'speed': random.uniform(0.01,0.03),
                'wavelength': random.uniform(80,200)
            })

        # psychedelic offset
        self.psychedelic_offset = 0

        # rain is empty initially
        self.rain_drops = []

    #########################################################
    #   Methods to trigger each effect
    #########################################################

    def run_rain(self):
        self.set_effect("rain")

    def run_quantum_particles(self):
        self.set_effect("quantum_particles")

    def run_void_portals(self):
        self.set_effect("void_portals")

    def run_reality_fractures(self):
        self.set_effect("reality_fractures")

    def run_time_ripples(self):
       self.set_effect("time_ripples")

    def run_dna_helix(self):
        self.set_effect("dna_helix")

    def run_dimensional_tears(self):
        self.set_effect("dimensional_tears")

    def run_matrix(self):
        self.set_effect("matrix")

    def run_particles(self):
        self.set_effect("particles")

    def run_binary(self):
        self.set_effect("binary")

    def run_lightning(self):
        self.set_effect("lightning")

    def run_vortex(self):
        self.set_effect("vortex")

    def run_cosmic(self):
        self.set_effect("cosmic")

    def run_quantum(self):
        self.set_effect("quantum")

    def run_psychedelic(self):
        self.set_effect("psychedelic")

    def run_block_blaster(self):
        self.launch_game()

    def clear(self):
        self.clear_effect()
        
    #########################################################
    #  set_effect / clear_effect
    #########################################################

    def set_effect(self, effect_name):
        self.current_effect = effect_name
        print(f"Effect '{effect_name}' activated.")
        if effect_name == "rain":
            # init some rain
            self.init_rain()
            self.sounds['rain'].setLoopCount(QSoundEffect.Infinite)
            self.sounds['rain'].play()
        elif effect_name == "lightning":
            self.sounds['lightning'].play()

    def clear_effect(self):
        print("All effects cleared.")
        self.current_effect = None
        # stop any sounds
        for s in self.sounds.values():
            s.stop()

        # stop game
        if self.game_thread and self.game_thread.running:
            self.game_thread.stop()
            self.game_thread = None

    #########################################################
    #  optional init for rain
    #########################################################

    def init_rain(self):
        self.rain_drops = []
        # continuously spawn new drops 
        # but let's also spawn a bunch at once
        for _ in range(100):
            self.rain_drops.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(-self.height(),0)
            })

    #########################################################
    #  update_effect calls
    #########################################################

    def update_effect(self):
        # call the update method for whichever effect is active
        if self.current_effect == "rain":
            self.update_rain()
        # if we have more updates for other effects
        elif self.current_effect == "quantum_particles":
            self.update_quantum_particles()
        elif self.current_effect == "void_portals":
            self.update_void_portals()
        elif self.current_effect == "reality_fractures":
            pass  # or define update if needed
        elif self.current_effect == "time_ripples":
            pass
        elif self.current_effect == "dna_helix":
            pass
        elif self.current_effect == "dimensional_tears":
            pass
        elif self.current_effect == "matrix":
            self.update_matrix()
        elif self.current_effect == "particles":
            self.update_particles()
        elif self.current_effect == "binary":
            self.update_binary()
        elif self.current_effect == "lightning":
            # or define logic
            pass
        elif self.current_effect == "vortex":
            self.update_vortex()
        elif self.current_effect == "cosmic":
            pass
        elif self.current_effect == "quantum":
            pass
        elif self.current_effect == "psychedelic":
            self.update_psychedelic()

        self.update()

    def update_rain(self):
        # move drops
        # also spawn new drops 
        if random.random()<0.2:
            # spawn new random drop near top
            self.rain_drops.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(-50,0)
            })
        for drop in self.rain_drops:
            drop['y'] += 6
        # purge drops that fall out
        self.rain_drops = [d for d in self.rain_drops if d['y']<self.height()+20]

    def update_quantum_particles(self):
        # apply wave phase
        for p in self.quantum_particles:
            p['wave_phase'] += p['frequency']
            dx = random.gauss(0, p['uncertainty'])
            dy = random.gauss(0, p['uncertainty'])
            p['x'] += dx
            p['y'] += dy
            # clamp
            p['x'] = max(0, min(self.width(), p['x']))
            p['y'] = max(0, min(self.height(), p['y']))

    def update_void_portals(self):
        for portal in self.void_portals:
            portal['rotation'] += portal['spin_speed']
            for particle in portal['particles']:
                particle['angle'] += particle['speed']
                # spiral in
                if particle['distance']>2:
                    particle['distance'] *= 0.99

    def update_matrix(self):
        for stream in self.matrix_chars:
            stream['y'] += stream['speed']
            if stream['y'] > self.height()+500:
                stream['y'] = random.randint(-500,0)

    def update_particles(self):
        for part in self.particles:
            part['x'] += part['dx']
            part['y'] += part['dy']
            # bounce
            if part['x']<0 or part['x']>self.width():
                part['dx']*=-1
            if part['y']<0 or part['y']>self.height():
                part['dy']*=-1

    def update_binary(self):
        for s in self.binary_streams:
            s['y']+= s['speed']
            if s['y']>self.height()+200:
                s['y'] = random.randint(-500,0)

    def update_vortex(self):
        for v in self.vortex_particles:
            v['angle']+=v['speed']
            v['radius']-=0.2
            if v['radius']<20:
                v['radius'] = max(self.width(), self.height())

    def update_psychedelic(self):
        self.psychedelic_offset+=0.1

    #########################################################
    # paintEvent
    #########################################################

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.current_effect == "rain":
            self.draw_rain(painter)
        elif self.current_effect == "quantum_particles":
            self.draw_quantum_particles(painter)
        elif self.current_effect == "void_portals":
            self.draw_void_portals(painter)
        elif self.current_effect == "reality_fractures":
            self.draw_reality_fractures(painter)
        elif self.current_effect == "time_ripples":
            # no draw_time_ripples defined => do nothing or define
            pass
        elif self.current_effect == "dna_helix":
            # no draw_dna_helix => we can define
            pass
        elif self.current_effect == "dimensional_tears":
            # no draw_dimensional_tears => define or skip
            pass
        elif self.current_effect == "matrix":
            self.draw_matrix(painter)
        elif self.current_effect == "particles":
            self.draw_particles(painter)
        elif self.current_effect == "binary":
            self.draw_binary(painter)
        elif self.current_effect == "lightning":
            # no actual lightning draw for now
            pass
        elif self.current_effect == "vortex":
            self.draw_vortex(painter)
        elif self.current_effect == "cosmic":
            self.draw_cosmic(painter)
        elif self.current_effect == "quantum":
            # we can define a separate quantum effect if needed
            pass
        elif self.current_effect == "psychedelic":
            self.draw_psychedelic(painter)

    #######################################################
    #  drawing stubs for each effect that can be called
    #######################################################

    def draw_rain(self, painter):
        painter.setPen(QPen(QColor(100,100,255,150),2))  # gentle watery color
        for drop in self.rain_drops:
            painter.drawLine(drop['x'], drop['y'], drop['x'], drop['y']+10)

    def draw_quantum_particles(self, painter):
        for p in self.quantum_particles:
            # radius
            r = 10 + math.sin(p['wave_phase'])*p['amplitude']
            # probability cloud
            painter.setPen(Qt.NoPen)
            c = QColor(p['color'])
            c.setAlpha(80)
            painter.setBrush(c)
            painter.drawEllipse(QPointF(p['x'], p['y']), r, r)

            # entanglement line
            if p['entangled_partner']:
                e = p['entangled_partner']
                grad = QLinearGradient(QPointF(p['x'],p['y']), QPointF(e['x'], e['y']))
                grad.setColorAt(0, p['color'])
                grad.setColorAt(1, e['color'])
                pen = QPen(QBrush(grad),1,Qt.DashLine)
                painter.setPen(pen)
                painter.drawLine(QPointF(p['x'],p['y']), QPointF(e['x'], e['y']))

    def draw_void_portals(self, painter):
        painter.setPen(Qt.NoPen)
        for portal in self.void_portals:
            # radial gradient
            rad = QRadialGradient(portal['center'], portal['radius'])
            rad.setColorAt(0, QColor(0,0,0,200))
            rad.setColorAt(1, QColor(0,0,0,0))
            painter.setBrush(rad)
            painter.drawEllipse(portal['center'], portal['radius'], portal['radius'])

            # portal swirl particles
            for pt in portal['particles']:
                angle = pt['angle']+ portal['rotation']
                dist = pt['distance']
                x = portal['center'].x() + math.cos(angle)*dist
                y = portal['center'].y() + math.sin(angle)*dist
                c = QColor(150,0,255,100)
                painter.setBrush(c)
                painter.drawEllipse(QPointF(x,y), pt['size'], pt['size'])

    def draw_reality_fractures(self, painter):
        for frac in self.fractures:
            path = QPainterPath()
            path.moveTo(frac['points'][0])
            for fpt in frac['points'][1:]:
                path.lineTo(fpt)
            # glow
            for i in range(3):
                c = QColor(frac['color'])
                alpha_ = int(100*frac['glow_intensity']/(i+1))
                c.setAlpha(alpha_)
                pen = QPen(c, frac['width']+i*2)
                painter.setPen(pen)
                painter.drawPath(path)

    def draw_matrix(self, painter):
        painter.setFont(QFont('Courier New', 14))
        for stream in self.matrix_chars:
            for i in range(stream['length']):
                ch_y = int(stream['y']) - i*20
                if 0<=ch_y<=self.height():
                    if i==0:
                        painter.setPen(QColor(255,255,255,200))
                    else:
                        alpha = 200-i*15
                        painter.setPen(QColor(0,255,0,max(0,alpha)))
                    # random change
                    if random.random()<0.04:
                        stream['chars'][i] = chr(random.randint(0x30A0,0x30FF))
                    painter.drawText(stream['x'], ch_y, stream['chars'][i])

    def draw_particles(self, painter):
        painter.setPen(Qt.NoPen)
        for part in self.particles:
            painter.setBrush(part['color'])
            painter.drawEllipse(QPointF(part['x'],part['y']), part['size'], part['size'])

    def draw_binary(self, painter):
        painter.setFont(QFont('Courier New',12))
        painter.setPen(QColor(0,255,0,180))
        for s in self.binary_streams:
            for i in range(s['length']):
                ch_y = s['y'] - i*15
                if 0<= ch_y <= self.height():
                    # random 0/1
                    painter.drawText(s['x'], ch_y, str(random.randint(0,1)))

    def draw_vortex(self, painter):
        painter.setPen(Qt.NoPen)
        center_x = self.width()/2
        center_y = self.height()/2
        for v in self.vortex_particles:
            angle = v['angle']
            r = v['radius']
            x = center_x + math.cos(angle)*r
            y = center_y + math.sin(angle)*r
            c = QColor(v['color'])
            c.setAlpha(150)
            painter.setBrush(c)
            painter.drawEllipse(QPointF(x,y),v['size'],v['size'])

    def draw_cosmic(self, painter):
        # stars
        for s in self.stars:
            twinkle = 0.5+0.5*math.sin(self.timer.interval()* s['twinkle_speed'])
            c = QColor(255,255,255,int(twinkle*255))
            painter.setPen(Qt.NoPen)
            painter.setBrush(c)
            painter.drawEllipse(QPoint(s['x'], s['y']), int(s['size']), int(s['size']))
        # nebulas
        for nb in self.nebulas:
            rg = QRadialGradient(QPointF(nb['x'],nb['y']), nb['size'])
            co = nb['color']
            alpha_ = int(255*(nb['alpha']))
            co.setAlpha(alpha_)
            rg.setColorAt(0, co)
            co2 = QColor(co)
            co2.setAlpha(0)
            rg.setColorAt(1, co2)
            painter.setBrush(rg)
            painter.drawEllipse(QPoint(nb['x'],nb['y']), nb['size'], nb['size'])

    def draw_psychedelic(self, painter):
        block = 20
        for xx in range(0, self.width(), block):
            for yy in range(0, self.height(), block):
                val = math.sin(xx*0.02+self.psychedelic_offset)+math.cos(yy*0.02+self.psychedelic_offset)
                col = self.get_rainbow_color((val+2)/4)
                col.setAlpha(100)
                painter.setPen(Qt.NoPen)
                painter.setBrush(col)
                painter.drawRect(xx,yy,block,block)

    #########################################################
    #  helper
    #########################################################

    def get_rainbow_color(self, pos):
        hue = pos%1.0
        r,g,b = colorsys.hsv_to_rgb(hue,1,1)
        return QColor(int(r*255), int(g*255), int(b*255))

    def launch_game(self):
        if not self.game_thread or not self.game_thread.running:
            self.game_thread = BlockBlastGameThread()
            self.game_thread.start()
        else:
            print("Game is already running.")


#########################################################
#           effect controller main window
#########################################################

class EffectController(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.overlay = SonderEffectsSuite()

        # possible effects
        # note that only "rain", "quantum_particles", etc. have real logic
        effects = [
            "energy", "quantum_particles", "void_portals","reality_fractures",
            "time_ripples","dna_helix","dimensional_tears","matrix",
            "particles","lightning","binary","vortex","cosmic",
            "quantum","psychedelic","rain", "block_blaster"
        ]

        btn_layout = QHBoxLayout()
        for eff in effects:
            b = QPushButton(eff.title())
            b.clicked.connect(lambda _, e=eff: self.handle_effect(e))
            btn_layout.addWidget(b)

        layout.addLayout(btn_layout)

        # clear
        clr = QPushButton("Clear Effect")
        clr.clicked.connect(self.clear_effect)
        layout.addWidget(clr)

        self.setLayout(layout)
        self.setWindowTitle("Screen Effects Controller")
        self.resize(800,200)
        self.show()

    def handle_effect(self, effect_name):
       if effect_name=="block_blaster":
            self.overlay.run_block_blaster()
       elif effect_name == "energy":
            self.overlay.run_energy()
       elif effect_name == "quantum_particles":
            self.overlay.run_quantum_particles()
       elif effect_name == "void_portals":
            self.overlay.run_void_portals()
       elif effect_name == "reality_fractures":
            self.overlay.run_reality_fractures()
       elif effect_name == "time_ripples":
            self.overlay.run_time_ripples()
       elif effect_name == "dna_helix":
            self.overlay.run_dna_helix()
       elif effect_name == "dimensional_tears":
            self.overlay.run_dimensional_tears()
       elif effect_name == "matrix":
            self.overlay.run_matrix()
       elif effect_name == "particles":
            self.overlay.run_particles()
       elif effect_name == "lightning":
            self.overlay.run_lightning()
       elif effect_name == "binary":
            self.overlay.run_binary()
       elif effect_name == "vortex":
            self.overlay.run_vortex()
       elif effect_name == "cosmic":
            self.overlay.run_cosmic()
       elif effect_name == "quantum":
            self.overlay.run_quantum()
       elif effect_name == "psychedelic":
            self.overlay.run_psychedelic()
       elif effect_name == "rain":
            self.overlay.run_rain()
       else:
           self.overlay.set_effect(effect_name)

    def clear_effect(self):
        self.overlay.clear()


#########################################################
#                      main
#########################################################

def main():
    app = QApplication(sys.argv)
    ctrl = EffectController()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()


exit()
import sys
import random
import math
import colorsys
import ctypes
import threading
import pygame
import wave
import struct
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import (
    Qt, QTimer, QPoint, QPointF, QRect, QUrl
)
from PyQt5.QtGui import (
    QPainter, QColor, QFont, QPainterPath,
    QLinearGradient, QRadialGradient, QPen, QBrush
)
from PyQt5.QtMultimedia import QSoundEffect

# --------------------- Sound Generation ---------------------

def generate_lightning_sound(filename="lightning.wav"):
    """
    Generates a simple lightning sound (sharp spike) and saves it as a WAV file.
    """
    framerate = 44100
    duration = 0.2  # seconds
    amplitude = 32767
    n_samples = int(framerate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, framerate, n_samples, 'NONE', 'not compressed'))
        for i in range(n_samples):
            # Generate a sharp spike with exponential decay
            t = i / framerate
            value = int(amplitude * math.exp(-50 * t) if i < framerate * duration else 0)
            data = struct.pack('<h', value)
            wav_file.writeframesraw(data)

def generate_rain_sound(filename="rain.wav"):
    """
    Generates a simple rain sound (white noise) and saves it as a WAV file.
    """
    framerate = 44100
    duration = 2.0  # seconds
    amplitude = 32767
    n_samples = int(framerate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, framerate, n_samples, 'NONE', 'not compressed'))
        for _ in range(n_samples):
            # Generate white noise
            value = random.randint(-amplitude, amplitude)
            data = struct.pack('<h', value)
            wav_file.writeframesraw(data)

# Generate sounds if they don't exist
if not os.path.exists("lightning.wav"):
    print("Generating lightning.wav...")
    generate_lightning_sound()
    print("lightning.wav generated.")

if not os.path.exists("rain.wav"):
    print("Generating rain.wav...")
    generate_rain_sound()
    print("rain.wav generated.")

# --------------------- Block Blast! Game ---------------------

class BlockBlastGame(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True  # Ensure thread exits when main program does
        self.running = False

    def run(self):
        self.running = True
        pygame.init()

        # Game constants
        GRID_SIZE = 8  # 8x8 grid
        BLOCK_SIZE = 45  # Adjusted based on grid size and screen
        GRID_WIDTH = GRID_SIZE * BLOCK_SIZE
        GRID_HEIGHT = GRID_SIZE * BLOCK_SIZE
        SCORE_AREA_HEIGHT = 120  # Increased for better spacing
        SCREEN_WIDTH = GRID_WIDTH
        SCREEN_HEIGHT = GRID_HEIGHT + SCORE_AREA_HEIGHT
        BACKGROUND_COLOR = (84, 84, 150)  # Matched from screenshot
        GRID_LINE_COLOR = (119, 119, 166)  # Matched from screenshot
        WHITE = (255, 255, 255)
        BLOCK_COLORS = [
            (157, 248, 110),
            (74, 222, 227),
            (217, 138, 244),
            (250, 155, 91),
            (249, 231, 137),
            (242, 101, 100)
        ]  # Colors from screenshot

        # Block shapes
        BLOCK_SHAPES = [
            [(0, 0), (1, 0), (2, 0), (0, 1)],  # L-shape
            [(0, 0), (0, 1), (1, 0), (1, 1)],  # Square
            [(0, 0), (1, 0), (2, 0), (3, 0)],  # Line
            [(0, 0), (1, 0), (1, 1), (2, 1)],  # Zig-zag
            [(1, 0), (0, 1), (1, 1), (2, 1)],  # Other Zig-zag
            [(1, 0), (0, 1), (1, 1), (1, 2)],  # T-shape
            [(0, 0), (0, 1), (0, 2), (1, 1)],  # Corner shape
            [(0, 0), (1, 0)],                  # 2x1
            [(0, 0), (0, 1)],                   # 1x2
            # Additional Blocks
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],  # 1x5 block
            [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)],  # 2x3 block
            [(0, 0), (1, 0), (2, 0)],  # a 3 by 1
            [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (2, 0)],  # 2x3 Zig-zag
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)],  # 2x3 Full
        ]

        # Function to rotate a block 90 degrees
        def rotate_block(block):
            rotated_block = []
            for row, col in block:
                rotated_block.append((-col, row))
            
            # Normalize the rotated block to the top-left corner (0,0)
            min_row = min(coord[0] for coord in rotated_block)
            min_col = min(coord[1] for coord in rotated_block)
            normalized_block = [(coord[0] - min_row, coord[1] - min_col) for coord in rotated_block]
            return normalized_block

        # Generate rotated versions of the blocks and add them to the list
        rotated_blocks = []
        for block in BLOCK_SHAPES.copy():
            rotated_1 = rotate_block(block)
            rotated_2 = rotate_block(rotated_1)
            rotated_3 = rotate_block(rotated_2)
            rotated_blocks.append(rotated_1)
            rotated_blocks.append(rotated_2)
            rotated_blocks.append(rotated_3)
        
        BLOCK_SHAPES.extend(rotated_blocks)

        class BlockBlastGameImplementation:
            def __init__(self):
                self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                pygame.display.set_caption("Block Blast!")
                self.clock = pygame.time.Clock()
                self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
                self.current_blocks = self._generate_blocks()
                self.score = 0
                self.game_over = False
                self.font = pygame.font.Font(None, 48)  # Font for score
                self.combo_score_text = []  # For floating score text

            def _generate_blocks(self):
                return [random.choice(BLOCK_SHAPES) for _ in range(3)]

            def _is_valid_move(self, block, anchor_row, anchor_col):
                for row_offset, col_offset in block:
                    row = anchor_row + row_offset
                    col = anchor_col + col_offset
                    if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and self.grid[row][col] == 0):
                        return False
                return True

            def _place_block(self, block, anchor_row, anchor_col, color_index):
                for row_offset, col_offset in block:
                    self.grid[anchor_row + row_offset][anchor_col + col_offset] = color_index + 1  # +1 to avoid 0

            def _clear_lines(self):
                rows_to_clear = [r for r in range(GRID_SIZE) if all(self.grid[r])]
                cols_to_clear = [c for c in range(GRID_SIZE) if all(self.grid[r][c] for r in range(GRID_SIZE))]
                lines_cleared = 0
                score_increase = 0

                # Clear rows without collapsing
                for row in rows_to_clear:
                    self.grid[row] = [0] * GRID_SIZE
                    lines_cleared += 1
                    score_increase += 10

                # Clear columns without collapsing
                for col in cols_to_clear:
                    for r in range(GRID_SIZE):
                        self.grid[r][col] = 0
                    lines_cleared += 1
                    score_increase += 10

                if score_increase > 0:
                    self.combo_score_text.append({
                        "score": score_increase,
                        "position": (GRID_WIDTH // 2, GRID_HEIGHT // 2),
                        "timer": 60
                    })
                    self.score += score_increase
                return lines_cleared > 0

            def _check_game_over(self):
                for block in self.current_blocks:
                    for r in range(GRID_SIZE):
                        for c in range(GRID_SIZE):
                            if self._is_valid_move(block, r, c):
                                return False
                self.game_over = True
                return True

            def run(self):
                selected_block_index = None
                block_being_dragged = False
                drag_start_pos = (0, 0)
                block_offset = (0, 0)
                potential_snap_pos = None

                print("Block Blast! Game Started.")
                while self.running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            pygame.quit()
                            print("Block Blast! Game Closed.")
                            return

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_pos = event.pos
                            for i, block in enumerate(self.current_blocks):
                                block_rect = pygame.Rect(
                                    50 + i * 130,
                                    GRID_HEIGHT + 20,
                                    BLOCK_SIZE * 2,
                                    BLOCK_SIZE * 2
                                )
                                if block_rect.collidepoint(mouse_pos):
                                    selected_block_index = i
                                    block_being_dragged = True
                                    drag_start_pos = mouse_pos
                                    block_offset = (block_rect.x - mouse_pos[0],
                                                    block_rect.y - mouse_pos[1])
                                    print(f"Selected block {i} for dragging.")
                                    break

                        elif event.type == pygame.MOUSEBUTTONUP and block_being_dragged:
                            block_being_dragged = False
                            if selected_block_index is not None and potential_snap_pos:
                                grid_row, grid_col = potential_snap_pos
                                placed_block = self.current_blocks[selected_block_index]
                                self._place_block(
                                    placed_block,
                                    grid_row,
                                    grid_col,
                                    selected_block_index
                                )
                                # Score based on block size
                                self.score += len(placed_block)
                                print(f"Placed block {selected_block_index} at ({grid_row}, {grid_col}). Score: {self.score}")
                                self.current_blocks.pop(selected_block_index)
                                if not self.current_blocks:
                                    self.current_blocks = self._generate_blocks()
                                self._clear_lines()
                                if self._check_game_over():
                                    print("Game Over!")
                                    pygame.time.delay(1000)
                                    self.running = False
                                    pygame.quit()
                                    return
                            selected_block_index = None
                            potential_snap_pos = None

                        elif event.type == pygame.MOUSEMOTION and block_being_dragged:
                            potential_snap_pos = None
                            mouse_pos = event.pos
                            if selected_block_index is not None:
                                block = self.current_blocks[selected_block_index]
                                dragged_block_top_left_x = mouse_pos[0] + block_offset[0]
                                dragged_block_top_left_y = mouse_pos[1] + block_offset[1]

                                for row in range(GRID_SIZE):
                                    for col in range(GRID_SIZE):
                                        grid_cell_x = col * BLOCK_SIZE
                                        grid_cell_y = row * BLOCK_SIZE
                                        grid_rect = pygame.Rect(
                                            grid_cell_x,
                                            grid_cell_y,
                                            BLOCK_SIZE,
                                            BLOCK_SIZE
                                        )
                                        if grid_rect.collidepoint(
                                            dragged_block_top_left_x,
                                            dragged_block_top_left_y
                                        ):
                                            if self._is_valid_move(block, row, col):
                                                potential_snap_pos = (row, col)
                                                break
                                    if potential_snap_pos:
                                        break

                    # Update floating text timers
                    for text_data in self.combo_score_text:
                        text_data["timer"] -= 1
                    self.combo_score_text = [
                        t for t in self.combo_score_text if t["timer"] > 0
                    ]

                    # Drawing
                    self.screen.fill(BACKGROUND_COLOR)

                    # Draw grid lines
                    for i in range(GRID_SIZE + 1):
                        pygame.draw.line(
                            self.screen,
                            GRID_LINE_COLOR,
                            (0, i * BLOCK_SIZE),
                            (GRID_WIDTH, i * BLOCK_SIZE)
                        )
                        pygame.draw.line(
                            self.screen,
                            GRID_LINE_COLOR,
                            (i * BLOCK_SIZE, 0),
                            (i * BLOCK_SIZE, GRID_HEIGHT)
                        )

                    # Draw placed blocks
                    for row in range(GRID_SIZE):
                        for col in range(GRID_SIZE):
                            if self.grid[row][col] != 0:
                                block_color = BLOCK_COLORS[self.grid[row][col] - 1]
                                pygame.draw.rect(
                                    self.screen,
                                    block_color,
                                    (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                                )
                                # shading
                                pygame.draw.line(
                                    self.screen,
                                    (0, 0, 0),
                                    (col * BLOCK_SIZE, row * BLOCK_SIZE),
                                    (col * BLOCK_SIZE + BLOCK_SIZE, row * BLOCK_SIZE),
                                    2
                                )
                                pygame.draw.line(
                                    self.screen,
                                    (0, 0, 0),
                                    (col * BLOCK_SIZE, row * BLOCK_SIZE),
                                    (col * BLOCK_SIZE, row * BLOCK_SIZE + BLOCK_SIZE),
                                    2
                                )
                                pygame.draw.line(
                                    self.screen,
                                    WHITE,
                                    (col * BLOCK_SIZE + BLOCK_SIZE - 1, row * BLOCK_SIZE),
                                    (col * BLOCK_SIZE + BLOCK_SIZE - 1, row * BLOCK_SIZE + BLOCK_SIZE),
                                    2
                                )
                                pygame.draw.line(
                                    self.screen,
                                    WHITE,
                                    (col * BLOCK_SIZE, row * BLOCK_SIZE + BLOCK_SIZE - 1),
                                    (col * BLOCK_SIZE + BLOCK_SIZE, row * BLOCK_SIZE + BLOCK_SIZE - 1),
                                    2
                                )

                    # Draw potential snap outline
                    if potential_snap_pos is not None and selected_block_index is not None:
                        block = self.current_blocks[selected_block_index]
                        grid_row, grid_col = potential_snap_pos
                        for row_offset, col_offset in block:
                            pygame.draw.rect(
                                self.screen,
                                WHITE,
                                (
                                    (grid_col + col_offset) * BLOCK_SIZE,
                                    (grid_row + row_offset) * BLOCK_SIZE,
                                    BLOCK_SIZE,
                                    BLOCK_SIZE
                                ),
                                1
                            )

                    # Draw the blocks waiting at the bottom
                    for i, block in enumerate(self.current_blocks):
                        base_x = 50 + i * 130
                        base_y = GRID_HEIGHT + 20
                        block_color = BLOCK_COLORS[i % len(BLOCK_COLORS)]
                        if selected_block_index == i and block_being_dragged:
                            base_x = pygame.mouse.get_pos()[0] + block_offset[0]
                            base_y = pygame.mouse.get_pos()[1] + block_offset[1]
                        for row_offset, col_offset in block:
                            # slightly smaller
                            pygame.draw.rect(
                                self.screen,
                                block_color,
                                (
                                    int(base_x + col_offset * BLOCK_SIZE),
                                    int(base_y + row_offset * BLOCK_SIZE),
                                    int(BLOCK_SIZE * 0.9),
                                    int(BLOCK_SIZE * 0.9)
                                )
                            )

                    # Display score
                    score_text_surface = self.font.render(str(self.score), True, WHITE)
                    score_rect = score_text_surface.get_rect(
                        midleft=(20, GRID_HEIGHT + (SCORE_AREA_HEIGHT // 2))
                    )
                    self.screen.blit(score_text_surface, score_rect)

                    # Draw combo text
                    for text_data in self.combo_score_text:
                        score_surface = self.font.render(f"+{text_data['score']}", True, WHITE)
                        floating_rect = score_surface.get_rect(center=text_data["position"])
                        self.screen.blit(score_surface, floating_rect)
                        # float it up
                        text_data["position"] = (
                            text_data["position"][0],
                            text_data["position"][1] - 2
                        )

                    pygame.display.flip()
                    self.clock.tick(60)

            def stop(self):
                print("Stopping Block Blast! Game...")
                self.running = False

    # --------------------- Reality Distortion Effects ---------------------
import sys
import random
import math
import colorsys
import ctypes
import threading
import pygame
import wave
import struct
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
)
from PyQt5.QtCore import (
    Qt, QTimer, QPoint, QPointF, QRect, QUrl
)
from PyQt5.QtGui import (
    QPainter, QColor, QFont, QPainterPath,
    QLinearGradient, QRadialGradient, QPen, QBrush
)
from PyQt5.QtMultimedia import QSoundEffect

#########################################################
#          Sound Generation for Rain + Lightning
#########################################################

def generate_lightning_sound(filename="lightning.wav"):
    """generates a short lightning-like crackle. lower amplitude so it's not so loud"""
    framerate = 44100
    duration = 0.2
    amplitude = 15000  # reduced amplitude from 32767 -> 15000
    n_samples = int(framerate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, framerate, n_samples, 'NONE', 'not compressed'))
        for i in range(n_samples):
            t = i / framerate
            val = int(amplitude * math.exp(-40 * t)) if i < framerate * duration else 0
            data = struct.pack('<h', val)
            wav_file.writeframesraw(data)

def generate_rain_sound(filename="rain.wav"):
    """generates simpler, quieter white noise for rain."""
    framerate = 44100
    duration = 2.0
    amplitude = 8000  # significantly reduced amplitude
    n_samples = int(framerate * duration)
    with wave.open(filename, 'w') as wav_file:
        wav_file.setparams((1, 2, framerate, n_samples, 'NONE', 'not compressed'))
        for _ in range(n_samples):
            val = random.randint(-amplitude, amplitude)
            data = struct.pack('<h', val)
            wav_file.writeframesraw(data)

if not os.path.exists("lightning.wav"):
    generate_lightning_sound()
if not os.path.exists("rain.wav"):
    generate_rain_sound()

#########################################################
#                Block Blast Game (Thread)
#########################################################

class BlockBlastGame(threading.Thread):
    """Runs the block-blast game in a separate thread."""
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.running = False

    def run(self):
        self.running = True
        pygame.init()

        # simple 800x600 window
        screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Block Blast!")
        clock = pygame.time.Clock()

        font = pygame.font.Font(None,36)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            screen.fill((40,40,40))
            textsurf = font.render("Block Blast! Game Running...", True, (255,255,255))
            screen.blit(textsurf,(50,50))

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    def stop(self):
        self.running = False

#########################################################
#        Reality Distortion Effects
#########################################################

class RealityDistortionEffect(QWidget):
    """Single overlay window that can do any effect: quantum, fractals, etc."""
    def __init__(self):
        super().__init__()

        # window config
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.set_click_through()

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_effect)
        self.timer.start(16)

        # Current effect
        self.current_effect = None

        # load quieted sounds
        self.sounds = {}
        self.sounds['lightning'] = QSoundEffect()
        self.sounds['lightning'].setSource(QUrl.fromLocalFile(os.path.abspath("lightning.wav")))
        self.sounds['lightning'].setVolume(0.3)  # quieter

        self.sounds['rain'] = QSoundEffect()
        self.sounds['rain'].setSource(QUrl.fromLocalFile(os.path.abspath("rain.wav")))
        self.sounds['rain'].setVolume(0.2)  # fairly quiet

        # store effect data
        self.energy_nodes = []
        self.quantum_particles = []
        self.void_portals = []
        self.fractures = []
        self.time_ripples = []
        self.dna_strands = []
        self.tears = []
        self.matrix_chars = []
        self.particles = []
        self.binary_streams = []
        self.lightning_points = []
        self.vortex_particles = []
        self.stars = []
        self.nebulas = []
        self.quantum_fields = []
        self.psychedelic_offset = 0
        self.rain_drops = []

        self.init_all_effect_data()

        self.show()

    def set_click_through(self):
        hwnd = self.winId().__int__()
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x80000
        WS_EX_TRANSPARENT = 0x20
        styles = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        new_styles = styles | WS_EX_LAYERED | WS_EX_TRANSPARENT
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_styles)

    ####################################################
    #  initialize data for each effect (avoid keyError)
    ####################################################

    def init_all_effect_data(self):
        """Initialize enough data to avoid KeyErrors for each effect"""
        # energy
        for _ in range(20):
            node = {
                'pos': QPointF(random.randint(0, self.width()), random.randint(0, self.height())),
                'velocity': QPointF(random.uniform(-2,2), random.uniform(-2,2)),
                'charge': random.choice([-1,1]),
                'energy': random.uniform(0.5,1.0),
            }
            self.energy_nodes.append(node)

        # quantum
        for _ in range(30):
            p = {
                'x': random.randint(0,self.width()),
                'y': random.randint(0,self.height()),
                'wave_phase': random.uniform(0,2*math.pi),
                'frequency': 0.03,
                'amplitude': random.uniform(10,30),
                'uncertainty': random.uniform(5,15),
                'color': QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                'entangled_partner': None
            }
            self.quantum_particles.append(p)
        # pair them
        for i in range(0,len(self.quantum_particles),2):
            if i+1<len(self.quantum_particles):
                self.quantum_particles[i]['entangled_partner'] = self.quantum_particles[i+1]
                self.quantum_particles[i+1]['entangled_partner'] = self.quantum_particles[i]

        # void portals
        for _ in range(2):
            portal = {
                'center': QPointF(random.randint(100,self.width()-100), random.randint(100,self.height()-100)),
                'radius': random.uniform(60,120),
                'rotation': 0,
                'spin_speed': random.uniform(0.01,0.03),
                'particles':[],
                'distortion':1.2
            }
            # add sub particles
            for _ in range(50):
                angle = random.uniform(0,2*math.pi)
                distance = random.uniform(0,portal['radius'])
                portal['particles'].append({
                    'angle': angle,
                    'distance': distance,
                    'speed': random.uniform(0.01,0.03),
                    'size': random.uniform(1,3)
                })
            self.void_portals.append(portal)

        # reality fractures
        for _ in range(3):
            f_points = []
            x = random.randint(0,self.width())
            y = random.randint(0,self.height())
            for _ in range(random.randint(5,8)):
                x+=random.randint(-80,80)
                y+=random.randint(-80,80)
                f_points.append(QPointF(x,y))
            frac = {
                'points': f_points,
                'width': random.uniform(2,4),
                'glow_intensity': random.uniform(0.5,1.0),
                'color': QColor(random.randint(150,255), random.randint(0,100), random.randint(100,255))
            }
            self.fractures.append(frac)

        # time ripples
        # for demo, just an empty list. no random data needed if we never show them
        self.time_ripples = []

        # dna helix
        # store some random strands
        for strand_i in range(2):
            dna_points = []
            for i in range(20):
                dna_points.append({
                    'base_y': i*25,
                    'phase': i*0.3 + strand_i*math.pi,
                    'nucleotide': random.choice(['A','T','G','C']),
                    'color': QColor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
                })
            self.dna_strands.append(dna_points)

        # dimensional tears
        for _ in range(2):
            dt_points = [QPointF(random.randint(0,self.width()), random.randint(0,self.height()))]
            # just some random tears
            dt = {
                'start': dt_points[0],
                'points': dt_points,
                'growth_direction': QPointF(random.uniform(-1,1),random.uniform(-1,1)),
                'width': random.uniform(4,8),
                'color': QColor(random.randint(100,255), random.randint(100,255), random.randint(100,255))
            }
            self.tears.append(dt)

        # matrix
        columns = self.width() // 20
        for x in range(columns):
            self.matrix_chars.append({
                'x': x*20,
                'y': random.randint(-500, 0),
                'speed': random.uniform(3,7),
                'length': random.randint(5,15),
                'chars': [chr(random.randint(0x30A0,0x30FF)) for _ in range(20)]
            })

        # particles
        for _ in range(50):
            self.particles.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(0,self.height()),
                'dx': random.uniform(-1,1),
                'dy': random.uniform(-1,1),
                'size': random.randint(2,6),
                'color': QColor(random.randint(50,255), random.randint(50,255), random.randint(50,255), 150)
            })

        # binary
        columns = self.width() // 15
        for x in range(columns):
            self.binary_streams.append({
                'x': x*15,
                'y': random.randint(-500,0),
                'speed': random.uniform(2,5),
                'length': random.randint(8,15)
            })

        # lightning
        # store some random points
        for _ in range(5):
            self.lightning_points.append((
                random.randint(0,self.width()), 
                random.randint(0,self.height())
            ))

        # vortex
        for _ in range(300):
            angle = random.uniform(0,2*math.pi)
            radius = random.uniform(60, max(self.width(), self.height()))
            self.vortex_particles.append({
                'angle': angle,
                'radius': radius,
                'speed': random.uniform(0.01,0.03),
                'size': random.uniform(1,3),
                'color': QColor(random.randint(50,255), random.randint(50,255), random.randint(50,255))
            })

        # cosmic
        for _ in range(100):
            self.stars.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(0,self.height()),
                'size': random.uniform(0.5,3),
                'twinkle_speed': random.uniform(0.02,0.1)
            })
        for _ in range(3):
            self.nebulas.append({
                'x': random.randint(100,self.width()-100),
                'y': random.randint(100,self.height()-100),
                'size': random.randint(150,300),
                'color': QColor(random.randint(20,200), random.randint(20,200), random.randint(20,200), 80),
                'alpha': random.uniform(0.1,0.3)
            })

        # quantum fields
        for _ in range(2):
            self.quantum_fields.append({
                'offset': random.uniform(0, 2*math.pi),
                'speed': random.uniform(0.01,0.03),
                'wavelength': random.uniform(80,200)
            })

        # psychedelic offset
        self.psychedelic_offset = 0

        # rain is empty initially
        self.rain_drops = []

    #########################################################
    #  set_effect / clear_effect
    #########################################################

    def set_effect(self, effect_name):
        self.current_effect = effect_name
        print(f"Effect '{effect_name}' activated.")
        if effect_name == "rain":
            # init some rain
            self.init_rain()
            self.sounds['rain'].setLoopCount(QSoundEffect.Infinite)
            self.sounds['rain'].play()
        elif effect_name == "lightning":
            self.sounds['lightning'].play()

    def clear_effect(self):
        print("All effects cleared.")
        self.current_effect = None
        # stop any sounds
        for s in self.sounds.values():
            s.stop()

    #########################################################
    #  optional init for rain
    #########################################################

    def init_rain(self):
        self.rain_drops = []
        # continuously spawn new drops 
        # but let's also spawn a bunch at once
        for _ in range(100):
            self.rain_drops.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(-self.height(),0)
            })

    #########################################################
    #  update_effect calls
    #########################################################

    def update_effect(self):
        # call the update method for whichever effect is active
        if self.current_effect == "rain":
            self.update_rain()
        # if we have more updates for other effects
        elif self.current_effect == "quantum_particles":
            self.update_quantum_particles()
        elif self.current_effect == "void_portals":
            self.update_void_portals()
        elif self.current_effect == "reality_fractures":
            pass  # or define update if needed
        elif self.current_effect == "time_ripples":
            pass
        elif self.current_effect == "dna_helix":
            pass
        elif self.current_effect == "dimensional_tears":
            pass
        elif self.current_effect == "matrix":
            self.update_matrix()
        elif self.current_effect == "particles":
            self.update_particles()
        elif self.current_effect == "binary":
            self.update_binary()
        elif self.current_effect == "lightning":
            # or define logic
            pass
        elif self.current_effect == "vortex":
            self.update_vortex()
        elif self.current_effect == "cosmic":
            pass
        elif self.current_effect == "quantum":
            pass
        elif self.current_effect == "psychedelic":
            self.update_psychedelic()

        self.update()

    def update_rain(self):
        # move drops
        # also spawn new drops 
        if random.random()<0.2:
            # spawn new random drop near top
            self.rain_drops.append({
                'x': random.randint(0,self.width()),
                'y': random.randint(-50,0)
            })
        for drop in self.rain_drops:
            drop['y'] += 6
        # purge drops that fall out
        self.rain_drops = [d for d in self.rain_drops if d['y']<self.height()+20]

    def update_quantum_particles(self):
        # apply wave phase
        for p in self.quantum_particles:
            p['wave_phase'] += p['frequency']
            dx = random.gauss(0, p['uncertainty'])
            dy = random.gauss(0, p['uncertainty'])
            p['x'] += dx
            p['y'] += dy
            # clamp
            p['x'] = max(0, min(self.width(), p['x']))
            p['y'] = max(0, min(self.height(), p['y']))

    def update_void_portals(self):
        for portal in self.void_portals:
            portal['rotation'] += portal['spin_speed']
            for particle in portal['particles']:
                particle['angle'] += particle['speed']
                # spiral in
                if particle['distance']>2:
                    particle['distance'] *= 0.99

    def update_matrix(self):
        for stream in self.matrix_chars:
            stream['y'] += stream['speed']
            if stream['y'] > self.height()+500:
                stream['y'] = random.randint(-500,0)

    def update_particles(self):
        for part in self.particles:
            part['x'] += part['dx']
            part['y'] += part['dy']
            # bounce
            if part['x']<0 or part['x']>self.width():
                part['dx']*=-1
            if part['y']<0 or part['y']>self.height():
                part['dy']*=-1

    def update_binary(self):
        for s in self.binary_streams:
            s['y']+= s['speed']
            if s['y']>self.height()+200:
                s['y'] = random.randint(-500,0)

    def update_vortex(self):
        for v in self.vortex_particles:
            v['angle']+=v['speed']
            v['radius']-=0.2
            if v['radius']<20:
                v['radius'] = max(self.width(), self.height())

    def update_psychedelic(self):
        self.psychedelic_offset+=0.1

    #########################################################
    # paintEvent
    #########################################################

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.current_effect == "rain":
            self.draw_rain(painter)
        elif self.current_effect == "quantum_particles":
            self.draw_quantum_particles(painter)
        elif self.current_effect == "void_portals":
            self.draw_void_portals(painter)
        elif self.current_effect == "reality_fractures":
            self.draw_reality_fractures(painter)
        elif self.current_effect == "time_ripples":
            # no draw_time_ripples defined => do nothing or define
            pass
        elif self.current_effect == "dna_helix":
            # no draw_dna_helix => we can define
            pass
        elif self.current_effect == "dimensional_tears":
            # no draw_dimensional_tears => define or skip
            pass
        elif self.current_effect == "matrix":
            self.draw_matrix(painter)
        elif self.current_effect == "particles":
            self.draw_particles(painter)
        elif self.current_effect == "binary":
            self.draw_binary(painter)
        elif self.current_effect == "lightning":
            # no actual lightning draw for now
            pass
        elif self.current_effect == "vortex":
            self.draw_vortex(painter)
        elif self.current_effect == "cosmic":
            self.draw_cosmic(painter)
        elif self.current_effect == "quantum":
            # we can define a separate quantum effect if needed
            pass
        elif self.current_effect == "psychedelic":
            self.draw_psychedelic(painter)

    #######################################################
    #  drawing stubs for each effect that can be called
    #######################################################

    def draw_rain(self, painter):
        painter.setPen(QPen(QColor(100,100,255,150),2))  # gentle watery color
        for drop in self.rain_drops:
            painter.drawLine(drop['x'], drop['y'], drop['x'], drop['y']+10)

    def draw_quantum_particles(self, painter):
        for p in self.quantum_particles:
            # radius
            r = 10 + math.sin(p['wave_phase'])*p['amplitude']
            # probability cloud
            painter.setPen(Qt.NoPen)
            c = QColor(p['color'])
            c.setAlpha(80)
            painter.setBrush(c)
            painter.drawEllipse(QPointF(p['x'], p['y']), r, r)

            # entanglement line
            if p['entangled_partner']:
                e = p['entangled_partner']
                grad = QLinearGradient(QPointF(p['x'],p['y']), QPointF(e['x'], e['y']))
                grad.setColorAt(0, p['color'])
                grad.setColorAt(1, e['color'])
                pen = QPen(QBrush(grad),1,Qt.DashLine)
                painter.setPen(pen)
                painter.drawLine(QPointF(p['x'],p['y']), QPointF(e['x'], e['y']))

    def draw_void_portals(self, painter):
        painter.setPen(Qt.NoPen)
        for portal in self.void_portals:
            # radial gradient
            rad = QRadialGradient(portal['center'], portal['radius'])
            rad.setColorAt(0, QColor(0,0,0,200))
            rad.setColorAt(1, QColor(0,0,0,0))
            painter.setBrush(rad)
            painter.drawEllipse(portal['center'], portal['radius'], portal['radius'])

            # portal swirl particles
            for pt in portal['particles']:
                angle = pt['angle']+ portal['rotation']
                dist = pt['distance']
                x = portal['center'].x() + math.cos(angle)*dist
                y = portal['center'].y() + math.sin(angle)*dist
                c = QColor(150,0,255,100)
                painter.setBrush(c)
                painter.drawEllipse(QPointF(x,y), pt['size'], pt['size'])

    def draw_reality_fractures(self, painter):
        for frac in self.fractures:
            path = QPainterPath()
            path.moveTo(frac['points'][0])
            for fpt in frac['points'][1:]:
                path.lineTo(fpt)
            # glow
            for i in range(3):
                c = QColor(frac['color'])
                alpha_ = int(100*frac['glow_intensity']/(i+1))
                c.setAlpha(alpha_)
                pen = QPen(c, frac['width']+i*2)
                painter.setPen(pen)
                painter.drawPath(path)

    def draw_matrix(self, painter):
        painter.setFont(QFont('Courier New', 14))
        for stream in self.matrix_chars:
            for i in range(stream['length']):
                ch_y = int(stream['y']) - i*20
                if 0<=ch_y<=self.height():
                    if i==0:
                        painter.setPen(QColor(255,255,255,200))
                    else:
                        alpha = 200-i*15
                        painter.setPen(QColor(0,255,0,max(0,alpha)))
                    # random change
                    if random.random()<0.04:
                        stream['chars'][i] = chr(random.randint(0x30A0,0x30FF))
                    painter.drawText(stream['x'], ch_y, stream['chars'][i])

    def draw_particles(self, painter):
        painter.setPen(Qt.NoPen)
        for part in self.particles:
            painter.setBrush(part['color'])
            painter.drawEllipse(QPointF(part['x'],part['y']), part['size'], part['size'])

    def draw_binary(self, painter):
        painter.setFont(QFont('Courier New',12))
        painter.setPen(QColor(0,255,0,180))
        for s in self.binary_streams:
            for i in range(s['length']):
                ch_y = s['y'] - i*15
                if 0<= ch_y <= self.height():
                    # random 0/1
                    painter.drawText(s['x'], ch_y, str(random.randint(0,1)))

    def draw_vortex(self, painter):
        painter.setPen(Qt.NoPen)
        center_x = self.width()/2
        center_y = self.height()/2
        for v in self.vortex_particles:
            angle = v['angle']
            r = v['radius']
            x = center_x + math.cos(angle)*r
            y = center_y + math.sin(angle)*r
            c = QColor(v['color'])
            c.setAlpha(150)
            painter.setBrush(c)
            painter.drawEllipse(QPointF(x,y),v['size'],v['size'])

    def draw_cosmic(self, painter):
        # stars
        for s in self.stars:
            twinkle = 0.5+0.5*math.sin(self.timer.interval()* s['twinkle_speed'])
            c = QColor(255,255,255,int(twinkle*255))
            painter.setPen(Qt.NoPen)
            painter.setBrush(c)
            painter.drawEllipse(QPoint(s['x'], s['y']), int(s['size']), int(s['size']))
        # nebulas
        for nb in self.nebulas:
            rg = QRadialGradient(QPointF(nb['x'],nb['y']), nb['size'])
            co = nb['color']
            alpha_ = int(255*(nb['alpha']))
            co.setAlpha(alpha_)
            rg.setColorAt(0, co)
            co2 = QColor(co)
            co2.setAlpha(0)
            rg.setColorAt(1, co2)
            painter.setBrush(rg)
            painter.drawEllipse(QPoint(nb['x'],nb['y']), nb['size'], nb['size'])

    def draw_psychedelic(self, painter):
        block = 20
        for xx in range(0, self.width(), block):
            for yy in range(0, self.height(), block):
                val = math.sin(xx*0.02+self.psychedelic_offset)+math.cos(yy*0.02+self.psychedelic_offset)
                col = self.get_rainbow_color((val+2)/4)
                col.setAlpha(100)
                painter.setPen(Qt.NoPen)
                painter.setBrush(col)
                painter.drawRect(xx,yy,block,block)

    #########################################################
    #  helper
    #########################################################

    def get_rainbow_color(self, pos):
        hue = pos%1.0
        r,g,b = colorsys.hsv_to_rgb(hue,1,1)
        return QColor(int(r*255), int(g*255), int(b*255))

#########################################################
#           effect controller main window
#########################################################

class EffectController(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.game_thread = None

    def initUI(self):
        layout = QVBoxLayout()

        self.overlay = RealityDistortionEffect()

        # possible effects
        # note that only "rain", "quantum_particles", etc. have real logic
        effects = [
            "energy", "quantum_particles", "void_portals","reality_fractures",
            "time_ripples","dna_helix","dimensional_tears","matrix",
            "particles","lightning","binary","vortex","cosmic",
            "quantum","psychedelic","rain","block_blaster"
        ]

        btn_layout = QHBoxLayout()
        for eff in effects:
            b = QPushButton(eff.title())
            b.clicked.connect(lambda _, e=eff: self.handle_effect(e))
            btn_layout.addWidget(b)

        layout.addLayout(btn_layout)

        # clear
        clr = QPushButton("Clear Effect")
        clr.clicked.connect(self.clear_effect)
        layout.addWidget(clr)

        self.setLayout(layout)
        self.setWindowTitle("Screen Effects Controller")
        self.resize(800,200)
        self.show()

    def handle_effect(self, effect_name):
        if effect_name=="block_blaster":
            self.launch_game()
        else:
            self.overlay.set_effect(effect_name)

    def clear_effect(self):
        self.overlay.clear_effect()
        # stop game
        if self.game_thread and self.game_thread.running:
            self.game_thread.stop()
            self.game_thread = None

    def launch_game(self):
        if not self.game_thread or not self.game_thread.running:
            self.game_thread = BlockBlastGame()
            self.game_thread.start()
        else:
            print("Game is already running.")

#########################################################
#                      main
#########################################################

def main():
    app = QApplication(sys.argv)
    ctrl = EffectController()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()






# #Isle
# exit()
# # import socket
# # import time

# # # -- START BROADCAST CONFIG --
# # BROADCAST_PORT = 45102  # The port that we are going to broadcast to
# # BROADCAST_MESSAGE = b"DISCOVERY"  # Message we will broadcast
# # RESPONSE_MESSAGE = b"ACK" # Response from devices that have the port open
# # RESPONSE_TIMEOUT = 5 # Time to listen before stopping broadcast and start server
# # # -- END BROADCAST CONFIG --

# # # -- START GLOBALS --
# # found_servers = []
# # # -- END GLOBALS --

# # def broadcast_sender():
# #     """Sends a broadcast message on the network."""
# #     # Create a UDP socket
# #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #     # Enable broadcasting mode
# #     sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# #     try:
# #         # Send the broadcast message to all devices
# #         sock.sendto(BROADCAST_MESSAGE, ('<broadcast>', BROADCAST_PORT))
# #         print(f"Broadcast message sent to port {BROADCAST_PORT}.")
# #     except OSError as e:
# #          print(f"Error sending broadcast: {e}")

# #     finally:
# #         sock.close() # Close the socket after sending

# # def broadcast_receiver():
# #     """Listens for responses to the broadcast message and updates `found_servers`"""
# #     global found_servers
# #     # Create a UDP socket
# #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #     # Bind the socket to the port
# #     sock.bind(('', BROADCAST_PORT))
# #     sock.settimeout(RESPONSE_TIMEOUT)  # Set a timeout for listening

# #     print(f"Listening for responses on port {BROADCAST_PORT}...")

# #     start_time = time.time()
# #     while (time.time() - start_time) < RESPONSE_TIMEOUT:
# #         try:
# #             # Receive data and sender's address
# #             data, addr = sock.recvfrom(1024)
# #             if data == RESPONSE_MESSAGE:
# #                 if addr[0] not in found_servers:
# #                    found_servers.append(addr[0])
# #                    print(f"Received ACK from {addr[0]}")
# #         except socket.timeout:
# #             print(f"No more responses after {RESPONSE_TIMEOUT} seconds.")
# #             break
# #         except Exception as e:
# #              print(f"An error occurred while receiving: {e}")
# #              break
# #     sock.close()

# # def server_responder():
# #     """Opens the port and listens for incoming connections. Responds to the discovery request"""
# #     # Create a UDP socket
# #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #     # Bind to the port, allowing all interfaces to listen
# #     sock.bind(('', BROADCAST_PORT))

# #     while True:
# #         try:
# #             # Receive data from any incoming request
# #             data, addr = sock.recvfrom(1024)
# #             if data == BROADCAST_MESSAGE:
# #                 # Send an ACK back
# #                 sock.sendto(RESPONSE_MESSAGE, addr)
# #                 print(f"Received discovery message from {addr[0]}. Sending ACK.")
# #         except Exception as e:
# #              print(f"An error occurred while responding: {e}")
# #              break
# #     sock.close()

# # def run_broadcast_discovery():
# #     broadcast_sender()
# #     broadcast_receiver()
# #     print(f"Found servers: {found_servers}")

# # def run_server_listener():
# #     server_responder()

# # # Example usage
# # if __name__ == "__main__":
# #     print("Starting broadcast discovery...")
# #     run_broadcast_discovery()
# #     print("Starting server listener...")
# #     run_server_listener()
# # exit()
# # import sys
# # import os
# # import numpy as np
# # import random

# # from PyQt5.QtCore import (
# #     Qt, QUrl, QTimer
# # )
# # from PyQt5.QtWidgets import (
# #     QApplication, QWidget, QOpenGLWidget
# # )
# # from PyQt5.QtMultimedia import (
# #     QMediaPlayer, QMediaContent, QAudioProbe, QAudioBuffer, QAudioFormat
# # )
# # from OpenGL.GL import *
# # from OpenGL.GLU import *

# # class Particle:
# #     def __init__(self, position, velocity, color, life):
# #         self.position = np.array(position, dtype=np.float32)
# #         self.velocity = np.array(velocity, dtype=np.float32)
# #         self.color = color
# #         self.life = life

# # class GLVisualizer(QOpenGLWidget):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.particles = []
# #         self.max_particles = 500
# #         self.audio_level = 0.0
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.update)
# #         self.timer.start(16)  # ~60 FPS

# #     def initializeGL(self):
# #         glClearColor(0.0, 0.0, 0.0, 0.0)  # Fully transparent black
# #         glEnable(GL_BLEND)
# #         glBlendFunc(GL_SRC_ALPHA, GL_ONE)

# #     def resizeGL(self, w, h):
# #         glViewport(0, 0, w, h)
# #         glMatrixMode(GL_PROJECTION)
# #         glLoadIdentity()
# #         gluOrtho2D(0, w, 0, h)  # Back to 2D projection
# #         glMatrixMode(GL_MODELVIEW)

# #     def paintGL(self):
# #         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# #         glLoadIdentity()

# #         # Emit new particles based on audio level
# #         num_new_particles = int(self.audio_level * 100)
# #         for _ in range(num_new_particles):
# #             position = [self.width() / 2, self.height() / 2]
# #             velocity = [
# #                 random.uniform(-1, 1) * 100,
# #                 random.uniform(-1, 1) * 100
# #             ]
# #             color = [
# #                 random.uniform(0.5, 1.0),
# #                 random.uniform(0.5, 1.0),
# #                 random.uniform(0.5, 1.0),
# #                 1.0
# #             ]
# #             life = random.uniform(1.0, 3.0)
# #             self.particles.append(Particle(position, velocity, color, life))

# #         # Update and render particles
# #         alive_particles = []
# #         dt = 0.016  # Assuming 60 FPS
# #         for p in self.particles:
# #             p.life -= dt
# #             if p.life > 0:
# #                 p.position += p.velocity * dt
# #                 p.color[3] = p.life / 3.0  # Fade out
# #                 alive_particles.append(p)

# #                 glColor4f(*p.color)
# #                 glBegin(GL_QUADS)
# #                 size = 3
# #                 glVertex2f(p.position[0] - size, p.position[1] - size)
# #                 glVertex2f(p.position[0] + size, p.position[1] - size)
# #                 glVertex2f(p.position[0] + size, p.position[1] + size)
# #                 glVertex2f(p.position[0] - size, p.position[1] + size)
# #                 glEnd()

# #         self.particles = alive_particles[-self.max_particles:]

# #     def update_audio_level(self, level):
# #         self.audio_level = level

# # class MusicPlayer(QWidget):
# #     def __init__(self, audio_file):
# #         super().__init__()
# #         self.audio_file = audio_file
# #         self.init_ui()
# #         self.init_player()

# #     def init_ui(self):
# #         self.setWindowFlags(Qt.FramelessWindowHint)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.showFullScreen()

# #         # OpenGL Visualizer
# #         self.visualizer = GLVisualizer(self)
# #         self.visualizer.setGeometry(0, 0, self.width(), self.height())
# #         self.visualizer.show()

# #     def init_player(self):
# #         self.player = QMediaPlayer()
# #         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.audio_file)))
# #         self.player.setVolume(100)
# #         self.player.play()

# #         self.probe = QAudioProbe()
# #         self.probe.setSource(self.player)
# #         self.probe.audioBufferProbed.connect(self.process_buffer)

# #     def process_buffer(self, buffer: QAudioBuffer):
# #         fmt = buffer.format()
# #         channels = fmt.channelCount()
# #         sample_type = fmt.sampleType()
# #         sample_size = fmt.sampleSize()
# #         sample_rate = fmt.sampleRate()

# #         # Determine the data type
# #         if sample_type == QAudioFormat.Float:
# #             dtype = np.float32
# #         elif sample_type == QAudioFormat.SignedInt:
# #             if sample_size == 32:
# #                 dtype = np.int32
# #             elif sample_size == 16:
# #                 dtype = np.int16
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         elif sample_type == QAudioFormat.UnSignedInt:
# #             if sample_size == 32:
# #                 dtype = np.uint32
# #             elif sample_size == 16:
# #                 dtype = np.uint16
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         else:
# #             print("Unsupported sample type:", sample_type)
# #             return

# #         # Get the raw audio data
# #         ptr = buffer.constData()
# #         size = buffer.byteCount()
# #         data = np.frombuffer(ptr.asstring(size), dtype=dtype)

# #         # Handle multi-channel audio
# #         if channels > 1:
# #             data = data.reshape(-1, channels)
# #             data = data.mean(axis=1)
# #         else:
# #             data = data.flatten()

# #         # Normalize the data
# #         if np.issubdtype(dtype, np.integer):
# #             max_value = np.iinfo(dtype).max
# #             data = data.astype(np.float32) / max_value

# #         level = np.abs(data).mean()

# #         # Update the visualizer
# #         self.visualizer.update_audio_level(level)



# #     def keyPressEvent(self, event):
# #         if event.key() == Qt.Key_Escape:
# #             self.close()

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     audio_file = r"C:\Users\thesh\Downloads\High Grade.mp3"  # Replace with your audio file

# #     if not os.path.exists(audio_file):
# #         print(f"Audio file not found: {audio_file}")
# #         sys.exit(1)

# #     player = MusicPlayer(audio_file)
# #     sys.exit(app.exec_())

# # exit() 
# # import sys

# # import os
# # import numpy as np
# # import random
# # import math
# # import colorsys

# # from PyQt5.QtCore import (
# #     Qt, QUrl, QTimer, QPointF
# # )
# # from PyQt5.QtWidgets import (
# #     QApplication, QWidget, QOpenGLWidget
# # )
# # from PyQt5.QtMultimedia import (
# #     QMediaPlayer, QMediaContent, QAudioProbe, QAudioBuffer, QAudioFormat
# # )
# # from PyQt5.QtGui import (
# #     QPainter, QPixmap, QColor, QBrush, QPalette
# # )
# # from OpenGL.GL import *
# # from OpenGL.GLU import *
# # from PyQt5.QtOpenGL import QGLFormat

# # class Particle:
# #     def __init__(self, position, velocity, color, life):
# #         self.position = np.array(position, dtype=np.float32)
# #         self.velocity = np.array(velocity, dtype=np.float32)
# #         self.color = color
# #         self.life = life

# # class GLVisualizer(QOpenGLWidget):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.particles = []
# #         self.max_particles = 500
# #         self.audio_level = 0.0
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.update)
# #         self.timer.start(16)  # ~60 FPS

# #     def initializeGL(self):
# #         fmt = QGLFormat()
# #         fmt.setAlpha(True)  # Explicitly request an alpha channel
# #         self.setFormat(fmt)

# #         glClearColor(0.0, 0.0, 0.0, 0.0)

# #     def resizeGL(self, w, h):
# #         glViewport(0, 0, w, h)
# #         glMatrixMode(GL_PROJECTION)
# #         glLoadIdentity()
# #         gluOrtho2D(0, w, 0, h)
# #         glMatrixMode(GL_MODELVIEW)

# #     def paintGL(self):
# #         glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
# #         glLoadIdentity()

# #         # Emit new particles based on audio level
# #         num_new_particles = int(self.audio_level * 100)
# #         for _ in range(num_new_particles):
# #             position = [self.width() / 2, self.height() / 2]
# #             velocity = [
# #                 random.uniform(-1, 1) * 100,
# #                 random.uniform(-1, 1) * 100
# #             ]
# #             color = [
# #                 random.uniform(0.5, 1.0),
# #                 random.uniform(0.5, 1.0),
# #                 random.uniform(0.5, 1.0),
# #                 1.0
# #             ]
# #             life = random.uniform(1.0, 3.0)
# #             self.particles.append(Particle(position, velocity, color, life))

# #         # Update and render particles
# #         alive_particles = []
# #         dt = 0.016  # Assuming 60 FPS
# #         for p in self.particles:
# #             p.life -= dt
# #             if p.life > 0:
# #                 p.position += p.velocity * dt
# #                 p.color[3] = p.life / 3.0  # Fade out
# #                 alive_particles.append(p)

# #                 glColor4f(*p.color)
# #                 glBegin(GL_QUADS)
# #                 size = 3
# #                 glVertex2f(p.position[0] - size, p.position[1] - size)
# #                 glVertex2f(p.position[0] + size, p.position[1] - size)
# #                 glVertex2f(p.position[0] + size, p.position[1] + size)
# #                 glVertex2f(p.position[0] - size, p.position[1] + size)
# #                 glEnd()

# #         self.particles = alive_particles[-self.max_particles:]

# #     def update_audio_level(self, level):
# #         self.audio_level = level

# # class MusicPlayer(QWidget):
# #     def __init__(self, audio_file, album_art_file):
# #         super().__init__()
# #         self.audio_file = audio_file
# #         self.album_art_file = album_art_file
# #         self.init_ui()
# #         self.init_player()

# #     def init_ui(self):
# #         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.showFullScreen() 


# #         # OpenGL Visualizer
# #         self.visualizer = GLVisualizer(self)
# #         self.visualizer.setGeometry(0, 0, self.width(), self.height())
# #         self.visualizer.show()

# #     def init_player(self):
# #         self.player = QMediaPlayer()
# #         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.audio_file)))
# #         self.player.setVolume(100)
# #         self.player.play()

# #         self.probe = QAudioProbe()
# #         self.probe.setSource(self.player)
# #         self.probe.audioBufferProbed.connect(self.process_buffer)

# #     def process_buffer(self, buffer: QAudioBuffer):
# #         fmt = buffer.format()
# #         channels = fmt.channelCount()
# #         sample_type = fmt.sampleType()
# #         sample_size = fmt.sampleSize()
# #         sample_rate = fmt.sampleRate()

# #         # Determine the data type
# #         if sample_type == QAudioFormat.Float:
# #             dtype = np.float32
# #         elif sample_type == QAudioFormat.SignedInt:
# #             if sample_size == 32:
# #                 dtype = np.int32
# #             elif sample_size == 16:
# #                 dtype = np.int16
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         elif sample_type == QAudioFormat.UnSignedInt:
# #             if sample_size == 32:
# #                 dtype = np.uint32
# #             elif sample_size == 16:
# #                 dtype = np.uint16
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         else:
# #             print("Unsupported sample type:", sample_type)
# #             return

# #         # Get the raw audio data
# #         ptr = buffer.constData()
# #         size = buffer.byteCount()
# #         data = np.frombuffer(ptr.asstring(size), dtype=dtype)

# #         # Handle multi-channel audio
# #         if channels > 1:
# #             data = data.reshape(-1, channels)
# #             data = data.mean(axis=1)
# #         else:
# #             data = data.flatten()

# #         # Normalize the data
# #         if np.issubdtype(dtype, np.integer):
# #             max_value = np.iinfo(dtype).max
# #             data = data.astype(np.float32) / max_value

# #         level = np.abs(data).mean()

# #         # Update the visualizer
# #         self.visualizer.update_audio_level(level)


# #     def keyPressEvent(self, event):
# #         if event.key() == Qt.Key_Escape:
# #             self.close()

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     album_art_file = r"C:\Users\thesh\Downloads\High Grade.png"
# #     audio_file = r"C:\Users\thesh\Downloads\High Grade.mp3"

# #     if not os.path.exists(audio_file):
# #         print(f"Audio file not found: {audio_file}")
# #         sys.exit(1)

# #     if not os.path.exists(album_art_file):
# #         print(f"Album art file not found: {album_art_file}")
# #         sys.exit(1)

# #     player = MusicPlayer(audio_file, album_art_file)
# #     sys.exit(app.exec_())




# # exit()
# # import sys
# # import os
# # import numpy as np
# # from PyQt5.QtCore import Qt, QUrl, QTimer, QRectF, QSize
# # from PyQt5.QtWidgets import (
# #     QApplication, QWidget, QLabel, QSlider, QHBoxLayout, 
# #     QVBoxLayout, QGraphicsBlurEffect, QGraphicsDropShadowEffect
# # )
# # from PyQt5.QtMultimedia import (
# #     QMediaPlayer, QAudioProbe, QAudioBuffer, QMediaContent,
# #     QAudioFormat
# # )
# # from PyQt5.QtGui import (
# #     QPainter, QColor, QBrush, QLinearGradient,
# #     QPixmap, QIcon
# # )
# # from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
# # from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
# # from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QTransform, QRadialGradient
# # import sys
# # import random
# # import sys
# # from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
# #                              QVBoxLayout, QPushButton, QSlider)
# # from PyQt5.QtGui import QPixmap, QPalette, QColor, QBrush
# # from PyQt5.QtCore import Qt, QTimer
# # from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# # from PyQt5.QtCore import QUrl
# # from PIL import Image
# # import librosa
# # import numpy as np
# # from mutagen.mp3 import MP3
# # from mutagen.flac import FLAC
# # from mutagen.oggvorbis import OggVorbis
# # import colorsys
# # import math
# # import math
# # class MusicPlayer(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
# #         self.player = QMediaPlayer()
# #         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(r"C:\Users\thesh\Downloads\High Grade.mp3")))
# #         self.player.play()

# #     def initUI(self):
# #         self.setWindowTitle('Glassy Music Player')
# #         self.showFullScreen()

# #         # Load and set the album art as background
# #         album_art = QImage(r"C:\Users\thesh\Downloads\High Grade.png")
# #         album_art = album_art.scaled(self.size(), Qt.KeepAspectRatioByExpanding)

# #         # Apply blur effect to the album art
# #         blurred_art = album_art.copy()
# #         size = self.size()

# #         for i in range(5):
# #             half_size = QSize(size.width() // 2, size.height() // 2)
# #             blurred_art = blurred_art.scaled(half_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
# #             blurred_art = blurred_art.scaled(size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

# #         palette = QPalette()
# #         palette.setBrush(QPalette.Window, QBrush(blurred_art))
# #         self.setPalette(palette)

# #         # Create a transparent overlay for interactive visuals (placeholder)
# #         self.visuals = QLabel(self)
# #         self.visuals.setGeometry(0, 0, self.width(), self.height())
# #         self.visuals.setStyleSheet("background-color: rgba(0, 0, 0, 0);")

# #         # Set up hidden controls
# #         self.play_button = QPushButton('▶️', self)
# #         self.play_button.setStyleSheet("font-size: 24px; background-color: rgba(255, 255, 255, 0.5);")
# #         self.play_button.clicked.connect(self.toggle_playback)
# #         self.play_button.hide()

# #         # Position the play button
# #         self.play_button.move(50, self.height() - 100)

# #         # Timer to hide controls
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.hide_controls)
# #         self.timer.start(3000)

# #     def mouseMoveEvent(self, event):
# #         self.play_button.show()
# #         self.timer.start(3000)  # Reset the timer

# #     def hide_controls(self):
# #         self.play_button.hide()

# #     def toggle_playback(self):
# #         if self.player.state() == QMediaPlayer.PlayingState:
# #             self.player.pause()
# #             self.play_button.setText('▶️')
# #         else:
# #             self.player.play()
# #             self.play_button.setText('⏸️')

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     player = MusicPlayer()
# #     sys.exit(app.exec_())


# # exit()
# # # ai studio attempt but it's very dull
# # import sys
# # from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
# #                              QVBoxLayout, QPushButton, QSlider)
# # from PyQt5.QtGui import QPixmap, QPalette, QColor, QBrush
# # from PyQt5.QtCore import Qt, QTimer
# # from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# # from PyQt5.QtCore import QUrl
# # from PIL import Image
# # import librosa
# # import numpy as np
# # from mutagen.mp3 import MP3
# # from mutagen.flac import FLAC
# # from mutagen.oggvorbis import OggVorbis
# # import colorsys
# # import math

# # class MusicPlayer(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()

# #     def initUI(self):
# #         # set window flags
# #         self.setWindowFlags(Qt.FramelessWindowHint)
# #         self.setAttribute(Qt.WA_TranslucentBackground)

# #         # Main layout
# #         self.main_layout = QVBoxLayout()

# #         # Album art
# #         self.album_art_label = QLabel(self)
# #         self.album_art_label.setPixmap(QPixmap("placeholder_album_art.png").scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
# #         self.main_layout.addWidget(self.album_art_label, alignment=Qt.AlignCenter)

# #         # Controls layout
# #         self.controls_layout = QHBoxLayout()
# #         self.play_button = QPushButton("Play")
# #         self.prev_button = QPushButton("Prev")
# #         self.next_button = QPushButton("Next")

# #         self.controls_layout.addWidget(self.prev_button)
# #         self.controls_layout.addWidget(self.play_button)
# #         self.controls_layout.addWidget(self.next_button)
# #         self.main_layout.addLayout(self.controls_layout)

# #         # Volume
# #         self.volume_slider = QSlider(Qt.Horizontal)
# #         self.volume_slider.setMinimum(0)
# #         self.volume_slider.setMaximum(100)
# #         self.volume_slider.setValue(70)  # Default volume
# #         self.main_layout.addWidget(self.volume_slider)

# #         self.setLayout(self.main_layout)
# #         self.setWindowTitle('Sonder Music Player')

# #         # set window background color
# #         palette = self.palette()
# #         palette.setColor(QPalette.Window, QColor(0, 0, 0, 100))
# #         self.setPalette(palette)
# #         self.setAutoFillBackground(True)

# #         # Media player
# #         self.player = QMediaPlayer()

# #         # Connect buttons
# #         self.play_button.clicked.connect(self.play_pause)
# #         self.prev_button.clicked.connect(self.previous_track)
# #         self.next_button.clicked.connect(self.next_track)
# #         self.volume_slider.valueChanged.connect(self.set_volume)

# #         self.current_playlist = []  # List to hold file paths
# #         self.current_track_index = 0 # track index

# #         self.setGeometry(300, 300, 400, 400)

# #         self.visualizer_timer = QTimer(self)
# #         self.visualizer_timer.timeout.connect(self.update_visualizer)

# #         # Placeholder for visualizer elements
# #         self.visualizer_bars = []
# #         self.create_visualizer(10)
# #         self.visualizer_data = np.zeros(10)

# #         self.show()
# #     def create_visualizer(self, num_bars):
# #         self.visualizer_layout = QHBoxLayout()
# #         for _ in range(num_bars):
# #             bar = QLabel(self)
# #             bar.setStyleSheet("background-color: rgba(255, 255, 255, 100); border-radius: 2px;")
# #             bar.setMinimumSize(5, 10)
# #             self.visualizer_layout.addWidget(bar)
# #             self.visualizer_bars.append(bar)
# #         self.main_layout.addLayout(self.visualizer_layout)

# #     def update_visualizer(self):
# #         if self.player.state() == QMediaPlayer.PlayingState:
# #             try:
# #                 y, sr = librosa.load(self.current_playlist[self.current_track_index], sr=None, mono=True, duration=0.1)
# #                 stft = np.abs(librosa.stft(y))
# #                 self.visualizer_data = librosa.amplitude_to_db(stft, ref=np.max)
# #                 self.visualizer_data = np.mean(self.visualizer_data, axis=1)

# #                 if len(self.visualizer_data) < len(self.visualizer_bars):
# #                     self.visualizer_data = np.pad(self.visualizer_data, (0, len(self.visualizer_bars) - len(self.visualizer_data)), 'constant')
# #                 elif len(self.visualizer_data) > len(self.visualizer_bars):
# #                     self.visualizer_data = self.visualizer_data[:len(self.visualizer_bars)]
# #                 for i, bar in enumerate(self.visualizer_bars):
# #                      height = max(5, int((self.visualizer_data[i] + 60) * 0.8))
# #                      bar.setFixedHeight(height)
# #             except Exception as e:
# #                print(f"Error in update_visualizer: {e}")

# #     def load_audio(self, audio_path):
# #         if audio_path:
# #             self.current_playlist = [audio_path] if isinstance(audio_path, str) else list(audio_path)
# #             self.current_track_index = 0
# #             self.play_track()

# #     def play_track(self):
# #         if self.current_playlist and 0 <= self.current_track_index < len(self.current_playlist):
# #             track_path = self.current_playlist[self.current_track_index]
# #             self.player.setMedia(QMediaContent(QUrl.fromLocalFile(track_path)))
# #             self.set_volume(self.volume_slider.value())
# #             self.player.play()
# #             self.play_button.setText("Pause")
# #             self.update_album_art_and_theme()
# #             self.visualizer_timer.start(50)
# #         else:
# #             print("Playlist is empty or invalid track index.")

# #     def play_pause(self):
# #         if self.player.state() == QMediaPlayer.PlayingState:
# #             self.player.pause()
# #             self.play_button.setText("Play")
# #             self.visualizer_timer.stop()
# #         else:
# #             self.player.play()
# #             self.play_button.setText("Pause")
# #             self.visualizer_timer.start(50)

# #     def previous_track(self):
# #         if self.current_playlist:
# #             self.current_track_index = (self.current_track_index - 1) % len(self.current_playlist)
# #             self.play_track()

# #     def next_track(self):
# #         if self.current_playlist:
# #             self.current_track_index = (self.current_track_index + 1) % len(self.current_playlist)
# #             self.play_track()

# #     def set_volume(self, volume):
# #         self.player.setVolume(volume)

# #     def update_album_art_and_theme(self):
# #         if self.current_playlist:
# #             track_path = self.current_playlist[self.current_track_index]
# #         try:
# #             if track_path.lower().endswith('.mp3'):
# #                 audio = MP3(track_path)
# #             elif track_path.lower().endswith('.flac'):
# #                 audio = FLAC(track_path)
# #             elif track_path.lower().endswith('.ogg'):
# #                 audio = OggVorbis(track_path)
# #             else:
# #                 print("Unsupported audio format")
# #                 return

# #             for key in audio.keys():
# #                 if key.startswith("APIC:") or key == "covr":
# #                    artwork_data = audio.tags[key].data
# #                    image = Image.open(io.BytesIO(artwork_data))

# #                    # Resize for display
# #                    display_image = image.copy()
# #                    display_image.thumbnail((300, 300))
# #                    temp_buffer = io.BytesIO()
# #                    display_image.save(temp_buffer, format=image.format)
# #                    qimage = QImage.fromData(temp_buffer.getvalue())
# #                    pixmap = QPixmap.fromImage(qimage)
# #                    self.album_art_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))

# #                    # Extract dominant color for theme
# #                    colors = image.getcolors(image.size[0] * image.size[1])
# #                    dominant_color_rgb = max(colors, key=lambda item: item[0])[1]
# #                    hsv_color = colorsys.rgb_to_hsv(dominant_color_rgb[0]/255, dominant_color_rgb[1]/255, dominant_color_rgb[2]/255)
# #                    darker_hsv = (hsv_color[0], hsv_color[1], hsv_color[2] * 0.7)
# #                    darker_rgb = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(*darker_hsv))
# #                    q_dominant_color = QColor(*dominant_color_rgb,100)
# #                    q_darker_color = QColor(*darker_rgb,100)
# #                    palette = self.palette()
# #                    palette.setColor(QPalette.Window, q_darker_color)
# #                    self.setPalette(palette)
# #                    self.setAutoFillBackground(True)
# #                    self.setStyleSheet(f"""
# #                        QPushButton {{
# #                            background-color: rgba({dominant_color_rgb[0]}, {dominant_color_rgb[1]}, {dominant_color_rgb[2]}, 180);
# #                            color: white;
# #                            border: none;
# #                            padding: 10px 20px;
# #                            margin: 5px;
# #                        }}
# #                        QPushButton:hover {{
# #                            background-color: rgba({dominant_color_rgb[0]}, {dominant_color_rgb[1]}, {dominant_color_rgb[2]}, 255);
# #                        }}
# #                         QSlider::groove:horizontal {{
# #                             border: 1px solid #999999;
# #                             height: 5px;
# #                             background: rgba({q_darker_color.red()}, {q_darker_color.green()}, {q_darker_color.blue()}, 150);
# #                             margin: 2px 0;
# #                         }}

# #                         QSlider::handle:horizontal {{
# #                             background: rgba({dominant_color_rgb[0]}, {dominant_color_rgb[1]}, {dominant_color_rgb[2]}, 255);
# #                             border: 1px solid #5c5c5c;
# #                             width: 18px;
# #                             margin: -7px 0;
# #                             border-radius: 5px;
# #                         }}
# #                        """)
# #                    return

# #             self.album_art_label.setPixmap(QPixmap("placeholder_album_art.png").scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
# #             palette = self.palette()
# #             palette.setColor(QPalette.Window, QColor(0,0,0,100))
# #             self.setPalette(palette)
# #             self.setAutoFillBackground(True)
# #         except Exception as e:
# #             print(f"Error updating album art and theme: {e}")
# #             self.album_art_label.setPixmap(QPixmap("placeholder_album_art.png").scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = MusicPlayer()
# #     if len(sys.argv) > 1:
# #         ex.load_audio(sys.argv[1:])
# #     sys.exit(app.exec_())

# # exit()







# """





# Working iteration is below for the music player of high grade


# """






# # import sys
# # import os
# # import numpy as np
# # from PyQt5.QtCore import Qt, QUrl, QTimer, QRectF, QSize
# # from PyQt5.QtWidgets import (
# #     QApplication, QWidget, QLabel, QSlider, QHBoxLayout,
# #     QVBoxLayout, QGraphicsBlurEffect, QGraphicsDropShadowEffect
# # )
# # from PyQt5.QtMultimedia import (
# #     QMediaPlayer, QAudioProbe, QAudioBuffer, QMediaContent,
# #     QAudioFormat
# # )
# # from PyQt5.QtGui import (
# #     QPainter, QColor, QBrush, QLinearGradient,
# #     QPixmap, QIcon
# # )


# # import sys
# # import os
# # import random
# # import math

# # import numpy as np
# # from PyQt5.QtCore import Qt, QUrl, QTimer, QRectF, QSize, QPoint
# # from PyQt5.QtWidgets import (
# #     QApplication, QWidget, QLabel, QSlider, QHBoxLayout,
# #     QVBoxLayout, QGraphicsBlurEffect, QGraphicsDropShadowEffect
# # )
# # from PyQt5.QtMultimedia import (
# #     QMediaPlayer, QAudioProbe, QAudioBuffer, QMediaContent,
# #     QAudioFormat
# # )
# # from PyQt5.QtGui import (
# #     QPainter, QColor, QBrush, QLinearGradient,
# #     QPixmap, QIcon, QRadialGradient
# # )


# # import sys
# # import os
# # import numpy as np
# # import random
# # import math
# # import colorsys
# # import platform

# # from PyQt5.QtCore import (
# #     Qt, QUrl, QTimer, QRectF, QSize, QPointF, QObject, pyqtSignal
# # )
# # from PyQt5.QtWidgets import (
# #     QApplication, QWidget, QLabel, QSlider, QHBoxLayout,
# #     QVBoxLayout, QGraphicsBlurEffect, QGraphicsDropShadowEffect
# # )
# # from PyQt5.QtMultimedia import (
# #     QMediaPlayer, QAudioProbe, QAudioBuffer, QMediaContent,
# #     QAudioFormat
# # )
# # from PyQt5.QtGui import (
# #     QPainter, QColor, QBrush, QPixmap, QIcon, QRadialGradient
# # )

# # # Import pynput for global mouse tracking
# # from pynput import mouse

# # # For making the window click-through on Windows
# # if platform.system() == 'Windows':
# #     import ctypes
# #     from ctypes import wintypes

# # class VisualizerWidget(QWidget):
# #     level_changed = pyqtSignal(float)  # Signal to emit audio level

# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.audio_levels = []
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.update)
# #         self.timer.start(16)  # Refresh at approximately 60 FPS
# #         self.setAttribute(Qt.WA_TransparentForMouseEvents)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.is_paused = False  # Track if the player is paused

# #     def update_levels(self, level):
# #         if not self.is_paused:
# #             # Keep a fixed number of levels for smooth visualization
# #             max_levels = 15  # Reduced to minimize delay
# #             self.audio_levels.append(level)
# #             if len(self.audio_levels) > max_levels:
# #                 self.audio_levels.pop(0)

# #             # Emit the level to be used by the cosmic effect
# #             self.level_changed.emit(level)

# #     def paintEvent(self, event):
# #         painter = QPainter(self)
# #         # Set background to transparent
# #         painter.setCompositionMode(QPainter.CompositionMode_Source)
# #         painter.fillRect(self.rect(), Qt.transparent)

# #         if self.audio_levels:
# #             bar_count = len(self.audio_levels)
# #             bar_width = self.width() / bar_count
# #             max_height = self.height()

# #             for i, level in enumerate(self.audio_levels):
# #                 # Apply easing for smoother animation
# #                 level = level ** 0.5
# #                 # Scale the level to the height of the widget
# #                 bar_height = level * max_height * 2  # Adjust scaling
# #                 x = i * bar_width
# #                 y = self.height() - bar_height  # Start from bottom

# #                 # Create gradient for the bars
# #                 gradient = QLinearGradient(x, y, x, y + bar_height)
# #                 gradient.setColorAt(0.0, QColor(255, 105, 180, 180))  # Pink (Hot Pink)
# #                 gradient.setColorAt(1.0, QColor(255, 182, 193, 180))  # Light Pink

# #                 painter.setBrush(QBrush(gradient))
# #                 painter.setPen(Qt.NoPen)

# #                 # Draw rounded bars
# #                 rect = QRectF(x, y, bar_width * 0.8, bar_height)
# #                 painter.drawRoundedRect(rect, bar_width * 0.4, bar_width * 0.4)
# #         else:
# #             # Clear the visualizer when paused
# #             painter.fillRect(self.rect(), Qt.transparent)

# # class RealityDistortionEffect(QWidget):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)

# #         # Window setup
# #         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.setFocusPolicy(Qt.NoFocus)  # Do not accept keyboard focus

# #         # Get parent dimensions
# #         if parent:
# #             self.setGeometry(parent.geometry())
# #         else:
# #             screen = QApplication.primaryScreen()
# #             self.setGeometry(screen.geometry())

# #         # Make the window click-through
# #         self.make_window_click_through()

# #         # Initialize effect parameters
# #         self.effect_time = 0

# #         # Initialize cosmic effect components
# #         self.init_cosmic()

# #         # Animation timer
# #         self.timer = QTimer(self)
# #         self.timer.timeout.connect(self.update_effect)
# #         self.timer.start(16)  # ~60 FPS

# #         # Mouse position
# #         self.mouse_pos = QPointF(self.width() / 2, self.height() / 2)

# #         # Start global mouse listener
# #         self.start_mouse_listener()

# #     def make_window_click_through(self):
# #         # Make the window click-through on Windows
# #         if platform.system() == 'Windows':
# #             hwnd = self.winId().__int__()

# #             # Constants
# #             GWL_EXSTYLE = -20
# #             WS_EX_LAYERED = 0x80000
# #             WS_EX_TRANSPARENT = 0x20

# #             # Get the window's current style
# #             styles = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

# #             # Add layered and transparent styles
# #             new_styles = styles | WS_EX_LAYERED | WS_EX_TRANSPARENT

# #             # Apply the new style
# #             ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, new_styles)

# #         elif platform.system() == 'Linux':
# #             # For X11 systems
# #             pass  # Implement as needed
# #         elif platform.system() == 'Darwin':
# #             # For macOS
# #             pass  # Implement as needed

# #     def start_mouse_listener(self):
# #         # Function to start a global mouse listener
# #         def on_move(x, y):
# #             self.mouse_pos = QPointF(x, y)

# #         # Create a listener and start it in a separate thread
# #         self.mouse_listener = mouse.Listener(on_move=on_move)
# #         self.mouse_listener.start()

# #     def closeEvent(self, event):
# #         # Stop the mouse listener when the application closes
# #         if hasattr(self, 'mouse_listener'):
# #             self.mouse_listener.stop()
# #         event.accept()

# #     def init_cosmic(self):
# #         self.stars = []
# #         self.nebulas = []

# #         # Create stars
# #         for _ in range(400):  # Increased number of stars
# #             self.stars.append({
# #                 'x': random.randint(0, self.width()),
# #                 'y': random.randint(0, self.height()),
# #                 'size': random.uniform(0.5, 2),
# #                 'twinkle_speed': random.uniform(0.02, 0.1)
# #             })

# #         # Create more nebulas with reduced size
# #         for _ in range(20):  # Increased number of nebulas
# #             nebula = {
# #                 'base_x': random.randint(0, self.width()),
# #                 'base_y': random.randint(0, self.height()),
# #                 'offset_x': 0,
# #                 'offset_y': 0,
# #                 'base_size': random.randint(80, 150),  # Reduced size
# #                 'size': random.randint(80, 150),
# #                 'color': self.get_subtle_color(),
# #                 'alpha': random.uniform(60, 120)
# #             }
# #             self.nebulas.append(nebula)

# #     def get_subtle_color(self):
# #         # Generate a subtle color for the nebula
# #         hue = random.uniform(0, 1)
# #         saturation = random.uniform(0.2, 0.4)
# #         value = random.uniform(0.5, 0.7)
# #         rgb = colorsys.hsv_to_rgb(hue, saturation, value)
# #         return QColor(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

# #     def update_effect(self):
# #         self.effect_time += 1

# #         # Calculate parallax movement for nebulas
# #         max_displacement = 50  # Maximum displacement from base position

# #         for nebula in self.nebulas:
# #             # Calculate displacement based on mouse position relative to screen center
# #             screen_center = QPointF(self.width() / 2, self.height() / 2)
# #             mouse_delta = self.mouse_pos - screen_center

# #             # Parallax factor (smaller factor for farther objects)
# #             parallax_factor = 0.02  # Adjust this for effect strength

# #             target_offset_x = mouse_delta.x() * parallax_factor
# #             target_offset_y = mouse_delta.y() * parallax_factor

# #             # Limit displacement to max_displacement
# #             target_offset_x = max(-max_displacement, min(max_displacement, target_offset_x))
# #             target_offset_y = max(-max_displacement, min(max_displacement, target_offset_y))

# #             # Smoothly interpolate offset
# #             nebula['offset_x'] += (target_offset_x - nebula['offset_x']) * 0.1
# #             nebula['offset_y'] += (target_offset_y - nebula['offset_y']) * 0.1

# #         self.update()  # Trigger repaint event

# #     def paintEvent(self, event):
# #         painter = QPainter(self)
# #         painter.setRenderHint(QPainter.Antialiasing)
# #         self.draw_cosmic(painter)

# #     def draw_cosmic(self, painter):
# #         # Draw background stars
# #         for star in self.stars:
# #             twinkle = math.sin(self.effect_time * star['twinkle_speed']) * 0.5 + 0.5
# #             color = QColor(255, 255, 255, int(twinkle * 255))
# #             painter.setPen(color)
# #             painter.setBrush(color)
# #             painter.drawEllipse(QPointF(star['x'], star['y']), star['size'], star['size'])

# #         # Draw nebulas
# #         for nebula in self.nebulas:
# #             x = nebula['base_x'] + nebula['offset_x']
# #             y = nebula['base_y'] + nebula['offset_y']

# #             gradient = QRadialGradient(x, y, nebula['size'])
# #             color = QColor(nebula['color'])
# #             color.setAlpha(int(nebula['alpha']))
# #             gradient.setColorAt(0.0, color)
# #             color.setAlpha(0)
# #             gradient.setColorAt(1.0, color)

# #             painter.setPen(Qt.NoPen)
# #             painter.setBrush(gradient)
# #             painter.drawEllipse(QPointF(x, y), nebula['size'], nebula['size'])

# # class AlbumArtWidget(QLabel):
# #     def __init__(self, pixmap, audio_visualizer, parent=None):
# #         super().__init__(parent)
# #         self.audio_visualizer = audio_visualizer
# #         self.setPixmap(pixmap)
# #         self.setScaledContents(True)
# #         self.is_hovered = False
# #         self.play_icon = QIcon(self.style().standardIcon(QApplication.style().SP_MediaPlay))
# #         self.pause_icon = QIcon(self.style().standardIcon(QApplication.style().SP_MediaPause))
# #         self.icon_label = QLabel(self)
# #         self.icon_label.setFixedSize(50, 50)
# #         self.icon_label.setAlignment(Qt.AlignCenter)
# #         self.icon_label.setStyleSheet("background-color: rgba(255, 255, 255, 0.7); border-radius: 25px;")
# #         self.icon_label.move(
# #             (self.width() - self.icon_label.width()) // 2,
# #             (self.height() - self.icon_label.height()) // 2)
# #         self.icon_label.setVisible(False)
# #         self.icon_label.setAttribute(Qt.WA_TransparentForMouseEvents)
# #         self.update_icon(QMediaPlayer.PlayingState)
# #         # Apply drop shadow effect
# #         shadow = QGraphicsDropShadowEffect()
# #         shadow.setBlurRadius(20)
# #         shadow.setColor(QColor(0, 0, 0, 160))
# #         shadow.setOffset(5, 5)
# #         self.setGraphicsEffect(shadow)

# #     def enterEvent(self, event):
# #         self.is_hovered = True
# #         self.icon_label.setVisible(True)
# #         self.setCursor(Qt.PointingHandCursor)

# #     def leaveEvent(self, event):
# #         self.is_hovered = False
# #         self.icon_label.setVisible(False)
# #         self.setCursor(Qt.ArrowCursor)

# #     def mousePressEvent(self, event):
# #         if event.button() == Qt.LeftButton:
# #             self.audio_visualizer.toggle_play()

# #     def update_icon(self, state):
# #         if state == QMediaPlayer.PlayingState:
# #             self.icon_label.setPixmap(self.pause_icon.pixmap(50, 50))
# #         else:
# #             self.icon_label.setPixmap(self.play_icon.pixmap(50, 50))

# #     def resizeEvent(self, event):
# #         self.icon_label.move(
# #             (self.width() - self.icon_label.width()) // 2,
# #             (self.height() - self.icon_label.height()) // 2)
# #         self.icon_label.raise_()  # Ensure icon_label is on top

# # class AudioVisualizer(QWidget):
# #     def __init__(self, audio_file, album_art_file):
# #         super().__init__()
# #         self.audio_file = audio_file
# #         self.album_art_file = album_art_file
# #         self.audio_levels = []
# #         self.init_ui()
# #         self.init_player()

# #     def init_ui(self):
# #         # Make the window frameless, always on top, and transparent
# #         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.showFullScreen()

# #         # Close mechanism: Press 'Esc' to close
# #         self.installEventFilter(self)

# #         # Get screen dimensions
# #         screen = QApplication.primaryScreen()
# #         size = screen.size()
# #         screen_width = size.width()
# #         screen_height = size.height()

# #         # Set album art size relative to screen size
# #         album_art_width = int(screen_width * 0.15)
# #         album_art_height = int(screen_height * 0.15)
# #         album_art_size = QSize(album_art_width, album_art_height)

# #         # Create main layout
# #         self.main_layout = QVBoxLayout(self)
# #         self.main_layout.setContentsMargins(20, screen_height * 25 // 32, 20, 0)   # A bit lower
# #         self.main_layout.setAlignment(Qt.AlignBottom)

# #         # Controls layout (volume slider and album art)
# #         controls_layout = QHBoxLayout()
# #         controls_layout.setContentsMargins(0, 0, 0, 0)
# #         controls_layout.setAlignment(Qt.AlignLeft)

# #         # Volume slider
# #         self.volume_slider = QSlider(Qt.Vertical)
# #         self.volume_slider.setRange(0, 100)
# #         self.volume_slider.setValue(100)
# #         self.volume_slider.valueChanged.connect(self.set_volume)
# #         self.volume_slider.setStyleSheet("""
# #             QSlider::groove:vertical {
# #                 background: rgba(255, 255, 255, 0.2);
# #                 width: 6px;
# #                 border-radius: 3px;
# #             }
# #             QSlider::handle:vertical {
# #                 background: qlineargradient(
# #                     x1: 0, y1: 0, x2: 1, y2: 1,
# #                     stop: 0 #FFFFFF,
# #                     stop: 1 #000000
# #                 );
# #                 width: 20px;
# #                 height: 8px;  /* Thin horizontal line */
# #                 margin: 0px -5px;  /* To make sure the handle is visible */
# #                 border-radius: 4px;
# #                 border: 1px solid rgba(255, 255, 255, 0.8);  /* White border for visibility */
# #             }
# #             QSlider::handle:vertical:hover {
# #                 background: qlineargradient(
# #                     x1: 0, y1: 0, x2: 1, y2: 1,
# #                     stop: 0 #FFFFFF,
# #                     stop: 1 #AAAAAA
# #                 );
# #                 border: 1px solid rgba(255, 255, 255, 1);
# #             }
# #         """)

# #         self.volume_slider.setFixedHeight(album_art_height)
# #         volume_slider_container = QWidget()
# #         volume_slider_layout = QVBoxLayout(volume_slider_container)
# #         volume_slider_layout.addWidget(self.volume_slider)
# #         volume_slider_layout.setContentsMargins(0, 0, 0, 0)
# #         volume_slider_layout.setAlignment(Qt.AlignCenter)
# #         # Apply shadow effect to volume slider
# #         volume_shadow = QGraphicsDropShadowEffect()
# #         volume_shadow.setBlurRadius(20)
# #         volume_shadow.setColor(QColor(0, 0, 0, 160))
# #         volume_shadow.setOffset(5, 5)
# #         volume_slider_container.setGraphicsEffect(volume_shadow)

# #         # Album art
# #         if os.path.exists(self.album_art_file):
# #             pixmap = QPixmap(self.album_art_file)
# #             # Scale pixmap while maintaining aspect ratio
# #             pixmap = pixmap.scaled(album_art_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
# #         else:
# #             # Placeholder pixmap if album art is not found
# #             pixmap = QPixmap(album_art_size)
# #             pixmap.fill(QColor(41, 50, 60))

# #         self.album_art = AlbumArtWidget(pixmap, self)
# #         # Set the album art size to the pixmap's actual size
# #         self.album_art.setFixedSize(self.album_art.pixmap().size())
# #         album_art_width = int(screen_width * 0.15)
# #         album_art_height = int(screen_height * 0.15)

# #         # Time Slider - Positioned above the player controls
# #         self.time_slider = QSlider(Qt.Horizontal, self)
# #         self.time_slider.setRange(0, 100)  # Initial range, will be updated with audio length
# #         self.time_slider.sliderMoved.connect(self.seek_audio)
# #         self.time_slider.setStyleSheet(""" [Slider CSS Styles] """)
# #         self.time_slider.setFixedWidth(album_art_width)

# #         # Time Label - Positioned below the player controls, aligned left
# #         self.time_label = QLabel("00:00 / 00:00", self)
# #         self.time_label.setStyleSheet("color: white;")

# #         # Layout for the slider and time label
# #         self.slider_layout = QVBoxLayout(self.album_art)  # Make album_art the parent for alignment
# #         self.slider_layout.addWidget(self.time_slider)
# #         self.slider_layout.addWidget(self.time_label)
# #         self.slider_layout.setContentsMargins(0, 0, 0, 0)  # Adjust negative top margin to move closer to album art
# #         self.slider_layout.setAlignment(Qt.AlignBottom | Qt.AlignCenter)  # Center align below album art

 
# #         # Add widgets to the controls layout
# #         controls_layout.addWidget(volume_slider_container)
# #         controls_layout.addWidget(self.album_art)
# #         controls_layout.addStretch()

# #         # Visualizer
# #         visualizer_height = int(self.album_art.height() * 0.5)
# #         visualizer_width = self.album_art.width()
# #         self.visualizer = VisualizerWidget(self.album_art)  # Make album_art the parent
# #         self.visualizer.setFixedSize(visualizer_width, visualizer_height)

# #         # Position visualizer directly atop album art
# #         self.visualizer.move(0, self.album_art.height() - visualizer_height)  # Relative to album_art

# #         # Apply blur effect to visualizer
# #         blur_effect = QGraphicsBlurEffect()
# #         blur_effect.setBlurRadius(10)
# #         self.visualizer.setGraphicsEffect(blur_effect)

# #         # Add layouts and widgets to the main layout
# #         self.main_layout.addLayout(controls_layout)

# #         # Cosmic effect
# #         self.cosmic_effect = RealityDistortionEffect(self)
# #         self.cosmic_effect.show()

# #         self.show()

# #     def update_time_display(self):
# #         current_time = self.player.position() / 1000  # in seconds
# #         total_time = self.player.duration() / 1000  # in seconds
# #         self.time_label.setText(f"{self.format_time(current_time)} / {self.format_time(total_time)}")
# #         self.time_slider.setValue(int(current_time * 100 / total_time if total_time > 0 else 0))

# #     def format_time(self, seconds):
# #         mins = int(seconds // 60)
# #         secs = int(seconds % 60)
# #         return f"{mins:02}:{secs:02}"

# #     def seek_audio(self, value):
# #         total_time = self.player.duration()
# #         seek_position = value * total_time / 100
# #         self.player.setPosition(int(seek_position))

# #     def eventFilter(self, source, event):
# #         if event.type() == event.KeyPress and event.key() == Qt.Key_Escape:
# #             self.close()
# #             return True
# #         return super().eventFilter(source, event)

# #     def init_player(self):
# #         self.player = QMediaPlayer()
# #         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.audio_file)))
# #         self.player.stateChanged.connect(self.state_changed)
# #         self.player.setVolume(100)
# #         self.player.play()
# #         self.player.positionChanged.connect(self.update_time_display)
# #         self.player.durationChanged.connect(self.update_duration)  # Adjust total time when the media loads

# #         self.probe = QAudioProbe()
# #         self.probe.setSource(self.player)
# #         self.probe.audioBufferProbed.connect(self.process_buffer)


# #     def update_duration(self):
# #         total_time = self.player.duration() / 1000  # in seconds
# #         self.time_slider.setMaximum(int(total_time))  # Set slider range based on total time


# #     def process_buffer(self, buffer: QAudioBuffer):
# #         format = buffer.format()
# #         sample_type = format.sampleType()
# #         sample_size = format.sampleSize()
# #         channel_count = format.channelCount()

# #         # Determine the data type
# #         if sample_type == QAudioFormat.Float:
# #             dtype = np.float32
# #         elif sample_type == QAudioFormat.SignedInt:
# #             if sample_size == 16:
# #                 dtype = np.int16
# #             elif sample_size == 32:
# #                 dtype = np.int32
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         elif sample_type == QAudioFormat.UnSignedInt:
# #             if sample_size == 16:
# #                 dtype = np.uint16
# #             elif sample_size == 32:
# #                 dtype = np.uint32
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         else:
# #             print("Unsupported sample type:", sample_type)
# #             return

# #         # Extract the raw audio data
# #         size = buffer.byteCount()
# #         ptr = buffer.constData()
# #         ptr.setsize(size)
# #         data_bytes = ptr.asstring(size)

# #         # Convert the raw data to a NumPy array
# #         data_array = np.frombuffer(data_bytes, dtype=dtype)

# #         # Convert multi-channel to mono by averaging
# #         if channel_count > 1:
# #             data_array = data_array.reshape(-1, channel_count)
# #             data_array = data_array.mean(axis=1)

# #         # Normalize data to range [-1, 1] for integer types
# #         if np.issubdtype(dtype, np.integer):
# #             max_value = np.iinfo(dtype).max
# #             data_array = data_array.astype(np.float32) / max_value

# #         level = np.abs(data_array).mean()
# #         # Update the visualizer
# #         self.visualizer.update_levels(level)

# #     def set_volume(self, value):
# #         self.player.setVolume(value)

# #     def toggle_play(self):
# #         if self.player.state() == QMediaPlayer.PlayingState:
# #             self.player.pause()
# #             self.album_art.update_icon(QMediaPlayer.PausedState)
# #         else:
# #             self.player.play()
# #             self.album_art.update_icon(QMediaPlayer.PlayingState)

# #     def state_changed(self, state):
# #         self.album_art.update_icon(state)
# #         if state == QMediaPlayer.PausedState:
# #             self.visualizer.is_paused = True
# #             self.visualizer.audio_levels.clear()  # Clear levels immediately
# #         else:
# #             self.visualizer.is_paused = False

# # def main():
# #     app = QApplication(sys.argv)
# #     audio_file = r"C:\Users\thesh\Downloads\High Grade.mp3"
# #     album_art_file = r"C:\Users\thesh\Downloads\High Grade.png"  # Replace with your album art file

# #     if not os.path.exists(audio_file):
# #         print(f"Audio file not found: {audio_file}")
# #         sys.exit(1)

# #     visualizer = AudioVisualizer(audio_file, album_art_file)
# #     sys.exit(app.exec_())

# # if __name__ == '__main__':
# #     main()

# # exit()
# import sys
# import os
# import numpy as np
# from PyQt5.QtCore import Qt, QUrl, QTimer, QRectF, QSize
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QLabel, QSlider, QHBoxLayout, 
#     QVBoxLayout, QGraphicsBlurEffect, QGraphicsDropShadowEffect
# )
# from PyQt5.QtMultimedia import (
#     QMediaPlayer, QAudioProbe, QAudioBuffer, QMediaContent,
#     QAudioFormat
# )
# from PyQt5.QtGui import (
#     QPainter, QColor, QBrush, QLinearGradient,
#     QPixmap, QIcon
# )
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
# from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QTransform, QRadialGradient
# import sys
# import random
# import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout,
#                              QVBoxLayout, QPushButton, QSlider)
# from PyQt5.QtGui import QPixmap, QPalette, QColor, QBrush
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
# from PyQt5.QtCore import QUrl
# from PIL import Image
# import librosa
# import numpy as np
# from mutagen.mp3 import MP3
# from mutagen.flac import FLAC
# from mutagen.oggvorbis import OggVorbis
# import colorsys
# import math
# import math
# # class VisualizerWidget(QWidget):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.audio_levels = []
# #         self.max_levels = 100
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.update)
# #         self.timer.start(16)
# #         self.setAttribute(Qt.WA_TransparentForMouseEvents)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.effect_time = 0
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.update_effect_time)
# #         self.timer.start(16)

# #     def update_effect_time(self):
# #         self.effect_time += 0.1
# #         self.update()

# #     def update_levels(self, level):
# #         self.audio_levels.append(level)
# #         if len(self.audio_levels) > self.max_levels:
# #             self.audio_levels.pop(0)

# #     def paintEvent(self, event):
# #         painter = QPainter(self)
# #         painter.setCompositionMode(QPainter.CompositionMode_Source)
# #         painter.fillRect(self.rect(), Qt.transparent)

# #         if self.audio_levels:
# #             bar_count = len(self.audio_levels)
# #             bar_width = self.width() / bar_count
# #             max_height = self.height()

# #             for i, level in enumerate(self.audio_levels):
# #                 level = level ** 0.5
# #                 bar_height = level * max_height * 1.5
# #                 x = i * bar_width
# #                 y = self.height() - bar_height

# #                 gradient = QLinearGradient(x, y, x, y + bar_height)
# #                 gradient.setColorAt(0.0, QColor(255, 105, 180, 180))
# #                 gradient.setColorAt(1.0, QColor(255, 182, 193, 180))

# #                 painter.setBrush(QBrush(gradient))
# #                 painter.setPen(Qt.NoPen)

# #                 rect = QRectF(x, y, bar_width * 0.8, bar_height)
# #                 painter.drawRoundedRect(rect, bar_width * 0.4, bar_width * 0.4)

# #     def init_cosmic(self):
# #         self.stars = []
# #         self.nebulas = []
# #         for _ in range(500):
# #             self.stars.append({
# #                 'x': random.randint(0, self.width()),
# #                 'y': random.randint(0, self.height()),
# #                 'size': random.uniform(0.5, 3),
# #                 'twinkle_speed': random.uniform(0.02, 0.1)
# #             })
# #         for _ in range(5):
# #             self.nebulas.append({
# #                 'x': random.randint(0, self.width()),
# #                 'y': random.randint(0, self.height()),
# #                 'size': random.randint(200, 400),
# #                 'color': self.get_rainbow_color(random.random()),
# #                 'alpha': random.uniform(0.1, 0.3)
# #             })

# #     def get_rainbow_color(self, value):
# #         hue = value * 360
# #         return QColor.fromHsv(hue, 255, 255)

# #     def draw_cosmic(self, painter):
# #         for star in self.stars:
# #             twinkle = math.sin(self.effect_time * star['twinkle_speed']) * 0.5 + 0.5
# #             color = QColor(255, 255, 255, int(twinkle * 255))
# #             painter.setPen(color)
# #             painter.setBrush(color)
# #             painter.drawEllipse(QPoint(int(star['x']), int(star['y'])),
# #                                int(star['size']), int(star['size']))
# #         for nebula in self.nebulas:
# #             gradient = QRadialGradient(nebula['x'], nebula['y'], nebula['size'])
# #             color = nebula['color']
# #             color.setAlpha(int(255 * nebula['alpha']))
# #             gradient.setColorAt(0, color)
# #             color.setAlpha(0)
# #             gradient.setColorAt(1, color)
# #             painter.setPen(Qt.NoPen)
# #             painter.setBrush(gradient)
# #             painter.drawEllipse(QPoint(int(nebula['x']), int(nebula['y'])),
# #                                nebula['size'], nebula['size'])


# # class AlbumArtWidget(QLabel):
# #     def __init__(self, pixmap, audio_visualizer, parent=None):
# #         super().__init__(parent)
# #         self.audio_visualizer = audio_visualizer
# #         self.original_pixmap = pixmap
# #         self.setPixmap(self.original_pixmap)
# #         self.setScaledContents(True)
# #         self.is_hovered = False
# #         self.play_icon = QIcon(self.style().standardIcon(QApplication.style().SP_MediaPlay))
# #         self.pause_icon = QIcon(self.style().standardIcon(QApplication.style().SP_MediaPause))
# #         self.icon_label = QLabel(self)
# #         self.icon_label.setFixedSize(50, 50)
# #         self.icon_label.setAlignment(Qt.AlignCenter)
# #         self.icon_label.setStyleSheet("background-color: rgba(255, 255, 255, 0.7); border-radius: 25px;")
# #         self.icon_label.move(
# #             (self.width() - self.icon_label.width()) // 2,
# #             (self.height() - self.icon_label.height()) // 2)
# #         self.icon_label.setVisible(False)
# #         self.icon_label.setAttribute(Qt.WA_TransparentForMouseEvents)
# #         self.update_icon(QMediaPlayer.PlayingState)
# #         shadow = QGraphicsDropShadowEffect()
# #         shadow.setBlurRadius(20)
# #         shadow.setColor(QColor(0, 0, 0, 160))
# #         shadow.setOffset(5, 5)
# #         self.setGraphicsEffect(shadow)
# #         self.hover_effect = QGraphicsDropShadowEffect()
# #         self.hover_effect.setBlurRadius(30)
# #         self.hover_effect.setColor(QColor(255, 255, 255, 200))
# #         self.hover_effect.setOffset(0, 0)

# #     def enterEvent(self, event):
# #         self.is_hovered = True
# #         self.icon_label.setVisible(True)
# #         self.setCursor(Qt.PointingHandCursor)
# #         self.setGraphicsEffect(self.hover_effect)  # Apply hover effect

# #     def leaveEvent(self, event):
# #         self.is_hovered = False
# #         self.icon_label.setVisible(False)
# #         self.setCursor(Qt.ArrowCursor)
# #         self.setGraphicsEffect(None)  # Remove hover effect

# #     def mousePressEvent(self, event):
# #         if event.button() == Qt.LeftButton:
# #             self.audio_visualizer.toggle_play()

# #     def update_icon(self, state):
# #         if state == QMediaPlayer.PlayingState:
# #             self.icon_label.setPixmap(self.pause_icon.pixmap(50, 50))
# #         else:
# #             self.icon_label.setPixmap(self.play_icon.pixmap(50, 50))

# #     def resizeEvent(self, event):
# #         self.icon_label.move(
# #             (self.width() - self.icon_label.width()) // 2,
# #             (self.height() - self.icon_label.height()) // 2)
# #         self.icon_label.raise_()
        
        
# # class AudioVisualizer(QWidget):
# #     def init(self, audio_file, album_art_file):
# #         super().init()
# #         self.audio_file = audio_file
# #         self.album_art_file = album_art_file
# #         self.audio_levels = []
# #         self.init_ui()
# #         self.init_player()
# #         self.effect_time = 0
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.update_effect_time)
# #         self.timer.start(16)
# #         self.bubbles = []
# #         self.init_bubbles()

# #     def init_bubbles(self):
# #         for _ in range(20):
# #             self.bubbles.append({
# #                 'x': random.randint(0, self.width()),
# #                 'y': random.randint(0, self.height()),
# #                 'size': random.randint(20, 50),
# #                 'color': self.get_random_color(),
# #                 'alpha': random.uniform(0.5, 0.8),
# #                 'speed_x': random.uniform(-1, 1),
# #                 'speed_y': random.uniform(-1, 1)
# #             })

# #     def get_random_color(self):
# #         return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# #     def update_effect_time(self):
# #         self.effect_time += 1
# #         self.update()
# #         self.visualizer.update()

# #     def init_ui(self):
# #         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.showFullScreen()

# #         self.installEventFilter(self)
# #         screen = QApplication.primaryScreen()
# #         size = screen.size()
# #         screen_width = size.width()
# #         screen_height = size.height()
# #         album_art_width = int(screen_width * 0.15)
# #         album_art_height = int(screen_height * 0.15)
# #         album_art_size = QSize(album_art_width, album_art_height)
# #         self.main_layout = QVBoxLayout(self)
# #         self.main_layout.setContentsMargins(20, screen_height * 25 // 32, 20, 0)
# #         self.main_layout.setAlignment(Qt.AlignBottom)
# #         controls_layout = QHBoxLayout()
# #         controls_layout.setContentsMargins(0, 0, 0, 0)
# #         controls_layout.setAlignment(Qt.AlignLeft)
# #         self.volume_slider = QSlider(Qt.Vertical)
# #         self.volume_slider.setRange(0, 100)
# #         self.volume_slider.setValue(100)
# #         self.volume_slider.valueChanged.connect(self.set_volume) 

# #         self.volume_slider.setStyleSheet("""
# #             QSlider::groove:vertical {
# #                 background: rgba(255, 255, 255, 0.2);
# #                 width: 6px;
# #                 border-radius: 3px;
# #             }
# #             QSlider::handle:vertical {
# #                 background: qlineargradient(
# #                     x1: 0, y1: 0, x2: 1, y2: 1,
# #                     stop: 0 #FFFFFF,
# #                     stop: 1 #000000
# #                 );
# #                 width: 20px;
# #                 height: 8px;
# #                 margin: 0px -5px;
# #                 border-radius: 4px;
# #                 border: 1px solid rgba(255, 255, 255, 0.8);
# #             }
# #             QSlider::handle:vertical:hover {
# #                 background: qlineargradient(
# #                     x1: 0, y1: 0, x2: 1, y2: 1,
# #                     stop: 0 #FFFFFF,
# #                     stop: 1 #AAAAAA
# #                 );
# #                 border: 1px solid rgba(255, 255, 255, 1);
# #             }
# #         """)
# #         self.volume_slider.setFixedHeight(album_art_height)
# #         volume_slider_container = QWidget()
# #         volume_slider_layout = QVBoxLayout(volume_slider_container)
# #         volume_slider_layout.addWidget(self.volume_slider)
# #         volume_slider_layout.setContentsMargins(0, 0, 0, 0)
# #         volume_slider_layout.setAlignment(Qt.AlignCenter)
# #         volume_shadow = QGraphicsDropShadowEffect()
# #         volume_shadow.setBlurRadius(20)
# #         volume_shadow.setColor(QColor(0, 0, 0, 160))
# #         volume_shadow.setOffset(5, 5)
# #         volume_slider_container.setGraphicsEffect(volume_shadow)
# #         if os.path.exists(self.album_art_file):
# #             pixmap = QPixmap(self.album_art_file)
# #             pixmap = pixmap.scaled(album_art_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
# #         else:
# #             pixmap = QPixmap(album_art_size)
# #             pixmap.fill(QColor(41, 50, 60))

# #         self.album_art = AlbumArtWidget(pixmap, self)
# #         self.album_art.setFixedSize(self.album_art.pixmap().size())
# #         controls_layout.addWidget(volume_slider_container)
# #         controls_layout.addWidget(self.album_art)
# #         controls_layout.addStretch()
# #         visualizer_height = int(self.album_art.height() * 0.5)
# #         visualizer_width = self.album_art.width()
# #         self.visualizer = VisualizerWidget(self.album_art)
# #         self.visualizer.setFixedSize(visualizer_width, visualizer_height)
# #         self.visualizer.move(0, self.album_art.height() - visualizer_height)
# #         blur_effect = QGraphicsBlurEffect()
# #         blur_effect.setBlurRadius(10)
# #         self.visualizer.setGraphicsEffect(blur_effect)
# #         self.main_layout.addLayout(controls_layout)
# #         self.show()

# #     def eventFilter(self, source, event):
# #         if event.type() == event.KeyPress and event.key() == Qt.Key_Escape:
# #             self.close()
# #             return True
# #         return super().eventFilter(source, event)

# #     def init_player(self):
# #         self.player = QMediaPlayer()
# #         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.audio_file)))
# #         self.player.stateChanged.connect(self.state_changed)
# #         self.player.setVolume(100)
# #         self.player.play()

# #         self.probe = QAudioProbe()
# #         self.probe.setSource(self.player)
# #         self.probe.audioBufferProbed.connect(self.process_buffer)

# #     def process_buffer(self, buffer: QAudioBuffer):
# #         format = buffer.format()
# #         sample_type = format.sampleType()
# #         sample_size = format.sampleSize()
# #         channel_count = format.channelCount()

# #         if sample_type == QAudioFormat.Float:
# #             dtype = np.float32
# #         elif sample_type == QAudioFormat.SignedInt:
# #             if sample_size == 16:
# #                 dtype = np.int16
# #             elif sample_size == 32:
# #                 dtype = np.int32
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         elif sample_type == QAudioFormat.UnSignedInt:
# #             if sample_size == 16:
# #                 dtype = np.uint16
# #             elif sample_size == 32:
# #                 dtype = np.uint32
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         else:
# #             print("Unsupported sample type:", sample_type)
# #             return

# #         size = buffer.byteCount()
# #         ptr = buffer.constData()
# #         ptr.setsize(size)
# #         data_bytes = ptr.asstring(size)

# #         data_array = np.frombuffer(data_bytes, dtype=dtype)

# #         if channel_count > 1:
# #             data_array = data_array.reshape(-1, channel_count)
# #             data_array = data_array.mean(axis=1)

# #         if np.issubdtype(dtype, np.integer):
# #             max_value = np.iinfo(dtype).max
# #             data_array = data_array.astype(np.float32) / max_value

# #         level = np.abs(data_array).mean()
# #         self.visualizer.update_levels(level)
# #         self.update_bubbles(level)

# #     def set_volume(self, value):
# #         self.player.setVolume(value)

# #     def toggle_play(self):
# #         if self.player.state() == QMediaPlayer.PlayingState:
# #             self.player.pause()
# #             self.album_art.update_icon(QMediaPlayer.PausedState)
# #         else:
# #             self.player.play()
# #             self.album_art.update_icon(QMediaPlayer.PlayingState)

# #     def state_changed(self, state):
# #         self.album_art.update_icon(state)

# #     def paintEvent(self, event):
# #         painter = QPainter(self)
# #         painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
# #         self.draw_bubbles(painter)

# #     def draw_bubbles(self, painter):
# #         for bubble in self.bubbles:
# #             x = bubble['x']
# #             y = bubble['y']
# #             size = bubble['size']
# #             color = bubble['color']
# #             alpha = bubble['alpha']

# #             gradient = QRadialGradient(x, y, size)
# #             gradient.setColorAt(0, color.lighter(150))
# #             gradient.setColorAt(0.5, color)
# #             gradient.setColorAt(1, color.darker(150))

# #             color.setAlphaF(alpha)
# #             painter.setPen(Qt.NoPen)
# #             painter.setBrush(gradient)
# #             painter.drawEllipse(QPoint(int(x), int(y)), size, size)

# #     def update_bubbles(self, level):
# #         for bubble in self.bubbles:
# #             bubble['x'] += bubble['speed_x'] * (level * 5 + 1)
# #             bubble['y'] += bubble['speed_y'] * (level * 5 + 1)

# #             if bubble['x'] > self.width() + bubble['size']:
# #                 bubble['x'] = -bubble['size']
# #             elif bubble['x'] < -bubble['size']:
# #                 bubble['x'] = self.width() + bubble['size']

# #             if bubble['y'] > self.height() + bubble['size']:
# #                 bubble['y'] = -bubble['size']
# #             elif bubble['y'] < -bubble['size']:
# #                 bubble['y'] = self.height() + bubble['size']

# #             bubble['size'] += level * 2
# #             if bubble['size'] > 80:
# #                 bubble['size'] = 20

# #             bubble['alpha'] = level * 0.8 + 0.2


# # def main():
# #     app = QApplication(sys.argv)
# #     audio_file = r"C:\Users\thesh\Downloads\High Grade.mp3"
# #     album_art_file = r"C:\Users\thesh\Downloads\High Grade.png"

# #     if not os.path.exists(audio_file):
# #         print(f"Audio file not found: {audio_file}")
# #         sys.exit(1)

# #     visualizer = AudioVisualizer(audio_file, album_art_file)
# #     sys.exit(app.exec_())


# # if __name__ == '__main__':
# #     main()

# # exit()
# # class VisualizerWidget(QWidget):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.audio_levels = []
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.update)
# #         self.timer.start(16)  # Refresh at approximately 60 FPS for less delay
# #         self.setAttribute(Qt.WA_TransparentForMouseEvents)
# #         self.setAttribute(Qt.WA_TranslucentBackground)

# #     def update_levels(self, level):
# #         # Keep a fixed number of levels for smooth visualization
# #         max_levels = 100  # Increase for smoother animation
# #         self.audio_levels.append(level)
# #         if len(self.audio_levels) > max_levels:
# #             self.audio_levels.pop(0)

# #     def paintEvent(self, event):
# #         painter = QPainter(self)
# #         # Set background to transparent
# #         painter.setCompositionMode(QPainter.CompositionMode_Source)
# #         painter.fillRect(self.rect(), Qt.transparent)

# #         if self.audio_levels:
# #             bar_count = len(self.audio_levels)
# #             bar_width = self.width() / bar_count
# #             max_height = self.height()

# #             for i, level in enumerate(self.audio_levels):
# #                 # Apply easing for smoother animation
# #                 level = level ** 0.5
# #                 # Scale the level to the height of the widget
# #                 bar_height = level * max_height * 1.5  # Adjust scaling for less lag
# #                 x = i * bar_width
# #                 y = self.height() - bar_height  # Start from bottom

# #                 # Create gradient for the bars
# #                 gradient = QLinearGradient(x, y, x, y + bar_height)
# #                 gradient.setColorAt(0.0, QColor(255, 105, 180, 180))  # Pink (Hot Pink)
# #                 gradient.setColorAt(1.0, QColor(255, 182, 193, 180))  # Light Pink

# #                 painter.setBrush(QBrush(gradient))
# #                 painter.setPen(Qt.NoPen)

# #                 # Draw rounded bars
# #                 rect = QRectF(x, y, bar_width * 0.8, bar_height)
# #                 painter.drawRoundedRect(rect, bar_width * 0.4, bar_width * 0.4)

# # class AlbumArtWidget(QLabel):
# #     def __init__(self, pixmap, audio_visualizer, parent=None):
# #         super().__init__(parent)
# #         self.audio_visualizer = audio_visualizer
# #         self.setPixmap(pixmap)
# #         self.setScaledContents(True)
# #         self.is_hovered = False
# #         self.play_icon = QIcon(self.style().standardIcon(QApplication.style().SP_MediaPlay))
# #         self.pause_icon = QIcon(self.style().standardIcon(QApplication.style().SP_MediaPause))
# #         self.icon_label = QLabel(self)
# #         self.icon_label.setFixedSize(50, 50)
# #         self.icon_label.setAlignment(Qt.AlignCenter)
# #         self.icon_label.setStyleSheet("background-color: rgba(255, 255, 255, 0.7); border-radius: 25px;")
# #         self.icon_label.move(
# #             (self.width() - self.icon_label.width()) // 2,
# #             (self.height() - self.icon_label.height()) // 2)
# #         self.icon_label.setVisible(False)
# #         self.icon_label.setAttribute(Qt.WA_TransparentForMouseEvents)
# #         self.update_icon(QMediaPlayer.PlayingState)
# #         # Apply drop shadow effect
# #         shadow = QGraphicsDropShadowEffect()
# #         shadow.setBlurRadius(20)
# #         shadow.setColor(QColor(0, 0, 0, 160))
# #         shadow.setOffset(5, 5)
# #         self.setGraphicsEffect(shadow)

# #     def enterEvent(self, event):
# #         self.is_hovered = True
# #         self.icon_label.setVisible(True)
# #         self.setCursor(Qt.PointingHandCursor)

# #     def leaveEvent(self, event):
# #         self.is_hovered = False
# #         self.icon_label.setVisible(False)
# #         self.setCursor(Qt.ArrowCursor)

# #     def mousePressEvent(self, event):
# #         if event.button() == Qt.LeftButton:
# #             self.audio_visualizer.toggle_play()

# #     def update_icon(self, state):
# #         if state == QMediaPlayer.PlayingState:
# #             self.icon_label.setPixmap(self.pause_icon.pixmap(50, 50))
# #         else:
# #             self.icon_label.setPixmap(self.play_icon.pixmap(50, 50))

# #     def resizeEvent(self, event):
# #         self.icon_label.move(
# #             (self.width() - self.icon_label.width()) // 2,
# #             (self.height() - self.icon_label.height()) // 2)
# #         self.icon_label.raise_()  # Ensure icon_label is on top

# # class AudioVisualizer(QWidget):
# #     def __init__(self, audio_file, album_art_file):
# #         super().__init__()
# #         self.audio_file = audio_file
# #         self.album_art_file = album_art_file
# #         self.audio_levels = []
# #         self.init_ui()
# #         self.init_player()

# #     def init_ui(self):
# #         # Make the window frameless, always on top, and transparent
# #         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.showFullScreen()

# #         # Close mechanism: Press 'Esc' to close
# #         self.installEventFilter(self)

# #         # Get screen dimensions
# #         screen = QApplication.primaryScreen()
# #         size = screen.size()
# #         screen_width = size.width()
# #         screen_height = size.height()

# #         # Set album art size relative to screen size
# #         album_art_width = int(screen_width * 0.15)
# #         album_art_height = int(screen_height * 0.15)
# #         album_art_size = QSize(album_art_width, album_art_height)

# #         # Create main layout
# #         self.main_layout = QVBoxLayout(self)
# #         self.main_layout.setContentsMargins(20, screen_height * 25 // 32, 20, 0)   # A bit lower



# #         self.main_layout.setAlignment(Qt.AlignBottom)

# #         # Controls layout (volume slider and album art)
# #         controls_layout = QHBoxLayout()
# #         controls_layout.setContentsMargins(0, 0, 0, 0)
# #         controls_layout.setAlignment(Qt.AlignLeft)

# #         # Volume slider
# #         self.volume_slider = QSlider(Qt.Vertical)
# #         self.volume_slider.setRange(0, 100)
# #         self.volume_slider.setValue(100)
# #         self.volume_slider.valueChanged.connect(self.set_volume)
# #         self.volume_slider.setStyleSheet("""
# #             QSlider::groove:vertical {
# #                 background: rgba(255, 255, 255, 0.2);
# #                 width: 6px;
# #                 border-radius: 3px;
# #             }
# #             QSlider::handle:vertical {
# #                 background: qlineargradient(
# #                     x1: 0, y1: 0, x2: 1, y2: 1,
# #                     stop: 0 #FFFFFF,
# #                     stop: 1 #000000
# #                 );
# #                 width: 20px;
# #                 height: 8px;  /* Thin horizontal line */
# #                 margin: 0px -5px;  /* To make sure the handle is visible */
# #                 border-radius: 4px;
# #                 border: 1px solid rgba(255, 255, 255, 0.8);  /* White border for visibility */
# #             }
# #             QSlider::handle:vertical:hover {
# #                 background: qlineargradient(
# #                     x1: 0, y1: 0, x2: 1, y2: 1,
# #                     stop: 0 #FFFFFF,
# #                     stop: 1 #AAAAAA
# #                 );
# #                 border: 1px solid rgba(255, 255, 255, 1);
# #             }
# #         """)



# #         self.volume_slider.setFixedHeight(album_art_height)
# #         volume_slider_container = QWidget()
# #         volume_slider_layout = QVBoxLayout(volume_slider_container)
# #         volume_slider_layout.addWidget(self.volume_slider)
# #         volume_slider_layout.setContentsMargins(0, 0, 0, 0)
# #         volume_slider_layout.setAlignment(Qt.AlignCenter)
# #         # Apply shadow effect to volume slider
# #         volume_shadow = QGraphicsDropShadowEffect()
# #         volume_shadow.setBlurRadius(20)
# #         volume_shadow.setColor(QColor(0, 0, 0, 160))
# #         volume_shadow.setOffset(5, 5)
# #         volume_slider_container.setGraphicsEffect(volume_shadow)

# #         # Album art
# #         if os.path.exists(self.album_art_file):
# #             pixmap = QPixmap(self.album_art_file)
# #             # Scale pixmap while maintaining aspect ratio
# #             pixmap = pixmap.scaled(album_art_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
# #         else:
# #             # Placeholder pixmap if album art is not found
# #             pixmap = QPixmap(album_art_size)
# #             pixmap.fill(QColor(41, 50, 60))

# #         self.album_art = AlbumArtWidget(pixmap, self)
# #         # Set the album art size to the pixmap's actual size
# #         self.album_art.setFixedSize(self.album_art.pixmap().size())

# #         # Add widgets to the controls layout
# #         controls_layout.addWidget(volume_slider_container)
# #         controls_layout.addWidget(self.album_art)
# #         controls_layout.addStretch()

# #             # Visualizer
# #         visualizer_height = int(self.album_art.height() * 0.5)
# #         visualizer_width = self.album_art.width()
# #         self.visualizer = VisualizerWidget(self.album_art)  # Make album_art the parent
# #         self.visualizer.setFixedSize(visualizer_width, visualizer_height)

# #         # Position visualizer directly atop album art
# #         self.visualizer.move(0, self.album_art.height() - visualizer_height)  # Relative to album_art

# #         # Apply blur effect to visualizer
# #         blur_effect = QGraphicsBlurEffect()
# #         blur_effect.setBlurRadius(10)
# #         self.visualizer.setGraphicsEffect(blur_effect)
# #         # Add layouts and widgets to the main layout (only album art, not visualizer)
# #         self.main_layout.addLayout(controls_layout)  # controls_layout already contains album_art

# #         self.show()

# #     def eventFilter(self, source, event):
# #         if event.type() == event.KeyPress and event.key() == Qt.Key_Escape:
# #             self.close()
# #             return True
# #         return super().eventFilter(source, event)

# #     def init_player(self):
# #         self.player = QMediaPlayer()
# #         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.audio_file)))
# #         self.player.stateChanged.connect(self.state_changed)
# #         self.player.setVolume(100)
# #         self.player.play()

# #         self.probe = QAudioProbe()
# #         self.probe.setSource(self.player)
# #         self.probe.audioBufferProbed.connect(self.process_buffer)

# #     def process_buffer(self, buffer: QAudioBuffer):
# #         format = buffer.format()
# #         sample_type = format.sampleType()
# #         sample_size = format.sampleSize()
# #         channel_count = format.channelCount()

# #         # Determine the data type
# #         if sample_type == QAudioFormat.Float:
# #             dtype = np.float32
# #         elif sample_type == QAudioFormat.SignedInt:
# #             if sample_size == 16:
# #                 dtype = np.int16
# #             elif sample_size == 32:
# #                 dtype = np.int32
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         elif sample_type == QAudioFormat.UnSignedInt:
# #             if sample_size == 16:
# #                 dtype = np.uint16
# #             elif sample_size == 32:
# #                 dtype = np.uint32
# #             else:
# #                 print("Unsupported sample size:", sample_size)
# #                 return
# #         else:
# #             print("Unsupported sample type:", sample_type)
# #             return

# #         # Extract the raw audio data
# #         size = buffer.byteCount()
# #         ptr = buffer.constData()
# #         ptr.setsize(size)
# #         data_bytes = ptr.asstring(size)

# #         # Convert the raw data to a NumPy array
# #         data_array = np.frombuffer(data_bytes, dtype=dtype)

# #         # Convert multi-channel to mono by averaging
# #         if channel_count > 1:
# #             data_array = data_array.reshape(-1, channel_count)
# #             data_array = data_array.mean(axis=1)

# #         # Normalize data to range [-1, 1] for integer types
# #         if np.issubdtype(dtype, np.integer):
# #             max_value = np.iinfo(dtype).max
# #             data_array = data_array.astype(np.float32) / max_value

# #         level = np.abs(data_array).mean()
# #         # Update the visualizer
# #         self.visualizer.update_levels(level)

# #     def set_volume(self, value):
# #         self.player.setVolume(value)

# #     def toggle_play(self):
# #         if self.player.state() == QMediaPlayer.PlayingState:
# #             self.player.pause()
# #             self.album_art.update_icon(QMediaPlayer.PausedState)
# #         else:
# #             self.player.play()
# #             self.album_art.update_icon(QMediaPlayer.PlayingState)

# #     def state_changed(self, state):
# #         self.album_art.update_icon(state)


# # def main():
# #     app = QApplication(sys.argv)
# #     audio_file = r"C:\Users\thesh\Downloads\High Grade.mp3"
# #     album_art_file = r"C:\Users\thesh\Downloads\High Grade.png"  # Replace with your album art file

# #     if not os.path.exists(audio_file):
# #         print(f"Audio file not found: {audio_file}")
# #         sys.exit(1)

# #     visualizer = AudioVisualizer(audio_file, album_art_file)
# #     sys.exit(app.exec_())


# # if __name__ == '__main__':
# #     main()


        
        
# # exit()
        

# # import sys
# # import random
# # import math
# # import colorsys

# # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
# # from PyQt5.QtCore import Qt, QTimer, QPoint
# # from PyQt5.QtGui import QPainter, QColor, QPen
# # import sys
# # import random
# # import math
# # import colorsys
# # import numpy as np

# # from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
# #                              QPushButton, QComboBox, QSlider)
# # from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
# # from PyQt5.QtGui import QPainter, QColor, QPen, QFont, QBrush
# # import pyaudio
# # import librosa

# # class AudioAnalyzer:
# #     def __init__(self, filepath):
# #         self.filepath = filepath
# #         # self.y, self.sr = librosa.load(filepath)
# #         self.y, self.sr = librosa.load(filepath, sr=None, mono=True) # Make mono explicitly

# #         self.p = pyaudio.PyAudio()
# #         self.stream = None
# #         self.CHUNK = 2**10  # Adjust as needed
# #         self.bass = 0
# #         self.mid = 0
# #         self.treble = 0
# #         self.volume = 0
# #         self.fft_data = np.array([])

# #     def start_analysis(self):
# #         self.stream = self.p.open(format=pyaudio.paFloat32,
# #                                   channels=1, # Ensure single channel
# #                                   rate=self.sr,
# #                                   output=True, # Stream is now specifically for output
# #                                   frames_per_buffer=self.CHUNK)
# #         self.timer = QTimer()
# #         self.timer.timeout.connect(self.analyze_audio)
# #         self.timer.start(50)  # Update every 50ms

# #     def analyze_audio(self):
# #         try:
# #             data = self.y[self.current_frame:self.current_frame + self.CHUNK]
# #             self.fft_data = np.fft.fft(data)

# #             freqs = np.fft.fftfreq(len(data), 1.0 / self.sr)
# #             bass_band = np.abs(self.fft_data[np.where((freqs >= 20) & (freqs <= 250))])
# #             mid_band = np.abs(self.fft_data[np.where((freqs > 250) & (freqs <= 4000))])
# #             treble_band = np.abs(self.fft_data[np.where((freqs > 4000) & (freqs <= 16000))])
# #             self.bass = np.average(bass_band) if len(bass_band) > 0 else 0
# #             self.mid = np.average(mid_band) if len(mid_band) > 0 else 0
# #             self.treble = np.average(treble_band) if len(treble_band) > 0 else 0

# #             self.volume = np.max(np.abs(data))

# #         except Exception as e:
# #             print(f"Error during audio analysis: {e}")

# #     def stop_analysis(self):
# #         if self.stream:
# #             self.stream.stop_stream()
# #             self.stream.close()
# #             self.p.terminate()
# #             self.timer.stop()

# # class ReactiveVisualizer(QWidget):
# #     def __init__(self, audio_analyzer):
# #         super().__init__()
# #         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # No Tool flag
# #         self.setAttribute(Qt.WA_TranslucentBackground)
# #         self.setGeometry(QApplication.primaryScreen().geometry())
# #         self.audio_analyzer = audio_analyzer
# #         self.timer = QTimer(self)
# #         self.timer.timeout.connect(self.update)  # Just call update
# #         self.timer.start(30)

# #     def paintEvent(self, event):
# #         if not self.audio_analyzer.fft_data.size: # Check for empty fft_data
# #             return

# #         painter = QPainter(self)
# #         painter.setRenderHint(QPainter.Antialiasing)
# #         width, height = self.width(), self.height()

# #         # Example visualization (replace with your creative effects)
# #         painter.setBrush(QColor(0, 0, 0, 50))  # Semi-transparent black background
# #         painter.drawRect(0, 0, width, height)  # Draw a rectangle

# #         fft_data = self.audio_analyzer.fft_data
# #         num_bars = min(50, len(fft_data) // 2)  # Limit num_bars
# #         bar_width = width / num_bars
# #         for i in range(num_bars):
# #             magnitude = np.abs(fft_data[i])
# #             bar_height = int(magnitude * height / 10000) # Suitable scaling
# #             x = int(i * bar_width)
# #             y = height - bar_height
# #             color = QColor.fromHsv(int(i * 360 / num_bars), 255, 255) # Rainbow colors

# #             painter.setBrush(color)
# #             painter.drawRect(QRect(x, y, int(bar_width), bar_height))

# # class MainUI(QWidget):
# #     def __init__(self, filepath):
# #         super().__init__()
# #         self.setWindowTitle("Audio Reactive Visualizer")
# #         self.audio_analyzer = AudioAnalyzer(filepath)
# #         self.visualizer = ReactiveVisualizer(self.audio_analyzer)

# #         layout = QVBoxLayout()

# #         self.play_button = QPushButton("Play")
# #         self.play_button.clicked.connect(self.toggle_playback)
# #         layout.addWidget(self.play_button)

# #         self.volume_slider = QSlider(Qt.Horizontal)
# #         self.volume_slider.setRange(0, 100)
# #         self.volume_slider.setValue(50)
# #         self.volume_slider.valueChanged.connect(self.change_volume)  # Volume control
# #         layout.addWidget(self.volume_slider)

# #         self.setLayout(layout)

# #         self.playing = False

# #     def toggle_playback(self):
# #         if not self.playing:
# #             self.playing = True
# #             self.play_button.setText("Pause")
# #             self.audio_analyzer.start_analysis()
# #             self.visualizer.show()  # Show the visualizer
# #         else:
# #             self.playing = False
# #             self.play_button.setText("Play")
# #             self.audio_analyzer.stop_analysis()
# #             self.visualizer.hide()  # Hide the visualizer when paused

# #     def change_volume(self, value):
# #         # Implement logic to scale audio based on slider value. Requires modifying audio_analyzer
# #         # Example (if directly modifying numpy audio data):
# #         # self.audio_analyzer.y = self.audio_analyzer.y * (value / 50.0)  # Example scaling

# #         pass  # Replace with actual volume control

# # def main():
# #     filepath = r"C:\Users\thesh\Downloads\High Grade.mp3"  # Add your file here
# #     app = QApplication(sys.argv)
# #     ex = MainUI(filepath)  # Use this as main class for UI
# #     ex.show()  # Show main UI
# #     sys.exit(app.exec_())

# # if __name__ == '__main__':
# #     main()
 
# # exit()
# import sys
# import random
# import math
# import colorsys

# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
#                              QPushButton)
# from PyQt5.QtCore import (Qt, QTimer, QPoint, QPointF, QRect,
#                           QPropertyAnimation, QEasingCurve)
# from PyQt5.QtGui import (QPainter, QColor, QTransform, QFont, QPainterPath,
#                          QLinearGradient, QRadialGradient, QPen, QBrush)

# class RealityDistortionEffect(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Window setup
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.setAttribute(Qt.WA_TransparentForMouseEvents)

#         # Get screen dimensions
#         screen = QApplication.primaryScreen()
#         self.screen_geometry = screen.geometry()
#         self.setGeometry(self.screen_geometry)

#         # Initialize effect parameters
#         self.effect_time = 0
#         self.phase = 0
#         self.current_effect = None  # Store the currently active effect

#         # Initialize components for all effects
#         self.init_effect_components()
#         self.lightning_alpha = 255
#         # Animation timer
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_effect)
#         self.timer.start(16)  # ~60 FPS

#     def init_effect_components(self):
#         # Energy field parameters
#         self.energy_nodes = []
#         self.energy_connections = []
#         self.init_energy_field()

#         # Quantum particles
#         self.quantum_particles = []
#         self.init_quantum_particles()

#         # Void portals
#         self.void_portals = []
#         self.init_void_portals()

#         # Reality fractures
#         self.fractures = []
#         self.init_reality_fractures()

#         # Time ripples
#         self.time_ripples = []

#         # DNA helix parameters
#         self.dna_offset = 0
#         self.dna_strands = []
#         self.init_dna_helix()

#         # Dimensional tears
#         self.tears = []
#         self.init_dimensional_tears()

#         # Matrix effect parameters
#         self.matrix_chars = []

#         # Particle effect parameters
#         self.particles = []

#         # Binary effect parameters
#         self.binary_streams = []

#         # Lightning effect parameters
#         self.lightning_points = []

#         # Vortex effect parameters
#         self.vortex_particles = []

#         # Cosmic effect parameters
#         self.stars = []
#         self.nebulas = []

#         # Quantum effect parameters (additional)
#         self.quantum_fields = []

#         # Psychedelic effect parameters (additional)
#         self.psychedelic_offset = 0

#     def set_effect(self, effect_name):
#         self.start_effect(effect_name)
#         self.show() 

#     def init_energy_field(self):
#         # Create energy nodes
#         for _ in range(20):
#             node = {
#                 'pos': QPointF(random.randint(0, self.width()),
#                               random.randint(0, self.height())),
#                 'velocity': QPointF(random.uniform(-2, 2),
#                                     random.uniform(-2, 2)),
#                 'charge': random.choice([-1, 1]),
#                 'energy': random.uniform(0.5, 1.0),
#                 'connections': set()
#             }
#             self.energy_nodes.append(node)

#     def init_quantum_particles(self):
#         self.quantum_particles = []
#         for _ in range(30):
#             particle = {
#                 'pos': QPointF(random.randint(0, self.width()),
#                             random.randint(0, self.height())),
#                 'wave_phase': random.uniform(0, 2 * math.pi),  # Add this line
#                 'frequency': random.uniform(0.02, 0.05),
#                 'amplitude': random.uniform(20, 50),
#                 'uncertainty': random.uniform(10, 30),
#                 'color': self.get_quantum_color(random.random()),
#                 'entangled_partner': None
#             }
#             self.quantum_particles.append(particle)

#         # Create entangled pairs
#         for i in range(0, len(self.quantum_particles), 2):
#             if i + 1 < len(self.quantum_particles):
#                 self.quantum_particles[i]['entangled_partner'] = self.quantum_particles[i + 1]
#                 self.quantum_particles[i + 1]['entangled_partner'] = self.quantum_particles[i]


#     def init_void_portals(self):
#         for _ in range(3):
#             portal = {
#                 'center': QPointF(random.randint(100, self.width() - 100),
#                                   random.randint(100, self.height() - 100)),
#                 'radius': random.uniform(50, 150),
#                 'rotation': random.uniform(0, 2 * math.pi),
#                 'spin_speed': random.uniform(0.01, 0.03),
#                 'particles': [],
#                 'distortion': random.uniform(0.5, 1.5)
#             }

#             # Add portal particles
#             for _ in range(100):
#                 angle = random.uniform(0, 2 * math.pi)
#                 dist = random.uniform(0, portal['radius'])
#                 particle = {
#                     'angle': angle,
#                     'distance': dist,
#                     'speed': random.uniform(0.01, 0.03),
#                     'size': random.uniform(1, 4)
#                 }
#                 portal['particles'].append(particle)

#             self.void_portals.append(portal)

#     def init_reality_fractures(self):
#         for _ in range(5):
#             points = []
#             x = random.randint(0, self.width())
#             y = random.randint(0, self.height())

#             # Generate fracture path
#             num_points = random.randint(5, 10)
#             for _ in range(num_points):
#                 x += random.randint(-100, 100)
#                 y += random.randint(-100, 100)
#                 points.append(QPoint(x, y))

#             fracture = {
#                 'points': points,
#                 'width': random.uniform(2, 5),
#                 'glow_intensity': random.uniform(0.5, 1.0),
#                 'color': self.get_quantum_color(random.random()),
#                 'distortion': random.uniform(0.5, 1.5)
#             }
#             self.fractures.append(fracture)

#     def init_dna_helix(self):
#         num_strands = 2
#         strand_length = 50

#         for strand in range(num_strands):
#             points = []
#             for i in range(strand_length):
#                 point = {
#                     'base_y': i * 20,
#                     'phase': (i * math.pi / 10) + (strand * math.pi),
#                     'nucleotide': random.choice(['A', 'T', 'G', 'C']),
#                     'color': self.get_quantum_color(random.random())
#                 }
#                 points.append(point)
#             self.dna_strands.append(points)

#     def init_dimensional_tears(self):
#         for _ in range(3):
#             start = QPoint(random.randint(0, self.width()),
#                            random.randint(0, self.height()))

#             tear = {
#                 'start': start,
#                 'points': [start],
#                 'growth_direction': QPointF(random.uniform(-1, 1),
#                                             random.uniform(-1, 1)),
#                 'length': random.randint(100, 300),
#                 'width': random.uniform(5, 15),
#                 'reality_fragments': [],
#                 'color': self.get_quantum_color(random.random())
#             }

#             # Generate tear path
#             current = QPointF(start)
#             for _ in range(10):
#                 angle = math.atan2(tear['growth_direction'].y(),
#                                   tear['growth_direction'].x())
#                 angle += random.uniform(-0.5, 0.5)
#                 length =random.uniform(20, 40)
#                 dx = math.cos(angle) * length
#                 dy = math.sin(angle) * length
#                 current += QPointF(dx, dy)
#                 tear['points'].append(QPoint(int(current.x()), int(current.y())))

#             # Add reality fragments
#             for _ in range(20):
#                 fragment = {
#                     'pos': QPointF(random.uniform(-50, 50),
#                                   random.uniform(-50, 50)),
#                     'rotation': random.uniform(0, 2 * math.pi),
#                     'size': random.uniform(5, 15)
#                 }
#                 tear['reality_fragments'].append(fragment)

#             self.tears.append(tear)

#     def init_matrix(self):
#         self.matrix_chars = []
#         columns = self.width() // 20  # character width

#         for x in range(columns):
#             self.matrix_chars.append({
#                 'x': x * 20,
#                 'y': random.randint(-500, 0),
#                 'speed': random.uniform(3, 7),
#                 'length': random.randint(5, 15),
#                 'chars': [chr(random.randint(0x30A0, 0x30FF)) for _ in range(20)]
#             })

#     def init_particles(self):
#         self.particles = []
#         for _ in range(100):
#             self.particles.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'dx': random.uniform(-2, 2),
#                 'dy': random.uniform(-2, 2),
#                 'size': random.randint(2, 6),
#                 'color': QColor(random.randint(100, 255),
#                                random.randint(100, 255),
#                                random.randint(100, 255),
#                                150)
#             })

#     def init_binary(self):
#         self.binary_streams = []
#         columns = self.width() // 15
#         for x in range(columns):
#             self.binary_streams.append({
#                 'x': x * 15,
#                 'y': random.randint(-500, 0),
#                 'speed': random.uniform(2, 5),
#                 'length': random.randint(10, 30),
#                 'color': QColor(0, 255, 0, 150)
#             })

#     def init_lightning(self):
#         self.lightning_points = []
#         start_x = random.randint(0, self.width())
#         current_x = start_x
#         current_y = 0

#         while current_y < self.height():
#             next_y = current_y + random.randint(20, 50)
#             next_x = current_x + random.randint(-50, 50)
#             self.lightning_points.append((current_x, current_y))
#             current_x, current_y = next_x, next_y

#     def init_vortex(self):
#         self.vortex_particles = []
#         for _ in range(1000):
#             angle = random.uniform(0, 2 * math.pi)
#             radius = random.uniform(100, max(self.width(), self.height()))
#             self.vortex_particles.append({
#                 'angle': angle,
#                 'radius': radius,
#                 'speed': random.uniform(0.01, 0.03),
#                 'size': random.uniform(2, 6),
#                 'color': self.get_rainbow_color(random.random())
#             })

#     def init_cosmic(self):
#         self.stars = []
#         self.nebulas = []
#         # Create stars
#         for _ in range(500):
#             self.stars.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'size': random.uniform(0.5, 3),
#                 'twinkle_speed': random.uniform(0.02, 0.1)
#             })
#         # Create nebula clouds
#         for _ in range(5):
#             self.nebulas.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'size': random.randint(200, 400),
#                 'color': self.get_rainbow_color(random.random()),
#                 'alpha': random.uniform(0.1, 0.3)
#             })

#     def init_quantum(self):  # For the additional quantum effect
#         self.quantum_particles = []
#         self.quantum_fields = []
#         # Quantum particles
#         for _ in range(50):
#             self.quantum_particles.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'phase': random.uniform(0, 2 * math.pi),
#                 'frequency': random.uniform(0.02, 0.1),
#                 'amplitude': random.uniform(20, 50),
#                 'color': self.get_rainbow_color(random.random())
#             })
#         # Quantum fields
#         for _ in range(3):
#             self.quantum_fields.append({
#                 'offset': random.uniform(0, 2 * math.pi),
#                 'speed': random.uniform(0.01, 0.03),
#                 'wavelength': random.uniform(100, 300)
#             })

#     def get_quantum_color(self, value):
#         # Generate quantum-inspired colors
#         hue = (math.sin(value * math.pi) + 1) / 2
#         sat = 0.8 + math.sin(value * 4 * math.pi) * 0.2
#         val = 0.8 + math.sin(value * 8 * math.pi) * 0.2
#         rgb = colorsys.hsv_to_rgb(hue, sat, val)
#         return QColor(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

#     def get_rainbow_color(self, pos):
#         hue = pos % 1.0
#         rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
#         return QColor(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

#     def update_energy_field(self):
#         # Update node positions
#         for node in self.energy_nodes:
#             # Update position
#             node['pos'] += node['velocity']

#             # Bounce off edges
#             if node['pos'].x() < 0 or node['pos'].x() > self.width():
#                 node['velocity'].setX(-node['velocity'].x())
#             if node['pos'].y() < 0 or node['pos'].y() > self.height():
#                 node['velocity'].setY(-node['velocity'].y())

#             # Reset connections
#             node['connections'].clear()

#         # Update connections
#         self.energy_connections.clear()
#         for i, node1 in enumerate(self.energy_nodes):
#             for j, node2 in enumerate(self.energy_nodes[i + 1:], i + 1):
#                 distance = QPointF.dotProduct(
#                     node1['pos'] - node2['pos'],
#                     node1['pos'] - node2['pos']
#                 ) ** 0.5

#                 if distance < 200:
#                     strength = 1 - (distance / 200)
#                     if node1['charge'] == node2['charge']:
#                         strength *= 0.5

#                     if strength > 0.2:
#                         self.energy_connections.append({
#                             'node1': node1,
#                             'node2': node2,
#                             'strength': strength
#                         })
#                         node1['connections'].add(j)
#                         node2['connections'].add(i)

#     def update_quantum_particles(self):
#         for particle in self.quantum_particles:
#             # Update wave phase
#             particle['wave_phase'] += particle['frequency']
#             # Update position based on quantum uncertainty
#             dx = random.gauss(0, particle['uncertainty'])
#             dy = random.gauss(0, particle['uncertainty'])
#             particle['pos'] += QPointF(dx, dy)

#             # Keep particles within bounds
#             particle['pos'].setX(max(0, min(self.width(), particle['pos'].x())))
#             particle['pos'].setY(max(0, min(self.height(), particle['pos'].y())))

#             # Entanglement effects
#             if particle['entangled_partner']:
#                 # Correlate some properties between entangled particles
#                 particle['wave_phase'] = -particle['entangled_partner']['wave_phase']

#     def update_void_portals(self):
#         for portal in self.void_portals:
#             portal['rotation'] += portal['spin_speed']

#             for particle in portal['particles']:
#                 particle['angle'] += particle['speed']

#                 # Spiral particles toward center
#                 if particle['distance'] > 5:
#                     particle['distance'] *= 0.99
#                 else:
#                     # Reset particle to edge when it reaches center
#                     particle['distance'] = portal['radius']
#                     particle['angle'] = random.uniform(0, 2 * math.pi)

#     def update_time_ripples(self):
#         # Update existing ripples
#         for ripple in self.time_ripples[:]:
#             ripple['radius'] += ripple['speed']
#             # Ensure alpha calculation results in an integer
#             ripple['alpha'] = int(max(0, 255 * (1 - ripple['radius'] / ripple['max_radius'])))

#             if ripple['radius'] > ripple['max_radius']:
#                 self.time_ripples.remove(ripple)

#         # Randomly add new ripples
#         if random.random() < 0.02:
#             pos = QPointF(random.randint(0, self.width()),
#                           random.randint(0, self.height()))
#             self.add_time_ripple(pos)

#     def add_time_ripple(self, pos):
#         ripple = {
#             'center': pos,
#             'radius': 0,
#             'max_radius': random.uniform(100, 300),
#             'speed': random.uniform(2, 5),
#             'width': random.uniform(20, 40),
#             'alpha': 255
#         }
#         self.time_ripples.append(ripple)

#     def update_dna_helix(self):
#         self.dna_offset += 0.02

#         # Update DNA strand positions
#         for strand in self.dna_strands:
#             for point in strand:
#                 point['phase'] += 0.02

#     def update_dimensional_tears(self):
#         for tear in self.tears:
#             # Update reality fragments
#             for fragment in tear['reality_fragments']:
#                 fragment['rotation'] += random.uniform(0.02, 0.05)

#                 # Random movement
#                 fragment['pos'] += QPointF(random.uniform(-1, 1),
#                                           random.uniform(-1, 1))

#                 # Keep fragments near the tear
#                 if fragment['pos'].manhattanLength() > 100:
#                     fragment['pos'] *= 0.95

#     def update_matrix(self):
#         for stream in self.matrix_chars:
#             # Update position
#             stream['y'] += stream['speed']
#             if stream['y'] > self.height() + 500:
#                 stream['y'] = random.randint(-500, 0)

#     def update_particles(self):
#         for particle in self.particles:
#             # Update position
#             particle['x'] += particle['dx']
#             particle['y'] += particle['dy']

#             # Bounce off edges
#             if particle['x'] < 0 or particle['x'] > self.width():
#                 particle['dx'] *= -1
#             if particle['y'] < 0 or particle['y'] > self.height():
#                 particle['dy'] *= -1

#     def update_binary(self):
#         for stream in self.binary_streams:
#             stream['y'] += stream['speed']
#             if stream['y'] > self.height() + 200:
#                 stream['y'] = random.randint(-500, 0)

#     def update_lightning(self):
#         if not hasattr(self, 'lightning_alpha'):
#             self.lightning_alpha = 255

#         # Fade out
#         self.lightning_alpha -= 15
#         if self.lightning_alpha <= 0:
#             self.init_lightning()
#             self.lightning_alpha = 255

#     def update_vortex(self):
#         center_x = self.width() // 2
#         center_y = self.height() // 2

#         # Update and draw particles
#         for particle in self.vortex_particles:
#             # Update position
#             particle['angle'] += particle['speed']
#             particle['radius'] -= 0.5

#             # Reset particles that reach center
#             if particle['radius'] < 10:
#                 particle['radius'] = max(self.width(), self.height())
#                 particle['angle'] = random.uniform(0, 2 * math.pi)

#     def update_cosmic(self):
#         pass  # No specific update needed for cosmic, twinkling is handled in drawing

#     def update_quantum(self):  # For the additional quantum effect
#         for field in self.quantum_fields:
#             field['offset'] += field['speed']

#         for particle in self.quantum_particles:
#             # Update quantum state
#             particle['phase'] += particle['frequency']

#     def update_psychedelic(self):
#         self.psychedelic_offset += 0.1

#     def draw_energy_field(self, painter):
#         # Draw connections
#         for conn in self.energy_connections:
#             gradient = QLinearGradient(conn['node1']['pos'], conn['node2']['pos'])

#             # Create electric color based on charge interaction
#             if conn['node1']['charge'] == conn['node2']['charge']:
#                 color1 = QColor(64, 64, 255, int(255 * conn['strength']))
#                 color2 = QColor(128, 128, 255, 0)
#             else:
#                 color1 = QColor(255, 64, 64, int(255 * conn['strength']))
#                 color2 = QColor(255, 128, 128, 0)

#             gradient.setColorAt(0, color1)
#             gradient.setColorAt(1, color2)

#             pen = QPen(QBrush(gradient), 2)
#             painter.setPen(pen)
#             painter.drawLine(conn['node1']['pos'], conn['node2']['pos'])

#         # Draw nodes
#         for node in self.energy_nodes:
#             # Create glow effect
#             radius = 20
#             gradient = QRadialGradient(node['pos'], radius)

#             base_color = QColor(64, 64, 255) if node['charge'] > 0 else QColor(255, 64, 64)
#             glow_color = QColor(base_color)
#             glow_color.setAlpha(int(100 * node['energy']))

#             gradient.setColorAt(0, glow_color)
#             gradient.setColorAt(1, QColor(0, 0, 0, 0))

#             painter.setPen(Qt.NoPen)
#             painter.setBrush(gradient)
#             painter.drawEllipse(node['pos'], radius, radius)

#             # Draw core
#             painter.setBrush(base_color)
#             painter.drawEllipse(node['pos'], 5, 5)

#     def draw_quantum_particles(self, painter):
#         self.init_quantum_particles()
#         for particle in self.quantum_particles:
#             radius = 10 + math.sin(particle['wave_phase']) * particle['amplitude']

#             # Draw quantum probability cloud
#             for i in range(5):
#                 cloud_color = QColor(particle['color'])
#                 cloud_color.setAlpha(50 - i * 10)

#                 cloud_radius = radius + i * 10
#                 uncertainty_offset = QPointF(
#                     random.gauss(0, particle['uncertainty']),
#                     random.gauss(0, particle['uncertainty'])
#                 )

#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(cloud_color)
#                 painter.drawEllipse(particle['pos'] + uncertainty_offset,
#                                    cloud_radius, cloud_radius)

#             # Draw entanglement lines
#             if particle['entangled_partner']:
#                 gradient = QLinearGradient(particle['pos'],
#                                           particle['entangled_partner']['pos'])
#                 gradient.setColorAt(0, QColor(particle['color']))
#                 gradient.setColorAt(1, QColor(particle['entangled_partner']['color']))

#                 pen = QPen(QBrush(gradient), 1)
#                 pen.setStyle(Qt.DashLine)
#                 painter.setPen(pen)
#                 painter.drawLine(particle['pos'],
#                                  particle['entangled_partner']['pos'])

#     def draw_void_portals(self, painter):
#         for portal in self.void_portals:
#             # Draw void background
#             gradient = QRadialGradient(portal['center'], portal['radius'])
#             gradient.setColorAt(0, QColor(0, 0, 0, 200))
#             gradient.setColorAt(0.7, QColor(20, 0, 40, 150))
#             gradient.setColorAt(1, QColor(0, 0, 0, 0))

#             painter.setPen(Qt.NoPen)
#             painter.setBrush(gradient)
#             painter.drawEllipse(portal['center'],
#                                portal['radius'], portal['radius'])

#             # Draw portal particles
#             for particle in portal['particles']:
#                 # Calculate particle position
#                 angle = particle['angle'] + portal['rotation']
#                 dist = particle['distance']
#                 spiral_x = math.cos(angle * portal['distortion']) * dist
#                 spiral_y = math.sin(angle * portal['distortion']) * dist

#                 pos = portal['center'] + QPointF(spiral_x, spiral_y)

#                 # Draw particle with trail
#                 for i in range(3):
#                     trail_angle = angle - i * 0.1
#                     trail_x = math.cos(trail_angle * portal['distortion']) * dist
#                     trail_y = math.sin(trail_angle * portal['distortion']) * dist
#                     trail_pos = portal['center'] + QPointF(trail_x, trail_y)

#                     color = QColor(128 + i * 40, 0, 255 - i * 40, 150 - i * 40)
#                     painter.setBrush(color)
#                     painter.drawEllipse(trail_pos,
#                                        particle['size'], particle['size'])

#     def draw_reality_fractures(self, painter):
#         for fracture in self.fractures:
#             # Create fracture path
#             path = QPainterPath()
#             path.moveTo(fracture['points'][0])

#             for i in range(1, len(fracture['points'])):
#                 path.lineTo(fracture['points'][i])

#             # Draw fracture glow
#             for i in range(3):
#                 glow_color = QColor(fracture['color'])
#                 glow_color.setAlpha(int(100 * fracture['glow_intensity'] / (i + 1)))

#                 pen = QPen(glow_color, fracture['width'] + i * 4)
#                 pen.setCapStyle(Qt.RoundCap)
#                 painter.setPen(pen)
#                 painter.drawPath(path)

#             # Draw distortion effects
#             for i in range(len(fracture['points']) - 1):
#                 p1 = fracture['points'][i]
#                 p2 = fracture['points'][i + 1]

#                 # Add random distortion lines
#                 num_lines = int(QPoint(p2 - p1).manhattanLength() / 10)
#                 for _ in range(num_lines):
#                     t = random.random()
#                     mid = p1 + (p2 - p1) * t

#                     offset = QPoint(
#                         random.randint(-20, 20),
#                         random.randint(-20, 20)
#                     )

#                     color = QColor(fracture['color'])
#                     color.setAlpha(random.randint(50, 150))
#                     painter.setPen(QPen(color, 1))
#                     painter.drawLine(mid, mid + offset)

#     def draw_time_ripples(self, painter):
#         for ripple in self.time_ripples:
#             # Create ripple gradient
#             gradient = QRadialGradient(ripple['center'], ripple['radius'])
#             # Convert alpha to integer
#             alpha = int(ripple['alpha'])
#             ripple_color = QColor(0, 255, 255, alpha)
#             gradient.setColorAt(0, QColor(0, 0, 0, 0))
#             gradient.setColorAt(ripple['radius'] / ripple['max_radius'], ripple_color)
#             gradient.setColorAt(1, QColor(0, 0, 0, 0))

#             # Draw ripple
#             painter.setPen(Qt.NoPen)
#             painter.setBrush(gradient)
#             painter.drawEllipse(ripple['center'],
#                                int(ripple['radius']), int(ripple['radius']))

#             # Draw time distortion artifacts
#             num_artifacts = int(ripple['radius'] / 10)
#             for _ in range(num_artifacts):
#                 angle = random.uniform(0, 2 * math.pi)
#                 distance = random.uniform(0.8, 1.2) * ripple['radius']

#                 pos = ripple['center'] + QPointF(
#                     math.cos(angle) * distance,
#                     math.sin(angle) * distance
#                 )

#                 artifact_alpha = int(ripple['alpha'] * random.uniform(0.2, 0.8))
#                 artifact_color = QColor(0, 255, 255, artifact_alpha)
#                 painter.setPen(QPen(artifact_color, 2))

#                 # Draw random time artifact symbols
#                 size = int(random.uniform(5, 15))
#                 if random.random() < 0.3:
#                     # Clock symbol
#                     painter.drawEllipse(pos, size, size)
#                     painter.drawLine(pos, pos + QPointF(size * 0.8, 0))
#                 else:
#                     # Abstract time rune
#                     for _ in range(3):
#                         angle = random.uniform(0, 2 * math.pi)
#                         painter.drawLine(
#                             pos,
#                             pos + QPointF(math.cos(angle) * size,
#                                           math.sin(angle) * size)
#                         )

#     def draw_dna_helix(self, painter):
#         center_x = self.width() * 0.8
#         base_y = (self.height() - len(self.dna_strands[0]) * 20) / 2
#         amplitude = 100

#         for i, strand in enumerate(self.dna_strands):
#             prev_point = None

#             for point in strand:
#                 # Calculate helix position
#                 x = center_x + math.cos(point['phase']) * amplitude
#                 y = base_y + point['base_y']
#                 current_point = QPointF(x, y)

#                 # Draw strand
#                 if prev_point:
#                     color = QColor(point['color'])
#                     color.setAlpha(150)
#                     painter.setPen(QPen(color, 3))
#                     painter.drawLine(prev_point, current_point)

#                 # Draw nucleotide
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(QColor(point['color']))
#                 painter.drawEllipse(current_point, 5, 5)

#                 # Draw base pair connections
#                 if i == 0:
#                     pair_x = center_x + math.cos(point['phase'] + math.pi) * amplitude
#                     pair_y = y
#                     pair_point = QPointF(pair_x, pair_y)

#                     # Draw connection with color based on base pair
#                     if point['nucleotide'] in 'AT':
#                         connection_color = QColor(255, 200, 0, 100)
#                     else:  # GC pair
#                         connection_color = QColor(0, 200, 255, 100)

#                     painter.setPen(QPen(connection_color, 2))
#                     painter.drawLine(current_point, pair_point)

#                 prev_point = current_point

#     def draw_dimensional_tears(self, painter):
#         for tear in self.tears:
#             # Create tear path
#             path = QPainterPath()
#             path.moveTo(tear['points'][0])

#             for point in tear['points'][1:]:
#                 path.lineTo(point)

#             # Draw tear glow
#             for i in range(4):
#                 glow_color = QColor(tear['color'])
#                 glow_color.setAlpha(150 - i * 30)

#                 pen = QPen(glow_color, tear['width'] + i * 4)
#                 pen.setCapStyle(Qt.RoundCap)
#                 painter.setPen(pen)
#                 painter.drawPath(path)

#             # Draw reality fragments
#             for fragment in tear['reality_fragments']:
#                 painter.save()

#                 # Transform for rotation
#                 painter.translate(
#                     tear['points'][0] + fragment['pos']
#                 )
#                 painter.rotate(math.degrees(fragment['rotation']))

#                 # Draw fragment
#                 fragment_color = QColor(tear['color'])
#                 fragment_color.setAlpha(100)
#                 painter.setPen(QPen(fragment_color, 2))
#                 painter.setBrush(Qt.NoBrush)

#                 # Random fragment shapes
#                 size = int(fragment['size'])  # Convert to integer
#                 if random.random() < 0.5:
#                     # Draw rectangle with integer coordinates
#                     painter.drawRect(-size // 2, -size // 2, size, size)
#                 else:
#                     # For ellipse we can use float values
#                     painter.drawEllipse(QPointF(0, 0),
#                                        fragment['size'] / 2,
#                                        fragment['size'] / 2)

#                 painter.restore()

#     def draw_matrix(self, painter):
#         painter.setFont(QFont('Courier New', 14))

#         for stream in self.matrix_chars:
#             # Draw characters with fading effect
#             for i in range(stream['length']):
#                 y_pos = int(stream['y']) - (i * 20)
#                 if 0 <= y_pos <= self.height():
#                     # Lead character is brighter
#                     if i == 0:
#                         painter.setPen(QColor(255, 255, 255, 200))
#                     else:
#                         alpha = 200 - (i * 15)
#                         painter.setPen(QColor(0, 255, 0, max(0, alpha)))

#                     # Randomly change characters
#                     if random.random() < 0.1:
#                         stream['chars'][i] = chr(random.randint(0x30A0, 0x30FF))

#                     painter.drawText(stream['x'], y_pos, stream['chars'][i])

#     def draw_particles(self, painter):
#         for particle in self.particles:
#             # Draw particle
#             painter.setPen(Qt.NoPen)
#             painter.setBrush(particle['color'])
#             painter.drawEllipse(int(particle['x']), int(particle['y']),
#                                particle['size'], particle['size'])

#     def draw_binary(self, painter):
#         painter.setFont(QFont('Courier New', 12))

#         for stream in self.binary_streams:
#             for i in range(stream['length']):
#                 y_pos = int(stream['y']) - (i * 15)
#                 if 0 <= y_pos <= self.height():
#                     # Randomly choose 0 or 1
#                     binary_char = str(random.randint(0, 1))
#                     alpha = 200 - (i * 8)
#                     painter.setPen(QColor(0, 255, 0, max(0, alpha)))
#                     painter.drawText(stream['x'], y_pos, binary_char)

#     def draw_lightning(self, painter):
#         # Draw lightning
#         pen = painter.pen()
#         pen.setColor(QColor(255, 255, 255, self.lightning_alpha))
#         pen.setWidth(2)
#         painter.setPen(pen)

#         for i in range(len(self.lightning_points) - 1):
#             painter.drawLine(self.lightning_points[i][0], self.lightning_points[i][1],
#                              self.lightning_points[i + 1][0], self.lightning_points[i + 1][1])

#     def draw_vortex(self, painter):
#         center_x = self.width() // 2
#         center_y = self.height() // 2

#         for particle in self.vortex_particles:
#             # Calculate position
#             x = center_x + math.cos(particle['angle']) * particle['radius']
#             y = center_y + math.sin(particle['angle']) * particle['radius']

#             # Draw particle with trail
#             painter.setPen(Qt.NoPen)
#             color = particle['color']
#             for i in range(3):
#                 trail_x = center_x + math.cos(particle['angle'] - i * 0.1) * (particle['radius'] + i * 10)
#                 trail_y = center_y + math.sin(particle['angle'] - i * 0.1) * (particle['radius'] + i * 10)
#                 color.setAlpha(150 - i * 40)
#                 painter.setBrush(color)
#                 painter.drawEllipse(QPoint(int(trail_x), int(trail_y)),
#                                    int(particle['size']), int(particle['size']))

#     def draw_cosmic(self, painter):
#         # Draw background stars
#         for star in self.stars:
#             twinkle = math.sin(self.effect_time * star['twinkle_speed']) * 0.5 + 0.5
#             color = QColor(255, 255, 255, int(twinkle * 255))
#             painter.setPen(color)
#             painter.setBrush(color)
#             painter.drawEllipse(QPoint(int(star['x']), int(star['y'])),
#                                int(star['size']), int(star['size']))

#         # Draw nebulas with gradient
#         for nebula in self.nebulas:
#             gradient = QRadialGradient(nebula['x'], nebula['y'], nebula['size'])
#             color = nebula['color']
#             color.setAlpha(int(255 * nebula['alpha']))
#             gradient.setColorAt(0, color)
#             color.setAlpha(0)
#             gradient.setColorAt(1, color)

#             painter.setPen(Qt.NoPen)
#             painter.setBrush(gradient)
#             painter.drawEllipse(QPoint(int(nebula['x']), int(nebula['y'])),
#                                nebula['size'], nebula['size'])

#     def draw_quantum(self, painter):  # For the additional quantum effect
#         # Draw quantum fields
#         for field in self.quantum_fields:
#             path = QPainterPath()
#             path.moveTo(0, self.height() / 2)

#             for x in range(0, self.width(), 2):
#                 y = self.height() / 2 + math.sin(x / field['wavelength'] + field['offset']) * 100
#                 path.lineTo(x, y)

#             pen = painter.pen()
#             pen.setWidth(2)
#             pen.setColor(QColor(0, 255, 255, 50))
#             painter.setPen(pen)
#             painter.drawPath(path)

#         # Draw quantum particles with probability clouds
#         for particle in self.quantum_particles:
#             # Calculate probability cloud
#             for i in range(10):
#                 angle = i * math.pi / 5
#                 distance = particle['amplitude'] * math.sin(particle['phase'])
#                 x = particle['x'] + math.cos(angle) * distance
#                 y = particle['y'] + math.sin(angle) * distance

#                 color = particle['color']
#                 color.setAlpha(50)
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(color)
#                 painter.drawEllipse(QPoint(int(x), int(y)), 5, 5)

#     def draw_psychedelic(self, painter):
#         for x in range(0, self.width(), 20):
#             for y in range(0, self.height(), 20):
#                 value = math.sin(x * 0.01 + self.psychedelic_offset) + \
#                         math.cos(y * 0.01 + self.psychedelic_offset)
#                 color = self.get_rainbow_color((value + 2) / 4)
#                 color.setAlpha(100)
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(color)
#                 painter.drawRect(x, y, 20, 20)

#     def start_effect(self, effect_name):
#         self.current_effect = effect_name
#         self.effect_time =0
#         self.phase = 0  # Reset phase for effects that use it

#         # Initialize effect-specific components if needed
#         if effect_name == "matrix":
#             self.init_matrix()
#         elif effect_name == "particles":
#             self.init_particles()
#         elif effect_name == "lightning":
#             self.init_lightning()
#         elif effect_name == "binary":
#             self.init_binary()
#         elif effect_name == "vortex":
#             self.init_vortex()
#         elif effect_name == "cosmic":
#             self.init_cosmic()
#         elif effect_name == "quantum":
#             self.init_quantum()

#     def clear_effect(self):
#         self.effect_time = 0
#         self.phase = 0
#         self.current_effect = None  # Store the currently active effect

#         # Initialize components for all effects
#         self.init_effect_components()

#         # Animation timer
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_effect)
#         self.timer.start(16)  # ~60 FPS
        
#     def update_effect(self):
#         self.effect_time += 1
#         self.phase += 0.02

#         # Update components based on the current effect
#         if self.current_effect == "energy":
#             self.update_energy_field()
#         elif self.current_effect == "quantum_particles":
#             self.update_quantum_particles()
#         elif self.current_effect == "void_portals":
#             self.update_void_portals()
#         elif self.current_effect == "time_ripples":
#             self.update_time_ripples()
#         elif self.current_effect == "dna_helix":
#             self.update_dna_helix()
#         elif self.current_effect == "dimensional_tears":
#             self.update_dimensional_tears()
#         elif self.current_effect == "matrix":
#             self.update_matrix()
#         elif self.current_effect == "particles":
#             self.update_particles()
#         elif self.current_effect == "binary":
#             self.update_binary()
#         elif self.current_effect == "lightning":
#             self.update_lightning()
#         elif self.current_effect == "vortex":
#             self.update_vortex()
#         elif self.current_effect == "cosmic":
#             self.update_cosmic()  # No specific update needed for cosmic
#         elif self.current_effect == "quantum":
#             self.update_quantum()
#         elif self.current_effect == "psychedelic":
#             self.update_psychedelic()

#         # Add random time ripples (if enabled)
#         if self.current_effect and random.random() < 0.02:
#             pos = QPointF(random.randint(0, self.width()),
#                           random.randint(0, self.height()))
#             self.add_time_ripple(pos)

#         self.update()  # Trigger repaint event

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)

#         # Draw effects based on the current effect
#         if self.current_effect == "energy":
#             self.draw_energy_field(painter)
#         elif self.current_effect == "quantum_particles":
#             self.draw_quantum_particles(painter)
#         elif self.current_effect == "void_portals":
#             self.draw_void_portals(painter)
#         elif self.current_effect == "reality_fractures":
#             self.draw_reality_fractures(painter)
#         elif self.current_effect == "time_ripples":
#             self.draw_time_ripples(painter)
#         elif self.current_effect == "dna_helix":
#             self.draw_dna_helix(painter)
#         elif self.current_effect == "dimensional_tears":
#             self.draw_dimensional_tears(painter)
#         elif self.current_effect == "matrix":
#             self.draw_matrix(painter)
#         elif self.current_effect == "particles":
#             self.draw_particles(painter)
#         elif self.current_effect == "binary":
#             self.draw_binary(painter)
#         elif self.current_effect == "lightning":
#             self.draw_lightning(painter)
#         elif self.current_effect == "vortex":
#             self.draw_vortex(painter)
#         elif self.current_effect == "cosmic":
#             self.draw_cosmic(painter)
#         elif self.current_effect == "quantum":
#             self.draw_quantum(painter)
#         elif self.current_effect == "psychedelic":
#             self.draw_psychedelic(painter)

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             self.close()

# class EffectController(QWidget):  # This class becomes less important, but can still be used for testing
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()

#         # Create effect buttons (optional, for testing)
#         effects = ["energy", "quantum_particles", "void_portals", "reality_fractures",
#                    "time_ripples", "dna_helix", "dimensional_tears", "matrix",
#                    "particles", "lightning", "binary", "vortex", "cosmic", "quantum", "psychedelic"]
#         self.screen_effect = RealityDistortionEffect()

#         for effect in effects:
#             btn = QPushButton(effect.replace("_", " ").title())
#             btn.clicked.connect(lambda checked, e=effect: self.screen_effect.set_effect(e))  # Use set_effect
#             layout.addWidget(btn)

#         # Add a clear button
#         clear_btn = QPushButton("Clear Effect")
#         clear_btn.clicked.connect(self.screen_effect.clear_effect)
#         layout.addWidget(clear_btn)

#         self.setLayout(layout)
#         self.setWindowTitle('Screen Effects Controller')
#         self.show()

# def main():
#     app = QApplication(sys.argv)
#     controller = EffectController()  # The controller is optional, just for the buttons

#     # Example of how to use set_effect directly:
#     effect = RealityDistortionEffect()
#     # effect.set_effect("matrix")  # Directly set the desired effect


#     # Or, if you keep the controller, you can still use the buttons.
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()



# exit()
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QTimer, QPoint, QPointF, QRect, QPropertyAnimation, QEasingCurve
# from PyQt5.QtGui import (QPainter, QColor, QTransform, QFont, QPainterPath, 
#                         QLinearGradient, QRadialGradient, QPen, QBrush)
# import sys
# import random
# import math
# import colorsys
# import numpy as np
# from datetime import datetime

# class RealityDistortionEffect(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.setAttribute(Qt.WA_TransparentForMouseEvents)
        
#         # Get screen dimensions
#         screen = QApplication.primaryScreen()
#         self.screen_geometry = screen.geometry()
#         self.setGeometry(self.screen_geometry)
        
#         # Initialize effect parameters
#         self.effect_time = 0
#         self.phase = 0
#         self.init_effect_components()
        
#         # Animation timer
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_effect)
#         self.timer.start(16)  # ~60 FPS

#     def init_effect_components(self):
#         # Energy field parameters
#         self.energy_nodes = []
#         self.energy_connections = []
#         self.init_energy_field()
        
#         # Quantum particles
#         self.quantum_particles = []
#         self.init_quantum_particles()
        
#         # Void portals
#         self.void_portals = []
#         self.init_void_portals()
        
#         # Reality fractures
#         self.fractures = []
#         self.init_reality_fractures()
        
#         # Time ripples
#         self.time_ripples = []
        
#         # DNA helix parameters
#         self.dna_offset = 0
#         self.dna_strands = []
#         self.init_dna_helix()
        
#         # Dimensional tears
#         self.tears = []
#         self.init_dimensional_tears()

#     def init_energy_field(self):
#         # Create energy nodes
#         for _ in range(20):
#             node = {
#                 'pos': QPointF(random.randint(0, self.width()),
#                              random.randint(0, self.height())),
#                 'velocity': QPointF(random.uniform(-2, 2),
#                                   random.uniform(-2, 2)),
#                 'charge': random.choice([-1, 1]),
#                 'energy': random.uniform(0.5, 1.0),
#                 'connections': set()
#             }
#             self.energy_nodes.append(node)

#     def init_quantum_particles(self):
#         for _ in range(30):
#             particle = {
#                 'pos': QPointF(random.randint(0, self.width()),
#                              random.randint(0, self.height())),
#                 'wave_phase': random.uniform(0, 2 * math.pi),
#                 'frequency': random.uniform(0.02, 0.05),
#                 'amplitude': random.uniform(20, 50),
#                 'uncertainty': random.uniform(10, 30),
#                 'color': self.get_quantum_color(random.random()),
#                 'entangled_partner': None
#             }
#             self.quantum_particles.append(particle)
        
#         # Create entangled pairs
#         for i in range(0, len(self.quantum_particles), 2):
#             if i + 1 < len(self.quantum_particles):
#                 self.quantum_particles[i]['entangled_partner'] = self.quantum_particles[i + 1]
#                 self.quantum_particles[i + 1]['entangled_partner'] = self.quantum_particles[i]

#     def init_void_portals(self):
#         for _ in range(3):
#             portal = {
#                 'center': QPointF(random.randint(100, self.width() - 100),
#                                 random.randint(100, self.height() - 100)),
#                 'radius': random.uniform(50, 150),
#                 'rotation': random.uniform(0, 2 * math.pi),
#                 'spin_speed': random.uniform(0.01, 0.03),
#                 'particles': [],
#                 'distortion': random.uniform(0.5, 1.5)
#             }
            
#             # Add portal particles
#             for _ in range(100):
#                 angle = random.uniform(0, 2 * math.pi)
#                 dist = random.uniform(0, portal['radius'])
#                 particle = {
#                     'angle': angle,
#                     'distance': dist,
#                     'speed': random.uniform(0.01, 0.03),
#                     'size': random.uniform(1, 4)
#                 }
#                 portal['particles'].append(particle)
                
#             self.void_portals.append(portal)

#     def init_reality_fractures(self):
#         for _ in range(5):
#             points = []
#             x = random.randint(0, self.width())
#             y = random.randint(0, self.height())
            
#             # Generate fracture path
#             num_points = random.randint(5, 10)
#             for _ in range(num_points):
#                 x += random.randint(-100, 100)
#                 y += random.randint(-100, 100)
#                 points.append(QPoint(x, y))
            
#             fracture = {
#                 'points': points,
#                 'width': random.uniform(2, 5),
#                 'glow_intensity': random.uniform(0.5, 1.0),
#                 'color': self.get_quantum_color(random.random()),
#                 'distortion': random.uniform(0.5, 1.5)
#             }
#             self.fractures.append(fracture)

#     def init_dna_helix(self):
#         num_strands = 2
#         strand_length = 50
        
#         for strand in range(num_strands):
#             points = []
#             for i in range(strand_length):
#                 point = {
#                     'base_y': i * 20,
#                     'phase': (i * math.pi / 10) + (strand * math.pi),
#                     'nucleotide': random.choice(['A', 'T', 'G', 'C']),
#                     'color': self.get_quantum_color(random.random())
#                 }
#                 points.append(point)
#             self.dna_strands.append(points)

#     def init_dimensional_tears(self):
#         for _ in range(3):
#             start = QPoint(random.randint(0, self.width()),
#                          random.randint(0, self.height()))
            
#             tear = {
#                 'start': start,
#                 'points': [start],
#                 'growth_direction': QPointF(random.uniform(-1, 1),
#                                          random.uniform(-1, 1)),
#                 'length': random.randint(100, 300),
#                 'width': random.uniform(5, 15),
#                 'reality_fragments': [],
#                 'color': self.get_quantum_color(random.random())
#             }
            
#             # Generate tear path
#             current = QPointF(start)
#             for _ in range(10):
#                 angle = math.atan2(tear['growth_direction'].y(),
#                                  tear['growth_direction'].x())
#                 angle += random.uniform(-0.5, 0.5)
#                 length = random.uniform(20, 40)
#                 dx = math.cos(angle) * length
#                 dy = math.sin(angle) * length
#                 current += QPointF(dx, dy)
#                 tear['points'].append(QPoint(int(current.x()), int(current.y())))
            
#             # Add reality fragments
#             for _ in range(20):
#                 fragment = {
#                     'pos': QPointF(random.uniform(-50, 50),
#                                  random.uniform(-50, 50)),
#                     'rotation': random.uniform(0, 2 * math.pi),
#                     'size': random.uniform(5, 15)
#                 }
#                 tear['reality_fragments'].append(fragment)
            
#             self.tears.append(tear)

#     def get_quantum_color(self, value):
#         # Generate quantum-inspired colors
#         hue = (math.sin(value * math.pi) + 1) / 2
#         sat = 0.8 + math.sin(value * 4 * math.pi) * 0.2
#         val = 0.8 + math.sin(value * 8 * math.pi) * 0.2
#         rgb = colorsys.hsv_to_rgb(hue, sat, val)
#         return QColor(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

#     def update_energy_field(self):
#         # Update node positions
#         for node in self.energy_nodes:
#             # Update position
#             node['pos'] += node['velocity']
            
#             # Bounce off edges
#             if node['pos'].x() < 0 or node['pos'].x() > self.width():
#                 node['velocity'].setX(-node['velocity'].x())
#             if node['pos'].y() < 0 or node['pos'].y() > self.height():
#                 node['velocity'].setY(-node['velocity'].y())
            
#             # Reset connections
#             node['connections'].clear()

#         # Update connections
#         self.energy_connections.clear()
#         for i, node1 in enumerate(self.energy_nodes):
#             for j, node2 in enumerate(self.energy_nodes[i+1:], i+1):
#                 distance = QPointF.dotProduct(
#                     node1['pos'] - node2['pos'],
#                     node1['pos'] - node2['pos']
#                 ) ** 0.5
                
#                 if distance < 200:
#                     strength = 1 - (distance / 200)
#                     if node1['charge'] == node2['charge']:
#                         strength *= 0.5
                    
#                     if strength > 0.2:
#                         self.energy_connections.append({
#                             'node1': node1,
#                             'node2': node2,
#                             'strength': strength
#                         })
#                         node1['connections'].add(j)
#                         node2['connections'].add(i)

#     def update_quantum_particles(self):
#         for particle in self.quantum_particles:
#             # Update wave phase
#             particle['wave_phase'] += particle['frequency']
            
#             # Update position based on quantum uncertainty
#             dx = random.gauss(0, particle['uncertainty'])
#             dy = random.gauss(0, particle['uncertainty'])
#             particle['pos'] += QPointF(dx, dy)
            
#             # Keep particles within bounds
#             particle['pos'].setX(max(0, min(self.width(), particle['pos'].x())))
#             particle['pos'].setY(max(0, min(self.height(), particle['pos'].y())))
            
#             # Entanglement effects
#             if particle['entangled_partner']:
#                 # Correlate some properties between entangled particles
#                 particle['wave_phase'] = -particle['entangled_partner']['wave_phase']

#     def update_void_portals(self):
#         for portal in self.void_portals:
#             portal['rotation'] += portal['spin_speed']
            
#             for particle in portal['particles']:
#                 particle['angle'] += particle['speed']
                
#                 # Spiral particles toward center
#                 if particle['distance'] > 5:
#                     particle['distance'] *= 0.99
#                 else:
#                     # Reset particle to edge when it reaches center
#                     particle['distance'] = portal['radius']
#                     particle['angle'] = random.uniform(0, 2 * math.pi)

#     def draw_time_ripples(self, painter):
#             for ripple in self.time_ripples:
#                 # Create ripple gradient
#                 gradient = QRadialGradient(ripple['center'], ripple['radius'])
#                 # Convert alpha to integer
#                 alpha = int(ripple['alpha'])
#                 ripple_color = QColor(0, 255, 255, alpha)
#                 gradient.setColorAt(0, QColor(0, 0, 0, 0))
#                 gradient.setColorAt(ripple['radius'] / ripple['max_radius'], ripple_color)
#                 gradient.setColorAt(1, QColor(0, 0, 0, 0))
                
#                 # Draw ripple
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(gradient)
#                 painter.drawEllipse(ripple['center'], 
#                                 int(ripple['radius']), int(ripple['radius']))
                
#                 # Draw time distortion artifacts
#                 num_artifacts = int(ripple['radius'] / 10)
#                 for _ in range(num_artifacts):
#                     angle = random.uniform(0, 2 * math.pi)
#                     distance = random.uniform(0.8, 1.2) * ripple['radius']
                    
#                     pos = ripple['center'] + QPointF(
#                         math.cos(angle) * distance,
#                         math.sin(angle) * distance
#                     )
                    
#                     artifact_alpha = int(ripple['alpha'] * random.uniform(0.2, 0.8))
#                     artifact_color = QColor(0, 255, 255, artifact_alpha)
#                     painter.setPen(QPen(artifact_color, 2))
                    
#                     # Draw random time artifact symbols
#                     size = int(random.uniform(5, 15))
#                     if random.random() < 0.3:
#                         # Clock symbol
#                         painter.drawEllipse(pos, size, size)
#                         painter.drawLine(pos, pos + QPointF(size * 0.8, 0))
#                     else:
#                         # Abstract time rune
#                         for _ in range(3):
#                             angle = random.uniform(0, 2 * math.pi)
#                             painter.drawLine(
#                                 pos,
#                                 pos + QPointF(math.cos(angle) * size,
#                                             math.sin(angle) * size)
#                             )

#     def add_time_ripple(self, pos):
#         ripple = {
#             'center': pos,
#             'radius': 0,
#             'max_radius': random.uniform(100, 300),
#             'speed': random.uniform(2, 5),
#             'width': random.uniform(20, 40),
#             'alpha': 255
#         }
#         self.time_ripples.append(ripple)

#     def update_time_ripples(self):
#         # Update existing ripples
#         for ripple in self.time_ripples[:]:
#             ripple['radius'] += ripple['speed']
#             # Ensure alpha calculation results in an integer
#             ripple['alpha'] = int(max(0, 255 * (1 - ripple['radius'] / ripple['max_radius'])))
            
#             if ripple['radius'] > ripple['max_radius']:
#                 self.time_ripples.remove(ripple)
        
#         # Randomly add new ripples
#         if random.random() < 0.02:
#             pos = QPointF(random.randint(0, self.width()),
#                         random.randint(0, self.height()))
#             self.add_time_ripple(pos)
            
            
#     def update_dna_helix(self):
#         self.dna_offset += 0.02
        
#         # Update DNA strand positions
#         for strand in self.dna_strands:
#             for point in strand:
#                 point['phase'] += 0.02

#     def update_dimensional_tears(self):
#         for tear in self.tears:
#             # Update reality fragments
#             for fragment in tear['reality_fragments']:
#                 fragment['rotation'] += random.uniform(0.02, 0.05)
                
#                 # Random movement
#                 fragment['pos'] += QPointF(random.uniform(-1, 1),
#                                          random.uniform(-1, 1))
                
#                 # Keep fragments near the tear
#                 if fragment['pos'].manhattanLength() > 100:
#                     fragment['pos'] *= 0.95

#     def draw_energy_field(self, painter):
#         # Draw connections
#         for conn in self.energy_connections:
#             gradient = QLinearGradient(conn['node1']['pos'], conn['node2']['pos'])
            
#             # Create electric color based on charge interaction
#             if conn['node1']['charge'] == conn['node2']['charge']:
#                 color1 = QColor(64, 64, 255, int(255 * conn['strength']))
#                 color2 = QColor(128, 128, 255, 0)
#             else:
#                 color1 = QColor(255, 64, 64, int(255 * conn['strength']))
#                 color2 = QColor(255, 128, 128, 0)
            
#             gradient.setColorAt(0, color1)
#             gradient.setColorAt(1, color2)
            
#             pen = QPen(QBrush(gradient), 2)
#             painter.setPen(pen)
#             painter.drawLine(conn['node1']['pos'], conn['node2']['pos'])
        
#         # Draw nodes
#         for node in self.energy_nodes:
#             # Create glow effect
#             radius = 20
#             gradient = QRadialGradient(node['pos'], radius)
            
#             base_color = QColor(64, 64, 255) if node['charge'] > 0 else QColor(255, 64, 64)
#             glow_color = QColor(base_color)
#             glow_color.setAlpha(int(100 * node['energy']))
            
#             gradient.setColorAt(0, glow_color)
#             gradient.setColorAt(1, QColor(0, 0, 0, 0))
            
#             painter.setPen(Qt.NoPen)
#             painter.setBrush(gradient)
#             painter.drawEllipse(node['pos'], radius, radius)
            
#             # Draw core
#             painter.setBrush(base_color)
#             painter.drawEllipse(node['pos'], 5, 5)

#     def draw_quantum_particles(self, painter):
#         for particle in self.quantum_particles:
#             # Continue from draw_quantum_particles method
#             radius = 10 + math.sin(particle['wave_phase']) * particle['amplitude']
            
#             # Draw quantum probability cloud
#             for i in range(5):
#                 cloud_color = QColor(particle['color'])
#                 cloud_color.setAlpha(50 - i * 10)
                
#                 cloud_radius = radius + i * 10
#                 uncertainty_offset = QPointF(
#                     random.gauss(0, particle['uncertainty']),
#                     random.gauss(0, particle['uncertainty'])
#                 )
                
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(cloud_color)
#                 painter.drawEllipse(particle['pos'] + uncertainty_offset, 
#                                   cloud_radius, cloud_radius)
            
#             # Draw entanglement lines
#             if particle['entangled_partner']:
#                 gradient = QLinearGradient(particle['pos'], 
#                                          particle['entangled_partner']['pos'])
#                 gradient.setColorAt(0, QColor(particle['color']))
#                 gradient.setColorAt(1, QColor(particle['entangled_partner']['color']))
                
#                 pen = QPen(QBrush(gradient), 1)
#                 pen.setStyle(Qt.DashLine)
#                 painter.setPen(pen)
#                 painter.drawLine(particle['pos'], 
#                                particle['entangled_partner']['pos'])

#     def draw_void_portals(self, painter):
#         for portal in self.void_portals:
#             # Draw void background
#             gradient = QRadialGradient(portal['center'], portal['radius'])
#             gradient.setColorAt(0, QColor(0, 0, 0, 200))
#             gradient.setColorAt(0.7, QColor(20, 0, 40, 150))
#             gradient.setColorAt(1, QColor(0, 0, 0, 0))
            
#             painter.setPen(Qt.NoPen)
#             painter.setBrush(gradient)
#             painter.drawEllipse(portal['center'], 
#                               portal['radius'], portal['radius'])
            
#             # Draw portal particles
#             for particle in portal['particles']:
#                 # Calculate particle position
#                 angle = particle['angle'] + portal['rotation']
#                 dist = particle['distance']
#                 spiral_x = math.cos(angle * portal['distortion']) * dist
#                 spiral_y = math.sin(angle * portal['distortion']) * dist
                
#                 pos = portal['center'] + QPointF(spiral_x, spiral_y)
                
#                 # Draw particle with trail
#                 for i in range(3):
#                     trail_angle = angle - i * 0.1
#                     trail_x = math.cos(trail_angle * portal['distortion']) * dist
#                     trail_y = math.sin(trail_angle * portal['distortion']) * dist
#                     trail_pos = portal['center'] + QPointF(trail_x, trail_y)
                    
#                     color = QColor(128 + i * 40, 0, 255 - i * 40, 150 - i * 40)
#                     painter.setBrush(color)
#                     painter.drawEllipse(trail_pos, 
#                                       particle['size'], particle['size'])

#     def draw_reality_fractures(self, painter):
#         for fracture in self.fractures:
#             # Create fracture path
#             path = QPainterPath()
#             path.moveTo(fracture['points'][0])
            
#             for i in range(1, len(fracture['points'])):
#                 path.lineTo(fracture['points'][i])
            
#             # Draw fracture glow
#             for i in range(3):
#                 glow_color = QColor(fracture['color'])
#                 glow_color.setAlpha(int(100 * fracture['glow_intensity'] / (i + 1)))
                
#                 pen = QPen(glow_color, fracture['width'] + i * 4)
#                 pen.setCapStyle(Qt.RoundCap)
#                 painter.setPen(pen)
#                 painter.drawPath(path)
            
#             # Draw distortion effects
#             for i in range(len(fracture['points']) - 1):
#                 p1 = fracture['points'][i]
#                 p2 = fracture['points'][i + 1]
                
#                 # Add random distortion lines
#                 num_lines = int(QPoint(p2 - p1).manhattanLength() / 10)
#                 for _ in range(num_lines):
#                     t = random.random()
#                     mid = p1 + (p2 - p1) * t
                    
#                     offset = QPoint(
#                         random.randint(-20, 20),
#                         random.randint(-20, 20)
#                     )
                    
#                     color = QColor(fracture['color'])
#                     color.setAlpha(random.randint(50, 150))
#                     painter.setPen(QPen(color, 1))
#                     painter.drawLine(mid, mid + offset)

    

#     def draw_dna_helix(self, painter):
#         center_x = self.width() * 0.8
#         base_y = (self.height() - len(self.dna_strands[0]) * 20) / 2
#         amplitude = 100
        
#         for i, strand in enumerate(self.dna_strands):
#             prev_point = None
            
#             for point in strand:
#                 # Calculate helix position
#                 x = center_x + math.cos(point['phase']) * amplitude
#                 y = base_y + point['base_y']
#                 current_point = QPointF(x, y)
                
#                 # Draw strand
#                 if prev_point:
#                     color = QColor(point['color'])
#                     color.setAlpha(150)
#                     painter.setPen(QPen(color, 3))
#                     painter.drawLine(prev_point, current_point)
                
#                 # Draw nucleotide
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(QColor(point['color']))
#                 painter.drawEllipse(current_point, 5, 5)
                
#                 # Draw base pair connections
#                 if i == 0:
#                     pair_x = center_x + math.cos(point['phase'] + math.pi) * amplitude
#                     pair_y = y
#                     pair_point = QPointF(pair_x, pair_y)
                    
#                     # Draw connection with color based on base pair
#                     if point['nucleotide'] in 'AT':
#                         connection_color = QColor(255, 200, 0, 100)
#                     else:  # GC pair
#                         connection_color = QColor(0, 200, 255, 100)
                    
#                     painter.setPen(QPen(connection_color, 2))
#                     painter.drawLine(current_point, pair_point)
                
#                 prev_point = current_point

#     def draw_dimensional_tears(self, painter):
#         for tear in self.tears:
#             # Create tear path
#             path = QPainterPath()
#             path.moveTo(tear['points'][0])
            
#             for point in tear['points'][1:]:
#                 path.lineTo(point)
            
#             # Draw tear glow
#             for i in range(4):
#                 glow_color = QColor(tear['color'])
#                 glow_color.setAlpha(150 - i * 30)
                
#                 pen = QPen(glow_color, tear['width'] + i * 4)
#                 pen.setCapStyle(Qt.RoundCap)
#                 painter.setPen(pen)
#                 painter.drawPath(path)
            
#             # Draw reality fragments
#             for fragment in tear['reality_fragments']:
#                 painter.save()
                
#                 # Transform for rotation
#                 painter.translate(
#                     tear['points'][0] + fragment['pos']
#                 )
#                 painter.rotate(math.degrees(fragment['rotation']))
                
#                 # Draw fragment
#                 fragment_color = QColor(tear['color'])
#                 fragment_color.setAlpha(100)
#                 painter.setPen(QPen(fragment_color, 2))
#                 painter.setBrush(Qt.NoBrush)
                
#                 # Random fragment shapes
#                 size = int(fragment['size'])  # Convert to integer
#                 if random.random() < 0.5:
#                     # Draw rectangle with integer coordinates
#                     painter.drawRect(-size//2, -size//2, size, size)
#                 else:
#                     # For ellipse we can use float values
#                     painter.drawEllipse(QPointF(0, 0), 
#                                       fragment['size']/2, 
#                                       fragment['size']/2)
                
#                 painter.restore()

#     def update_effect(self):
#         self.effect_time += 1
#         self.phase += 0.02
        
#         # Update all effect components
#         self.update_energy_field()
#         self.update_quantum_particles()
#         self.update_void_portals()
#         self.update_time_ripples()
#         self.update_dna_helix()
#         self.update_dimensional_tears()
        
#         # Add random time ripples
#         if random.random() < 0.02:
#             pos = QPointF(random.randint(0, self.width()),
#                          random.randint(0, self.height()))
#             self.add_time_ripple(pos)
        
#         self.update()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
        
#         # Draw all effects in order
#         self.draw_void_portals(painter)
#         self.draw_dimensional_tears(painter)
#         self.draw_energy_field(painter)
#         self.draw_quantum_particles(painter)
#         self.draw_reality_fractures(painter)
#         self.draw_time_ripples(painter)
#         self.draw_dna_helix(painter)

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             self.close()

# def main():
#     app = QApplication(sys.argv)
#     effect = RealityDistortionEffect()
#     effect.show()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


# exit()
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QTimer, QPoint, QRect, QPropertyAnimation, QEasingCurve
# from PyQt5.QtGui import QPixmap, QPainter, QColor, QTransform, QFont, QPainterPath, QLinearGradient, QRadialGradient
# import sys
# import random
# import math
# import colorsys

# class ScreenEffects(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.setAttribute(Qt.WA_TransparentForMouseEvents)
        
#         screen = QApplication.primaryScreen()
#         self.screen_geometry = screen.geometry()
#         self.setGeometry(self.screen_geometry)
        
#         self.effect_time = 0
#         self.current_effect = None
#         self.particles = []
#         self.entities = []
#         self.plasma_offset = 0
#         self.vortex_angle = 0
        
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_effect)
#         self.timer.start(16)

#     def start_effect(self, effect_name):
#         self.current_effect = effect_name
#         self.effect_time = 0
        
#         if effect_name == "vortex":
#             self.init_vortex()
#         elif effect_name == "energy":
#             self.init_energy_field()
#         elif effect_name == "psychedelic":
#             self.init_psychedelic()
#         elif effect_name == "cyber":
#             self.init_cyber()
#         elif effect_name == "quantum":
#             self.init_quantum()
#         elif effect_name == "cosmic":
#             self.init_cosmic()

#     def init_vortex(self):
#         self.vortex_particles = []
#         for _ in range(1000):
#             angle = random.uniform(0, 2 * math.pi)
#             radius = random.uniform(100, max(self.width(), self.height()))
#             self.vortex_particles.append({
#                 'angle': angle,
#                 'radius': radius,
#                 'speed': random.uniform(0.01, 0.03),
#                 'size': random.uniform(2, 6),
#                 'color': self.get_rainbow_color(random.random())
#             })

#     def init_cosmic(self):
#         self.stars = []
#         self.nebulas = []
#         # Create stars
#         for _ in range(500):
#             self.stars.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'size': random.uniform(0.5, 3),
#                 'twinkle_speed': random.uniform(0.02, 0.1)
#             })
#         # Create nebula clouds
#         for _ in range(5):
#             self.nebulas.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'size': random.randint(200, 400),
#                 'color': self.get_rainbow_color(random.random()),
#                 'alpha': random.uniform(0.1, 0.3)
#             })

#     def init_quantum(self):
#         self.quantum_particles = []
#         self.quantum_fields = []
#         # Quantum particles
#         for _ in range(50):
#             self.quantum_particles.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'phase': random.uniform(0, 2 * math.pi),
#                 'frequency': random.uniform(0.02, 0.1),
#                 'amplitude': random.uniform(20, 50),
#                 'color': self.get_rainbow_color(random.random())
#             })
#         # Quantum fields
#         for _ in range(3):
#             self.quantum_fields.append({
#                 'offset': random.uniform(0, 2 * math.pi),
#                 'speed': random.uniform(0.01, 0.03),
#                 'wavelength': random.uniform(100, 300)
#             })

#     def get_rainbow_color(self, pos):
#         hue = pos % 1.0
#         rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
#         return QColor(int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))

#     def vortex_effect(self, painter):
#         center_x = self.width() // 2
#         center_y = self.height() // 2
        
#         # Update and draw particles
#         for particle in self.vortex_particles:
#             # Update position
#             particle['angle'] += particle['speed']
#             particle['radius'] -= 0.5
            
#             # Reset particles that reach center
#             if particle['radius'] < 10:
#                 particle['radius'] = max(self.width(), self.height())
#                 particle['angle'] = random.uniform(0, 2 * math.pi)
            
#             # Calculate position
#             x = center_x + math.cos(particle['angle']) * particle['radius']
#             y = center_y + math.sin(particle['angle']) * particle['radius']
            
#             # Draw particle with trail
#             painter.setPen(Qt.NoPen)
#             color = particle['color']
#             for i in range(3):
#                 trail_x = center_x + math.cos(particle['angle'] - i * 0.1) * (particle['radius'] + i * 10)
#                 trail_y = center_y + math.sin(particle['angle'] - i * 0.1) * (particle['radius'] + i * 10)
#                 color.setAlpha(150 - i * 40)
#                 painter.setBrush(color)
#                 painter.drawEllipse(QPoint(int(trail_x), int(trail_y)), 
#                                   int(particle['size']), int(particle['size']))

#     def cosmic_effect(self, painter):
#         # Draw background stars
#         for star in self.stars:
#             twinkle = math.sin(self.effect_time * star['twinkle_speed']) * 0.5 + 0.5
#             color = QColor(255, 255, 255, int(twinkle * 255))
#             painter.setPen(color)
#             painter.setBrush(color)
#             painter.drawEllipse(QPoint(int(star['x']), int(star['y'])), 
#                               int(star['size']), int(star['size']))
        
#         # Draw nebulas with gradient
#         for nebula in self.nebulas:
#             gradient = QRadialGradient(nebula['x'], nebula['y'], nebula['size'])
#             color = nebula['color']
#             color.setAlpha(int(255 * nebula['alpha']))
#             gradient.setColorAt(0, color)
#             color.setAlpha(0)
#             gradient.setColorAt(1, color)
            
#             painter.setPen(Qt.NoPen)
#             painter.setBrush(gradient)
#             painter.drawEllipse(QPoint(int(nebula['x']), int(nebula['y'])), 
#                               nebula['size'], nebula['size'])

#     def quantum_effect(self, painter):
#         # Draw quantum fields
#         for field in self.quantum_fields:
#             path = QPainterPath()
#             path.moveTo(0, self.height() / 2)
            
#             for x in range(0, self.width(), 2):
#                 y = self.height() / 2 + math.sin(x / field['wavelength'] + field['offset']) * 100
#                 path.lineTo(x, y)
            
#             field['offset'] += field['speed']
            
#             pen = painter.pen()
#             pen.setWidth(2)
#             pen.setColor(QColor(0, 255, 255, 50))
#             painter.setPen(pen)
#             painter.drawPath(path)
        
#         # Draw quantum particles with probability clouds
#         for particle in self.quantum_particles:
#             # Update quantum state
#             particle['phase'] += particle['frequency']
            
#             # Calculate probability cloud
#             for i in range(10):
#                 angle = i * math.pi / 5
#                 distance = particle['amplitude'] * math.sin(particle['phase'])
#                 x = particle['x'] + math.cos(angle) * distance
#                 y = particle['y'] + math.sin(angle) * distance
                
#                 color = particle['color']
#                 color.setAlpha(50)
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(color)
#                 painter.drawEllipse(QPoint(int(x), int(y)), 5, 5)

#     def psychedelic_effect(self, painter):
#         for x in range(0, self.width(), 20):
#             for y in range(0, self.height(), 20):
#                 value = math.sin(x * 0.01 + self.effect_time * 0.1) + \
#                        math.cos(y * 0.01 + self.effect_time * 0.1)
#                 color = self.get_rainbow_color((value + 2) / 4)
#                 color.setAlpha(100)
#                 painter.setPen(Qt.NoPen)
#                 painter.setBrush(color)
#                 painter.drawRect(x, y, 20, 20)

#     def update_effect(self):
#         self.effect_time += 1
#         self.update()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
        
#         if self.current_effect == "vortex":
#             self.vortex_effect(painter)
#         elif self.current_effect == "cosmic":
#             self.cosmic_effect(painter)
#         elif self.current_effect == "quantum":
#             self.quantum_effect(painter)
#         elif self.current_effect == "psychedelic":
#             self.psychedelic_effect(painter)

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             self.close()

# class EffectController(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
        
#     def init_ui(self):
#         layout = QVBoxLayout()
#         effects = ["vortex", "cosmic", "quantum", "psychedelic"]
#         self.screen_effect = ScreenEffects()
        
#         for effect in effects:
#             btn = QPushButton(effect.title())
#             btn.clicked.connect(lambda checked, e=effect: self.screen_effect.start_effect(e))
#             layout.addWidget(btn)
            
#         self.setLayout(layout)
#         self.setWindowTitle('Crazy Effects')
#         self.show()
#         self.screen_effect.show()

# def main():
#     app = QApplication(sys.argv)
#     controller = EffectController()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()



# exit()
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
# from PyQt5.QtGui import QPixmap, QPainter, QColor, QTransform, QFont
# import sys
# import random
# import math

# class ScreenEffects(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.setAttribute(Qt.WA_TransparentForMouseEvents)  # Let mouse events pass through
        
#         screen = QApplication.primaryScreen()
#         self.screen_geometry = screen.geometry()
#         self.setGeometry(self.screen_geometry)
        
#         # Initialize effect parameters
#         self.matrix_chars = []
#         self.particles = []
#         self.effect_time = 0
#         self.current_effect = None
        
#         # Setup animation timer
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_effect)
#         self.timer.start(16)  # ~60 FPS

#     def start_effect(self, effect_name):
#         self.current_effect = effect_name
#         self.effect_time = 0
        
#         if effect_name == "matrix":
#             self.init_matrix()
#         elif effect_name == "particles":
#             self.init_particles()
#         elif effect_name == "lightning":
#             self.init_lightning()
#         elif effect_name == "binary":
#             self.init_binary()

#     def init_matrix(self):
#         self.matrix_chars = []
#         columns = self.width() // 20  # character width
        
#         for x in range(columns):
#             self.matrix_chars.append({
#                 'x': x * 20,
#                 'y': random.randint(-500, 0),
#                 'speed': random.uniform(3, 7),
#                 'length': random.randint(5, 15),
#                 'chars': [chr(random.randint(0x30A0, 0x30FF)) for _ in range(20)]
#             })

#     def init_particles(self):
#         self.particles = []
#         for _ in range(100):
#             self.particles.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'dx': random.uniform(-2, 2),
#                 'dy': random.uniform(-2, 2),
#                 'size': random.randint(2, 6),
#                 'color': QColor(random.randint(100, 255), 
#                               random.randint(100, 255), 
#                               random.randint(100, 255), 
#                               150)
#             })

#     def init_binary(self):
#         self.binary_streams = []
#         columns = self.width() // 15
#         for x in range(columns):
#             self.binary_streams.append({
#                 'x': x * 15,
#                 'y': random.randint(-500, 0),
#                 'speed': random.uniform(2, 5),
#                 'length': random.randint(10, 30),
#                 'color': QColor(0, 255, 0, 150)
#             })

#     def init_lightning(self):
#         self.lightning_points = []
#         start_x = random.randint(0, self.width())
#         current_x = start_x
#         current_y = 0
        
#         while current_y < self.height():
#             next_y = current_y + random.randint(20, 50)
#             next_x = current_x + random.randint(-50, 50)
#             self.lightning_points.append((current_x, current_y))
#             current_x, current_y = next_x, next_y

#     def matrix_effect(self, painter):
#         painter.setFont(QFont('Courier New', 14))
        
#         for stream in self.matrix_chars:
#             # Update position
#             stream['y'] += stream['speed']
#             if stream['y'] > self.height() + 500:
#                 stream['y'] = random.randint(-500, 0)
                
#             # Draw characters with fading effect
#             for i in range(stream['length']):
#                 y_pos = int(stream['y']) - (i * 20)
#                 if 0 <= y_pos <= self.height():
#                     # Lead character is brighter
#                     if i == 0:
#                         painter.setPen(QColor(255, 255, 255, 200))
#                     else:
#                         alpha = 200 - (i * 15)
#                         painter.setPen(QColor(0, 255, 0, max(0, alpha)))
                    
#                     # Randomly change characters
#                     if random.random() < 0.1:
#                         stream['chars'][i] = chr(random.randint(0x30A0, 0x30FF))
                    
#                     painter.drawText(stream['x'], y_pos, stream['chars'][i])

#     def particles_effect(self, painter):
#         for particle in self.particles:
#             # Update position
#             particle['x'] += particle['dx']
#             particle['y'] += particle['dy']
            
#             # Bounce off edges
#             if particle['x'] < 0 or particle['x'] > self.width():
#                 particle['dx'] *= -1
#             if particle['y'] < 0 or particle['y'] > self.height():
#                 particle['dy'] *= -1
            
#             # Draw particle
#             painter.setPen(Qt.NoPen)
#             painter.setBrush(particle['color'])
#             painter.drawEllipse(int(particle['x']), int(particle['y']), 
#                               particle['size'], particle['size'])

#     def binary_effect(self, painter):
#         painter.setFont(QFont('Courier New', 12))
        
#         for stream in self.binary_streams:
#             stream['y'] += stream['speed']
#             if stream['y'] > self.height() + 200:
#                 stream['y'] = random.randint(-500, 0)
            
#             for i in range(stream['length']):
#                 y_pos = int(stream['y']) - (i * 15)
#                 if 0 <= y_pos <= self.height():
#                     # Randomly choose 0 or 1
#                     binary_char = str(random.randint(0, 1))
#                     alpha = 200 - (i * 8)
#                     painter.setPen(QColor(0, 255, 0, max(0, alpha)))
#                     painter.drawText(stream['x'], y_pos, binary_char)

#     def lightning_effect(self, painter):
#         if not hasattr(self, 'lightning_alpha'):
#             self.lightning_alpha = 255
        
#         # Draw lightning
#         pen = painter.pen()
#         pen.setColor(QColor(255, 255, 255, self.lightning_alpha))
#         pen.setWidth(2)
#         painter.setPen(pen)
        
#         for i in range(len(self.lightning_points) - 1):
#             painter.drawLine(self.lightning_points[i][0], self.lightning_points[i][1],
#                            self.lightning_points[i + 1][0], self.lightning_points[i + 1][1])
        
#         # Fade out
#         self.lightning_alpha -= 15
#         if self.lightning_alpha <= 0:
#             self.init_lightning()
#             self.lightning_alpha = 255

#     def update_effect(self):
#         self.effect_time += 1
#         self.update()

#     def paintEvent(self, event):
#         painter = QPainter(self)
        
#         if self.current_effect == "matrix":
#             self.matrix_effect(painter)
#         elif self.current_effect == "particles":
#             self.particles_effect(painter)
#         elif self.current_effect == "lightning":
#             self.lightning_effect(painter)
#         elif self.current_effect == "binary":
#             self.binary_effect(painter)

#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             self.close()

# class EffectController(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
        
#     def init_ui(self):
#         layout = QVBoxLayout()
#         effects = ["matrix", "particles", "lightning", "binary"]
#         self.screen_effect = ScreenEffects()
        
#         for effect in effects:
#             btn = QPushButton(effect.title())
#             btn.clicked.connect(lambda checked, e=effect: self.screen_effect.start_effect(e))
#             layout.addWidget(btn)
            
#         self.setLayout(layout)
#         self.setWindowTitle('Screen Effects')
#         self.show()
#         self.screen_effect.show()

# def main():
#     app = QApplication(sys.argv)
#     controller = EffectController()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


# exit()
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
# from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
# from PyQt5.QtGui import QPixmap, QImage, QPainter, QColor, QTransform, QRadialGradient
# import sys
# import random
# import math

# class ScreenEffects(QWidget):
#     def __init__(self):
#         super().__init__()
#         # Make window frameless and always on top
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
        
#         # Get screen geometry
#         screen = QApplication.primaryScreen()
#         self.screen_geometry = screen.geometry()
#         self.setGeometry(self.screen_geometry)
        
#         # Capture initial screen
#         self.original_pixmap = screen.grabWindow(0)
#         self.current_pixmap = self.original_pixmap.copy()
        
#         # Initialize effect parameters
#         self.effect_time = 0
#         self.wave_offset = 0
#         self.glitch_lines = []
#         self.shatter_pieces = []
#         self.current_effect = None
        
#         # Setup animation timer
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_effect)
#         self.timer.start(16)  # ~60 FPS
        
#     def start_effect(self, effect_name):
#         self.current_effect = effect_name
#         self.effect_time = 0
#         self.current_pixmap = self.original_pixmap.copy()
        
#         if effect_name == "shatter":
#             self.init_shatter()
#         elif effect_name == "glitch":
#             self.init_glitch()
            
#     def init_shatter(self):
#         # Create shatter pieces
#         piece_size = 50
#         self.shatter_pieces = []
        
#         for y in range(0, self.height(), piece_size):
#             for x in range(0, self.width(), piece_size):
#                 piece = {
#                     'rect': QRect(x, y, piece_size, piece_size),
#                     'velocity': QPoint(random.randint(-5, 5), random.randint(-5, 5)),
#                     'rotation': random.uniform(-5, 5),
#                     'scale': 1.0
#                 }
#                 self.shatter_pieces.append(piece)

#     def init_glitch(self):
#         # Create random glitch lines
#         self.glitch_lines = []
#         for _ in range(20):
#             y = random.randint(0, self.height())
#             height = random.randint(5, 30)
#             offset = random.randint(-50, 50)
#             self.glitch_lines.append({'y': y, 'height': height, 'offset': offset})
 

#     def shatter_effect(self):
#         new_pixmap = QPixmap(self.size())
#         new_pixmap.fill(Qt.transparent)
#         painter = QPainter(new_pixmap)
        
#         # Update and draw shatter pieces
#         for piece in self.shatter_pieces:
#             # Update position
#             piece['rect'].translate(piece['velocity'].x(), piece['velocity'].y())
#             piece['velocity'] = QPoint(piece['velocity'].x(), piece['velocity'].y() + 1)  # gravity
#             piece['rotation'] += piece['rotation'] * 0.01
#             piece['scale'] *= 0.995
            
#             # Draw piece
#             transform = QTransform()
#             transform.translate(piece['rect'].center().x(), piece['rect'].center().y())
#             transform.rotate(piece['rotation'])
#             transform.scale(piece['scale'], piece['scale'])
#             transform.translate(-piece['rect'].center().x(), -piece['rect'].center().y())
            
#             painter.setTransform(transform)
#             painter.drawPixmap(piece['rect'], self.original_pixmap, piece['rect'])
            
#         painter.end()
#         return new_pixmap
 

#     def matrix_effect(self):
#         new_pixmap = QPixmap(self.size())
#         new_pixmap.fill(Qt.transparent)
#         painter = QPainter(new_pixmap)
        
#         # Create matrix rain effect
#         char_size = 20
#         columns = self.width() // char_size
        
#         for x in range(columns):
#             y = (self.effect_time + x * 50) % self.height()
#             color = QColor(0, 255, 0, 150)
#             painter.setPen(color)
            
#             # Draw random matrix characters
#             for i in range(10):
#                 char_y = (y + i * char_size) % self.height()
#                 char = chr(random.randint(0x30A0, 0x30FF))  # Japanese characters
#                 painter.drawText(x * char_size, char_y, char)
                
#         painter.end()
#         return new_pixmap

#     def update_effect(self):
 
#         if self.current_effect == "shatter":
#             self.current_pixmap = self.shatter_effect()
 
#         elif self.current_effect == "matrix":
#             self.current_pixmap = self.matrix_effect()
            
#         self.effect_time += 1
#         self.update()
        
#     def paintEvent(self, event):
#         if self.current_pixmap:
#             painter = QPainter(self)
#             painter.drawPixmap(0, 0, self.current_pixmap)
            
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             self.close()

# class EffectController(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
        
#     def init_ui(self):
#         layout = QVBoxLayout()
        
#         # Create effect buttons
#         effects = ["shatter", "matrix"]
#         self.screen_effect = ScreenEffects()
        
#         for effect in effects:
#             btn = QPushButton(effect.title())
#             btn.clicked.connect(lambda checked, e=effect: self.screen_effect.start_effect(e))
#             layout.addWidget(btn)  # Changed from addButton to addWidget
            
#         self.setLayout(layout)
#         self.setWindowTitle('Screen Effects Controller')
#         self.show()
#         self.screen_effect.show()

# def main():
#     app = QApplication(sys.argv)
#     controller = EffectController()
#     sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()
    


# # from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# # from PyQt5.QtCore import Qt, QTimer
# # from PyQt5.QtGui import QPixmap, QImage, QPainter, QScreen
# # import sys
# # import random

# # class MeltEffect(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         # Make window frameless and always on top
# #         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
# #         self.setAttribute(Qt.WA_TranslucentBackground)
        
# #         # Get primary screen geometry
# #         screen = QApplication.primaryScreen()
# #         self.screen_geometry = screen.geometry()
# #         self.setGeometry(self.screen_geometry)
        
# #         # Capture initial screen
# #         self.original_pixmap = screen.grabWindow(0)
# #         self.current_pixmap = self.original_pixmap.copy()
        
# #         # Initialize melt parameters
# #         self.melt_positions = [0] * self.height()
# #         self.melt_speeds = [random.uniform(0.5, 2.0) for _ in range(self.height())]
        
# #         # Setup animation timer
# #         self.timer = QTimer(self)
# #         self.timer.timeout.connect(self.update_melt)
# #         self.timer.start(16)  # ~60 FPS
        
# #     def update_melt(self):
# #         # Create a painter for the current pixmap
# #         new_pixmap = QPixmap(self.size())
# #         new_pixmap.fill(Qt.transparent)
# #         painter = QPainter(new_pixmap)
        
# #         # Update melt positions and draw
# #         for y in range(self.height()):
# #             self.melt_positions[y] += self.melt_speeds[y]
            
# #             # Calculate stretching and displacement
# #             stretch = random.uniform(1.0, 1.02)
# #             displacement = int(self.melt_positions[y])
            
# #             # Source rectangle
# #             src_rect = self.original_pixmap.copy(0, y, self.width(), 1)
            
# #             # Draw with stretching effect
# #             painter.drawPixmap(
# #                 0, y + displacement,
# #                 self.width(), max(1, int(stretch)),
# #                 src_rect
# #             )
            
# #             # Add some random drips
# #             if random.random() < 0.001:
# #                 drip_height = random.randint(10, 30)
# #                 painter.drawPixmap(
# #                     0, y + displacement,
# #                     self.width(), drip_height,
# #                     src_rect
# #                 )
        
# #         painter.end()
# #         self.current_pixmap = new_pixmap
# #         self.update()
        
# #     def paintEvent(self, event):
# #         painter = QPainter(self)
# #         painter.drawPixmap(0, 0, self.current_pixmap)
        
# #     def keyPressEvent(self, event):
# #         if event.key() == Qt.Key_Escape:
# #             self.close()

# # def main():
# #     app = QApplication(sys.argv)
# #     effect = MeltEffect()
# #     effect.show()
# #     sys.exit(app.exec_())

# # if __name__ == '__main__':
# #     main()


# exit()
# import keyboard
# import pynput

# import random
# import time
# import threading
# import pyautogui
# import string
# import win32gui
# import win32con
# pynput_keyboard = pynput.keyboard
# import random
# import time
# import threading
# import pyautogui
# import string
# import win32gui
# import win32con
# import ctypes
# import math
# from pynput import keyboard as pynput_keyboard

# def intermittent_internet():
#     while True:
#         time.sleep(random.randint(2, 5))  # Yes it's going to be often and trigger the dumbass no internet but i'll disable it.
#         print("Dropping internet...")
#         os.system("ipconfig /release")  # Releases the IP address # it fucking actually disables the internet..
#         time.sleep(3)  # Brief disconnect
#         os.system("ipconfig /renew")  # Renews the IP address
#         print("Internet restored.")


# import screen_brightness_control as sbc
# import time
# import random
# from PIL import Image, ImageEnhance

# import screen_brightness_control as sbc
# import time
# import random

# def set_screen_brightness(target_brightness):
#     """Sets the screen brightness to a specific value."""
#     sbc.set_brightness(target_brightness)


# def subtly_mess_with_text():
#     """occasionally swaps letters or inserts random characters."""

#     def on_press(key):
#         """callback for key presses."""
#         print(f"Key pressed: {key}")  # debug print

#         try:
#             char = key.char
#             print(f"Character: {char}")  # debug print

#             if char.isalnum() and random.random() < 0.1: # glitch condition
#                 glitch_char = random.choice([
#                     lambda c: list(c)[0],  # same char
#                     lambda c: "".join(random.sample(list(c), len(c))),  # swaps chars
#                     lambda c: c + random.choice(string.printable) # adds a char
#                 ])(char)

#                 print(f"Glitching: {char} -> {glitch_char}") # debug print
#                 write_text_delayed(glitch_char)
#                 return True # block the key

#         except AttributeError:
#             print("Special key pressed")  # debug print
#             pass  # ignore special keys
#         return True  # process key normally


#     def write_text_delayed(text):
#         time.sleep(0.001)  # small delay
#         keyboard.write(text)

#     with pynput_keyboard.Listener(on_press=on_press) as listener:
#         listener.join()


# def subtly_mess_with_mouse():
#     """Messes with mouse speed using delta calculations, applying speed changes
#     for a duration of 10 seconds."""
#     prev_x, prev_y = pyautogui.position()
#     speed_change_duration = 10  # Seconds
#     speed_change_timer = time.time()
#     speed_change_active = False
#     speed_change_type = None  # "faster" or "slower"

#     while True:
#         time.sleep(0.05)  # Check every 0.1 seconds
#         current_x, current_y = pyautogui.position()
#         dx = current_x - prev_x
#         dy = current_y - prev_y
#         if dx != 0 or dy != 0:  # Only mess if mouse moved
#             if (not speed_change_active and
#                 random.random() < 0.1):  # 20% chance of messing
#                 speed_change_active = True
#                 speed_change_timer = time.time()
#                 speed_change_type = "faster" if random.random() < 0.5 else "slower"
#             if not speed_change_active and random.random() < 0.05:  # 5% chance of random teleport of screen resolution
#                    pyautogui.moveTo(random.randint(0, pyautogui.size()[0]), random.randint(0, pyautogui.size()[1]), duration=0)  # Instant tp
#                    print('Teleport')
#                    continue  # Skip the rest of the loop for this iteration
#             print(random.random())
#             if not speed_change_active:
#                 print('Sleeping for 5 seconds')
#                 time.sleep(5)

#             if speed_change_active:
#                 if time.time() - speed_change_timer > speed_change_duration:
#                     speed_change_active = False
#                     speed_change_type = None
#                 else:
#                     if speed_change_type == "faster":
#                         print('fast')
#                         dx = dx * random.randint(1, 100) / 30
#                         dy = dy * random.randint(1, 100) / 30
#                     elif speed_change_type == "slower":
#                         print("slower")
#                         dx = -dx / 1.05
#                         dy = -dy / 1.05

#             try:
#                 pyautogui.move(dx, dy, duration=0)
#             except Exception as e:
#                 print(e)
#             prev_x, prev_y = pyautogui.position()
#         else:
#             prev_x, prev_y = pyautogui.position()




# import tkinter as tk
# from tkinter import messagebox

# def create_phantom_notification():
#     """creates a fake notification that disappears quickly."""
#     # this requires a GUI library, example w/ tkinter:
#     root = tk.Tk()
#     root.withdraw()  # hide the main window
#     messagebox.showinfo("System Update", "A new update is available!")
#     root.after(500, root.destroy) # disappears after 0.5 seconds


# def trigger_phantom_notification():
#     """periodically triggers phantom notifications."""
#     while True:
#         time.sleep(random.randint(300, 600))
#         if random.random() < 0.2:  # 20% chance of a notification
#             create_phantom_notification()

# def subtly_mess_with_windows():
#     """makes windows briefly minimize/maximize randomly."""
#     while True:
#         # print('did')
#         window = win32gui.GetForegroundWindow()
#         if window and random.random() < 0.05: # 5% chance of minimizing or maximizing
#             print('Windows messing triggered')
#             current_state = win32gui.GetWindowPlacement(window)[1]  # 1 is the minimization status
#             try:
#                     if current_state == win32con.SW_SHOWMINIMIZED:  # if minimized
#                         win32gui.ShowWindow(window, win32con.SW_RESTORE)  # restore to original
#                         time.sleep(0.2)  # wait a bit
#                         win32gui.ShowWindow(window, win32con.SW_SHOWMINIMIZED)  # minimize back
#                         win32gui.ShowWindow(window, win32con.SW_RESTORE)  # restore to original state

#                     elif current_state == win32con.SW_SHOWMAXIMIZED:  # if maximized
#                         win32gui.ShowWindow(window, win32con.SW_SHOWMINIMIZED)  # minimize
#                         time.sleep(0.2)  # wait a bit
#                         win32gui.ShowWindow(window, win32con.SW_RESTORE)  # restore to original state

#                     elif current_state == win32con.SW_SHOWNORMAL:  # if normal
#                         win32gui.ShowWindow(window, win32con.SW_SHOWMINIMIZED)  # minimize
#                         time.sleep(0.2)  # wait a bit
#                         win32gui.ShowWindow(window, win32con.SW_SHOWMAXIMIZED)  # maximize
#                         time.sleep(0.2)  # wait a bit
#                         win32gui.ShowWindow(window, win32con.SW_SHOWNORMAL)  # restore to original state

#                     else:
#                         pass
#                         # print(f'Unsupported state: {current_state}')
#             except Exception as e:
#                    print(f"Messing with Windows Errored: {e}")
#         time.sleep(5)  # wait a random amount of time


# subtly_mess_with_windows()

# exit()

# import threading
# import socket
# from scapy.all import *

# def scan_port(ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.settimeout(0.1)  # Adjust timeout as needed
#     result = sock.connect_ex((ip, port))
#     if result == 0:
#         print(f"Port {port} is open on {ip}")
#     sock.close()

# def scan_subnet(subnet, port):
#     threads = []
#     for i in range(256):
#         for j in range(256):
#             ip = f"{subnet}.{i}.{j}"
#             thread = threading.Thread(target=scan_port, args=(ip, port))
#             threads.append(thread)
#             thread.start()

#     for thread in threads:
#         thread.join()


# if __name__ == "__main__":
#     import time
#     starttime = time.time()
#     scan_subnet("192.168", 45433)
#     print(f'Total: {time.time() - starttime}')
# exit()
# import ctypes
# import random
# import time

# def fake_bsod(duration=5):
#     """Simulates a BSOD (Blue Screen of Death) for a specified duration."""
#     user32 = ctypes.windll.user32
#     gdi32 = ctypes.windll.gdi32

#     class LOGFONTA(ctypes.Structure):
#         _fields_ = [
#             ("lfHeight", ctypes.c_long),
#             ("lfWidth", ctypes.c_long),
#             ("lfEscapement", ctypes.c_long),
#             ("lfOrientation", ctypes.c_long),
#             ("lfWeight", ctypes.c_long),
#             ("lfItalic", ctypes.c_byte),
#             ("lfUnderline", ctypes.c_byte),
#             ("lfStrikeOut", ctypes.c_byte),
#             ("lfCharSet", ctypes.c_byte),
#             ("lfOutPrecision", ctypes.c_byte),
#             ("lfClipPrecision", ctypes.c_byte),
#             ("lfQuality", ctypes.c_byte),
#             ("lfPitchAndFamily", ctypes.c_byte),
#             ("lfFaceName", ctypes.c_char * 32)
#         ]

#     screen_width = user32.GetSystemMetrics(0)
#     screen_height = user32.GetSystemMetrics(1)

#     hwnd = user32.CreateWindowExA(
#         0,
#         "STATIC",
#         None,
#         0x80000000 | 0x40000000,
#         0,
#         0,
#         screen_width,
#         screen_height,
#         None,
#         None,
#         None,
#         None
#     )

#     user32.SetClassLongA(hwnd, -10, int("0x000000FF", 16))
#     user32.UpdateWindow(hwnd)

#     hdc = user32.GetDC(hwnd)

#     logfont = LOGFONTA()
#     logfont.lfHeight = -20
#     logfont.lfWeight = 400
#     logfont.lfFaceName = b"Lucida Console"

#     font = gdi32.CreateFontIndirectA(ctypes.byref(logfont))

#     # Call SelectObject from gdi32
#     gdi32.SelectObject(hdc, font)

#  # Call SetTextColor from gdi32
#     gdi32.SetTextColor(hdc, int("0xFFFFFF", 16))
#     # ... other code ...

#     # Call TextOutA from gdi32
#     gdi32.TextOutA(hdc, 100, 100, b"A problem has been detected and Windows has been shut down to prevent damage\nto your computer.", len("A problem has been detected and Windows has been shut down to prevent damage\nto your computer."))
#     gdi32.TextOutA(hdc, 100, 200, b"DRIVER_IRQL_NOT_LESS_OR_EQUAL", len("DRIVER_IRQL_NOT_LESS_OR_EQUAL"))
#     gdi32.TextOutA(hdc, 100, 300, f"Technical information: *** STOP: 0x{random.randint(10000000, 99999999):X}".encode(), len(f"Technical information: *** STOP: 0x{random.randint(10000000, 99999999):X}"))

#     # ... rest of the code ...
#     time.sleep(duration)

#     user32.DeleteObject(font)
#     user32.ReleaseDC(hwnd, hdc)
#     user32.DestroyWindow(hwnd)

# fake_bsod()
# exit()
# information_msg_beforelower =  r"https://www.youtube.com/watch?v=dc5Cy0CL0Fw&list=RDoyeMrEU8-GU&index=7splitterofty1243splitterofty1243"


# print(information_msg_beforelower.lower().split("splitterofty1243")[1], information_msg_beforelower.lower().split("splitterofty1243")[2])


# exit()
# import win32gui
# import win32con
# import win32process
# import win32com.client
# import psutil
# import time

# def force_show_hidden_windows(name):  # e.g. chrome.exe
#     def enum_windows_callback(hwnd, result):
#         _, pid = win32process.GetWindowThreadProcessId(hwnd)
#         try:
#             process = psutil.Process(pid)
#             if process.name().lower() == name.lower():
#                 # Include the window even if it's not currently visible
#                 title = win32gui.GetWindowText(hwnd)
#                 if title:  # Only include windows with a title
#                     result.append((hwnd, title))
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#         return True

#     windows = []
#     win32gui.EnumWindows(enum_windows_callback, windows)

#     if not windows:
#         print(f"No windows found for process: {name}")
#         return

#     shell = win32com.client.Dispatch("Shell.Application")

#     for hwnd, title in windows:
#         try:
#             print(f"Attempting to show window: '{title}' (handle: {hwnd})")

#             # Make the window visible first
#             win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

#             # Try to restore the window if it's minimized
#             win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

#             # Bring the window to the foreground
#             win32gui.SetForegroundWindow(hwnd)

#             # Force the taskbar button to flash
#             win32gui.FlashWindow(hwnd, True)

#             # Use the shell to force the window to the foreground
#             shell.MinimizeAll()
#             time.sleep(0.5)  # Give some time for minimization
#             win32gui.SetForegroundWindow(hwnd)

#             print(f"Successfully showed window: '{title}' (handle: {hwnd})")
#         except Exception as e:
#             print(f"Error showing window '{title}' (handle: {hwnd}): {str(e)}")

#     print("Finished attempting to show hidden windows.")

# # Usage
# force_show_hidden_windows("notepad.exe")  # Replace with your process name