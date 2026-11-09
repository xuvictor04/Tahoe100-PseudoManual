---
symbol: "PROSER2"
type: "gene"
col: 7282
ensembl_id: "ENSG00000148426"
name: "proline and serine rich 2"
location: "10p14"
module: 31
arm: "+"
pooled_cpm: 31.27
n_lines_expressing: 36
n_dd_up: 17
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 19
direction_downstream: 13
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# PROSER2

*proline and serine rich 2* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.42× (z +7.6, q 2e-11, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.414× (z -18.8, q 0e+00, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC9]] (+0.62, fdr 7e-06), [[CRYBG2]] (+0.60, fdr 1e-05), [[GJB3]] (+0.60, fdr 1e-05); moves opposite to [[EFCAB2]] (-0.56, fdr 1e-04), [[PRKAR1A]] (-0.54, fdr 3e-05), [[ZFP91]] (-0.51, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[FA2H]] → it (grade B ⚠); 13 go from it, the strongest it → [[PCDH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7282.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.42×** | +7.6 | 2e-11 | 19/34 (HT-29, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.56×** | +6.8 | 4e-09 | 18/32 (HT-29, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +5.8 | 1e-06 | 20/34 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +5.7 | 2e-06 | 17/34 (HT-29, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.5 | 3e-06 | 12/34 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **1.25×** | +4.9 | 1e-04 | 11/34 (J82, A549, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +4.7 | 2e-04 | 14/33 (HT-29, SW480, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +4.5 | 6e-04 | 14/33 (HT-29, LS 180, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.002 | 16/32 (Panc 03.27, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.0 | 0.003 | 12/31 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.010 | 7/33 (J82, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.012 | 12/34 (HT-29, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.019 | 13/31 (HT-29, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.26×** | +3.3 | 0.036 | 7/32 (HT-29, KATO III, …) | all doses, flat |  |
| [[Neratinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.036 | 11/33 (NCI-H460, A-172, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.043 | 10/32 (HT-29, COLO 205, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7282.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.414×** | -18.8 | 0e+00 | 27/31 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.395×** | -14.0 | 4e-42 | 25/28 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.563×** | -12.2 | 4e-32 | 23/34 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.452×** | -12.0 | 6e-31 | 24/34 (AsPC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.455×** | -11.4 | 4e-28 | 22/24 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.495×** | -10.2 | 2e-22 | 30/33 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -8.8 | 2e-16 | 30/33 (Panc 03.27, A-427, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.671×** | -8.5 | 2e-15 | 25/34 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.572×** | -8.1 | 4e-14 | 22/34 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.603×** | -7.6 | 2e-12 | 22/33 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.663×** | -6.2 | 3e-08 | 21/34 (AsPC-1, Panc 03.27, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -5.4 | 4e-06 | 2/35 (HOP62, SW 900) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.713×** | -4.7 | 1e-04 | 18/26 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.807×** | -4.5 | 2e-04 | 18/34 (J82, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.758×** | -4.2 | 0.001 | 11/34 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.775×** | -3.8 | 0.005 | 14/33 (HCT15, LoVo, …) | top dose only |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.046 | 7/34 (SW 1271, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7282. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 57.4 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -23.6) |
| [[AsPC-1 (line)]] | alt | 195 | 1 | 9 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 7.29× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -28.6) |
| [[Panc 03.27 (line)]] | alt | 85.6 | 1 | 9 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 7.14× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -21.2) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -26.2) |
| [[HEC-1-A (line)]] | alt | 70.6 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -23.6) |
| [[HT-29 (line)]] | alt | 43.7 | 6 (2 ⚠) | 3 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 4.16× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -17.1) |
| [[SW480 (line)]] | alt | 26.1 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.04× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0713× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -17.5) |
| [[HCT15 (line)]] | alt | 78.1 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -12.2) |
| [[LoVo (line)]] | wt | 46.9 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.70× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -17.6) |
| [[A549 (line)]] | wt | 46.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -15.2) |
| [[J82 (line)]] | alt | 45.1 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.8) |
| [[BT-474 (line)]] | alt | 43.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 51.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0871× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -15.3) |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -19.1) |
| [[A-172 (line)]] | wt | 25.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -12.2) |
| [[Hs 766T (line)]] | wt | 29.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.2) |
| [[KATO III (line)]] | alt | 24.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -13.8) |
| [[A-427 (line)]] | wt | 16.4 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0897× (z -13.7) |
| [[SNU-1 (line)]] | wt | 36.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.3) |
| [[A498 (line)]] | wt | 24.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.267× (z -8.6) |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.270× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -9.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -8.9) |
| [[AN3 CA (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.49 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7282), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CRYBG2]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GJB3]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SEMA3B]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[GIPC1]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PROSER2-AS1]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DENND2C]] | +0.56 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[HMOX2]] | +0.55 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[GPRC5A]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CBLC]] | +0.55 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[CRLF3]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[WNT7A]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[FNBP1L]] | +0.55 | +0.61 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.56 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[PRKAR1A]] | -0.54 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ZFP91]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[RCBTB2]] | -0.51 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[USP11]] | -0.50 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[DCAF8]] | -0.50 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[SPART-AS1]] | -0.50 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[UBAP2L]] | -0.49 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[CASD1]] | -0.48 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[MLH1]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TIA1]] | -0.47 | -0.57 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 19, C 0. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FA2H]] | B | FA2H activity raises PROSER2's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without FA2H | 0.003 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[IRF6]] | B | IRF6 activity raises PROSER2's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without IRF6 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[PCDH1]] | B | PCDH1 activity raises PROSER2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.66× lower at baseline in the lines without PCDH1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[IFNLR1]] | B | IFNLR1 activity raises PROSER2's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without IFNLR1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2 |
| [[TOP2A]] | B | TOP2A activity raises PROSER2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYO5B]] | B | MYO5B activity raises PROSER2's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.44× lower at baseline in the lines without MYO5B | 0.022 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[PRSS3]] | B | PRSS3 activity raises PROSER2's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without PRSS3 | 0.027 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[SEMA3B]] | B | SEMA3B activity raises PROSER2's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.99× lower at baseline in the lines without SEMA3B | 0.028 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[PTK2B]] | B | PTK2B activity raises PROSER2's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 3.18× lower at baseline in the lines without PTK2B | 0.028 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CAPG]] | B | CAPG activity raises PROSER2's level | lines that do not express CAPG (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without CAPG | 0.032 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[FA2H]] | B | FA2H activity strengthens PROSER2's drug response | lines that do not express FA2H (15) vs lines expressing it (19) | the lines without FA2H respond 0.63× as strongly (z diff +2.11); strongest at Panobinostat 0.5 µM: 0.52x vs 0.31x (z diff +3.3) | 0.033 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2; target measured in part of the lines; artifact flags |
| [[KCNK1]] | B | KCNK1 activity raises PROSER2's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.67× lower at baseline in the lines without KCNK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | B | PROSER2 activity raises PCDH1's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without PROSER2 | 0.002 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[RRAS2]] | B | PROSER2 activity raises RRAS2's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without PROSER2 | 0.003 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[CORO2A]] | B | PROSER2 activity raises CORO2A's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without PROSER2 | 0.009 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[CAPG]] | B | PROSER2 activity raises CAPG's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without PROSER2 | 0.022 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[FLNB]] | B | PROSER2 activity raises FLNB's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.84× lower at baseline in the lines without PROSER2 | 0.028 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[ALS2CL]] | B | PROSER2 activity raises ALS2CL's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.33× lower at baseline in the lines without PROSER2 | 0.032 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[MFSD14CP]] | B | PROSER2 activity raises MFSD14CP's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.39× lower at baseline in the lines without PROSER2 | 0.035 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[PTK2B]] | B | PROSER2 activity raises PTK2B's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.23× lower at baseline in the lines without PROSER2 | 0.040 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[RALGPS2]] | B | PROSER2 activity raises RALGPS2's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without PROSER2 | 0.050 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[CARD11]] | B | PROSER2 activity raises CARD11's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.93× lower at baseline in the lines without PROSER2 | 0.058 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[ST6GALNAC2]] | B | PROSER2 activity raises ST6GALNAC2's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without PROSER2 | 0.062 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[PRSS3]] | B | PROSER2 activity raises PRSS3's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.96× lower at baseline in the lines without PROSER2 | 0.067 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.1, 59.6); signed map (-2.7, 38.0). **Vector** length 92.3, 23.8% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.9 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.0 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +0.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.0 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -8.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.2 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.0 | -14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -2.7 | -11.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | proline and serine rich 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:11,823,339-11,872,277 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35403; previously C10orf47 |
| Matched by | ensembl_id |

UniProt [Q86WR7](https://www.uniprot.org/uniprotkb/Q86WR7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23728) · Entrez [254427](https://www.ncbi.nlm.nih.gov/gene/254427) · UniProt [Q86WR7](https://www.uniprot.org/uniprotkb/Q86WR7) · Ensembl [ENSG00000148426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148426)

## Data

Gene col 7282: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7282); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7282, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7282]; `tensor/DDL_lfc|DDL_z.npy` [7282]; `embed/gene_vectors.npy` [7282]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7282 or target_col == 7282). Every well: [[PROSER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PROSER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
