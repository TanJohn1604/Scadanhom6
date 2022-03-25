import { Component, OnInit } from '@angular/core';
import * as Chartist from 'chartist';
import { AngularFireDatabase } from '@angular/fire/database';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  mintemp =0
  maxtemp=0
  temp3pos=0

  mintemp2
  maxtemp2

  mintemp3
  maxtemp3

  mintem4=0
  maxtemp4=0
  temp=0

  url
  mask

 timeStamp
  constructor(private db:AngularFireDatabase) { }
  
  ngOnInit() {
    this.read();
  }

  writemin(){
    this.mintemp2="\""+ this.mintemp + "\""
    this.db.object("node1/min").set(this.mintemp2)
  }

  writemax(){
    this.maxtemp2="\""+ this.maxtemp + "\""
    this.db.object("node1/max").set(this.maxtemp2)
  }

  read(){

    this.db.object("/node3/mask").valueChanges().subscribe(
      mas=>{
        this.mask=mas
        this.timeStamp = (new Date()).getTime();
      }
    )

    this.db.object("/node/url").valueChanges().subscribe(
      url=>{
        this.url=url
        
      }
    )


    this.db.object('/node1/min').valueChanges().subscribe(
    courses=>{this.mintemp3=String(courses).slice(1,-1)
      
    }    
  )
  this.db.object('/node1/max').valueChanges().subscribe(
    courses=>{this.maxtemp3=String(courses).slice(1,-1)
      
    }    
  )

  this.db.object('/node/1').valueChanges().subscribe(
    courses=>{this.temp= Number(courses)
      this.mintem4=Number(this.mintemp3)
      this.maxtemp4=Number(this.maxtemp3)

      
      // if(this.temp<this.mintem4 && this.temp3pos==0){
      //   this.temp3pos=1
      //   // this.db.object("node2/error").set(1)
      // }
      // if (this.temp>this.maxtemp4 && this.temp3pos==0) {
      //   this.temp3pos=2
      //   // this.db.object("node2/error").set(1)
        
      // } 
      
    }    

    
  )

  this.db.object('/node2/error').valueChanges().subscribe(
    courses=>{
      

      
      if(this.temp<this.mintem4 && courses=="1"){
        this.temp3pos=1
        // this.db.object("node2/error").set(1)
      }
      if (this.temp>this.maxtemp4 && courses=="1") {
        this.temp3pos=2
        // this.db.object("node2/error").set(1)
        
      } 

      if(courses=="0"){
        this.temp3pos=0
      }
      
    }    

    
  )

}

check(a,b,c){
  if( a<b&&b<c){
    return false
  }
  else{
    return true
  }

}
reset(){
  // this.temp3pos=0
  // if(this.temp<this.mintem4 && this.temp3pos==0){
  //   this.temp3pos=1
  // }
  // if (this.temp>this.maxtemp4 && this.temp3pos==0) {
  //   this.temp3pos=2
    
  // } 
  // if(this.temp3pos==0)
  // {
    this.db.object("node2/error").set(String(0))
  // }
}

resetmask(){
  this.db.object("node3/mask").set(String(0))
}

urlink(){
  return this.url+ '?' + this.timeStamp;
}
}
