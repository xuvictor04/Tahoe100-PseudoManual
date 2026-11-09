---
symbol: "PPARGC1B"
type: "gene"
col: 7921
ensembl_id: "ENSG00000155846"
name: "PPARG coactivator 1 beta"
location: "5q32"
module: 18
arm: "+"
pooled_cpm: 12.21
n_lines_expressing: 47
n_dd_up: 46
n_dd_down: 2
n_dd_up_clean: 33
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PPARGC1B

*PPARG coactivator 1 beta* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +15.3, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 0.526× (z -5.4, q 4e-05, down in 20 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.172×, A-427 0.175×, LOX-IMVI 0.171×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.317×, LOX-IMVI 0.226×, LoVo 0.292×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.267×, RKO 0.197×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0581×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0728×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UCK2]] (+0.76, fdr 7e-06), [[CCDC88C]] (+0.70, fdr 7e-06), [[PALS2]] (+0.69, fdr 7e-06); moves opposite to [[GOLGB1]] (-0.56, fdr 1e-05), [[SENP2]] (-0.56, fdr 1e-05), [[AP1G1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); 10 go from it, the strongest it → [[ADCY3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7921.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +15.3 | 0e+00 | 37/42 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.27×** | +13.8 | 5e-41 | 39/44 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.85×** | +12.2 | 4e-32 | 38/44 (NCI-H23, SW480, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.57×** | +11.0 | 5e-26 | 37/44 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +10.6 | 3e-24 | 35/44 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.27×** | +9.5 | 1e-19 | 34/44 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.26×** | +9.5 | 2e-19 | 32/42 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.01×** | +8.1 | 4e-14 | 29/44 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +7.7 | 1e-12 | 22/39 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.50×** | +7.6 | 1e-12 | 34/44 (A-427, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.83×** | +6.8 | 6e-10 | 21/38 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +6.6 | 3e-09 | 24/44 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +6.2 | 2e-08 | 20/44 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.45×** | +6.1 | 6e-08 | 24/44 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +5.7 | 5e-07 | 25/42 (A-427, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +5.6 | 6e-07 | 19/44 (NCI-H460, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 3e-06 | 19/42 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **2.35×** | +5.2 | 6e-06 | 13/37 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +4.8 | 5e-05 | 17/43 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.4 | 3e-04 | 20/44 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.67×** | +4.3 | 5e-04 | 10/44 (NCI-H460, SW48, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7921.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.172×, A-427 0.175×, LOX-IMVI 0.171×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.317×, LOX-IMVI 0.226×, LoVo 0.292×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.267×, RKO 0.197×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0581×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (SNU-423 0.0728×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.526×** | -5.4 | 4e-05 | 20/40 (A498, LS 180, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.504×** | -4.2 | 0.007 | 13/42 (A-427, A498, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.747× | -3.4 | 0.11 | 8/44 (NCI-H2347, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.824× | -3.3 | 0.16 | 10/44 (NCI-H2030, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 16.1 | 17 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 10.8× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.267× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 13.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +11.2) | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.197× (z -9.4) |
| [[A-427 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 16.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +11.6) | — |
| [[C32 (line)]] | wt | 9.01 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0837× (z -9.6) ⚠ toxic |
| [[J82 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.211× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.99× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 3.28 | 0 | 1 | — | [[Zileuton (drug)]] 0.05 µM 0.0567× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0581× (z -12.9) |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 6.07 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0728× (z -9.4) |
| [[SW48 (line)]] | wt | 34.5 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.206× (z -8.7) |
| [[A-172 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCK2]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 | same gene group |
| [[CCDC88C]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[PALS2]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[FXN]] | +0.63 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[SLC27A2]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LRP5L]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD13B]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[EBPL]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[AKAP1]] | +0.62 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TBC1D14]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGB1]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[SENP2]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[AP1G1]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TOX4]] | -0.53 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SLU7]] | -0.52 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[PRMT2]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TSG101]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[DNAL4]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises PPARGC1B's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without MCOLN2 | 0.023 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[ADCY3]] | B | ADCY3 activity raises PPARGC1B's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without ADCY3 | 0.032 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[CENPV]] | B | CENPV activity raises PPARGC1B's level | lines that do not express CENPV (9) vs lines expressing it (41) | 1.67× lower at baseline in the lines without CENPV | 0.039 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NCS1]] | C | NCS1 activity raises PPARGC1B's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.99× lower at baseline in the lines without NCS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent; co-absent with the target |
| [[GPD1L]] | C | GPD1L activity raises PPARGC1B's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without GPD1L | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[ANKRD13B]] | C | ANKRD13B activity raises PPARGC1B's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 3.07× lower at baseline in the lines without ANKRD13B | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | C | PPARGC1B activity raises ADCY3's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 4.27× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[ANKS6]] | C | PPARGC1B activity raises ANKS6's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.61× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[PALS2]] | C | PPARGC1B activity raises PALS2's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[TFAP4]] | C | PPARGC1B activity raises TFAP4's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.02× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[MACROD1]] | C | PPARGC1B activity raises MACROD1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |
| [[EEF2K]] | C | PPARGC1B activity raises EEF2K's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 1.70× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent |
| [[NCS1]] | C | PPARGC1B activity raises NCS1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 5.21× lower at baseline in the lines without PPARGC1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; co-absent with the target; its own permutation p |
| [[TCOF1]] | C | PPARGC1B activity raises TCOF1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without PPARGC1B | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent |
| [[MDN1]] | C | PPARGC1B activity raises MDN1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without PPARGC1B | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent |
| [[ANKRD13B]] | C | PPARGC1B activity raises ANKRD13B's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 3.37× lower at baseline in the lines without PPARGC1B | 0.095 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.701). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.6, -38.2); signed map (-5.7, -54.7). **Vector** length 106, 27.0% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +10.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +15.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.4 | +5.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.7 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | +4.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.5 | -5.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PPARG coactivator 1 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,730,298-149,855,022 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PERC, PGC1B, PPARAGCIβ |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Reactome | 16 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; Transcriptional activation of mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YN6](https://www.uniprot.org/uniprotkb/Q86YN6) (Peroxisome proliferator-activated receptor gamma coactivator 1-beta):

> Plays a role of stimulator of transcription factors and nuclear receptors activities. Activates transcriptional activity of estrogen receptor alpha, nuclear respiratory factor 1 (NRF1) and glucocorticoid receptor in the presence of glucocorticoids. May play a role in constitutive non-adrenergic-mediated mitochondrial biogenesis as suggested by increased basal oxygen consumption and mitochondrial number when overexpressed. May be involved in fat oxidation and non-oxidative glucose metabolism and …

**Summary**, from NCBI Gene [133522](https://www.ncbi.nlm.nih.gov/gene/133522):

> The protein encoded by this gene stimulates the activity of several transcription factors and nuclear receptors, including estrogen receptor alpha, nuclear respiratory factor 1, and glucocorticoid receptor. The encoded protein may be involved in fat oxidation, non-oxidative glucose metabolism, and the regulation of energy expenditure. This protein is downregulated in prediabetic and type 2 diabetes mellitus patients. Certain allelic variations in this gene increase the risk of the development …

**Accessions** — [HGNC:30022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30022) · Entrez [133522](https://www.ncbi.nlm.nih.gov/gene/133522) · UniProt [Q86YN6](https://www.uniprot.org/uniprotkb/Q86YN6) · Ensembl [ENSG00000155846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155846)

## Data

Gene col 7921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7921); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7921]; `tensor/DDL_lfc|DDL_z.npy` [7921]; `embed/gene_vectors.npy` [7921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7921 or target_col == 7921). Every well: [[PPARGC1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPARGC1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
