from manim import *
import numpy as np

class SolarFunctionIntroduction(Scene):
    def construct(self):
        # Titel
        title = Text("Funktionen am Beispiel einer Solaranlage", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.scale(0.7).to_corner(UL))
        
        # Einführung zur Funktion
        func_def = Text("Eine Funktion beschreibt, wie eine Größe von einer anderen abhängt", 
                        font_size=28)
        func_def.next_to(title, DOWN, buff=1)
        self.play(Write(func_def))
        self.wait(2)
        self.play(FadeOut(func_def))
        
        # Pfeildiagramm für funktionalen Zusammenhang
        arrow_diagram = self.create_function_diagram()
        self.play(Create(arrow_diagram))
        self.wait(2)
        self.play(FadeOut(arrow_diagram))
        
        # Definitionsmenge visualisieren
        self.show_domain()
        
        # Wertemenge visualisieren
        self.show_range()
        
        # Funktionsgleichung darstellen
        self.show_function_equation()
        
        # Wertetabelle erstellen
        self.show_value_table()
        
        # Grafische Darstellung
        self.show_graph()
        
        # Übergang zu Funktionen mehrerer Variablen
        self.preview_multivariate_functions()
        
        # Abschluss
        final_text = Text("Vielen Dank für Ihre Aufmerksamkeit!", font_size=36)
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)
        self.play(FadeOut(final_text), FadeOut(title))
        self.wait(1)

    def create_function_diagram(self):
        # Erstellt ein Pfeildiagramm für die Funktion
        arrow_group = VGroup()
        
        box1 = Rectangle(height=1, width=2, color=BLUE)
        box1_text = Text("Tageszeit", font_size=24)
        box1_text.move_to(box1.get_center())
        box1_group = VGroup(box1, box1_text)
        
        box2 = Rectangle(height=1, width=2, color=GREEN)
        box2_text = Text("f(t) = P", font_size=24)
        box2_text.move_to(box2.get_center())
        box2_group = VGroup(box2, box2_text)
        box2_group.next_to(box1_group, RIGHT, buff=1.5)
        
        box3 = Rectangle(height=1, width=2, color=RED)
        box3_text = Text("Stromproduktion", font_size=20)
        box3_text.move_to(box3.get_center())
        box3_group = VGroup(box3, box3_text)
        box3_group.next_to(box2_group, RIGHT, buff=1.5)
        
        arrow1 = Arrow(box1.get_right(), box2.get_left(), buff=0.1, color=WHITE)
        arrow2 = Arrow(box2.get_right(), box3.get_left(), buff=0.1, color=WHITE)
        
        arrow_group.add(box1_group, box2_group, box3_group, arrow1, arrow2)
        arrow_group.move_to(ORIGIN)
        
        return arrow_group

    def show_domain(self):
        # Visualisierung der Definitionsmenge
        domain_title = Text("Definitionsmenge", font_size=36, color=BLUE)
        domain_title.to_edge(UP)
        
        time_line = NumberLine(
            x_range=[0, 24, 1],
            length=10,
            include_numbers=True,
            include_tip=True
        )
        time_line.shift(DOWN)
        
        brace = Brace(time_line, UP)
        domain_def = MathTex(r"D = \{t \mid 6 \leq t \leq 20, t \text{ in Stunden}\}")
        domain_def.next_to(brace, UP)
        
        day_time = time_line.copy()
        day_time.set_color(YELLOW)
        
        # Highlight nur den gültigen Bereich
        highlight = Line(
            time_line.number_to_point(6),
            time_line.number_to_point(20),
            color=YELLOW,
            stroke_width=10
        )
        
        sun_emoji = Text("☀️", font_size=36)
        sun_emoji.next_to(time_line.number_to_point(13), UP, buff=0.5)
        
        moon_emoji = Text("🌙", font_size=36)
        moon_emoji.next_to(time_line.number_to_point(0), UP, buff=0.5)
        
        night_emoji = Text("🌃", font_size=36)
        night_emoji.next_to(time_line.number_to_point(22), UP, buff=0.5)
        
        self.play(Write(domain_title))
        self.play(Create(time_line))
        self.wait(1)
        self.play(
            FadeIn(sun_emoji), 
            FadeIn(moon_emoji), 
            FadeIn(night_emoji)
        )
        self.wait(1)
        self.play(Create(highlight))
        self.play(GrowFromCenter(brace), Write(domain_def))
        self.wait(2)
        
        self.play(
            FadeOut(domain_title),
            FadeOut(time_line),
            FadeOut(highlight),
            FadeOut(brace),
            FadeOut(domain_def),
            FadeOut(sun_emoji),
            FadeOut(moon_emoji),
            FadeOut(night_emoji)
        )
        
    def show_range(self):
        # Visualisierung der Wertemenge
        range_title = Text("Wertemenge", font_size=36, color=RED)
        range_title.to_edge(UP)
        
        power_meter = VGroup()
        circle = Circle(radius=1.5, color=WHITE)
        
        # Skala des Strommessers
        for i in range(0, 11):
            angle = 135 * DEGREES + i * (270 * DEGREES) / 10
            line_length = 0.2 if i % 5 == 0 else 0.1
            line = Line(
                circle.point_at_angle(angle),
                circle.point_at_angle(angle) * (1 - line_length),
                color=WHITE
            )
            power_meter.add(line)
            
            if i % 5 == 0:
                value = Text(f"{i}", font_size=20)
                value.move_to(circle.point_at_angle(angle) * 0.7)
                power_meter.add(value)
        
        # Messzeiger
        pointer = Line(ORIGIN, UP * 1.3, color=RED, stroke_width=5)
        pointer.rotate(-45 * DEGREES, about_point=ORIGIN)
        power_meter.add(pointer)
        
        # kW Einheit
        unit = Text("kW", font_size=24, color=YELLOW)
        unit.move_to(circle.point_at_angle(270 * DEGREES) * 0.5)
        power_meter.add(unit)
        
        # Äußerer Rahmen
        outer_circle = Circle(radius=1.6, color=GREY)
        power_meter.add(circle, outer_circle)
        
        power_meter.shift(DOWN * 0.5)
        
        range_def = MathTex(r"W = \{P \mid 0 \leq P \leq P_{max}, P \text{ in Kilowatt}\}")
        range_def.next_to(power_meter, DOWN, buff=0.7)
        
        self.play(Write(range_title))
        self.play(Create(power_meter))
        self.wait(1)
        
        # Animation des Zeigers
        self.play(Rotate(
            pointer, 
            angle=270 * DEGREES, 
            about_point=ORIGIN, 
            run_time=3
        ))
        self.wait(1)
        
        self.play(Write(range_def))
        self.wait(2)
        
        self.play(
            FadeOut(range_title),
            FadeOut(power_meter),
            FadeOut(range_def)
        )
        
    def show_function_equation(self):
        # Visualisierung der Funktionsgleichung
        eq_title = Text("Funktionsgleichung", font_size=36, color=GREEN)
        eq_title.to_edge(UP)
        
        # Schrittweiser Aufbau der Formel
        eq_basic = MathTex("P(t) =")
        eq_max = MathTex("P(t) = P_{max}")
        eq_sin = MathTex(r"P(t) = P_{max} \cdot \sin\left(\right)")
        eq_fraction = MathTex(r"P(t) = P_{max} \cdot \sin\left(\frac{\pi \cdot (t-6)}{14}\right)")
        eq_domain = MathTex(r"P(t) = P_{max} \cdot \sin\left(\frac{\pi \cdot (t-6)}{14}\right), \; \text{für } 6 \leq t \leq 20")
        
        equations = [eq_basic, eq_max, eq_sin, eq_fraction, eq_domain]
        
        # Platzierung der Formeln
        for eq in equations:
            eq.move_to(ORIGIN)
            
        # Beschreibung der Gleichung
        explanation = Text(
            "Diese Formel beschreibt, wie die Leistung morgens ansteigt,\n"
            "mittags ihr Maximum erreicht und abends wieder abfällt.",
            font_size=24
        )
        explanation.next_to(eq_domain, DOWN, buff=0.7)
        
        self.play(Write(eq_title))
        self.play(Write(eq_basic))
        self.wait(1)
        
        for i in range(1, len(equations)):
            self.play(TransformMatchingTex(equations[i-1], equations[i]))
            self.wait(1)
            
        self.play(Write(explanation))
        self.wait(2)
        
        self.play(
            FadeOut(eq_title),
            FadeOut(equations[-1]),
            FadeOut(explanation)
        )
        
    def show_value_table(self):
        # Wertetabelle erstellen
        table_title = Text("Wertetabelle", font_size=36, color=BLUE)
        table_title.to_edge(UP)
        
        # Tabelle mit Wertepaaren
        table = MathTable(
            [["\\text{Uhrzeit}", "\\text{Leistung (kW)}"],
             ["6:00", "0"],
             ["9:00", "2.5"],
             ["13:00", "5.0"],
             ["17:00", "2.5"],
             ["20:00", "0"]],
            include_outer_lines=True
        )
        table.scale(0.7)
        
        self.play(Write(table_title))
        self.play(Create(table))
        self.wait(2)
        
        # Koordinatensystem für Darstellung als Punkte
        axes = Axes(
            x_range=[6, 20, 2],
            y_range=[0, 5.5, 1],
            axis_config={"include_tip": False},
            x_length=6,
            y_length=4
        )
        
        axes.next_to(table, RIGHT, buff=0.8)
        
        # Achsenbeschriftungen
        x_label = axes.get_x_axis_label("t \\text{ (Stunden)}", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label("P \\text{ (kW)}", edge=LEFT, direction=LEFT)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Punkte einzeln einblenden
        dots = []
        times = [6, 9, 13, 17, 20]
        powers = [0, 2.5, 5.0, 2.5, 0]
        
        for i, (t, p) in enumerate(zip(times, powers)):
            dot = Dot(axes.c2p(t, p), color=YELLOW)
            dots.append(dot)
            # Hervorhebung in der Tabelle
            cell_time = table.get_entries((i+2, 1))
            cell_power = table.get_entries((i+2, 2))
            
            self.play(
                cell_time.animate.set_color(YELLOW),
                cell_power.animate.set_color(YELLOW),
                FadeIn(dot, scale=1.5)
            )
            self.wait(0.5)
            self.play(
                cell_time.animate.set_color(WHITE),
                cell_power.animate.set_color(WHITE)
            )
            
        self.wait(1)
        
        self.play(
            FadeOut(table_title),
            FadeOut(table),
            *[dot.animate.set_color(RED) for dot in dots]
        )
        
        # Animation zum nächsten Abschnitt vorbereiten
        self.dots = dots
        self.axes = axes
        self.x_label = x_label
        self.y_label = y_label
        
    def show_graph(self):
        # Grafische Darstellung
        graph_title = Text("Grafische Darstellung", font_size=36, color=YELLOW)
        graph_title.to_edge(UP)
        
        # Funktion definieren
        def solar_power(t):
            if 6 <= t <= 20:
                return 5 * np.sin(np.pi * (t - 6) / 14)
            return 0
        
        # Graph erstellen
        graph = self.axes.plot(
            lambda t: solar_power(t), 
            x_range=[6, 20], 
            color=YELLOW
        )
        
        self.play(Write(graph_title))
        self.wait(1)
        
        # Verbindung der Punkte zum vollständigen Graphen
        self.play(Create(graph))
        self.wait(2)
        
        # Erklärungstext
        explanation = Text(
            "Diese Kurve beschreibt die Stromproduktion einer Solaranlage\n"
            "über den Tagesverlauf - von Sonnenaufgang bis Sonnenuntergang.",
            font_size=24
        )
        explanation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(2)
        
        self.play(
            FadeOut(graph_title),
            FadeOut(explanation),
            FadeOut(graph),
            *[FadeOut(dot) for dot in self.dots],
            FadeOut(self.axes),
            FadeOut(self.x_label),
            FadeOut(self.y_label)
        )
        
    def preview_multivariate_functions(self):
        # Vorschau auf Funktionen mehrerer Variablen
        preview_title = Text("Ausblick: Funktionen mehrerer Variablen", font_size=36, color=BLUE)
        preview_title.to_edge(UP)
        
        # Einfaches vs. komplexes Modell
        simple_model = MathTex("P = f(t)")
        complex_model = MathTex("P = f(t, w, s, l)")
        
        simple_model.shift(LEFT * 3 + UP * 1)
        complex_model.shift(RIGHT * 3 + UP * 1)
        
        simple_text = Text("Abhängig nur von\nder Tageszeit", font_size=24)
        complex_text = Text("Abhängig von Tageszeit, Wetter,\nJahreszeit und Standort", font_size=24)
        
        simple_text.next_to(simple_model, DOWN, buff=0.5)
        complex_text.next_to(complex_model, DOWN, buff=0.5)
        
        # 3D-Visualisierung
        axes_3d = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 5, 1],
            x_length=4,
            y_length=4,
            z_length=2.5
        ).scale(0.7)
        
        axes_3d.shift(DOWN * 1.5)
        
        # Beschriftungen
        x_label = Text("Zeit", font_size=20).next_to(axes_3d.x_axis, RIGHT)
        y_label = Text("Wetter", font_size=20).next_to(axes_3d.y_axis, UP)
        z_label = Text("Leistung", font_size=20).next_to(axes_3d.z_axis, UP)
        
        self.play(Write(preview_title))
        self.wait(1)
        
        self.play(
            Write(simple_model),
            Write(complex_model)
        )
        
        self.play(
            Write(simple_text),
            Write(complex_text)
        )
        self.wait(2)
        
        self.play(
            FadeOut(simple_model),
            FadeOut(simple_text),
            FadeOut(complex_text),
            complex_model.animate.move_to(UP * 1)
        )
        
        # 3D-Darstellung hinzufügen
        self.play(
            Create(axes_3d),
            Write(x_label),
            Write(y_label),
            Write(z_label)
        )
        
        # Einfache Parametrisierte Fläche
        def param_surface(u, v):
            x = u
            y = v
            # Funktion, die von Zeit und Wetter abhängt
            z = 5 * np.sin(np.pi * (u + 3) / 6) * np.exp(-0.5 * v**2)
            return np.array([x, y, z])
        
        surface = Surface(
            lambda u, v: axes_3d.c2p(*param_surface(u, v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(20, 20),
            fill_opacity=0.7,
            stroke_width=0.5,
            stroke_color=WHITE
        )
        
        self.play(Create(surface))
        self.wait(2)
        
        # Kamerarotation
        self.move_camera(phi=60 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        
        conclusion_text = Text(
            "In den nächsten Videos werden wir solche Funktionen\n"
            "mehrerer Variablen genauer untersuchen.",
            font_size=24
        )
        conclusion_text.to_edge(DOWN)
        
        self.play(Write(conclusion_text))
        self.wait(2)
        
        self.play(
            FadeOut(preview_title),
            FadeOut(complex_model),
            FadeOut(axes_3d),
            FadeOut(surface),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(z_label),
            FadeOut(conclusion_text)
        )
        
    def move_camera(self, phi=None, theta=None, distance=None, gamma=None):
        if self.renderer.camera_class == ThreeDCamera:
            camera: ThreeDCamera = self.renderer.camera
            if phi is not None:
                camera.set_phi(phi)
            if theta is not None:
                camera.set_theta(theta)
            if distance is not None:
                camera.set_distance(distance)
            if gamma is not None:
                camera.set_gamma(gamma)
                
    def begin_ambient_camera_rotation(self, rate=0.02):
        if self.renderer.camera_class == ThreeDCamera:
            camera: ThreeDCamera = self.renderer.camera
            camera.theta_tracker.add_updater(
                lambda m, dt: m.increment_value(rate * dt)
            )
            self.renderer.camera.theta_tracker = camera.theta_tracker
            
    def stop_ambient_camera_rotation(self):
        if self.renderer.camera_class == ThreeDCamera:
            self.renderer.camera.theta_tracker.clear_updaters()


class SolarFunctionSimplified(Scene):
    """Eine kürzere Version für schnelleres Rendering"""
    def construct(self):
        # Titel
        title = Text("Funktionen am Beispiel einer Solaranlage")
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Definitionsmenge
        domain_text = Text("Definitionsmenge: Tageszeit (6-20 Uhr)")
        domain_text.next_to(title, DOWN, buff=1)
        self.play(Write(domain_text))
        self.wait(1)
        
        # Wertemenge
        range_text = Text("Wertemenge: Stromproduktion (0-5 kW)")
        range_text.next_to(domain_text, DOWN)
        self.play(Write(range_text))
        self.wait(1)
        
        # Graph
        axes = Axes(
            x_range=[0, 24, 6],
            y_range=[0, 6, 1],
            axis_config={"include_tip": True}
        )
        axes.next_to(range_text, DOWN, buff=0.5)
        
        # Achsenbeschriftungen
        x_label = axes.get_x_axis_label("t (Stunden)")
        y_label = axes.get_y_axis_label("P (kW)")
        
        # Funktion plotten
        def solar_power(t):
            if 6 <= t <= 20:
                return 5 * np.sin(np.pi * (t - 6) / 14)
            return 0
        
        graph = axes.plot(
            lambda t: solar_power(t), 
            x_range=[0, 24], 
            color=YELLOW
        )
        
        self.play(
            Create(axes), 
            Write(x_label), 
            Write(y_label)
        )
        self.wait(1)
        self.play(Create(graph))
        self.wait(2)
        
        # Abschluss
        final_text = Text("Vielen Dank für Ihre Aufmerksamkeit!")
        final_text.to_edge(DOWN)
        self.play(Write(final_text))
        self.wait(2)


# Führen Sie diesen Befehl in der Kommandozeile aus, um die Animation zu rendern:
# manim -pql solar_function_animation.py SolarFunctionSimplified
# oder für die vollständige Version mit hoher Qualität:
# manim -pqh solar_function_animation.py SolarFunctionIntroduction