const calculateNumber = require('./0-calcul')
const assert = require('assert');

describe('calculateNumber', () => {
    it('checks ouput', () => {
        assert.strictEqual(calculateNumber(1.5, 2.1), 4);
    });
    it('checks ouput', () => {
        assert.strictEqual(calculateNumber(0, 0.0), 0);
    });
    it('Checks Negatives Numbers', ()=> {
        assert.strictEqual(calculateNumber(-10, -5), -15);
    })
    it('Checks Negatives Numbers', ()=> {
        assert.strictEqual(calculateNumber(-2, -2), -4);
    })
    it('If can convert to number', ()=> {
        assert.strictEqual(isNaN(calculateNumber(5)), true);
    })
    it('If can convert to number', ()=> {
        assert.strictEqual(isNaN(calculateNumber('string')), true)
    })
})

