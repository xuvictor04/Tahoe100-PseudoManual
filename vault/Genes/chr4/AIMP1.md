---
symbol: "AIMP1"
type: "gene"
col: 8834
ensembl_id: "ENSG00000164022"
name: "aminoacyl tRNA synthetase complex interacting multifunctional protein 1"
location: "4q24"
module: 28
arm: "+"
pooled_cpm: 57.59
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AIMP1

*aminoacyl tRNA synthetase complex interacting multifunctional protein 1* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.37× (z +12.8, q 6e-35, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.76× (z +8.4, q 5e-15, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A46]] (+0.75, fdr 7e-06), [[COPS5]] (+0.74, fdr 7e-06), [[METTL6]] (+0.74, fdr 7e-06); moves opposite to [[UBE2G1]] (-0.66, fdr 1e-05), [[SRPK2]] (-0.63, fdr 3e-05), [[PAQR4]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +12.8 | 6e-35 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +11.6 | 2e-28 | 39/41 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +8.8 | 3e-16 | 40/45 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +8.4 | 5e-15 | 41/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.64×** | +7.1 | 2e-10 | 41/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.8 | 7e-10 | 40/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.37×** | +6.6 | 2e-09 | 34/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.002 | 28/48 (NCI-H23, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.0 | 0.004 | 26/47 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.30×** | +3.9 | 0.006 | 27/47 (J82, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +3.8 | 0.009 | 26/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.010 | 17/48 (NCI-H2347, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.010 | 26/48 (C32, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.281×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 69.5 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 46.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 55.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.3) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[A498 (line)]] | wt | 91.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 63.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 51.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 51.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 53.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 48.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 45.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 68.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 66.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 66.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 65.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +11.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 53.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 71.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.73× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 51.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +11.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.281× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 73.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A46]] | +0.75 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[COPS5]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | STRING 463 |
| [[METTL6]] | +0.74 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.73 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[TRMT13]] | +0.72 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[CCDC25]] | +0.72 | +0.77 / +0.67 | both halves | 7e-06 | STRING 475 |
| [[TMEM260]] | +0.71 | +0.78 / +0.52 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.70 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[FCF1]] | +0.70 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.69 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[SSBP1]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 | STRING 416 |
| [[RAD52]] | +0.68 | +0.76 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2G1]] | -0.66 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[SRPK2]] | -0.63 | -0.70 / -0.46 | both halves | 3e-05 |  |
| [[PAQR4]] | -0.63 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[CTXN1]] | -0.62 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[PGP]] | -0.62 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD13D]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[LSM4]] | -0.61 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.60 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[CYTH3]] | -0.60 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[CCNE1]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[BRI3BP]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[LRRC20]] | -0.59 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.772). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.6, 7.2); signed map (9.1, -23.6). **Vector** length 77.1, 20.0% of its response variance represented; |z| ≥ 3 in 623 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +6.8 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.1 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | +0.8 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -0.9 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | aminoacyl tRNA synthetase complex interacting multifunctional protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:106,315,544-106,349,456 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EMAPII, EMAP-2, p43; previously SCYE1 |
| Gene groups (HGNC) | Aminoacyl tRNA synthetase complex interacting multifunctional proteins |
| Reactome | 7 pathways, smallest: Cytosolic tRNA aminoacylation; tRNA Aminoacylation; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12904](https://www.uniprot.org/uniprotkb/Q12904) (Aminoacyl tRNA synthase complex-interacting multifunctional protein 1):

> Non-catalytic component of the multisynthase complex. Stimulates the catalytic activity of cytoplasmic arginyl-tRNA synthase. Binds tRNA. Possesses inflammatory cytokine activity. Negatively regulates TGF-beta signaling through stabilization of SMURF2 by binding to SMURF2 and inhibiting its SMAD7-mediated degradation (By similarity). Involved in glucose homeostasis through induction of glucagon secretion at low glucose levels (By similarity). Promotes dermal fibroblast proliferation and wound …

**Summary**, from NCBI Gene [9255](https://www.ncbi.nlm.nih.gov/gene/9255):

> The protein encoded by this gene is a cytokine that is specifically induced by apoptosis, and it is involved in the control of angiogenesis, inflammation, and wound healing. The release of this cytokine renders the tumor-associated vasculature sensitive to tumor necrosis factor. The precursor protein is identical to the p43 subunit, which is associated with the multi-tRNA synthetase complex, and it modulates aminoacylation activity of tRNA synthetase in normal cells. This protein is also …

**Accessions** — [HGNC:10648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10648) · Entrez [9255](https://www.ncbi.nlm.nih.gov/gene/9255) · UniProt [Q12904](https://www.uniprot.org/uniprotkb/Q12904) · Ensembl [ENSG00000164022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164022)

## Data

Gene col 8834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8834); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8834]; `tensor/DDL_lfc|DDL_z.npy` [8834]; `embed/gene_vectors.npy` [8834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8834 or target_col == 8834). Every well: [[AIMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AIMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
