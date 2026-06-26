import streamlit as st
from datetime import datetime, timedelta
import random
import pandas as pd 

def local_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)  

# Call this right after your st.set_page_config
# Just add "styles/" to the path
local_css("styles/style.css")
  
# --------------------------------------------------
# CONFIG & GLOBAL ENTERPRISE STYLING
# --------------------------------------------------
st.set_page_config(
    page_title="Biztab Logistics Dashboard",
    page_icon="🚚",
    layout="wide"
)



# --------------------------------------------------
# SUBSYSTEM MASTER MEMORY REPOSITORY
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "login"

if "shipment" not in st.session_state:
    st.session_state.shipment = None

if "history_ledger" not in st.session_state:
    st.session_state.history_ledger = []

# Core Constants
STAGES = ["Created", "Packed", "Dispatched", "In Transit", "Out for Delivery", "Delivered"]
COURIER_POOL = [
    ("Rahul Kumar", "TS-09-AB-1234"),
    ("Priya Sharma", "TS-10-CD-5678"),
    ("Arjun Reddy", "TS-08-EF-9012"),
    ("Ananya Rao", "TS-11-GH-3456")
]

# Helper to capture and update structural historical state changes
def update_history_ledger(shipment_id, customer, destination, current_status):
    for record in st.session_state.history_ledger:
        if record["Shipment ID"] == shipment_id:
            record["Current Status"] = current_status
            return
    st.session_state.history_ledger.append({
        "Shipment ID": shipment_id,
        "Customer": customer,
        "Destination": destination,
        "Current Status": current_status,
        "Last System Sync": datetime.now().strftime("%I:%M %p")
    })

# =====================================================================
# 1. PREMIUM GLASS LOGIN PORTAL VIEW
# =====================================================================
if st.session_state.page == "login":
    st.markdown("<style>.main .block-container { max-width: 420px !important; padding-top: 9rem !important; }</style>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #F8FAFC; font-weight: 800; letter-spacing: -1px; margin-bottom: 2px;'>biztab</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748B; font-size: 11px; letter-spacing: 2px; margin-bottom: 2rem;'>LOGISTICS MANAGEMENT PORTAL</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Sign In to System →", use_container_width=True):
        if username == "admin" and password == "biztab2026":
            st.session_state.page = "create"
            st.rerun()
        else:
            st.error("Authentication Rejected: Invalid Credentials")
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 2. CREATE MANIFEST NODE
# =====================================================================
elif st.session_state.page == "create":
    st.markdown("<h2 style='color: #F8FAFC; font-weight: 700;'>🚚 Create Shipment</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8;'>Register a new shipment and begin tracking its delivery lifecycle.</p>", unsafe_allow_html=True)
    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        customer = st.text_input("Customer Name", placeholder="Enter customer name")
        destination = st.text_input("Destination City", placeholder="e.g., Hyderabad")
    with col2:
        package_type = st.selectbox("Package Type", ["Electronics", "Documents", "Clothing", "Furniture"])
        priority = st.selectbox("Priority", ["Standard", "Express"])
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🚚 Create Shipment", use_container_width=True):
        if not customer or not destination:
            st.warning("⚠️ Please fill in all fields to register the manifest profile.")
        else:
            shipment_id = "SHP-" + datetime.now().strftime("%H%M%S")
            assigned_courier, assigned_vehicle = random.choice(COURIER_POOL)
            
            # Generate deterministic dynamic past logs based on current execution hour
            base_time = datetime.now()
            st.session_state.shipment = {
                "shipment_id": shipment_id,
                "customer": customer,
                "destination": destination,
                "package_type": package_type,
                "priority": priority,
                "status_index": 0,
                "courier": assigned_courier,
                "vehicle": assigned_vehicle,
                "timestamps": {
                    "Created": base_time.strftime("%I:%M %p"),
                    "Packed": (base_time + timedelta(minutes=15)).strftime("%I:%M %p"),
                    "Dispatched": (base_time + timedelta(minutes=40)).strftime("%I:%M %p"),
                    "In Transit": (base_time + timedelta(hours=1, minutes=10)).strftime("%I:%M %p"),
                    "Out for Delivery": (base_time + timedelta(hours=2, minutes=5)).strftime("%I:%M %p"),
                    "Delivered": (base_time + timedelta(hours=2, minutes=35)).strftime("%I:%M %p"),
                }
            }
            update_history_ledger(shipment_id, customer, destination, STAGES[0])
            st.session_state.page = "tracking"
            st.rerun()

# =====================================================================
# 3. INTERACTIVE LOGISTICS ROUTING METRICS VIEW
# =====================================================================
elif st.session_state.page == "tracking":
    shipment = st.session_state.shipment
    current = shipment["status_index"]

    st.markdown(f"<h2 style='color: #F8FAFC; font-weight: 700;'> Live Shipment Tracking</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #94A3B8;'>Real-time orchestration overview for core tracking node: <b style='color: #3B82F6;'>{shipment['shipment_id']}</b></p>", unsafe_allow_html=True)
    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    # 5. VISUAL HORIZONTAL PIPELINE WORKFLOW STEPPER
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    step_cols = st.columns(len(STAGES))
    timeline_icons = ["✨", "📦", "🚚", "🛣️", "🛵", "✅"]
    
    for i, stage in enumerate(STAGES):
        with step_cols[i]:
            if i < current:
                st.markdown(f"<div style='text-align: center; color: #10B981;'>{timeline_icons[i]}<br><b style='font-size:14px;'>{stage}</b><br><small style='color: #059669; font-weight:600;'>COMPLETED</small></div>", unsafe_allow_html=True)
            elif i == current:
                st.markdown(f"<div style='text-align: center; color: #3B82F6; background: rgba(59, 130, 246, 0.08); padding: 8px 4px; border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.4);'>{timeline_icons[i]}<br><b style='font-size:14px;'>{stage}</b><br><small style='color: #3B82F6; font-weight: bold;'>ACTIVE</small></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: center; color: #4B5563;'>{timeline_icons[i]}<br><span style='font-size:14px;'>{stage}</span><br><small style='color: #4B5563;'>PENDING</small></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Summary Metadata Rows
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Shipment ID", shipment["shipment_id"])
    m2.metric("Customer", shipment["customer"])
    m3.metric("Destination", shipment["destination"])
    m4.metric("Current Status", STAGES[current])
    st.markdown("</div>", unsafe_allow_html=True)

    # Split Pane: Courier Assignment vs History Timestamp Stream
    col_left, col_right = st.columns([1.3, 2.7])
    with col_left:
        st.markdown("<div class='premium-card' style='height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #F8FAFC; margin-bottom: 1.2rem; font-weight: 600;'>👨‍✈️ Delivery Agent</h4>", unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color: #94A3B8; margin-bottom: 0.6rem; font-size: 14px;'><b>Agent Name:</b> {shipment['courier']}</p>
        <p style='color: #94A3B8; margin-bottom: 0.6rem; font-size: 14px;'><b>Vehicle Number:</b> {shipment['vehicle']}</p>
        <p style='color: #94A3B8; font-size: 14px;'><b>Priority Service:</b> {shipment['priority']}</p>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_right:
        st.markdown("<div class='premium-card' style='height: 100%;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #F8FAFC; margin-bottom: 1.2rem; font-weight: 600;'>📍 Activity Tracking Timeline</h4>", unsafe_allow_html=True)
        for i, stage in enumerate(STAGES):
            if i <= current:
                t_stamp = shipment["timestamps"][stage]
                st.markdown(f"<p style='color: #F8FAFC; font-size: 14px; margin-bottom: 0.5rem;'>⏱️ <b style='color: #3B82F6; font-family: monospace;'>{t_stamp}</b> &nbsp;&nbsp;—&nbsp;&nbsp; Shipment Status set to <b>{stage}</b></p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Real-World Role Simulation Controls
    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
    st.subheader("⚙️ Logistics Operations Desk")
    st.markdown("<p style='color: #94A3B8; font-size: 13px; margin-top:-10px;'>Simulate real physical scans from the warehouse, hub, and courier mobile app.</p>", unsafe_allow_html=True)
    
    # Define cleaner, action-oriented button text based on the current stage
    action_labels = [
        "📦 Scan & Pack Items (Warehouse Desk)",         # When status is 'Created'
        "🚚 Assign Driver & Dispatch (Hub Scan)",       # When status is 'Packed'
        "🛣️ Ship to Destination Terminal (In Transit)", # When status is 'Dispatched'
        "🛵 Out for Delivery (Courier App Trigger)",     # When status is 'In Transit'
        "✅ Confirm Handover & Signature (Delivered)"   # When status is 'Out for Delivery'
    ]

    b1, b2, b3 = st.columns([2, 1, 1])
    
    with b1:
        if current < len(STAGES) - 1:
            # Show the realistic action required for the NEXT step
            if st.button(f"⚡ {action_labels[current]}", use_container_width=True):
                st.session_state.shipment["status_index"] += 1
                next_stage = STAGES[st.session_state.shipment["status_index"]]
                update_history_ledger(shipment["shipment_id"], shipment["customer"], shipment["destination"], next_stage)
                
                if st.session_state.shipment["status_index"] == len(STAGES) - 1:
                    st.session_state.page = "delivered"
                st.rerun()
        else:
            st.write("✅ Shipment lifecycle completely processed.")
            
    with b2:
        if st.button("📩 Send Customer SMS Alert", use_container_width=True):
            st.toast(f"Tracking alert pinged to {shipment['customer']}", icon="🔔")
            
    with b3:
        if st.button("⚠ Flag Delivery Exception", use_container_width=True):
            st.error("""
            ### 🛑 Delivery Exception Logged
            * **Issue:** Recipient address door locked.
            * **Resolution:** Re-attempting delivery sequence automatically on next business shift.
            """)

    # 4. ENTERPRISE HISTORICAL SHIPMENT PERSISTENT RECORD LEDGER
    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
    st.subheader("📋 Master Shipment Records Ledger")
    if st.session_state.history_ledger:
        df_history = pd.DataFrame(st.session_state.history_ledger)
        st.dataframe(df_history, use_container_width=True, hide_index=True)

# =====================================================================
# 4. FINAL DELIVERED SUCCESS LANDING TARGET
# =====================================================================
elif st.session_state.page == "delivered":
    shipment = st.session_state.shipment
    st.balloons()

    st.markdown("<div style='text-align: center; padding: 3rem 0;'>", unsafe_allow_html=True)
    st.success(f"""
    # 🎉 Delivery Completed Successfully!
    
    * **Shipment ID:** `{shipment['shipment_id']}`
    * **Customer Account:** {shipment['customer']}
    * **Destination Terminal Handover Location:** {shipment['destination']}
    
    `System Registry Resolution State: 200 SUCCESSFUL_DELIVERY`
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # Historical Database even displayed on the final summary landing context
    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
    st.subheader("📋 Master Shipment Records Ledger")
    if st.session_state.history_ledger:
        df_history = pd.DataFrame(st.session_state.history_ledger)
        st.dataframe(df_history, use_container_width=True, hide_index=True)

    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)
    if st.button("🚚 Create New Shipment Lifecycle", use_container_width=True):
        st.session_state.shipment = None
        st.session_state.page = "create"
        st.rerun()
