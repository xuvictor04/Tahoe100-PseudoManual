---
symbol: "MON1B"
type: "gene"
col: 2320
ensembl_id: "ENSG00000103111"
name: "MON1 vesicular trafficking associated B"
location: "16q23.1"
module: 38
arm: "+"
pooled_cpm: 37.11
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# MON1B

*MON1 vesicular trafficking associated B* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +8.8, q 6e-16, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.589× (z -10.8, q 1e-24, down in 31 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.597× (z -10.2, q 9e-22, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYCE1L]] (+0.69, fdr 7e-06, ⚠ same locus), [[AKAP17A]] (+0.69, fdr 1e-05), [[TTLL3]] (+0.66, fdr 7e-06), [[ZNF432]] (+0.65, fdr 7e-06); moves opposite to [[SSX2IP]] (-0.55, fdr 3e-05), [[COX11]] (-0.55, fdr 6e-05), [[ATP5F1A]] (-0.55, fdr 6e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +8.8 | 6e-16 | 31/47 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +8.8 | 6e-16 | 31/48 (SW480, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.9 | 7e-10 | 27/46 (NCI-H1573, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +5.5 | 4e-06 | 24/44 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.003 | 19/46 (LoVo, C32, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.24×** | +4.2 | 0.003 | 15/48 (SHP-77, LoVo, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.15× | +4.1 | 0.003 | 13/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.006 | 14/47 (NCI-H2030, SW480, …) | two highest doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.006 | 12/46 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.20× | +3.7 | 0.014 | 10/48 (HEC-1-A, A-172, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.044 | 9/45 (RKO, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.044 | 11/48 (SW 1088, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -10.8 | 1e-24 | 31/47 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.597×** | -10.2 | 9e-22 | 31/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -9.6 | 2e-19 | 35/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.687×** | -7.7 | 2e-12 | 29/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -6.5 | 9e-09 | 30/48 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.768×** | -5.2 | 2e-05 | 18/35 (LoVo, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.769×** | -5.2 | 2e-05 | 22/46 (NCI-H1573, A549, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.783×** | -5.0 | 4e-05 | 22/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.794×** | -4.7 | 1e-04 | 20/44 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.810×** | -4.3 | 8e-04 | 20/48 (KATO III, H4, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.816×** | -4.2 | 0.002 | 19/47 (A-427, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.867× | -4.1 | 0.002 | 18/47 (HT-29, J82, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.827×** | -3.9 | 0.005 | 12/48 (NCI-H1573, COLO 205, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.832×** | -3.8 | 0.006 | 20/48 (KATO III, COLO 205, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.835× | -3.7 | 0.008 | 16/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.889× | -3.4 | 0.022 | 7/48 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Malotilate (drug)]] 5 µM |  | 0.856× | -3.2 | 0.047 | 7/48 (A-427, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 91.4 | 2 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.408× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.529× (z -9.5) |
| [[KATO III (line)]] | alt | 52.8 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.258× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -12.1) |
| [[HT-29 (line)]] | alt | 51.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.396× (z -8.5) |
| [[A-172 (line)]] | wt | 28.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[A-427 (line)]] | wt | 28.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[COLO 205 (line)]] | alt | 55.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[H4 (line)]] | wt | 45.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[J82 (line)]] | alt | 35.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.382× (z -8.8) |
| [[LoVo (line)]] | wt | 37.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.344× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 43.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[RPMI-7951 (line)]] | alt | 32.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -11.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[HepG2_C3A (line)]] | wt | 41.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.264× (z -8.8) |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[NCI-H1573 (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.315× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -8.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SNU-423 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.336× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW48 (line)]] | wt | 20.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.104× (z -9.9) |
| [[A498 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYCE1L]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 | STRING 543; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[AKAP17A]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.66 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ZNF432]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[NOXRED1]] | +0.65 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ZNF547]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GOSR2]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[LRIF1]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.62 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[MTF1]] | +0.62 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[TRIM39]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[KIN]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[FAM32A]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[COX11]] | -0.55 | -0.38 / -0.67 | both halves | 6e-05 |  |
| [[ATP5F1A]] | -0.55 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[LRRCC1]] | -0.54 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[MAP3K4]] | -0.54 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[MTHFD1]] | -0.52 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[NELFCD]] | -0.52 | -0.39 / -0.66 | both halves | 6e-05 |  |
| [[COQ2]] | -0.51 | -0.37 / -0.46 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.2, -21.0); signed map (10.0, 11.5). **Vector** length 101, 23.0% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.9 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.5 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +3.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -5.5 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | -4.4 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -3.5 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | MON1 vesicular trafficking associated B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:77,190,835-77,202,398 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAND2, HSRG1, KIAA0872 |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

UniProt [Q7L1V2](https://www.uniprot.org/uniprotkb/Q7L1V2) carries no function annotation.

**Summary**, from NCBI Gene [22879](https://www.ncbi.nlm.nih.gov/gene/22879):

> Predicted to contribute to guanyl-nucleotide exchange factor activity. Involved in early viral transcription and late viral transcription. Located in late endosome. Part of Mon1-Ccz1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25020](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25020) · Entrez [22879](https://www.ncbi.nlm.nih.gov/gene/22879) · UniProt [Q7L1V2](https://www.uniprot.org/uniprotkb/Q7L1V2) · Ensembl [ENSG00000103111](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103111)

## Data

Gene col 2320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2320); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2320]; `tensor/DDL_lfc|DDL_z.npy` [2320]; `embed/gene_vectors.npy` [2320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2320 or target_col == 2320). Every well: [[MON1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MON1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
