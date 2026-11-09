---
symbol: "CEP44"
type: "gene"
col: 8875
ensembl_id: "ENSG00000164118"
name: "centrosomal protein 44"
location: "4q34.1"
module: 69
arm: "+"
pooled_cpm: 52.03
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CEP44

*centrosomal protein 44* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.21× (z +6.0, q 1e-06, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LS 180 3.06×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.03×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.405× (z -19.6, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.417× (z -9.9, q 1e-20, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDCD4]] (+0.67, fdr 1e-05), [[CENPC]] (+0.66, fdr 7e-06), [[HBP1]] (+0.62, fdr 2e-05); moves opposite to [[ZNF787]] (-0.50, fdr 4e-05), [[B3GALT6]] (-0.49, fdr 1e-05), [[RRP7A]] (-0.49, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8875.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LS 180 3.06×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 2.03×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +6.0 | 1e-06 | 20/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.013 | 19/48 (LS 180, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.405×** | -19.6 | 0e+00 | 47/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.417×** | -9.9 | 1e-20 | 42/48 (A498, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.419×** | -9.9 | 1e-20 | 40/48 (HEC-1-A, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.474×** | -8.5 | 3e-15 | 37/48 (SW48, RKO, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.484×** | -8.2 | 2e-14 | 36/48 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.488×** | -8.1 | 4e-14 | 38/48 (HEC-1-A, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.730×** | -6.4 | 1e-08 | 26/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -6.4 | 1e-08 | 31/48 (SW 1088, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[EX229 (drug)]] 0.5 µM |  | **0.668×** | -5.8 | 3e-07 | 33/48 (J82, RKO, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.677×** | -5.6 | 1e-06 | 29/48 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.845× | -5.1 | 2e-05 | 22/48 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.646×** | -4.9 | 4e-05 | 26/45 (Panc 03.27, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.795×** | -4.7 | 1e-04 | 22/47 (HOP62, Panc 03.27, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.800×** | -4.6 | 2e-04 | 22/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.668×** | -4.6 | 2e-04 | 24/47 (HCT15, NCI-H661, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.811×** | -4.5 | 2e-04 | 23/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.802×** | -4.5 | 2e-04 | 20/48 (NCI-H661, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 89.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.261× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.339× (z -9.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 55.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.361× (z -8.9) |
| [[RKO (line)]] | wt | 69.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.136× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 44.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.310× (z -15.2) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 43.8 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.362× (z -13.6) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 78.1 | 0 | 2 | — | [[Cepharanthine (drug)]] 0.5 µM 0.103× (z -9.6) |
| [[SW48 (line)]] | wt | 50.7 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -10.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0679× (z -9.5) |
| [[SW480 (line)]] | alt | 62.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.389× (z -12.6) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.504× (z -9.1) |
| [[A-427 (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[CFPAC-1 (line)]] | alt | 87.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -8.8) |
| [[COLO 205 (line)]] | alt | 63.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.329× (z -8.6) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 74.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[HCT15 (line)]] | alt | 66.5 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0885× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 73.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -14.5) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.437× (z -9.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.184× (z -12.4) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.262× (z -12.4) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 53.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.399× (z -10.4) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.332× (z -10.3) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.279× (z -12.5) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -8.8) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 56.3 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.369× (z -10.4) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 89.3 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.125× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.384× (z -9.9) ⚠ unreliable plate only |
| [[SW 1088 (line)]] | alt | 65.1 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.5 µM 0.0650× (z -8.9) |
| [[SW 900 (line)]] | alt | 46.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.232× (z -12.2) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -9.4) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD4]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[CENPC]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HBP1]] | +0.62 | +0.46 / +0.68 | both halves | 2e-05 |  |
| [[HMGB2]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CEP57]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CCDC28A]] | +0.60 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[TXNDC16]] | +0.60 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MBIP]] | +0.59 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CDK19]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[UBN2]] | +0.58 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[MIS18BP1]] | +0.58 | +0.61 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF787]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[B3GALT6]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RRP7A]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[NACC1]] | -0.49 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ZNF513]] | -0.49 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[EIF6]] | -0.49 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[ZNF195]] | -0.48 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NOP2]] | -0.48 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SNHG17]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[DDX21]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[RRP1]] | -0.46 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-26.3, -52.8); signed map (-46.4, -35.5). **Vector** length 109, 27.0% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.3 | +4.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.6 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.6 | -19.6 |
|  | [[EX229 (drug)]] 5 µM |  | -7.5 | -9.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.5 | -8.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.4 | -8.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.4 | -8.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.0 | -9.9 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:174,283,730-174,333,380 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1712 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0F1](https://www.uniprot.org/uniprotkb/Q9C0F1) (Centrosomal protein of 44 kDa):

> Centriole-enriched microtubule-binding protein involved in centriole biogenesis. In collaboration with CEP295 and POC1B, is required for the centriole-to-centrosome conversion by ensuring the formation of bona fide centriole wall. Functions as a linker component that maintains centrosome cohesion. Associates with CROCC and regulates its stability and localization to the centrosome.

**Summary**, from NCBI Gene [80817](https://www.ncbi.nlm.nih.gov/gene/80817):

> Enables microtubule binding activity. Involved in centriole replication and centriole-centriole cohesion. Located in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29356) · Entrez [80817](https://www.ncbi.nlm.nih.gov/gene/80817) · UniProt [Q9C0F1](https://www.uniprot.org/uniprotkb/Q9C0F1) · Ensembl [ENSG00000164118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164118)

## Data

Gene col 8875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8875); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8875]; `tensor/DDL_lfc|DDL_z.npy` [8875]; `embed/gene_vectors.npy` [8875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8875 or target_col == 8875). Every well: [[CEP44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
