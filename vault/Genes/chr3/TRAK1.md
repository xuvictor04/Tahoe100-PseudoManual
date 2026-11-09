---
symbol: "TRAK1"
type: "gene"
col: 11307
ensembl_id: "ENSG00000182606"
name: "trafficking kinesin protein 1"
location: "3p22.1"
module: 23
arm: "-"
pooled_cpm: 89.09
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# TRAK1

*trafficking kinesin protein 1* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +8.2, q 1e-13, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.634× (z -14.7, q 0e+00, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF5]] (+0.65, fdr 7e-06), [[COBL]] (+0.65, fdr 1e-05), [[SOAT1]] (+0.64, fdr 1e-05); moves opposite to [[NMNAT1]] (-0.70, fdr 7e-06), [[KIAA0753]] (-0.62, fdr 1e-05), [[RECQL5]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.2 | 1e-13 | 33/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +6.2 | 2e-07 | 30/49 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +6.1 | 2e-07 | 28/48 (SW1417, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +5.6 | 3e-06 | 29/49 (SW1417, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +5.5 | 4e-06 | 26/48 (SW1417, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +5.0 | 5e-05 | 24/48 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.18× | +3.7 | 0.017 | 16/48 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.15× | +3.1 | 0.12 | 12/47 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11307.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -14.7 | 0e+00 | 35/49 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.764×** | -8.7 | 1e-15 | 28/48 (RKO, KATO III, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -7.0 | 6e-10 | 28/48 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.1 | 1e-07 | 33/50 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.777×** | -5.7 | 1e-06 | 27/48 (LoVo, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.841× | -5.6 | 2e-06 | 21/48 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.796×** | -5.0 | 5e-05 | 27/48 (RKO, SW48, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.792×** | -4.9 | 6e-05 | 24/45 (SW 900, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.811×** | -4.8 | 1e-04 | 24/49 (SHP-77, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.814×** | -4.5 | 4e-04 | 23/43 (SNU-1, LS 180, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.844× | -3.9 | 0.006 | 22/48 (RKO, SW48, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.848× | -3.8 | 0.008 | 18/48 (RKO, SW48, …) | rises with dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 0.862× | -3.4 | 0.030 | 17/47 (SNU-1, SW1417, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.5 µM |  | 0.862× | -3.4 | 0.030 | 13/48 (LoVo, SW 1271, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~1% of this change | 0.859× | -3.3 | 0.033 | 20/47 (KATO III, RKO, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.877× | -3.0 | 0.096 | 12/49 (HEC-1-A, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 102 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -23.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -17.5) |
| [[SW1417 (line)]] | alt | 103 | 4 (1 ⚠) | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.66× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -15.4) |
| [[KATO III (line)]] | alt | 275 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -18.2) |
| [[HS-578T (line)]] | alt | 86.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 65.2 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 95.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -11.1) |
| [[SNU-1 (line)]] | wt | 171 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0943× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.471× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 77.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -12.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 41.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 67.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.57× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 78.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW48 (line)]] | wt | 133 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -10.8) |
| [[A-172 (line)]] | wt | 48.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AsPC-1 (line)]] | alt | 64.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 82.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -10.1) |
| [[COLO 205 (line)]] | alt | 147 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 144 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.0) |
| [[HT-29 (line)]] | alt | 130 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.350× (z -9.2) |
| [[LS 180 (line)]] | wt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 99.9 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.61× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.3) |
| [[PANC-1 (line)]] | alt | 65.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -10.7) |
| [[SHP-77 (line)]] | alt | 100 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 97.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.5) |
| [[AN3 CA (line)]] | alt | 83.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.236× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.464× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 72.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 63.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.601× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H661 (line)]] | alt | 307 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[A-427 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF5]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[COBL]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SOAT1]] | +0.64 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ARHGAP8]] | +0.63 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SPATA13]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[EDA]] | +0.62 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SLC27A2]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CYRIB]] | +0.61 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CARMIL1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[VOPP1]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[PRKAR2B]] | +0.58 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ATP8A1]] | +0.58 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMNAT1]] | -0.70 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[KIAA0753]] | -0.62 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[RECQL5]] | -0.62 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[UBE3B]] | -0.61 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[MFF-DT]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | -0.58 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[TBP]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[SENP8]] | -0.57 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[C12orf60]] | -0.56 | -0.56 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[DENND6A-AS1]] | -0.55 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | -0.55 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[METTL6]] | -0.55 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[CCDC59]] | -0.55 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TRAK1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TRAK1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TRAK1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-3.4, 35.7); signed map (-18.4, 36.7). **Vector** length 107, 26.8% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.1 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.6 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +5.2 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +5.2 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -14.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | +1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | trafficking kinesin protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,013,802-42,225,890 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OIP106, KIAA1042, MILT1 |
| Reactome | 7 pathways, smallest: RHOT1 GTPase cycle; RHOT2 GTPase cycle; Miro GTPase Cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPV9](https://www.uniprot.org/uniprotkb/Q9UPV9) (Trafficking kinesin-binding protein 1):

> Involved in the regulation of endosome-to-lysosome trafficking, including endocytic trafficking of EGF-EGFR complexes and GABA-A receptors. Involved in mitochondrial motility. When O-glycosylated, abolishes mitochondrial motility. Crucial for recruiting OGT to the mitochondrial surface of neuronal processes. TRAK1 and RHOT form an essential protein complex that links KIF5 to mitochondria for light chain-independent, anterograde transport of mitochondria (By similarity).

**Summary**, from NCBI Gene [22906](https://www.ncbi.nlm.nih.gov/gene/22906):

> Predicted to enable GABA receptor binding activity and myosin binding activity. Involved in endosome to lysosome transport. Located in early endosome and mitochondrion. Implicated in developmental and epileptic encephalopathy 68. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29947) · Entrez [22906](https://www.ncbi.nlm.nih.gov/gene/22906) · UniProt [Q9UPV9](https://www.uniprot.org/uniprotkb/Q9UPV9) · Ensembl [ENSG00000182606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182606)

## Data

Gene col 11307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11307); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11307]; `tensor/DDL_lfc|DDL_z.npy` [11307]; `embed/gene_vectors.npy` [11307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11307 or target_col == 11307). Every well: [[TRAK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
