import { Component } from '@angular/core';
import {TechsService} from './services/techs.service';


@Component({
    moduleId: module.id,
    selector: 'my-app',
    templateUrl: 'app.component.html',
    providers: [TechsService]
})
export class AppComponent { }
