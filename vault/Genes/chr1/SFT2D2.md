---
symbol: "SFT2D2"
type: "gene"
col: 13078
ensembl_id: "ENSG00000213064"
name: "SFT2 domain containing 2"
location: "1q24.2"
module: 25
arm: "+"
pooled_cpm: 60.18
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SFT2D2

*SFT2 domain containing 2* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +8.1, q 4e-13, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~19% of this change. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.40× (z +3.6, q 0.031, up in 11 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2347 2.10×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (RKO 1.91×; ⚠ cell-cycle shift, explains ~19% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.767× (z -7.2, q 4e-10, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.445×, SK-MEL-2 0.518×, Hs 766T 0.528×; ⚠ cell-cycle shift, explains ~4% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C32 0.389×, NCI-H2030 0.365×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0906×; ⚠ toxic); [[Nevirapine (drug)]] 0.05 µM in 1 line (SW48 0.289×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1A]] (+0.60, fdr 3e-05), [[ARPP19]] (+0.58, fdr 3e-05), [[RBBP9]] (+0.56, fdr 3e-05); moves opposite to [[RAB5A]] (-0.53, fdr 5e-05), [[HM13]] (-0.52, fdr 5e-05), [[CCDC107]] (-0.50, fdr 4e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GMFB]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13078.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H2347 2.10×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (RKO 1.91×; ⚠ cell-cycle shift, explains ~19% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.34×** | +8.1 | 4e-13 | 34/48 (RKO, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +6.2 | 1e-07 | 27/41 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.8 | 4e-04 | 25/48 (C-33 A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.22×** | +3.8 | 0.019 | 24/47 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.20× | +3.6 | 0.027 | 21/48 (NCI-H1792, J82, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +3.6 | 0.027 | 13/47 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.031 | 11/47 (C32, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.032 | 20/48 (NCI-H2347, KATO III, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.076 | 18/48 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.2 | 0.076 | 18/45 (C-33 A, HS-578T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.078 | 14/48 (CFPAC-1, Panc 03.27, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13078.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AsPC-1 0.445×, SK-MEL-2 0.518×, Hs 766T 0.528×; ⚠ cell-cycle shift, explains ~4% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (C32 0.389×, NCI-H2030 0.365×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 1 line (LOX-IMVI 0.0906×; ⚠ toxic); [[Nevirapine (drug)]] 0.05 µM in 1 line (SW48 0.289×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.767×** | -7.2 | 4e-10 | 35/48 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.762×** | -5.5 | 1e-05 | 25/48 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.849× | -4.5 | 0.001 | 21/49 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.833× | -3.7 | 0.030 | 19/48 (SK-MEL-2, C32, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 64.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.91× (z +8.5) ⚠ cell-cycle shift, explains ~19% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.288× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~2% of this change |
| [[SK-MEL-2 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[AsPC-1 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -11.4) ⚠ cell-cycle shift, explains ~4% of this change |
| [[Hs 766T (line)]] | wt | 84.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LOX-IMVI (line)]] | wt | 49.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0906× (z -13.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 50.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 89.6 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 58.6 | 0 | 1 | — | [[Nevirapine (drug)]] 0.05 µM 0.289× (z -8.7) |
| [[A-172 (line)]] | wt | 85.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ARPP19]] | +0.58 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[RBBP9]] | +0.56 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[FAM199X]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[MMGT1]] | +0.53 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[PABIR2]] | +0.53 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[NRAS]] | +0.52 | +0.26 / +0.63 | both halves | 4e-04 |  |
| [[ANKRD52]] | +0.52 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[PPP2R1B]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[GPD2]] | +0.51 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[VPS26A]] | +0.51 | +0.37 / +0.57 | both halves | 8e-05 |  |
| [[CAPN1]] | +0.51 | +0.37 / +0.59 | both halves | 9e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5A]] | -0.53 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[HM13]] | -0.52 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[CCDC107]] | -0.50 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[TMEM258]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PI4KA]] | -0.48 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PRPF38B]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MT1X]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[TFAP2E]] | -0.47 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ANGPTL4]] | -0.46 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[OSBP]] | -0.46 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[MIDN]] | -0.46 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[GCAT]] | -0.46 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GMFB]] | C | GMFB's natural level weakens SFT2D2's drug response | GMFB's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.14; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[HNRNPM]] | C | HNRNPM's natural level weakens SFT2D2's drug response | HNRNPM's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse -0.14; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.9, -20.1); signed map (-17.9, -38.2). **Vector** length 104, 24.4% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +8.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +6.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.4 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.6 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -3.2 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.2 | -3.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.1 | -2.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.0 | -0.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SFT2 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:168,225,938-168,253,021 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ512, dJ747L4.C1.2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O95562](https://www.uniprot.org/uniprotkb/O95562) (Vesicle transport protein SFT2B):

> May be involved in fusion of retrograde transport vesicles derived from an endocytic compartment with the Golgi complex.

**Summary**, from NCBI Gene [375035](https://www.ncbi.nlm.nih.gov/gene/375035):

> Predicted to be involved in protein transport and vesicle-mediated transport. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25140) · Entrez [375035](https://www.ncbi.nlm.nih.gov/gene/375035) · UniProt [O95562](https://www.uniprot.org/uniprotkb/O95562) · Ensembl [ENSG00000213064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213064)

## Data

Gene col 13078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13078); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13078]; `tensor/DDL_lfc|DDL_z.npy` [13078]; `embed/gene_vectors.npy` [13078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13078 or target_col == 13078). Every well: [[SFT2D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFT2D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
