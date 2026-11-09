---
symbol: "PTPRM"
type: "gene"
col: 10393
ensembl_id: "ENSG00000173482"
name: "protein tyrosine phosphatase receptor type M"
location: "18p11.23"
module: 104
arm: "+"
pooled_cpm: 261.33
n_lines_expressing: 32
n_dd_up: 2
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 4
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# PTPRM

*protein tyrosine phosphatase receptor type M* — 18p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.05× (z +8.8, q 1e-15, up in 20 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (CFPAC-1 5.42×, HepG2/C3A 6.22×, J82 3.99×, SK-MEL-2 4.10×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (J82 2.57×, HOP62 2.81×, HS-578T 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (A-427 2.28×, NCI-H23 1.67×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (J82 1.93×, A498 1.83×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.485× (z -15.5, q 0e+00, down in 27 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.739× (z -7.0, q 2e-10, down in 17 of 30 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPC6]] (+0.57, fdr 1e-05), [[HS3ST3B1]] (+0.56, fdr 2e-05), [[BASP1]] (+0.54, fdr 3e-05); moves opposite to [[IQCK]] (-0.43, fdr 5e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CPS1]] → it (grade B ⚠); 4 go from it, the strongest it → [[FSTL5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10393.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (CFPAC-1 5.42×, HepG2/C3A 6.22×, J82 3.99×, SK-MEL-2 4.10×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (J82 2.57×, HOP62 2.81×, HS-578T 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Tucidinostat (drug)]] 5 µM in 2 lines (A-427 2.28×, NCI-H23 1.67×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (J82 1.93×, A498 1.83×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +8.8 | 1e-15 | 20/31 (CFPAC-1, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +5.3 | 4e-05 | 11/30 (A-427, NCI-H23, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.21×** | +4.4 | 0.002 | 15/30 (A549, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.006 | 16/30 (J82, HS-578T, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.011 | 16/30 (J82, HOP62, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.015 | 10/30 (SW 900, A549, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.17× | +3.7 | 0.015 | 9/31 (A-427, NCI-H2347, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.025 | 11/30 (A549, SW 900, …) | all doses, flat |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.045 | 8/31 (A498, A-427, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.11 | 13/30 (A549, Panc 03.27, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.485×** | -15.5 | 0e+00 | 27/31 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -14.3 | 6e-44 | 26/28 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.576×** | -12.3 | 1e-32 | 25/29 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.650×** | -9.3 | 3e-18 | 23/28 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.682×** | -8.9 | 8e-17 | 21/30 (NCI-H1573, HepG2/C3A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.776×** | -8.3 | 9e-15 | 17/30 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.739×** | -7.0 | 2e-10 | 17/30 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.721×** | -7.0 | 2e-10 | 23/30 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.745×** | -6.8 | 6e-10 | 23/30 (HOP62, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.757×** | -6.5 | 6e-09 | 19/30 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.765×** | -6.2 | 2e-08 | 21/30 (NCI-H1573, HepG2/C3A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.763×** | -6.0 | 8e-08 | 15/30 (NCI-H1573, NCI-H1792, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.824×** | -4.5 | 3e-04 | 15/30 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.880× | -4.2 | 0.001 | 16/31 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.893× | -3.7 | 0.008 | 4/31 (A-427, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.858× | -3.5 | 0.014 | 12/30 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.860× | -3.5 | 0.016 | 11/31 (NCI-H1573, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.854× | -3.4 | 0.023 | 12/29 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.767×** | -3.2 | 0.038 | 9/29 (hTERT-HPNE, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 271 | 0 | 15 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -26.2) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.434× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 1,398 | 0 | 13 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -34.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -25.5) |
| [[LS 180 (line)]] | wt | 169 | 0 | 12 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -22.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 793 | 2 | 9 (9 ⚠) | [[PH-797804 (drug)]] 5 µM 3.85× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -18.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 510 | 8 (6 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.99× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 142 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -18.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -10.5) |
| [[HOP62 (line)]] | alt | 715 | 3 (3 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.252× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 872 | 1 | 8 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -18.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 685 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 6.22× (z +11.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -15.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 679 | 0 | 8 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -17.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.469× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 221 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.42× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.270× (z -17.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.501× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 489 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.10× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -23.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.520× (z -9.5) |
| [[A-172 (line)]] | wt | 236 | 2 (1 ⚠) | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.28× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -13.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 362 | 3 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.484× (z -9.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 406 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -15.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 368 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -13.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 66.7 | 4 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +10.9) | — |
| [[A498 (line)]] | wt | 184 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.83× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.569× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 90.4 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 126 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.29× (z +9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.67× (z +8.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.395× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~49% of this change |
| [[Panc 03.27 (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.485× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 204 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.452× (z -10.5) ⚠ toxic |
| [[A549 (line)]] | wt | 577 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -16.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 324 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 5 µM 0.303× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 343 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.225× (z -8.7) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 50.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 35.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 36.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 24.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 36.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 51.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 257 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 48.0 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 479 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 337 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 23.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 32.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 33.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 33.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPC6]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[HS3ST3B1]] | +0.56 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[BASP1]] | +0.54 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[TANC2]] | +0.51 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PID1]] | +0.51 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[DNER]] | +0.50 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[KCNJ6]] | +0.50 | +0.27 / +0.48 | both halves | 3e-04 |  |
| [[MAPK4]] | +0.50 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SRGN]] | +0.49 | +0.55 / +0.30 | both halves | 2e-04 |  |
| [[SLC7A2]] | +0.48 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[IRAK3]] | +0.48 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[AFAP1L1]] | +0.48 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCK]] | -0.43 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPS1]] | B | CPS1 activity raises PTPRM's level | lines that do not express CPS1 (36) vs lines expressing it (14) | 3.15× lower at baseline in the lines without CPS1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, ENSG00000241168, GLP2R |
| [[CSGALNACT1]] | B | CSGALNACT1 activity raises PTPRM's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.90× lower at baseline in the lines without CSGALNACT1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[FAM13A]] | B | FAM13A activity raises PTPRM's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 3.04× lower at baseline in the lines without FAM13A | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[ENOX1]] | B | ENOX1 activity raises PTPRM's level | lines that do not express ENOX1 (12) vs lines expressing it (38) | 3.48× lower at baseline in the lines without ENOX1 | 0.099 | ⚠ within organs, on part of the lines; also absent: CYP1B1-AS1, HTR7, SLC1A3; maybe low, not absent |
| [[HSD11B1]] | C | HSD11B1 activity raises PTPRM's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 3.96× lower at baseline in the lines without HSD11B1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA; co-absent with the target |
| [[TREM1]] | C | TREM1 activity raises PTPRM's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 3.61× lower at baseline in the lines without TREM1 | 0.066 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF; co-absent with the target |
| [[RGS2]] | C | RGS2 activity raises PTPRM's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 3.48× lower at baseline in the lines without RGS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent; co-absent with the target |
| [[FAM110B]] | C | FAM110B activity raises PTPRM's level | lines that do not express FAM110B (27) vs lines expressing it (23) | 4.41× lower at baseline in the lines without FAM110B | 0.095 | ⚠ within organs, on part of the lines; also absent: LRRK2, PIEZO2, GFRA1; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSTL5]] | B | PTPRM activity raises FSTL5's level | lines that do not express PTPRM (18) vs lines expressing it (32) | 2.32× lower at baseline in the lines without PTPRM | 0.062 | ⚠ within organs, on part of the lines; also absent: FIGN, MAP9, CCDC169 |
| [[PAG1]] | B | PTPRM activity raises PAG1's level | lines that do not express PTPRM (18) vs lines expressing it (32) | 2.90× lower at baseline in the lines without PTPRM | 0.087 | ⚠ within organs, on part of the lines; also absent: FIGN, MAP9, CCDC169 |
| [[RNF165]] | C | PTPRM activity raises RNF165's level | lines that do not express PTPRM (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without PTPRM | 0.090 | ⚠ within organs, on part of the lines; also absent: FIGN, MAP9, CCDC169; co-absent with the target |
| [[RNF150]] | C | PTPRM activity raises RNF150's level | lines that do not express PTPRM (18) vs lines expressing it (32) | 3.98× lower at baseline in the lines without PTPRM | 0.093 | ⚠ within organs, on part of the lines; also absent: FIGN, MAP9, CCDC169; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.6, 14.3); signed map (18.6, 33.8). **Vector** length 92.1, 22.4% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.9 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | -15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +6.0 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | -9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +0.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.0 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.0 | -12.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -2.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.1 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.7 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.23 — chr18:7,566,782-8,406,861 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPTPU, hR-PTPu; previously PTPRL1 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Protein tyrosine phosphatases receptor type; Ig-like cell adhesion molecule family |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [P28827](https://www.uniprot.org/uniprotkb/P28827) (Receptor-type tyrosine-protein phosphatase mu):

> Receptor protein-tyrosine phosphatase that mediates homotypic cell-cell interactions and plays a role in adipogenic differentiation via modulation of p120 catenin/CTNND1 phosphorylation. Promotes CTNND1 dephosphorylation and prevents its cytoplasmic localization where it inhibits SLC2A4 membrane trafficking. In turn, SLC2A4 is directed to the plasma membrane and performs its glucose transporter function.

**Summary**, from NCBI Gene [5797](https://www.ncbi.nlm.nih.gov/gene/5797):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and two tandem catalytic domains, and thus represents a receptor-type PTP. The extracellular region contains a meprin-A5 antigen-PTP mu (MAM) domain, an …

**Accessions** — [HGNC:9675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9675) · Entrez [5797](https://www.ncbi.nlm.nih.gov/gene/5797) · UniProt [P28827](https://www.uniprot.org/uniprotkb/P28827) · Ensembl [ENSG00000173482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173482)

## Data

Gene col 10393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10393); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10393]; `tensor/DDL_lfc|DDL_z.npy` [10393]; `embed/gene_vectors.npy` [10393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10393 or target_col == 10393). Every well: [[PTPRM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
