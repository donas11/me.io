import pandas as pd

#Variables del conjunto global del archivo HTML
metas ="""
<meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link
            rel="stylesheet"
            href="https://www.w3schools.com/w3css/4/w3.css"
        />
        <link
            rel="stylesheet"
            href="https://fonts.googleapis.com/css?family=Roboto"
        />
        <link
            rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        />
"""
stylo ="""
<style>
            html,
            body,
            h1,
            h2 {
                color: whitesmoke;
            }
            ,
            h3,
            h4,
            h5,
            h6 {
                font-family: "Roboto", sans-serif;
            }
        </style>
"""

titulo ="<title>Alejandro Manuel do Nascimento Rodríguez - Curriculum Vitae </title>"

head = "<head>"+titulo+"<!-- Template adapted from W3Schools.com -->"+ metas + stylo +"</head>"

imagen="""
<img src="./foto-perfil-banner.jpeg" style="width: 100%" alt="Avatar"/>
"""

nombre_cabecera="<h2>Alejandro Manuel do Nascimento Rodríguez</h2>"

description_jobs="""
Computer Engineer | Software Development |
Devops Junior
"""

place="Granada, Spain"

email="amdnrdevops@gmail.com"

skills="""
<p>Docker</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 80%"
    >
        80%
    </div>
</div>
<p>Git-hub</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 75%"
    >
        75%
    </div>
</div>
<p>Python</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 65%"
    >
        65%
    </div>
</div>
<p>HTML/CSS/Javascript</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 50%"
    >
        50%
    </div>
</div>
<p>Kubernetes</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 35%"
    >
        <div class="w3-center w3-text-white">
            35%
        </div>
    </div>
</div>
<p>Terraform</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 10%"
    >
        <div class="w3-center w3-text-white">
            10%
        </div>
    </div>
</div>
<p>AWS</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 5%"
    >
        <div class="w3-center w3-text-white">
            5%
        </div>
    </div>
</div>
<p>Mongo-DB</p>
<div class="w3-light-grey w3-round-xlarge w3-small">
    <div
        class="w3-container w3-center w3-round-xlarge w3-teal"
        style="width: 5%"
    >
        <div class="w3-center w3-text-white">
            5%
        </div>
    </div>
</div>
"""

languages="""
<p>Spanish</p>
<div class="w3-light-grey w3-round-xlarge">
    <div
        class="w3-round-xlarge w3-teal"
        style="height: 24px; width: 100%"
    ></div>
</div>
<p>English</p>
<div class="w3-light-grey w3-round-xlarge">
    <div
        class="w3-round-xlarge w3-teal"
        style="height: 24px; width: 40%"
    ></div>
</div>
"""

left_column="""
<!-- Left Column -->
                <div class="w3-third">
                    <div class="w3-white w3-text-grey w3-card-4">
                        <div class="w3-display-container">
                            """ +imagen+"""
                            <div
                                class="w3-display-bottomleft w3-container w3-text-black">
                                """+nombre_cabecera+"""
                            </div>
                        </div>
                        <div class="w3-container">
                            <p>
                                <i
                                    class="fa fa-briefcase fa-fw w3-margin-right w3-large w3-text-teal"
                                ></i>
                                """+description_jobs+"""
                            </p>
                            <p>
                                <i
                                    class="fa fa-home fa-fw w3-margin-right w3-large w3-text-teal"
                                ></i
                                >"""+place+"""
                            </p>
                            <p>
                                <i
                                    class="fa fa-envelope fa-fw w3-margin-right w3-large w3-text-teal"
                                ></i
                                >"""+email+"""
                            </p>
                            <hr />

                            <p class="w3-large">
                                <b
                                    ><i
                                        class="fa fa-asterisk fa-fw w3-margin-right w3-text-teal"
                                    ></i
                                    >Skills</b
                                >
                            </p>
                            """+skills+"""
                            <br />

                            <p class="w3-large w3-text-theme">
                                <b
                                    ><i
                                        class="fa fa-globe fa-fw w3-margin-right w3-text-teal"
                                    ></i
                                    >Languages</b
                                >
                            </p>"""+languages+"""
                            <br />
                        </div>
                    </div>
                    <br />

                    <!-- End Left Column -->
                </div>
"""

data_projects = pd.read_csv('csvs/Projects.csv', delimiter=';')
data_projects.columns = data_projects.columns.str.strip()
projects=""
for _,row in data_projects.iterrows():
    title = row['Title']
    date = row['Time']
    description = row['Description']
    projects+=f"""
    <div class="w3-container">
            <h5 class="w3-opacity">
                <b
                    >"""+title+"""</b
                >
            </h5>
            <h6 class="w3-text-teal">
                <i
                    class="fa fa-calendar fa-fw w3-margin-right"
                ></i
                >"""+date+"""
            </h6>
            <p>
                """+description+"""
            </p>
            <hr />
        </div>
    """

project_experience="""
<div class="w3-container w3-card w3-white w3-margin-bottom">
    <h2 class="w3-text-grey w3-padding-16">
        <i
            class="fa fa-suitcase fa-fw w3-margin-right w3-xxlarge w3-text-teal"
        ></i
        >Project Experience
        """+projects+"""
    </h2>
    
</div>
"""


data_education = pd.read_csv('csvs/Education.csv', delimiter=';')
data_education.columns = data_education.columns.str.strip()
educations=""
for _, row in data_education.iterrows():
    title = row['Title']
    date = row['Time']
    description = row['Description']
    educations+=f"""
    <div class="w3-container">
        <h5 class="w3-opacity">
            <b> """+title+"""</b>
        </h5>
        <h6 class="w3-text-teal">
            <i
                class="fa fa-calendar fa-fw w3-margin-right"
            ></i>
            """+date+"""
        </h6>
        <p>"""+description+"""</p>
        <hr />
    </div>
    """

educations_exp="""<div class="w3-container w3-card w3-white">
    <h2 class="w3-text-grey w3-padding-16">
        <i
            class="fa fa-book fa-fw w3-margin-right w3-xxlarge w3-text-teal"
        ></i
        >Education
    </h2>
    """+educations+"""
</div>
"""


data_certifications = pd.read_csv('csvs/Certificates.csv', delimiter=';')
data_certifications.columns = data_certifications.columns.str.strip()
certifications=""
for _, row in data_certifications.iterrows():
    certifications+=f"""
    <div class="w3-container">
        <h5 class="w3-opacity">
            <a
                href="{row['Link']}"
            >
                <b>{row['Title']}</b
                >
            </a>
        </h5>
        <h6 class="w3-text-teal">
            <i
                class="fa fa-calendar fa-fw w3-margin-right"
            ></i>
            {row['Date']}
        </h6>
        <hr />
    </div>
    """
certification_exp ="""
<div class="w3-container w3-card w3-white">
    <h2 class="w3-text-grey w3-padding-16">
        <i
            class="fa fa-certificate fa-fw w3-margin-right w3-xxlarge w3-text-teal"
        ></i
        >Certificates
    </h2>
    """+certifications+"""
    
 </div>
"""



data_courses = pd.read_csv('csvs/Courses.csv', delimiter=';')
data_courses.columns = data_courses.columns.str.strip()
courses=""
for _, row in data_courses.iterrows():
    courses+=f"""
    <div class="w3-container">
        <h5 class="w3-opacity">
            <a
                href="{row['Link']}"
                ><b> {row['Title']}</b></a
            >
        </h5>
        <h6 class="w3-text-teal">
            <i
                class="fa fa-calendar fa-fw w3-margin-right"
            ></i>
            {row['Date']}
        </h6>

        <hr />
    </div>
    """

courses_exp="""
<div class="w3-container w3-card w3-white">
    <h2 class="w3-text-grey w3-padding-16">
        <i
            class="fa fa-plus fa-fw w3-margin-right w3-xxlarge w3-text-teal"
        ></i
        >Courses
    </h2>
    """+courses+"""
</div>
"""

right_column="""
<!-- Right Column -->
<div class="w3-twothird"> 
"""+project_experience+educations_exp+certification_exp+courses_exp+"""
<!-- End Right Column -->
</div>
"""

footer="""
<footer class="w3-container w3-teal w3-center w3-margin-top">
            <p>Find me on social media.</p>
            <a href="https://www.linkedin.com/in/amdnr/">
                <i class="fa fa-linkedin w3-hover-opacity"></i
            ></a>
            <a href="https://github.com/donas11">
                <i class="fa fa-github w3-hover-opacity"></i
            ></a>
            <p>
                Powered by
                <a
                    href="https://www.w3schools.com/w3css/default.asp"
                    target="_blank"
                    >w3.css</a
                >
            </p>
        </footer>
"""

the_grid= """
<!-- The Grid -->
<div class="w3-row-padding">
"""+left_column + right_column +"""

 <!-- End Grid -->
</div>
"""

page_container="""
<!-- Page Container -->
        <div class="w3-content w3-margin-top" style="max-width: 1400px">
        """+ the_grid +"""
<!-- End Page Container -->
        </div>

"""

body ="""
<body class="w3-light-grey">
"""+page_container +footer+"""
</body>
"""




html= "<!doctype html><html> "+ head + body +"</html>"

with open('./index.html', 'w') as f:
    f.write(html)