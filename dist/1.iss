; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{56B2D8C5-90CB-400D-B41B-47F630F8B55D}
AppName=EunsunRun
AppVersion=1.5
;AppVerName=EunsunRun 1.5
AppPublisher=KPU
AppPublisherURL=www.kpu.ac.kr
AppSupportURL=www.kpu.ac.kr
AppUpdatesURL=www.kpu.ac.kr
DefaultDirName={pf}\EunsunRun
DisableProgramGroupPage=yes
OutputDir=C:\Temp
OutputBaseFilename=MyGame_setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\project\2dgp\dist\mygame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\project\2dgp\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\EunsunRun"; Filename: "{app}\mygame.exe"
Name: "{commondesktop}\EunsunRun"; Filename: "{app}\mygame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\mygame.exe"; Description: "{cm:LaunchProgram,EunsunRun}"; Flags: nowait postinstall skipifsilent

