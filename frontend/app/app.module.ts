import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';
import { MaterialModule } from '@angular/material';

import { ChartModule } from 'primeng/primeng';

import { AppComponent }  from './app.component';
import { SettingsComponent } from './modules/settings_panel/settings_panel.component';
import { TimegraphComponent } from './modules/graphs/timegraph.component';


@NgModule({
  imports: [ BrowserModule, HttpModule, MaterialModule.forRoot(), ChartModule],
  declarations: [ AppComponent, SettingsComponent, TimegraphComponent],
  bootstrap: [ AppComponent ],
  providers: []
})
export class AppModule { }
