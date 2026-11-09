---
symbol: "DNAH7"
type: "gene"
col: 4034
ensembl_id: "ENSG00000118997"
name: "dynein axonemal heavy chain 7"
location: "2q32.3"
module: 27
arm: "+"
pooled_cpm: 6.09
n_lines_expressing: 49
n_dd_up: 36
n_dd_down: 7
n_dd_up_clean: 31
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# DNAH7

*dynein axonemal heavy chain 7* — 2q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.73× (z +17.3, q 0e+00, up in 46 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.592× (z -6.5, q 5e-08, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLEU1]] (+0.63, fdr 1e-05), [[LINC01876]] (+0.60, fdr 1e-05), [[TEX9]] (+0.58, fdr 7e-06); moves opposite to [[ABCC10]] (-0.56, fdr 1e-04), [[TUBGCP5]] (-0.56, fdr 1e-04), [[CCM2]] (-0.55, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NIHCOLE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.73×** | +17.3 | 0e+00 | 46/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.12×** | +13.8 | 7e-41 | 41/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.85×** | +13.8 | 7e-41 | 43/44 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +11.8 | 4e-30 | 28/39 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +11.7 | 2e-29 | 26/38 (AsPC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +8.1 | 5e-14 | 4/11 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.54×** | +7.8 | 5e-13 | 34/46 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.85×** | +7.6 | 3e-12 | 25/45 (LOX-IMVI, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.88×** | +7.2 | 3e-11 | 34/43 (A498, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +6.7 | 1e-09 | 8/17 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.16×** | +6.7 | 1e-09 | 21/38 (SHP-77, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +6.3 | 1e-08 | 13/27 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +6.0 | 7e-08 | 22/46 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.92×** | +5.7 | 5e-07 | 20/44 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.93×** | +5.5 | 1e-06 | 22/44 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.84×** | +5.3 | 4e-06 | 21/43 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.3 | 4e-06 | 15/47 (A-172, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.75×** | +4.9 | 3e-05 | 19/43 (LoVo, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.592×** | -6.5 | 5e-08 | 25/44 (HT-29, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.597×** | -4.5 | 0.002 | 18/38 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.455×** | -3.6 | 0.055 | 14/29 (MIA PaCa-2, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -3.5 | 0.055 | 13/46 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.572×** | -3.5 | 0.055 | 13/37 (HT-29, NCI-H23, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.684×** | -3.3 | 0.083 | 12/46 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.688×** | -3.3 | 0.083 | 17/45 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.705× | -3.1 | 0.14 | 17/45 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.707× | -3.0 | 0.14 | 12/42 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.709× | -3.0 | 0.14 | 11/44 (CFPAC-1, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.01 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 16.9× (z +11.1) | [[Sunitinib (drug)]] 5 µM 0.0541× (z -11.6) ⚠ toxic |
| [[A498 (line)]] | wt | 5.12 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 32.1× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 6.03 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 14.2× (z +9.3) | [[Sulfatinib (drug)]] 0.05 µM 0.0787× (z -8.6) |
| [[A-172 (line)]] | wt | 3.92 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 25.6× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 8.63 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0331× (z -10.6) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.0402× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 11.2 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0380× (z -12.3) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0786× (z -10.0) |
| [[PANC-1 (line)]] | alt | 3.53 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 18.0× (z +10.3) | — |
| [[C32 (line)]] | wt | 1.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0634× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 4.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0651× (z -10.9) |
| [[SHP-77 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0897× (z -14.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[A-427 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLEU1]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[LINC01876]] | +0.60 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TEX9]] | +0.58 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CFAP69]] | +0.58 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[DNAH6]] | +0.58 | +0.67 / +0.54 | both halves | 1e-05 | same gene group; STRING 583 |
| [[MAPK10]] | +0.57 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[DCDC1]] | +0.57 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[DRC3]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 | STRING 544 |
| [[TRMT10A]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[BRINP3]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MAPRE2]] | +0.54 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[MAP2K6]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC10]] | -0.56 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[TUBGCP5]] | -0.56 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[CCM2]] | -0.55 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[TAF12]] | -0.53 | -0.17 / -0.48 | ⚠ not reproduced | 0.001 |  |
| [[RAB11FIP3]] | -0.52 | -0.37 / -0.53 | both halves | 8e-05 | same gene group |
| [[ZBED4]] | -0.52 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ZNF767P-1]] | -0.51 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[TRIM27]] | -0.51 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[FBH1]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TRIM65]] | -0.51 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[RUSC2]] | -0.50 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[GAN]] | -0.50 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[PARVB]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIHCOLE]] | B | NIHCOLE activity raises DNAH7's level | lines that do not express NIHCOLE (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without NIHCOLE | 0.075 | ⚠ within organs, on part of the lines; also absent: RORC, TSPAN1, VIL1 |
| [[LINC01611]] | B | LINC01611 activity raises DNAH7's level | lines that do not express LINC01611 (34) vs lines expressing it (16) | 1.59× lower at baseline in the lines without LINC01611 | 0.096 | ⚠ within organs, on part of the lines; also absent: CDH13, ENSG00000248973, LINC02377 |
| [[WHRN]] | C | WHRN activity lowers DNAH7's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.42× higher at baseline in the lines without WHRN | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.429). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 38.6); signed map (54.6, 19.3). **Vector** length 66.5, 11.7% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +11.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +1.5 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -6.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.1 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -4.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.3 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.3 — chr2:195,737,703-196,068,837 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0944 |
| Gene groups (HGNC) | EF-hand domain containing; Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXX0](https://www.uniprot.org/uniprotkb/Q8WXX0) (Dynein axonemal heavy chain 7):

> Force generating protein that plays an important role in respiratory cilia and sperm flagella beating. Produces force towards the minus ends of microtubules. Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP (By similarity).

**Summary**, from NCBI Gene [56171](https://www.ncbi.nlm.nih.gov/gene/56171):

> DNAH7 is a component of the inner dynein arm of ciliary axonemes (Zhang et al., 2002 [PubMed 11877439]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18661) · Entrez [56171](https://www.ncbi.nlm.nih.gov/gene/56171) · UniProt [Q8WXX0](https://www.uniprot.org/uniprotkb/Q8WXX0) · Ensembl [ENSG00000118997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118997)

## Data

Gene col 4034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4034); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4034]; `tensor/DDL_lfc|DDL_z.npy` [4034]; `embed/gene_vectors.npy` [4034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4034 or target_col == 4034). Every well: [[DNAH7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
