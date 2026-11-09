---
symbol: "CCDC117"
type: "gene"
col: 8281
ensembl_id: "ENSG00000159873"
name: "coiled-coil domain containing 117"
location: "22q12.1"
module: 64
arm: "+"
pooled_cpm: 27.65
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CCDC117

*coiled-coil domain containing 117* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.16× (z +21.9, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.899× (z -6.8, q 5e-09, down in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.714× (z -6.4, q 4e-08, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJB4]] (+0.67, fdr 1e-05), [[UBXN4]] (+0.66, fdr 1e-05), [[TDP2]] (+0.65, fdr 3e-05); moves opposite to [[MSH5]] (-0.60, fdr 4e-05), [[C20orf27]] (-0.59, fdr 1e-04), [[NOMO1]] (-0.57, fdr 5e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.16×** | +21.9 | 0e+00 | 45/47 (LoVo, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +16.5 | 0e+00 | 44/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.24×** | +15.3 | 0e+00 | 39/47 (SW1417, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.11×** | +14.2 | 2e-43 | 39/48 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +10.3 | 1e-22 | 38/47 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.42×** | +9.3 | 9e-19 | 29/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +8.0 | 1e-13 | 35/47 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +7.6 | 1e-12 | 26/40 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.46×** | +7.2 | 3e-11 | 31/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.9 | 2e-10 | 29/46 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.9 | 3e-10 | 26/47 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +6.5 | 5e-09 | 31/47 (NCI-H2030, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **1.81×** | +5.9 | 1e-07 | 24/44 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.9 | 2e-07 | 20/48 (NCI-H460, A498, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Infigratinib (drug)]] 5 µM |  | **1.77×** | +5.7 | 5e-07 | 24/47 (HEC-1-A, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 2e-04 | 17/48 (NCI-H2347, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +4.2 | 7e-04 | 16/47 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.2 | 7e-04 | 19/47 (LS 180, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.899× | -6.8 | 5e-09 | 2/48 (NCI-H2030, H4) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.714×** | -6.4 | 4e-08 | 25/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.744×** | -5.6 | 4e-06 | 24/48 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.575×** | -5.5 | 5e-06 | 23/48 (SHP-77, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.768×** | -5.0 | 6e-05 | 22/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.813×** | -3.9 | 0.008 | 21/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.679×** | -3.8 | 0.010 | 14/47 (NCI-H460, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.687×** | -3.7 | 0.014 | 12/45 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.838× | -3.2 | 0.075 | 16/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | 0.733× | -3.1 | 0.11 | 10/46 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change | 0.839× | -3.1 | 0.11 | 15/40 (LoVo, SW 900, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.4 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -10.3) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -10.0) |
| [[LoVo (line)]] | wt | 31.3 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.97× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[NCI-H2347 (line)]] | alt | 17.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.11× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 15.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 3.83× (z +12.3) | — |
| [[RKO (line)]] | wt | 27.3 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.79× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 14.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +11.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.17× (z +9.9) | — |
| [[KATO III (line)]] | alt | 38.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 22.9 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +12.3) | — |
| [[NCI-H1573 (line)]] | alt | 32.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW1417 (line)]] | alt | 32.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.92× (z +12.2) | — |
| [[A498 (line)]] | wt | 59.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.457× (z -8.9) |
| [[A549 (line)]] | wt | 19.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 38.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.390× (z -8.6) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 12.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.51× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.38× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[SW480 (line)]] | alt | 24.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.60× (z +9.2) | — |
| [[A-172 (line)]] | wt | 29.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.17× (z +11.3) | — |
| [[A-427 (line)]] | wt | 27.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.66× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 21.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.16× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 34.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.19× (z +9.3) | — |
| [[C32 (line)]] | wt | 18.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.44× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 26.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.76× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 37.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.10× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 27.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.80× (z +12.6) | — |
| [[J82 (line)]] | alt | 27.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.33× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 30.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.59× (z +10.1) | — |
| [[SW48 (line)]] | wt | 30.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.45× (z +10.0) | — |
| [[AN3 CA (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB4]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.66 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[TDP2]] | +0.65 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[RNF6]] | +0.63 | +0.71 / +0.35 | both halves | 1e-04 |  |
| [[TIRAP]] | +0.63 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[MRPL18]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[RHBDD3]] | +0.60 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[UBB]] | +0.59 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[IGHMBP2]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TSSC4]] | +0.57 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[FBXO30]] | +0.57 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[DNAJA4]] | +0.56 | +0.47 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSH5]] | -0.60 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[C20orf27]] | -0.59 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[NOMO1]] | -0.57 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ARL6IP6]] | -0.56 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[EML4]] | -0.56 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[CD320]] | -0.54 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[PODXL2]] | -0.53 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[GUSB]] | -0.53 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[MAPK1]] | -0.50 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[CLYBL]] | -0.50 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[PAFAH1B3]] | -0.50 | -0.50 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[SMYD3]] | -0.50 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[GVQW3]] | -0.50 | -0.39 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CCDC117's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-19.1, 8.9); signed map (7.8, -29.5). **Vector** length 110, 27.0% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +21.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +16.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +15.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.8 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +4.5 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.6 | +5.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.6 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -6.1 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -5.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 117 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:28,772,674-28,789,301 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33814 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWD4](https://www.uniprot.org/uniprotkb/Q8IWD4) (Coiled-coil domain-containing protein 117):

> Facilitates DNA repair, cell cycle progression, and cell proliferation through its interaction with CIAO2B.

**Summary**, from NCBI Gene [150275](https://www.ncbi.nlm.nih.gov/gene/150275):

> Involved in positive regulation of DNA repair and positive regulation of cell population proliferation. Located in mitotic spindle. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26599) · Entrez [150275](https://www.ncbi.nlm.nih.gov/gene/150275) · UniProt [Q8IWD4](https://www.uniprot.org/uniprotkb/Q8IWD4) · Ensembl [ENSG00000159873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159873)

## Data

Gene col 8281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8281); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8281]; `tensor/DDL_lfc|DDL_z.npy` [8281]; `embed/gene_vectors.npy` [8281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8281 or target_col == 8281). Every well: [[CCDC117 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC117.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
