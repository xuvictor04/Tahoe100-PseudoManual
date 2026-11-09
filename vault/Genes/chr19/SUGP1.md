---
symbol: "SUGP1"
type: "gene"
col: 2649
ensembl_id: "ENSG00000105705"
name: "SURP and G-patch domain containing 1"
location: "19p13.11"
module: 20
arm: "-"
pooled_cpm: 27.85
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SUGP1

*SURP and G-patch domain containing 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.64× (z +17.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.651× (z -7.9, q 1e-12, down in 29 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW1417 0.177×, HCT15 0.158×, Panc 03.27 0.298×, KATO III 0.190×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1792 0.205×, H4 0.117×, SW1417 0.310×, LS 180 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.215×, CFPAC-1 0.242×, RPMI-7951 0.250×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOSIP]] (+0.76, fdr 7e-06), [[RBBP5]] (+0.75, fdr 7e-06), [[MTIF3]] (+0.71, fdr 7e-06); moves opposite to [[VMA21]] (-0.71, fdr 7e-06), [[MOB1A]] (-0.66, fdr 1e-05), [[GNG12]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC00888-1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ACTR6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2649.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.64×** | +17.9 | 0e+00 | 47/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.41×** | +16.2 | 0e+00 | 47/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +12.5 | 2e-33 | 35/47 (LS 180, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +10.8 | 7e-25 | 40/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.6 | 5e-09 | 26/47 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +6.6 | 5e-09 | 26/48 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.4 | 2e-08 | 25/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.8 | 4e-07 | 28/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.002 | 19/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.003 | 17/46 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 19/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.006 | 20/48 (SW480, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.040 | 13/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.13× | +3.3 | 0.045 | 18/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.046 | 10/48 (RKO, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.064 | 17/48 (LS 180, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2649.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW1417 0.177×, HCT15 0.158×, Panc 03.27 0.298×, KATO III 0.190×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H1792 0.205×, H4 0.117×, SW1417 0.310×, LS 180 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LS 180 0.215×, CFPAC-1 0.242×, RPMI-7951 0.250×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.651×** | -7.9 | 1e-12 | 29/43 (NCI-H1792, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.682×** | -6.5 | 2e-08 | 26/42 (LS 180, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.723×** | -5.7 | 2e-06 | 21/37 (SW1417, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.790×** | -4.2 | 0.004 | 20/47 (NCI-H1792, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.827×** | -3.5 | 0.052 | 18/47 (H4, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -3.2 | 0.14 | 15/48 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.1 | 0.16 | 9/47 (NCI-H2030, NCI-H460, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2649. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 31.4 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.37× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 33.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.57× (z +17.5) | — |
| [[KATO III (line)]] | alt | 20.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.55× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.190× (z -11.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 22.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.303× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 64.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -12.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 26.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 35.8 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -15.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.1 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +10.0) | — |
| [[A498 (line)]] | wt | 20.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.15× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 22.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 19.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 31.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.05× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -8.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.55× (z +8.8) | — |
| [[CFPAC-1 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -10.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -12.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 39.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.80× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 21.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 22.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0727× (z -18.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2649), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOSIP]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[RBBP5]] | +0.75 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[RANBP10]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[RNF113A]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ZNHIT3]] | +0.70 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[NBPF11]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[DRG1]] | +0.68 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[NBPF12]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CTR9]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[NFKBIL1]] | +0.66 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[LINC00888-1]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.71 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.66 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[GNG12]] | -0.65 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.63 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[IPO5]] | -0.63 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[M6PR]] | -0.62 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[MBNL3]] | -0.61 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PSME3]] | -0.60 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[UBQLN4]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[RBBP7]] | -0.58 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.58 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[MMGT1]] | -0.58 | -0.62 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00888-1]] | B | LINC00888-1 activity raises SUGP1's level | lines that do not express LINC00888-1 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without LINC00888-1 | 0.091 | ⚠ within organs, on part of the lines; co-absent genes; also absent: KIF3C, TBKBP1, GDAP1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTR6]] | C | SUGP1's natural level weakens ACTR6's drug response | SUGP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.05; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-37.9, -11.9); signed map (-15.8, -4.8). **Vector** length 93.0, 20.6% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +16.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.8 | +5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +17.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.5 | -6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.2 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | SURP and G-patch domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,276,018-19,320,509 (-) |
| Ensembl biotype | protein_coding |
| Also known as | F23858, DKFZp434E2216, RBP; previously SF4 |
| Gene groups (HGNC) | G-patch domain containing; Spliceosomal A complex |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWZ8](https://www.uniprot.org/uniprotkb/Q8IWZ8) (SURP and G-patch domain-containing protein 1):

> Plays a role in pre-mRNA splicing.

**Summary**, from NCBI Gene [57794](https://www.ncbi.nlm.nih.gov/gene/57794):

> SF4 is a member of the SURP family of splicing factors.[supplied by OMIM, Sep 2003]

**Accessions** — [HGNC:18643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18643) · Entrez [57794](https://www.ncbi.nlm.nih.gov/gene/57794) · UniProt [Q8IWZ8](https://www.uniprot.org/uniprotkb/Q8IWZ8) · Ensembl [ENSG00000105705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105705)

## Data

Gene col 2649: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2649); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2649, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2649]; `tensor/DDL_lfc|DDL_z.npy` [2649]; `embed/gene_vectors.npy` [2649]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2649 or target_col == 2649). Every well: [[SUGP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUGP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
