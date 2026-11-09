---
symbol: "PDE4A"
type: "gene"
col: 813
ensembl_id: "ENSG00000065989"
name: "phosphodiesterase 4A"
location: "19p13.2"
module: 100
arm: "+"
pooled_cpm: 11.2
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 16
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# PDE4A

*phosphodiesterase 4A* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.87× (z +23.7, q 0e+00, up in 31 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.544× (z -9.7, q 1e-19, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRTN]] (+0.62, fdr 1e-05), [[HAPLN3]] (+0.59, fdr 6e-05), [[PPP3R1]] (+0.57, fdr 5e-05); moves opposite to [[HERC2P9-1]] (-0.48, fdr 8e-05), [[LINC00630]] (-0.48, fdr 6e-05), [[ZNF254]] (-0.47, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GATA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +23.7 | 0e+00 | 31/38 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +12.7 | 1e-34 | 34/41 (NCI-H2030, BT-474, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +9.6 | 2e-19 | 29/40 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.79×** | +9.3 | 2e-18 | 25/41 (NCI-H1792, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +7.8 | 9e-13 | 21/39 (A-172, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +6.5 | 6e-09 | 18/38 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.1 | 1e-07 | 7/20 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +6.0 | 2e-07 | 18/41 (NCI-H2030, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +4.7 | 2e-04 | 10/41 (NCI-H2030, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.4 | 6e-04 | 16/38 (A498, C32, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 7e-04 | 8/37 (SW480, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.002 | 6/39 (HOP62, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 10/41 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.003 | 7/41 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.0 | 0.003 | 12/31 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.005 | 7/41 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.012 | 3/41 (SW480, A-172, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -9.7 | 1e-19 | 24/41 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -8.7 | 8e-16 | 25/41 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.617×** | -7.7 | 2e-12 | 23/39 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.621×** | -7.6 | 4e-12 | 22/40 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.620×** | -7.2 | 6e-11 | 25/39 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.678×** | -6.2 | 5e-08 | 25/41 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -6.0 | 1e-07 | 17/40 (SW480, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.700×** | -5.7 | 9e-07 | 18/41 (RPMI-7951, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -5.3 | 6e-06 | 19/40 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -5.0 | 3e-05 | 19/40 (LS 180, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.741×** | -4.8 | 8e-05 | 15/40 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.737×** | -4.7 | 1e-04 | 17/40 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.769×** | -4.2 | 0.001 | 10/41 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.784×** | -3.9 | 0.004 | 10/41 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.788×** | -3.8 | 0.005 | 13/41 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.794×** | -3.7 | 0.008 | 10/41 (A-427, PANC-1, …) | top dose only |  |
| [[Ritonavir (drug)]] 0.05 µM |  | **0.829×** | -3.0 | 0.080 | 2/41 (SW 1271, H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.8 | 1 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.6) |
| [[A-172 (line)]] | wt | 5.61 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +13.1) | — |
| [[A-427 (line)]] | wt | 31.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.289× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 3.84 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.51× (z +10.3) | [[Temsirolimus (drug)]] 0.5 µM 0.0805× (z -9.1) |
| [[HOP62 (line)]] | alt | 9.69 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.4) | [[Bosentan (hydrate) (drug)]] 5 µM 0.198× (z -9.3) |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -9.5) |
| [[A498 (line)]] | wt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +15.1) | — |
| [[A549 (line)]] | wt | 8.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 2.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.1× (z +9.9) | — |
| [[C32 (line)]] | wt | 3.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -12.0) |
| [[H4 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0797× (z -10.3) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.383× (z -8.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[LOX-IMVI (line)]] | wt | 9.91 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.199× (z -11.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[LS 180 (line)]] | wt | 3.34 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0592× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 9.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 8.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 28.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.24× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.209× (z -8.8) |
| [[SNU-423 (line)]] | alt | 5.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRTN]] | +0.62 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[HAPLN3]] | +0.59 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[PPP3R1]] | +0.57 | +0.40 / +0.60 | both halves | 5e-05 | pathway: DARPP-32 events |
| [[KREMEN2]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[TFEB]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[CCDC28B]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[RARG]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NOL4L]] | +0.51 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[CDC42EP4]] | +0.51 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[ITGA7]] | +0.50 | +0.29 / +0.60 | both halves | 2e-04 |  |
| [[CDC42EP5]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[TMCC2]] | +0.49 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2P9-1]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[LINC00630]] | -0.48 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[ZNF254]] | -0.47 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[POU5F2]] | -0.46 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[ZNF770]] | -0.45 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[SNX19]] | -0.44 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ATXN10]] | -0.43 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[VPS45]] | -0.43 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[AP3M1]] | -0.42 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[TOP3B]] | -0.42 | -0.24 / -0.50 | both halves | 4e-04 |  |
| [[PPWD1]] | -0.41 | -0.17 / -0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[TAS2R30]] | -0.41 | -0.33 / -0.43 | both halves | 1e-04 | pathway: G alpha (i) signalling events |
| [[SMARCD1]] | -0.41 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GATA2]] | B | GATA2 activity raises PDE4A's level | lines that do not express GATA2 (8) vs lines expressing it (42) | 2.25× lower at baseline in the lines without GATA2 | 0.040 | ⚠ within organs, on part of the lines; also absent: GATA2-AS1, EFR3B |
| [[CFAP45]] | B | CFAP45 activity lowers PDE4A's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 2.10× higher at baseline in the lines without CFAP45 | 0.044 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.0, 36.9); signed map (21.1, 20.1). **Vector** length 69.5, 11.6% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +23.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +9.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +7.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -8.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -5.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,416,773-10,469,630 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DPDE2 |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 6 pathways, smallest: DARPP-32 events; Opioid Signalling; G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P27815](https://www.uniprot.org/uniprotkb/P27815) (3',5'-cyclic-AMP phosphodiesterase 4A):

> Hydrolyzes the second messenger 3',5'-cyclic AMP (cAMP), which is a key regulator of many important physiological processes.; [Isoform 1]: Efficiently hydrolyzes cAMP.; [Isoform 2]: Efficiently hydrolyzes cAMP.; [Isoform 3]: Efficiently hydrolyzes cAMP. The phosphodiesterase activity is not affected by calcium, calmodulin or cyclic GMP (cGMP) levels. Does not hydrolyze cGMP.; [Isoform 4]: Efficiently hydrolyzes cAMP.; [Isoform 6]: Efficiently hydrolyzes cAMP.; [Isoform 7]: Efficiently …

**Summary**, from NCBI Gene [5141](https://www.ncbi.nlm.nih.gov/gene/5141):

> The protein encoded by this gene belongs to the cyclic nucleotide phosphodiesterase (PDE) family, and PDE4 subfamily. This PDE hydrolyzes the second messenger, cAMP, which is a regulator and mediator of a number of cellular responses to extracellular signals. Thus, by regulating the cellular concentration of cAMP, this protein plays a key role in many important physiological processes. Alternatively spliced transcript variants encoding different isoforms have been described for this …

**Accessions** — [HGNC:8780](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8780) · Entrez [5141](https://www.ncbi.nlm.nih.gov/gene/5141) · UniProt [P27815](https://www.uniprot.org/uniprotkb/P27815) · Ensembl [ENSG00000065989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065989)

## Data

Gene col 813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 813); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 813]; `tensor/DDL_lfc|DDL_z.npy` [813]; `embed/gene_vectors.npy` [813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 813 or target_col == 813). Every well: [[PDE4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
