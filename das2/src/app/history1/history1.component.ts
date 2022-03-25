import { Component, OnInit } from '@angular/core';
import { AngularFireDatabase } from '@angular/fire/database';
import { range } from 'rxjs';
import * as XLSX from 'xlsx';

export interface PeriodicElement {
  time: string;
  position: number;
  value: number;
  
}


@Component({
  selector: 'app-history1',
  templateUrl: './history1.component.html',
  styleUrls: ['./history1.component.scss']
})
export class History1Component implements OnInit {
  
  temp 
  temp2
  ELEMENT_DATA: PeriodicElement[] = [
    {position: 1, time: 'Hydrogen', value: 1.0079},
    
  ];

  displayedColumns: string[] = ['position', 'time', 'value'];
  dataSource = this.ELEMENT_DATA;

  dataSource2 = this.ELEMENT_DATA;
  constructor(private db:AngularFireDatabase) { }

  ngOnInit(): void {
    this.read();
    this.read2()
  }

  read(){
    this.db.object('/node_backup').valueChanges().subscribe(
    courses=>{
    this.temp= courses
    console.log(courses)
    this.dataSource = [
      {position: 0, time: courses[0]['time'], value: courses[0]['value']},
      {position: 1, time: courses[1]['time'], value: courses[1]['value']},
      {position: 2, time: courses[2]['time'], value: courses[2]['value']},
      {position: 3, time: courses[3]['time'], value: courses[3]['value']},
      {position: 4, time: courses[4]['time'], value: courses[4]['value']},
      {position: 5, time: courses[5]['time'], value: courses[5]['value']},
      {position: 6, time: courses[6]['time'], value: courses[6]['value']},
      {position: 7, time: courses[7]['time'], value: courses[7]['value']},
      {position: 8, time: courses[8]['time'], value: courses[8]['value']},
      {position: 9, time: courses[9]['time'], value: courses[9]['value']},
      {position: 10, time: courses[10]['time'], value: courses[10]['value']},
      {position: 11, time: courses[11]['time'], value: courses[11]['value']},
      {position: 12, time: courses[12]['time'], value: courses[12]['value']},
      {position: 13, time: courses[13]['time'], value: courses[13]['value']},
      {position: 14, time: courses[14]['time'], value: courses[14]['value']},
      {position: 15, time: courses[15]['time'], value: courses[15]['value']},
      {position: 16, time: courses[16]['time'], value: courses[16]['value']},
      {position: 17, time: courses[17]['time'], value: courses[17]['value']},
      {position: 18, time: courses[18]['time'], value: courses[18]['value']},
      {position: 19, time: courses[19]['time'], value: courses[19]['value']},
      
      
    ];
    
    }
    

  )
  
}

read2(){
  this.db.object('/nodebackup2').valueChanges().subscribe(
  courses=>{
  this.temp2= courses
  console.log(courses)
  this.dataSource2 = [
    {position: 0, time: courses[0]['time'], value: courses[0]['value']},
    {position: 1, time: courses[1]['time'], value: courses[1]['value']},
    {position: 2, time: courses[2]['time'], value: courses[2]['value']},
    {position: 3, time: courses[3]['time'], value: courses[3]['value']},
    {position: 4, time: courses[4]['time'], value: courses[4]['value']},
    {position: 5, time: courses[5]['time'], value: courses[5]['value']},
    {position: 6, time: courses[6]['time'], value: courses[6]['value']},
    {position: 7, time: courses[7]['time'], value: courses[7]['value']},
    {position: 8, time: courses[8]['time'], value: courses[8]['value']},
    {position: 9, time: courses[9]['time'], value: courses[9]['value']},
    {position: 10, time: courses[10]['time'], value: courses[10]['value']},
    {position: 11, time: courses[11]['time'], value: courses[11]['value']},
    {position: 12, time: courses[12]['time'], value: courses[12]['value']},
    {position: 13, time: courses[13]['time'], value: courses[13]['value']},
    {position: 14, time: courses[14]['time'], value: courses[14]['value']},
    {position: 15, time: courses[15]['time'], value: courses[15]['value']},
    {position: 16, time: courses[16]['time'], value: courses[16]['value']},
    {position: 17, time: courses[17]['time'], value: courses[17]['value']},
    {position: 18, time: courses[18]['time'], value: courses[18]['value']},
    {position: 19, time: courses[19]['time'], value: courses[19]['value']},
    
    
  ];
  
  }
  

)

}

exportexcel():void{
  const ws:XLSX.WorkSheet=XLSX.utils.json_to_sheet(this.temp);
  const wb:XLSX.WorkBook=XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb,ws,'All Data Export');
  XLSX.writeFile(wb,'CanhBaoNhietDo.xlsx');
}

exportexcel2():void{
  const ws:XLSX.WorkSheet=XLSX.utils.json_to_sheet(this.temp2);
  const wb:XLSX.WorkBook=XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(wb,ws,'All Data Export');
  XLSX.writeFile(wb,'CanhBaoKhauTrang.xlsx');
}

}
