# **Theme Park Simulation - AI Project**

This repository contains a **theme park simulation** developed as part of an **Artificial Intelligence** course project. The simulation models the behavior of visitors in a theme park, from arrival to departure, using **SimPy**, a process-based discrete-event simulation framework. The project aims to **analyze operational efficiency, visitor experience, and attraction performance** using computational modeling and data analysis techniques.

---

## **Project Overview**  
The simulation accurately replicates a theme park's dynamic environment, incorporating key factors such as:
- **Randomized visitor behavior:** Each visitor has unique preferences, deciding which attractions to visit and how long to stay.
- **Attraction constraints:** Each ride has a **capacity limit and a predefined duration**, influencing wait times and queue formations.
- **Queue and scheduling system:** The simulation manages **visitor flow**, ensuring realistic waiting times and attraction interactions.
- **Statistical analysis of visitor trends:** Data is collected and analyzed using **Pandas** and **Jupyter Notebook** to identify **trends, peak hours, and optimization opportunities**.

---

## **Technical Implementation**  
The project consists of several Python scripts structured as follows:

### **1. Core Simulation Components**
- `Menu.py`: Handles simulation start and stop operations.
- `Parks.py`: Defines the theme park environment, initializing attractions and visitors.
- `Sim.py`: Manages visitor interactions with attractions, using SimPy to model real-world constraints such as **capacity limits, queue management, and wait times**.
- `Attractions.py`: Defines the characteristics of each ride, including name, capacity, and duration, based on an external **text file containing real-world attraction data**.

### **2. Data Management and Analysis**
- **CSV-based data storage:** Visitor interactions are recorded in structured **CSV files**.
- `StatisticsCollector.py`: Gathers simulation data, tracking key performance metrics such as **visitor counts, ride popularity, and average wait times**.
- `att_analysis.ipynb`: Uses Jupyter Notebook for advanced **data visualization and statistical analysis**, including:
  - **Visitor distribution per attraction**
  - **Visit duration statistics**
  - **Queue time analysis**
  - **Peak time detection**
  - **Visitor behavior trends**

### **3. Randomized Visitor Behavior**
- `names.py` & `ESP_common_names.py`: Generate **random visitor names** to add realism.
- Visitors select **random attractions**, simulating the unpredictability of real-world behavior.

---

## **Objectives and Outcomes**
The goal of this project was to **simulate, analyze, and optimize** the operations of a theme park. By adjusting variables such as attraction capacity, wait times, and visitor behavior, we could predict:
- **Bottlenecks in park operations** (e.g., overcrowded rides).
- **Optimal attraction capacity adjustments** to improve visitor flow.
- **The impact of operational decisions on visitor experience**.

### **Key Takeaways:**
- **Understanding SimPy**: The project enhanced our knowledge of **event-driven simulations** in Python.
- **Data-Driven Decision Making**: The statistical analysis provided insights into how a **theme park could improve efficiency and visitor satisfaction**.
- **Scalability and Future Applications**: This simulation could be extended to **real-world business applications**, such as optimizing **theme park management, event logistics, or customer experience modeling**.
