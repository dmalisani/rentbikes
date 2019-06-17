# rentbikes
Test for an Applicattion

## Install
```
git clone https://github.com/dmalisani/rentbikes.git
pip install -r requirements.txt
```


## Usage
You can use for get quotes and for set rent
* getquote(\<bikes>, \<start_datetime>, \<end_datetime>) returns a number (_float or int [it depends of rate cofiguration]_)
* rent_instance = Rent(\<Name of customer>,  [identification])
* rent_instance.add_rented_period(\<bikes>, \<start_datetime>, \<end_datetime>)
* rent_instance.rented_periods will has as list with data of each period


### Example
```
rent = Rent("daniel", 23)
period = rent.add_rented_period(1, "2019-06-01T16:00", "2019-06-01T20:00")
print(period.bikes, period.paid)
```
