---
symbol: "CYP2J2"
type: "gene"
col: 5593
ensembl_id: "ENSG00000134716"
name: "cytochrome P450 family 2 subfamily J member 2"
location: "1p32.1"
module: 32
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 38
n_dd_up: 12
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 26
direction_downstream: 18
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CYP2J2

*cytochrome P450 family 2 subfamily J member 2* — 1p32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.02× (z +16.2, q 0e+00, up in 33 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.492× (z -7.3, q 1e-10, down in 21 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMPR]] (+0.67, fdr 3e-05), [[BATF2]] (+0.65, fdr 7e-06), [[CD5L]] (+0.58, fdr 4e-05); moves opposite to [[TMCO3]] (-0.53, fdr 4e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[SMPDL3B]] → it (grade B ⚠); 18 go from it, the strongest it → [[GBP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.02×** | +16.2 | 0e+00 | 33/33 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.02×** | +11.5 | 5e-28 | 24/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.02×** | +7.3 | 7e-11 | 17/35 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +7.0 | 3e-10 | 15/35 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.9 | 5e-10 | 0/5 | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +6.2 | 7e-08 | 0/10 | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.79×** | +5.8 | 6e-07 | 9/24 (NCI-H23, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +5.3 | 9e-06 | 7/33 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.64×** | +5.2 | 2e-05 | 7/33 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.0 | 0.003 | 2/15 (LS 180, J82) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.006 | 5/32 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.5 | 0.024 | 1/11 (BT-474) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.492×** | -7.3 | 1e-10 | 21/31 (LoVo, SW480, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -6.9 | 2e-09 | 20/32 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -6.5 | 1e-08 | 21/30 (SW1417, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -5.9 | 5e-07 | 19/34 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.567×** | -5.9 | 5e-07 | 15/29 (A498, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.681×** | -5.6 | 2e-06 | 18/32 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -5.5 | 2e-06 | 15/29 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -5.2 | 1e-05 | 12/24 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.703×** | -5.2 | 2e-05 | 13/32 (SW1417, A549, …) | all doses, stronger at high dose |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -4.4 | 6e-04 | 10/35 (A549, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.658×** | -4.3 | 8e-04 | 9/35 (LS 180, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -4.3 | 8e-04 | 15/31 (LoVo, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.664×** | -4.2 | 0.001 | 14/22 (COLO 205, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.671×** | -4.1 | 0.001 | 12/34 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.665×** | -4.1 | 0.002 | 11/25 (LS 180, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.697×** | -3.7 | 0.007 | 12/26 (Panc 03.27, NCI-H2347, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 14.5 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0838× (z -13.7) |
| [[SW480 (line)]] | alt | 4.71 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 3.46× (z +9.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.133× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 5.86 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0973× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.314× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 4.54 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0705× (z -9.0) |
| [[SW1417 (line)]] | alt | 4.35 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0487× (z -11.2) |
| [[A498 (line)]] | wt | 2.44 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 0.05 µM 0.0615× (z -8.8) |
| [[BT-474 (line)]] | alt | 8.23 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0766× (z -9.6) |
| [[COLO 205 (line)]] | alt | 9.30 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[PANC-1 (line)]] | alt | 0.978 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.3× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 7.81 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.973 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMPR]] | +0.67 | +0.44 / +0.73 | both halves | 3e-05 | **novel candidate** |
| [[BATF2]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CD5L]] | +0.58 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[LGALS9]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[IFI44]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[SHFL]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[TRIM34]] | +0.56 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[OAS1]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LINC00540]] | +0.56 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[TNFRSF1B]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[IQGAP2]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RBM11]] | +0.55 | +0.33 / +0.68 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCO3]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 26, C 0. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMPDL3B]] | B | SMPDL3B activity raises CYP2J2's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without SMPDL3B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[OAS2]] | B | OAS2 activity raises CYP2J2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without OAS2 | 0.007 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[SRMS]] | B | SRMS activity raises CYP2J2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.14× lower at baseline in the lines without SRMS | 0.011 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[SLC27A2]] | B | SLC27A2 activity raises CYP2J2's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without SLC27A2 | 0.011 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[HSH2D]] | B | HSH2D activity raises CYP2J2's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without HSH2D | 0.018 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises CYP2J2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without PLSCR1 | 0.033 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises CYP2J2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.69× lower at baseline in the lines without CMPK2 | 0.037 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[MUC3A]] | B | MUC3A activity raises CYP2J2's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.78× lower at baseline in the lines without MUC3A | 0.037 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[MX1]] | B | MX1 activity raises CYP2J2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without MX1 | 0.042 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[CPNE4]] | B | CPNE4 activity raises CYP2J2's level | lines that do not express CPNE4 (21) vs lines expressing it (29) | 1.85× lower at baseline in the lines without CPNE4 | 0.042 | ⚠ within organs, on part of the lines; also absent: MIR646HG, TMEM156, BCL2A1; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises CYP2J2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without TRIM22 | 0.045 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[NOD2]] | B | NOD2 activity weakens CYP2J2's drug response | lines that do not express NOD2 (10) vs lines expressing it (25) | the lines without NOD2 respond 1.21× as strongly (z diff -0.51); strongest at Panobinostat 5 µM: 3.88x vs 1.29x (z diff -3.0) | 0.049 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | CYP2J2 activity raises GBP4's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 3.01× lower at baseline in the lines without CYP2J2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[MX1]] | B | CYP2J2 activity raises MX1's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 4.45× lower at baseline in the lines without CYP2J2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[PLSCR1]] | B | CYP2J2 activity raises PLSCR1's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 2.29× lower at baseline in the lines without CYP2J2 | 0.021 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[IFI6]] | B | CYP2J2 activity raises IFI6's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 2.48× lower at baseline in the lines without CYP2J2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[PARP9]] | B | CYP2J2 activity raises PARP9's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without CYP2J2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[CMPK2]] | B | CYP2J2 activity raises CMPK2's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without CYP2J2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[MX2]] | B | CYP2J2 activity raises MX2's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 4.60× lower at baseline in the lines without CYP2J2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[XAF1]] | B | CYP2J2 activity raises XAF1's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 2.60× lower at baseline in the lines without CYP2J2 | 0.047 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[TRIM25]] | B | CYP2J2 activity raises TRIM25's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without CYP2J2 | 0.052 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[ETV7]] | B | CYP2J2 activity raises ETV7's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without CYP2J2 | 0.066 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[UBE2L6]] | B | CYP2J2 activity raises UBE2L6's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 2.27× lower at baseline in the lines without CYP2J2 | 0.066 | ⚠ within organs, on part of the lines; also absent: CDK18 |
| [[SMPDL3B]] | B | CYP2J2 activity raises SMPDL3B's level | lines that do not express CYP2J2 (12) vs lines expressing it (38) | 1.89× lower at baseline in the lines without CYP2J2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CDK18 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.521). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.9, 54.1); signed map (67.4, 31.5). **Vector** length 65.7, 13.2% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *OAS antiviral response* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +16.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +6.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | -0.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -5.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -6.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.7 | -5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.0 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 2 subfamily J member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.1 — chr1:59,893,308-59,926,773 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome P450 family 2 |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 9 pathways, smallest: Synthesis of epoxy (EET) and dihydroxyeicosatrienoic acids (DHET); Fatty acids; Xenobiotics |
| Matched by | ensembl_id |

**Function**, from UniProt [P51589](https://www.uniprot.org/uniprotkb/P51589) (Cytochrome P450 2J2):

> A cytochrome P450 monooxygenase involved in the metabolism of polyunsaturated fatty acids (PUFA) in the cardiovascular system. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (NADPH--hemoprotein reductase). Catalyzes the epoxidation of double bonds of PUFA. Converts arachidonic acid to four regioisomeric epoxyeicosatrienoic acids (EpETrE), likely …

**Summary**, from NCBI Gene [1573](https://www.ncbi.nlm.nih.gov/gene/1573):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This protein localizes to the endoplasmic reticulum and is thought to be the predominant enzyme responsible for epoxidation of endogenous arachidonic acid in cardiac tissue. Multiple transcript variants have been found for this gene. [provided by RefSeq, Jan …

**Accessions** — [HGNC:2634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2634) · Entrez [1573](https://www.ncbi.nlm.nih.gov/gene/1573) · UniProt [P51589](https://www.uniprot.org/uniprotkb/P51589) · Ensembl [ENSG00000134716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134716)

## Data

Gene col 5593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5593); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5593]; `tensor/DDL_lfc|DDL_z.npy` [5593]; `embed/gene_vectors.npy` [5593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5593 or target_col == 5593). Every well: [[CYP2J2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP2J2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
