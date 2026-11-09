---
symbol: "PRPF31"
type: "gene"
col: 2629
ensembl_id: "ENSG00000105618"
name: "pre-mRNA processing factor 31"
location: "19q13.42"
module: 127
arm: "+"
pooled_cpm: 21.73
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# PRPF31

*pre-mRNA processing factor 31* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +13.7, q 3e-40, up in 41 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.68× (z +9.1, q 2e-17, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.813× (z -4.6, q 0.002, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.361×, RPMI-7951 0.337×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SNU-1 0.0873×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.163×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAP1]] (+0.75, fdr 7e-06), [[LAS1L]] (+0.69, fdr 7e-06), [[DHX16]] (+0.69, fdr 7e-06); moves opposite to [[TRIM36]] (-0.55, fdr 3e-05), [[MAPK6]] (-0.52, fdr 4e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2629.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.19×** | +13.7 | 3e-40 | 41/42 (SW480, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.92×** | +11.0 | 9e-26 | 27/32 (A498, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.83×** | +10.6 | 8e-24 | 41/48 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.91×** | +10.5 | 9e-24 | 29/38 (A498, LS 180, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.68×** | +9.1 | 2e-17 | 38/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.65×** | +8.8 | 2e-16 | 38/48 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.47×** | +6.8 | 1e-09 | 25/48 (SW480, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.44×** | +6.4 | 1e-08 | 27/48 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.42×** | +6.1 | 7e-08 | 25/45 (CFPAC-1, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +6.0 | 1e-07 | 24/47 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +5.7 | 5e-07 | 28/48 (SNU-423, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 5e-06 | 20/47 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +5.0 | 3e-05 | 21/46 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.7 | 1e-04 | 16/44 (NCI-H2030, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[NG25 (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 15/46 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.001 | 15/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.001 | 15/48 (RPMI-7951, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.022 | 13/48 (A-172, NCI-H2030, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.025 | 14/46 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.030 | 10/48 (A549, PANC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.061 | 11/46 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.26×** | +2.8 | 0.089 | 6/46 (HCT15, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2629.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.361×, RPMI-7951 0.337×); [[Temsirolimus (drug)]] 0.5 µM in 1 line (SNU-1 0.0873×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-423 0.163×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -4.6 | 0.002 | 21/48 (RKO, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.783×** | -4.3 | 0.005 | 14/48 (RKO, COLO 205, …) | inconsistent across doses |  |
| [[Oleic acid (drug)]] 0.05 µM |  | **0.793×** | -3.8 | 0.021 | 6/48 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.805×** | -3.8 | 0.021 | 15/48 (LS 180, RPMI-7951, …) | two highest doses |  |
| [[Saquinavir (drug)]] 0.05 µM |  | 0.834× | -3.2 | 0.17 | 8/46 (HCT15, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.873× | -3.0 | 0.22 | 14/48 (A-172, LS 180, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2629. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[PANC-1 (line)]] | alt | 31.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW480 (line)]] | alt | 22.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Decitabine (drug)]] 0.05 µM 0.0803× (z -8.8) |
| [[A-172 (line)]] | wt | 25.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RKO (line)]] | wt | 27.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 25.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -9.0) |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0873× (z -10.9) |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.163× (z -9.4) |
| [[A-427 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2629), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAP1]] | +0.75 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[LAS1L]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 | STRING 902 |
| [[DHX16]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 965 |
| [[RNF40]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[SNRNP200]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[ABCF3]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[USP19]] | +0.67 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[NOP9]] | +0.66 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[DMAP1]] | +0.65 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.65 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PRPF19]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 518 |
| [[STK36]] | +0.64 | +0.73 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM36]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MAPK6]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.0, -3.1); signed map (-13.2, -29.1). **Vector** length 69.7, 12.3% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.4 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +5.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.3 | +10.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -2.9 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:54,115,410-54,131,719 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-BR-99, PRP31, hPrp31, SNRNP61; previously RP11 |
| Gene groups (HGNC) | U4/U6 small nuclear ribonucleoprotein particle |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWY3](https://www.uniprot.org/uniprotkb/Q8WWY3) (U4/U6 small nuclear ribonucleoprotein Prp31):

> Involved in pre-mRNA splicing as component of the spliceosome. Required for the assembly of the U4/U5/U6 tri-snRNP complex, one of the building blocks of the spliceosome.

**Summary**, from NCBI Gene [26121](https://www.ncbi.nlm.nih.gov/gene/26121):

> This gene encodes a component of the spliceosome complex and is one of several retinitis pigmentosa-causing genes. When the gene product is added to the spliceosome complex, activation occurs.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:15446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15446) · Entrez [26121](https://www.ncbi.nlm.nih.gov/gene/26121) · UniProt [Q8WWY3](https://www.uniprot.org/uniprotkb/Q8WWY3) · Ensembl [ENSG00000105618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105618)

## Data

Gene col 2629: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2629); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2629, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2629]; `tensor/DDL_lfc|DDL_z.npy` [2629]; `embed/gene_vectors.npy` [2629]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2629 or target_col == 2629). Every well: [[PRPF31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
