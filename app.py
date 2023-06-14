from flask import Flask, render_template, request
import pyodbc


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#    # Set up the connection parameters
#    server = 'your_server_name'
#    database = 'SolarSystem'
#    username = 'sa'
#    password = 'Kode1234!'
#
#    # Create a connection string
#    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
#
#    try:
#        # Establish a connection
#        connection = pyodbc.connect(connection_string)
#
#        # Create a cursor to execute queries
#        cursor = connection.cursor()
#
#        # Execute the query to fetch data from the "planets" and "Texts" tables
#        query = '''
#            SELECT ImagePath, DanishText, EnglishText, EstonianText
#            FROM planets
#            JOIN Texts ON TextId = Texts.id
#        '''
#        cursor.execute(query)
#
#        # Fetch all the rows
#        rows = cursor.fetchall()
#
#        # Get the selected language from the request parameters
#        selected_language = request.args.get('language', 'danish')  # Default to Danish if no language is selected
#
#        # Create a list to hold the generated image and text elements
#        elements = []
#
#        # Iterate over the rows and generate image and text elements
#        for row in rows:
#            # Extract the relevant data from the row
#            image_path = row.ImagePath
#            danish_text = row.DanishText
#            english_text = row.EnglishText
#            estonian_text = row.EstonianText
#
#            # Get the text based on the selected language
#            if selected_language == 'danish':
#                text = danish_text
#            elif selected_language == 'english':
#                text = english_text
#            elif selected_language == 'estonian':
#                text = estonian_text
#            else:
#                text = danish_text  # Default to Danish if an invalid language is selected
#
#            # Create a new HTML image element with the image path
#            img_element = f'<img src="{image_path}" alt="{text}" width="200" height="200">'
#
#            # Create a new HTML text element with the selected language text
#            text_element = f'<p>{selected_language.capitalize()}: {text}</p>'
#
#            # Append the image and text elements to the list
#            elements.append((img_element, text_element))
#
#        # Close the cursor and the connection
#        cursor.close()
#        connection.close()
#
#        # Render the template with the elements and the selected language
#        return render_template('index.html', elements=elements, selected_language=selected_language)
#
#    except pyodbc.Error as e:
#        print(f"Error connecting to SQL Server: {e}")

@app.route('/Home')
def Home():
    return render_template('index.html')

@app.route('/Game')
def Game():
    return render_template('Game.html')

@app.route('/Planets')
def Planets():
    return render_template('Planets.html')

@app.route('/Galaxies')
def Galaxies():
    return render_template('Galaxies.html')

@app.route('/Comets')
def Comets():
    return render_template('Comets.html')




if __name__ == '__main__':
    app.run()