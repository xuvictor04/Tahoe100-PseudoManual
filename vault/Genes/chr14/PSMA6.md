---
symbol: "PSMA6"
type: "gene"
col: 2039
ensembl_id: "ENSG00000100902"
name: "proteasome 20S subunit alpha 6"
location: "14q13.2"
module: 72
arm: "+"
pooled_cpm: 87.66
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMA6

*proteasome 20S subunit alpha 6* — 14q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.29× (z +12.8, q 9e-35, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2347 0.523×, RKO 0.435×, H4 0.417×, MIA PaCa-2 0.499×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.263×; ⚠ toxic; cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMC6]] (+0.71, fdr 7e-06), [[PSMA2]] (+0.71, fdr 7e-06), [[TENT2]] (+0.69, fdr 7e-06); moves opposite to [[IER2]] (-0.55, fdr 2e-05), [[SLC4A7]] (-0.55, fdr 1e-05), [[TNFRSF12A]] (-0.55, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM241A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.29×** | +12.8 | 9e-35 | 47/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.15×** | +11.8 | 8e-30 | 46/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.62×** | +11.4 | 1e-27 | 47/49 (RPMI-7951, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.07×** | +10.6 | 4e-24 | 47/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +6.2 | 6e-08 | 37/48 (LS 180, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.3 | 1e-05 | 34/48 (SW480, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.40×** | +5.1 | 3e-05 | 30/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.0 | 0.005 | 21/38 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.29×** | +4.0 | 0.005 | 28/48 (PANC-1, LS 180, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.013 | 30/49 (LOX-IMVI, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.4 | 0.035 | 25/45 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.23×** | +3.2 | 0.057 | 24/48 (LS 180, SW480, …) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2039.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H2347 0.523×, RKO 0.435×, H4 0.417×, MIA PaCa-2 0.499×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.263×; ⚠ toxic; cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.345×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.3 | 0.21 | 23/48 (NCI-H2347, RKO, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.805× | -3.3 | 0.21 | 23/48 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.859× | -3.3 | 0.21 | 17/48 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -3.0 | 0.34 | 15/48 (RPMI-7951, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 98.7 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.96× (z +11.2) | — |
| [[SW480 (line)]] | alt | 64.4 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.69× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 64.5 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.56× (z +10.4) | — |
| [[KATO III (line)]] | alt | 63.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.10× (z +11.3) | — |
| [[LoVo (line)]] | wt | 95.0 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.89× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 102 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.53× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 61.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.11× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 42.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.59× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 49.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 90.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.04× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 79.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.63× (z +11.4) | — |
| [[A-427 (line)]] | wt | 85.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +9.8) | — |
| [[C32 (line)]] | wt | 72.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.95× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 141 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 62.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.71× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 93.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.92× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 108 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.36× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 65.2 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.76× (z +9.3) | — |
| [[RKO (line)]] | wt | 64.9 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[RPMI-7951 (line)]] | alt | 89.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 16.0× (z +11.7) | — |
| [[SW48 (line)]] | wt | 102 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.24× (z +9.3) | — |
| [[H4 (line)]] | wt | 88.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 73.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +8.9) | — |
| [[J82 (line)]] | alt | 74.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.21× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 190 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 89.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 77.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 69.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC6]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMA2]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[TENT2]] | +0.69 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PSMA3]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMB2]] | +0.67 | +0.76 / +0.60 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CLASP1]] | +0.66 | +0.72 / +0.52 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[PSMA1]] | +0.65 | +0.71 / +0.59 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[TXNL1]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 | STRING 591 |
| [[PSMC2]] | +0.64 | +0.67 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[ZNF148]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[RTCA]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[JKAMP]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SLC4A7]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.55 | -0.61 / -0.44 | both halves | 3e-05 | pathway: TNFR2 non-canonical NF-kB pathway; STRING 401 |
| [[SEPTIN10]] | -0.52 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[THOC6]] | -0.52 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MYL12A]] | -0.51 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[COTL1]] | -0.50 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[EGR1]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[CEP135]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 | pathway: G2/M Transition |
| [[PPP3CB]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 | pathway: Beta-catenin independent WNT signaling |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM241A]] | B | FAM241A activity lowers PSMA6's level | lines that do not express FAM241A (7) vs lines expressing it (43) | 1.30× higher at baseline in the lines without FAM241A | 0.012 | ⚠ within organs, on part of the lines; also absent: TES, TRIB1, LRRCC1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, -10.2); signed map (-26.6, -23.8). **Vector** length 114, 36.8% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.2 | +12.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.1 | +11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.8 | +10.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.3 | +1.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.4 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +1.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit alpha 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q13.2 — chr14:35,278,633-35,317,493 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IOTA, PROS27, p27K, MGC22756, MGC2333, MGC23846 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 170 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P60900](https://www.uniprot.org/uniprotkb/P60900) (Proteasome subunit alpha type-6):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5687](https://www.ncbi.nlm.nih.gov/gene/5687):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9535) · Entrez [5687](https://www.ncbi.nlm.nih.gov/gene/5687) · UniProt [P60900](https://www.uniprot.org/uniprotkb/P60900) · Ensembl [ENSG00000100902](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100902)

## Data

Gene col 2039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2039); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2039]; `tensor/DDL_lfc|DDL_z.npy` [2039]; `embed/gene_vectors.npy` [2039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2039 or target_col == 2039). Every well: [[PSMA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
