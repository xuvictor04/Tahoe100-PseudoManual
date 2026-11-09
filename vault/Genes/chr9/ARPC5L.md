---
symbol: "ARPC5L"
type: "gene"
col: 5950
ensembl_id: "ENSG00000136950"
name: "actin related protein 2/3 complex subunit 5 like"
location: "9q33.3"
module: 36
arm: "+"
pooled_cpm: 32.45
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ARPC5L

*actin related protein 2/3 complex subunit 5 like* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (21 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.24× (z +19.4, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.688× (z -4.0, q 0.036, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Bimiralisib (drug)]] 5 µM: 0.546× (z -3.7, q 0.036, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.534×, HOP62 0.637×, NCI-H23 0.645×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.166×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (AN3 CA 0.0841×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC10]] (+0.68, fdr 1e-05), [[SENP5]] (+0.65, fdr 3e-05), [[RAB43]] (+0.64, fdr 2e-05); moves opposite to [[KPNA5]] (-0.64, fdr 2e-05), [[NDUFA5]] (-0.62, fdr 3e-05), [[CDC73]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MYOF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 21 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +19.4 | 0e+00 | 47/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.05×** | +13.2 | 3e-37 | 47/47 (SW480, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.77×** | +12.0 | 5e-31 | 48/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.47×** | +10.7 | 2e-24 | 46/47 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.35×** | +10.1 | 7e-22 | 47/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +10.1 | 9e-22 | 43/45 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.94×** | +7.5 | 4e-12 | 39/47 (SNU-423, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.81×** | +7.0 | 2e-10 | 43/47 (A-172, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.85×** | +7.0 | 2e-10 | 39/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.81×** | +7.0 | 2e-10 | 42/47 (SW480, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.74×** | +6.5 | 3e-09 | 34/45 (C-33 A, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.73×** | +6.5 | 5e-09 | 36/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.63×** | +5.5 | 1e-06 | 32/47 (A-172, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.59×** | +5.5 | 1e-06 | 33/47 (SW480, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +5.2 | 8e-06 | 28/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.2 | 9e-06 | 32/48 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +4.7 | 9e-05 | 32/47 (SNU-423, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 3e-04 | 27/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 6e-04 | 28/47 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.005 | 27/48 (SNU-423, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.006 | 24/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.79×** | +3.6 | 0.006 | 23/48 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +3.6 | 0.006 | 24/46 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.020 | 26/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.030 | 17/48 (MIA PaCa-2, A498, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.036 | 18/46 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.051 | 16/47 (LOX-IMVI, RPMI-7951, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5950.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (MIA PaCa-2 0.534×, HOP62 0.637×, NCI-H23 0.645×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.166×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (AN3 CA 0.0841×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.688×** | -4.0 | 0.036 | 22/48 (AsPC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.546×** | -3.7 | 0.036 | 22/47 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.730×** | -3.7 | 0.036 | 23/47 (LS 180, HOP62, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -3.6 | 0.042 | 4/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.579×** | -3.4 | 0.083 | 21/47 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.609× | -3.1 | 0.21 | 12/48 (A-172, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.78 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.3 | 10 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 29.3 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +15.3) | — |
| [[A549 (line)]] | wt | 15.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.92× (z +16.4) | — |
| [[LoVo (line)]] | wt | 21.1 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.60× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 20.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 22.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 23.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +10.5) | [[Adagrasib (drug)]] 0.05 µM 0.637× (z -10.1) ⚠ position not correctable |
| [[HS-578T (line)]] | alt | 19.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +12.6) | [[Adagrasib (drug)]] 0.05 µM 0.534× (z -14.7) ⚠ position not correctable |
| [[BT-474 (line)]] | alt | 50.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +14.9) | — |
| [[HEC-1-A (line)]] | alt | 43.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 38.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 32.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 35.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +11.0) | — |
| [[SW48 (line)]] | wt | 37.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.7) | — |
| [[A-172 (line)]] | wt | 41.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +12.2) | — |
| [[A498 (line)]] | wt | 49.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 28.2 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0841× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 42.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.46× (z +9.3) | — |
| [[C32 (line)]] | wt | 25.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 27.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +10.4) | — |
| [[KATO III (line)]] | alt | 61.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.645× (z -9.6) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 33.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 30.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +12.4) | — |
| [[RKO (line)]] | wt | 69.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.46× (z +8.9) | — |
| [[SNU-1 (line)]] | wt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 24.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +14.6) | — |
| [[A-427 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC10]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[SENP5]] | +0.65 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[RAB43]] | +0.64 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[FBXL18]] | +0.64 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[PITPNA]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[PGP]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[GATAD2A]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[IPPK]] | +0.61 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PDCD6]] | +0.61 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[IL9RP3]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NACC1]] | +0.60 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NIPA2]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA5]] | -0.64 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[NDUFA5]] | -0.62 | -0.44 / -0.69 | both halves | 3e-05 |  |
| [[CDC73]] | -0.61 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[SETDB2]] | -0.60 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[LGALS3]] | -0.59 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[ZNF608]] | -0.58 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[CHIC1]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[AMOT]] | -0.56 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SNX2]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[PMPCB]] | -0.55 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[NR1D2]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[AMZ2P1]] | -0.55 | -0.45 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYOF]] | B | MYOF activity lowers ARPC5L's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.28× higher at baseline in the lines without MYOF | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[TOP2A]] | B | TOP2A activity lowers ARPC5L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIK3CB]] | B | PIK3CB activity raises ARPC5L's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-14.7, -0.7); signed map (-46.7, 0.7). **Vector** length 82.1, 23.1% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.1 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +19.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.7 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +3.5 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.9 | +3.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.7 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex subunit 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,862,130-124,877,733 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3038, ARC16-2 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits |
| Hallmark sets | MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPX5](https://www.uniprot.org/uniprotkb/Q9BPX5) (Actin-related protein 2/3 complex subunit 5-like protein):

> May function as component of the Arp2/3 complex which is involved in regulation of actin polymerization and together with an activating nucleation-promoting factor (NPF) mediates the formation of branched actin networks.

**Summary**, from NCBI Gene [81873](https://www.ncbi.nlm.nih.gov/gene/81873):

> Predicted to enable protein-macromolecule adaptor activity. Involved in Arp2/3 complex-mediated actin nucleation. Located in extracellular exosome and focal adhesion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23366) · Entrez [81873](https://www.ncbi.nlm.nih.gov/gene/81873) · UniProt [Q9BPX5](https://www.uniprot.org/uniprotkb/Q9BPX5) · Ensembl [ENSG00000136950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136950)

## Data

Gene col 5950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5950); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5950]; `tensor/DDL_lfc|DDL_z.npy` [5950]; `embed/gene_vectors.npy` [5950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5950 or target_col == 5950). Every well: [[ARPC5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPC5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
