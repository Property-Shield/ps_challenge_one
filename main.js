const fs = require('fs');
const geolib = require('geolib'); // for geodistance calculation

// Assuming markets is an array of market objects with name, latitude, and longitude
const markets = JSON.parse(fs.readFileSync('markets.json'));

function getClosestMarket(lat, lon) {
    // Calculate the closest market using geodistance
    return markets.reduce((prev, curr) => {
        const prevDistance = geolib.getDistance({latitude: lat, longitude: lon}, prev);
        const currDistance = geolib.getDistance({latitude: lat, longitude: lon}, curr);
        return (prevDistance < currDistance) ? prev : curr;
    });
}

function processCompanyData(day) {
    let properties = getCompanyDataFeedsForDay(day);
    let snapshot = JSON.parse(fs.readFileSync(`data/snapshots/day_${day - 1}.json`));

    properties = properties.map(property => {
        // Check for market attribute
        if (property.market && markets.includes(property.market)) {
            property.market = property.market;
        } else {
            property.market = getClosestMarket(property.latitude, property.longitude);
        }

        // Check for duplicate addresses
        if (snapshot.find(p => p.address === property.address)) {
            return null;
        }

        // Track status of property
        property.status = snapshot.find(p => p.id === property.id) ? 'off_market' : 'actively_listed';

        // Ensure typing is compliant with the Simple List system
        // This would depend on the specifics of your data and requirements

        return property;
    });

    // Remove null values (duplicates)
    properties = properties.filter(property => property !== null);

    generateSnapshotForDay(day, ...properties);
}

for (let day = 0; day < 3; day++) {
    processCompanyData(day);
}