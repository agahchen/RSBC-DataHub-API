from python.common.rsi_email import get_jinja2_env, get_email_content
import pytest


def test_admin_notice_method():
    template = get_jinja2_env().get_template('admin_notice.html')
    body = 'Here is something you should know.'
    title = "Error: Unknown event type"
    html = template.render(subject=title,
                           body=body)
    print(html)
    assert body in html
    assert title in html


def test_application_accepted():
    template = get_jinja2_env().get_template('application_accepted.html')
    full_name = 'Bob Smith'
    number = "201234567"
    subject = "Application received"
    html = template.render(subject=subject,
                           full_name=full_name,
                           prohibition_number=number)
    print(html)
    assert full_name in html
    assert subject in html
    assert number in html
    assert "You must <strong>not</strong> drive" in html
    assert "Please do not respond to this email" in html


def test_schedule_review_email():
    template = get_jinja2_env().get_template('select_review_date.html')
    full_name = 'Bob Smith'
    number = "201234567"
    subject = "Re: Driving Prohibition Review - Select a Review Date {}".format(number)
    html = template.render(subject=subject,
                           full_name=full_name,
                           prohibition_number=number)
    print(html)
    assert "To select a date for your driving prohibition review" in html
    assert full_name in html
    assert subject in html
    assert number in html
    assert "Please do not respond to this email" in html


template_names = [
    ("last_name_mismatch.html", "Prohibition Number or Name Don't Match - Driving Prohibition Review 9999"),
    ('template_does_not_exist.html', "Unknown template")
]


@pytest.mark.parametrize("template_name, subject_string", template_names)
def test_get_email_content(template_name, subject_string):
    content = get_email_content(template_name, '9999')
    assert content['subject'] == subject_string
