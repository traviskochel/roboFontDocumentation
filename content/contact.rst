.. _contact:

Contact
=======

Get in touch, we will reply as soon as possible.

.. raw:: html

    <form method="post" action="http://tools.robofont.com/roboForms.php"  id="contactForm" class="cleanForm">
        <input type="hidden" name="returnURL" value="">
        <fieldset>
            <label>Name <em>*</em></label>
            <input type="text" name="name" required>

            <label>Your e-mail address<em>*</em></label>
            <input type="email" name="email" required>

            <label>Subject <em>*</em></label>
            <input type="text" name="subject" required>
            <input type="hidden" name="presubject" value="[RoboFont Contact]">

            <label>Message <em>*</em></label>
            <textarea name="body" required></textarea>

            <label>Type 'MAPSON' reversed <em>*</em></label>
            <input type="text" name="gotit" required>

            <input type="submit" id="formSend" value=" Send ">
        </fieldset>
    </form>
    <script type="text/javascript" src="http://ajax.aspnetcdn.com/ajax/jquery.validate/1.13.0/jquery.validate.min.js"></script>
    <script>
        $("#contactForm").validate();
        $("#contactForm input[name='returnURL']").val(location.pathname.substring(0, location.pathname.lastIndexOf('/'))+'/thanks.html');
    </script>