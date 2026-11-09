---
symbol: "HEXD"
type: "gene"
col: 9832
ensembl_id: "ENSG00000169660"
name: "hexosaminidase D"
location: "17q25.3"
module: 89
arm: "+"
pooled_cpm: 13.91
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 26
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# HEXD

*hexosaminidase D* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.43× (z +4.7, q 0.001, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.446× (z -14.9, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETDB1]] (+0.60, fdr 7e-06), [[PHYKPL]] (+0.60, fdr 7e-06), [[MAFIP]] (+0.59, fdr 1e-05); moves opposite to [[TLN1]] (-0.56, fdr 1e-05), [[SEPTIN11]] (-0.50, fdr 5e-05), [[LMO7DN]] (-0.49, fdr 3e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +4.7 | 0.001 | 20/47 (HOP62, LS 180, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.5 | 0.002 | 21/47 (BT-474, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.004 | 14/46 (KATO III, LS 180, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.058 | 14/47 (A498, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.058 | 15/47 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.11 | 10/48 (SK-MEL-2, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.2 | 0.11 | 14/48 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.11 | 13/47 (LS 180, SW 900, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.12 | 9/44 (HOP62, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.12 | 8/48 (LoVo, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.446×** | -14.9 | 0e+00 | 42/47 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.477×** | -9.3 | 5e-18 | 32/46 (PANC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -9.1 | 1e-17 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -9.1 | 1e-17 | 31/45 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -8.4 | 4e-15 | 37/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.319×** | -7.8 | 6e-13 | 34/47 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -7.6 | 3e-12 | 27/45 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -7.5 | 5e-12 | 31/47 (PANC-1, CHP-212, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.604×** | -6.3 | 2e-08 | 22/42 (COLO 205, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -6.1 | 5e-08 | 25/43 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.676×** | -5.1 | 2e-05 | 23/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -4.6 | 2e-04 | 21/47 (Panc 03.27, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -4.6 | 2e-04 | 16/46 (HCT15, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.734×** | -4.0 | 0.003 | 12/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -4.0 | 0.003 | 19/44 (SW480, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.764×** | -3.3 | 0.024 | 14/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.025 | 14/44 (SW480, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.034 | 12/47 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.054 | 13/47 (SW480, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.5 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -23.4) |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.9) |
| [[SW480 (line)]] | alt | 20.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -12.3) |
| [[COLO 205 (line)]] | alt | 23.9 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0576× (z -15.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.1) |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.275× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 11.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -13.2) |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -16.0) |
| [[A549 (line)]] | wt | 17.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -18.0) |
| [[KATO III (line)]] | alt | 24.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.8) |
| [[LoVo (line)]] | wt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 9.31 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.6) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -9.6) |
| [[C32 (line)]] | wt | 7.42 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0804× (z -8.8) |
| [[CHP-212 (line)]] | wt | 34.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 7.09 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.35× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 5.62 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0881× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.1) |
| [[RKO (line)]] | wt | 6.81 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0617× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -18.5) |
| [[SNU-1 (line)]] | wt | 9.80 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0664× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETDB1]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PHYKPL]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MAFIP]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ZNF594-DT]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[EXO5-DT]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[CCZ1P1]] | +0.56 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MAP2K7]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[MED9]] | +0.54 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[TDG]] | +0.53 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[ZNF493]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ZNF790-AS1]] | +0.52 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[LINC03006-1]] | +0.52 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLN1]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SEPTIN11]] | -0.50 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[LMO7DN]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[FH]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ANO6]] | -0.48 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CYFIP1]] | -0.47 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CLOCK]] | -0.47 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[CFL1]] | -0.46 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[CYB5D1]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ACLY]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[EPB41L2]] | -0.44 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[ERI2]] | -0.44 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.9, 12.5); signed map (-15.5, -18.4). **Vector** length 66.4, 11.6% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | +2.1 | +2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.7 | +3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.4 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.9 | -0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.7 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -3.3 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | hexosaminidase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,418,318-82,442,645 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23825; previously HEXDC |
| Gene groups (HGNC) | Hexosaminidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVB3](https://www.uniprot.org/uniprotkb/Q8WVB3) (Hexosaminidase D):

> Has hexosaminidase activity. Responsible for the cleavage of the monosaccharides N-acetylglucosamine (GlcNAc) and N-acetylgalactosamine (GalNAc) from cellular substrates. Has a preference for galactosaminide over glucosaminide substrates.

**Summary**, from NCBI Gene [284004](https://www.ncbi.nlm.nih.gov/gene/284004):

> Enables beta-N-acetylhexosaminidase activity. Predicted to be involved in carbohydrate metabolic process. Located in extracellular vesicle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26307) · Entrez [284004](https://www.ncbi.nlm.nih.gov/gene/284004) · UniProt [Q8WVB3](https://www.uniprot.org/uniprotkb/Q8WVB3) · Ensembl [ENSG00000169660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169660)

## Data

Gene col 9832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9832); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9832]; `tensor/DDL_lfc|DDL_z.npy` [9832]; `embed/gene_vectors.npy` [9832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9832 or target_col == 9832). Every well: [[HEXD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEXD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
