import { expect, test } from "@jest/globals";
import ocean from "./initClient";

beforeEach(async () => {
  await ocean.reset();
});

test("it should list collections", async () => {
  let collections = await ocean.listCollections();
  expect(collections).toBeDefined();
  expect(collections).toBeInstanceOf(Array);
  expect(collections.length).toBe(0);
  const collection = await ocean.createCollection("test");
  collections = await ocean.listCollections();
  expect(collections.length).toBe(1);
});

test("it should create a collection", async () => {
  const collection = await ocean.createCollection("test");
  expect(collection).toBeDefined();
  expect(collection).toHaveProperty("name");
  expect(collection).toHaveProperty('id')
  expect(collection.name).toBe("test");
  let collections = await ocean.listCollections();
  expect([{ name: "test", metadata: null, id: collection.id }]).toEqual(
    expect.arrayContaining(collections)
  );
  expect([{ name: "test2", metadata: null }]).not.toEqual(
    expect.arrayContaining(collections)
  );

  await ocean.reset();
  const collection2 = await ocean.createCollection("test2", { test: "test" });
  expect(collection2).toBeDefined();
  expect(collection2).toHaveProperty("name");
  expect(collection2).toHaveProperty('id')
  expect(collection2.name).toBe("test2");
  expect(collection2).toHaveProperty("metadata");
  expect(collection2.metadata).toHaveProperty("test");
  expect(collection2.metadata).toEqual({ test: "test" });
  let collections2 = await ocean.listCollections();
  expect([{ name: "test2", metadata: { test: "test" }, id: collection2.id }]).toEqual(
    expect.arrayContaining(collections2)
  );
});

test("it should get a collection", async () => {
  const collection = await ocean.createCollection("test");
  const collection2 = await ocean.getCollection("test");
  expect(collection).toBeDefined();
  expect(collection2).toBeDefined();
  expect(collection).toHaveProperty("name");
  expect(collection2).toHaveProperty("name");
  expect(collection.name).toBe(collection2.name);
});

// test("it should get or create a collection", async () => {
//   await ocean.createCollection("test");

//   const collection2 = await ocean.getOrCreateCollection("test");
//   expect(collection2).toBeDefined();
//   expect(collection2).toHaveProperty("name");
//   expect(collection2.name).toBe("test");

//   const collection3 = await ocean.getOrCreateCollection("test3");
//   expect(collection3).toBeDefined();
//   expect(collection3).toHaveProperty("name");
//   expect(collection3.name).toBe("test3");
// });

test("it should delete a collection", async () => {
  const collection = await ocean.createCollection("test");
  let collections = await ocean.listCollections();
  expect(collections.length).toBe(1);
  await ocean.deleteCollection("test");
  collections = await ocean.listCollections();
  expect(collections.length).toBe(0);
});

// TODO: I want to test this, but I am not sure how to
// test('custom index params', async () => {
//     throw new Error('not implemented')
//     await ocean.reset()
//     const collection = await ocean.createCollection('test', {"hnsw:space": "cosine"})
// })
