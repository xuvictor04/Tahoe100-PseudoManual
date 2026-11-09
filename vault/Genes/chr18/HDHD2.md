---
symbol: "HDHD2"
type: "gene"
col: 9438
ensembl_id: "ENSG00000167220"
name: "haloacid dehalogenase like hydrolase domain containing 2"
location: "18q21.1"
module: 25
arm: "+"
pooled_cpm: 32.36
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# HDHD2

*haloacid dehalogenase like hydrolase domain containing 2* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.44× (z +5.8, q 4e-06, up in 24 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 3.77×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 3.23×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.538× (z -10.2, q 1e-21, down in 38 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.662× (z -6.8, q 2e-09, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUF1]] (+0.75, fdr 7e-06), [[ALG10B]] (+0.70, fdr 1e-05), [[GTF2H3]] (+0.69, fdr 7e-06); moves opposite to [[RNF122]] (-0.68, fdr 3e-05), [[CARHSP1]] (-0.67, fdr 1e-05), [[TRIM62]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9438.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 3.77×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A-172 3.23×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +5.8 | 4e-06 | 24/40 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.6 | 8e-06 | 26/44 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.4 | 0.15 | 0/48 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.15× | +3.3 | 0.15 | 17/48 (AsPC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.23× | +3.1 | 0.22 | 19/43 (SHP-77, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9438.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.538×** | -10.2 | 1e-21 | 38/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.588×** | -8.7 | 7e-16 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -6.8 | 2e-09 | 36/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.711×** | -5.6 | 3e-06 | 29/48 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.725×** | -5.3 | 1e-05 | 27/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.753×** | -4.7 | 3e-04 | 25/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.586×** | -4.6 | 4e-04 | 23/48 (MIA PaCa-2, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -4.5 | 4e-04 | 25/48 (HCT15, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -4.1 | 0.003 | 24/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.841× | -4.0 | 0.003 | 24/48 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.789×** | -3.9 | 0.005 | 23/47 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.785×** | -3.8 | 0.006 | 22/47 (H4, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.807×** | -3.5 | 0.018 | 19/48 (H4, NCI-H1792, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.694×** | -3.1 | 0.066 | 20/42 (NCI-H1792, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.818×** | -3.1 | 0.066 | 17/48 (Hs 766T, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9438. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 38.1 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.266× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 28.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 28.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -15.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 31.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.77× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.337× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[C-33 A (line)]] | alt | 75.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -14.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 42.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0985× (z -14.9) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1792 (line)]] | alt | 57.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.23× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0708× (z -11.2) |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.244× (z -9.0) |
| [[HOP62 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.141× (z -8.5) ⚠ toxic |
| [[J82 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.318× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0481× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.397× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -11.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 57.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0928× (z -9.6) ⚠ toxic |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9438), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUF1]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[ALG10B]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[GTF2H3]] | +0.69 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NEK9]] | +0.69 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[LIN7C]] | +0.69 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[MRRF]] | +0.69 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.68 | +0.45 / +0.71 | both halves | 3e-05 |  |
| [[MBTPS2]] | +0.68 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[GMFB]] | +0.68 | +0.39 / +0.75 | both halves | 5e-05 |  |
| [[DPY19L4]] | +0.68 | +0.33 / +0.74 | both halves | 1e-04 |  |
| [[TRMT13]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.68 | +0.61 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF122]] | -0.68 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[CARHSP1]] | -0.67 | -0.50 / -0.71 | both halves | 1e-05 |  |
| [[TRIM62]] | -0.66 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[RALGDS]] | -0.64 | -0.44 / -0.68 | both halves | 3e-05 |  |
| [[SLC66A2]] | -0.64 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.63 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[RASSF7]] | -0.63 | -0.32 / -0.68 | both halves | 2e-04 |  |
| [[SDHAF1]] | -0.62 | -0.30 / -0.61 | both halves | 2e-04 |  |
| [[ARID3A]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[RABAC1]] | -0.61 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[LIN7B]] | -0.61 | -0.28 / -0.63 | both halves | 3e-04 |  |
| [[VKORC1]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-30.7, -17.6); signed map (0.8, -36.8). **Vector** length 72.9, 13.4% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | -1.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.1 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.4 | -3.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -2.9 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | haloacid dehalogenase like hydrolase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:47,107,408-47,150,500 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564D1378 |
| Gene groups (HGNC) | Haloacid dehalogenase like hydrolase domain containing |
| Matched by | ensembl_id |

UniProt [Q9H0R4](https://www.uniprot.org/uniprotkb/Q9H0R4) carries no function annotation.

**Summary**, from NCBI Gene [84064](https://www.ncbi.nlm.nih.gov/gene/84064):

> Enables enzyme binding activity. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25364](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25364) · Entrez [84064](https://www.ncbi.nlm.nih.gov/gene/84064) · UniProt [Q9H0R4](https://www.uniprot.org/uniprotkb/Q9H0R4) · Ensembl [ENSG00000167220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167220)

## Data

Gene col 9438: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9438); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9438, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9438]; `tensor/DDL_lfc|DDL_z.npy` [9438]; `embed/gene_vectors.npy` [9438]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9438 or target_col == 9438). Every well: [[HDHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
