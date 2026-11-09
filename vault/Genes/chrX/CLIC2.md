---
symbol: "CLIC2"
type: "gene"
col: 7933
ensembl_id: "ENSG00000155962"
name: "CLIC family member 2"
location: "Xq28"
module: 10
arm: "+"
pooled_cpm: 3.89
n_lines_expressing: 36
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CLIC2

*CLIC family member 2* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.36× (z +10.5, q 4e-23, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.68× (z +8.9, q 1e-16, up in 14 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.512× (z -6.1, q 7e-07, down in 11 of 27 measured lines) ⚠ cell-cycle shift, explains ~29% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0677×; ⚠ cell-cycle shift, explains ~29% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0679×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNLS]] (+0.69, fdr 1e-05), [[SLCO2B1]] (+0.69, fdr 8e-06), [[CATSPERE]] (+0.67, fdr 2e-05); moves opposite to [[DHTKD1]] (-0.66, fdr 2e-05), [[POGLUT2]] (-0.62, fdr 8e-05), [[LCMT1]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPNMB]] → it (grade B ⚠); 2 go from it, the strongest it → [[HMOX1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +10.5 | 4e-23 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +9.2 | 7e-18 | 5/12 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.68×** | +8.9 | 1e-16 | 14/23 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +8.6 | 1e-15 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +7.8 | 6e-13 | 8/22 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +6.4 | 1e-08 | 8/30 (NCI-H2347, H4, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.0 | 5e-05 | 3/20 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.41×** | +4.4 | 8e-04 | 6/28 (PANC-1, C32, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +4.3 | 1e-03 | 9/30 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.8 | 0.010 | 4/16 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.48×** | +3.5 | 0.023 | 2/22 (NCI-H2347, SK-MEL-2) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.041 | 6/21 (NCI-H460, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.054 | 5/16 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.054 | 5/25 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.086 | 8/28 (A-172, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7933.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0677×; ⚠ cell-cycle shift, explains ~29% of this change); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0679×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.512×** | -6.1 | 7e-07 | 11/27 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.776× | -3.3 | 0.29 | 6/30 (SHP-77, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 0.719× | -3.0 | 0.38 | 12/31 (HEC-1-A, HOP62, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 49.2 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +15.5) | — |
| [[A-172 (line)]] | wt | 5.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +13.4) | — |
| [[HEC-1-A (line)]] | alt | 5.37 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0677× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0679× (z -9.3) |
| [[SW 900 (line)]] | alt | 13.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +13.1) | — |
| [[A-427 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.595 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNLS]] | +0.69 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SLCO2B1]] | +0.69 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[CATSPERE]] | +0.67 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[GNGT1]] | +0.67 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[LINC01933]] | +0.67 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[FMO4]] | +0.66 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[LINC01725]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CFAP70]] | +0.65 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CELF6]] | +0.65 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[TRIML2]] | +0.65 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FBXL19-AS1]] | +0.64 | +0.60 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHTKD1]] | -0.66 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[POGLUT2]] | -0.62 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[LCMT1]] | -0.61 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[SRGAP2D]] | -0.59 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.59 | -0.50 / -0.32 | both halves | 1e-04 |  |
| [[FBH1]] | -0.58 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[SOCS7]] | -0.58 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[MINK1]] | -0.58 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[GMCL1]] | -0.57 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[ODF2]] | -0.57 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MIGA2]] | -0.55 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPNMB]] | B | GPNMB activity raises CLIC2's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.15× lower at baseline in the lines without GPNMB | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[KATNAL2]] | B | KATNAL2 activity lowers CLIC2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.19× higher at baseline in the lines without KATNAL2 | 0.055 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMOX1]] | B | CLIC2 activity lowers HMOX1's level | lines that do not express CLIC2 (14) vs lines expressing it (36) | 2.51× higher at baseline in the lines without CLIC2 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526; maybe low, not absent |
| [[FBH1]] | B | CLIC2 activity lowers FBH1's level | lines that do not express CLIC2 (14) vs lines expressing it (36) | 1.14× higher at baseline in the lines without CLIC2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (28.5, 25.5); signed map (40.6, 20.1). **Vector** length 39.9, 6.02% of its response variance represented; |z| ≥ 3 in 651 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.1 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -1.5 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.7 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | CLIC family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:155,276,211-155,334,657 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XAP121, CLCNL2 |
| Gene groups (HGNC) | CLIC family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 6 pathways, smallest: Ion homeostasis; Stimuli-sensing channels; Cardiac conduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O15247](https://www.uniprot.org/uniprotkb/O15247) (Chloride intracellular channel protein 2):

> In the soluble state, catalyzes glutaredoxin-like thiol disulfide exchange reactions with reduced glutathione as electron donor. Displays weak glutathione peroxidase activity (Probable). Can insert into membranes and form chloride ion channels. Membrane insertion seems to be redox-regulated and may occur only under oxidizing conditions. Modulates the activity of RYR2 and inhibits calcium influx.

**Summary**, from NCBI Gene [1193](https://www.ncbi.nlm.nih.gov/gene/1193):

> This gene encodes a chloride intracellular channel protein. Chloride channels are a diverse group of proteins that regulate fundamental cellular processes including stabilization of cell membrane potential, transepithelial transport, maintenance of intracellular pH, and regulation of cell volume. This protein plays a role in inhibiting the function of ryanodine receptor 2. A mutation in this gene is the cause of an X-linked form of cognitive disability. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:2063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2063) · Entrez [1193](https://www.ncbi.nlm.nih.gov/gene/1193) · UniProt [O15247](https://www.uniprot.org/uniprotkb/O15247) · Ensembl [ENSG00000155962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155962)

## Data

Gene col 7933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7933); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7933]; `tensor/DDL_lfc|DDL_z.npy` [7933]; `embed/gene_vectors.npy` [7933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7933 or target_col == 7933). Every well: [[CLIC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
