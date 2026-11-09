---
symbol: "MAFK"
type: "gene"
col: 12606
ensembl_id: "ENSG00000198517"
name: "MAF bZIP transcription factor K"
location: "7p22.3"
module: 2
arm: "+"
pooled_cpm: 49.04
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MAFK

*MAF bZIP transcription factor K* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +9.5, q 2e-18, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.513× (z -13.4, q 2e-38, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD12]] (+0.69, fdr 7e-06), [[MEGF6]] (+0.60, fdr 1e-05), [[SHC2]] (+0.60, fdr 9e-06); moves opposite to [[TIMM21]] (-0.55, fdr 1e-05), [[TOMM70]] (-0.53, fdr 1e-05), [[ASH2L]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GEM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +9.5 | 2e-18 | 30/45 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +6.3 | 9e-08 | 29/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.1 | 2e-07 | 30/46 (SW480, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.53×** | +6.1 | 2e-07 | 32/46 (SHP-77, H4, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +6.0 | 3e-07 | 27/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 4e-07 | 31/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.5 | 4e-06 | 26/45 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +5.2 | 2e-05 | 25/47 (SHP-77, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +5.0 | 3e-05 | 26/39 (SW480, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.8 | 9e-05 | 18/44 (SK-MEL-2, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.39×** | +4.7 | 1e-04 | 23/45 (CFPAC-1, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 3e-04 | 22/45 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +4.3 | 9e-04 | 23/44 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.002 | 22/45 (SW 900, SW 1271, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.002 | 21/45 (RKO, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.005 | 21/46 (hTERT-HPNE, HOP62, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.015 | 23/46 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.033 | 16/46 (BT-474, SW480, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.040 | 17/45 (SW480, HT-29, …) | two highest doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.074 | 13/46 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.513×** | -13.4 | 2e-38 | 38/46 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.709×** | -4.7 | 7e-04 | 24/47 (NCI-H23, NCI-H460, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.561×** | -4.3 | 0.003 | 23/46 (LoVo, RPMI-7951, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -4.2 | 0.004 | 23/46 (LOX-IMVI, AsPC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.740×** | -4.1 | 0.004 | 21/46 (hTERT-HPNE, NCI-H1792, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.588×** | -3.9 | 0.007 | 24/46 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.591×** | -3.9 | 0.007 | 19/46 (Hs 766T, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.739×** | -3.9 | 0.008 | 20/47 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.756×** | -3.8 | 0.008 | 21/47 (NCI-H1573, SW 1088, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.767×** | -3.8 | 0.009 | 22/46 (SW 1271, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **0.770×** | -3.7 | 0.011 | 22/46 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.783×** | -3.5 | 0.024 | 17/46 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.635×** | -3.4 | 0.032 | 21/46 (A549, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.060 | 16/46 (NCI-H1573, SW 900, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.802×** | -3.1 | 0.065 | 21/46 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.808×** | -3.0 | 0.086 | 21/46 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 140 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -18.2) |
| [[A498 (line)]] | wt | 25.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.9) | — |
| [[A549 (line)]] | wt | 128 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -18.6) |
| [[HepG2_C3A (line)]] | wt | 46.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -14.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 46.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 2 | — | [[Belzutifan (drug)]] 5 µM 0.0507× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 129 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -9.8) |
| [[SW480 (line)]] | alt | 33.1 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.95× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -8.8) |
| [[C32 (line)]] | wt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 44.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -13.4) |
| [[H4 (line)]] | wt | 86.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 47.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 45.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.0) |
| [[J82 (line)]] | alt | 30.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.4) | — |
| [[KATO III (line)]] | alt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 46.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 49.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -9.9) |
| [[PANC-1 (line)]] | alt | 64.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 44.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.3) |
| [[SNU-423 (line)]] | alt | 50.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -10.3) |
| [[SW48 (line)]] | wt | 44.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.0) |
| [[A-172 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD12]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[MEGF6]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SHC2]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[GDI1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[JOSD1]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[R3HDM4]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CDKN2B]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CD55]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ZMIZ2]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[KLHL21]] | +0.54 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[PIM1]] | +0.54 | +0.49 / +0.57 | both halves | 2e-05 |  |
| [[CHMP1B]] | +0.54 | +0.46 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM21]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TOMM70]] | -0.53 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ASH2L]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 | pathway: Affinity selection of immunoglobulins |
| [[TDRD3]] | -0.51 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[LIN9]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[NUP54]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[PDSS2]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MTREX]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[CNPY2]] | -0.49 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[SMARCAD1]] | -0.48 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[NUP35]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[FANCM]] | -0.47 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GEM]] | B | GEM activity raises MAFK's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without GEM | 0.010 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[IGFN1]] | B | IGFN1 activity raises MAFK's level | lines that do not express IGFN1 (36) vs lines expressing it (14) | 1.88× lower at baseline in the lines without IGFN1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GLYATL2, LINC01411, PSG9 |
| [[FAM107B]] | B | FAM107B activity raises MAFK's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without FAM107B | 0.037 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[IER3]] | B | IER3 activity raises MAFK's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without IER3 | 0.037 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[NR3C1]] | B | NR3C1 activity lowers MAFK's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[RAB27B]] | B | RAB27B activity raises MAFK's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without RAB27B | 0.092 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (20.4, -1.1); signed map (-4.9, 24.7). **Vector** length 122, 34.1% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +4.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.1 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -13.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.5 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | MAF bZIP transcription factor K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,530,702-1,543,043 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P18, NFE2U |
| Gene groups (HGNC) | Small MAF bZIP transcription factor family |
| Reactome | 25 pathways, smallest: NFE2L2 regulating ER-stress associated genes; Regulation of HMOX1 expression and activity; NFE2L2 regulating inflammation associated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O60675](https://www.uniprot.org/uniprotkb/O60675) (Transcription factor MafK):

> Since they lack a putative transactivation domain, the small Mafs behave as transcriptional repressors when they dimerize among themselves. However, they act as transcriptional activators by dimerizing with other (usually larger) basic-zipper proteins, such as NFE2, NFE2L1/NRF1, NFE2L2/NRF2 and NFE2L3/NRF3, and recruiting them to specific DNA-binding sites. Small Maf proteins heterodimerize with Fos and may act as competitive repressors of the NF-E2 transcription factor.

**Summary**, from NCBI Gene [7975](https://www.ncbi.nlm.nih.gov/gene/7975):

> The developmentally regulated expression of the globin genes depends on upstream regulatory elements termed locus control regions (LCRs). LCRs are associated with powerful enhancer activity that is mediated by the transcription factor NFE2 (nuclear factor erythroid-2). NFE2 recognition sites are also present in the gene promoters of 2 heme biosynthetic enzymes, porphobilinogen deaminase (PBGD; MIM 609806) and ferrochelatase (FECH; MIM 612386). NFE2 DNA-binding activity consists of a heterodimer …

**Accessions** — [HGNC:6782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6782) · Entrez [7975](https://www.ncbi.nlm.nih.gov/gene/7975) · UniProt [O60675](https://www.uniprot.org/uniprotkb/O60675) · Ensembl [ENSG00000198517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198517)

## Data

Gene col 12606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12606); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12606]; `tensor/DDL_lfc|DDL_z.npy` [12606]; `embed/gene_vectors.npy` [12606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12606 or target_col == 12606). Every well: [[MAFK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAFK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
