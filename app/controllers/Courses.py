from system.core.controller import *
class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
    # Note that we have to load the model before using it
        self.load_model('Course')

    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses=courses)

    # This is how a method with a route parameter that provides the id would work
    # We would set up a GET route for this method
    def show(self, id):
    # Note how we access the model using self.models
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('show.html', course=course)

    # This is how a method used to add a course would look
    # We would set up a POST route for this method
    def add(self):
    # in actuality, data for the new course would come 
    # from a form on our client
        course = {
        'title': request.form['title'],
        'description': request.form['description']
        }
        valid = self.models['Course'].add_course(course)
    # flash
        if valid == False:
            flash('your course is invalid. please enter at least 15 characters.')
        return redirect('/')

    # This is how a method used to update a course would look
    # We would set up a POST route for this method
    def update(self, course_id):
    # in actuality, data for updating the course would come 
    # from a form on our client
        course_details = {
        'id': course_id,
        'title': 'Python 2.0',
        'description': 'This course is unreal!'
        }
        self.models['Course'].update_course(course_details)
        return redirect('/')

    def destroy(self,course_id):
        course = self.models['Course'].get_course_by_id(course_id)
        return self.load_view('destroy.html', course=course)

    # This is how a method used to delete a course would look
    # We would set up a POST route for this method
    def delete(self, course_id):
        self.models['Course'].delete_course(course_id)
        return redirect('/')
