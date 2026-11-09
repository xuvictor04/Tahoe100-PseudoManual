---
symbol: "RAB14"
type: "gene"
col: 4059
ensembl_id: "ENSG00000119396"
name: "RAB14, member RAS oncogene family"
location: "9q33.2"
module: 29
arm: "+"
pooled_cpm: 107.99
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# RAB14

*RAB14, member RAS oncogene family* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.52× (z +15.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.821× (z -4.7, q 7e-04, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX11]] (+0.61, fdr 1e-05), [[ATP5F1A]] (+0.58, fdr 1e-05), [[NCOA4]] (+0.57, fdr 6e-05); moves opposite to [[ZNF787]] (-0.62, fdr 1e-05), [[SYCE1L]] (-0.56, fdr 3e-05), [[C19orf25]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.52×** | +15.6 | 0e+00 | 48/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +10.0 | 4e-21 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +9.7 | 4e-20 | 42/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.75×** | +9.5 | 3e-19 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +9.1 | 1e-17 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +7.3 | 3e-11 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.7 | 2e-09 | 35/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +6.2 | 3e-08 | 35/48 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.0 | 9e-08 | 37/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.26×** | +3.8 | 0.008 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.036 | 24/48 (PANC-1, SK-MEL-2, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.3 | 0.048 | 1/50 (MIA PaCa-2) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.21×** | +3.2 | 0.061 | 21/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.071 | 18/48 (A498, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | 1.20× | +3.0 | 0.090 | 20/48 (A-427, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -4.7 | 7e-04 | 28/49 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.678×** | -4.7 | 7e-04 | 36/48 (A-172, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.792×** | -3.8 | 0.026 | 24/44 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.802×** | -3.7 | 0.026 | 30/48 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.859× | -3.7 | 0.030 | 19/48 (NCI-H2347, hTERT-HPNE, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 92.7 | 10 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +17.6) | — |
| [[PANC-1 (line)]] | alt | 67.9 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.34× (z +21.7) | — |
| [[HOP62 (line)]] | alt | 86.2 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +13.3) | — |
| [[RKO (line)]] | wt | 161 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 119 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +18.1) | — |
| [[LoVo (line)]] | wt | 73.6 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +16.2) | — |
| [[NCI-H23 (line)]] | alt | 64.8 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 209 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 109 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.53× (z +15.8) | — |
| [[NCI-H1573 (line)]] | alt | 64.7 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.84× (z +15.3) | — |
| [[A549 (line)]] | wt | 93.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.80× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 82.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +14.0) | — |
| [[SHP-77 (line)]] | alt | 106 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -14.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 83.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +12.9) | — |
| [[H4 (line)]] | wt | 101 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.7) | — |
| [[HEC-1-A (line)]] | alt | 140 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.7) ⚠ cell-cycle shift, explains ~32% of this change | [[Dinaciclib (drug)]] 5 µM 0.383× (z -11.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 103 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 157 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +17.7) | — |
| [[SW 900 (line)]] | alt | 97.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 151 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +12.6) | — |
| [[SW48 (line)]] | wt | 113 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.58× (z +13.2) | — |
| [[A-427 (line)]] | wt | 54.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A498 (line)]] | wt | 148 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 112 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +11.3) | — |
| [[HCT15 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 114 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 123 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 63.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 127 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 76.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0934× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 145 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 98.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 200 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX11]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ATP5F1A]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.57 | +0.38 / +0.70 | both halves | 6e-05 |  |
| [[ZBTB41]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PYURF]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ABITRAM]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MANEA]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[FBXO7]] | +0.55 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MBTPS2]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ATRAID]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[CFL2]] | +0.55 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[TWF1]] | +0.55 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF787]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[SYCE1L]] | -0.56 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[C19orf25]] | -0.54 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[BIN3]] | -0.54 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[PFDN2]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[USP36]] | -0.52 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TMEM44]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[FPGS]] | -0.51 | -0.37 / -0.56 | both halves | 7e-05 |  |
| [[MPP3]] | -0.51 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[RABGEF1P1]] | -0.51 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[UBE2CP5]] | -0.50 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ZNF83]] | -0.50 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.9, -18.2); signed map (-19.4, -39.7). **Vector** length 92.8, 27.8% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | -1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | -0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +1.1 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +2.3 | +1.9 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.6 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.1 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | +1.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.7 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RAB14, member RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:121,178,133-121,223,014 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBP, RAB-14 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 12 pathways, smallest: Synthesis of PIPs at the plasma membrane; RAB geranylgeranylation; Translocation of SLC2A4 (GLUT4) to the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [P61106](https://www.uniprot.org/uniprotkb/P61106) (Ras-related protein Rab-14):

> The small GTPases Rab are key regulators of intracellular membrane trafficking, from the formation of transport vesicles to their fusion with membranes. Rabs cycle between an inactive GDP-bound form and an active GTP-bound form that is able to recruit to membranes different set of downstream effectors directly responsible for vesicle formation, movement, tethering and fusion. RAB14 is involved in membrane trafficking between the Golgi complex and endosomes during early embryonic development (By …

**Summary**, from NCBI Gene [51552](https://www.ncbi.nlm.nih.gov/gene/51552):

> RAB14 belongs to the large RAB family of low molecular mass GTPases that are involved in intracellular membrane trafficking. These proteins act as molecular switches that flip between an inactive GDP-bound state and an active GTP-bound state in which they recruit downstream effector proteins onto membranes (Junutula et al., 2004 [PubMed 15004230]).[supplied by OMIM, Mar 2009]

**Accessions** — [HGNC:16524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16524) · Entrez [51552](https://www.ncbi.nlm.nih.gov/gene/51552) · UniProt [P61106](https://www.uniprot.org/uniprotkb/P61106) · Ensembl [ENSG00000119396](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119396)

## Data

Gene col 4059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4059); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4059]; `tensor/DDL_lfc|DDL_z.npy` [4059]; `embed/gene_vectors.npy` [4059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4059 or target_col == 4059). Every well: [[RAB14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
