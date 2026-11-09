---
symbol: "GABRA2"
type: "gene"
col: 7570
ensembl_id: "ENSG00000151834"
name: "gamma-aminobutyric acid type A receptor subunit alpha2"
location: "4p12"
module: 9
arm: "+"
pooled_cpm: 2.75
n_lines_expressing: 26
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GABRA2

*gamma-aminobutyric acid type A receptor subunit alpha2* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.75× (z +12.9, q 1e-35, up in 3 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.630× (z -4.2, q 0.015, down in 7 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.0969×, HT-29 0.0901×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.0184×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HT-29 0.0410×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.0464×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HT-29 0.0487×); [[Panobinostat (drug)]] 5 µM in 1 line (HT-29 0.0564×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK6]] (+0.64, fdr 1e-05), [[KHDRBS2]] (+0.63, fdr 2e-05), [[MARCHF1]] (+0.61, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[RIN3]] → it (grade B ⚠); 11 go from it, the strongest it → [[MGAT4C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +12.9 | 1e-35 | 3/12 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.96×** | +12.5 | 3e-33 | 1/7 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.74×** | +11.5 | 3e-28 | 1/4 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.45×** | +11.5 | 3e-28 | 15/18 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.27×** | +7.4 | 1e-11 | 12/16 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +7.1 | 8e-11 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.87×** | +5.7 | 1e-06 | 9/20 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +4.3 | 0.001 | 3/18 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.9 | 0.006 | 0/9 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +3.8 | 0.007 | 1/5 (CHP-212) | top dose only | noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +3.8 | 0.009 | 1/5 (SHP-77) | top dose only | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.5 | 0.020 | 0/12 | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.5 | 0.024 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.035 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.062 | 6/12 (NCI-H1573, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7570.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 18 here, 10 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.0969×, HT-29 0.0901×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.0184×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HT-29 0.0410×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HT-29 0.0464×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (HT-29 0.0487×); [[Panobinostat (drug)]] 5 µM in 1 line (HT-29 0.0564×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -4.2 | 0.015 | 7/16 (HT-29, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.679× | -3.3 | 0.32 | 3/18 (SW1417, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 27.5 | 0 | 20 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0184× (z -26.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0464× (z -14.6) |
| [[SW480 (line)]] | alt | 2.46 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.32× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.0831× (z -9.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 4.46 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0791× (z -9.1) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H1573 (line)]] | alt | 6.15 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.23× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 6.06 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0735× (z -9.0) ⚠ cell-cycle shift, explains ~12% of this change |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0969× (z -13.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.686 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.669 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.707 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.584 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK6]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Neuronal System |
| [[KHDRBS2]] | +0.63 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MARCHF1]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PDGFD]] | +0.60 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[KCNH7]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 | pathway: Neuronal System |
| [[NELL1]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RERG]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[LRP2]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ASXL3]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[NRXN1]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 | pathway: Neuronal System; STRING 440 |
| [[VAV3]] | +0.58 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[NELL2]] | +0.58 | +0.60 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIN3]] | B | RIN3 activity lowers GABRA2's level | lines that do not express RIN3 (6) vs lines expressing it (43) | 1.77× higher at baseline in the lines without RIN3 | 0.088 | ⚠ within organs, on part of the lines |
| [[NOL4]] | C | NOL4 activity raises GABRA2's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 2.23× lower at baseline in the lines without NOL4 | 0.010 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[ASXL3]] | C | ASXL3 activity raises GABRA2's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.07× lower at baseline in the lines without ASXL3 | 0.040 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[MARCHF1]] | C | MARCHF1 activity raises GABRA2's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without MARCHF1 | 0.055 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises GABRA2's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.41× lower at baseline in the lines without RIT2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[FUT9]] | C | FUT9 activity raises GABRA2's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.88× lower at baseline in the lines without FUT9 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; co-absent with the target |
| [[FREM2]] | C | FREM2 activity raises GABRA2's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without FREM2 | 0.078 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; co-absent with the target |
| [[LINC02253]] | C | LINC02253 activity raises GABRA2's level | lines that do not express LINC02253 (35) vs lines expressing it (15) | 1.93× lower at baseline in the lines without LINC02253 | 0.079 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02058, ENSG00000289349; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT4C]] | B | GABRA2 activity raises MGAT4C's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without GABRA2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |
| [[EGLN3]] | B | GABRA2 activity raises EGLN3's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.52× lower at baseline in the lines without GABRA2 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |
| [[SLAIN1]] | B | GABRA2 activity raises SLAIN1's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without GABRA2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |
| [[CACNA1D]] | B | GABRA2 activity raises CACNA1D's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.79× lower at baseline in the lines without GABRA2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent |
| [[NOL4]] | C | GABRA2 activity raises NOL4's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without GABRA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[LINC02253]] | C | GABRA2 activity raises LINC02253's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 3.14× lower at baseline in the lines without GABRA2 | 0.023 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[FREM2]] | C | GABRA2 activity raises FREM2's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.94× lower at baseline in the lines without GABRA2 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[CHST8]] | C | GABRA2 activity raises CHST8's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.34× lower at baseline in the lines without GABRA2 | 0.045 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[FUT9]] | C | GABRA2 activity raises FUT9's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without GABRA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[ASXL3]] | C | GABRA2 activity raises ASXL3's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.09× lower at baseline in the lines without GABRA2 | 0.068 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[ABCB1]] | C | GABRA2 activity raises ABCB1's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without GABRA2 | 0.099 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.0, 35.9); signed map (42.9, 35.7). **Vector** length 36.4, 7.49% of its response variance represented; |z| ≥ 3 in 472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | gamma-aminobutyric acid type A receptor subunit alpha2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:46,243,548-46,475,230 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Gamma-aminobutyric acid type A receptor subunits |
| Reactome | 4 pathways, smallest: GABA receptor activation; Neurotransmitter receptors and postsynaptic signal transmission; Transmission across Chemical Synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [P47869](https://www.uniprot.org/uniprotkb/P47869) (Gamma-aminobutyric acid receptor subunit alpha-2):

> Alpha subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA), a major inhibitory neurotransmitter in the brain. GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interfaces (By similarity). When activated by GABA, GABAARs selectively allow the flow of chloride anions across the cell membrane down …

**Summary**, from NCBI Gene [2555](https://www.ncbi.nlm.nih.gov/gene/2555):

> GABA is the major inhibitory neurotransmitter in the mammalian brain where it acts at GABA-A receptors, which are ligand-gated chloride channels. Chloride conductance of these channels can be modulated by agents such as benzodiazepines that bind to the GABA-A receptor. At least 16 distinct subunits of GABA-A receptors have been identified. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:4076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4076) · Entrez [2555](https://www.ncbi.nlm.nih.gov/gene/2555) · UniProt [P47869](https://www.uniprot.org/uniprotkb/P47869) · Ensembl [ENSG00000151834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151834)

## Data

Gene col 7570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7570); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7570]; `tensor/DDL_lfc|DDL_z.npy` [7570]; `embed/gene_vectors.npy` [7570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7570 or target_col == 7570). Every well: [[GABRA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABRA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
