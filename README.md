
# Django Browser Verification

Provides warning or lockout for outdated browsers


## Installation

install with pip `pip install django-browser-verification`

Use the mixin in your views:

    class TestView(BrowserVerificationMixin, TemplateView):
        ...

You can override `unsupported_browser` and `unknown_browser` to customize
what you want to do with those users.

By default it will do nothing other than setting the `user_agent` on the request
along with `browser_unsupported` and `browser_unknown`.

You can customize a warning message in the template.

## Middleware

Add `browser_verification` to the INSTALLED_APPS setting in your settings file.

ADD 'BrowserVerificationMiddleware` to your MIDDLEWARE_CLASSES setting,
probably dosen't really matter where.

It will just tag the request with user agent information and provide you with
support information as documented above

## testing

this app uses tox for testing: ```tox```
