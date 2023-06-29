const get_customer_data = async (endpoint,customer_id) => {
    try {
      const response = await fetch(`/${endpoint}/${customer_id}`);
      if (!response.ok) {
        throw new Error('Network response was not OK');
        }
      const data = await response.json();
      return data;
    } catch (error) {
      // Handle the error here
      console.error('Error fetching customer data:', error);
    }
  };

const process_customer_orders = async (customer_id) => {
    const customer_orders = await get_customer_data("orders",customer_id);
    const customer_tlv = await get_customer_data("customer_tlv",customer_id);
    const orders_subtotal = customer_orders.reduce((total, product) => total + product.subtotal, 0);
    const discount = (orders_subtotal * customer_tlv["discount"]) / 100
    const total = orders_subtotal - discount
    populate_customer(customer_orders);
    populate_totals (orders_subtotal,discount,total);
}

const populate_customer = (selected_customer_data) => {
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
     selected_customer_data.forEach((line) => {
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

const populate_totals = (sub_total, discount, total) => {
    const totals_detail = document.querySelector("#totals_detail");
    totals_detail.innerHTML = ""
    totals_detail.innerHTML = `
    <h4 >Total Order $${(sub_total / 100).toFixed(2)} </h4>
    <h4 >Discount $${(discount / 100).toFixed(2)} </h4>
    <hr>
    <h4 >To Pay $${(total / 100).toFixed(2)} </h4>
    <button class="btn btn-secondary text-right"> Pay Now </button>
    `
}



