from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import gzip

app = Flask(__name__)
model = pickle.load(gzip.open("Model.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Hospital_region_code -----------------------------------------------------------------------------------

        hrc = request.form['Hospital_region_code']
        
        hrc_Y = hrc_Z = 0

        if(hrc == 'Y'):
            hrc_Y = 1

        elif(hrc == 'Z'):
            hrc_Z = 1


        # City_Code_Hospital ---------------------------------------------------------------------------------------

        cch = request.form['City_Code_Hospital']
        
        cch_2 = cch_3 = cch_4 = cch_5 = cch_6 = cch_7 = cch_9 = cch_10 = cch_11 = cch_13 = 0

        if(cch == '2'):
            cch_2 = 1

        elif(cch == '3'):
            cch_3 = 1   

        elif(cch == '4'):
            cch_4 = 1
           
        elif(cch == '5'):
            cch_5 = 1    

        elif(cch == '6'):
            cch_6 = 1
            
        elif(cch == '7'):
            cch_7 = 1     

        elif(cch == '9'):
            cch_9 = 1            

        elif(cch == '10'):
            cch_10 = 1
           
        elif(cch == '11'):
            cch_11 = 1
          
        elif(cch == '13'):
            cch_13 = 1
           

        # Hospital_code --------------------------------------------------------------------------------

        hc = request.form['Hospital_code']
        
        hc_2 = hc_3 = hc_4 = hc_5 = hc_6 = hc_7 = hc_8 = hc_9 = hc_10 = hc_11 = hc_12 = hc_13 = hc_14 = hc_15 = hc_16 = hc_17 = hc_18 =     hc_19 = hc_20 = hc_21 = hc_22 = hc_23 = hc_24 = hc_25 = hc_26 = hc_27 = hc_28 = hc_29 = hc_30 = hc_31 = hc_32 = 0

        if (hc == '2'):
            hc_2 = 1

        elif (hc == '3'):
            hc_3 = 1
              
        elif (hc == '4'):
            hc_4 = 1
      
        elif (hc == '5'):
            hc_5 = 1
               
        elif (hc == '6'):
            hc_6 = 1
   
        elif (hc == '7'):
            hc_7 = 1

        elif (hc == '8'):
            hc_8 = 1
          
        elif (hc == '9'):
            hc_9 = 1
              
        elif (hc == '10'):
            hc_10 = 1
       
        elif (hc == '11'):
            hc_11 = 1
    
        elif (hc == '12'):
            hc_12 = 1
          
        elif (hc == '13'):
            hc_13 = 1

        elif (hc == '14'):
            hc_14 = 1

        elif (hc == '15'):
            hc_15 = 1
            
        elif (hc == '16'):
            hc_16 = 1

        elif (hc == '17'):
            hc_17 = 1
              
        elif (hc == '18'):
            hc_18 = 1
      
        elif (hc == '19'):
            hc_19 = 1
               
        elif (hc == '20'):
            hc_20 = 1
   
        elif (hc == '21'):
            hc_21 = 1

        elif (hc == '22'):
            hc_22 = 1
          
        elif (hc == '23'):
            hc_23 = 1
              
        elif (hc == '24'):
            hc_24 = 1
       
        elif (hc == '25'):
            hc_25 = 1
    
        elif (hc == '26'):
            hc_26 = 1
          
        elif (hc == '27'):
            hc_27 = 1
        
        elif (hc == '28'):
            hc_28 = 1

        elif (hc == '29'):
            hc_29 = 1
            
        elif (hc == '30'):
            hc_30 = 1
        
        elif (hc == '31'):
            hc_31 = 1

        elif (hc == '32'):
            hc_32 = 1
       
           
        # Hospital_type_code -----------------------------------------------------------------------------------

        htc = request.form['Hospital_type_code']
        
        htc_b = htc_c = htc_d = htc_e = htc_f = htc_g = 0

        if (htc == 'b'):
            htc_b = 1

        elif (htc == 'c'):
            htc_c = 1
           
        elif (htc == 'd'):
            htc_d = 1
           
        elif (htc == 'e'):
            htc_e = 1

        elif (htc == 'f'):
            htc_f = 1

        elif (htc == 'g'):
            htc_g = 1


        # City_code_patient -------------------------------------------------------------------------------

        ccp = request.form['City_Code_Patient']
        
        ccp_2 = ccp_3 = ccp_4 = ccp_5 = ccp_6 = ccp_7 = ccp_8 = ccp_9 = ccp_10 = ccp_11 = ccp_12 = ccp_13 = ccp_14 = ccp_15 = ccp_16 = ccp_18 = ccp_19 = ccp_20 = ccp_21 = ccp_22 = ccp_23 = ccp_24 = ccp_25 = ccp_26 = ccp_27 = ccp_28 = ccp_29 = ccp_30 = ccp_31 = ccp_32 = ccp_33 = ccp_34 = ccp_35 = ccp_36 = ccp_37 = ccp_38 = 0
        
        if (ccp == '2'):
            ccp_2 = 1

        elif (ccp == '3'):
            ccp_3 = 1
              
        elif (ccp == '4'):
            ccp_4 = 1
      
        elif (ccp == '5'):
            ccp_5 = 1
               
        elif (ccp == '6'):
            ccp_6 = 1
   
        elif (ccp == '7'):
            ccp_7 = 1

        elif (ccp == '8'):
            ccp_8 = 1
          
        elif (ccp == '9'):
            ccp_9 = 1
              
        elif (ccp == '10'):
            ccp_10 = 1
       
        elif (ccp == '11'):
            ccp_11 = 1
    
        elif (ccp == '12'):
            ccp_12 = 1
          
        elif (ccp == '13'):
            ccp_13 = 1

        elif (ccp == '14'):
            ccp_14 = 1

        elif (ccp == '15'):
            ccp_15 = 1
            
        elif (ccp == '16'):
            ccp_16 = 1
              
        elif (ccp == '18'):
            ccp_18 = 1
      
        elif (ccp == '19'):
            ccp_19 = 1
               
        elif (ccp == '20'):
            ccp_20 = 1
   
        elif (ccp == '21'):
            ccp_21 = 1

        elif (ccp == '22'):
            ccp_22 = 1
          
        elif (ccp == '23'):
            ccp_23 = 1
              
        elif (ccp == '24'):
            ccp_24 = 1
       
        elif (ccp == '25'):
            ccp_25 = 1
    
        elif (ccp == '26'):
            ccp_26 = 1
          
        elif (ccp == '27'):
            ccp_27 = 1
        
        elif (ccp == '28'):
            ccp_28 = 1

        elif (ccp == '29'):
            ccp_29 = 1
            
        elif (ccp == '30'):
            ccp_30 = 1
        
        elif (ccp == '31'):
            ccp_31 = 1

        elif (ccp == '32'):
            ccp_32 = 1
            
        elif (ccp == '33'):
            ccp_33 = 1
            
        elif (ccp == '34'):
            ccp_34 = 1
            
        elif (ccp == '35'):
            ccp_35 = 1
            
        elif (ccp == '36'):
            ccp_36 = 1
            
        elif (ccp == '37'):
            ccp_37 = 1
            
        elif (ccp == '38'):
            ccp_38 = 1
            
        
   
        # Department ---------------------------------------------------------------------------------------

        d = request.form['Department']
        
        d_anesthesia = d_gynecology = d_radiotherapy = d_surgery = 0

        if(d == 'anesthesia'):
            d_anesthesia = 1
           
        elif(d == 'gynecology'):
            d_gynecology = 1

        elif(d == 'radiotherapy'):
            d_radiotherapy = 1

        elif(d == 'surgery'):
            d_surgery = 1


        # Type of Admission ----------------------------------------------------------------------------------

        ta = request.form['Type_of_Admission']
        
        if (ta == 'Trauma'):
            ta = 1

        elif (ta == 'Urgent'):
            ta = 2

        elif (ta == 'Emergency'):
            ta = 3


        # Severity of Illness -------------------------------------------------------------------------------

        si = request.form['Severity_of_Illness']

        if (si == 'Minor'):
            si = 1

        elif (si == 'Moderate'):
            si = 2

        elif (si == 'Extreme'):
            si = 3


        # Ward type ------------------------------------------------------------------------------------------

        wt = request.form['Ward_Type']
        
        wt_Q = wt_R = wt_S = wt_T = wt_U = 0

        if(wt == 'Q'):
            wt_Q = 1

        elif(wt == 'R'):
            wt_R = 1

        elif(wt == 'S'):
            wt_S = 1         

        elif(wt == 'T'):
            wt_T = 1

        elif(wt == 'U'):
            wt_U = 1


        # Ward_Facility_Code ---------------------------------------------------------------------------------

        wfc = request.form['Ward_Facility_Code']
        
        wfc_B = wfc_C = wfc_D = wfc_E = wfc_F = 0

        if(wfc == 'B'):
            wfc_B = 1

        elif(wfc == 'C'):
            wfc_C = 1

        elif(wfc == 'D'):
            wfc_D = 1

        elif(wfc == 'E'):
            wfc_E = 1

        elif(wfc == 'F'):
            wfc_F = 1


        # Bed Grade --------------------------------------------------------------------------------
        
        bg = request.form['Bed_Grade']

        bg_2 =  bg_3 = bg_4 = 0
        
        if(bg == '2'):
            bg_2 = 1

        elif(bg == '3'):
            bg_3 = 1

        elif(bg == '4'):
            bg_4 = 1


        # Age -------------------------------------------------------------------------------

        age = request.form['Age']

        if (age == '0-10'):
            age = 10

        elif (age == '11-20'):
            age = 20

        elif (age == '21-30'):
            age = 30

        elif (age == '31-40'):
            age = 40

        elif (age == '41-50'):
            age = 50

        elif (age == '51-60'):
            age = 60

        elif (age == '61-70'):
            age = 70

        elif (age == '71-80'):
            age = 80

        elif (age == '81-90'):
            age = 90

        elif (age == '91-100'):
            age = 100


        # Numerical Columns ------------------------------------------------------------------------------

        Available_Extra_Rooms = int(request.form["Available_Extra_Rooms"])
        Visitors_with_Patient = int(request.form["Visitors_with_Patient"])
        Admission_Deposit     = int(request.form["Admission_Deposit"])


        # Prediction -------------------------------------------------------------------------------------

        prediction = model.predict([[
            Available_Extra_Rooms,
            ta,
            si,
            Visitors_with_Patient,
            Admission_Deposit,
            age,
            hc_2,hc_3,hc_4,hc_5,hc_6,hc_7,hc_8,hc_9,hc_10,hc_11,hc_12,hc_13,hc_14,hc_15,hc_16,hc_17,hc_18,hc_19,hc_20,hc_21,hc_22,hc_23,hc_24,hc_25,hc_26,hc_27,hc_28,hc_29,hc_30,hc_31,hc_32,
            htc_b,htc_c,htc_d,htc_e,htc_f,htc_g,
            cch_2,cch_3,cch_4,cch_5,cch_6,cch_7,cch_9,cch_10,cch_11,cch_13,
            hrc_Y,hrc_Z,
            d_anesthesia,d_gynecology,d_radiotherapy,d_surgery,
            wt_Q,wt_R,wt_S,wt_T,wt_U,
            wfc_B,wfc_C,wfc_D,wfc_E,wfc_F,
            ccp_2,ccp_3,ccp_4,ccp_5,ccp_6,ccp_7,ccp_8,ccp_9,ccp_10,ccp_11,ccp_12,ccp_13,ccp_14,ccp_15,ccp_16,ccp_18,ccp_19,ccp_20,ccp_21,ccp_22,ccp_23,ccp_24,ccp_25,ccp_26,ccp_27,ccp_28,ccp_29,ccp_30,ccp_31,ccp_32,ccp_33,ccp_34,ccp_35,ccp_36,ccp_37,ccp_38,
            bg_2,bg_3,bg_4
        ]])
    
    
        if (prediction==1):
            output = '0-10'
        elif (prediction==2):
            output = '11-20'
        elif (prediction==3):
            output = '21-30'
        elif (prediction==4):
            output = '31-40'
        elif (prediction==5):
            output = '41-50'
        elif (prediction==6):
            output = '51-60'
        elif (prediction==7):
            output = '61-70'
        elif (prediction==8):
            output = '71-80'
        elif (prediction==9):
            output = '81-90'
        elif (prediction==10):
            output = '91-100'
        elif (prediction==11):
            output = '100+'
            
        return render_template('result.html', prediction_text="LOS = {} days".format(output))

    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
