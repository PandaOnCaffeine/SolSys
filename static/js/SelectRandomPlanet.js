function selectRandomPlanet() {
    var planets = [
      "Mercury",
      "Venus",
      "Earth",
      "Mars",
      "Jupiter",
      "Saturn",
      "Uranus",
      "Neptune"
    ];
  
    var randomIndex = Math.floor(Math.random() * planets.length);
    var randomPlanet = planets[randomIndex];
  
    var randomPlanetElement = document.getElementById("randomPlanet");
    randomPlanetElement.textContent = "You have to shoot: " + randomPlanet;
  }