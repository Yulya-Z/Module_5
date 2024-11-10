import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def hash(self):
        return hash(self.password)

class Video:
    def __init__(self, title, duration, *adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self): # current_user
        self.users = {}  # Хранит пользователей
        self.videos = []  # Хранит видео
        self.current_user = ()

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users[nickname] = User(nickname, password, age)
            self.current_user = self.users[nickname]
            print("Пользователь успешно зарегистрирован")

    def log_out(self):
        current_user = None

    def log_in(self, nickname, password):
        user = self.users.get(nickname)
        if user and user.password == password:  #сравнение по хэшу/дополнить
            self.current_user = user
        else:
            print("Неверный логин или пароль")

    def add(self, video):
        self.videos.append(video)
        print(f"Видео успешно добавлено.")

    def get_videos(self, title):
        for video in self.videos:
            if title.upper() in video.title.upper():
                print(video.title)

    def watch_video(self, title):
        user = self.current_user
        if not user:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            for video in self.videos:
                if video.title.lower() == title.lower():
                    if video.adult_mode and user.age < 18:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        while video.time_now != video.duration:
                            video.time_now += 1
                            print("Вы смотрите видео на секунде: ", video.time_now)
                            time.sleep(1)

                print("Конец видео")

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    #print(ur.get_videos('лучший'))
    #print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    #ur.watch_video('Лучший язык программирования 2024 года!')





