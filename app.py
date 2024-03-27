from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
    {
        "job_title":" Software Engineer",

        "job_desc":"Seeking a skilled software engineer proficient in multiple programming languages to develop innovative software solutions, collaborate with cross-functional teams, and contribute to the full software development lifecycle.",

        "location":"Delhi,India",

        "salary": "Rs.12,00,000",

        "skills":"Proficiency in programming languages like Java, Python, or JavaScript; experience with web development frameworks like React or Angular; strong problem-solving skills.",
        "card_img":"https://images.pexels.com/photos/3861958/pexels-photo-3861958.jpeg?auto=compress&cs=tinysrgb&w=600"
    },
    {
    "job_title": "Digital Marketing Specialist",
    "job_desc": "We are looking for a digital marketing specialist to plan and execute digital marketing campaigns across various channels, analyze campaign performance, and optimize strategies for maximum ROI.",
    "location": "Mumbai, India",
    "salary": "Rs. 9,00,000",
    "skills": "Proficiency in SEO, SEM, social media marketing; experience with tools like Google Analytics, Facebook Ads Manager; strong analytical and communication skills.",
    "card_img":"https://images.pexels.com/photos/905163/pexels-photo-905163.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
},
{
    "job_title": "UX/UI Designer",
    "job_desc": "Join our team as a UX/UI designer to create intuitive and visually appealing user interfaces, conduct user research, and collaborate with cross-functional teams to deliver exceptional user experiences.",
    "location": "Bangalore, India",
    "salary": "Rs. 8,00,000",
    "skills": "Proficiency in design tools like Adobe XD, Sketch, or Figma; understanding of UX principles and best practices; strong creativity and attention to detail.",
    "card_img":"https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
},
{
    "job_title": "Data Analyst",
    "job_desc": "We are hiring a data analyst to analyze complex datasets, develop and maintain dashboards and reports, and provide actionable insights to drive business decisions.",
    "location": "Hyderabad, India",
    "salary": "Rs. 10,00,000",
    "skills": "Proficiency in SQL, Excel, or Python for data manipulation and analysis; experience with data visualization tools like Tableau or Power BI; strong analytical and problem-solving skills.",
    "card_img":"https://images.pexels.com/photos/590022/pexels-photo-590022.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
},
{
    "job_title": "Content Writer",
    "job_desc": "We are seeking a talented content writer to produce high-quality content for blogs, websites, and social media platforms, conduct thorough research, and collaborate with the marketing team to create engaging content.",
    "location": "Pune, India",
    "salary": "Rs. 6,00,000",
    "skills": "Excellent writing and editing skills; proficiency in SEO writing; ability to conduct thorough research and adapt writing style based on target audience.",
    "card_img":"https://images.pexels.com/photos/4126743/pexels-photo-4126743.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
},
{
    "job_title": "Network Administrator",
    "job_desc": "We are in need of a skilled network administrator to maintain and configure our organization's network infrastructure, troubleshoot network issues, and ensure network security and reliability.",
    "location": "Chennai, India",
    "salary": "Rs. 7,50,000",
    "skills": "Experience with network protocols and technologies such as TCP/IP, DNS, DHCP, VPN; proficiency in network hardware configuration and troubleshooting; knowledge of network security best practices.",
    "card_img":"https://images.pexels.com/photos/3756679/pexels-photo-3756679.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
}


    
]
@app.route("/")
def home():
    return render_template("home.html",jobs=JOBS)

@app.route("/about")
def about_us():
    return render_template("about.html")

if __name__== "__main__":
    app.run(host="0.0.0.0",debug=True)