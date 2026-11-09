---
symbol: "RETREG2"
type: "gene"
col: 6896
ensembl_id: "ENSG00000144567"
name: "reticulophagy regulator family member 2"
location: "2q35"
module: 76
arm: "+"
pooled_cpm: 28.23
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# RETREG2

*reticulophagy regulator family member 2* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.12× (z +5.8, q 3e-06, up in 5 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.50× (z +4.3, q 0.004, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.513× (z -14.3, q 9e-44, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHDC3]] (+0.68, fdr 7e-06), [[MOSPD3]] (+0.65, fdr 7e-06), [[WASF2]] (+0.64, fdr 1e-05); moves opposite to [[POGLUT1]] (-0.57, fdr 1e-05), [[GCFC2]] (-0.57, fdr 2e-05), [[ABCE1]] (-0.56, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIK3CB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.8 | 3e-06 | 5/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +5.0 | 2e-04 | 25/45 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 0.004 | 27/47 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.038 | 17/48 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.071 | 16/48 (J82, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.18 | 15/48 (J82, A498, …) | top dose only | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.18 | 15/47 (SHP-77, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | 1.46× | +3.0 | 0.18 | 8/47 (HOP62, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6896.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.513×** | -14.3 | 9e-44 | 43/47 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.414×** | -12.9 | 2e-35 | 43/48 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -10.5 | 1e-23 | 39/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -9.4 | 1e-18 | 36/48 (SNU-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -8.2 | 2e-14 | 32/47 (C32, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.610×** | -7.5 | 7e-12 | 36/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -7.4 | 1e-11 | 37/48 (AsPC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -6.1 | 6e-08 | 30/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -5.6 | 1e-06 | 32/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.684×** | -5.5 | 2e-06 | 26/47 (NCI-H23, SW 900, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.695×** | -5.5 | 2e-06 | 28/48 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.727×** | -4.6 | 2e-04 | 30/47 (A498, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.728×** | -4.6 | 2e-04 | 26/48 (RKO, SW48, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.576×** | -4.4 | 5e-04 | 20/34 (C32, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.583×** | -4.3 | 7e-04 | 26/47 (RPMI-7951, AsPC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.598×** | -4.1 | 0.002 | 24/48 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.765×** | -4.1 | 0.002 | 23/47 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -4.1 | 0.002 | 25/48 (SW1417, SHP-77, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.611×** | -3.9 | 0.003 | 21/47 (LOX-IMVI, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.801×** | -3.4 | 0.021 | 17/48 (C32, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 34.7 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.2) |
| [[A549 (line)]] | wt | 26.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -13.9) |
| [[SNU-1 (line)]] | wt | 33.4 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -13.2) |
| [[A-172 (line)]] | wt | 41.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 40.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -20.4) |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -18.2) |
| [[A-427 (line)]] | wt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.8) |
| [[HOP62 (line)]] | alt | 23.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -11.7) |
| [[HS-578T (line)]] | alt | 28.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 27.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 33.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.355× (z -9.0) |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.0) |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 33.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.173× (z -9.7) |
| [[HCT15 (line)]] | alt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.9) |
| [[LoVo (line)]] | wt | 18.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.253× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -18.1) |
| [[NCI-H2030 (line)]] | alt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.4) |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0818× (z -8.7) |
| [[SW480 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.7) |
| [[A498 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHDC3]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[WASF2]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[HSDL1]] | +0.62 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SPSB3]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TBC1D17]] | +0.62 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CALCOCO1]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TPRG1L]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[UBXN6]] | +0.61 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[HECTD3]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MEF2D]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[NTAN1]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT1]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GCFC2]] | -0.57 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ABCE1]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD18A]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.55 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ST7L]] | -0.54 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[CSTF3]] | -0.53 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[PRDM5]] | -0.53 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[SLC35F2]] | -0.52 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[SNX5]] | -0.52 | -0.42 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CB]] | B | PIK3CB activity lowers RETREG2's level | compounds that target PIK3CB: 2 of 3 raise it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.0, -37.7); signed map (-21.5, 8.9). **Vector** length 89.7, 20.6% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +0.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.6 | +5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | -0.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.3 | +2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | reticulophagy regulator family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,176,225-219,185,475 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3035, MAG-2; previously C2orf17, FAM134A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NC44](https://www.uniprot.org/uniprotkb/Q8NC44) (Reticulophagy regulator 2):

> Endoplasmic reticulum (ER)-anchored autophagy regulator which exists in an inactive state under basal conditions but is activated following cellular stress. When activated, induces ER fragmentation and mediates ER delivery into lysosomes through sequestration into autophagosomes via interaction with ATG8 family proteins. Required for collagen quality control in a LIR motif-independent manner (By similarity).

**Summary**, from NCBI Gene [79137](https://www.ncbi.nlm.nih.gov/gene/79137):

> Predicted to enable endoplasmic reticulum-autophagosome adaptor activity. Predicted to be involved in substrate localization to autophagosome. Predicted to act upstream of or within collagen catabolic process; endoplasmic reticulum organization; and reticulophagy. Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28450](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28450) · Entrez [79137](https://www.ncbi.nlm.nih.gov/gene/79137) · UniProt [Q8NC44](https://www.uniprot.org/uniprotkb/Q8NC44) · Ensembl [ENSG00000144567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144567)

## Data

Gene col 6896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6896); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6896]; `tensor/DDL_lfc|DDL_z.npy` [6896]; `embed/gene_vectors.npy` [6896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6896 or target_col == 6896). Every well: [[RETREG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RETREG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
