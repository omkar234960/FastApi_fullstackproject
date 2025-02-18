const baseUrl = 'http://127.0.0.1:8000';

const fetchProducts = async () => {
    const response = await fetch(`${baseUrl}/products/`);
    const products = await response.json();
    const productList = document.getElementById('productList');
    productList.innerHTML = '';

    products.forEach(product => {
        const listItem = document.createElement('li');
        listItem.textContent = `ID: ${product.id} | Name: ${product.name} | Add: ${product.add} | Quantity: ${product.Quantity} | Price: ${product.price}`;
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = () => deleteProduct(product.id);
        listItem.appendChild(deleteButton);
        productList.appendChild(listItem);
    });
};

document.getElementById('addProductForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const newProduct = {
        name: document.getElementById('name').value,
        add: document.getElementById('add').value,
        Quantity: parseInt(document.getElementById('quantity').value),
        price: parseFloat(document.getElementById('price').value),
        date_added: document.getElementById('date_added').value
    };

    await fetch(`${baseUrl}/productadd/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newProduct)
    });

    event.target.reset();
    fetchProducts();
});

document.getElementById('updateProductForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    const productId = document.getElementById('updateProductId').value;
    const updatedProduct = {
        name: document.getElementById('updateName').value,
        add: document.getElementById('updateAdd').value,
        Quantity: parseInt(document.getElementById('updateQuantity').value),
        price: parseFloat(document.getElementById('updatePrice').value)
    };

    await fetch(`${baseUrl}/product/${productId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(updatedProduct)
    });

    event.target.reset();
    fetchProducts();
});

const deleteProduct = async (id) => {
    await fetch(`${baseUrl}/product/${id}`, {
        method: 'DELETE'
    });
    fetchProducts();
};

// Initial fetch
fetchProducts();
