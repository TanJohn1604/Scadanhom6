import { ComponentFixture, TestBed } from '@angular/core/testing';

import { History1Component } from './history1.component';

describe('History1Component', () => {
  let component: History1Component;
  let fixture: ComponentFixture<History1Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ History1Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(History1Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
