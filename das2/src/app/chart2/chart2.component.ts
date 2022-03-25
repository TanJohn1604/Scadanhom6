import { Component, OnInit } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/database';
import { interval } from 'rxjs';

import { ChartDataSets,ChartType, ChartOptions } from 'chart.js';




@Component({
  selector: 'app-chart2',
  templateUrl: './chart2.component.html',
  styleUrls: ['./chart2.component.scss']
})
export class Chart2Component implements OnInit {

  data=[0, 0, 0,0,0,0,0,0,0]
  label=['1', '2','3','4','5','6','7','8','9'];
  updateCount=0;
  numberElements=20;
  sub:any

  
  lineChartData = [
    { data: this.data, label: 'Hiệu điện thế động cơ (V)' },
    
  ];
  lineChartLabels = this.label;
    
   lineChartOptions:ChartOptions = {
    
    responsive: true,
    animation:{
      duration:0
    },

  };
     
   lineChartLegend = true;
   lineChartType:ChartType = 'line';
   lineChartPlugins = [];
  
  
  
  
  // courses:any[];
  courses2:any;
  // co:any;
  temp:any;


  constructor(private db:AngularFireDatabase) { }

  ngOnInit(): void {
    this.read();
    this.updateData();
  }
  read(){
    this.db.object('/node/1').valueChanges().subscribe(
    courses=>{
      this.temp= Number(courses)
      this.courses2=courses;
      console.log(this.courses2);
      this.addData({
        "xA":courses
      })
      
    }
  )
  
}
addData(data : {}){
if(data){
 this.label.push(String(new Date().toLocaleTimeString()));
 this.data.push(data['xA'])
  if(this.updateCount>this.numberElements){
    this.label.shift();
    this.data.shift();
  }
  else{
    this.updateCount++;
  }
  

}
}
updateData(){
  this.sub = interval(1000)
  .subscribe(
    (val) => { 
      console.log('called');
   
      this.label.push(String(new Date().toLocaleTimeString()));
      this.data.push(this.temp)
       if(this.updateCount>this.numberElements){
         this.label.shift();
         this.data.shift();
       }
       else{
         this.updateCount++;
       }
    }      
    );
  
  

 
}
}
