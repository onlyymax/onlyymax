# Importa le librerie necessarie da Kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Definisci la classe della tua applicazione
class SimpleGUIApp(App):
    
    def build(self):
        # Creazione di un layout principale (Box Layout)
        layout = BoxLayout(orientation='vertical')
        
        # Creazione di un widget di testo (Label) e un widget pulsante (Button)
        label = Label(text='Ciao da Kivy!')
        button = Button(text='Premi!')
        
        # Aggiunta dei widget al layout
        layout.add_widget(label)
        layout.add_widget(button)
        
        # Collegamento di una funzione all'evento "on_press" del pulsante
        button.bind(on_press=self.on_button_press)
        
        return layout
    
    def on_button_press(self, instance):
        # Azione da eseguire quando il pulsante viene premuto
        print("Hai premuto il pulsante!")

# Istanzia e avvia l'applicazione
if __name__ == '__main__':
    app = SimpleGUIApp()
    app.run()
