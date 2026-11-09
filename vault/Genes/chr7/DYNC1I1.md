---
symbol: "DYNC1I1"
type: "gene"
col: 8174
ensembl_id: "ENSG00000158560"
name: "dynein cytoplasmic 1 intermediate chain 1"
location: "7q21.3"
module: 72
arm: "+"
pooled_cpm: 7.79
n_lines_expressing: 38
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# DYNC1I1

*dynein cytoplasmic 1 intermediate chain 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 10.3× (z +27.7, q 0e+00, up in 29 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.662× (z -5.3, q 8e-05, down in 17 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AA2P]] (+0.68, fdr 7e-06), [[SNX29]] (+0.68, fdr 7e-06), [[GCKR]] (+0.62, fdr 3e-05); moves opposite to [[HDGF]] (-0.51, fdr 4e-05), [[TPRA1]] (-0.46, fdr 1e-04), [[MAML1]] (-0.45, fdr 7e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[POPDC3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01060]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **10.3×** | +27.7 | 0e+00 | 29/31 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **7.22×** | +24.9 | 0e+00 | 29/33 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **5.87×** | +22.3 | 0e+00 | 31/32 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.95×** | +20.2 | 0e+00 | 30/34 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.36×** | +18.6 | 0e+00 | 22/30 (A498, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.21×** | +14.7 | 0e+00 | 24/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +12.5 | 5e-34 | 19/33 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.50×** | +11.6 | 5e-29 | 21/34 (SW480, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.15×** | +10.3 | 4e-23 | 21/33 (SW480, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.23×** | +10.1 | 4e-22 | 8/21 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.16×** | +9.3 | 7e-19 | 5/15 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +9.2 | 1e-18 | 19/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +9.2 | 2e-18 | 11/29 (NCI-H460, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.89×** | +8.9 | 1e-17 | 13/17 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +5.6 | 6e-07 | 11/32 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | **1.55×** | +5.5 | 1e-06 | 17/34 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +4.1 | 0.001 | 11/31 (SW480, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.005 | 8/30 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Hydroxyfasudil (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.047 | 3/31 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.56×** | +2.9 | 0.074 | 5/30 (SW 900, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.662×** | -5.3 | 8e-05 | 17/33 (J82, A-172, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.755×** | -5.1 | 8e-05 | 10/33 (HS-578T, SHP-77, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -5.1 | 8e-05 | 16/32 (J82, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.674×** | -5.0 | 8e-05 | 11/34 (J82, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.511×** | -4.5 | 1e-03 | 16/30 (SHP-77, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Pemigatinib (drug)]] 0.05 µM |  | **0.742×** | -3.6 | 0.032 | 2/31 (BT-474, NCI-H1573) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.763×** | -3.4 | 0.044 | 15/34 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Sulfatinib (drug)]] 5 µM |  | **0.757×** | -3.4 | 0.044 | 9/32 (A-172, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.762×** | -3.3 | 0.055 | 12/31 (RPMI-7951, HEC-1-A, …) | two highest doses | composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | 0.787× | -3.1 | 0.12 | 2/33 (RKO, LOX-IMVI) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.781× | -3.0 | 0.12 | 6/32 (SHP-77, J82, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.635× | -3.0 | 0.12 | 4/32 (SK-MEL-2, J82, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.5 | 10 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 21.3× (z +19.0) | — |
| [[A498 (line)]] | wt | 18.7 | 5 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 12.6× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.9) |
| [[LoVo (line)]] | wt | 5.26 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 27.6× (z +14.7) | — |
| [[A-172 (line)]] | wt | 19.6 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 9.80× (z +11.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0863× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 25.1 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 21.4× (z +14.3) | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 12.4× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 2.76 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 26.7× (z +12.0) | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0820× (z -9.1) |
| [[SW 900 (line)]] | alt | 14.3 | 4 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 14.6× (z +10.6) | [[Docetaxel (drug)]] 0.05 µM 0.0909× (z -9.4) ⚠ transcription drop; cell-cycle shift, explains ~96% of this change |
| [[H4 (line)]] | wt | 27.7 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 32.6× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.123× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 5.88 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.2× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 57.9 | 1 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.52× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 9.20 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 34.6× (z +15.0) | — |
| [[NCI-H1792 (line)]] | alt | 7.77 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 27.8× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0803× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 9.02 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.40× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 8.68 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0812× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 6.68 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.8× (z +10.5) | — |
| [[A-427 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AA2P]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[SNX29]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[GCKR]] | +0.62 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[PLAA]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 | same gene group |
| [[DGKG]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[PSMD13]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[PCYT1A]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SSX1]] | +0.58 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[HSP90AA1]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 | pathway: Aggrephagy; STRING 545 |
| [[HSP90AB3P]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[NSFL1C]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDGF]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TPRA1]] | -0.46 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[MAML1]] | -0.45 | -0.37 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POPDC3]] | B | POPDC3 activity raises DYNC1I1's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without POPDC3 | 0.073 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1 |
| [[DGKG]] | B | DGKG activity raises DYNC1I1's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.88× lower at baseline in the lines without DGKG | 0.098 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01060]] | B | DYNC1I1 activity raises LINC01060's level | lines that do not express DYNC1I1 (12) vs lines expressing it (38) | 2.48× lower at baseline in the lines without DYNC1I1 | 0.080 | ⚠ within organs, on part of the lines; also absent: CAMK4, CDK14, MEIS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.9, -8.3); signed map (-28.4, -26.2). **Vector** length 90.4, 21.3% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +9.6 | +24.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.3 | +22.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.2 | +27.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +18.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.7 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +12.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.5 | +10.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -5.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -1.9 | -5.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | +0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | dynein cytoplasmic 1 intermediate chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:95,772,506-96,110,322 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DNCIC1; previously DNCI1 |
| Gene groups (HGNC) | WD repeat domain containing; Dynein 1 complex subunits; Dynein intermediate chains |
| Reactome | 41 pathways, smallest: Aggrephagy; COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand |
| Matched by | ensembl_id |

**Function**, from UniProt [O14576](https://www.uniprot.org/uniprotkb/O14576) (Cytoplasmic dynein 1 intermediate chain 1):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 1 complex that are thought to be involved in linking dynein to cargos and to adapter proteins that regulate dynein function. Cytoplasmic dynein 1 acts as a motor for the intracellular retrograde motility of vesicles and organelles along microtubules. The intermediate chains mediate the binding of dynein to dynactin via its 150 kDa component (p150-glued) DCTN1. May play a role in mediating the interaction of …

**Summary**, from NCBI Gene [1780](https://www.ncbi.nlm.nih.gov/gene/1780):

> Enables spectrin binding activity. Involved in vesicle transport along microtubule. Located in several cellular components, including kinetochore; recycling endosome; and spindle pole. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:2963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2963) · Entrez [1780](https://www.ncbi.nlm.nih.gov/gene/1780) · UniProt [O14576](https://www.uniprot.org/uniprotkb/O14576) · Ensembl [ENSG00000158560](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158560)

## Data

Gene col 8174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8174); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8174]; `tensor/DDL_lfc|DDL_z.npy` [8174]; `embed/gene_vectors.npy` [8174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8174 or target_col == 8174). Every well: [[DYNC1I1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC1I1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
