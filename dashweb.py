import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Setup logging for debugging purposes
logging.basicConfig(level=logging.DEBUG)

# SMTP Email Configuration
smtp_server = "abc@.com"
smtp_port =abc
smtp_user = "abc@example.com"
smtp_password = "qwertyuiop"
sender_email = "andop.com"
receiver_email = "example@gmail.com"

# Initialize session state for login and page navigation
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# Login function
def login(email, password):
    if email == "user@example.com" and password == "password123":
        st.session_state.logged_in = True
        st.session_state.page = "dashboard"  # Go to dashboard page after login
        st.success("🎉 Login successful! Welcome to the GDP Dashboard! 🎉")  # Success message after login
    else:
        st.warning("❌ Incorrect email or password. Please try again. ❌")

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.page = "login"

# Function to send feedback via email
def send_feedback(feedback):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "New Feedback from GDP Dashboard"
        
        body = f"User Feedback:\n\n{feedback}"
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        
        st.success("Thank you for your feedback! We have received it. 😊")
    except Exception as e:
        st.error("Failed to send feedback. Please try again later. 😞")
        logging.error(f"Feedback sending failed: {e}")

# Page Routing Logic
st.set_page_config(page_title="GDP and Productivity Dashboard", page_icon=":bar_chart:", layout="wide")

# Main content area (to the right of the sidebar)
if st.session_state.page == "login":
    st.title("Login to GDP and Productivity Dashboard")
    st.markdown("""
    Welcome to the GDP and Productivity Dashboard 🚀  
    This platform allows you to explore GDP and productivity insights across Indian cities through interactive visualizations and data-driven insights.

    Features:
    - 🌐 Explore the GDP of Indian cities: Discover economic patterns and sectoral data.
    - 📈 Interactive Analytics: Visualize productivity trends across sectors.
    - 💼 In-Depth Analysis: Gain insights into key metrics shaping city economies.
    
    Contact Us 📨  
    If you have questions, suggestions, or need assistance, we're here to help! Feel free to reach out to us using the contact details below.

    <div style='background-color: #f1f1f1; padding: 15px; border-radius: 8px; font-size: 16px; color: black;'>
        <b>📧 Email:</b> <a href='mailto:support@aptpath.in' style='text-decoration: none; color: #0073e6;'>support@aptpath.in</a>  
        <br><b>☎ Phone:</b> +91 123 456 7890  
        <br><b>🌐 Website:</b> <a href='https://www.aptpath.in' target='_blank' style='text-decoration: none; color: #0073e6;'>www.aptpath.in</a>
    </div>
    """, unsafe_allow_html=True)

    email = st.text_input("Email  📧")
    password = st.text_input("Password 🔑", type="password")
    if st.button("Login 🔓"):
        login(email, password)

else:
    # Sidebar navigation (only shown after login)
    with st.sidebar:
        st.header("Dashboard Controls")
        st.markdown("Use these options to adjust the dashboard view.")

        # Fixed buttons in the sidebar with icons
        project_lookover = st.sidebar.button("🚀 Project Lookover")
        project_view = st.sidebar.button("🔍 Project View")
        project_processing = st.sidebar.button("⚙ Project Processing")
        objective_of_work = st.sidebar.button("🎯 Objective of the Work")
        lookover_insights = st.sidebar.button("💡 Lookover Insights")
        feedback_page = st.sidebar.button("📬 Feedback")

        # Handle button clicks
        if project_lookover:
            st.session_state.page = "project_lookover"
        elif project_view:
            st.session_state.page = "project_view"
        elif project_processing:
            st.session_state.page = "project_processing"
        elif objective_of_work:
            st.session_state.page = "objective_of_work"
        elif lookover_insights:
            st.session_state.page = "lookover_insights"
        elif feedback_page:
            st.session_state.page = "feedback"
        
        if st.sidebar.button("Logout"):
            logout()

        # Contact Us moved to the bottom of the sidebar
        st.sidebar.info("""📞📩☎️ Contact Us  
        For feedback or support, reach out to our team at [support@aptpath.in](mailto:support@aptpath.in).""")

    # Page Content Based on Selected Page
    if st.session_state.page == "project_lookover":
        st.title("Project Lookover ✅⚙️🧩📂")
        st.write("""
### GDP and Productivity of Indian Cities

**Objective:**  
To visualize and analyze economic data across Indian cities, showcasing GDP contributions, sectoral strengths, and productivity metrics through an interactive dashboard. 

**Key Features:**
- **Interactive Dashboard 🖥️**: A Power BI dashboard that allows users to explore economic metrics city-by-city, with filters for GDP, sectoral contributions, and year-over-year growth.
- **Sectoral Insights 📊**: Detailed analysis of each city’s main economic sectors, from agriculture and manufacturing to IT and services, helping identify regional productivity patterns.
- **State-by-State Summary 🌍**: Economic summaries for each Indian state, highlighting GDP, major industries, and employment trends.
- **Chatbot Integration 🤖**: A chatbot in Streamlit to answer specific queries, enabling easy access to city-level data, sectoral insights, and GDP statistics.

**Data Sources:**  
Leveraging publicly available data on economic productivity and employment across sectors in major Indian cities. Additional data points, such as historical growth rates, may enhance insights.

**Future Scope:**
- **Additional Visualizations 📈**: Incorporating maps and filled map visuals to show geographic economic distribution.
- **Data Enrichment 🔍**: Adding more granular data like sector-specific employment numbers, FDI inflow, and GDP per capita.
- **User Interaction 💬**: Enhancing chatbot responses and building custom queries based on user interests.
""")

    elif st.session_state.page == "project_view":
        st.title("Project View (⊙_⊙)-->👀")
        st.markdown("Here, we provide a comprehensive and detailed view of the various components of the project, highlighting how the Power BI dashboard 🖥️ efficiently works to visualize and display economic data 📊. This includes interactive features that allow users to explore key metrics such as GDP contributions 💰, sectoral growth 📈, and year-over-year changes 📅. The dashboard is designed to provide a clear and user-friendly experience for analyzing economic performance across Indian cities 🏙️ and states 🌍, offering valuable insights into regional productivity and industry strengths ⚙️.")
            
        # Embed Power BI Dashboard with adjusted iframe size
        embed_link = "https://app.powerbi.com/view?r=abcdefghijklmnopqrstuvwxyz"  # Replace with your Power BI report URL
        st.markdown(f'''
        <iframe src="{embed_link}" width="100%" height="600px" frameborder="0" allowFullScreen="true"></iframe>
        ''', unsafe_allow_html=True)

    elif st.session_state.page == "project_processing":
        st.title("Project Processing ﹌﹌﹌﹌﹌🤖🛠")
        st.write("""
    The processing phase of this project is essential for transforming raw data into actionable insights. It involves several stages to ensure the data is accurate, well-structured, and ready for visualization. The following steps outline the detailed process:

    ### Data Collection 📑
    - Sources: Economic data is sourced from trusted institutions such as the Ministry of Statistics and Programme Implementation (MOSPI), Reserve Bank of India (RBI), National Sample Survey Office (NSSO), and other government reports. 📊
    - Key Metrics: Data on GDP, sectoral employment, industry contributions, productivity indices, and demographic variables for each city are gathered.
    - Time Period: The dataset spans multiple years (e.g., 2010–2023) to show trends over time.

    ### Data Cleaning and Preprocessing 🧹
    - Handling Missing Data: Missing or incomplete data points are addressed using imputation techniques such as mean imputation or predictive modeling.
    - Outlier Detection: Extreme values are detected and either removed or adjusted to ensure they don’t distort the analysis. For instance, cities with anomalous GDP values are flagged for review. 🔍
    - Standardization: Different datasets are standardized to ensure consistent units (e.g., converting all GDP values to constant prices for comparison across years).

    ### Data Transformation 🔧
    - Normalization: GDP values across different cities are normalized to account for population differences. For example, GDP per capita is calculated to make cities with larger populations comparable to smaller ones. 💰
    - Calculating Key Ratios: Productivity indices and sectoral shares in GDP are calculated. For example, if a city's manufacturing sector contributes 25% to its GDP, this value is isolated and analyzed. 🏭
    - Geospatial Data Integration 🌍: City-level data is enriched with geospatial information, ensuring that maps can reflect economic performance across different regions of India.

    ### Data Aggregation and Summarization 📅
    - Regional Grouping: Cities are grouped into regions (e.g., North, South, West) to identify regional patterns. This helps to understand broader economic trends and to compare cities within the same region.
    - Sectoral Analysis: Data is aggregated by industry sectors (e.g., agriculture, manufacturing, services) to see the contributions of each sector to GDP. For example, the services sector in Bangalore might contribute 60%, while manufacturing in Pune might contribute 45%. 📊
    - Yearly Comparisons: Data is aggregated annually to compare GDP growth rates, sectoral shifts, and employment trends over time. For example, a city’s GDP might grow by 5% annually, while another city shows stagnation.

    ### Visualization and Analysis 📈
    - Power BI Dashboards: Using Power BI, the processed data is visualized through dynamic charts, including:
        - Line Graphs: To show GDP growth trends over time for individual cities and sectors.
        - Bar Charts: To compare sectoral contributions to GDP across cities.
        - Maps: Geospatial visualizations to depict regional economic performance, highlighting high-growth areas. 🗺
    - Interactive Filters: Users can filter the data by city, sector, year, and economic indicators to explore different scenarios. This allows for a personalized exploration of the data. 🧭

    ### Streamlit Application Development 💻
    - User Interface: The processed data is integrated into the Streamlit app, providing an intuitive interface for users to interact with the data. This includes options to:
        - Select cities, sectors, and time frames for detailed analysis.
        - Visualize trends through graphs and tables.
        - Compare economic metrics across different urban centers in real-time. ⏱
    - Interactive Widgets: Data filters (e.g., dropdowns, sliders) are implemented to allow users to explore specific segments of data interactively.

    ### Error Checking and Validation 🔍
    - Cross-Verification: The processed data is cross-verified with external sources (such as government publications) to ensure consistency and accuracy. Any discrepancies are investigated and corrected.
    - Statistical Checks: Basic statistical analyses (e.g., mean, median, standard deviation) are performed to ensure the processed data makes sense and is free of significant errors. 📊
    """)

    elif st.session_state.page == "objective_of_work":
        st.title("Objective of the Work 📈")
        st.write("""
    The "GDP and Productivity of Indian Cities" project aims to achieve several key objectives, all centered around providing a clear and actionable understanding of the economic dynamics of India’s urban centers. The core goals include:

    ### Understanding Economic Contributions by City
    The project seeks to analyze how different cities contribute to the national GDP, focusing on both overall economic output and sector-specific productivity. By identifying cities that drive economic growth, the project helps to visualize which urban centers are performing well economically and which need further support. 🌆💡

    ### Highlighting Sectoral Contributions
    One of the main objectives is to break down GDP contributions by sector (e.g., agriculture, manufacturing, services). This analysis helps in understanding which industries dominate in specific cities, providing valuable insights for policymakers and business leaders looking to foster growth in particular sectors. 🏭📊

    ### Promoting Regional Comparisons
    The project allows for regional comparisons to reveal economic disparities and growth trends. By grouping cities into regions (such as North, South, West), the project highlights the economic performance at a broader level, fostering regional development strategies. 📍🔍

    ### Providing Data-Driven Insights for Policy and Decision-Making
    By visualizing economic data through interactive dashboards, the project aims to empower policymakers with the insights needed to craft informed, data-driven strategies for urban development. This includes decisions related to infrastructure investments, job creation, and resource allocation based on each city's economic strengths and needs. 🏙📈

    ### Facilitating Business Expansion and Investment
    The project helps businesses understand the economic environment in different cities, offering insights into where to invest or expand based on sectoral strengths, regional performance, and GDP growth trends. This information aids companies in making strategic decisions for growth. 💼📉

    ### Driving Sustainable Economic Development
    Ultimately, the project aims to support sustainable growth by identifying key areas for improvement and investment. Understanding the economic drivers of cities will help guide sustainable development practices and ensure that growth is balanced and inclusive, benefiting all sectors and regions of the country. 🌱🌍

    ### Fostering Public Engagement and Awareness
    By providing an easy-to-navigate interface for both experts and the general public, the project ensures that economic data is accessible to all, encouraging public engagement and raising awareness about the importance of GDP and productivity in shaping the future of cities. 📚🌐

    Through these objectives, the project not only seeks to provide a detailed, data-driven portrait of India’s urban economies but also aims to drive impactful change in how cities plan for future growth and prosperity.
    """)

    elif st.session_state.page == "lookover_insights":
        st.title("Lookover Insights  💬")
        st.write("""
    The "GDP and Productivity of Indian Cities" project offers a deep dive into the economic fabric of India's urban centers. Here are the key insights drawn from the analysis and visualizations:

    ### Regional Economic Disparities 🌍
    The data reveals significant differences in economic performance across regions in India. For instance, southern cities like Bengaluru and Hyderabad are strongholds for the IT and technology sectors, contributing significantly to national GDP, while northern cities like Delhi and Chandigarh show a balanced mix of services, manufacturing, and trade. 📍
    Cities in the western region, such as Mumbai and Pune, stand out for their industrial and financial sector growth, whereas cities in the eastern region, like Kolkata, have a more diversified economic base but with slower GDP growth. This regional disparity highlights the need for targeted economic strategies for each area. 🏙

    ### Sectoral Contributions to GDP 🏭📈
    - Services dominate the GDP of most major cities, with Bengaluru, Mumbai, and Delhi being key contributors to the national service sector, particularly in IT, finance, and business services. These sectors account for as much as 60%–70% of the GDP in these cities.
    - Manufacturing remains a crucial part of cities like Pune, Ahmedabad, and Chennai, where automotive, engineering, and textiles contribute significantly to the economy. For example, Pune's automotive sector accounts for 25% of the city's GDP. ⚙
    - Agriculture, though less dominant, still plays an important role in cities like Jaipur, Lucknow, and Bhopal, contributing to the livelihoods of millions. However, these cities show slower growth compared to those driven by industrial or service sectors. 🌾

    ### GDP Growth Trends 📅
    - Over the past decade, cities like Bengaluru, Hyderabad, and Ahmedabad have shown remarkable GDP growth rates, surpassing the national average of 5% per year, driven by the rapid growth of tech startups, manufacturing, and service industries. 🚀
    - In contrast, some cities in rural-urban transition zones or historically agrarian regions have seen stagnation or slower growth in GDP, indicating the need for infrastructure development and industrial diversification to spark economic growth. 📉

    ### Employment and Productivity Analysis 💼
    - The project also highlights the varying productivity levels between cities. High-productivity cities like Delhi and Bengaluru show a high output per worker, reflecting the dominance of knowledge-based and technology-driven industries. 👩‍💻
    - Cities such as Lucknow and Bhopal, with more traditional industries, show lower productivity but still serve as crucial employment hubs in the agriculture and manufacturing sectors. The data emphasizes the importance of investing in education, skills, and technology to enhance productivity in these cities. 📊

    ### Urbanization and Economic Growth 📈🏙
    - As urbanization increases, cities like Chennai, Delhi, and Mumbai are seeing a rise in economic activities due to increased population density and migration from rural areas. The project reveals that urbanization correlates strongly with economic expansion, but it also brings challenges such as infrastructure strain, environmental impact, and the need for effective urban planning. 🏙
    - The rapid growth of smaller cities like Surat and Indore, which are emerging as new economic hubs, underscores the importance of fostering growth beyond the largest metros to achieve more balanced national development. 🚀

    ### Investment Opportunities 💰
    - The project uncovers potential investment opportunities by highlighting cities with rapid growth and emerging sectors. For example, Bengaluru's tech sector and Ahmedabad's manufacturing hub present lucrative opportunities for businesses looking to expand. 💼
    - The analysis also suggests that cities with underperforming sectors, such as those in the North-East or some parts of Central India, are ripe for investment in infrastructure, industry, and services to boost GDP growth. 🏗

    ### Policy Implications for Balanced Growth 📊💡
    - The insights gathered indicate that while high-performing cities should continue to be supported in their growth, there is a pressing need for policies that promote balanced development across all regions. Urban areas with slower growth could benefit from government initiatives focused on infrastructure, industrialization, and skills development. 🤝
    - Sustainable economic development strategies are crucial to address the environmental and social challenges posed by rapid urbanization and to ensure long-term growth. 🌱

    These insights provide a comprehensive understanding of the economic patterns across Indian cities, highlighting areas of strength, opportunity, and challenges. The visualizations in the Power BI dashboard and Streamlit application allow users to explore these insights interactively, making it easier to derive actionable strategies for economic growth and development.
    """)

    elif st.session_state.page == "feedback" and st.session_state.logged_in:
        st.title("Feedback Page 🌍")
        st.subheader("We value your feedback!")
        feedback = st.text_area("Enter your feedback here")
        if st.button("Submit Feedback"):
            if feedback:
                send_feedback(feedback)
            else:
                st.warning("Please enter your feedback before submitting.")
        
        # Button to go back to the dashboard
        if st.button("Back to Dashboard"):
            st.session_state.page = "dashboard"
