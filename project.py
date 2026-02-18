import math
import sys

import pygame


WIDTH, HEIGHT = 1200, 760
RADAR_CENTER = (450, 380)
RADAR_RADIUS = 320
FPS = 60

MIN_SEPARATION_PX = 80
MIN_SEPARATION_ALT = 1000

BG = (8, 20, 32)
RADAR_BG = (15, 35, 40)
GRID = (40, 95, 85)
TEXT = (210, 236, 245)
SAFE = (86, 233, 176)
WARN = (247, 89, 89)
SELECTED = (255, 214, 88)
PLANE_COLOR = (148, 207, 255)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def wrap_angle(angle: float) -> float:
    return angle % 360.0


def distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


class Aircraft:
    def __init__(self, callsign: str, x: float, y: float, heading: float, speed: float, altitude: float) -> None:
        self.callsign = callsign
        self.x = x
        self.y = y
        self.heading = heading
        self.speed = speed
        self.altitude = altitude

    def position(self) -> tuple[float, float]:
        return (self.x, self.y)

    def update(self, dt: float) -> None:
        px_per_sec = self.speed * 0.09
        rad = math.radians(self.heading)
        self.x += math.cos(rad) * px_per_sec * dt
        self.y += math.sin(rad) * px_per_sec * dt
        self._keep_inside_radar()

    def _keep_inside_radar(self) -> None:
        dx = self.x - RADAR_CENTER[0]
        dy = self.y - RADAR_CENTER[1]
        d = math.hypot(dx, dy)

        if d >= RADAR_RADIUS - 8 and d > 0:
            nx, ny = dx / d, dy / d
            vx = math.cos(math.radians(self.heading))
            vy = math.sin(math.radians(self.heading))
            dot = vx * nx + vy * ny
            rvx = vx - 2 * dot * nx
            rvy = vy - 2 * dot * ny
            self.heading = wrap_angle(math.degrees(math.atan2(rvy, rvx)))
            self.x = RADAR_CENTER[0] + nx * (RADAR_RADIUS - 9)
            self.y = RADAR_CENTER[1] + ny * (RADAR_RADIUS - 9)

    def draw(self, surface: pygame.Surface, selected: bool = False) -> None:
        size = 9
        rad = math.radians(self.heading)

        nose = (self.x + math.cos(rad) * size * 1.6, self.y + math.sin(rad) * size * 1.6)
        left = (self.x + math.cos(rad + 2.4) * size, self.y + math.sin(rad + 2.4) * size)
        right = (self.x + math.cos(rad - 2.4) * size, self.y + math.sin(rad - 2.4) * size)

        color = SELECTED if selected else PLANE_COLOR
        pygame.draw.polygon(surface, color, [nose, left, right])
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 2)


class ThreePlaneATC:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("ATC Simulator - Three Aircraft")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("consolas", 19)
        self.small = pygame.font.SysFont("consolas", 15)

        self.paused = False
        self.selected_index = 0
        self.aircraft: list[Aircraft] = []

        self.alert = False
        self.conflict_pairs: list[tuple[str, str, int, int]] = []

        self.reset()

    def reset(self) -> None:
        self.aircraft = [
            Aircraft("Buddha airlines", 220, 220, 25, 230, 7000),
            Aircraft("Shree airlines", 660, 520, 210, 225, 7800),
            Aircraft("Yeti Airlines", 320, 560, 310, 220, 8400),
        ]
        self.selected_index = 0
        self.alert = False
        self.conflict_pairs = []
        self.evaluate_conflicts()

    def selected(self) -> Aircraft:
        return self.aircraft[self.selected_index]

    def evaluate_conflicts(self) -> None:
        self.conflict_pairs = []

        for i in range(len(self.aircraft)):
            for j in range(i + 1, len(self.aircraft)):
                a = self.aircraft[i]
                b = self.aircraft[j]
                hdist = int(distance(a.position(), b.position()))
                adiff = int(abs(a.altitude - b.altitude))

                # Conflict requires BOTH close horizontal distance and low vertical separation.
                if hdist < MIN_SEPARATION_PX and adiff <= MIN_SEPARATION_ALT:
                    self.conflict_pairs.append((a.callsign, b.callsign, hdist, adiff))

        self.alert = len(self.conflict_pairs) > 0

    def update(self, dt: float) -> None:
        if not self.paused:
            for plane in self.aircraft:
                plane.update(dt)

        # Recompute every frame so alert state stays accurate even while paused/manual edits.
        self.evaluate_conflicts()

    def draw(self) -> None:
        self.screen.fill(BG)
        self.draw_radar()
        self.draw_planes()
        self.draw_ui()
        pygame.display.flip()

    def draw_radar(self) -> None:
        pygame.draw.circle(self.screen, RADAR_BG, RADAR_CENTER, RADAR_RADIUS)
        pygame.draw.circle(self.screen, GRID, RADAR_CENTER, RADAR_RADIUS, 2)

        for r in (80, 160, 240):
            pygame.draw.circle(self.screen, GRID, RADAR_CENTER, r, 1)

        for a in range(0, 360, 30):
            rad = math.radians(a)
            x = RADAR_CENTER[0] + math.cos(rad) * RADAR_RADIUS
            y = RADAR_CENTER[1] + math.sin(rad) * RADAR_RADIUS
            pygame.draw.line(self.screen, GRID, RADAR_CENTER, (x, y), 1)

    def draw_planes(self) -> None:
        for i, plane in enumerate(self.aircraft):
            selected = i == self.selected_index
            plane.draw(self.screen, selected=selected)

            label_color = SELECTED if selected else TEXT
            txt = self.small.render(
                f"{plane.callsign}  HDG {int(plane.heading)}  SPD {int(plane.speed)}kt  ALT {int(plane.altitude)}ft",
                True,
                label_color,
            )
            self.screen.blit(txt, (plane.x + 12, plane.y - 16))

    def draw_ui(self) -> None:
        panel = pygame.Rect(800, 30, 370, 700)
        pygame.draw.rect(self.screen, (19, 28, 44), panel, border_radius=8)
        pygame.draw.rect(self.screen, (48, 69, 98), panel, 2, border_radius=8)

        min_sep = 999999
        min_alt_sep = 999999
        for i in range(len(self.aircraft)):
            for j in range(i + 1, len(self.aircraft)):
                a = self.aircraft[i]
                b = self.aircraft[j]
                min_sep = min(min_sep, int(distance(a.position(), b.position())))
                min_alt_sep = min(min_alt_sep, int(abs(a.altitude - b.altitude)))

        status = "ALERT: PLANES TOO CLOSE" if self.alert else "Normal: Safe Separation"
        status_color = WARN if self.alert else SAFE

        lines = [
            "ATC - Three Airplanes",
            f"Status: {'PAUSED' if self.paused else 'LIVE'}",
            "",
            status,
            f"Min Horizontal Separation: {min_sep} px",
            f"Min Vertical Separation: {min_alt_sep} ft",
            "",
            "Altitude separation rule:",
            f"Safe: > {MIN_SEPARATION_ALT} ft difference",
            f"Danger: 0-{MIN_SEPARATION_ALT} ft difference",
            "(Danger alert needs horizontal < 80 px too)",
            "",
            "Selected Aircraft:",
            f"{self.selected().callsign}",
            "",
            "Controls:",
            "TAB : Select plane",
            "A/D : Turn left/right",
            "W/S : Altitude up/down",
            "Q/E : Speed down/up",
            "R   : Reset positions",
            "SPACE: Pause/Resume",
            "ESC : Quit",
        ]

        y = panel.y + 10
        for i, line in enumerate(lines):
            font = self.font if i == 0 else self.small
            color = status_color if line == status else TEXT
            txt = font.render(line, True, color)
            self.screen.blit(txt, (panel.x + 12, y))
            y += 30 if i == 0 else 24

        if self.alert:
            alert = self.font.render("CONFLICT ALERT", True, WARN)
            self.screen.blit(alert, (30, 28))

            if len(self.conflict_pairs) == 3:
                all_three = self.small.render("Conflict among all three planes", True, WARN)
                self.screen.blit(all_three, (30, 58))
            else:
                for idx, pair in enumerate(self.conflict_pairs):
                    pair_text = self.small.render(
                        f"{pair[0]} <-> {pair[1]}  (H:{pair[2]}px, V:{pair[3]}ft)",
                        True,
                        WARN,
                    )
                    self.screen.blit(pair_text, (30, 58 + idx * 20))

    def handle_key(self, key: int) -> None:
        if key == pygame.K_TAB:
            self.selected_index = (self.selected_index + 1) % len(self.aircraft)
            return

        if key == pygame.K_SPACE:
            self.paused = not self.paused
            return

        if key == pygame.K_r:
            self.reset()
            return

        p = self.selected()

        if key == pygame.K_a:
            p.heading = wrap_angle(p.heading - 10)
        if key == pygame.K_d:
            p.heading = wrap_angle(p.heading + 10)
        if key == pygame.K_w:
            p.altitude = clamp(p.altitude + 500, 1000, 20000)
        if key == pygame.K_s:
            p.altitude = clamp(p.altitude - 500, 1000, 20000)
        if key == pygame.K_q:
            p.speed = clamp(p.speed - 10, 120, 320)
        if key == pygame.K_e:
            p.speed = clamp(p.speed + 10, 120, 320)

    def run(self) -> None:
        while True:
            dt = self.clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    self.handle_key(event.key)

            self.update(dt)
            self.draw()


if __name__ == "__main__":
    ThreePlaneATC().run()
