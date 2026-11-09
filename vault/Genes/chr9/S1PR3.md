---
symbol: "S1PR3"
type: "gene"
col: 13127
ensembl_id: "ENSG00000213694"
name: "sphingosine-1-phosphate receptor 3"
location: "9q22.1"
module: 120
arm: "+"
pooled_cpm: 4.8
n_lines_expressing: 29
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 5
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# S1PR3

*sphingosine-1-phosphate receptor 3* — 9q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.21× (z +11.1, q 5e-26, up in 16 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PALM2AKAP2]] (+0.51, fdr 5e-05), [[FBN2]] (+0.50, fdr 1e-05), [[SNAI2]] (+0.50, fdr 4e-05); moves opposite to [[PPOX]] (-0.49, fdr 3e-05), [[NDUFAF7]] (-0.48, fdr 2e-05), [[ZFP14]] (-0.46, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IL7R]] → it (grade C ⚠); 5 go from it, the strongest it → [[SVEP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.21×** | +11.1 | 5e-26 | 16/22 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.98×** | +10.8 | 6e-25 | 23/27 (HS-578T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.84×** | +10.4 | 8e-23 | 16/23 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.80×** | +10.2 | 3e-22 | 23/27 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.49×** | +9.1 | 2e-17 | 16/24 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.48×** | +9.0 | 2e-17 | 21/27 (PANC-1, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +8.2 | 1e-14 | 16/27 (J82, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +7.8 | 4e-13 | 16/24 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.96×** | +6.7 | 1e-09 | 16/26 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +5.9 | 2e-07 | 14/27 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.80×** | +5.6 | 9e-07 | 6/14 (A-172, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.76×** | +5.6 | 1e-06 | 3/15 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.70×** | +5.1 | 2e-05 | 5/17 (HOP62, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.59×** | +4.6 | 2e-04 | 8/27 (A-172, HS-578T, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.57×** | +4.5 | 3e-04 | 9/26 (A-172, HS-578T, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.002 | 10/27 (A549, HS-578T, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.0 | 0.002 | 8/27 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.004 | 8/25 (A549, H4, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.004 | 10/26 (A549, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.012 | 5/27 (A549, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +3.2 | 0.040 | 2/26 (PANC-1, HS-578T) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.042 | 5/26 (A-427, A549, …) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +2.9 | 0.088 | 3/16 (RPMI-7951, BT-474, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -3.5 | 0.23 | 9/27 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.532× | -3.3 | 0.23 | 8/20 (A-427, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Oxaprozin (drug)]] 0.05 µM |  | 0.722× | -3.2 | 0.23 | 6/25 (HS-578T, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +8.8) | — |
| [[A498 (line)]] | wt | 31.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +10.4) | — |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.336 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.282 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALM2AKAP2]] | +0.51 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[FBN2]] | +0.50 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SNAI2]] | +0.50 | +0.43 / +0.57 | both halves | 4e-05 |  |
| [[CACNA1C]] | +0.50 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CDC42EP3]] | +0.49 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[VGLL3]] | +0.48 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[SVEP1]] | +0.47 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[STARD13]] | +0.47 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[TIGD2]] | +0.47 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[DNAJB5]] | +0.47 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[NHSL2]] | +0.47 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PTX3]] | +0.47 | +0.53 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPOX]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[NDUFAF7]] | -0.48 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ZFP14]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[GNRH1]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 | pathway: Class A/1 (Rhodopsin-like receptors) |
| [[C20orf96]] | -0.45 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[KCTD7]] | -0.44 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[DZANK1]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[SARNP]] | -0.44 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[SCAI]] | -0.44 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[RELCH]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[FAM174A]] | -0.43 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[MFSD8]] | -0.42 | -0.34 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL7R]] | C | IL7R activity raises S1PR3's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.90× lower at baseline in the lines without IL7R | 0.012 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[NHSL2]] | C | NHSL2 activity raises S1PR3's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 3.50× lower at baseline in the lines without NHSL2 | 0.014 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent; co-absent with the target |
| [[PTX3]] | C | PTX3 activity raises S1PR3's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 3.29× lower at baseline in the lines without PTX3 | 0.057 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1; co-absent with the target |
| [[LINC02930]] | C | LINC02930 activity raises S1PR3's level | lines that do not express LINC02930 (33) vs lines expressing it (17) | 2.38× lower at baseline in the lines without LINC02930 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000232053, GYPC, PLPP4; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SVEP1]] | B | S1PR3 activity raises SVEP1's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without S1PR3 | 0.059 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1 |
| [[STARD13]] | B | S1PR3 activity raises STARD13's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without S1PR3 | 0.088 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1 |
| [[NKX3-1]] | C | S1PR3 activity raises NKX3-1's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 2.98× lower at baseline in the lines without S1PR3 | 0.012 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1; co-absent with the target |
| [[NHSL2]] | C | S1PR3 activity raises NHSL2's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 2.72× lower at baseline in the lines without S1PR3 | 0.060 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1; co-absent with the target |
| [[PTX3]] | C | S1PR3 activity raises PTX3's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 4.61× lower at baseline in the lines without S1PR3 | 0.088 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.443). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, 16.6); signed map (20.0, 36.2). **Vector** length 53.6, 10.4% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.0 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.4 | +7.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +4.0 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[NG25 (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | sphingosine-1-phosphate receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.1 — chr9:88,990,863-89,005,155 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EDG-3, FLJ37523, bA791O21.3; previously EDG3, C9orf47, C9orf108 |
| Gene groups (HGNC) | Sphingosine 1-phosphate receptors |
| Reactome | 9 pathways, smallest: Lysosphingolipid and LPA receptors; Extra-nuclear estrogen signaling; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99500](https://www.uniprot.org/uniprotkb/Q99500) (Sphingosine 1-phosphate receptor 3):

> Receptor for the lysosphingolipid sphingosine 1-phosphate (S1P). S1P is a bioactive lysophospholipid that elicits diverse physiological effect on most types of cells and tissues. When expressed in rat HTC4 hepatoma cells, is capable of mediating S1P-induced cell proliferation and suppression of apoptosis.

**Summary**, from NCBI Gene [1903](https://www.ncbi.nlm.nih.gov/gene/1903):

> This gene encodes a member of the EDG family of receptors, which are G protein-coupled receptors. This protein has been identified as a functional receptor for sphingosine 1-phosphate and likely contributes to the regulation of angiogenesis and vascular endothelial cell function. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3167) · Entrez [1903](https://www.ncbi.nlm.nih.gov/gene/1903) · UniProt [Q99500](https://www.uniprot.org/uniprotkb/Q99500) · Ensembl [ENSG00000213694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213694)

## Data

Gene col 13127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13127); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13127]; `tensor/DDL_lfc|DDL_z.npy` [13127]; `embed/gene_vectors.npy` [13127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13127 or target_col == 13127). Every well: [[S1PR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/S1PR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
