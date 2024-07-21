import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqtf, floors) {
    super(sqtf);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
