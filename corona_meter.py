from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import requests
import time
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def mainpage():
    l = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
         'Chhattisgarh', 'Delhi', 'Dadra and Nagar Haveli and Daman and Diu', 'Goa', 'Gujarat', 'Himachal Pradesh',
         'Haryana', 'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra',
         'Meghalaya', 'Manipur', 'Madhya Pradesh', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Puducherry', 'Rajasthan',
         'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
    return render_template("home.html",l=l)
@app.route("/analysis",methods=['GET','POST'])
def analysis():
    try:
        State=request.form.get("state")
        City=request.form.get("city")
        Data=requests.get("https://api.covid19india.org/state_district_wise.json")
        Json_data=Data.json()
        State=State.title().strip()
        City=City.title().strip()
        x=Json_data[State]['districtData'][City]
        timestr=time.strftime("%Y%m%d-%H%M%S")
        s = {}
        s['Active'] = x['active']
        confirmed = x['confirmed']
        s['Deaths'] = x['deceased']
        s['Recovered'] = x['recovered']
        new_confirmed=x['delta']['confirmed']
        new_recovered=x['delta']['recovered']
        new_deaths=x['delta']['deceased']
        Active = s['Active']
        Deaths = s['Deaths']
        Recovered = s['Recovered']
        fig, ax = plt.subplots()
        ax.pie(s.values(),labels=s.keys(),autopct='%1.5f%%')
        plt.title(f"{City} Corona Meter")
        fig.autofmt_xdate()
        plt.savefig("/home/abhinav/PycharmProjects/Corona_meter/static/"+timestr+".png")
        return render_template("page2.html",Active=Active,Confirmed=confirmed,Deaths=Deaths,Recovered=Recovered,City=City,new_recovered=new_recovered,new_confirmed=new_confirmed,new_deaths=new_deaths,Pic=timestr)
    except:
        return render_template("error.html")

@app.route("/guide")
def guide():
        l=['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Delhi', 'Dadra and Nagar Haveli and Daman and Diu', 'Goa', 'Gujarat', 'Himachal Pradesh', 'Haryana', 'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra', 'Meghalaya', 'Manipur', 'Madhya Pradesh', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Puducherry', 'Rajasthan', 'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
        kl = [['Nicobars', 'North and Middle Andaman', 'South Andaman', 'Unknown'],
              ['Foreign Evacuees', 'Anantapur', 'Chittoor', 'East Godavari', 'Guntur', 'Krishna', 'Kurnool',
               'Other State', 'Prakasam', 'S.P.S. Nellore', 'Srikakulam', 'Visakhapatnam', 'Vizianagaram',
               'West Godavari', 'Y.S.R. Kadapa'],
              ['Anjaw', 'Changlang', 'East Kameng', 'East Siang', 'Kamle', 'Kra Daadi', 'Kurung Kumey', 'Lepa Rada',
               'Lohit', 'Longding', 'Lower Dibang Valley', 'Lower Siang', 'Lower Subansiri', 'Namsai', 'Pakke Kessang',
               'Papum Pare', 'Shi Yomi', 'Siang', 'Tawang', 'Tirap', 'Upper Dibang Valley', 'Upper Siang',
               'Upper Subansiri', 'West Kameng', 'West Siang'],
              ['Baksa', 'Barpeta', 'Biswanath', 'Bongaigaon', 'Cachar', 'Charaideo', 'Chirang', 'Darrang', 'Dhemaji',
               'Dhubri', 'Dibrugarh', 'Dima Hasao', 'Goalpara', 'Golaghat', 'Hailakandi', 'Hojai', 'Jorhat', 'Kamrup',
               'Kamrup Metropolitan', 'Karbi Anglong', 'Karimganj', 'Kokrajhar', 'Lakhimpur', 'Majuli', 'Morigaon',
               'Nagaon', 'Nalbari', 'Other State', 'Sivasagar', 'Sonitpur', 'South Salmara Mankachar', 'Tinsukia',
               'Udalguri', 'West Karbi Anglong', 'Unknown'],
              ['Araria', 'Arwal', 'Aurangabad', 'Banka', 'Begusarai', 'Bhagalpur', 'Bhojpur', 'Buxar', 'Darbhanga',
               'East Champaran', 'Gaya', 'Gopalganj', 'Jamui', 'Jehanabad', 'Kaimur', 'Katihar', 'Khagaria',
               'Kishanganj', 'Lakhisarai', 'Madhepura', 'Madhubani', 'Munger', 'Muzaffarpur', 'Nalanda', 'Nawada',
               'Patna', 'Purnia', 'Rohtas', 'Saharsa', 'Samastipur', 'Saran', 'Sheikhpura', 'Sheohar', 'Sitamarhi',
               'Siwan', 'Supaul', 'Vaishali', 'West Champaran'], ['Chandigarh'],
              ['Other State', 'Balod', 'Baloda Bazar', 'Balrampur', 'Bametara', 'Bastar', 'Bijapur', 'Bilaspur',
               'Dakshin Bastar Dantewada', 'Dhamtari', 'Durg', 'Gariaband', 'Janjgir Champa', 'Jashpur', 'Kabeerdham',
               'Kondagaon', 'Korba', 'Koriya', 'Mahasamund', 'Mungeli', 'Narayanpur', 'Raigarh', 'Raipur',
               'Rajnandgaon', 'Sukma', 'Surajpur', 'Surguja', 'Uttar Bastar Kanker', 'Gaurela Pendra Marwahi'],
              ['Central Delhi', 'East Delhi', 'New Delhi', 'North Delhi', 'North East Delhi', 'North West Delhi',
               'Shahdara', 'South Delhi', 'South East Delhi', 'South West Delhi', 'West Delhi', 'Unknown'],
              ['Dadra and Nagar Haveli', 'Daman', 'Diu'], ['North Goa', 'South Goa', 'Unknown'],
              ['Other State', 'Ahmedabad', 'Amreli', 'Anand', 'Aravalli', 'Banaskantha', 'Bharuch', 'Bhavnagar',
               'Botad', 'Chhota Udaipur', 'Dahod', 'Dang', 'Devbhumi Dwarka', 'Gandhinagar', 'Gir Somnath', 'Jamnagar',
               'Junagadh', 'Kheda', 'Kutch', 'Mahisagar', 'Mehsana', 'Morbi', 'Narmada', 'Navsari', 'Panchmahal',
               'Patan', 'Porbandar', 'Rajkot', 'Sabarkantha', 'Surat', 'Surendranagar', 'Tapi', 'Vadodara', 'Valsad'],
              ['Bilaspur', 'Chamba', 'Hamirpur', 'Kangra', 'Kinnaur', 'Kullu', 'Lahaul and Spiti', 'Mandi', 'Shimla',
               'Sirmaur', 'Solan', 'Una'],
              ['Foreign Evacuees', 'Ambala', 'Bhiwani', 'Charkhi Dadri', 'Faridabad', 'Fatehabad', 'Gurugram', 'Hisar',
               'Italians', 'Jhajjar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Mahendragarh', 'Nuh', 'Palwal',
               'Panchkula', 'Panipat', 'Rewari', 'Rohtak', 'Sirsa', 'Sonipat', 'Yamunanagar'],
              ['Bokaro', 'Chatra', 'Deoghar', 'Dhanbad', 'Dumka', 'East Singhbhum', 'Garhwa', 'Giridih', 'Godda',
               'Gumla', 'Hazaribagh', 'Jamtara', 'Khunti', 'Koderma', 'Latehar', 'Lohardaga', 'Pakur', 'Palamu',
               'Ramgarh', 'Ranchi', 'Sahibganj', 'Saraikela-Kharsawan', 'Simdega', 'West Singhbhum'],
              ['Anantnag', 'Bandipora', 'Baramulla', 'Budgam', 'Doda', 'Ganderbal', 'Jammu', 'Kathua', 'Kishtwar',
               'Kulgam', 'Kupwara', 'Mirpur', 'Muzaffarabad', 'Pulwama', 'Punch', 'Rajouri', 'Ramban', 'Reasi', 'Samba',
               'Shopiyan', 'Srinagar', 'Udhampur'],
              ['Bagalkote', 'Ballari', 'Belagavi', 'Bengaluru Rural', 'Bengaluru Urban', 'Bidar', 'Chamarajanagara',
               'Chikkaballapura', 'Chikkamagaluru', 'Chitradurga', 'Dakshina Kannada', 'Davanagere', 'Dharwad', 'Gadag',
               'Hassan', 'Haveri', 'Kalaburagi', 'Kodagu', 'Kolar', 'Koppal', 'Mandya', 'Mysuru', 'Other State',
               'Raichur', 'Ramanagara', 'Shivamogga', 'Tumakuru', 'Udupi', 'Uttara Kannada', 'Vijayapura', 'Yadgir'],
              ['Other State', 'Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasaragod', 'Kollam', 'Kottayam',
               'Kozhikode', 'Malappuram', 'Palakkad', 'Pathanamthitta', 'Thiruvananthapuram', 'Thrissur', 'Wayanad'],
              ['Kargil', 'Leh'], ['Lakshadweep'],
              ['Ahmednagar', 'Akola', 'Amravati', 'Aurangabad', 'Beed', 'Bhandara', 'Buldhana', 'Chandrapur', 'Dhule',
               'Gadchiroli', 'Gondia', 'Hingoli', 'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Mumbai', 'Mumbai Suburban',
               'Nagpur', 'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Other State', 'Palghar', 'Parbhani', 'Pune',
               'Raigad', 'Ratnagiri', 'Sangli', 'Satara', 'Sindhudurg', 'Solapur', 'Thane', 'Wardha', 'Washim',
               'Yavatmal'], ['East Garo Hills', 'East Jaintia Hills', 'East Khasi Hills', 'North Garo Hills', 'Ribhoi',
                             'South Garo Hills', 'South West Garo Hills', 'South West Khasi Hills', 'West Garo Hills',
                             'West Jaintia Hills', 'West Khasi Hills', 'Unknown'],
              ['Bishnupur', 'Chandel', 'Churachandpur', 'Imphal East', 'Imphal West', 'Jiribam', 'Kakching', 'Kamjong',
               'Kangpokpi', 'Noney', 'Pherzawl', 'Senapati', 'Tamenglong', 'Tengnoupal', 'Thoubal', 'Ukhrul',
               'Unknown'],
              ['Agar Malwa', 'Alirajpur', 'Anuppur', 'Ashoknagar', 'Balaghat', 'Barwani', 'Betul', 'Bhind', 'Bhopal',
               'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dindori', 'Guna', 'Gwalior',
               'Harda', 'Hoshangabad', 'Indore', 'Jabalpur', 'Jhabua', 'Katni', 'Khandwa', 'Khargone', 'Mandla',
               'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch', 'Niwari', 'Other Region', 'Panna', 'Raisen', 'Rajgarh',
               'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri',
               'Sidhi', 'Singrauli', 'Tikamgarh', 'Ujjain', 'Umaria', 'Vidisha'],
              ['Aizawl', 'Champhai', 'Hnahthial', 'Khawzawl', 'Kolasib', 'Lawngtlai', 'Lunglei', 'Mamit', 'Saiha',
               'Saitual', 'Serchhip'],
              ['Dimapur', 'Kiphire', 'Kohima', 'Longleng', 'Mokokchung', 'Mon', 'Peren', 'Phek', 'Tuensang', 'Wokha',
               'Zunheboto'],
              ['NDRF-ODRF', 'Angul', 'Balangir', 'Balasore', 'Bargarh', 'Bhadrak', 'Boudh', 'Cuttack', 'Deogarh',
               'Dhenkanal', 'Gajapati', 'Ganjam', 'Jagatsinghpur', 'Jajpur', 'Jharsuguda', 'Kalahandi', 'Kandhamal',
               'Kendrapara', 'Kendujhar', 'Khordha', 'Koraput', 'Malkangiri', 'Mayurbhanj', 'Nabarangapur', 'Nayagarh',
               'Nuapada', 'Puri', 'Rayagada', 'Sambalpur', 'Subarnapur', 'Sundargarh'],
              ['Amritsar', 'Barnala', 'Bathinda', 'Faridkot', 'Fatehgarh Sahib', 'Fazilka', 'Ferozepur', 'Gurdaspur',
               'Hoshiarpur', 'Jalandhar', 'Kapurthala', 'Ludhiana', 'Mansa', 'Moga', 'Pathankot', 'Patiala', 'Rupnagar',
               'S.A.S. Nagar', 'Sangrur', 'Shahid Bhagat Singh Nagar', 'Sri Muktsar Sahib', 'Tarn Taran'],
              ['Karaikal', 'Mahe', 'Puducherry', 'Yanam'],
              ['Ajmer', 'Alwar', 'Banswara', 'Baran', 'Barmer', 'Bharatpur', 'Bhilwara', 'Bikaner', 'BSF Camp', 'Bundi',
               'Chittorgarh', 'Churu', 'Dausa', 'Dholpur', 'Dungarpur', 'Evacuees', 'Ganganagar', 'Hanumangarh',
               'Italians', 'Jaipur', 'Jaisalmer', 'Jalore', 'Jhalawar', 'Jhunjhunu', 'Jodhpur', 'Karauli', 'Kota',
               'Nagaur', 'Other State', 'Pali', 'Pratapgarh', 'Rajsamand', 'Sawai Madhopur', 'Sikar', 'Sirohi', 'Tonk',
               'Udaipur'], ['East Sikkim', 'North Sikkim', 'South Sikkim', 'West Sikkim', 'Unknown'],
              ['Foreign Evacuees', 'Other State', 'Adilabad', 'Bhadradri Kothagudem', 'Hyderabad', 'Jagtial', 'Jangaon',
               'Jayashankar Bhupalapally', 'Jogulamba Gadwal', 'Kamareddy', 'Karimnagar', 'Khammam', 'Komaram Bheem',
               'Mahabubabad', 'Mahabubnagar', 'Mancherial', 'Medak', 'Medchal Malkajgiri', 'Mulugu', 'Nagarkurnool',
               'Nalgonda', 'Narayanpet', 'Nirmal', 'Nizamabad', 'Peddapalli', 'Rajanna Sircilla', 'Ranga Reddy',
               'Sangareddy', 'Siddipet', 'Suryapet', 'Vikarabad', 'Wanaparthy', 'Warangal Rural', 'Warangal Urban',
               'Yadadri Bhuvanagiri', 'Unknown'],
              ['Railway Quarantine', 'Airport Quarantine', 'Other State', 'Ariyalur', 'Chengalpattu', 'Chennai',
               'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode', 'Kallakurichi', 'Kancheepuram',
               'Kanyakumari', 'Karur', 'Krishnagiri', 'Madurai', 'Nagapattinam', 'Namakkal', 'Nilgiris', 'Perambalur',
               'Pudukkottai', 'Ramanathapuram', 'Ranipet', 'Salem', 'Sivaganga', 'Tenkasi', 'Thanjavur', 'Theni',
               'Thiruvallur', 'Thiruvarur', 'Thoothukkudi', 'Tiruchirappalli', 'Tirunelveli', 'Tirupathur', 'Tiruppur',
               'Tiruvannamalai', 'Vellore', 'Viluppuram', 'Virudhunagar'],
              ['Dhalai', 'Gomati', 'Khowai', 'North Tripura', 'Sipahijala', 'South Tripura', 'Unokoti', 'West Tripura'],
              ['Agra', 'Aligarh', 'Ambedkar Nagar', 'Amethi', 'Amroha', 'Auraiya', 'Ayodhya', 'Azamgarh', 'Baghpat',
               'Bahraich', 'Ballia', 'Balrampur', 'Banda', 'Barabanki', 'Bareilly', 'Basti', 'Bhadohi', 'Bijnor',
               'Budaun', 'Bulandshahr', 'Chandauli', 'Chitrakoot', 'Deoria', 'Etah', 'Etawah', 'Farrukhabad',
               'Fatehpur', 'Firozabad', 'Gautam Buddha Nagar', 'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur',
               'Hamirpur', 'Hapur', 'Hardoi', 'Hathras', 'Jalaun', 'Jaunpur', 'Jhansi', 'Kannauj', 'Kanpur Dehat',
               'Kanpur Nagar', 'Kasganj', 'Kaushambi', 'Kushinagar', 'Lakhimpur Kheri', 'Lalitpur', 'Lucknow',
               'Maharajganj', 'Mahoba', 'Mainpuri', 'Mathura', 'Mau', 'Meerut', 'Mirzapur', 'Moradabad',
               'Muzaffarnagar', 'Pilibhit', 'Pratapgarh', 'Prayagraj', 'Rae Bareli', 'Rampur', 'Saharanpur', 'Sambhal',
               'Sant Kabir Nagar', 'Shahjahanpur', 'Shamli', 'Shrawasti', 'Siddharthnagar', 'Sitapur', 'Sonbhadra',
               'Sultanpur', 'Unnao', 'Varanasi'],
              ['Almora', 'Bageshwar', 'Chamoli', 'Champawat', 'Dehradun', 'Haridwar', 'Nainital', 'Pauri Garhwal',
               'Pithoragarh', 'Rudraprayag', 'Tehri Garhwal', 'Udham Singh Nagar', 'Uttarkashi'],
              ['Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur', 'Darjeeling', 'Hooghly', 'Howrah',
               'Jalpaiguri', 'Jhargram', 'Kalimpong', 'Kolkata', 'Malda', 'Murshidabad', 'Nadia', 'North 24 Parganas',
               'Other State', 'Paschim Bardhaman', 'Paschim Medinipur', 'Purba Bardhaman', 'Purba Medinipur', 'Purulia',
               'South 24 Parganas', 'Uttar Dinajpur']]

        return render_template("guide.html",op=kl,len=len(l),l=l)
@app.route("/dropdown",methods=['GET','POST'])
def dropdown():
    l = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
         'Chhattisgarh', 'Delhi', 'Dadra and Nagar Haveli and Daman and Diu', 'Goa', 'Gujarat', 'Himachal Pradesh',
         'Haryana', 'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra',
         'Meghalaya', 'Manipur', 'Madhya Pradesh', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Puducherry', 'Rajasthan',
         'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

    return render_template("dropdown.html",l=l)

app.run(debug=True)
