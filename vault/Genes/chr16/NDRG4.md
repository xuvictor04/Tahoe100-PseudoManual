---
symbol: "NDRG4"
type: "gene"
col: 2305
ensembl_id: "ENSG00000103034"
name: "NDRG family member 4"
location: "16q21"
module: 61
arm: "+"
pooled_cpm: 4.21
n_lines_expressing: 40
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# NDRG4

*NDRG family member 4* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.59× (z +15.5, q 0e+00, up in 28 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 0.106×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (A549 0.0558×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.214×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (PANC-1 0.0726×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENTHD1]] (+0.69, fdr 7e-06), [[SLC35F1]] (+0.68, fdr 7e-06), [[TUBB2B]] (+0.67, fdr 7e-06); moves opposite to [[POLE3]] (-0.50, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SUSD4]] → it (grade B ⚠); 4 go from it, the strongest it → [[UAP1L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.59×** | +15.5 | 0e+00 | 28/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.47×** | +15.3 | 0e+00 | 25/34 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.86×** | +15.1 | 0e+00 | 30/35 (SW1417, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.78×** | +14.7 | 0e+00 | 21/27 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.80×** | +13.1 | 5e-37 | 3/6 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.69×** | +9.3 | 1e-18 | 3/8 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.48×** | +9.3 | 2e-18 | 24/34 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +9.0 | 1e-17 | 7/16 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +8.6 | 7e-16 | 20/34 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.15×** | +7.8 | 3e-13 | 21/36 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +7.1 | 6e-11 | 10/29 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.99×** | +6.7 | 9e-10 | 12/32 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +6.5 | 4e-09 | 13/29 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +5.7 | 6e-07 | 15/32 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.8 | 5e-05 | 6/24 (SNU-423, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 1e-04 | 12/33 (CHP-212, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +4.6 | 1e-04 | 11/35 (NCI-H1573, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +4.6 | 2e-04 | 8/26 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +4.5 | 3e-04 | 7/29 (SNU-423, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2305.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SNU-423 0.106×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (A549 0.0558×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SNU-423 0.214×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (PANC-1 0.0726×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.05 µM |  | 0.703× | -3.6 | 0.17 | 5/33 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Fingolimod (hydrochloride) (drug)]] 0.5 µM |  | 0.732× | -3.2 | 0.39 | 4/34 (HepG2/C3A, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 33.0 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -9.2) |
| [[SW480 (line)]] | alt | 2.82 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.8× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 1.60 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 12.9× (z +8.6) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0726× (z -8.9) |
| [[A-172 (line)]] | wt | 5.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +10.0) | — |
| [[A549 (line)]] | wt | 5.62 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0558× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 3.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 2.13 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.5× (z +9.0) | — |
| [[A-427 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.953 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.843 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTHD1]] | +0.69 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SLC35F1]] | +0.68 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[TUBB2B]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[XKR4]] | +0.65 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[RPLP0P2]] | +0.64 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MIR325HG]] | +0.61 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[LINC02511]] | +0.60 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[SORCS1]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[TPPP]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLE3]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUSD4]] | B | SUSD4 activity raises NDRG4's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without SUSD4 | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UAP1L1]] | B | NDRG4 activity raises UAP1L1's level | lines that do not express NDRG4 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without NDRG4 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, SMARCA1, ZNF606; maybe low, not absent |
| [[GPR158]] | B | NDRG4 activity raises GPR158's level | lines that do not express NDRG4 (10) vs lines expressing it (40) | 1.87× lower at baseline in the lines without NDRG4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, SMARCA1, ZNF606; maybe low, not absent |
| [[TNFSF9]] | B | NDRG4 activity lowers TNFSF9's level | lines that do not express NDRG4 (10) vs lines expressing it (40) | 1.83× higher at baseline in the lines without NDRG4 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, SMARCA1, ZNF606; maybe low, not absent |
| [[PAK1]] | B | NDRG4 activity lowers PAK1's level | lines that do not express NDRG4 (10) vs lines expressing it (40) | 1.58× higher at baseline in the lines without NDRG4 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, SMARCA1, ZNF606; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.3, -0.0); signed map (34.8, 21.2). **Vector** length 60.6, 10.4% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +15.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +14.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.3 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | NDRG family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,462,846-58,513,628 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1180, SMAP-8 |
| Gene groups (HGNC) | NDRG family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULP0](https://www.uniprot.org/uniprotkb/Q9ULP0) (Protein NDRG4):

> Contributes to the maintenance of intracerebral BDNF levels within the normal range, which is necessary for the preservation of spatial learning and the resistance to neuronal cell death caused by ischemic stress (By similarity). May enhance growth factor-induced ERK1 and ERK2 phosphorylation, including that induced by PDGF and FGF. May attenuate NGF-promoted ELK1 phosphorylation in a microtubule-dependent manner.

**Summary**, from NCBI Gene [65009](https://www.ncbi.nlm.nih.gov/gene/65009):

> This gene is a member of the N-myc downregulated gene family which belongs to the alpha/beta hydrolase superfamily. The protein encoded by this gene is a cytoplasmic protein that is required for cell cycle progression and survival in primary astrocytes and may be involved in the regulation of mitogenic signalling in vascular smooth muscles cells. Alternative splicing results in multiple transcripts encoding different isoforms.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:14466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14466) · Entrez [65009](https://www.ncbi.nlm.nih.gov/gene/65009) · UniProt [Q9ULP0](https://www.uniprot.org/uniprotkb/Q9ULP0) · Ensembl [ENSG00000103034](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103034)

## Data

Gene col 2305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2305); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2305]; `tensor/DDL_lfc|DDL_z.npy` [2305]; `embed/gene_vectors.npy` [2305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2305 or target_col == 2305). Every well: [[NDRG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDRG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
