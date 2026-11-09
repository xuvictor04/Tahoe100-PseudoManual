---
symbol: "ABCC3"
type: "gene"
col: 3003
ensembl_id: "ENSG00000108846"
name: "ATP binding cassette subfamily C member 3"
location: "17q21.33"
module: 31
arm: "+"
pooled_cpm: 114.95
n_lines_expressing: 34
n_dd_up: 11
n_dd_down: 50
n_dd_up_clean: 9
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 50
direction_downstream: 69
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ABCC3

*ATP binding cassette subfamily C member 3* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.28× (z +4.8, q 7e-04, up in 17 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.136× (z -27.6, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN8]] (+0.70, fdr 7e-06), [[MST1R]] (+0.65, fdr 7e-06), [[LAMA3]] (+0.64, fdr 7e-06); moves opposite to [[PRKAB2]] (-0.47, fdr 5e-05), [[BLTP3B]] (-0.44, fdr 3e-05), [[PLEKHO1]] (-0.44, fdr 2e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 50 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 69 go from it, the strongest it → [[TBC1D8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 7e-04 | 17/32 (AsPC-1, NCI-H1792, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 0.001 | 21/32 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 0.002 | 17/32 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.006 | 18/32 (BT-474, LS 180, …) | two highest doses |  |
| [[Bexarotene (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.007 | 18/32 (LS 180, SW480, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.33×** | +4.0 | 0.007 | 16/32 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.012 | 16/31 (LoVo, COLO 205, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.6 | 0.021 | 16/32 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Mifepristone (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.022 | 17/32 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.067 | 16/32 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +3.2 | 0.067 | 14/33 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.136×** | -27.6 | 0e+00 | 32/32 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.141×** | -27.1 | 0e+00 | 32/32 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.297×** | -23.8 | 0e+00 | 30/32 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.183×** | -23.5 | 0e+00 | 32/32 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.386×** | -13.2 | 2e-37 | 30/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.454×** | -10.9 | 7e-26 | 29/32 (SW 900, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.594×** | -10.2 | 1e-22 | 26/32 (BT-474, CHP-212, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -9.4 | 5e-19 | 24/33 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.532×** | -8.7 | 2e-16 | 30/32 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.541×** | -8.5 | 1e-15 | 27/32 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.545×** | -8.4 | 2e-15 | 27/32 (LoVo, SW 900, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.332×** | -8.0 | 8e-14 | 29/33 (BT-474, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.546×** | -7.9 | 1e-13 | 26/32 (NCI-H1573, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.553×** | -7.9 | 1e-13 | 23/32 (NCI-H1573, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.341×** | -7.8 | 3e-13 | 29/33 (NCI-H1573, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.630×** | -7.5 | 3e-12 | 24/34 (BT-474, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 650 | 0 | 58 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -27.5) |
| [[KATO III (line)]] | alt | 429 | 0 | 29 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0220× (z -39.8) |
| [[LoVo (line)]] | wt | 229 | 0 | 22 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0332× (z -38.8) |
| [[HEC-1-A (line)]] | alt | 340 | 0 | 16 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -29.1) |
| [[NCI-H1573 (line)]] | alt | 233 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0528× (z -40.7) |
| [[HT-29 (line)]] | alt | 341 | 0 | 14 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -24.6) |
| [[LS 180 (line)]] | wt | 181 | 1 | 13 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.79× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -28.9) |
| [[SW 900 (line)]] | alt | 179 | 0 | 12 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0531× (z -21.4) |
| [[HCT15 (line)]] | alt | 152 | 0 | 11 | — | [[Panobinostat (drug)]] 5 µM 0.0877× (z -19.3) |
| [[NCI-H460 (line)]] | wt | 99.9 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0658× (z -22.5) |
| [[SW480 (line)]] | alt | 68.8 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0809× (z -28.3) |
| [[A549 (line)]] | wt | 280 | 0 | 9 | — | [[Panobinostat (drug)]] 0.5 µM 0.0602× (z -20.8) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0691× (z -19.8) |
| [[SW1417 (line)]] | alt | 96.2 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -21.1) |
| [[COLO 205 (line)]] | alt | 290 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0399× (z -32.2) |
| [[NCI-H23 (line)]] | alt | 47.8 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.183× (z -11.6) |
| [[A498 (line)]] | wt | 139 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.5) |
| [[PANC-1 (line)]] | alt | 48.8 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 156 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -18.7) |
| [[AsPC-1 (line)]] | alt | 64.2 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -16.0) |
| [[NCI-H2030 (line)]] | alt | 98.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -19.5) |
| [[SW48 (line)]] | wt | 56.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 67.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -13.1) |
| [[HOP62 (line)]] | alt | 39.5 | 1 | 3 | [[Clobetasol propionate (drug)]] 0.05 µM 3.80× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -10.7) |
| [[H4 (line)]] | wt | 57.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0714× (z -14.2) |
| [[Hs 766T (line)]] | wt | 78.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -16.7) |
| [[J82 (line)]] | alt | 52.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 58.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 62.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -14.1) |
| [[CHP-212 (line)]] | wt | 61.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.184× (z -10.1) |
| [[NCI-H596 (line)]] | alt | 98.5 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.139× (z -16.2) |
| [[A-172 (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN8]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[MST1R]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LAMA3]] | +0.64 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TNS4]] | +0.62 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[SLC16A5]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[PCED1B]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.59 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CASC19]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SLC22A3]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 | pathway: Drug ADME; STRING 484 |
| [[SDR16C5]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[SH2D3A]] | +0.56 | +0.57 / +0.62 | both halves | 1e-05 | STRING 433 |
| [[MUC2]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAB2]] | -0.47 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[BLTP3B]] | -0.44 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PLEKHO1]] | -0.44 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*50 arrows, 50 of them with an alert ⚠; grade A 0, B 36, C 14. Shown: the 12 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises ABCC3's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.82× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TBC1D8]] | B | TBC1D8 activity raises ABCC3's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 5.83× lower at baseline in the lines without TBC1D8 | 0.002 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ABCC3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.88× lower at baseline in the lines without TMPRSS4 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[MET]] | B | MET activity raises ABCC3's level | lines that do not express MET (9) vs lines expressing it (41) | 5.26× lower at baseline in the lines without MET | 0.008 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[MALL]] | B | MALL activity raises ABCC3's level | lines that do not express MALL (21) vs lines expressing it (29) | 3.26× lower at baseline in the lines without MALL | 0.008 | ⚠ within organs, on part of the lines; also absent: SDR16C5, SPNS2, CLDN4 |
| [[KRT7]] | B | KRT7 activity raises ABCC3's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 3.04× lower at baseline in the lines without KRT7 | 0.009 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[PSORS1C1]] | B | PSORS1C1 activity raises ABCC3's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.45× lower at baseline in the lines without PSORS1C1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[SYT12]] | B | SYT12 activity raises ABCC3's level | lines that do not express SYT12 (9) vs lines expressing it (41) | 3.25× lower at baseline in the lines without SYT12 | 0.013 | ⚠ within organs, on part of the lines; also absent: EMSLR; maybe low, not absent |
| [[PRKCA]] | B | PRKCA activity raises ABCC3's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 5.35× lower at baseline in the lines without PRKCA | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[GJB2]] | B | GJB2 activity raises ABCC3's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 2.46× lower at baseline in the lines without GJB2 | 0.018 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |
| [[KRT86]] | B | KRT86 activity raises ABCC3's level | lines that do not express KRT86 (19) vs lines expressing it (31) | 3.56× lower at baseline in the lines without KRT86 | 0.019 | ⚠ within organs, on part of the lines; also absent: SPNS2, EDN2, SLPI |
| [[AREG]] | B | AREG activity raises ABCC3's level | lines that do not express AREG (26) vs lines expressing it (24) | 3.82× lower at baseline in the lines without AREG | 0.020 | ⚠ within organs, on part of the lines; also absent: TC2N, ESRP1, CRB3 |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 55, C 14. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D8]] | B | ABCC3 activity raises TBC1D8's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.55× lower at baseline in the lines without ABCC3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[MET]] | B | ABCC3 activity raises MET's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.66× lower at baseline in the lines without ABCC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[PRKCA]] | B | ABCC3 activity raises PRKCA's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without ABCC3 | 0.004 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[PSORS1C1]] | B | ABCC3 activity raises PSORS1C1's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.16× lower at baseline in the lines without ABCC3 | 0.008 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ACSL5]] | B | ABCC3 activity raises ACSL5's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.76× lower at baseline in the lines without ABCC3 | 0.009 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[B3GNT3]] | B | ABCC3 activity raises B3GNT3's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 3.68× lower at baseline in the lines without ABCC3 | 0.010 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ITGA6]] | B | ABCC3 activity raises ITGA6's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.42× lower at baseline in the lines without ABCC3 | 0.013 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[HAS3]] | B | ABCC3 activity raises HAS3's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without ABCC3 | 0.015 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ADGRE2]] | B | ABCC3 activity raises ADGRE2's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without ABCC3 | 0.017 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | ABCC3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express ABCC3 (16) vs lines expressing it (32) | the lines without ABCC3: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[SOX12]] | B | ABCC3 activity lowers SOX12's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 1.93× higher at baseline in the lines without ABCC3 | 0.018 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[EPHA2-AS1]] | B | ABCC3 activity raises EPHA2-AS1's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without ABCC3 | 0.028 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, 50.5); signed map (5.1, 37.7). **Vector** length 131, 46.6% of its response variance represented; |z| ≥ 3 in 1,592 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.6 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +2.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.0 | -7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.0 | -8.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.8 | -10.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.6 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily C member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,634,777-50,692,253 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP3, cMOAT2, EST90757, MLP2, MOAT-D |
| Gene groups (HGNC) | ATP binding cassette subfamily C |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 15 pathways, smallest: NFE2L2 regulating MDR associated enzymes; Recycling of bile acids and salts; Aspirin ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [O15438](https://www.uniprot.org/uniprotkb/O15438) (ATP-binding cassette sub-family C member 3):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family that hydrolyzes ATP to enable active transport of substrates conjugated with glucuronate, glutathione or sulfate. Operates at basolateral membranes of polarized cells such as hepatocytes and intestinal epithelial cells, where it mediates the efflux of conjugated substrates from intestine and liver into the bloodstream. Involved in enterohepatic recirculation of steroid glucuronates. Shares substrate specificity with MRP2, …

**Summary**, from NCBI Gene [8714](https://www.ncbi.nlm.nih.gov/gene/8714):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the MRP subfamily which is involved in multi-drug resistance. The specific function of this protein has not yet been determined; however, this protein may play a role in the …

**Accessions** — [HGNC:54](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54) · Entrez [8714](https://www.ncbi.nlm.nih.gov/gene/8714) · UniProt [O15438](https://www.uniprot.org/uniprotkb/O15438) · Ensembl [ENSG00000108846](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108846)

## Data

Gene col 3003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3003); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3003]; `tensor/DDL_lfc|DDL_z.npy` [3003]; `embed/gene_vectors.npy` [3003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3003 or target_col == 3003). Every well: [[ABCC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
