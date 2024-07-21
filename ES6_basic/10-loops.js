/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
  const new_array = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    new_array[idx] = appendString + value;
  }

  return new_array;
}
