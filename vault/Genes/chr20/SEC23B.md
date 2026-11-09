---
symbol: "SEC23B"
type: "gene"
col: 2113
ensembl_id: "ENSG00000101310"
name: "SEC23 homolog B, COPII component"
location: "20p11.23"
module: 49
arm: "+"
pooled_cpm: 70.52
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SEC23B

*SEC23 homolog B, COPII component* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +13.1, q 1e-36, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.763× (z -4.3, q 0.009, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.121×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0738×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAN2]] (+0.66, fdr 7e-06), [[GOLGA1]] (+0.65, fdr 1e-05), [[ARFIP2]] (+0.64, fdr 1e-05); moves opposite to [[HACD3]] (-0.60, fdr 1e-05), [[NCK2]] (-0.55, fdr 5e-05), [[IGF1R]] (-0.55, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ST6GAL1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PACS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +13.1 | 1e-36 | 44/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +10.9 | 3e-25 | 38/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.76×** | +8.6 | 1e-15 | 38/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.1 | 2e-07 | 33/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.4 | 0.001 | 28/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 0.001 | 29/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.002 | 27/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.008 | 22/48 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.012 | 23/49 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.019 | 18/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.023 | 20/48 (LoVo, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.033 | 17/48 (LOX-IMVI, LoVo, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.043 | 14/48 (MIA PaCa-2, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.045 | 15/48 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.048 | 22/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2113.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.121×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 1271 0.0738×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -4.3 | 0.009 | 25/48 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -3.8 | 0.049 | 23/48 (COLO 205, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.802× | -3.4 | 0.14 | 19/47 (NCI-H1573, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.785× | -3.2 | 0.18 | 20/49 (SW48, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 66.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +15.4) | — |
| [[A-427 (line)]] | wt | 39.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 141 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 64.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +17.3) | — |
| [[RKO (line)]] | wt | 79.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +13.6) | — |
| [[A549 (line)]] | wt | 85.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 56.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +17.2) | — |
| [[NCI-H2347 (line)]] | alt | 60.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.0) | — |
| [[SNU-1 (line)]] | wt | 75.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +9.2) | — |
| [[SW480 (line)]] | alt | 63.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.50× (z +11.0) | — |
| [[A-172 (line)]] | wt | 51.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.7) | — |
| [[C32 (line)]] | wt | 40.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 56.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.1) | — |
| [[CHP-212 (line)]] | wt | 61.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.121× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 56.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 74.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 48.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 46.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 87.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0738× (z -10.2) |
| [[A498 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 168 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 97.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAN2]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[GOLGA1]] | +0.65 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ARFIP2]] | +0.64 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[RUSF1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[YIPF6]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[SLC35B1]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[COPG1]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 | STRING 562 |
| [[COPE]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LYSMD3]] | +0.59 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[SLC15A2]] | +0.58 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[SLC33A1]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[XRRA1]] | +0.57 | +0.64 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD3]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[NCK2]] | -0.55 | -0.63 / -0.39 | both halves | 5e-05 |  |
| [[IGF1R]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PTK2]] | -0.55 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[TFDP2]] | -0.51 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[RNF130]] | -0.51 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[SRPK2]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CYTH3]] | -0.50 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[CDYL]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[EXOC6B]] | -0.48 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[RAP1GDS1]] | -0.48 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[KPNA3]] | -0.47 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST6GAL1]] | B | ST6GAL1 activity lowers SEC23B's level | lines that do not express ST6GAL1 (14) vs lines expressing it (36) | 1.21× higher at baseline in the lines without ST6GAL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PACS1]] | C | SEC23B's natural level weakens PACS1's drug response | SEC23B's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.67, reverse +0.05; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, -39.4); signed map (-55.7, 12.7). **Vector** length 113, 33.7% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +7.5 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.5 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +13.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.6 | -0.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +8.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.4 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.1 | +1.8 |
|  | [[EX229 (drug)]] 0.5 µM |  | +3.0 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.2 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SEC23 homolog B, COPII component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:18,507,520-18,561,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDA-II, CDAII, HEMPAS; previously CDAN2 |
| Gene groups (HGNC) | Coat protein complex II |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15437](https://www.uniprot.org/uniprotkb/Q15437) (Protein transport protein Sec23B):

> Component of the coat protein complex II (COPII) which promotes the formation of transport vesicles from the endoplasmic reticulum (ER). The coat has two main functions, the physical deformation of the endoplasmic reticulum membrane into vesicles and the selection of cargo molecules for their transport to the Golgi complex.

**Summary**, from NCBI Gene [10483](https://www.ncbi.nlm.nih.gov/gene/10483):

> The protein encoded by this gene is a member of the SEC23 subfamily of the SEC23/SEC24 family, which is involved in vesicle trafficking. The encoded protein has similarity to yeast Sec23p component of COPII. COPII is the coat protein complex responsible for vesicle budding from the ER. The function of this gene product has been implicated in cargo selection and concentration. Multiple alternatively spliced transcript variants have been identified in this gene. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:10702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10702) · Entrez [10483](https://www.ncbi.nlm.nih.gov/gene/10483) · UniProt [Q15437](https://www.uniprot.org/uniprotkb/Q15437) · Ensembl [ENSG00000101310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101310)

## Data

Gene col 2113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2113); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2113]; `tensor/DDL_lfc|DDL_z.npy` [2113]; `embed/gene_vectors.npy` [2113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2113 or target_col == 2113). Every well: [[SEC23B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC23B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
