---
symbol: "TTC12"
type: "gene"
col: 7361
ensembl_id: "ENSG00000149292"
name: "tetratricopeptide repeat domain 12"
location: "11q23.2"
module: 51
arm: "+"
pooled_cpm: 15.08
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# TTC12

*tetratricopeptide repeat domain 12* — 11q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.69× (z +5.7, q 7e-06, up in 12 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.44× (z +4.2, q 0.009, up in 20 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.388× (z -10.7, q 5e-24, down in 41 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.477× (z -8.4, q 1e-14, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHFR2]] (+0.67, fdr 7e-06), [[CARF]] (+0.62, fdr 1e-05), [[ZNF839]] (+0.61, fdr 1e-05); moves opposite to [[DAGLB]] (-0.54, fdr 7e-05), [[LRRC8A]] (-0.53, fdr 2e-05), [[TMEM184B]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.7 | 7e-06 | 12/25 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.009 | 20/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.011 | 18/46 (KATO III, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.28×** | +3.9 | 0.013 | 19/47 (AsPC-1, LoVo, …) | top dose only | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.016 | 17/46 (KATO III, SW480, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.035 | 16/46 (SW480, HCT15, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.057 | 19/46 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.31× | +3.1 | 0.15 | 10/46 (KATO III, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.388×** | -10.7 | 5e-24 | 41/46 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.420×** | -9.8 | 3e-20 | 34/46 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.477×** | -8.4 | 1e-14 | 38/46 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.254×** | -8.1 | 6e-14 | 38/46 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.267×** | -7.8 | 6e-13 | 33/45 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.503×** | -7.8 | 7e-13 | 31/46 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.505×** | -7.7 | 8e-13 | 31/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -6.8 | 1e-09 | 29/46 (Panc 03.27, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.562×** | -6.5 | 4e-09 | 35/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.561×** | -6.3 | 2e-08 | 27/41 (HCT15, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.606×** | -5.7 | 8e-07 | 26/46 (PANC-1, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.643×** | -4.7 | 1e-04 | 25/46 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.674×** | -4.5 | 3e-04 | 22/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -4.3 | 8e-04 | 21/47 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.683×** | -4.1 | 0.001 | 21/45 (A549, RPMI-7951, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.002 | 21/46 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.724×** | -3.7 | 0.008 | 19/46 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.740×** | -3.4 | 0.020 | 12/46 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.755×** | -3.2 | 0.040 | 14/46 (NCI-H661, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 23.3 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.160× (z -16.0) |
| [[PANC-1 (line)]] | alt | 23.8 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -14.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -10.3) |
| [[KATO III (line)]] | alt | 54.7 | 0 | 5 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0815× (z -10.4) |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 13.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 23.7 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.220× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 23.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -9.3) |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.194× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -10.8) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.180× (z -9.1) |
| [[BT-474 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0715× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[H4 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0210× (z -13.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0599× (z -12.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 6.30 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 0.05 µM 0.0652× (z -8.7) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0501× (z -12.4) |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 13.5 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0786× (z -9.1) |
| [[A-172 (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR2]] | +0.67 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[CARF]] | +0.62 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ZNF839]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SENP6]] | +0.61 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[TMEM254]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LYRM9]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SREK1]] | +0.59 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CCDC191]] | +0.55 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[NHLRC2]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[WDR31]] | +0.55 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SCAF8]] | +0.55 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[ZMAT1]] | +0.54 | +0.63 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAGLB]] | -0.54 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[LRRC8A]] | -0.53 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TMEM184B]] | -0.51 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ZNF668]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[GRIN2D]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[ZCCHC17]] | -0.48 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[POR]] | -0.47 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[TBC1D20]] | -0.47 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-28.7, 21.6); signed map (12.3, -35.3). **Vector** length 61.9, 11.0% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.2 | -0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +2.1 | +3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -7.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.2 — chr11:113,314,579-113,383,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13859, FLJ20535, TPARM |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H892](https://www.uniprot.org/uniprotkb/Q9H892) (Tetratricopeptide repeat protein 12):

> Cytoplasmic protein that plays a role in the proper assembly of dynein arm complexes in motile cilia in both respiratory cells and sperm flagella.

**Summary**, from NCBI Gene [54970](https://www.ncbi.nlm.nih.gov/gene/54970):

> Involved in axonemal dynein complex assembly and sperm axoneme assembly. Located in centrosome and cytoplasm. Implicated in acute lymphoblastic leukemia; alcohol dependence; drug dependence (multiple); nicotine dependence; and primary ciliary dyskinesia 45. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23700) · Entrez [54970](https://www.ncbi.nlm.nih.gov/gene/54970) · UniProt [Q9H892](https://www.uniprot.org/uniprotkb/Q9H892) · Ensembl [ENSG00000149292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149292)

## Data

Gene col 7361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7361); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7361]; `tensor/DDL_lfc|DDL_z.npy` [7361]; `embed/gene_vectors.npy` [7361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7361 or target_col == 7361). Every well: [[TTC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
