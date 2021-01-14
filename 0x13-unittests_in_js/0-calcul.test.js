const calculateNumber = require('./0-calcul')
const assert = require('assert');

describe('calculateNumber step 1', () => {
    it('checks ouput', () => {
        assert.strictEqual(calculateNumber(1.5, 2.1), 4);
    });
})

describe('calculateNumber step 2', () => {
    it('checks ouput part2', () => {
        assert.strictEqual(calculateNumber(0, 0.0), 0);
    });
})

describe('calculateNumber step 2 negatives', () => {
    it('Checks Negatives Numbers', ()=> {
        assert.strictEqual(calculateNumber(-10, -5), -15);
    });
})

describe('calculateNumber step 3 negatives v2', () => {
    it('Checks Negatives Numbers part2', ()=> {
        assert.strictEqual(calculateNumber(-2, -2), -4);
    });
})

describe('Coverts to number', () => {
    it('If can convert to number', ()=> {
        assert.strictEqual(isNaN(calculateNumber(5)), true);
    });
})

describe('Coverts to number part2', () => {
    it('If can convert to number part2', ()=> {
        assert.strictEqual(isNaN(calculateNumber('string')), true)
    });
})