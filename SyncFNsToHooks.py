#coding: utf-8
#@category Functions
#@author 

from ghidra.program.model.listing import FunctionManager
from ghidra.program.model.symbol import SourceType
from ghidra.program.model.listing import Parameter

functionList = '''0xb80481c0 custom_wget_1
0xb8048400 custom_wput_1
0xb8048560 vpos
0xb8048595 DMACONR
0xb80485bc VPOSR
0xb80485d3 VPOSW
0xb8048604 VHPOSR
0xb8048630 INTENAR
0xb8048640 INTREQR
0xb8048650 sound_start_channel
0xb80486f0 DMACON
0xb8048770 INTENA
0xb80487e0 INTREQ
0xb8048850 POTGO
0xb8048860 POTGOR
0xb80488b0 JOY0DAT
0xb80488d0 vsync_handler
0xb8048930 custom_vsync_handler
0xb8048960 customreset
0xb8048a00 intlev
0xb8048a80 custom_init
0xb8048d50 amigarom
0xb8048d80 sound_handle_timer
0xb8049400 read_ciaa
0xb8049590 ciaa_set_control_a
0xb8049750 ciaa_set_control_b
0xb8049a20 write_ciaa
0xb804a5d0 read_ciab
0xb804a6ec ciab_set_control_a
0xb804a8b0 ciab_set_control_b
0xb804ab90 write_ciab
0xb804b100 init_keyboard
0xb804b4d0 inject_key
0xb804b820 add_keybinding
0xb804bbd0 cia_recalc_events
0xb804c120 putfifo
0xb804c150 getfifo
0xb804c190 cia_handler_timer
0xb804c220 dumpcia
0xb804c4b0 eavesdrop
0xb804c890 write_log
0xb804cb50 LED
0xb804cb60 get_log_fifo
0xb804cba0 get_loglevel
0xb804d7a0 init_m68k
0xb804e7e0 get_disp_ea_020
0xb804e910 MakeFromSR
0xb804eae0 Exception
0xb804edb0 m68k_move2c
0xb804efb0 m68k_movec2
0xb804f1d0 m68k_divl
0xb804f420 m68k_mull
0xb804f5f0 m68k_reset
0xb804f870 do_trace
0xb804fc50 do_specialties
0xb804ff90 execute_normal
0xb8050770 newcpu_showstate
0xb80508d0 get_disp_ea_000
0xb8050900 MakeSR
0xb80509a0 div_unsigned
0xb8050a10 mul_unsigned
0xb8050a70 mmu_op
0xb8050ac0 do_nothing
0xb8050ad0 exec_nostats
0xb8050b80 m68k_run_2a
0xb8050bc0 m68k_go
0xb8089c70 set_fpsr
0xb8089ee0 to_pack
0xb808a030 from_pack
0xb808a160 get_fp_value
0xb808a690 put_fp_value
0xb808b730 get_fp_ad
0xb808b880 fpp_cond
0xb808bb40 fscc_opp
0xb808bc20 fsave_opp
0xb808bd00 frestore_opp
0xb808be40 fpp_opp
0xb808d900 get_fpsr
0xb808d990 fdbcc_opp
0xb808da40 ftrapcc_opp
0xb808da90 fbcc_opp
0xb8112e10 init_comp
0xb8113100 flush
0xb8113ac0 flush_keepflags
0xb8114350 freescratch
0xb8115280 calc_disp_ea_020
0xb8115610 check_for_cache_miss
0xb8115cc0 call68k
0xb8115f60 restartx86
0xb8115ff0 prepare_block
0xb81164d0 build_comp
0xb8117520 flush_icache_hard
0xb8117610 flush_icache
0xb8117740 undo_countdown
0xb8117990 compile_block
0xb8117ce0 checksum_bigstate
0xb8118250 generate_code
0xb8119c70 compile_one_block
0xb811bd90 kill_rodent
0xb811bdd0 align_target
0xb811be30 set_cache_state
0xb811be60 get_cache_state
0xb811be70 get_jitted_size
0xb811be90 alloc_cache
0xb811bf20 register_finish
0xb811bf90 finished_x86
0xb811c090 startx86
0xb811c0d0 check_inline
0xb811c150 add_state_code
0xb811c1d0 find_state_code
0xb811c1f0 comp_get_fp_value
0xb811c6e0 comp_put_fp_value
0xb811cbe0 comp_fp_ad
0xb811cd10 comp_fscc_opp
0xb811cea0 comp_fbcc_opp
0xb811d050 comp_fsave_opp
0xb811d060 comp_frestore_opp
0xb811d070 comp_fpp_opp
0xb811dc00 comp_fdbcc_opp
0xb811dc10 comp_ftrapcc_opp
0xb811fcb0 put_config
0xb811ff30 get_config
0xb8120040 get_next_key
0xb8120210 wipe_config
0xb8120900 map_x86_irq
0xb8120b70 handle_ps2
0xb8120ce0 init_ps2
0xb8120f40 x86_interrupt
0xb8121fe0 generic_custom_lget_1
0xb81220c0 generic_custom_wget_1
0xb81223b0 generic_custom_lput_1
0xb81224d0 generic_custom_wput_1
0xb8122e00 init_native_mem
0xb81235a0 extended_bget
0xb8123860 extended_lget
0xb8123b50 extended_bput
0xb8123da0 extended_lput
0xb8123f90 sleep_on_sleeplist
0xb81241c0 amithlon_sanabeginio
0xb8124270 unit_to_index
0xb8124430 stop_the_clones
0xb8124550 amithlon_hardopen
0xb8124680 do_scsi_command
0xb81249e0 do_scsi_rw
0xb8124c30 amithlon_scsibeginio
0xb8125150 amithlon_hardbeginio
0xb812ab70 amithlon_hardinit
0xb812b4b0 elf_read_bytes
0xb812b6e0 elf_close
0xb812b7b0 elf_open_afile
0xb812b890 object_size
0xb812b9d0 elf_add_symbol
0xb812bb30 find_sym
0xb812bb80 load_object
0xb812c280 elf_find_symbol_1
0xb812c3e0 open_elf_1
0xb812cf60 wipe_mem
0xb812d150 get_xintmask
0xb812d160 set_config_word
0xb812d230 change_config_word
0xb812d270 schedule_timers
0xb812d3e0 fiddle_50hz
0xb812d430 set_sound_timer
0xb812d4e0 cia_schedule_timer
0xb812d500 unhook_int
0xb812d5a0 close_all_intfd
0xb812d5d0 set_irq_state
0xb812d5e0 inc_pend
0xb812d600 trigger_aint
0xb812d640 da_deliver_pend
0xb812d6d0 remove_pending_ints
0xb812d6f0 da_maybe_reenable
0xb812d7b0 aio_interrupt
0xb812d7c0 set_timer_abs
0xb812d820 set_timer_rel
0xb812daf0 conditional_fopen
0xb812db70 map_x86_mem
0xb812dc50 da_set_special
0xb812dc80 da_unset_special
0xb812dcb0 set_hardware_clock
0xb812dd70 extended_wget
0xb812dd90 extended_wput
0xb812ddb0 wakeup_one_sleeplist
0xb812de00 add_sleeplist
0xb812de30 wakeup_sleeplist
0xb812df20 handle_iolist
0xb812dfc0 amithlon_x86cb
0xb812e000 amithlon_sanainit
0xb812e050 amithlon_sanaopen
0xb812e0b0 amithlon_sanaclose
0xb812e100 amithlon_sanaabortio
0xb812e110 saveread
0xb812e180 savewrite
0xb812e280 checksum_block
0xb812e2e0 device_to_unit
0xb812e360 amithlon_hardclose
0xb812e3b0 amithlon_hardabortio
0xb812e400 notify_write_logfifo
0xb812e410 notify_screendump_requested
0xb812e5d0 elf_read_string
0xb812e630 elf_read_sectionheader
0xb812e660 elf_read_sym
0xb812e680 elf_read_rel
0xb812e6a0 elf_read_elfheader
0xb812e700 get_eobject
0xb812e730 elf_open_file
0xb812e770 elf_open_mem
0xb812e7d0 find_sym_ind
0xb812e7f0 close_elf_1
0xb81340e0 powerfb_init
0xb8134ba0 fb_softreset
'''

print "Starting to sync"

# Get the FunctionManager
fm = currentProgram.getFunctionManager()

for line in functionList.splitlines():
    # print "line:" + line
    pieces = line.split(' ')
    #
    print "src address:" + pieces[0]
    print "destination function:" + pieces[1]

    # Get address from String
    srcAddress = currentProgram.getAddressFactory().getAddress(pieces[0])
    # Get a function at a certain address
    srcFunc = fm.getFunctionAt(srcAddress)
    print "src function at address:" + srcFunc.getName()

    # find dest
    try:
        functions = fm.getFunctions(True)
        for f in functions:
            # print(f.getSignature().getPrototypeString())
            if pieces[1] == f.getName():
                print "destination found:" + f.getName()
                destAddress = f.getEntryPoint()
                print "--> addr:" + destAddress.toString()

                parameterCountDest = f.getParameterCount()
                parameterCountSrc = srcFunc.getParameterCount()
                f.setReturnType(srcFunc.getReturnType(), srcFunc.getSignatureSource())
                f.setCallingConvention(srcFunc.getCallingConventionName())
                for ii in reversed(range(parameterCountDest)):
                    f.removeParameter(ii)
                for ii in range(parameterCountSrc):
                    parameter = srcFunc.getParameter(ii)
                    f.addParameter(parameter, SourceType.USER_DEFINED)
                break
    except Exception as error:
        print "Error: " + repr(error)

print "Finished with sync"