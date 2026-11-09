---
symbol: "LMLN"
type: "gene"
col: 11703
ensembl_id: "ENSG00000185621"
name: "leishmanolysin like peptidase"
location: "3q29"
module: 28
arm: "+"
pooled_cpm: 26.5
n_lines_expressing: 48
n_dd_up: 26
n_dd_down: 15
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# LMLN

*leishmanolysin like peptidase* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +14.8, q 0e+00, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.433× (z -11.8, q 3e-29, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DARS1]] (+0.65, fdr 7e-06), [[FCF1]] (+0.61, fdr 1e-05), [[WASHC3]] (+0.59, fdr 1e-05); moves opposite to [[MCOLN2]] (-0.56, fdr 3e-05), [[ZNF341]] (-0.54, fdr 2e-05), [[PALS2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BHLHE41]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 1 with an alert ⚠; shown: the 15 strongest. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +14.8 | 0e+00 | 36/45 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +9.1 | 3e-17 | 36/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +8.7 | 6e-16 | 35/46 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +7.9 | 4e-13 | 36/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.4 | 2e-08 | 25/46 (BT-474, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +5.3 | 1e-05 | 24/46 (BT-474, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.0 | 5e-05 | 24/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 5e-05 | 22/46 (BT-474, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.9 | 6e-05 | 24/46 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 1e-04 | 20/45 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.3 | 9e-04 | 23/45 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +4.2 | 0.001 | 15/46 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 27/46 (KATO III, LoVo, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 22/46 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.003 | 20/45 (HOP62, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.433×** | -11.8 | 3e-29 | 37/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.493×** | -9.9 | 7e-21 | 39/44 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.548×** | -8.5 | 5e-15 | 31/46 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.558×** | -8.2 | 3e-14 | 33/46 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -6.6 | 6e-09 | 26/45 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -5.5 | 3e-06 | 25/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.759×** | -5.5 | 4e-06 | 26/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.681×** | -5.4 | 5e-06 | 24/46 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.712×** | -4.8 | 1e-04 | 25/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -4.4 | 7e-04 | 23/46 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.767×** | -3.7 | 0.011 | 23/46 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Pimozide (drug)]] 5 µM |  | **0.773×** | -3.6 | 0.015 | 12/46 (Panc 03.27, SNU-423, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.015 | 22/46 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.777×** | -3.5 | 0.016 | 20/46 (SW 1088, CHP-212, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.800×** | -3.1 | 0.069 | 16/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 41.1 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.5) | [[Digitoxin (drug)]] 5 µM 0.254× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.272× (z -14.2) |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0860× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 67.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.307× (z -10.5) |
| [[A498 (line)]] | wt | 8.13 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +10.4) | — |
| [[H4 (line)]] | wt | 43.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 31.3 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +13.6) | [[Digitoxin (drug)]] 0.5 µM 0.244× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 21.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.225× (z -11.7) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.314× (z -9.4) |
| [[C32 (line)]] | wt | 35.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0570× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.261× (z -8.7) |
| [[HCT15 (line)]] | alt | 31.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.149× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 18.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.4) | — |
| [[J82 (line)]] | alt | 26.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.261× (z -9.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 16.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.274× (z -8.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 32.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.218× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 14.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +10.5) | — |
| [[SW480 (line)]] | alt | 33.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.9) | [[Digitoxin (drug)]] 0.5 µM 0.289× (z -11.5) |
| [[BT-474 (line)]] | alt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 25.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.207× (z -9.2) |
| [[KATO III (line)]] | alt | 32.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 38.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS1]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[FCF1]] | +0.61 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[WASHC3]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[DZIP3]] | +0.59 | +0.77 / +0.40 | both halves | 5e-05 |  |
| [[LZIC]] | +0.59 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[ZNF429]] | +0.58 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[USP40]] | +0.58 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[KDM4C]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MCPH1-AS1]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SCAPER]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RBKS]] | +0.56 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[FANK1]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCOLN2]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ZNF341]] | -0.54 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[PALS2]] | -0.54 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[TOMM5]] | -0.54 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[ARHGEF26]] | -0.53 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[TRABD]] | -0.52 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[CMTM4]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[EEF1E1]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[SLC41A3]] | -0.51 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[UNC5A]] | -0.51 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[CPSF4]] | -0.50 | -0.68 / -0.32 | both halves | 2e-04 |  |
| [[PACC1]] | -0.50 | -0.61 / -0.40 | both halves | 5e-05 | STRING 481 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | B | BHLHE41 activity raises LMLN's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without BHLHE41 | 0.014 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[TOP2A]] | B | TOP2A activity lowers LMLN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EFCAB6]] | B | EFCAB6 activity raises LMLN's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without EFCAB6 | 0.044 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[NR2F2-AS1]] | B | NR2F2-AS1 activity raises LMLN's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without NR2F2-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[SESTD1]] | C | SESTD1 activity lowers LMLN's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.76× higher at baseline in the lines without SESTD1 | 0.071 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[CAVIN4]] | C | CAVIN4 activity raises LMLN's level | lines that do not express CAVIN4 (4) vs lines expressing it (46) | 2.14× lower at baseline in the lines without CAVIN4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GPR135, SYCP2L, FAM229B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.501). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.4, 8.4); signed map (10.7, -23.9). **Vector** length 89.7, 21.1% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +4.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.1 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.8 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.6 | -6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -5.5 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | leishmanolysin like peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,960,200-198,043,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Gp63, Msp, LMNL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KR4](https://www.uniprot.org/uniprotkb/Q96KR4) (Leishmanolysin-like peptidase):

> Metalloprotease.

**Summary**, from NCBI Gene [89782](https://www.ncbi.nlm.nih.gov/gene/89782):

> This gene encodes a zinc-metallopeptidase. The encoded protein may play a role in cell migration and invasion. Studies of a similar protein in Drosophila indicate a potential role in mitotic progression. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:15991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15991) · Entrez [89782](https://www.ncbi.nlm.nih.gov/gene/89782) · UniProt [Q96KR4](https://www.uniprot.org/uniprotkb/Q96KR4) · Ensembl [ENSG00000185621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185621)

## Data

Gene col 11703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11703); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11703]; `tensor/DDL_lfc|DDL_z.npy` [11703]; `embed/gene_vectors.npy` [11703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11703 or target_col == 11703). Every well: [[LMLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
