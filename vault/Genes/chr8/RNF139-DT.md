---
symbol: "RNF139-DT"
type: "gene"
col: 14421
ensembl_id: "ENSG00000245149"
name: "RNF139 divergent transcript"
location: "8q24.13"
module: 179
arm: "+"
pooled_cpm: 6.74
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# RNF139-DT

*RNF139 divergent transcript* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.42× (z +13.7, q 5e-40, up in 37 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 3.30×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 7.09×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.264× (z -14.3, q 2e-43, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP4-1]] (+0.71, fdr 7e-06), [[METTL21EP-1]] (+0.70, fdr 7e-06), [[ZFC3H1]] (+0.67, fdr 7e-06); moves opposite to [[TIGD2]] (-0.64, fdr 7e-06), [[PPP6R3]] (-0.58, fdr 2e-04), [[STX17]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF141]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14421.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H2347 3.30×; ⚠ cell-cycle shift, explains ~51% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 7.09×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +13.7 | 5e-40 | 37/41 (LOX-IMVI, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.52×** | +6.5 | 2e-08 | 22/47 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.9 | 6e-07 | 13/29 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +5.2 | 3e-05 | 6/19 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.52×** | +4.7 | 3e-04 | 21/44 (SW480, HT-29, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.34× | +3.2 | 0.11 | 5/48 (A498, HS-578T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.72× | +3.2 | 0.11 | 1/12 (A498) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 1.33× | +3.2 | 0.11 | 8/45 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14421.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.264×** | -14.3 | 2e-43 | 34/43 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.343×** | -11.9 | 3e-30 | 35/45 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.594×** | -5.8 | 1e-06 | 21/43 (HS-578T, COLO 205, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.608×** | -5.5 | 4e-06 | 22/48 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.609×** | -5.3 | 1e-05 | 20/43 (HS-578T, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.628×** | -5.2 | 2e-05 | 18/44 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.649×** | -4.6 | 3e-04 | 17/33 (AsPC-1, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.758×** | -4.2 | 0.002 | 18/38 (AsPC-1, SW 900, …) | all doses, flat | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.705×** | -3.9 | 0.006 | 13/43 (HCT15, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.731×** | -3.5 | 0.028 | 14/44 (AsPC-1, hTERT-HPNE, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.744×** | -3.3 | 0.052 | 15/38 (HS-578T, AsPC-1, …) | all doses, flat |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **0.735×** | -3.2 | 0.056 | 7/45 (Hs 766T, SHP-77, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.735×** | -3.2 | 0.066 | 15/41 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Meloxicam (drug)]] 0.05 µM |  | **0.757×** | -3.1 | 0.074 | 4/44 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.758×** | -3.1 | 0.074 | 11/46 (COLO 205, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.764×** | -3.0 | 0.081 | 10/45 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.764×** | -3.0 | 0.081 | 6/46 (CHP-212, SW480, …) | inconsistent across doses |  |
| [[LJI308 (drug)]] 0.05 µM |  | **0.757×** | -2.9 | 0.097 | 7/44 (SNU-1, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14421. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 21.4 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.139× (z -11.3) |
| [[A498 (line)]] | wt | 15.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.162× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 10.0 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.149× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 10.8 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 3.30× (z +9.6) ⚠ cell-cycle shift, explains ~51% of this change | [[Harringtonine (drug)]] 0.5 µM 0.200× (z -9.3) |
| [[A-172 (line)]] | wt | 5.42 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0376× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 5.25 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0487× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 6.93 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0639× (z -11.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 3.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 4.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[Panc 03.27 (line)]] | alt | 4.75 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0473× (z -9.2) |
| [[SW480 (line)]] | alt | 4.70 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.101× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14421), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4-1]] | +0.71 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[METTL21EP-1]] | +0.70 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[ZFC3H1]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[HYPK]] | +0.66 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.66 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[SGSM3]] | +0.66 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[GET1-SH3BGR]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[NDEL1]] | +0.65 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CAPN10-DT]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 | same gene group |
| [[TMED7-TICAM2]] | +0.65 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[GOLT1B]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CDC26]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGD2]] | -0.64 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[PPP6R3]] | -0.58 | -0.30 / -0.65 | both halves | 2e-04 |  |
| [[STX17]] | -0.55 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[VPS13C]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ROCK2]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[MYCBP2]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CMTR2]] | -0.53 | -0.51 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF141]] | B | ZNF141 activity raises RNF139-DT's level | lines that do not express ZNF141 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without ZNF141 | 0.087 | ⚠ within organs, on part of the lines; also absent: SLC1A3 |
| [[MICE]] | B | MICE activity raises RNF139-DT's level | lines that do not express MICE (14) vs lines expressing it (36) | 1.19× lower at baseline in the lines without MICE | 0.097 | ⚠ within organs, on part of the lines; also absent: TRIM2, ACSL5, TNFRSF14-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (17.7, -29.0); signed map (-46.4, 10.5). **Vector** length 88.7, 17.6% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +13.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.6 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +5.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +0.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.5 | +2.0 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | -0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -14.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -11.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RNF139 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.13 — chr8:124,462,485-124,474,582 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously RNF139-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48940) · Entrez [101927612](https://www.ncbi.nlm.nih.gov/gene/101927612) · Ensembl [ENSG00000245149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245149)

## Data

Gene col 14421: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14421); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14421, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14421]; `tensor/DDL_lfc|DDL_z.npy` [14421]; `embed/gene_vectors.npy` [14421]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14421 or target_col == 14421). Every well: [[RNF139-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF139-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
