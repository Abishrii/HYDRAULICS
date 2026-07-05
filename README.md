HydroSense
Democratizing Edge AI for Sustainable Hydraulic Systems

HydroSense is an Edge AI-powered hydraulic health monitoring platform that brings enterprise-grade predictive maintenance to affordable embedded hardware. By combining TinyML, Explainable AI, and intelligent edge computing, HydroSense enables sustainable, energy-efficient operation of heavy machinery without cloud dependency or expensive subscription services.



Problem Statement

Hydraulic systems are the heart of construction and mining equipment. Components such as pumps, valves, coolers, and accumulators continuously degrade due to wear, contamination, overheating, and pressure fluctuations.

Existing enterprise solutions like ConSite provide intelligent diagnostics but remain inaccessible for many small and medium fleet operators because of:

- High subscription costs
- Proprietary cloud ecosystems
- Continuous internet dependency
- Expensive hardware requirements

As a result, many machines still rely on scheduled maintenance rather than condition-based maintenance, leading to:

- Premature oil replacement
- Unexpected machine breakdowns
- Increased fuel consumption
- Higher maintenance costs
- Reduced equipment lifespan
- Loss of productivity

The challenge is not building another predictive maintenance model.

The challenge is making industrial intelligence affordable, sustainable, and deployable at the edge.



Our Vision

HydroSense aims to democratize predictive maintenance by bringing enterprise-grade hydraulic health monitoring directly onto an affordable ESP32 microcontroller.

Instead of relying on cloud servers and expensive subscription platforms, HydroSense performs intelligent analysis locally, allowing every excavator to benefit from real-time diagnostics regardless of internet availability.

Our vision aligns directly with Tata Technologies' focus on:

- Edge AI
- Sustainable Industrial Systems
- Smart Heavy Machinery
- Energy Efficient Computing

-

Our Solution

HydroSense is an intelligent Edge AI pipeline that continuously monitors hydraulic system behaviour and detects abnormalities before catastrophic failures occur.

Unlike conventional monitoring systems, HydroSense performs all critical inference directly on the edge device.

The system:

- Learns healthy machine behaviour
- Detects anomalies in real time
- Identifies the affected hydraulic subsystem
- Explains why the prediction was made
- Operates completely offline

This significantly reduces maintenance costs while extending machine lifespan and improving sustainability.

---

System Architecture


Hydraulic Sensors
        │
        ▼
Feature Engineering
        │
        ▼
Standard Scaling
        │
        ▼
Autoencoder
        │
        ▼
Healthy ?
   │          │
  Yes         No
   │          │
   ▼          ▼
 Continue   Random Forest Classifiers
                  │
                  ▼
          Pump
          Valve
          Cooler
          Accumulator
                  │
                  ▼
           SHAP Explainability
                  │
                  ▼
         Maintenance Recommendation


---

Core Innovation

HydroSense introduces **Gated Cascade Inference**, a modern Edge AI architecture where a lightweight anomaly detector controls when specialist diagnostic models are activated.

Instead of continuously running multiple AI models, HydroSense first determines whether the machine is operating normally.

Only when abnormal behaviour is detected are the diagnostic classifiers executed.

This significantly reduces:

- Computation
- Power consumption
- Memory usage

while maintaining high diagnostic accuracy.

---

Why Autoencoder?

Industrial machines spend most of their operational life in healthy conditions.

Fault data is:

- Rare
- Difficult to collect
- Expensive to label

Rather than requiring thousands of failure examples, HydroSense trains an Autoencoder exclusively on healthy hydraulic behaviour.

The Autoencoder learns:

"This is how a healthy hydraulic system should behave.”

During deployment:

- Low reconstruction error → Healthy operation
- High reconstruction error → Possible anomaly

This approach makes HydroSense practical for real industrial environments where fault samples are limited.

---

Why Four Independent Random Forest Models?

Instead of training one large multi-output classifier, HydroSense uses four specialized Random Forest models dedicated to:

- Pump
- Valve
- Cooler
- Accumulator

This modular architecture provides:

- Better specialization
- Easier maintenance
- Independent retraining
- Higher scalability
- Lower model complexity

Each subsystem becomes independently upgradeable without retraining the complete system.

---

Explainable AI using SHAP

Industrial engineers require more than a fault label—they need to understand why the AI reached its decision.

HydroSense integrates SHAP (SHapley Additive Explanations) to provide feature-level interpretability.

Instead of acting as a black box, the system identifies:

- Most influential sensors
- Root cause indicators
- Feature contributions
- Diagnostic confidence

This enables engineers to make informed maintenance decisions with greater trust.

---

Flash-Resident Intelligence

HydroSense is designed for resource-constrained embedded hardware.

The optimized AI models are converted using TensorFlow Lite and embedded directly into the ESP32 firmware.

This creates Flash-Resident Intelligence, where the AI permanently resides inside Flash memory and executes locally without requiring cloud downloads or external computation.

Benefits include:

- Offline operation
- Low latency
- Reduced RAM usage
- Lower deployment cost
- High reliability

---

Adaptive Energy Intelligence

HydroSense minimizes energy consumption by adapting computational effort based on machine health.

Healthy Mode

- Low monitoring frequency
- Minimal computation
- Power-efficient operation

 Alert Mode

- Increased monitoring frequency
- Autoencoder validation

 Critical Mode

- Specialist Random Forest activation
- Explainability
- Maintenance recommendation

This adaptive strategy enables energy-efficient continuous monitoring while maximizing battery life.

---

Technical Stack

Machine Learning

- TensorFlow 2.21
- TensorFlow Lite
- TensorFlow Lite Micro
- Autoencoder
- Random Forest
- SHAP Explainability
- Scikit-Learn
- NumPy
- Pandas

Embedded AI

- ESP32 DevKit V1
- TinyML
- TensorFlow Lite Micro
- PlatformIO
- INT8 Quantization
- Static Memory Allocation

Development Tools

- Python
- Jupyter Notebook
- VS Code
- Git
- GitHub

---

 Machine Learning Pipeline


Raw Hydraulic Dataset
        │
        ▼
Feature Engineering
        │
        ▼
StandardScaler
        │
        ▼
Healthy Dataset
        │
        ▼
Autoencoder Training
        │
        ▼
Reconstruction Error
        │
        ▼
Random Forest Classifiers
        │
        ▼
SHAP Explainability
        │
        ▼
TensorFlow Lite Conversion
        │
        ▼
ESP32 Deployment

---


 Edge AI Pipeline


Sensor Data
      │
      ▼
Feature Extraction
      │
      ▼
Scaling
      │
      ▼
Autoencoder
      │
      ▼
Healthy ?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Continue   Specialist Random Forest
                 │
                 ▼
        SHAP Explainability
                 │
                 ▼
     Maintenance Recommendation


---

Sustainability Impact

HydroSense contributes directly to sustainable industrial operations by:

- Extending hydraulic component lifespan
- Reducing unnecessary oil replacement
- Lowering maintenance costs
- Preventing catastrophic failures
- Improving fuel efficiency
- Eliminating continuous cloud computation
- Supporting affordable AI adoption for small businesses

HydroSense promotes **condition-based maintenance instead of schedule-based maintenance**, reducing waste while improving operational efficiency.

---

Current Progress

✅ Feature Engineering Pipeline

✅ Autoencoder Training

✅ Random Forest Diagnostics

✅ SHAP Explainability

✅ TensorFlow Lite Model Conversion

✅ INT8 Quantization

✅ ESP32 Data Preprocessing Pipeline

✅ Edge AI Deployment Preparation

---

Future Scope

- Real-time sensor integration
- CAN Bus communication
- Remaining Useful Life estimation
- Digital Twin integration
- Fleet-wide analytics
- OTA model updates
- Federated learning
- Multi-machine deployment

---

Repository Structure


HydroSense/
│
├── dashboard/
├── dataset/
├── docs/
├── esp32/
├── models/
├── notebooks/
├── runtime/
├── src/
├── README.md
└── requirements.txt


---

Authors

Developed as part of Tata Technologies InnoVent 2027 under the theme:

AI at the Edge for Sustainable & Energy-Efficient Industrial Systems

---

Final Vision

HydroSense implements Gated Cascade Inference—a modern Edge AI architecture where a lightweight Autoencoder continuously monitors hydraulic health and activates specialized diagnostic models only when required. By combining anomaly detection, Explainable AI, and flash-resident TinyML deployment, HydroSense brings enterprise-grade hydraulic intelligence to affordable embedded hardware, making sustainable industrial AI accessible beyond premium fleets.
