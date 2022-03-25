import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CaroComponent } from './caro.component';

describe('CaroComponent', () => {
  let component: CaroComponent;
  let fixture: ComponentFixture<CaroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CaroComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CaroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
