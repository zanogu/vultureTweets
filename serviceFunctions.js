// JavaScript Document


// BETWEEN

Number.prototype.between  = function (a, inclusive) {
    var min = Math.min.apply(Math, a),
        max = Math.max.apply(Math, a);
    return inclusive ? this >= min && this <= max : this > min && this < max;
};

			
// DATA


	function getBase(startTime){
				
				
				var zero = Math.floor(startTime/everySec)*everySec;
				
				
				return zero; 

				
				}
			
			function getColumn(uTime, startTime) {
				//var a =  new Date(uTime*1000);
				var res = Math.floor((uTime - startTime)/everySec);
				return (res > 0) ? res : 0;  
				
				
				}
				
			function calculateRangeX(sTime,eTime,interval)
			{
				var r = Math.ceil(eTime/interval) - Math.floor(sTime/interval);
				return r;}
				
				
				
			function timeExtract (sTime,eTime, d)
			{
				var nd =  $.deepclone(d);
				for(i = nd.length - 1; i >= 0 ; i--){
					if (parseInt(nd[i].date) < sTime || parseInt(nd[i].date) > eTime  ){
						nd.splice(i,1);
					}
					
				}
				
				return nd;
			}
			
			function timeExtractArray (sT, eT, d)
			{
				
				var dn = $.deepclone(d);
			
				
				
				for(ii = dn.length - 1; ii >= 0 ; ii--){
					
					dn[ii].data = timeExtract(sT, eT, dn[ii].data);
					recalculateCumDeathsInArea(dn[ii].data);
					
					
					
				}
					
				return dn;
				
					
				}
				
				
			function repairTime (d)
				{
					d.forEach(function(ddd) { ddd.date = ddd.date * 1000; });
					} 	
					
					
					
			function recalculateCumDeathsInArea(d)
			{
				
				
				minDeaths = d3.min( d, function(d1){
										return parseInt(d1.cumDeaths)});
										
				console.log("mindeaths:" + minDeaths)
				for(i = d.length - 1; i >= 0 ; i--){
					d[i].cumDeaths -= minDeaths;
					}
				
				
				
				
				}
				
			
			function getMin(d)
			{
				
				
				minDeaths = d3.min( d, function(d1){
										return parseInt(d1.cumDeaths)});
										
			
				
				
				return minDeaths;
				
				}
				
				
			function getMax(d)
			{
				
				
				minDeaths = d3.max( d, function(d1){
										return parseInt(d1.cumDeaths)});
										
			
				
				
				return minDeaths;
				
				}
				

/// move to front

d3.selection.prototype.moveToFront = function() {
  return this.each(function(){
    this.parentNode.appendChild(this);
  });
};



d3.selection.prototype.moveToBack = function() { 
    return this.each(function() { 
        var firstChild = this.parentNode.firstChild; 
        if (firstChild) { 
            this.parentNode.insertBefore(this, firstChild); 
        } 
    }); 
};


// clone d3 element

function clone_d3_selection(selection, i) {
            // Assume the selection contains only one object, or just 	
            // on the first object. 'i' is an index to add to the id of the
            // newly cloned DOM element.
    var attr = selection.node().attributes;
    var length = attr.length;
    var node_name = selection.property("nodeName");
    var parent = d3.select(selection.node().parentNode);
    var cloned = parent.append(node_name)
                 .attr("id", selection.attr("id") + i);
    for (var j = 0; j < length; j++) { // Iterate on attributes and skip on "id"
        if (attr[j].nodeName == "id") continue;
        cloned.attr(attr[j].name,attr[j].value);
    }
    return cloned;
}
			


function getTweetsByTime (time, cl) {
				var format1 = d3.time.format("%b_%d");
				console.log(time);

				var date = new Date(time);
				
				var dayString = format1(date);
				var filename = cl + "_" + dayString + ".tsv";

				

				d3.tsv(filename, function(data) {

					//console.log(data);


					var closestTime = 0;
					var closestElement;

					data.forEach(function (element, index, array) {

						var elementTime = parseFloat(element.unixTime)*1000;

						

						if (Math.abs(closestTime - time) > Math.abs(elementTime - time) ) {

							closestTime =   elementTime;
							

							closestElement = element;


						};
					});

				console.log(closestElement);
	
				

				return closestElement;


				});






}	


function getTweetsByTimeSent (time, cl,sent, sentBorder, callback) {
				
				var format1 = d3.time.format("%b_%d");
				console.log(time);

				var date = new Date(time);
				
				var dayString = format1(date);
				var filename = cl + "_" + dayString + ".tsv";

				var interval = [-1, 1];

				if (sent == "neg"){
					interval = [-1, -Math.abs(sentBorder)];
				}
				else if (sent == "neu"){
					interval = [ -Math.abs(sentBorder),  Math.abs(sentBorder)];
				}
				else if (sent == "pos"){
					interval = [ Math.abs(sentBorder), 1];
				}

				d3.tsv(filename, function(data) {

					//console.log(data);


					var closestTime = 0;
					var closestElement;

					data.forEach(function (element, index, array) {

						var elementTime = parseFloat(element.unixTime)*1000;
						var sentiment = parseFloat(element.sentiment);

						

						if (Math.abs(closestTime - time) > Math.abs(elementTime - time) && sentiment.between(interval, true) ) {

							closestTime =   elementTime;
							

							closestElement = element;


						}

					

					
					});

				//console.log(closestElement);
				callback(closestElement);

				//console.log(closestTime);
				return closestElement;

				
				

				






				});






}	
				