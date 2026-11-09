---
symbol: "PALM2AKAP2"
type: "gene"
col: 8093
ensembl_id: "ENSG00000157654"
name: "PALM2 and AKAP2 fusion"
location: "9q31.3"
module: 147
arm: "+"
pooled_cpm: 277.26
n_lines_expressing: 41
n_dd_up: 22
n_dd_down: 22
n_dd_up_clean: 18
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 12
direction_downstream: 4
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# PALM2AKAP2

*PALM2 and AKAP2 fusion* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.99× (z +13.9, q 4e-41, up in 31 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.661× (z -11.3, q 1e-26, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELK3]] (+0.68, fdr 7e-06), [[ETS1]] (+0.68, fdr 7e-06), [[MAP4K4]] (+0.67, fdr 7e-06); moves opposite to [[COG7]] (-0.52, fdr 4e-05), [[MBIP]] (-0.51, fdr 2e-05), [[UBE4B]] (-0.50, fdr 1e-04).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CCBE1]] → it (grade B ⚠); 4 go from it, the strongest it → [[DCBLD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.99×** | +13.9 | 4e-41 | 31/40 (HOP62, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.64×** | +9.5 | 7e-19 | 31/39 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +7.7 | 2e-12 | 23/39 (SW480, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.49×** | +7.3 | 3e-11 | 31/38 (SHP-77, C32, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +7.3 | 3e-11 | 26/39 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.44×** | +7.0 | 2e-10 | 36/39 (SHP-77, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.41×** | +6.6 | 4e-09 | 28/38 (C32, CHP-212, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +5.9 | 2e-07 | 21/40 (SHP-77, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.3 | 6e-06 | 24/39 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.1 | 2e-05 | 22/39 (CFPAC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 3e-05 | 23/39 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 3e-05 | 23/40 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 4e-05 | 21/39 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.7 | 1e-04 | 20/39 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +4.6 | 2e-04 | 21/38 (C32, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.003 | 20/39 (SW480, CHP-212, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.006 | 17/39 (SK-MEL-2, A-172, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +3.7 | 0.006 | 19/39 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.661×** | -11.3 | 1e-26 | 26/40 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.643×** | -8.5 | 6e-15 | 22/39 (J82, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.659×** | -7.7 | 2e-12 | 28/38 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.791×** | -6.4 | 3e-08 | 21/39 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.780×** | -5.8 | 8e-07 | 21/39 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.747×** | -5.6 | 2e-06 | 25/40 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.594×** | -5.2 | 1e-05 | 25/38 (RKO, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.756×** | -5.2 | 2e-05 | 24/38 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.769×** | -4.9 | 8e-05 | 24/39 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.788×** | -4.6 | 2e-04 | 20/39 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.825×** | -4.5 | 4e-04 | 19/41 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.824×** | -4.3 | 8e-04 | 20/39 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.821×** | -4.2 | 0.001 | 20/40 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.795×** | -4.1 | 0.002 | 20/38 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.799×** | -4.1 | 0.002 | 18/39 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.858× | -4.1 | 0.002 | 16/40 (C32, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 442 | 7 (3 ⚠) | 24 (8 ⚠) | [[Daptomycin (drug)]] 5 µM 2.45× (z +11.3) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 2.40× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 232 | 1 | 14 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.53× (z +12.0) | [[Selinexor (drug)]] 5 µM 0.467× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.384× (z -13.6) |
| [[RKO (line)]] | wt | 336 | 1 | 12 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -25.8) |
| [[J82 (line)]] | alt | 1,015 | 1 | 10 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 4.26× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -25.2) |
| [[Hs 766T (line)]] | wt | 913 | 1 | 7 | [[TAK-901 (drug)]] 5 µM 17.8× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -12.4) |
| [[SW480 (line)]] | alt | 122 | 6 (2 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 1.82× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -15.3) |
| [[A-172 (line)]] | wt | 783 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +19.1) | — |
| [[AsPC-1 (line)]] | alt | 470 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 710 | 6 | 1 | [[Harringtonine (drug)]] 5 µM 7.31× (z +18.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 101 | 6 (4 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.20× (z +14.8) ⚠ unreliable plate only · without an alert: [[Tucidinostat (drug)]] 5 µM 2.26× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.2) |
| [[PANC-1 (line)]] | alt | 80.8 | 7 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 5.50× (z +21.1) | — |
| [[SW1417 (line)]] | alt | 78.0 | 7 (3 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.43× (z +12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.0) | — |
| [[A498 (line)]] | wt | 700 | 5 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.27× (z +13.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.407× (z -10.1) ⚠ toxic |
| [[A549 (line)]] | wt | 436 | 3 | 3 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.82× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 165 | 1 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -9.2) ⚠ cell-cycle shift, explains ~12% of this change |
| [[HS-578T (line)]] | alt | 330 | 4 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.49× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 355 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -18.1) |
| [[LS 180 (line)]] | wt | 120 | 6 (5 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.6) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 1,018 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.66× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -21.4) |
| [[CHP-212 (line)]] | wt | 330 | 4 (2 ⚠) | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.85× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 202 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.86× (z +13.8) | — |
| [[SHP-77 (line)]] | alt | 117 | 5 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.59× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 216 | 5 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.49× (z +13.0) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 9.23× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 203 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.24× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 190 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -17.4) |
| [[HOP62 (line)]] | alt | 397 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 14.1× (z +14.6) | [[Ponatinib (drug)]] 5 µM 0.325× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 232 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 1.69× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -10.3) |
| [[SNU-423 (line)]] | alt | 359 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 7.83× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.8) |
| [[H4 (line)]] | wt | 294 | 1 | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.05× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 495 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 215 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -24.3) |
| [[A-427 (line)]] | wt | 73.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 1,014 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -16.2) |
| [[AN3 CA (line)]] | alt | 40.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 38.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 61.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 59.3 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 35.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 390 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELK3]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ETS1]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MIR222HG]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CDK14]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[RPSAP52]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[AKAP12]] | +0.60 | +0.49 / +0.67 | both halves | 1e-05 | STRING 521 |
| [[CDC42EP3]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[MACF1]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ASAP1]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[BCAR3]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | -0.52 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[MBIP]] | -0.51 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[UBE4B]] | -0.50 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[P4HTM]] | -0.50 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ZFP14]] | -0.49 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[GID8]] | -0.48 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCBE1]] | B | CCBE1 activity raises PALM2AKAP2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 4.01× lower at baseline in the lines without CCBE1 | 0.004 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[PLPP4]] | B | PLPP4 activity raises PALM2AKAP2's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 3.50× lower at baseline in the lines without PLPP4 | 0.018 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6 |
| [[ZFPM2-AS1]] | B | ZFPM2-AS1 activity raises PALM2AKAP2's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 3.35× lower at baseline in the lines without ZFPM2-AS1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |
| [[SERPINE1]] | B | SERPINE1 activity raises PALM2AKAP2's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 3.25× lower at baseline in the lines without SERPINE1 | 0.028 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[RFTN1]] | B | RFTN1 activity raises PALM2AKAP2's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 4.14× lower at baseline in the lines without RFTN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[KIRREL1]] | B | KIRREL1 activity raises PALM2AKAP2's level | lines that do not express KIRREL1 (8) vs lines expressing it (42) | 4.34× lower at baseline in the lines without KIRREL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEX3, ARHGAP31, ROBO3 |
| [[ETS1]] | B | ETS1 activity raises PALM2AKAP2's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 3.84× lower at baseline in the lines without ETS1 | 0.052 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23 |
| [[LNCOG]] | B | LNCOG activity raises PALM2AKAP2's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 3.23× lower at baseline in the lines without LNCOG | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |
| [[MAP2K1]] | B | MAP2K1 activity raises PALM2AKAP2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ABLIM3]] | B | ABLIM3 activity strengthens PALM2AKAP2's drug response | lines that do not express ABLIM3 (11) vs lines expressing it (29) | the lines without ABLIM3 respond 0.50× as strongly (z diff +2.55); rises at some drug-doses, falls at others (73% from rises): Idarubicin (hydrochloride) 5 µM: 1.04x vs 0.59x (z diff +6.0); Harringtonine 0.5 µM: 1.21x vs 2.07x (z diff +4.8); Harringtonine 5 µM: 1.06x vs 1.86x (z diff +4.1) | 0.089 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[CD44]] | B | CD44 activity raises PALM2AKAP2's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.00× lower at baseline in the lines without CD44 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[SACS]] | C | SACS activity raises PALM2AKAP2's level | lines that do not express SACS (5) vs lines expressing it (45) | 5.95× lower at baseline in the lines without SACS | 0.055 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCBLD2]] | B | PALM2AKAP2 activity raises DCBLD2's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 2.97× lower at baseline in the lines without PALM2AKAP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L |
| [[DLC1]] | B | PALM2AKAP2 activity raises DLC1's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 4.04× lower at baseline in the lines without PALM2AKAP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L |
| [[AKAP12]] | B | PALM2AKAP2 activity raises AKAP12's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 5.05× lower at baseline in the lines without PALM2AKAP2 | 0.057 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L |
| [[SACS]] | C | PALM2AKAP2 activity raises SACS's level | lines that do not express PALM2AKAP2 (9) vs lines expressing it (41) | 3.07× lower at baseline in the lines without PALM2AKAP2 | 0.037 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MPP1, LIX1L; co-absent with the target |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.0, 10.2); signed map (12.4, 41.6). **Vector** length 142, 44.7% of its response variance represented; |z| ≥ 3 in 1,661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.3 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +5.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.1 | +7.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.0 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.5 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.1 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.1 | +3.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.0 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -5.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.4 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | PALM2 and AKAP2 fusion |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:109,498,325-110,172,512 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PALM2-AKAP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2D5](https://www.uniprot.org/uniprotkb/Q9Y2D5) (PALM2-AKAP2 fusion protein):

> Binds to regulatory subunit (RII) of protein kinase A. May be involved in establishing polarity in signaling systems or in integrating PKA-RII isoforms with downstream effectors to capture, amplify and focus diffuse, trans-cellular signals carried by cAMP. Binds to and modulates the structure of the actin cytoskeleton.

**Summary**, from NCBI Gene [445815](https://www.ncbi.nlm.nih.gov/gene/445815):

> This gene belongs to the paralemmin downstream gene (PDG) family defined in PMID:22855693. Paralemmin downstream genes may have evolved contiguously with the paralemmin genes and are associated with other paralemmin paralogs in humans and several other taxa. The gene encodes three distinct protein isoforms, the PALM2 isoform, the AKAP2 isoform and the PALM2-AKAP2 isoform. The biological significance of the PALM2-AKAP2 isoforms is yet unknown. Earlier, PALM2 and AKAP2 were annotated as separate …

**Accessions** — [HGNC:33529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33529) · Entrez [445815](https://www.ncbi.nlm.nih.gov/gene/445815) · UniProt [Q9Y2D5](https://www.uniprot.org/uniprotkb/Q9Y2D5) · Ensembl [ENSG00000157654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157654)

## Data

Gene col 8093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8093); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8093]; `tensor/DDL_lfc|DDL_z.npy` [8093]; `embed/gene_vectors.npy` [8093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8093 or target_col == 8093). Every well: [[PALM2AKAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALM2AKAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
