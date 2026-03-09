let cart = {};

function addToCart(name, price) {
    if (cart[name]) {
        cart[name].qty += 1;
    } else {
        cart[name] = { price: price, qty: 1, notes: '' };
    }
    renderCart();
}

function removeFromCart(name) {
    delete cart[name];
    renderCart();
}

function updateQuantity(name, qty) {
    if (qty <= 0) {
        removeFromCart(name);
    } else {
        cart[name].qty = qty;
        renderCart();
    }
}

function updateCustomization(name) {
    const notes = document.getElementById(`notes-${name}`).value;
    if (cart[name]) {
        cart[name].notes = notes;
    }
}

function renderCart() {
    let cartDiv = document.getElementById("cart-items");
    let subtotal = 0;
    let itemsList = [];
    let customizationList = [];
    let itemCount = 0;

    cartDiv.innerHTML = "";

    if (Object.keys(cart).length === 0) {
        cartDiv.innerHTML = '<div class="no-items"><p>Your cart is empty</p></div>';
    } else {
        for (let item in cart) {
            let itemTotal = cart[item].price * cart[item].qty;
            subtotal += itemTotal;
            itemCount += cart[item].qty;
            itemsList.push(`${item} x${cart[item].qty}`);
            
            if (cart[item].notes) {
                customizationList.push(`${item}: ${cart[item].notes}`);
            }

            cartDiv.innerHTML += `
                <div class="cart-item">
                    <div style="flex: 1;">
                        <div class="cart-item-name">${item}</div>
                        <div style="display: flex; gap: 10px; align-items: center; margin-top: 8px;">
                            <button style="background: #f0f0f0; border: none; width: 24px; height: 24px; border-radius: 4px; cursor: pointer; font-weight: bold;" onclick="updateQuantity('${item}', ${cart[item].qty - 1})">−</button>
                            <span style="min-width: 20px; text-align: center; font-weight: 600;">${cart[item].qty}</span>
                            <button style="background: #f0f0f0; border: none; width: 24px; height: 24px; border-radius: 4px; cursor: pointer; font-weight: bold;" onclick="updateQuantity('${item}', ${cart[item].qty + 1})">+</button>
                        </div>
                    </div>
                    <div style="text-align: right;">
                        <div class="cart-item-price">₹${itemTotal}</div>
                        <button style="background: #ff6b6b; color: white; border: none; padding: 4px 8px; border-radius: 4px; cursor: pointer; font-size: 11px; margin-top: 8px;" onclick="removeFromCart('${item}')">Remove</button>
                    </div>
                </div>
            `;
        }
    }

    // Update totals and form fields
    document.getElementById("subtotal").innerText = subtotal;
    document.getElementById("items").value = itemsList.join(" | ");
    document.getElementById("customization").value = customizationList.join(" | ");
    document.getElementById("total").value = subtotal;
    
    // Enable/disable order button
    const orderBtn = document.getElementById("order-btn");
    if (itemCount > 0) {
        orderBtn.disabled = false;
    } else {
        orderBtn.disabled = true;
    }
}
