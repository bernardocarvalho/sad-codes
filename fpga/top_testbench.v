`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 11.05.2018 17:05:35
// Design Name: 
// Module Name: top_testbench
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


module top_testbench;

reg  [3:0]  switches_in=0;
wire  [3:0]  leds_out=0;
reg clk_in = 1'b0;
   
top  dut (
    .switches(switches_in),
    .leds(leds_out),
    .board_clk(clk_in)
);

    // generate a clock
    always     // no sensitivity list, so it always executes
        begin
        clk_in= 1; #5; 
        clk_in= 0; #5; 
    // 10ns period
    end

initial 
    begin   
        switches_in = 4'b0;
        #100
        switches_in = 4'b0010;
    end
                  
endmodule
