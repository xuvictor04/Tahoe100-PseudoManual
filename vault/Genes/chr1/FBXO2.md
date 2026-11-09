---
symbol: "FBXO2"
type: "gene"
col: 3813
ensembl_id: "ENSG00000116661"
name: "F-box protein 2"
location: "1p36.22"
module: 21
arm: "+"
pooled_cpm: 6.33
n_lines_expressing: 27
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# FBXO2

*F-box protein 2* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.45× (z +10.7, q 4e-24, up in 14 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.590× (z -4.5, q 0.004, down in 12 of 24 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.111×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.222×); [[Verteporfin (drug)]] 5 µM in 1 line (CFPAC-1 0.0802×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC26A11]] (+0.62, fdr 1e-05), [[HSPB1]] (+0.56, fdr 1e-05), [[TNFSF9]] (+0.56, fdr 2e-05); moves opposite to [[EEFSEC]] (-0.57, fdr 2e-05), [[FARSB]] (-0.51, fdr 9e-05), [[TBCCD1]] (-0.50, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LRRC4B]] → it (grade B ⚠); 4 go from it, the strongest it → [[FBXO44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.45×** | +10.7 | 4e-24 | 14/23 (LS 180, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +9.1 | 3e-17 | 12/16 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +8.8 | 2e-16 | 8/8 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +7.3 | 6e-11 | 6/10 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.75×** | +6.7 | 3e-09 | 12/24 (LS 180, HCT15, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.004 | 8/24 (Hs 766T, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.005 | 10/22 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.60×** | +4.0 | 0.005 | 6/18 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.005 | 11/24 (HOP62, PANC-1, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.007 | 8/21 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.88×** | +3.8 | 0.007 | 6/18 (A-427, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +3.7 | 0.011 | 10/23 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.52×** | +3.5 | 0.017 | 9/24 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.017 | 8/18 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.017 | 4/19 (HCT15, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.022 | 5/22 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.73×** | +3.3 | 0.030 | 6/19 (A-427, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.040 | 9/24 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3813.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.111×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.222×); [[Verteporfin (drug)]] 5 µM in 1 line (CFPAC-1 0.0802×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.590×** | -4.5 | 0.004 | 12/24 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.677× | -3.3 | 0.24 | 12/24 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0802× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.149× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 88.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC26A11]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[HSPB1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TNFSF9]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[SPACA6]] | +0.55 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RNF10]] | +0.55 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[ATP6V0E1]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[MTCH1]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[MMP24]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ARMH1]] | +0.54 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[PANX2]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[SLC26A5]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PPM1N]] | +0.53 | +0.38 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.57 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[FARSB]] | -0.51 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[TBCCD1]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[XRCC5]] | -0.50 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[ATIC]] | -0.49 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[PMS1]] | -0.47 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[SRBD1]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[TRIP13]] | -0.47 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[TMEM209]] | -0.47 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[NUP188]] | -0.47 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[VRK1]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ATP6V0A2]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC4B]] | B | LRRC4B activity raises FBXO2's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.60× lower at baseline in the lines without LRRC4B | 0.080 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[HES2]] | C | HES2 activity raises FBXO2's level | lines that do not express HES2 (20) vs lines expressing it (30) | 2.61× lower at baseline in the lines without HES2 | 0.002 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2; co-absent with the target |
| [[PALM]] | C | PALM activity raises FBXO2's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.30× lower at baseline in the lines without PALM | 0.074 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO44]] | B | FBXO2 activity raises FBXO44's level | lines that do not express FBXO2 (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without FBXO2 | 0.005 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, LAMP3 |
| [[ARMH1]] | B | FBXO2 activity raises ARMH1's level | lines that do not express FBXO2 (23) vs lines expressing it (27) | 1.91× lower at baseline in the lines without FBXO2 | 0.037 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, LAMP3 |
| [[SLC16A13]] | B | FBXO2 activity raises SLC16A13's level | lines that do not express FBXO2 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without FBXO2 | 0.048 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, LAMP3 |
| [[HES2]] | C | FBXO2 activity raises HES2's level | lines that do not express FBXO2 (23) vs lines expressing it (27) | 2.09× lower at baseline in the lines without FBXO2 | 0.005 | ⚠ within organs, on part of the lines; also absent: HES2, YBX2, LAMP3; co-absent with the target |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.2, 28.8); signed map (36.3, 0.5). **Vector** length 45.1, 9.27% of its response variance represented; |z| ≥ 3 in 508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.3 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.6 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.6 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +4.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,637,018-11,655,785 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX2, Nfb42, Fbs1, Fbg1; previously OCP1 |
| Gene groups (HGNC) | F-boxes other |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UK22](https://www.uniprot.org/uniprotkb/Q9UK22) (F-box only protein 2):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex that mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Involved in the endoplasmic reticulum-associated degradation pathway (ERAD) for misfolded lumenal proteins by recognizing and binding sugar chains on unfolded glycoproteins that are retrotranslocated into the cytosol and promoting their ubiquitination and subsequent degradation. Prevents formation of …

**Summary**, from NCBI Gene [26232](https://www.ncbi.nlm.nih.gov/gene/26232):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of the ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13581) · Entrez [26232](https://www.ncbi.nlm.nih.gov/gene/26232) · UniProt [Q9UK22](https://www.uniprot.org/uniprotkb/Q9UK22) · Ensembl [ENSG00000116661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116661)

## Data

Gene col 3813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3813); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3813]; `tensor/DDL_lfc|DDL_z.npy` [3813]; `embed/gene_vectors.npy` [3813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3813 or target_col == 3813). Every well: [[FBXO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
