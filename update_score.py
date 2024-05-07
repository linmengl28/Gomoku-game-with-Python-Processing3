import re


class UpdateScore:

    def add_new_score(self):
        name = self.input('YOU WIN! Enter your name for scores ranking.')
        info_dict = self.read_scores()
        if name in info_dict.keys():
            info_dict[name] += 1
        else:
            info_dict[name] = 1

        sorted_info = sorted(info_dict.items(),
                             key=lambda x: x[1],
                             reverse=True)

        out = ""
        for item in sorted_info:
            # out += f"{item[0]} {item[1]}\n"
            out += "{} {}\n".format(item[0], item[1])
        print(out)
        self.write_scores(out)

    def read_scores(self):
        try:
            with open('scores.txt', 'r') as file:
                content = file.read()
                info = re.findall(r'(.+)\s(\d+)\n', content)
                dict_info = dict((key, int(value)) for key, value in info)
                return dict_info
        except FileNotFoundError:
            print("There is no file for scores.")

        return {}

    def write_scores(self, out):
        try:
            with open('scores.txt', 'w') as file:
                file.write(out)
        except FileNotFoundError:
            print("There is no file for scores.")

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
