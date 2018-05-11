`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.05.2018 15:57:03
// Design Name: 
// Module Name: top
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module top(
    input [3:0] switches,
    output [3:0] leds,
    input board_clk
    );

reg [15:0] conter_clk = 'b0 ;
//assign leds =  switches;

assign leds =  conter_clk[15:12];

always @(posedge board_clk)
      conter_clk <= conter_clk + 1'b1;
   
endmodule
