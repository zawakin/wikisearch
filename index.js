$(function(){

	console.log(encodeURI("焼売"));
	console.log(encodeURIComponent("焼売"));
	
	var wikiurl = "http://ja.wikipedia.org/w/api.php";
	//wikiurl = "https://ja.wikipedia.org/w/api.php?action=query&list=backlinks&format=json&bltitle=焼売";
	//wikiurl = "https://ja.wikipedia.org/w/api.php?action=query&list=backlinks&format=json&bltitle=perfume";

			
	var BackLink = (function(){
		var BackLink = function(){
			this.blList = ["初音ミク"];
			this.depth = 0;
			this.maxdepth = 2;
			this.nextIndex = 0;
			this.n = 0;
		};
		
		
		var p = BackLink.prototype;
		
		p.Start = function(){
			this.Next();
		};
		
		p.Next = function(){
			console.log(this.depth);
			if(this.depth >= this.maxdepth){
				console.log("finish");	
				return;
			}
			
			this.n = this.blList.length;
			
			for(var i=this.nextIndex;i<this.n;i++){
				this.BackLinkSearch(this.blList[i]);
			}
		
			this.nextIndex = this.n;
			this.depth ++ ;
				
			
		};
		
		p.BackLinkSearch = function(title){
				
			var self = this;
			var blList = this.blList;
			var data =  {
				"action":"query",
				"list":"backlinks",
				"format":"json",
				"bltitle":title,
				"bllimit":"max"
				};
			$.ajax({
				type:"GET",
				dataType:"jsonp",
				url: wikiurl,
				data:data,
				async:false
			}).done(function(data){ //ajaxの通信に成功した場合
				//alert("success!");
				for(bl of data.query.backlinks){
					if($.inArray(bl.title,blList)==-1){
						//console.log(bl.title);
						blList.push(bl.title);
						//console.log(blList.length);
						$("#results").append(bl.title + "<br>");
					}
				}
				self.Next();
		//		$("#results").append(bl);
			
				
			}).fail(function(data){ //ajaxの通信に失敗した場合
				console.log("error!");
			});	
		}
		
		return BackLink;
	})();
	
var bl = new BackLink();
bl.Start();
	
});