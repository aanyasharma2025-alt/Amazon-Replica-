import streamlit as st

st.set_page_config(page_title="Mini Shop", layout="wide")
st.title("🛒 Mini Online Store")

# --- Sample product data ---
products = [
    {"name": "Wireless Headphones", "price": 49.99, "image": "https://via.placeholder.com/150"},
    {"name": "Smart Watch", "price": 89.99, "image": "https://via.placeholder.com/150"},
    {"name": "Bluetooth Speaker", "price": 29.99, "image": "https://via.placeholder.com/150"},
    {"name": "USB-C Charger", "price": 15.99, "image": "https://via.placeholder.com/150"},
]

# --- Cart state ---
if "cart" not in st.session_state:
    st.session_state.cart = []

# --- Display products ---
st.subheader("Products")
cols = st.columns(4)

for i, p in enumerate(products):
    with cols[i]:
        st.image(p["image"], width=150)
        st.write(f"**{p['name']}**")
        st.write(f"💲 {p['price']}")
        if st.button(f"Add to Cart #{i}", key=f"add_{i}"):
            st.session_state.cart.append(p)
            st.success(f"Added {p['name']} to cart!")

# --- Cart Section ---
st.subheader("🛒 Your Cart")

if len(st.session_state.cart) == 0:
    st.info("Your cart is empty.")
else:
    total = 0
    for item in st.session_state.cart:
        st.write(f"- {item['name']} — ${item['price']}")
        total += item["price"]

    st.write(f"### Total: **${total:.2f}**")

    if st.button("Clear Cart"):
        st.session_state.cart = []
        st.success("Cart cleared!")
