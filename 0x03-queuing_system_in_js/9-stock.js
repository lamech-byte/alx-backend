const listProducts = [
  { itemId: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { itemId: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { itemId: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { itemId: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
  return listProducts.find(product => product.itemId === id);
}

const express = require('express');
const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});

const redis = require('redis');
const { promisify } = require('util');
const client = redis.createClient();

const reserveStockById = (itemId, stock) => {
  const setAsync = promisify(client.set).bind(client);
  return setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async itemId => {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - currentReservedStock;

  res.json({
    itemId: product.itemId,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentQuantity
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  if (currentReservedStock >= product.stock) {
    res.json({ status: 'Not enough stock available', itemId: itemId });
    return;
  }

  await reserveStockById(itemId, currentReservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  const currentReservedStock = await getCurrentReservedStockById(itemId);
  if (currentReservedStock >= product.stock) {
    res.json({ status: 'Not enough stock available', itemId: itemId });
    return;
  }

  await reserveStockById(itemId, currentReservedStock + 1);
  res.json({ status: 'Reservation confirmed', itemId: itemId });
});
