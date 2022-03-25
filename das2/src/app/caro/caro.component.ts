import { Component, OnInit } from '@angular/core';
import { NgbCarouselConfig } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-caro',
  templateUrl: './caro.component.html',
  styleUrls: ['./caro.component.scss']
})
export class CaroComponent implements OnInit {
  images = [
    {title: 'Nvidia', short: 'Jetson Nano Dev Kit', src: "assets/img/zson.jpg"},
    {title: 'Espressif Systems', short: 'ESP8266 NodeMCU', src: "assets/img/esp.jpg"},
    {title: 'C270 + LM35 + Buzzer5v + Led', short: '', src: "assets/img/cam.jpg"}
  ];
  constructor(config: NgbCarouselConfig) {
    config.interval = 2000;
    config.keyboard = true;
    config.pauseOnHover = true;
  }

  ngOnInit(): void {
  }

}
