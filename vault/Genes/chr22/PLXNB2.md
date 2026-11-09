---
symbol: "PLXNB2"
type: "gene"
col: 12240
ensembl_id: "ENSG00000196576"
name: "plexin B2"
location: "22q13.33"
module: 14
arm: "+"
pooled_cpm: 56.69
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PLXNB2

*plexin B2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +10.4, q 2e-22, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.459× (z -11.5, q 6e-28, down in 42 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.478× (z -10.9, q 3e-25, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL3]] (+0.67, fdr 7e-06), [[PRR14]] (+0.66, fdr 7e-06), [[ACP2]] (+0.66, fdr 7e-06); moves opposite to [[GSTO1]] (-0.61, fdr 1e-05), [[UQCRH]] (-0.61, fdr 1e-05), [[RABEPK]] (-0.59, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ANO9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +10.4 | 2e-22 | 33/46 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.0 | 6e-10 | 31/44 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.0 | 6e-10 | 27/38 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +5.6 | 3e-06 | 29/46 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.6 | 5e-04 | 25/46 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +4.3 | 0.002 | 22/39 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.9 | 0.009 | 23/44 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +3.7 | 0.015 | 19/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.068 | 22/46 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.084 | 13/46 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.096 | 19/46 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.100 | 15/45 (AsPC-1, C-33 A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.459×** | -11.5 | 6e-28 | 42/46 (LoVo, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -10.9 | 3e-25 | 41/46 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.513×** | -9.9 | 1e-20 | 44/46 (C32, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -8.7 | 6e-16 | 28/47 (HT-29, HCT15, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.546×** | -8.4 | 3e-15 | 42/46 (HT-29, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.358×** | -8.0 | 2e-13 | 37/42 (Hs 766T, SW 900, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.596×** | -7.6 | 2e-12 | 34/46 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -6.9 | 5e-10 | 34/46 (HCT15, HT-29, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.631×** | -6.5 | 4e-09 | 41/46 (HS-578T, C32, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.648×** | -6.4 | 9e-09 | 36/46 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.686×** | -5.3 | 5e-06 | 24/44 (Hs 766T, BT-474, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -4.9 | 4e-05 | 31/46 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.734×** | -4.5 | 2e-04 | 29/46 (HepG2/C3A, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.588×** | -4.1 | 0.002 | 23/47 (C32, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.699×** | -3.8 | 0.006 | 21/47 (HOP62, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.795×** | -3.3 | 0.029 | 21/45 (A-427, SW1417, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.803×** | -3.2 | 0.044 | 14/46 (SW48, LS 180, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.862× | -3.0 | 0.074 | 14/47 (NCI-H1573, CFPAC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 88.1 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -18.0) |
| [[Hs 766T (line)]] | wt | 95.7 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 59.5 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.237× (z -12.3) |
| [[SW 900 (line)]] | alt | 55.1 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -10.8) |
| [[COLO 205 (line)]] | alt | 59.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 77.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +15.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.9) |
| [[KATO III (line)]] | alt | 71.0 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -12.3) |
| [[SW480 (line)]] | alt | 43.3 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -13.9) |
| [[A498 (line)]] | wt | 79.2 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.170× (z -10.1) ⚠ toxic · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.380× (z -9.9) |
| [[C32 (line)]] | wt | 111 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -12.9) |
| [[HOP62 (line)]] | alt | 66.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.1) | [[Bortezomib (drug)]] 0.05 µM 0.301× (z -10.6) |
| [[LoVo (line)]] | wt | 63.1 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 36.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -9.3) |
| [[A549 (line)]] | wt | 41.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 55.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 100.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -10.5) |
| [[HCT15 (line)]] | alt | 99.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -15.2) |
| [[LS 180 (line)]] | wt | 110 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 37.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 64.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.5) |
| [[PANC-1 (line)]] | alt | 38.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -8.6) |
| [[SNU-423 (line)]] | alt | 43.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.5) | — |
| [[SW48 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.265× (z -10.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 88.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -12.2) |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 54.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 65.4 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.388× (z -8.6) |
| [[J82 (line)]] | alt | 48.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 70.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 37.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 73.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.4) |
| [[SW1417 (line)]] | alt | 56.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -8.8) |
| [[A-172 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL3]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PRR14]] | +0.66 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ACP2]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[AGRN]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS; STRING 512 |
| [[MED12]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[TRIP6]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[SRRM2]] | +0.62 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[AJUBA]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CIC]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[SLC39A1]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CNOT3]] | +0.61 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTO1]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.61 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RABEPK]] | -0.59 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.57 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[DAP3]] | -0.56 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[MAP2K1]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[CUTC]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[ANKRD39]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PWWP3A]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[QPCTL]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SNRPD2]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO9]] | B | ANO9 activity raises PLXNB2's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.79× lower at baseline in the lines without ANO9 | 0.006 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[ANO9]] | B | ANO9 activity strengthens PLXNB2's drug response | lines that do not express ANO9 (20) vs lines expressing it (27) | the lines without ANO9 respond 0.70× as strongly (z diff +1.14); strongest at Idarubicin (hydrochloride) 5 µM: 0.71x vs 0.59x (z diff +2.6) | 0.033 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29; target measured in part of the lines; artifact flags |
| [[KRT80]] | B | KRT80 activity raises PLXNB2's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 1.62× lower at baseline in the lines without KRT80 | 0.050 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[STAT5A]] | B | STAT5A activity raises PLXNB2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without STAT5A | 0.078 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[SPATA18]] | B | SPATA18 activity raises PLXNB2's level | lines that do not express SPATA18 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without SPATA18 | 0.089 | ⚠ within organs, on part of the lines; also absent: GPRIN2, MUC5AC, SIDT1 |
| [[EPS8L2]] | B | EPS8L2 activity raises PLXNB2's level | lines that do not express EPS8L2 (19) vs lines expressing it (31) | 1.58× lower at baseline in the lines without EPS8L2 | 0.092 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[KRT80]] | B | KRT80 activity strengthens PLXNB2's drug response | lines that do not express KRT80 (20) vs lines expressing it (27) | the lines without KRT80 respond 0.70× as strongly (z diff +1.00); strongest at Panobinostat 0.5 µM: 0.55x vs 0.41x (z diff +2.7) | 0.097 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2; target measured in part of the lines; artifact flags |
| [[COL16A1]] | B | COL16A1 activity raises PLXNB2's level | lines that do not express COL16A1 (18) vs lines expressing it (32) | 1.18× lower at baseline in the lines without COL16A1 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02220, ENSG00000253227, IL2RG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.7, 3.7); signed map (11.9, -18.0). **Vector** length 136, 42.3% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.9 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.1 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.6 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.3 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +5.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +4.6 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.6 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.5 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.3 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.5 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.4 | -6.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.6 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -6.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.3 | -6.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | plexin B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,274,979-50,307,646 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MM1, KIAA0315, PLEXB2, lncFAL |
| Gene groups (HGNC) | Plexins; IPT domain containing |
| Hallmark sets | MYOGENESIS, P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [O15031](https://www.uniprot.org/uniprotkb/O15031) (Plexin-B2):

> Cell surface receptor for SEMA4C, SEMA4D and SEMA4G that plays an important role in cell-cell signaling (By similarity). Plays a role in glutamatergic synapse development and is required for SEMA4A-mediated excitatory synapse development (By similarity). Binding to class 4 semaphorins promotes downstream activation of RHOA and phosphorylation of ERBB2 at 'Tyr-1248' (By similarity). Also acts as a cell surface receptor for angiogenin (ANG); promoting ANG endocytosis and translocation to the …

**Summary**, from NCBI Gene [23654](https://www.ncbi.nlm.nih.gov/gene/23654):

> Members of the B class of plexins, such as PLXNB2 are transmembrane receptors that participate in axon guidance and cell migration in response to semaphorins (Perrot et al. (2002) [PubMed 12183458]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:9104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9104) · Entrez [23654](https://www.ncbi.nlm.nih.gov/gene/23654) · UniProt [O15031](https://www.uniprot.org/uniprotkb/O15031) · Ensembl [ENSG00000196576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196576)

## Data

Gene col 12240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12240); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12240]; `tensor/DDL_lfc|DDL_z.npy` [12240]; `embed/gene_vectors.npy` [12240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12240 or target_col == 12240). Every well: [[PLXNB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLXNB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
