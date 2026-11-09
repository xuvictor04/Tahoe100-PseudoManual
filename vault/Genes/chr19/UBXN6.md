---
symbol: "UBXN6"
type: "gene"
col: 9515
ensembl_id: "ENSG00000167671"
name: "UBX domain protein 6"
location: "19p13"
module: 76
arm: "+"
pooled_cpm: 18.21
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# UBXN6

*UBX domain protein 6* — 19p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.76× (z +8.3, q 4e-14, up in 30 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.35× (z +4.5, q 8e-04, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 4.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.18×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.595× (z -7.7, q 9e-12, down in 35 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.781× (z -5.2, q 3e-05, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALCOCO1]] (+0.67, fdr 7e-06), [[IKZF5]] (+0.66, fdr 8e-06), [[ATF6B]] (+0.65, fdr 7e-06); moves opposite to [[NOC3L]] (-0.61, fdr 7e-06), [[NME1]] (-0.56, fdr 1e-05), [[PA2G4]] (-0.55, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9515.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H23 4.97×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (HEC-1-A 3.18×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.3 | 4e-14 | 30/41 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +6.0 | 6e-07 | 30/45 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +5.7 | 2e-06 | 22/37 (NCI-H1573, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.6 | 4e-06 | 19/32 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.5 | 8e-04 | 19/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.034 | 14/47 (NCI-H2030, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.4 | 0.056 | 12/47 (HOP62, PANC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.50× | +3.2 | 0.11 | 6/44 (LS 180, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.23× | +3.1 | 0.12 | 12/46 (A-172, SHP-77, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -7.7 | 9e-12 | 35/48 (HT-29, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.690×** | -5.5 | 1e-05 | 29/48 (hTERT-HPNE, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.702×** | -5.2 | 3e-05 | 23/48 (NCI-H1573, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -5.2 | 3e-05 | 30/48 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.728×** | -4.7 | 3e-04 | 23/48 (hTERT-HPNE, SW 900, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.730×** | -4.6 | 3e-04 | 20/48 (hTERT-HPNE, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.830×** | -3.9 | 0.008 | 22/47 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.014 | 21/46 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.783×** | -3.5 | 0.032 | 18/46 (H4, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.090 | 15/47 (hTERT-HPNE, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.668×** | -3.1 | 0.096 | 11/46 (A498, PANC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | 0.674× | -3.0 | 0.11 | 12/45 (MIA PaCa-2, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.815× | -3.0 | 0.11 | 10/47 (SW 900, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0753× (z -12.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 30.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +13.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCOCO1]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[IKZF5]] | +0.66 | +0.57 / +0.67 | both halves | 8e-06 |  |
| [[ATF6B]] | +0.65 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[FOXO4]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[KLHL24]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[CTDSP2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[YPEL3]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PTOV1]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[WBP1]] | +0.62 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[CCDC28A]] | +0.61 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[ATG14]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOC3L]] | -0.61 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[NME1]] | -0.56 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PA2G4]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[PDSS1]] | -0.51 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UBXN6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UBXN6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.4, -46.7); signed map (-17.0, 8.8). **Vector** length 63.9, 10.7% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.2 | +4.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | UBX domain protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13 — chr19:4,444,999-4,457,794 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UBXDC2; previously UBXD1 |
| Gene groups (HGNC) | UBX domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZV1](https://www.uniprot.org/uniprotkb/Q9BZV1) (UBX domain-containing protein 6):

> May negatively regulate the ATPase activity of VCP, an ATP-driven segregase that associates with different cofactors to control a wide variety of cellular processes. As a cofactor of VCP, it may play a role in the transport of CAV1 to lysosomes for degradation. It may also play a role in endoplasmic reticulum-associated degradation (ERAD) of misfolded proteins. Together with VCP and other cofactors, it may play a role in macroautophagy, regulating for instance the clearance of damaged lysosomes.

**Summary**, from NCBI Gene [80700](https://www.ncbi.nlm.nih.gov/gene/80700):

> Enables ATPase binding activity. Involved in several processes, including ERAD pathway; endosome to lysosome transport via multivesicular body sorting pathway; and protein unfolding. Located in bounding membrane of organelle and cytosol. Part of endosome and protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14928) · Entrez [80700](https://www.ncbi.nlm.nih.gov/gene/80700) · UniProt [Q9BZV1](https://www.uniprot.org/uniprotkb/Q9BZV1) · Ensembl [ENSG00000167671](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167671)

## Data

Gene col 9515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9515); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9515]; `tensor/DDL_lfc|DDL_z.npy` [9515]; `embed/gene_vectors.npy` [9515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9515 or target_col == 9515). Every well: [[UBXN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBXN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
