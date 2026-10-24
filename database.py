import mysql.connector
conn = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password ="Sql123.,!",
   database = "quizz_db"  
)
cursor = conn.cursor()
def save_score(name,score,total,grade,percentage):
    sql = ("""INSERT INTO student_scores(student_name,score,total_questions,grade,percentage)VALUES(%s,%s,%s,%s,%s)""")
    values = (name,score,total,grade,percentage)
    cursor.execute(sql,values)
    conn.commit()
    print("score saved successfully successfully")