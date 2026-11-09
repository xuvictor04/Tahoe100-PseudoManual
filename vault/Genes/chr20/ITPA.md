---
symbol: "ITPA"
type: "gene"
col: 4687
ensembl_id: "ENSG00000125877"
name: "inosine triphosphatase"
location: "20p13"
module: 124
arm: "+"
pooled_cpm: 20.32
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 17
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# ITPA

*inosine triphosphatase* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +13.7, q 4e-40, up in 37 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.08× (z +9.9, q 6e-21, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.447× (z -10.9, q 6e-25, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH4]] (+0.76, fdr 7e-06), [[ZC3H7B]] (+0.74, fdr 7e-06), [[ST7L]] (+0.72, fdr 1e-05); moves opposite to [[RAB3A]] (-0.77, fdr 7e-06), [[CDON]] (-0.72, fdr 7e-06), [[PJA2]] (-0.72, fdr 2e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +13.7 | 4e-40 | 37/41 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +12.5 | 3e-33 | 25/30 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.08×** | +9.9 | 6e-21 | 42/46 (NCI-H1792, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +8.1 | 1e-13 | 27/35 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.7 | 2e-12 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.5 | 8e-12 | 36/48 (A-172, RKO, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +6.3 | 2e-08 | 34/47 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.0 | 2e-07 | 25/44 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +5.5 | 2e-06 | 31/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +5.4 | 3e-06 | 30/48 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +4.8 | 1e-04 | 23/47 (A-172, HCT15, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 1e-04 | 23/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.4 | 4e-04 | 19/46 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +4.4 | 4e-04 | 20/45 (A-172, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +4.2 | 0.001 | 23/46 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.002 | 14/46 (A498, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.71×** | +3.8 | 0.005 | 15/46 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.006 | 18/47 (RPMI-7951, SW 900, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.026 | 11/45 (KATO III, A549, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.58×** | +3.2 | 0.032 | 8/43 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -10.9 | 6e-25 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.464×** | -10.4 | 7e-23 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.501×** | -9.4 | 2e-18 | 37/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.598×** | -7.0 | 5e-10 | 35/48 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.702×** | -6.8 | 2e-09 | 34/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.501×** | -4.9 | 9e-05 | 23/48 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.552×** | -4.2 | 0.002 | 17/48 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.749×** | -3.9 | 0.006 | 20/48 (SK-MEL-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.621×** | -3.4 | 0.047 | 14/45 (SW480, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -12.4) |
| [[SW480 (line)]] | alt | 35.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.283× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 25.3 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.28× (z +9.3) | — |
| [[A-427 (line)]] | wt | 13.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -9.9) |
| [[H4 (line)]] | wt | 14.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0762× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 21.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -9.4) |
| [[LS 180 (line)]] | wt | 17.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.74× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -10.6) |
| [[RKO (line)]] | wt | 29.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -8.9) |
| [[SNU-423 (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.105× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH4]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[ZC3H7B]] | +0.74 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ST7L]] | +0.72 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[METTL8]] | +0.72 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.71 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.71 | +0.75 / +0.41 | both halves | 4e-05 |  |
| [[DNAJC11]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[AVEN]] | +0.71 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[QTRT1]] | +0.71 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[UTP20]] | +0.70 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.70 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[TMEM192]] | +0.70 | +0.70 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.77 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[CDON]] | -0.72 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[PJA2]] | -0.72 | -0.75 / -0.46 | both halves | 2e-05 |  |
| [[GMCL1]] | -0.69 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[NXPH4]] | -0.69 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[DNAAF3]] | -0.69 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ARL3]] | -0.68 | -0.65 / -0.40 | both halves | 4e-05 |  |
| [[YIF1B]] | -0.68 | -0.62 / -0.27 | both halves | 3e-04 |  |
| [[ALKBH5]] | -0.67 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[ARL6]] | -0.66 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[RIMS3]] | -0.66 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[POGLUT2]] | -0.66 | -0.60 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ITPA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C2]] | B | NR3C2 activity lowers ITPA's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.34× higher at baseline in the lines without NR3C2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[BMPR1B]] | B | BMPR1B activity lowers ITPA's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.39× higher at baseline in the lines without BMPR1B | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1 |
| [[NR3C2]] | B | NR3C2 activity weakens ITPA's drug response | lines that do not express NR3C2 (15) vs lines expressing it (33) | the lines without NR3C2 respond 1.04× as strongly (z diff -0.21); strongest at Belinostat 5 µM: 0.43x vs 0.55x (z diff -2.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ITPA's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ITPA's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LRP1]] | C | LRP1 activity lowers ITPA's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 1.69× higher at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.835). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (6.6, -7.0); signed map (20.9, -29.2). **Vector** length 101, 24.9% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +5.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.5 | +2.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -10.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | inosine triphosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,208,868-3,223,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HLC14-06-P, dJ794I6.3; previously C20orf37 |
| Hallmark sets | DNA_REPAIR |
| Reactome | 5 pathways, smallest: Ribavirin ADME; Purine catabolism; Nucleotide catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BY32](https://www.uniprot.org/uniprotkb/Q9BY32) (Inosine triphosphate pyrophosphatase):

> Pyrophosphatase that hydrolyzes the non-canonical purine nucleotides inosine triphosphate (ITP), deoxyinosine triphosphate (dITP) as well as 2'-deoxy-N-6-hydroxylaminopurine triphosphate (dHAPTP) and xanthosine 5'-triphosphate (XTP) to their respective monophosphate derivatives. The enzyme does not distinguish between the deoxy- and ribose forms. Probably excludes non-canonical purines from RNA and DNA precursor pools, thus preventing their incorporation into RNA and DNA and avoiding …

**Summary**, from NCBI Gene [3704](https://www.ncbi.nlm.nih.gov/gene/3704):

> This gene encodes an inosine triphosphate pyrophosphohydrolase. The encoded protein hydrolyzes inosine triphosphate and deoxyinosine triphosphate to the monophosphate nucleotide and diphosphate. This protein, which is a member of the HAM1 NTPase protein family, is found in the cytoplasm and acts as a homodimer. Defects in the encoded protein can result in inosine triphosphate pyrophosphorylase deficiency which causes an accumulation of ITP in red blood cells. Alternate splicing results in …

**Accessions** — [HGNC:6176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6176) · Entrez [3704](https://www.ncbi.nlm.nih.gov/gene/3704) · UniProt [Q9BY32](https://www.uniprot.org/uniprotkb/Q9BY32) · Ensembl [ENSG00000125877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125877)

## Data

Gene col 4687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4687); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4687]; `tensor/DDL_lfc|DDL_z.npy` [4687]; `embed/gene_vectors.npy` [4687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4687 or target_col == 4687). Every well: [[ITPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
