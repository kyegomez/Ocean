import { expect, test } from "@jest/globals";
import ocean from "./initClient";

test("it should modify collection", async () => {
  await ocean.reset();
  const collection = await ocean.createCollection("test");
  expect(collection.name).toBe("test");
  expect(collection.metadata).toBeUndefined();

  await collection.modify("test2");
  expect(collection.name).toBe("test2");
  expect(collection.metadata).toBeUndefined();

  const collection2 = await ocean.getCollection("test2");
  expect(collection2.name).toBe("test2");
  expect(collection2.metadata).toBeNull();

  // test changing name and metadata independently
  // and verify there are no side effects
  const original_name = "test3";
  const new_name = "test4";
  const original_metadata = { test: "test" };
  const new_metadata = { test: "test2" };

  const collection3 = await ocean.createCollection(
    original_name,
    original_metadata
  );
  expect(collection3.name).toBe(original_name);
  expect(collection3.metadata).toEqual(original_metadata);

  await collection3.modify(new_name);
  expect(collection3.name).toBe(new_name);
  expect(collection3.metadata).toEqual(original_metadata);

  const collection4 = await ocean.getCollection(new_name);
  expect(collection4.name).toBe(new_name);
  expect(collection4.metadata).toEqual(original_metadata);

  await collection3.modify(undefined, new_metadata);
  expect(collection3.name).toBe(new_name);
  expect(collection3.metadata).toEqual(new_metadata);

  const collection5 = await ocean.getCollection(new_name);
  expect(collection5.name).toBe(new_name);
  expect(collection5.metadata).toEqual(new_metadata);
});

test("it should store metadata", async () => {
  await ocean.reset();
  const collection = await ocean.createCollection("test", { test: "test" });
  expect(collection.metadata).toEqual({ test: "test" });

  // get the collection
  const collection2 = await ocean.getCollection("test");
  expect(collection2.metadata).toEqual({ test: "test" });

  // get or create the collection
  const collection3 = await ocean.getOrCreateCollection("test");
  expect(collection3.metadata).toEqual({ test: "test" });

  // modify
  await collection3.modify(undefined, { test: "test2" });
  expect(collection3.metadata).toEqual({ test: "test2" });

  // get it again
  const collection4 = await ocean.getCollection("test");
  expect(collection4.metadata).toEqual({ test: "test2" });
});
