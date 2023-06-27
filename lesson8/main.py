class Questions:
    def __init__(self):
        self.questions = ...
        self.hard = [range(1,5)]
        self.anwers = ...
        self.asked = False
        self.user_answer = None
        self.points = [range(10, 50, 10)]

    def get_points(self):
        return self.points[self.hard]
    
    def is_correct(self, user_answer):
        if user_answer.lower() == self.anwers:
            return True
        else:
            return False
        
    def build_question(self):
        return 
    
    def get_positive_fidback(self):
        return f"Ответ верный, получено {self.point} балов"

    def get_negative_feedback(self):
        return f'Ответ неверный. Правильный ответ {self.anwers}'
