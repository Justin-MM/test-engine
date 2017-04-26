class TestCategory(object):
    def __init__(self, name):
        self.name = name
        self.questions_list = [] # each category has a question(s)

class Question(object):
    def __init__(self, question_string):
        self.question_string = question_string

        # each question has a correct answer(s) and wrong answers
        self.correct_answers = []
        self.dummy_answers = []


class TestEngine(TestCategory, Question):
    def __init__(self):
        self.test_categories = []   # this list is an array of test categories objects. Each object has question objects

    # add one or more test categories
    def add_category(self, *args):

        user_input = list(args)
        # create an instance of TestCategory
        for category in user_input:
            category = TestCategory(category)

            # check to see if a category by that name exists
            category_name = category.name
            if self.check_if_a_category_exists(category_name) is True:
                print("Test category {} already exists!".format(category.name))

            # if it does not exist create it
            else:
                self.test_categories.append(category)
                print("Test category {} successfully created!".format(category.name))

    def check_if_a_category_exists(self, category_name):
        # check to see if a category by that name exists
        check_list = [obj.name for obj in self.test_categories if len(self.test_categories) > 0]
        if category_name in check_list:
            return True
        else:
            return False

    # show the user the test categories they have created
    def show_created_categories(self):
        if self.test_categories == []:
            return "You have not created any categories. Create a category to continue"
        else:
            available_categories = [obj.name for obj in self.test_categories if len(self.test_categories) > 0]
            return available_categories

    def show_questions_in_a_category(self, category):
        # check if that category exists
        if self.check_if_a_category_exists(category) is True:
            for obj in self.test_categories:
                if category == obj.name:
                    # if there are no questions to show
                    if obj.questions_list == []:
                        print("There are no questions to show")
                    else:
                        temp_questions_list = [questions_obj.question_string for questions_obj in obj.questions_list]
                        return temp_questions_list
        else:
            return "Sorry! That category does not exist."

    # add a question. One at a time
    def add_question(self, category, *question_string):
        # create an object of type Question
        question_string = " ".join(list(question_string))
        question = Question(question_string)

        # append to questions list if the category exists
        if self.check_if_a_category_exists(category) is True:
            # check if a similar question exists
            if self.check_if_a_question_already_exists(category, question.question_string) is True:
                return("A similarly worded question already exists!! Consider making another question")
            else:
                # if it does not exist, append it
                for obj in self.test_categories:
                    if category == obj.name: # make sure we are adding to the correct category
                        obj.questions_list.append(question)
        else:
            return "Cannot add questions to a category that doesn't exist"

    def check_if_a_question_already_exists(self, category, check_string):
        # check if the category exist first
        if self.check_if_a_category_exists(category) is True:
            for obj in self.test_categories:
                if category == obj.name:
                    # make a list of available questions
                    available_questions = [question.question_string for question in obj.questions_list if len(obj.questions_list) > 0]
                    if check_string in available_questions:
                        return True
                    else:
                        return False
        else:
            return "questions cannot exist in a category that doesn't exist"




    def add_answer(self):
        pass

    def take_quiz(self):
        pass

    def track_test_progress(self):
        pass


class TestResults(TestEngine):

    def show_graph(self):
        pass

    def track_improvement(self):
        pass

