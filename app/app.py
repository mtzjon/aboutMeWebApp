from dash import Dash, html, dcc, callback, Output, Input


class App(Dash):
    def __init__(self):
        super(App, self).__init__()

        #self._favicon = '.png'
        self.title = 'Home'

        self.layout = self.__init_layout__()
        self.__init_callbacks__()
        self.run_server(debug=True, port=5000)

    def __init_layout__(self):
        return html.Div([
            dcc.Location(id='url'),
            html.Div([
                html.Div([
                    html.Div([
                        html.A('Jon Mart{}nez de Aguirre Yeregui'.format(b'\xc3\xad'.decode()), href='/', className='nav-link logo'),
                        ], className='left-aligned'),
                    html.Div([
                        html.A('Home', href='/', id='home-link', className='nav-link nav-item'),
                        html.A('Experience', href='/experience', id='experience-link', className='nav-link nav-item'),
                        html.A('Contact', href='/contact', id='contact-link', className='nav-link nav-item'),
                        ], className='right-aligned'),
                    ], className='nav-content')
                ], className='nav-bar'),
            html.Div(id='content'),
            ]
        )

    def __init_callbacks__(self):
        @callback(
            [Output('home-link', 'className'),
             Output('experience-link', 'className'),
             Output('contact-link', 'className'),],
            Input('url', 'pathname'),)
        def toggle_nav_underline(path):
            active = 'nav-link nav-item active-url'
            inactive = 'nav-link nav-item'

            if path == '/':
                return active, inactive, inactive
            if path == '/experience':
                return inactive, active, inactive
            if path == '/contact':
                return inactive, inactive, active
            return inactive, inactive, inactive

        @callback(
            Output('content', 'children'),
            Input('url', 'pathname'),)
        def toggle_page_content(path):
            if path == '/':
                return self.home_children()
            if path == '/me':
                return self.about_me_children()
            if path == '/contact':
                return self.contact_children()
            return ['Error 404: Not found.']

    def home_children(self):
        return [
            html.Div([
                html.H2('About me'),
                html.P('Hello, my name is Jon.'),
                ], className='first container')
        ]

    def about_me_children(self):
        return []

    def contact_children(self):
        return []

if __name__ == "__main__":
    App()
    

