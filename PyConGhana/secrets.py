
SECRET_KEY = '@pspnupf89kwcp0*=c=&&etw2=_r!&(_um=+xgfp=jv^o*@%4q'

RECAPTCHA_PRIVATE_KEY = '6Ldbq1IUAAAAABhyiq30Ur9ySQgsM_Mnc7rNk3Y7'
RECAPTCHA_PUBLIC_KEY = '6Ldbq1IUAAAAAGLKryi-oZs8tE1D4DAXQx6hFzAf' 

#SENDGRID_API_KEY =  os.path.join["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"]

# Django Email configuration
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = "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"
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
DEFAULT_FROM_EMAIL = 'PyCon Ghana <noreply@gh.pycon.org>'

