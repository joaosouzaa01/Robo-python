import tkinter as tk
import time
import subprocess

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer App")

        # Centralize a janela na tela
        window_width = 400
        window_height = 250
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.counter_label = tk.Label(root, text="Tempo: 0 segundos", font=("Helvetica", 20))
        self.counter_label.pack(pady=20)

        # Crie um frame para centralizar os botões verticalmente
        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_button = tk.Button(button_frame, text="Iniciar", font=("Helvetica", 12), command=self.start_timer, bg="green", bd=5, relief="ridge", fg="white")
        self.stop_button = tk.Button(button_frame, text="Parar", font=("Helvetica", 12), command=self.stop_timer, bg="red", bd=5, relief="ridge", fg="white")

        # Centralize os botões horizontalmente no frame
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.status_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.status_label.pack(pady=20)

        self.timer_running = False
        self.start_time = None
        self.processes = []

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time()
            self.update_timer()
            self.status_label.config(text="APLICAÇÃO RODANDO", fg="green")

            # Inicie o arquivo ou aplicação desejada e adicione o processo à lista
            process = subprocess.Popen(["python", "src\script-abrir-pag.py"])
            self.processes.append(process)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.status_label.config(text="APLICAÇÃO PARADA", fg="red")

            # Pare todos os processos em execução e limpe a lista
            for process in self.processes:
                process.terminate()
            self.processes.clear()

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.counter_label.config(text=f"Tempo: {int(elapsed_time)} segundos")
            self.root.after(1000, self.update_timer)  # Atualiza a cada 1000ms (1 segundo)

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
