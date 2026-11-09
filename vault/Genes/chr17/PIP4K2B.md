---
symbol: "PIP4K2B"
type: "gene"
col: 15873
ensembl_id: "ENSG00000276293"
name: "phosphatidylinositol-5-phosphate 4-kinase type 2 beta"
location: "17q12"
module: 127
arm: "+"
pooled_cpm: 41.34
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# PIP4K2B

*phosphatidylinositol-5-phosphate 4-kinase type 2 beta* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.25× (z +3.8, q 0.099, up in 19 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.20× (z +3.5, q 0.100, up in 10 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 3.22×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.499× (z -12.5, q 3e-33, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF5]] (+0.62, fdr 3e-05), [[SCRIB]] (+0.61, fdr 1e-05), [[ZNF607]] (+0.60, fdr 2e-05); moves opposite to [[NDUFB1]] (-0.48, fdr 6e-05), [[CCDC126]] (-0.48, fdr 1e-04), [[CEP164P1]] (-0.45, fdr 8e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 3.22×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.8 | 0.099 | 19/45 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.100 | 10/48 (A549, HOP62, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.5 | 0.100 | 14/41 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15873.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.499×** | -12.5 | 3e-33 | 41/48 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.577×** | -10.3 | 2e-22 | 39/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -9.8 | 3e-20 | 38/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -9.6 | 9e-20 | 34/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -9.1 | 9e-18 | 36/47 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.630×** | -8.7 | 5e-16 | 35/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -8.1 | 3e-14 | 33/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.641×** | -7.5 | 5e-12 | 29/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.678×** | -7.3 | 2e-11 | 32/48 (HT-29, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -6.9 | 4e-10 | 30/48 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.691×** | -6.5 | 3e-09 | 31/48 (NCI-H661, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.706×** | -6.5 | 3e-09 | 29/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.708×** | -6.5 | 4e-09 | 26/48 (BT-474, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.719×** | -5.9 | 1e-07 | 28/47 (NCI-H460, BT-474, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.807×** | -5.7 | 5e-07 | 26/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -5.6 | 7e-07 | 25/48 (A-172, BT-474, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.752×** | -5.3 | 3e-06 | 29/48 (H4, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.760×** | -5.1 | 8e-06 | 23/48 (SW1417, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.864× | -3.9 | 0.003 | 19/48 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 245 | 0 | 10 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 39.3 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -14.4) |
| [[HOP62 (line)]] | alt | 50.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.308× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.320× (z -10.2) |
| [[PANC-1 (line)]] | alt | 30.5 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.326× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.330× (z -12.3) |
| [[A549 (line)]] | wt | 41.5 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.209× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -18.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.354× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 33.3 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 52.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.278× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.400× (z -8.6) |
| [[SW1417 (line)]] | alt | 30.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -11.0) |
| [[AN3 CA (line)]] | alt | 54.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.121× (z -10.4) |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 40.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 47.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -8.8) |
| [[A-172 (line)]] | wt | 55.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.336× (z -10.4) |
| [[A-427 (line)]] | wt | 59.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -12.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 42.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.397× (z -8.9) |
| [[HCT15 (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0354× (z -18.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 35.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 67.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 35.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.337× (z -8.6) |
| [[RKO (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -14.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.482× (z -9.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF5]] | +0.62 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[SCRIB]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZNF607]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ATP13A1]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MEN1]] | +0.58 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CUL9]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PRRC2A]] | +0.57 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[U2AF2]] | +0.56 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[SRCAP]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BACE1-AS]] | +0.54 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ZNF512B]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB1]] | -0.48 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[CCDC126]] | -0.48 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[CEP164P1]] | -0.45 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[DNAJC1]] | -0.44 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.2, -25.6); signed map (-12.6, -33.4). **Vector** length 83.5, 18.4% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.9 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.6 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.6 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -10.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -6.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-5-phosphate 4-kinase type 2 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:38,765,691-38,800,126 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIP5KIIB, PIP5KIIbeta; previously PIP5K2B |
| Gene groups (HGNC) | Phosphatidylinositol-5-phosphate 4-kinase type 2 family |
| Reactome | 13 pathways, smallest: Synthesis of PIPs in the nucleus; PI5P Regulates TP53 Acetylation; Regulation of TP53 Activity through Acetylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P78356](https://www.uniprot.org/uniprotkb/P78356) (Phosphatidylinositol 5-phosphate 4-kinase type-2 beta):

> Participates in the biosynthesis of phosphatidylinositol 4,5-bisphosphate. Preferentially utilizes GTP, rather than ATP, for PI(5)P phosphorylation and its activity reflects changes in direct proportion to the physiological GTP concentration. Its GTP-sensing activity is critical for metabolic adaptation. PIP4Ks negatively regulate insulin signaling through a catalytic-independent mechanism. They interact with PIP5Ks and suppress PIP5K-mediated PtdIns(4,5)P2 synthesis and insulin-dependent …

**Summary**, from NCBI Gene [8396](https://www.ncbi.nlm.nih.gov/gene/8396):

> The protein encoded by this gene catalyzes the phosphorylation of phosphatidylinositol-5-phosphate on the fourth hydroxyl of the myo-inositol ring to form phosphatidylinositol-5,4-bisphosphate. This gene is a member of the phosphatidylinositol-5-phosphate 4-kinase family. The encoded protein sequence does not show similarity to other kinases, but the protein does exhibit kinase activity. Additionally, the encoded protein interacts with p55 TNF receptor. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8998](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8998) · Entrez [8396](https://www.ncbi.nlm.nih.gov/gene/8396) · UniProt [P78356](https://www.uniprot.org/uniprotkb/P78356) · Ensembl [ENSG00000276293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276293)

## Data

Gene col 15873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15873); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15873]; `tensor/DDL_lfc|DDL_z.npy` [15873]; `embed/gene_vectors.npy` [15873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15873 or target_col == 15873). Every well: [[PIP4K2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP4K2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
