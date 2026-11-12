import reflex as rx

# Estado da aplicação para armazenar os exercícios concluídos
class WorkoutState(rx.State):
    completed_exercises: list[str] = []

    def toggle_exercise(self, exercise: str):
        if exercise in self.completed_exercises:
            self.completed_exercises.remove(exercise)
        else:
            self.completed_exercises.append(exercise)

# Componente reutilizável para cada exercício
def exercise_item(name: str, sets: str) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.checkbox(
                on_change=lambda _: WorkoutState.toggle_exercise(name),
                size="3",
                color_scheme="green",
            ),
            rx.vstack(
                rx.text(name, weight="bold", size="3"),
                rx.text(sets, color="gray", size="2"),
                spacing="1",
                align_items="start",
            ),
            spacing="3",
            align_items="center",
        ),
        width="100%",
        margin_bottom="8px",
    )

# Treino A
def workout_a() -> rx.Component:
    return rx.vstack(
        rx.heading("Treino A - Pernas Completas", size="5", margin_bottom="4"),
        exercise_item("Hack squat", "4 séries x 15"),
        exercise_item("Hack machine", "4 séries x 15"),
        exercise_item("Cadeira extensora", "3 séries x 10/10/10"),
        exercise_item("Leg 45 pés paralelo + abdução", "3 séries x 21+21"),
        exercise_item("Stiff + mesa flexora", "4 séries x 15+15"),
        exercise_item("Agachamento sumo barra à frente", "4 séries x 15"),
        exercise_item("Cadeira adutora + abdutora (isometria)", "4 séries x 15+15(ISO)"),
        exercise_item("Avanço com hbc", "3 séries x 15"),
        exercise_item("Panturrilha no hack squat", "3 séries x 25"),
        width="100%",
    )

# Treino B
def workout_b() -> rx.Component:
    return rx.vstack(
        rx.heading("Treino B - Peito, Dorsal e Abdômen", size="5", margin_bottom="4"),
        exercise_item("Supino vertical 2 pegadas", "3 séries x 10+10"),
        exercise_item("Crucifixo máquina", "4 séries x 15"),
        exercise_item("Cross over polia baixa", "3 séries x 07/7/7"),
        exercise_item("Voador frontal", "Séries: 15/12/10/08"),
        exercise_item("Extensão dorsal", "3 séries x 21"),
        exercise_item("Pulley pegada semi pronada", "4 séries x 12(8iso) +15"),
        exercise_item("Remada articulada triângulo", "4 séries x 12"),
        exercise_item("Remada baixa peg. supinada + pronada", "3 séries x 15"),
        exercise_item("Remada apoiada", "3 séries x 15"),
        exercise_item("Abdominal livre", "4 séries x Máximo"),
        width="100%",
    )

# Treino C
def workout_c() -> rx.Component:
    return rx.vstack(
        rx.heading("Treino C - Ombros e Trapézio", size="5", margin_bottom="4"),
        exercise_item("Desenvolvimento hammer (2 pos)", "3 séries x 15/15"),
        exercise_item("Desenvolvimento Arnold", "4 séries x min 12 máx 15"),
        exercise_item("Desenvolvimento por trás Smith", "4 séries x 15"),
        exercise_item("Elevação lateral Cross uni front+post", "3 séries x 12/12"),
        exercise_item("Adução de escápula com hbc", "3 séries x 15"),
        exercise_item("Face Pull na barra", "4 séries x 15"),
        exercise_item("Remada alta hbc + encolhimento barra", "4 séries x 15/15"),
        exercise_item("Abdominal no pneu", "4 séries x 70"),
        width="100%",
    )

# Treino D
def workout_d() -> rx.Component:
    return rx.vstack(
        rx.heading("Treino D - Posterior, Bíceps e Tríceps", size="5", margin_bottom="4"),
        exercise_item("Stiff + mesa flexora (Post. do A)", "4 séries x 15+15"),
        exercise_item("Tríceps francês + bíceps corda", "3 séries x 15/15"),
        exercise_item("Tríceps + bíceps martelo", "3 séries x 15+15"),
        exercise_item("Bíceps uni roboot + tríceps testa", "3 séries x 12+15"),
        exercise_item("Tríceps coice + bíceps (21 B w)", "3 séries"),
        exercise_item("Abdominal remador com caneleira", "4 séries x 70"),
        width="100%",
    )

# Treino E
def workout_e() -> rx.Component:
    return rx.vstack(
        rx.heading("Treino E - Peito, Dorsal e Trapézio", size="5", margin_bottom="4"),
        rx.text("Peito e Dorsal (Repetição B)", weight="bold", color="blue", margin_top="3"),
        exercise_item("Supino vertical 2 pegadas", "3 séries x 10+10"),
        exercise_item("Crucifixo máquina", "4 séries x 15"),
        exercise_item("Cross over polia baixa", "3 séries x 07/7/7"),
        exercise_item("Voador frontal", "Séries: 15/12/10/08"),
        exercise_item("Extensão dorsal", "3 séries x 21"),
        exercise_item("Pulley pegada semi pronada", "4 séries x 12(8iso) +15"),
        exercise_item("Remada articulada triângulo", "4 séries x 12"),
        exercise_item("Remada baixa peg. supinada + pronada", "3 séries x 15"),
        exercise_item("Remada apoiada", "3 séries x 15"),
        rx.text("Trapézio (Repetição C)", weight="bold", color="blue", margin_top="3"),
        exercise_item("Adução de escápula com hbc", "3 séries x 15"),
        exercise_item("Face Pull na barra", "4 séries x 15"),
        exercise_item("Remada alta hbc + encolhimento barra", "4 séries x 15/15"),
        width="100%",
    )

# Treino F
def workout_f() -> rx.Component:
    return rx.vstack(
        rx.heading("Treino F - Ombro e Quadríceps", size="5", margin_bottom="4"),
        rx.text("Ombros (Repetição C)", weight="bold", color="blue", margin_top="3"),
        exercise_item("Desenvolvimento hammer (2 pos)", "3 séries x 15/15"),
        exercise_item("Desenvolvimento Arnold", "4 séries x min 12 máx 15"),
        exercise_item("Desenvolvimento por trás Smith", "4 séries x 15"),
        exercise_item("Elevação lateral Cross uni front+post", "3 séries x 12/12"),
        rx.text("Quadríceps (Repetição A)", weight="bold", color="blue", margin_top="3"),
        exercise_item("Hack squat", "4 séries x 15"),
        exercise_item("Hack machine", "4 séries x 15"),
        exercise_item("Cadeira extensora", "3 séries x 10/10/10"),
        exercise_item("Leg 45 pés paralelo + abdução", "3 séries x 21+21"),
        exercise_item("Agachamento sumo barra à frente", "4 séries x 15"),
        exercise_item("Cadeira adutora + abdutora (iso)", "4 séries x 15+15(ISO)"),
        exercise_item("Avanço com hbc", "3 séries x 15"),
        width="100%",
    )

# Página Principal com Abas
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Academia MAIA", size="7", margin_bottom="2", margin_top="4"),
            rx.text("Planilha de Treino A-F", color="gray", margin_bottom="5"),
            
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("A", value="tab_a"),
                    rx.tabs.trigger("B", value="tab_b"),
                    rx.tabs.trigger("C", value="tab_c"),
                    rx.tabs.trigger("D", value="tab_d"),
                    rx.tabs.trigger("E", value="tab_e"),
                    rx.tabs.trigger("F", value="tab_f"),
                    # Permite rolar as abas horizontalmente em telas pequenas
                    overflow_x="auto", 
                    width="100%",
                ),
                rx.tabs.content(workout_a(), value="tab_a"),
                rx.tabs.content(workout_b(), value="tab_b"),
                rx.tabs.content(workout_c(), value="tab_c"),
                rx.tabs.content(workout_d(), value="tab_d"),
                rx.tabs.content(workout_e(), value="tab_e"),
                rx.tabs.content(workout_f(), value="tab_f"),
                default_value="tab_a",
                width="100%",
            ),
            width="100%",
            padding_bottom="40px",
        ),
        size="2", 
    )

app = rx.App()
app.add_page(index, title="Treino MAIA")