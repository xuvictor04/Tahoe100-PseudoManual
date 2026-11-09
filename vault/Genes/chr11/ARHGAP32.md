---
symbol: "ARHGAP32"
type: "gene"
col: 5626
ensembl_id: "ENSG00000134909"
name: "Rho GTPase activating protein 32"
location: "11q24.3"
module: 23
arm: "-"
pooled_cpm: 291.44
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ARHGAP32

*Rho GTPase activating protein 32* — 11q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +6.0, q 1e-06, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.466× (z -21.4, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAK1]] (+0.57, fdr 2e-05), [[NR6A1]] (+0.56, fdr 3e-05), [[SUSD4]] (+0.54, fdr 2e-04); moves opposite to [[PSKH1]] (-0.56, fdr 3e-05), [[NMNAT1]] (-0.54, fdr 2e-05), [[ANXA2R-OT1]] (-0.53, fdr 1e-04).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SKAP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.0 | 1e-06 | 28/47 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +5.3 | 3e-05 | 29/48 (NCI-H2347, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +3.9 | 0.016 | 25/46 (C-33 A, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.016 | 24/46 (RKO, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.019 | 24/48 (SNU-423, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.466×** | -21.4 | 0e+00 | 46/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.477×** | -14.9 | 0e+00 | 40/43 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.503×** | -14.1 | 6e-43 | 40/48 (LS 180, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.541×** | -12.4 | 6e-33 | 46/46 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.648×** | -12.1 | 7e-32 | 28/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -9.7 | 4e-20 | 35/47 (SW480, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.617×** | -9.4 | 6e-19 | 35/44 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -9.0 | 1e-17 | 38/47 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -7.9 | 1e-13 | 37/49 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.706×** | -7.3 | 2e-11 | 39/47 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -7.2 | 4e-11 | 34/47 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.792×** | -4.8 | 8e-05 | 29/47 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.811×** | -4.3 | 8e-04 | 25/46 (CFPAC-1, BT-474, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.821×** | -4.1 | 0.001 | 22/47 (SW480, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -4.0 | 0.002 | 22/47 (SW1417, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.837× | -3.7 | 0.006 | 20/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | 0.852× | -3.2 | 0.037 | 12/48 (KATO III, HepG2/C3A, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.861× | -3.0 | 0.070 | 14/47 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.072 | 18/47 (BT-474, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 497 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -23.1) |
| [[LS 180 (line)]] | wt | 608 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 210 | 1 | 8 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.60× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -14.6) |
| [[SW1417 (line)]] | alt | 589 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 372 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -17.4) |
| [[HT-29 (line)]] | alt | 763 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -15.6) |
| [[LoVo (line)]] | wt | 333 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -22.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -14.8) |
| [[C-33 A (line)]] | alt | 732 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -16.7) |
| [[COLO 205 (line)]] | alt | 477 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 220 | 2 (2 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.59× (z +9.9) ⚠ cell-cycle shift, explains ~75% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -16.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -8.5) |
| [[KATO III (line)]] | alt | 865 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 318 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -20.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -14.0) |
| [[SNU-423 (line)]] | alt | 187 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -18.3) |
| [[A-172 (line)]] | wt | 112 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.475× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -13.4) |
| [[HOP62 (line)]] | alt | 178 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -19.2) |
| [[HS-578T (line)]] | alt | 138 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -16.1) |
| [[NCI-H1792 (line)]] | alt | 338 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -17.8) |
| [[RPMI-7951 (line)]] | alt | 223 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -13.6) |
| [[J82 (line)]] | alt | 128 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -12.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 189 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -16.7) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 223 | 1 (1 ⚠) | 3 (2 ⚠) | [[Trametinib (drug)]] 5 µM 2.08× (z +9.9) ⚠ cell-cycle shift, explains ~64% of this change | [[Dinaciclib (drug)]] 5 µM 0.363× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.8) |
| [[PANC-1 (line)]] | alt | 416 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -14.3) |
| [[SW48 (line)]] | wt | 446 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 231 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -14.5) |
| [[HCT15 (line)]] | alt | 275 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.381× (z -10.7) |
| [[Hs 766T (line)]] | wt | 169 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.462× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 207 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 569 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -18.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -15.7) |
| [[NCI-H2347 (line)]] | alt | 125 | 2 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 1.69× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -14.4) |
| [[BT-474 (line)]] | alt | 378 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -13.7) |
| [[CHP-212 (line)]] | wt | 231 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -11.8) |
| [[RKO (line)]] | wt | 228 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.71× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 198 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.408× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -8.8) |
| [[SW 900 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -13.8) |
| [[A549 (line)]] | wt | 147 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -15.5) |
| [[H4 (line)]] | wt | 244 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.429× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW 1271 (line)]] | alt | 126 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -9.4) |
| [[A-427 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 92.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 99.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAK1]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[NR6A1]] | +0.56 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[SUSD4]] | +0.54 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[LRBA]] | +0.53 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[RABGAP1L]] | +0.51 | +0.30 / +0.47 | both halves | 2e-04 |  |
| [[PPP2R2A]] | +0.51 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[STK3]] | +0.51 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[RAPGEF5]] | +0.51 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[GMDS]] | +0.50 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[CERS6]] | +0.50 | +0.51 / +0.43 | both halves | 4e-05 |  |
| [[ZBTB7C]] | +0.50 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[USP2]] | +0.50 | +0.36 / +0.41 | both halves | 1e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSKH1]] | -0.56 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[NMNAT1]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ANXA2R-OT1]] | -0.53 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[PDCD6P1]] | -0.52 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[SPRY3]] | -0.50 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[C10orf88]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[RECQL5]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CENPL]] | -0.49 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[ZNF425]] | -0.49 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.49 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[LINC01772]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[DNAAF10]] | -0.49 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SKAP1]] | B | SKAP1 activity raises ARHGAP32's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 1.95× lower at baseline in the lines without SKAP1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[SAMD12]] | B | SAMD12 activity raises ARHGAP32's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without SAMD12 | 0.062 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[ARHGAP8]] | B | ARHGAP8 activity raises ARHGAP32's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.73× lower at baseline in the lines without ARHGAP8 | 0.083 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[TOP2A]] | B | TOP2A activity raises ARHGAP32's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-7.4, 18.5); signed map (-16.8, 31.8). **Vector** length 98.1, 30.5% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +7.6 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.5 | -14.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.3 | -12.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.8 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -21.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -2.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.9 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 32 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.3 — chr11:128,965,060-129,279,324 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRIT, KIAA0712, MGC1892, RICS, GC-GAP |
| Gene groups (HGNC) | Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 23 pathways, smallest: Regulation of CDH1 posttranslational processing and trafficking to plasma membrane; RHOF GTPase cycle; RHOD GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [A7KAX9](https://www.uniprot.org/uniprotkb/A7KAX9) (Rho GTPase-activating protein 32):

> GTPase-activating protein (GAP) promoting GTP hydrolysis on RHOA, CDC42 and RAC1 small GTPases. May be involved in the differentiation of neuronal cells during the formation of neurite extensions. Involved in NMDA receptor activity-dependent actin reorganization in dendritic spines. May mediate cross-talks between Ras- and Rho-regulated signaling pathways in cell growth regulation. Isoform 2 has higher GAP activity (By similarity).

**Summary**, from NCBI Gene [9743](https://www.ncbi.nlm.nih.gov/gene/9743):

> RICS is a neuron-associated GTPase-activating protein that may regulate dendritic spine morphology and strength by modulating Rho GTPase (see RHOA; MIM 165390) activity (Okabe et al., 2003 [PubMed 12531901]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17399) · Entrez [9743](https://www.ncbi.nlm.nih.gov/gene/9743) · UniProt [A7KAX9](https://www.uniprot.org/uniprotkb/A7KAX9) · Ensembl [ENSG00000134909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134909)

## Data

Gene col 5626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5626); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5626]; `tensor/DDL_lfc|DDL_z.npy` [5626]; `embed/gene_vectors.npy` [5626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5626 or target_col == 5626). Every well: [[ARHGAP32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
