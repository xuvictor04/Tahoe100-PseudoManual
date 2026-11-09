---
symbol: "KCTD12"
type: "gene"
col: 10949
ensembl_id: "ENSG00000178695"
name: "potassium channel tetramerization domain containing 12"
location: "13q22.3"
module: 9
arm: "+"
pooled_cpm: 9.48
n_lines_expressing: 34
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KCTD12

*potassium channel tetramerization domain containing 12* — 13q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +9.9, q 2e-20, up in 8 of 13 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.90× (z +9.0, q 5e-17, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.538× (z -6.2, q 4e-07, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KITLG]] (+0.61, fdr 7e-06), [[ADAMTS3]] (+0.59, fdr 1e-05), [[ENC1]] (+0.58, fdr 1e-05); moves opposite to [[CRYZL1]] (-0.56, fdr 1e-05), [[TULP3]] (-0.55, fdr 1e-05), [[ALKBH7]] (-0.55, fdr 2e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DCLK1]] → it (grade B ⚠); 3 go from it, the strongest it → [[ARSJ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.83×** | +9.9 | 2e-20 | 8/13 (LOX-IMVI, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.52×** | +9.2 | 1e-17 | 20/24 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +9.0 | 5e-17 | 24/32 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +8.8 | 1e-16 | 13/19 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +6.4 | 2e-08 | 19/31 (NCI-H460, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +6.4 | 2e-08 | 17/30 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.0 | 1e-07 | 18/32 (J82, CFPAC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +5.8 | 4e-07 | 19/31 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +5.5 | 2e-06 | 19/32 (J82, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +4.8 | 9e-05 | 11/32 (NCI-H1573, SW48, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +4.8 | 1e-04 | 13/29 (HOP62, CFPAC-1, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +4.2 | 0.001 | 15/31 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.002 | 12/32 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.44×** | +3.7 | 0.010 | 14/31 (A498, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +3.5 | 0.016 | 7/29 (HT-29, A549, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.026 | 8/32 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.041 | 9/32 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.538×** | -6.2 | 4e-07 | 22/31 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.559×** | -5.8 | 2e-06 | 19/31 (BT-474, SW48, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.583×** | -5.1 | 8e-05 | 18/31 (SHP-77, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.646×** | -4.3 | 0.002 | 16/30 (A549, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.661×** | -4.1 | 0.005 | 12/32 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.764×** | -3.8 | 0.015 | 15/32 (CHP-212, Hs 766T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -3.7 | 0.020 | 15/29 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0237× (z -12.7) |
| [[Hs 766T (line)]] | wt | 137 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -9.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.121× (z -8.6) |
| [[HOP62 (line)]] | alt | 8.31 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +13.9) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 7.70 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0572× (z -9.7) |
| [[J82 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.12× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0871× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 5.94 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0650× (z -9.0) |
| [[SW48 (line)]] | wt | 12.4 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0860× (z -8.6) |
| [[A-172 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KITLG]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ADAMTS3]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ENC1]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[SYNM]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[C21orf91]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TNC]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[BBS10]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NETO2]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[CHRM3]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FAT1]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[ZNF462]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[MMP16]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TULP3]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ALKBH7]] | -0.55 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ULK1]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[MIGA2]] | -0.54 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[ATP5MJ]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[CBFA2T2]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[ZNF500]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PSMD9]] | -0.53 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MZT2B]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[EGFL8]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[RANBP10]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK1]] | B | DCLK1 activity raises KCTD12's level | lines that do not express DCLK1 (19) vs lines expressing it (31) | 2.83× lower at baseline in the lines without DCLK1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, VAT1L, ENSG00000283982 |
| [[HHEX]] | B | HHEX activity lowers KCTD12's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.07× higher at baseline in the lines without HHEX | 0.033 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |
| [[PSMB5]] | B | PSMB5 activity raises KCTD12's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FZD1]] | B | FZD1 activity raises KCTD12's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 3.01× lower at baseline in the lines without FZD1 | 0.093 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARSJ]] | B | KCTD12 activity raises ARSJ's level | lines that do not express KCTD12 (16) vs lines expressing it (34) | 2.84× lower at baseline in the lines without KCTD12 | 0.060 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, NALCN, LINC01828 |
| [[WLS]] | B | KCTD12 activity raises WLS's level | lines that do not express KCTD12 (16) vs lines expressing it (34) | 1.33× lower at baseline in the lines without KCTD12 | 0.081 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, NALCN, LINC01828 |
| [[NEGR1]] | C | KCTD12 activity raises NEGR1's level | lines that do not express KCTD12 (16) vs lines expressing it (34) | 3.73× lower at baseline in the lines without KCTD12 | 0.090 | ⚠ within organs, on part of the lines; also absent: CACNA2D1, NALCN, LINC01828; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.422). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.3, 26.7); signed map (28.1, 35.5). **Vector** length 69.3, 14.7% of its response variance represented; |z| ≥ 3 in 772 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.1 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.9 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +4.8 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -5.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.2 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q22.3 — chr13:76,880,175-76,886,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1778, PFET1; previously C13orf2 |
| Gene groups (HGNC) | BTB domain containing; KCTD family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CX2](https://www.uniprot.org/uniprotkb/Q96CX2) (BTB/POZ domain-containing protein KCTD12):

> Auxiliary subunit of GABA-B receptors that determine the pharmacology and kinetics of the receptor response. Increases agonist potency and markedly alter the G protein signaling of the receptors by accelerating onset and promoting desensitization (By similarity).

**Summary**, from NCBI Gene [115207](https://www.ncbi.nlm.nih.gov/gene/115207):

> Enables identical protein binding activity. Predicted to be involved in regulation of G protein-coupled receptor signaling pathway. Predicted to be part of signaling receptor complex. Predicted to be active in GABA-ergic synapse; postsynaptic membrane; and presynaptic active zone membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14678) · Entrez [115207](https://www.ncbi.nlm.nih.gov/gene/115207) · UniProt [Q96CX2](https://www.uniprot.org/uniprotkb/Q96CX2) · Ensembl [ENSG00000178695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178695)

## Data

Gene col 10949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10949); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10949]; `tensor/DDL_lfc|DDL_z.npy` [10949]; `embed/gene_vectors.npy` [10949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10949 or target_col == 10949). Every well: [[KCTD12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
