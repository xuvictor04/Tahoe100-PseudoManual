---
symbol: "ADAM28"
type: "gene"
col: 491
ensembl_id: "ENSG00000042980"
name: "ADAM metallopeptidase domain 28"
location: "8p21.2"
module: 155
arm: "+"
pooled_cpm: 22.14
n_lines_expressing: 19
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 32
direction_downstream: 42
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# ADAM28

*ADAM metallopeptidase domain 28* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.50× (z +13.6, q 3e-39, up in 13 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.491× (z -7.4, q 8e-11, down in 15 of 16 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB3]] (+0.69, fdr 7e-06), [[SERPINB4]] (+0.66, fdr 7e-06), [[C2CD4A]] (+0.62, fdr 1e-05); moves opposite to [[NDST1]] (-0.48, fdr 2e-04), [[HOMER2]] (-0.46, fdr 6e-05), [[TXNRD3]] (-0.44, fdr 3e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[SCAT1]] → it (grade B ⚠); 42 go from it, the strongest it → [[MILR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +13.6 | 3e-39 | 13/17 (KATO III, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +7.6 | 5e-12 | 0/14 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +7.6 | 5e-12 | 14/17 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.1 | 1e-07 | 0/12 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.7 | 2e-04 | 0/16 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.042 | 4/16 (KATO III, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.075 | 1/16 (BT-474) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.075 | 4/16 (AsPC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.491×** | -7.4 | 8e-11 | 15/16 (SHP-77, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.542×** | -6.3 | 6e-08 | 13/16 (NCI-H1792, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.559×** | -5.8 | 1e-06 | 12/15 (NCI-H1792, COLO 205, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.587×** | -5.5 | 4e-06 | 12/16 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.587×** | -5.5 | 4e-06 | 15/16 (SHP-77, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.692×** | -5.4 | 7e-06 | 15/16 (NCI-H1792, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.620×** | -4.9 | 6e-05 | 12/16 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -4.9 | 6e-05 | 13/16 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.625×** | -4.9 | 7e-05 | 6/16 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.637×** | -4.7 | 2e-04 | 12/16 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.629×** | -4.4 | 5e-04 | 6/16 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.669×** | -4.2 | 0.001 | 9/16 (CFPAC-1, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.659×** | -4.2 | 0.001 | 9/16 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.680×** | -4.0 | 0.003 | 11/16 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.767×** | -3.9 | 0.004 | 14/18 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.722×** | -3.4 | 0.026 | 8/16 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 404 | 0 | 22 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -21.6) |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0389× (z -29.0) |
| [[NCI-H1573 (line)]] | alt | 69.6 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0714× (z -22.2) |
| [[SW 900 (line)]] | alt | 64.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -21.4) |
| [[KATO III (line)]] | alt | 57.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0814× (z -18.3) |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0873× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.145× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 54.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -15.8) |
| [[COLO 205 (line)]] | alt | 7.15 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0364× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.7) |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0952× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H23 (line)]] | alt | 6.57 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0459× (z -11.3) |
| [[A-172 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB3]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB4]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[C2CD4A]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[ADGRE2]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TREM1]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[GPR141]] | +0.59 | +0.41 / +0.62 | both halves | 4e-05 | **novel candidate** |
| [[SLC15A1]] | +0.58 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[ACKR3]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DUOX2]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CEMIP]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TMEM163]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CLDN10]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDST1]] | -0.48 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[HOMER2]] | -0.46 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[TXNRD3]] | -0.44 | -0.45 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 7, C 25. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAT1]] | B | SCAT1 activity raises ADAM28's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 2.92× lower at baseline in the lines without SCAT1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[ABHD17C]] | B | ABHD17C activity raises ADAM28's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 2.76× lower at baseline in the lines without ABHD17C | 0.070 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ADAM28's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[GNA15]] | B | GNA15 activity raises ADAM28's level | lines that do not express GNA15 (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without GNA15 | 0.077 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent |
| [[DHRS3]] | B | DHRS3 activity raises ADAM28's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without DHRS3 | 0.087 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[PTGES]] | B | PTGES activity raises ADAM28's level | lines that do not express PTGES (17) vs lines expressing it (33) | 2.55× lower at baseline in the lines without PTGES | 0.092 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |
| [[TMEM92]] | B | TMEM92 activity raises ADAM28's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without TMEM92 | 0.0996 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[MMP13]] | C | MMP13 activity raises ADAM28's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 3.67× lower at baseline in the lines without MMP13 | 0.003 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4; co-absent with the target |
| [[SERPINB3]] | C | SERPINB3 activity raises ADAM28's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 4.62× lower at baseline in the lines without SERPINB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[CP]] | C | CP activity raises ADAM28's level | lines that do not express CP (39) vs lines expressing it (11) | 4.15× lower at baseline in the lines without CP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |
| [[SLC24A3]] | C | SLC24A3 activity raises ADAM28's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 2.31× lower at baseline in the lines without SLC24A3 | 0.008 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent; co-absent with the target |
| [[LINC02015]] | C | LINC02015 activity raises ADAM28's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without LINC02015 | 0.009 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 23, C 19. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MILR1]] | B | ADAM28 activity raises MILR1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without ADAM28 | 0.003 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[NDST1]] | B | ADAM28 activity lowers NDST1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.44× higher at baseline in the lines without ADAM28 | 0.005 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[DHRS3]] | B | ADAM28 activity raises DHRS3's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.51× lower at baseline in the lines without ADAM28 | 0.008 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[ABHD17C]] | B | ADAM28 activity raises ABHD17C's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.43× lower at baseline in the lines without ADAM28 | 0.010 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[SCAT1]] | B | ADAM28 activity raises SCAT1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.74× lower at baseline in the lines without ADAM28 | 0.017 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[TYMP]] | B | ADAM28 activity raises TYMP's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.26× lower at baseline in the lines without ADAM28 | 0.025 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[PECAM1]] | B | ADAM28 activity raises PECAM1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without ADAM28 | 0.027 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[ODF3B]] | B | ADAM28 activity raises ODF3B's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without ADAM28 | 0.033 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[SIPA1L2]] | B | ADAM28 activity raises SIPA1L2's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without ADAM28 | 0.034 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[DNAH2]] | B | ADAM28 activity raises DNAH2's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.82× lower at baseline in the lines without ADAM28 | 0.048 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[TMC1]] | B | ADAM28 activity raises TMC1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 1.37× lower at baseline in the lines without ADAM28 | 0.055 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[MILR1]] | B | ADAM28 activity strengthens MILR1's drug response | lines that do not express ADAM28 (16) vs lines expressing it (12) | the lines without ADAM28 respond 0.81× as strongly (z diff +0.66); strongest at Panobinostat 5 µM: 0.49x vs 0.25x (z diff +2.8) | 0.055 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.4, 47.5); signed map (53.8, 23.9). **Vector** length 79.9, 27.2% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.9 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +3.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.9 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -5.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -4.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:24,294,069-24,359,014 (+) |
| Ensembl biotype | protein_coding |
| Also known as | eMDCII, MDC-Lm, MDC-Ls, ADAM23 |
| Gene groups (HGNC) | ADAM metallopeptidase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKQ2](https://www.uniprot.org/uniprotkb/Q9UKQ2) (Disintegrin and metalloproteinase domain-containing protein 28):

> May play a role in the adhesive and proteolytic events that occur during lymphocyte emigration or may function in ectodomain shedding of lymphocyte surface target proteins, such as FASL and CD40L. May be involved in sperm maturation.

**Summary**, from NCBI Gene [10863](https://www.ncbi.nlm.nih.gov/gene/10863):

> This gene encodes a member of the ADAM (a disintegrin and metalloprotease domain) family. Members of this family are membrane-anchored proteins structurally related to snake venom disintegrins, and have been implicated in a variety of biological processes involving cell-cell and cell-matrix interactions, including fertilization, muscle development, and neurogenesis. The protein encoded by this gene is a lymphocyte-expressed ADAM protein. This gene is present in a gene cluster with other members …

**Accessions** — [HGNC:206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:206) · Entrez [10863](https://www.ncbi.nlm.nih.gov/gene/10863) · UniProt [Q9UKQ2](https://www.uniprot.org/uniprotkb/Q9UKQ2) · Ensembl [ENSG00000042980](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042980)

## Data

Gene col 491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 491); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 491]; `tensor/DDL_lfc|DDL_z.npy` [491]; `embed/gene_vectors.npy` [491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 491 or target_col == 491). Every well: [[ADAM28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
