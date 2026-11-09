---
symbol: "AKT1"
type: "gene"
col: 6608
ensembl_id: "ENSG00000142208"
name: "AKT serine/threonine kinase 1"
location: "14q32.33"
module: 2
arm: "+"
pooled_cpm: 17.8
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# AKT1

*AKT serine/threonine kinase 1* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +16.9, q 0e+00, up in 38 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Thymol (drug)]] 0.5 µM: 1.36× (z +4.9, q 1e-04, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.518× (z -14.9, q 0e+00, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SBF1]] (+0.78, fdr 7e-06), [[SELENON]] (+0.74, fdr 7e-06), [[PCNX3]] (+0.73, fdr 7e-06); moves opposite to [[SEC62]] (-0.75, fdr 7e-06), [[PIGBOS1]] (-0.73, fdr 7e-06), [[SNRPB2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[B4GALNT4]] → it (grade B ⚠); 5 go from it, the strongest it → [[MMGT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +16.9 | 0e+00 | 38/42 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +15.8 | 0e+00 | 32/32 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +10.9 | 1e-25 | 31/36 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +6.6 | 6e-09 | 28/43 (J82, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 1e-04 | 25/44 (SW48, C32, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.022 | 13/45 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.4 | 0.047 | 7/33 (SW48, C32, …) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.047 | 8/46 (J82, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.070 | 11/47 (HCT15, A549, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.518×** | -14.9 | 0e+00 | 36/47 (J82, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -12.0 | 8e-31 | 32/47 (SW48, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.491×** | -11.0 | 1e-25 | 40/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -7.6 | 3e-12 | 31/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.587×** | -4.5 | 9e-04 | 17/44 (HOP62, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.620×** | -4.0 | 0.006 | 16/40 (SW 900, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.639×** | -3.8 | 0.012 | 17/48 (RKO, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.792×** | -3.8 | 0.012 | 16/47 (Panc 03.27, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.6 | 0.022 | 18/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.803×** | -3.5 | 0.022 | 17/48 (SK-MEL-2, SNU-1, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 22.9 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -14.3) |
| [[HOP62 (line)]] | alt | 18.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -11.8) |
| [[PANC-1 (line)]] | alt | 17.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -8.8) |
| [[A-427 (line)]] | wt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.7) |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.5) |
| [[LoVo (line)]] | wt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 29.8 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.1) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 13.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 0.05 µM 0.316× (z -8.9) |
| [[SW480 (line)]] | alt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 14.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.127× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.19× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -10.8) |
| [[SW1417 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0880× (z -14.9) |
| [[A-172 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBF1]] | +0.78 | +0.70 / +0.79 | both halves | 7e-06 | same gene group; pathway: RAB GEFs exchange GTP for GDP on RABs; STRING 412 |
| [[SELENON]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[PCNX3]] | +0.73 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ARHGAP4]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[PLCB3]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 | pathway: G-protein beta:gamma signalling; STRING 537 |
| [[COLGALT1]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[CDK16]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[CAPN1]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | STRING 597 |
| [[TCF3]] | +0.66 | +0.71 / +0.68 | both halves | 7e-06 | STRING 408 |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC62]] | -0.75 | -0.75 / -0.74 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.73 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[SNRPB2]] | -0.68 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[SNW1]] | -0.67 | -0.64 / -0.60 | both halves | 7e-06 | pathway: Regulation of beta-cell development |
| [[MRPS18B]] | -0.66 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.65 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[COIL]] | -0.65 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[ASB8]] | -0.65 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[TCEAL8]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.64 | -0.61 / -0.58 | both halves | 8e-06 |  |
| [[C1orf131]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[PPIG]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 | STRING 471 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT4]] | B | B4GALNT4 activity raises AKT1's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without B4GALNT4 | 0.036 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMGT1]] | B | AKT1, [[AKT2]], [[AKT3]] activity raises MMGT1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[GTF3C4]] | B | AKT1, [[AKT2]], [[AKT3]] activity raises GTF3C4's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 0.8% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |
| [[HSPA13]] | B | AKT1, [[AKT2]], [[AKT3]] activity raises HSPA13's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[TWF1]] | B | AKT1, [[AKT2]], [[AKT3]] activity raises TWF1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ZHX1]] | B | AKT1, [[AKT2]], [[AKT3]] activity raises ZHX1's level | compounds that target AKT1, AKT2, AKT3: 2 of 3 lower it (BAY1125976, Ipatasertib) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-20.5, -26.0); signed map (-25.1, -42.7). **Vector** length 85.4, 17.1% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +10.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.0 | +2.9 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.8 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.6 | -7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | AKT serine/threonine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,769,349-104,795,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAC, PKB, PRKBA, AKT, RAC-alpha |
| Gene groups (HGNC) | Pleckstrin homology domain containing; AKT kinase family |
| Hallmark sets | ANDROGEN_RESPONSE, PI3K_AKT_MTOR_SIGNALING, ALLOGRAFT_REJECTION |
| Reactome | 104 pathways, smallest: AKT-mediated inactivation of FOXO1A; Inhibition of TSC complex formation by AKT (PKB); RUNX2 regulates genes involved in cell migration |
| Matched by | ensembl_id |

**Function**, from UniProt [P31749](https://www.uniprot.org/uniprotkb/P31749) (RAC-alpha serine/threonine-protein kinase):

> AKT1 is one of 3 closely related serine/threonine-protein kinases (AKT1, AKT2 and AKT3) called the AKT kinase, and which regulate many processes including metabolism, proliferation, cell survival, growth and angiogenesis. This is mediated through serine and/or threonine phosphorylation of a range of downstream substrates. Over 100 substrate candidates have been reported so far, but for most of them, no isoform specificity has been reported. AKT is responsible of the regulation of glucose uptake …

**Summary**, from NCBI Gene [207](https://www.ncbi.nlm.nih.gov/gene/207):

> This gene encodes one of the three members of the human AKT serine-threonine protein kinase family which are often referred to as protein kinase B alpha, beta, and gamma. These highly similar AKT proteins all have an N-terminal pleckstrin homology domain, a serine/threonine-specific kinase domain and a C-terminal regulatory domain. These proteins are phosphorylated by phosphoinositide 3-kinase (PI3K). AKT/PI3K forms a key component of many signalling pathways that involve the binding of …

**Accessions** — [HGNC:391](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:391) · Entrez [207](https://www.ncbi.nlm.nih.gov/gene/207) · UniProt [P31749](https://www.uniprot.org/uniprotkb/P31749) · Ensembl [ENSG00000142208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142208)

## Data

Gene col 6608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6608); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6608]; `tensor/DDL_lfc|DDL_z.npy` [6608]; `embed/gene_vectors.npy` [6608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6608 or target_col == 6608). Every well: [[AKT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
