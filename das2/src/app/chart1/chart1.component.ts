import { Component, OnInit } from '@angular/core';

import { ChartDataSets,ChartType, ChartOptions } from 'chart.js';
import { Color, Label } from 'ng2-charts';
import { AngularFireDatabase } from '@angular/fire/database';
import { interval } from 'rxjs';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-chart1',
  templateUrl: './chart1.component.html',
  styleUrls: ['./chart1.component.scss']
})
export class Chart1Component implements OnInit {
  data=[25, 24, 27,28,24,25,26,27,25,23,25, 24, 27,28,24,25,26,27,25,23]
  label=['1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'];
  updateCount=20;
  numberElements=20;
  sub:any
 
  lineChartData = [
  { data: this.data, label: 'Nhiệt độ (°C)' },
  
];
lineChartLabels = this.label;
  
 lineChartOptions:ChartOptions = {
  responsive: true,
  animation:{
    duration:0
  }
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
        this.temp= courses
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
