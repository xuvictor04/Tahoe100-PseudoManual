---
symbol: "FAM76A"
type: "gene"
col: 191
ensembl_id: "ENSG00000009780"
name: "family with sequence similarity 76 member A"
location: "1p35.3"
module: 47
arm: "+"
pooled_cpm: 10.83
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 12
n_dd_up_clean: 26
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# FAM76A

*family with sequence similarity 76 member A* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.29× (z +21.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.524× (z -11.9, q 7e-30, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HABP4]] (+0.58, fdr 2e-05), [[MTM1]] (+0.54, fdr 7e-05), [[ZC2HC1A]] (+0.53, fdr 3e-05); moves opposite to [[FERMT3]] (-0.51, fdr 3e-05), [[TTN-AS1]] (-0.50, fdr 3e-04), [[PTOV1-AS1]] (-0.49, fdr 5e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYH15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.29×** | +21.9 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.22×** | +21.5 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.75×** | +18.6 | 0e+00 | 44/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +15.7 | 0e+00 | 30/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +11.1 | 2e-26 | 36/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +9.8 | 1e-20 | 29/40 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +9.5 | 1e-19 | 25/43 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +8.4 | 3e-15 | 29/45 (HT-29, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.43×** | +7.6 | 2e-12 | 22/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +6.9 | 2e-10 | 21/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.6 | 3e-09 | 24/45 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.9 | 1e-07 | 8/18 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 1e-06 | 15/43 (C-33 A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.2 | 6e-06 | 15/48 (A-427, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +5.0 | 2e-05 | 13/47 (HS-578T, A-427, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.7 | 9e-05 | 12/45 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +4.3 | 5e-04 | 4/47 (SW480, HCT15, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.524×** | -11.9 | 7e-30 | 33/47 (HT-29, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.292×** | -10.5 | 2e-23 | 31/47 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.432×** | -7.2 | 1e-10 | 22/43 (HS-578T, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -6.5 | 8e-09 | 18/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -5.8 | 9e-07 | 20/44 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.749×** | -5.3 | 9e-06 | 19/46 (HT-29, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.744×** | -5.2 | 2e-05 | 17/46 (SNU-1, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.760×** | -5.1 | 3e-05 | 15/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.770×** | -4.6 | 3e-04 | 14/46 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.617×** | -4.1 | 0.002 | 7/41 (NCI-H1792, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.638×** | -3.9 | 0.006 | 13/44 (J82, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.785×** | -3.2 | 0.067 | 8/47 (HS-578T, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.844× | -3.1 | 0.074 | 1/47 (COLO 205) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.845× | -3.1 | 0.074 | 13/47 (PANC-1, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.9 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.71× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -11.7) |
| [[A498 (line)]] | wt | 10.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.8) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.254× (z -9.9) |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0315× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 7.01 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0859× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Hesperidin (drug)]] 5 µM 0.136× (z -9.3) |
| [[SW480 (line)]] | alt | 9.57 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.54× (z +10.0) | — |
| [[A-172 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0416× (z -16.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 15.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 6.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 9.97 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0772× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HABP4]] | +0.58 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[MTM1]] | +0.54 | +0.37 / +0.52 | both halves | 7e-05 |  |
| [[ZC2HC1A]] | +0.53 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[GALNT11]] | +0.53 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[SLC66A3]] | +0.51 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[ILKAP]] | +0.50 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[WASHC4]] | +0.50 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[ELMO2]] | +0.48 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[OPTN]] | +0.48 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[RUSC1]] | +0.47 | +0.15 / +0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[TRIM36]] | +0.47 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[KIF3A]] | +0.47 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[FLYWCH2]] | +0.47 | +0.24 / +0.49 | both halves | 4e-04 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT3]] | -0.51 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[TTN-AS1]] | -0.50 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[PTOV1-AS1]] | -0.49 | -0.24 / -0.57 | both halves | 5e-04 |  |
| [[LAT2]] | -0.48 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[SLC9A5]] | -0.47 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[CCNH]] | -0.46 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[DNAH1]] | -0.46 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[TRA2B]] | -0.46 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[MPP4]] | -0.46 | -0.26 / -0.42 | both halves | 3e-04 |  |
| [[TBC1D22A]] | -0.46 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[SLC4A10]] | -0.45 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[XRCC4]] | -0.45 | -0.30 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYH15]] | B | MYH15 activity lowers FAM76A's level | lines that do not express MYH15 (10) vs lines expressing it (40) | 1.30× higher at baseline in the lines without MYH15 | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FAM76A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction -0.439). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.0, -21.8); signed map (-25.2, 5.0). **Vector** length 63.4, 10.1% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.2 | +4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +9.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.7 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +6.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.7 | -11.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.4 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 76 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,725,961-27,763,116 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34648 |
| Matched by | ensembl_id |

UniProt [Q8TAV0](https://www.uniprot.org/uniprotkb/Q8TAV0) carries no function annotation.

**Summary**, from NCBI Gene [199870](https://www.ncbi.nlm.nih.gov/gene/199870):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28530) · Entrez [199870](https://www.ncbi.nlm.nih.gov/gene/199870) · UniProt [Q8TAV0](https://www.uniprot.org/uniprotkb/Q8TAV0) · Ensembl [ENSG00000009780](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009780)

## Data

Gene col 191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 191); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 191]; `tensor/DDL_lfc|DDL_z.npy` [191]; `embed/gene_vectors.npy` [191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 191 or target_col == 191). Every well: [[FAM76A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM76A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
