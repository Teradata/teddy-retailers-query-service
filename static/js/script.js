const load_data = () => {
    fetch('/static/mock_data/orders.json')
    .then(response => response.json())
    .then(data => {
        // Now you can access the orders data
        mock_data = data;
        // Do further processing with the data here
    })
    .catch(error => {
        // Handle any errors that occurred during the fetch
        console.error('Error:', error);
    });
}

const get_customer_data = (customer_id) => {
    //make request to get customer data to backend
    console.log() //the customer data
}

const get_customer_discount = () => {
    //make request to get customer discount to backend
    console.log()
}

const populate_customer = (customer_id) => {
    const selected_customer_data = mock_data.orders.find((order) => {return order.customer === customer});
    const table_orders = document.querySelector("#orderTable");
    table_orders.innerHTML = "";
    const heading_row = document.createElement("tr");
    heading_row.innerHTML = `
        <th>Product Code</th>
        <th>Product Name</th>
        <th>Quantity</th>
        <th>Price</th>
    `;
    table_orders.appendChild(heading_row)
    selected_customer_data.lines.forEach((line) => {
        const newRow = document.createElement("tr");
        newRow.innerHTML = `
          <td>${line.product_code}</td>
          <td>${line.product_name}</td>
          <td>${line.quantity}</td>
          <td>$${(line.subtotal / 100).toFixed(2)}</td>
        `;
        table_orders.appendChild(newRow);
      });
}

let mock_data = "";
load_data();
console.log(mock_data);



