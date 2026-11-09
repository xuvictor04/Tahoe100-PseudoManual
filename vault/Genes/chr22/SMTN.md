---
symbol: "SMTN"
type: "gene"
col: 11476
ensembl_id: "ENSG00000183963"
name: "smoothelin"
location: "22q12.2"
module: 81
arm: "+"
pooled_cpm: 40.72
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# SMTN

*smoothelin* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +9.1, q 6e-17, up in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.67× (z +7.3, q 1e-10, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.640× (z -6.1, q 7e-07, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDLIM7]] (+0.67, fdr 7e-06), [[PNP]] (+0.63, fdr 7e-06), [[STC1]] (+0.62, fdr 9e-06); moves opposite to [[KCTD3]] (-0.50, fdr 2e-05), [[FIGN]] (-0.49, fdr 3e-05), [[MBNL2]] (-0.48, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[BCL2A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.58×** | +9.1 | 6e-17 | 30/48 (A498, RKO, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +7.3 | 1e-10 | 32/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.54×** | +6.1 | 2e-07 | 28/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +5.0 | 7e-05 | 24/48 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.6 | 4e-04 | 24/49 (A498, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.38×** | +4.6 | 4e-04 | 21/48 (SW1417, HT-29, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +4.5 | 4e-04 | 21/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +4.3 | 9e-04 | 21/48 (SW1417, KATO III, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 9e-04 | 20/47 (PANC-1, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +4.2 | 0.002 | 20/47 (SW 900, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 22/48 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +3.9 | 0.004 | 20/48 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +3.9 | 0.004 | 20/48 (PANC-1, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +3.5 | 0.021 | 22/48 (SW1417, KATO III, …) | rises with dose | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.026 | 16/48 (SW48, HCT15, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.028 | 16/48 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.082 | 12/48 (Hs 766T, PANC-1, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.095 | 13/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.640×** | -6.1 | 7e-07 | 27/47 (RKO, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.666×** | -5.8 | 2e-06 | 27/48 (RKO, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.713×** | -4.4 | 0.002 | 25/48 (RKO, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.746×** | -4.2 | 0.004 | 19/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.781×** | -4.1 | 0.004 | 22/48 (RKO, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.827×** | -3.8 | 0.012 | 18/48 (NCI-H1573, H4, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.771×** | -3.7 | 0.018 | 18/48 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.779×** | -3.5 | 0.028 | 16/49 (RKO, HS-578T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.035 | 19/48 (RKO, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.749×** | -3.4 | 0.036 | 15/47 (RKO, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.055 | 19/48 (NCI-H1573, H4, …) | rises with dose | position effect removed |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **0.796×** | -3.2 | 0.057 | 14/48 (SNU-423, A549, …) | inconsistent across doses |  |
| [[Encorafenib (drug)]] 5 µM |  | **0.652×** | -3.2 | 0.065 | 10/48 (RKO, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.801×** | -3.1 | 0.065 | 15/48 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.795×** | -3.1 | 0.065 | 18/48 (HOP62, SW 1088, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 55.6 | 7 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +13.5) | — |
| [[KATO III (line)]] | alt | 28.7 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.06× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 98.0 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -13.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 167 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.9) ⚠ cell-cycle shift, explains ~27% of this change | [[Selinexor (drug)]] 5 µM 0.457× (z -11.4) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.323× (z -11.2) |
| [[A498 (line)]] | wt | 34.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +19.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HepG2_C3A (line)]] | wt | 54.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +13.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.27× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 103 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.350× (z -8.5) |
| [[SW480 (line)]] | alt | 48.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 13.1 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | [[Menadione (drug)]] 0.05 µM 0.0828× (z -9.5) |
| [[HT-29 (line)]] | alt | 22.1 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.59× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 33.7 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +11.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 40.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 29.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SW48 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM7]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS; STRING 652 |
| [[PNP]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[STC1]] | +0.62 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TMEM132A]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SEMA7A]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.60 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CALM1]] | +0.59 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[LRWD1]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ADGRL1-AS1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TMEM158]] | +0.58 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PAEP]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD3]] | -0.50 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[FIGN]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MBNL2]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZZZ3]] | -0.48 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[RPRD2]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MRPS30]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2A1]] | B | BCL2A1 activity raises SMTN's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without BCL2A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[STC1]] | B | STC1 activity raises SMTN's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without STC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[MEG3]] | B | MEG3 activity raises SMTN's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 1.59× lower at baseline in the lines without MEG3 | 0.043 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[TMEM158]] | B | TMEM158 activity raises SMTN's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.47× lower at baseline in the lines without TMEM158 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[MIR493HG]] | B | MIR493HG activity raises SMTN's level | lines that do not express MIR493HG (36) vs lines expressing it (14) | 1.60× lower at baseline in the lines without MIR493HG | 0.048 | ⚠ within organs, on part of the lines; also absent: MEG3, MEG8, ENSG00000232252 |
| [[LFNG]] | B | LFNG activity strengthens SMTN's drug response | lines that do not express LFNG (14) vs lines expressing it (35) | the lines without LFNG respond 0.59× as strongly (z diff +1.25); strongest at Homoharringtonine 5 µM: 0.99x vs 1.80x (z diff +4.6) | 0.058 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity raises SMTN's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[DPF3]] | B | DPF3 activity raises SMTN's level | lines that do not express DPF3 (13) vs lines expressing it (37) | 1.77× lower at baseline in the lines without DPF3 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000267175, RNF152, RORA; maybe low, not absent |
| [[STX1A]] | C | STX1A activity raises SMTN's level | lines that do not express STX1A (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without STX1A | 0.089 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 1.8); signed map (2.5, 47.7). **Vector** length 119, 32.2% of its response variance represented; |z| ≥ 3 in 1,262 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.2 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +4.6 | +2.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.6 | +4.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.1 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +4.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.8 | +4.3 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.3 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.5 | -4.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | smoothelin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:31,064,105-31,104,757 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P53814](https://www.uniprot.org/uniprotkb/P53814) (Smoothelin):

> Structural protein of the cytoskeleton.

**Summary**, from NCBI Gene [6525](https://www.ncbi.nlm.nih.gov/gene/6525):

> This gene encodes a structural protein that is found exclusively in contractile smooth muscle cells. It associates with stress fibers and constitutes part of the cytoskeleton. This gene is localized to chromosome 22q12.3, distal to the TUPLE1 locus and outside the DiGeorge syndrome deletion. Alternative splicing of this gene results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:11126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11126) · Entrez [6525](https://www.ncbi.nlm.nih.gov/gene/6525) · UniProt [P53814](https://www.uniprot.org/uniprotkb/P53814) · Ensembl [ENSG00000183963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183963)

## Data

Gene col 11476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11476); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11476]; `tensor/DDL_lfc|DDL_z.npy` [11476]; `embed/gene_vectors.npy` [11476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11476 or target_col == 11476). Every well: [[SMTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
