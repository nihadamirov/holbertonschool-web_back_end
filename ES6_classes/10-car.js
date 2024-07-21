export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Cls = this.constructor[Symbol.species];
    return new Cls(this._brand, this._motor, this._color);
  }
}
