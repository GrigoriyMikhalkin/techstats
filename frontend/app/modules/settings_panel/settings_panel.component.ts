import { Component } from '@angular/core';

import {TechsService} from '../../services/techs.service';
import {Tech} from '../../Tech';


@Component({
  moduleId: module.id,
  selector: 'settings',
  templateUrl: 'settings_panel.component.html',
  styleUrls: ['settings_panel.component.css']
})
export class SettingsComponent {
  techs: Tech[];
  title: string;
  isNavOpened = true;

  constructor (private techsService: TechsService) {
    this.techsService.getTechs()
	.subscribe(techs => {
	  this.techs = techs['techs'];
	})
  }

  selectTech (tech: string) {
    console.log(tech);
  }
}
