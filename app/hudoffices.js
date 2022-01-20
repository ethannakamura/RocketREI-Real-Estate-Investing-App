function getData(){
    console.log("Hello")
 let city=document.querySelector("#cityselect").value;
 let statecode= document.querySelector("#stateselect").value;
 let countrycode= document.querySelector("#countryselect").value;
 
    
 fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city},${statecode},${countrycode}&appid=1def280a29d59478ec5c51b3f01db79a `)
 .then(response => response.json())
 .then(weatherdata => {
     console.log(weatherdata)
 
     let high= weatherdata.main.temp_max;
     let outputFahrenheit=((high-273.15)*1.8)+32;   
        console.log(high)           
     document.querySelector(`#high-0`).innerHTML=outputFahrenheit.toFixed(2);
 
     let low= weatherdata.main.temp_min;
     let low_1=((low-273.15)*1.8)+32;   
     console.log(low)           
     document.querySelector(`#low-0`).innerHTML=low_1.toFixed(2)
 
  
     let forecast= weatherdata.weather[0].main;
     console.log(forecast)           
     document.querySelector(`#forecast-0`).innerHTML=forecast
 
 
     let humidity= weatherdata.main.humidity;
     console.log(humidity)           
     document.querySelector(`#humidity-0`).innerHTML=humidity
 
 })
 }