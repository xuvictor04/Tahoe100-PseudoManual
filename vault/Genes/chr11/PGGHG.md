---
symbol: "PGGHG"
type: "gene"
col: 6596
ensembl_id: "ENSG00000142102"
name: "protein-glucosylgalactosylhydroxylysine glucosidase"
location: "11p15.5"
module: 2
arm: "+"
pooled_cpm: 10.47
n_lines_expressing: 46
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PGGHG

*protein-glucosylgalactosylhydroxylysine glucosidase* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +7.2, q 4e-10, up in 13 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bosentan (hydrate) (drug)]] 5 µM: 1.45× (z +3.3, q 0.089, up in 11 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (HT-29 8.42×, COLO 205 8.47×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (HT-29 4.52×, NCI-H2347 3.86×; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 3.57×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.417× (z -11.3, q 8e-27, down in 32 of 38 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.356× (z -9.4, q 1e-18, down in 35 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK12]] (+0.71, fdr 7e-06), [[TMEM259]] (+0.69, fdr 7e-06), [[ENGASE]] (+0.64, fdr 1e-05); moves opposite to [[INIP]] (-0.46, fdr 4e-05), [[IGIP]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[CPNE2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (HT-29 8.42×, COLO 205 8.47×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (HT-29 4.52×, NCI-H2347 3.86×; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 3.57×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.2 | 4e-10 | 13/28 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +7.1 | 4e-10 | 10/15 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.0 | 9e-05 | 11/23 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +3.7 | 0.030 | 10/21 (A-427, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.49×** | +3.5 | 0.055 | 11/43 (MIA PaCa-2, A498, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.089 | 11/38 (Panc 03.27, HT-29, …) | top dose only | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.13 | 12/40 (A-427, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.61× | +3.1 | 0.13 | 11/37 (SW48, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.417×** | -11.3 | 8e-27 | 32/38 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.356×** | -9.4 | 1e-18 | 35/40 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.358×** | -9.0 | 3e-17 | 32/42 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.419×** | -7.9 | 3e-13 | 36/43 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.469×** | -6.9 | 5e-10 | 31/42 (SK-MEL-2, A-427, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.525×** | -5.9 | 4e-07 | 25/42 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -5.8 | 5e-07 | 26/40 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.320×** | -5.5 | 4e-06 | 24/39 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.562×** | -5.3 | 9e-06 | 25/43 (A-427, NCI-H23, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.353×** | -5.0 | 4e-05 | 26/41 (PANC-1, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.609×** | -4.5 | 3e-04 | 19/43 (HT-29, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.593×** | -4.5 | 3e-04 | 17/40 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.624×** | -4.3 | 7e-04 | 18/38 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.635×** | -4.0 | 0.003 | 15/37 (H4, A-427, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.753×** | -3.7 | 0.010 | 15/42 (BT-474, COLO 205, …) | rises with dose | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.765×** | -3.4 | 0.020 | 13/41 (RKO, KATO III, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.500×** | -3.3 | 0.030 | 15/36 (NCI-H1792, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.720×** | -3.0 | 0.078 | 16/42 (A549, BT-474, …) | top dose only | position effect removed |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.724×** | -2.9 | 0.087 | 7/43 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 22.5 | 2 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.42× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -8.5) |
| [[A-427 (line)]] | wt | 61.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.57× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0572× (z -20.5) |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 3 | — | [[Apalutamide (drug)]] 0.05 µM 0.0635× (z -9.1) |
| [[COLO 205 (line)]] | alt | 23.4 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 8.47× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -9.8) |
| [[PANC-1 (line)]] | alt | 22.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -10.5) |
| [[A549 (line)]] | wt | 11.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -8.5) |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0524× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[J82 (line)]] | alt | 8.63 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0790× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 8.64 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 6.03 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.0572× (z -10.3) |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 2 | — | [[Saquinavir (drug)]] 0.05 µM 0.0711× (z -10.4) |
| [[SW1417 (line)]] | alt | 5.17 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0610× (z -9.7) |
| [[C32 (line)]] | wt | 5.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0503× (z -10.8) |
| [[HOP62 (line)]] | alt | 4.43 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.0607× (z -9.9) |
| [[Hs 766T (line)]] | wt | 7.37 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.119× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 8.97 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0897× (z -11.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H2347 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.86× (z +8.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 5.76 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0436× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 5.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -9.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK12]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TMEM259]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ENGASE]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 | same gene group |
| [[NRBP2]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[B4GALNT4]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 | STRING 707 |
| [[MED16]] | +0.61 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[LENG8]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GLI4]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[EME2]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[PLA2G4B]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[OPLAH]] ⚠ | +0.59 | +0.55 / +0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[UCKL1]] | +0.58 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[MAPK11]] | +0.58 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INIP]] | -0.46 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[IGIP]] | -0.45 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPNE2]] | C | PGGHG activity raises CPNE2's level | lines that do not express PGGHG (4) vs lines expressing it (46) | 2.52× lower at baseline in the lines without PGGHG | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GARIN1B; maybe low, not absent |
| [[ACADVL]] | C | PGGHG activity lowers ACADVL's level | lines that do not express PGGHG (4) vs lines expressing it (46) | 1.68× higher at baseline in the lines without PGGHG | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GARIN1B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.5, -23.1); signed map (-27.8, 0.2). **Vector** length 76.6, 14.8% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.7 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +5.0 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +3.0 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.0 | -11.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | protein-glucosylgalactosylhydroxylysine glucosidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:289,126-296,107 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22635; previously ATHL1 |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q32M88](https://www.uniprot.org/uniprotkb/Q32M88) (Protein-glucosylgalactosylhydroxylysine glucosidase):

> Catalyzes the hydrolysis of glucose from the disaccharide unit linked to hydroxylysine residues of collagen and collagen-like proteins.

**Summary**, from NCBI Gene [80162](https://www.ncbi.nlm.nih.gov/gene/80162):

> Enables protein-glucosylgalactosylhydroxylysine glucosidase activity. Involved in carbohydrate metabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26210) · Entrez [80162](https://www.ncbi.nlm.nih.gov/gene/80162) · UniProt [Q32M88](https://www.uniprot.org/uniprotkb/Q32M88) · Ensembl [ENSG00000142102](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142102)

## Data

Gene col 6596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6596); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6596]; `tensor/DDL_lfc|DDL_z.npy` [6596]; `embed/gene_vectors.npy` [6596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6596 or target_col == 6596). Every well: [[PGGHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGGHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
