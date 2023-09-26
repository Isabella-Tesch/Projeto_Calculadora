import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QWidget, QPushButton, QGridLayout

class CreateWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calculadora")
        
        self.setGeometry(500, 210, 300, 300)
        
        central_widget = QWidget()
        
        self.setCentralWidget(central_widget) #Widget central é o componente que ocupa maior parte da janela.
    
        self.display = QLineEdit()
        
        self.display.setFixedHeight(30) #Tamanho da caixa de texto
        
        grid_layout = QGridLayout(central_widget) #Layout de grade para organizar os botões
        
        grid_layout.addWidget(self.display, 0, 0, 1, 4) #posicionar a tela na linha 0, coluna 0, número de linhas que a tela vai ocupar 1, número de colunas que a tela vai ocupar 4.
          
        self.ButtonsCalc(grid_layout)
    
    def ButtonsCalc(self, grid_layout):
        """
        Essa função serve para gerar os botões da calculadora.
        """
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "x"],
            ["1", "2", "3", "-"],
            ["0", ".", "+", "="]
        ]
        
        for linha in range(len(buttons)):
            for indice in range(len(buttons[linha])):
                btn =  QPushButton(buttons[linha][indice])  
                
                btn.setStyleSheet("background: blue; color: white")
                
                btn.clicked.connect(self.Btn_Clicked)
                 
                grid_layout.addWidget(btn)
    
    def Btn_Clicked(self):
        GetBtnClicado = self.sender()
        
        GetTxtBtn = GetBtnClicado.text()
        
        self.display.setText(GetTxtBtn)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    root = CreateWindow()
    
    root.show()
    
    sys.exit(app.exec_())