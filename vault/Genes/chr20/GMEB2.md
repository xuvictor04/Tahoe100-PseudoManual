---
symbol: "GMEB2"
type: "gene"
col: 2098
ensembl_id: "ENSG00000101216"
name: "glucocorticoid modulatory element binding protein 2"
location: "20q13.33"
module: 114
arm: "+"
pooled_cpm: 27.57
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# GMEB2

*glucocorticoid modulatory element binding protein 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.97× (z +15.7, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.452× (z -13.1, q 3e-36, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3HC1]] (+0.74, fdr 7e-06), [[GGA3]] (+0.69, fdr 1e-05), [[ZNF721]] (+0.68, fdr 1e-05); moves opposite to [[SLC39A6]] (-0.60, fdr 1e-05), [[PAPSS1]] (-0.56, fdr 2e-05), [[LDHB]] (-0.55, fdr 3e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +15.7 | 0e+00 | 41/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.32×** | +13.8 | 9e-41 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +13.0 | 1e-36 | 44/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.08×** | +12.0 | 7e-31 | 42/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.95×** | +10.9 | 8e-26 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +7.7 | 1e-12 | 31/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.7 | 1e-12 | 32/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +7.0 | 2e-10 | 34/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +6.0 | 1e-07 | 28/47 (SW480, NCI-H1573, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +5.4 | 4e-06 | 27/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +4.7 | 1e-04 | 23/48 (KATO III, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.005 | 19/48 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.008 | 16/48 (KATO III, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.011 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.018 | 11/47 (SW480, A-427, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.073 | 15/48 (LoVo, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2098.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -13.1 | 3e-36 | 45/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.510×** | -11.1 | 5e-26 | 45/48 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.533×** | -10.3 | 9e-23 | 44/48 (SW1417, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.577×** | -9.0 | 2e-17 | 32/45 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.585×** | -8.5 | 2e-15 | 25/36 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -8.1 | 4e-14 | 26/47 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.563×** | -7.7 | 2e-12 | 38/48 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -7.0 | 1e-10 | 31/46 (Panc 03.27, A-172, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -6.7 | 1e-09 | 32/48 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.470×** | -6.5 | 5e-09 | 34/48 (A498, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -5.8 | 3e-07 | 27/48 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.760×** | -4.5 | 3e-04 | 21/48 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.838× | -4.1 | 0.002 | 20/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.025 | 18/48 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.865× | -3.4 | 0.026 | 21/48 (NCI-H2347, Hs 766T, …) | top dose only | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.040 | 8/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 54.2 | 2 (1 ⚠) | 6 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.40× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.346× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 48.2 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.49× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 23.9 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.403× (z -8.5) |
| [[PANC-1 (line)]] | alt | 20.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 33.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 35.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.324× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.336× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 36.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0662× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SW480 (line)]] | alt | 28.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.6) | — |
| [[A-172 (line)]] | wt | 23.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.6) |
| [[A549 (line)]] | wt | 20.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 41.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 33.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -11.8) |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.5 µM 0.113× (z -9.4) |
| [[A498 (line)]] | wt | 26.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +14.6) | — |
| [[C32 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 24.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.7) | — |
| [[KATO III (line)]] | alt | 28.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.7) | — |
| [[LoVo (line)]] | wt | 14.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.167× (z -8.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0707× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.41× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.5) | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -10.5) |
| [[A-427 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3HC1]] | +0.74 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[GGA3]] | +0.69 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[ZNF721]] | +0.68 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[MED18]] | +0.68 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LIPT1]] | +0.68 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.67 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[DOHH]] | +0.66 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[GMEB1]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 | same gene group; STRING 860 |
| [[ZNF316]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.65 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[AFG3L1P]] | +0.64 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[SNRNP35]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A6]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[PAPSS1]] | -0.56 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[LDHB]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[ADAM10]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TMED4]] | -0.53 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[SCARB2]] | -0.53 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[MYH10]] | -0.52 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[WRNIP1]] | -0.52 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GMEB2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.0, 6.9); signed map (-2.4, -13.4). **Vector** length 69.7, 14.5% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +15.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.7 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | -8.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.9 | -0.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.8 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -7.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -6.5 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.8 | -0.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | glucocorticoid modulatory element binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,587,602-63,627,101 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P79PIF, KIAA1269, PIF79 |
| Gene groups (HGNC) | SAND domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKD1](https://www.uniprot.org/uniprotkb/Q9UKD1) (Glucocorticoid modulatory element-binding protein 2):

> Trans-acting factor that binds to glucocorticoid modulatory elements (GME) present in the TAT (tyrosine aminotransferase) promoter and increases sensitivity to low concentrations of glucocorticoids. Also binds to the transferrin receptor promoter. Essential auxiliary factor for the replication of parvoviruses.

**Summary**, from NCBI Gene [26205](https://www.ncbi.nlm.nih.gov/gene/26205):

> This gene is a member of KDWK gene family. The product of this gene associates with GMEB1 protein, and the complex is essential for parvovirus DNA replication. Study of rat homolog implicates the role of this gene in modulation of transactivation by the glucocorticoid receptor bound to glucocorticoid response elements. This gene appears to use multiple polyadenylation sites. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4371) · Entrez [26205](https://www.ncbi.nlm.nih.gov/gene/26205) · UniProt [Q9UKD1](https://www.uniprot.org/uniprotkb/Q9UKD1) · Ensembl [ENSG00000101216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101216)

## Data

Gene col 2098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2098); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2098]; `tensor/DDL_lfc|DDL_z.npy` [2098]; `embed/gene_vectors.npy` [2098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2098 or target_col == 2098). Every well: [[GMEB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMEB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
