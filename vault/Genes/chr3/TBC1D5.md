---
symbol: "TBC1D5"
type: "gene"
col: 5198
ensembl_id: "ENSG00000131374"
name: "TBC1 domain family member 5"
location: "3p24.3"
module: 200
arm: "+"
pooled_cpm: 324.97
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 34
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/200"]
generated_by: "tahoemap"
---

# TBC1D5

*TBC1 domain family member 5* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.40× (z +5.0, q 3e-04, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.271× (z -28.2, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC4]] (+0.69, fdr 7e-06), [[IMMP2L]] (+0.67, fdr 7e-06), [[ARID1B]] (+0.65, fdr 7e-06); moves opposite to [[GIPR]] (-0.63, fdr 1e-05), [[TMEM92-AS1]] (-0.61, fdr 1e-05), [[BAIAP3]] (-0.60, fdr 1e-05).
> It is in [[Module 200]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NFIA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +5.0 | 3e-04 | 39/47 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +3.4 | 0.18 | 17/48 (SW 900, LS 180, …) | rises with dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 1.24× | +3.3 | 0.18 | 23/48 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.23× | +3.2 | 0.18 | 27/48 (CFPAC-1, HS-578T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.22× | +3.0 | 0.27 | 28/48 (A-172, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.271×** | -28.2 | 0e+00 | 47/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.321×** | -16.7 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.377×** | -14.3 | 3e-44 | 46/47 (KATO III, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.399×** | -14.0 | 1e-42 | 47/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.432×** | -12.8 | 1e-35 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.447×** | -12.3 | 7e-33 | 46/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.454×** | -12.1 | 1e-31 | 47/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.466×** | -11.7 | 1e-29 | 46/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.490×** | -10.9 | 6e-26 | 46/48 (A-427, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.536×** | -9.5 | 1e-19 | 44/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -9.5 | 1e-19 | 42/48 (SW480, HCT15, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.576×** | -8.1 | 2e-14 | 41/47 (LoVo, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.595×** | -7.9 | 1e-13 | 39/48 (SW480, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.617×** | -7.4 | 7e-12 | 40/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -6.2 | 2e-08 | 39/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.655×** | -6.1 | 4e-08 | 41/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -5.6 | 6e-07 | 30/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.661×** | -5.1 | 9e-06 | 38/48 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.777×** | -3.5 | 0.008 | 35/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.651×** | -3.4 | 0.012 | 28/48 (Panc 03.27, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.737×** | -3.3 | 0.017 | 35/49 (PANC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.865× | -3.1 | 0.034 | 8/49 (KATO III, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 408 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -18.3) |
| [[PANC-1 (line)]] | alt | 326 | 0 | 19 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -35.2) |
| [[LoVo (line)]] | wt | 271 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -21.1) |
| [[NCI-H460 (line)]] | wt | 255 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -22.0) |
| [[A-427 (line)]] | wt | 538 | 0 | 16 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -20.3) |
| [[MIA PaCa-2 (line)]] | alt | 352 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -24.5) |
| [[Panc 03.27 (line)]] | alt | 309 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -30.0) |
| [[SW480 (line)]] | alt | 376 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -24.3) |
| [[NCI-H23 (line)]] | alt | 474 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -22.3) |
| [[HEC-1-A (line)]] | alt | 655 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -28.9) |
| [[J82 (line)]] | alt | 253 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -23.4) |
| [[SW48 (line)]] | wt | 374 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.1) |
| [[HepG2_C3A (line)]] | wt | 296 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -20.8) |
| [[LOX-IMVI (line)]] | wt | 330 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -24.6) |
| [[RKO (line)]] | wt | 343 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -19.5) |
| [[SW1417 (line)]] | alt | 411 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -25.9) |
| [[HCT15 (line)]] | alt | 448 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -14.2) |
| [[HT-29 (line)]] | alt | 230 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -22.2) |
| [[NCI-H1573 (line)]] | alt | 306 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -28.8) |
| [[SHP-77 (line)]] | alt | 351 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -14.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.518× (z -13.9) |
| [[BT-474 (line)]] | alt | 274 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -25.0) |
| [[C-33 A (line)]] | alt | 390 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.355× (z -12.6) |
| [[COLO 205 (line)]] | alt | 274 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -25.5) |
| [[LS 180 (line)]] | wt | 501 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -16.5) |
| [[C32 (line)]] | wt | 384 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -28.8) |
| [[NCI-H2030 (line)]] | alt | 397 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.3) |
| [[AN3 CA (line)]] | alt | 330 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.4) |
| [[Hs 766T (line)]] | wt | 290 | 0 | 7 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.349× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 416 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -29.8) |
| [[A549 (line)]] | wt | 424 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -28.5) |
| [[HOP62 (line)]] | alt | 358 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -27.7) |
| [[KATO III (line)]] | alt | 306 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -18.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.503× (z -12.3) |
| [[A-172 (line)]] | wt | 249 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -22.3) |
| [[RPMI-7951 (line)]] | alt | 287 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -22.6) |
| [[SW 900 (line)]] | alt | 170 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -19.7) |
| [[NCI-H1792 (line)]] | alt | 343 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.7) |
| [[SNU-423 (line)]] | alt | 330 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -21.1) |
| [[A498 (line)]] | wt | 226 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -23.1) |
| [[AsPC-1 (line)]] | alt | 172 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -22.1) |
| [[HS-578T (line)]] | alt | 262 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.2) |
| [[hTERT-HPNE (line)]] | wt | 235 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -18.3) |
| [[CFPAC-1 (line)]] | alt | 117 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -17.4) |
| [[CHP-212 (line)]] | wt | 312 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.6) |
| [[SW 1271 (line)]] | alt | 582 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.5) |
| [[H4 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 292 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 231 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC4]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 | STRING 538 |
| [[IMMP2L]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[ARID1B]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[FBXL17]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SUCLG2]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[PARD3B]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TCF12]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | +0.58 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[USP24]] | +0.58 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[NFIB]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[FARS2]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[DPH6]] | +0.57 | +0.63 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GIPR]] | -0.63 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[TMEM92-AS1]] | -0.61 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[BAIAP3]] | -0.60 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[KCTD21]] | -0.59 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.59 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[PHLDB3]] | -0.57 | -0.49 / -0.51 | both halves | 2e-05 |  |
| [[NAGK]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HID1]] | -0.57 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[TNFRSF25]] | -0.56 | -0.51 / -0.46 | both halves | 2e-05 |  |
| [[RGS9]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[GDPD5]] | -0.55 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[KLC3]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIA]] | B | NFIA activity strengthens TBC1D5's drug response | lines that do not express NFIA (11) vs lines expressing it (37) | the lines without NFIA respond 0.76× as strongly (z diff +2.36); strongest at Ixazomib citrate 5 µM: 0.70x vs 0.49x (z diff +3.9) | 0.065 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LYPD3]] | B | LYPD3 activity lowers TBC1D5's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.16× higher at baseline in the lines without LYPD3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 200]]; 16 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.6, 13.4); signed map (10.2, -13.0). **Vector** length 93.7, 44.9% of its response variance represented; |z| ≥ 3 in 1,616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.2 | -12.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.2 | -7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.4 | -7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -0.4 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | +2.2 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.8 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.8 | -14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.4 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -12.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.4 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:17,157,162-18,444,817 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0210 |
| Gene groups (HGNC) | TBC1 domain family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92609](https://www.uniprot.org/uniprotkb/Q92609) (TBC1 domain family member 5):

> May act as a GTPase-activating protein (GAP) for Rab family protein(s). May act as a GAP for RAB7A. Can displace RAB7A and retromer CSC subcomplex from the endosomal membrane to the cytosol; at least retromer displacement seems to require its catalytic activity. Required for retrograde transport of cargo proteins from endosomes to the trans-Golgi network (TGN); the function seems to require its catalytic activity. Involved in regulation of autophagy. May act as a molecular switch between …

**Summary**, from NCBI Gene [9779](https://www.ncbi.nlm.nih.gov/gene/9779):

> Enables AP-2 adaptor complex binding activity and retromer complex binding activity. Involved in several processes, including macroautophagy; positive regulation of receptor internalization; and retrograde transport, endosome to Golgi. Located in Atg1/ULK1 kinase complex; autophagosome; and cytoplasmic vesicle membrane. Part of retromer complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19166) · Entrez [9779](https://www.ncbi.nlm.nih.gov/gene/9779) · UniProt [Q92609](https://www.uniprot.org/uniprotkb/Q92609) · Ensembl [ENSG00000131374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131374)

## Data

Gene col 5198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5198); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5198]; `tensor/DDL_lfc|DDL_z.npy` [5198]; `embed/gene_vectors.npy` [5198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5198 or target_col == 5198). Every well: [[TBC1D5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
