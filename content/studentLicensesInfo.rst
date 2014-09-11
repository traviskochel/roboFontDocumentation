.. _studentLicensesInfo:

Student Licenses Info
=====================

Only professors/teachers can apply for student licenses.

If you want to apply for student licenses it is required to provide a little bit of info about the course.

RoboFont is not distributed to individual students.

.. raw:: html

    <form method="post" action="http://tools.robofont.com/roboForms.php"  id="contactForm" class="cleanForm">
        <input type="hidden" name="returnURL" value="">
        <fieldset>
            <label>Name <em>*</em></label>
            <input type="text" name="name" required>

            <label>Your e-mail address<em>*</em></label>
            <input type="email" name="email" required>

            <input type="hidden" name="presubject" value="RoboFont Student License Request">

            <label>Name of the school<em>*</em></label>
            <input type="text" name="Name of the school" required>

            <label>Address of the school<em>*</em></label>
            <textarea name="Address of the school" required></textarea>

            <label>URL of the school<em>*</em></label>
            <input type="url" name="URL of the school" required>

            <label>URL of the course<em>*</em></label>
            <input type="url" name="URL of the course" required>

            <label>Number of students<em>*</em></label>
            <input type="number" name="Number of students" required>

            <label>Grade<em>*</em></label>
            <input type="text" name="Grade" required>

            <label>Some info about the teachers, links, names, … <em>*</em></label>
            <textarea name="Info" required></textarea>

            <label>Type 'MAPSON' reversed <em>*</em></label>
            <input type="text" name="gotit" required>

            <input type="submit" id="formSend" value=" Send ">
        </fieldset>
    </form>
    <script type="text/javascript" src="http://ajax.aspnetcdn.com/ajax/jquery.validate/1.13.0/jquery.validate.min.js"></script>
    <script>
        $("#contactForm").validate();
        $("#contactForm input[returnURL]").val(location.pathname.substring(0, location.pathname.lastIndexOf('/'))+'/thanks.html');
    </script>