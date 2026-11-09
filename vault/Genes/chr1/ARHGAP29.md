---
symbol: "ARHGAP29"
type: "gene"
col: 6101
ensembl_id: "ENSG00000137962"
name: "Rho GTPase activating protein 29"
location: "1p22.1"
module: 184
arm: "+"
pooled_cpm: 180.95
n_lines_expressing: 40
n_dd_up: 18
n_dd_down: 27
n_dd_up_clean: 13
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# ARHGAP29

*Rho GTPase activating protein 29* — 1p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.58× (z +14.2, q 7e-43, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.613× (z -15.2, q 0e+00, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLCXD2]] (+0.70, fdr 7e-06), [[UCHL3]] (+0.61, fdr 1e-05), [[WNT7A]] (+0.59, fdr 2e-05); moves opposite to [[HEXA]] (-0.54, fdr 4e-05), [[EFCAB2]] (-0.53, fdr 1e-04), [[KANSL1L]] (-0.51, fdr 6e-04).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLEK2]] → it (grade B ⚠); 3 go from it, the strongest it → [[ASAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.58×** | +14.2 | 7e-43 | 35/39 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.68×** | +11.5 | 5e-28 | 33/38 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.60×** | +10.3 | 9e-23 | 30/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.55×** | +9.7 | 3e-20 | 28/37 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.57×** | +9.6 | 1e-19 | 32/37 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.52×** | +9.2 | 2e-18 | 29/37 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +7.7 | 1e-12 | 17/38 (SW480, C32, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.55×** | +6.9 | 5e-10 | 27/38 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.30×** | +5.8 | 5e-07 | 19/38 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +5.7 | 7e-07 | 21/39 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 5 µM |  | **1.62×** | +5.6 | 1e-06 | 25/36 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +5.4 | 3e-06 | 21/38 (NCI-H23, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.30×** | +4.8 | 6e-05 | 16/38 (C32, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 2e-04 | 20/38 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +4.4 | 5e-04 | 16/38 (SW480, hTERT-HPNE, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 1.19× | +3.8 | 0.005 | 17/39 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.030 | 12/39 (NCI-H23, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.066 | 4/39 (Panc 03.27, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6101.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -15.2 | 0e+00 | 32/39 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.718×** | -10.2 | 3e-22 | 28/38 (HEC-1-A, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -8.0 | 3e-13 | 23/38 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.774×** | -7.9 | 3e-13 | 22/38 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -7.2 | 7e-11 | 24/38 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -7.2 | 7e-11 | 25/37 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.711×** | -6.3 | 3e-08 | 26/38 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.754×** | -6.2 | 5e-08 | 25/38 (J82, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.715×** | -6.1 | 5e-08 | 23/38 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -6.0 | 1e-07 | 22/38 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.764×** | -5.9 | 2e-07 | 24/38 (J82, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.774×** | -5.6 | 1e-06 | 21/38 (J82, HS-578T, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -5.6 | 1e-06 | 25/38 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.786×** | -5.3 | 5e-06 | 19/38 (BT-474, HS-578T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.796×** | -5.0 | 2e-05 | 20/39 (J82, SNU-423, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.851× | -5.0 | 2e-05 | 17/38 (HOP62, A-172, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.796×** | -4.8 | 5e-05 | 22/38 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.810×** | -4.6 | 1e-04 | 19/38 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.802×** | -4.5 | 2e-04 | 16/37 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.819×** | -4.4 | 3e-04 | 15/38 (J82, HS-578T, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.814×** | -4.3 | 3e-04 | 21/40 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 220 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -26.7) |
| [[MIA PaCa-2 (line)]] | alt | 199 | 10 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 4.57× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 384 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -19.2) |
| [[HT-29 (line)]] | alt | 286 | 6 (2 ⚠) | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.13× (z +10.5) | [[Selinexor (drug)]] 5 µM 0.469× (z -10.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.7) |
| [[J82 (line)]] | alt | 183 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -17.5) |
| [[SW480 (line)]] | alt | 84.5 | 8 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.39× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 148 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.7) |
| [[LS 180 (line)]] | wt | 204 | 2 (1 ⚠) | 4 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.08× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -10.0) |
| [[RKO (line)]] | wt | 74.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.6) |
| [[A-172 (line)]] | wt | 120 | 1 | 4 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.92× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -16.2) |
| [[KATO III (line)]] | alt | 244 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 254 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 247 | 1 (1 ⚠) | 3 | [[Daptomycin (drug)]] 5 µM 2.34× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.2) |
| [[HCT15 (line)]] | alt | 158 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 79.2 | 3 | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.04× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.374× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 134 | 2 (1 ⚠) | 2 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.84× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.6) |
| [[BT-474 (line)]] | alt | 175 | 1 (1 ⚠) | 2 | [[Daptomycin (drug)]] 5 µM 2.46× (z +8.5) ⚠ unreliable plate only | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 166 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.43× (z +12.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.98× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 270 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -10.2) |
| [[A498 (line)]] | wt | 237 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -12.4) |
| [[C32 (line)]] | wt | 47.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.89× (z +13.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -10.4) |
| [[Hs 766T (line)]] | wt | 443 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.5) |
| [[LoVo (line)]] | wt | 202 | 2 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.93× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 302 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -12.6) |
| [[Panc 03.27 (line)]] | alt | 450 | 2 (1 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 1.95× (z +8.9) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 3.45× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 184 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.514× (z -12.9) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -12.1) |
| [[A-427 (line)]] | wt | 54.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.82× (z +9.2) | — |
| [[A549 (line)]] | wt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.43× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 344 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.77× (z +12.7) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 70.0 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.97× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 23.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 39.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 42.1 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLCXD2]] | +0.70 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[UCHL3]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[WNT7A]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[SLC35F3]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SMS]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[FLNB]] | +0.57 | +0.48 / +0.40 | both halves | 4e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[TSC22D2]] | +0.55 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[PROSER2]] | +0.55 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[DLC1]] | +0.54 | +0.47 / +0.47 | both halves | 2e-05 | pathway: CDC42 GTPase cycle |
| [[SMURF2]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[NF2]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[RAB3B]] | +0.52 | +0.49 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXA]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[EFCAB2]] | -0.53 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[KANSL1L]] | -0.51 | -0.54 / -0.22 | both halves | 6e-04 |  |
| [[C1RL]] | -0.51 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[RRAGB]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LINC01278]] | -0.49 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[RBKS]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[MED24]] | -0.48 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[THBS3]] | -0.48 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[DTX3]] | -0.48 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[KMT2E-AS1]] | -0.48 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[WASHC2C]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEK2]] | B | PLEK2 activity raises ARHGAP29's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.91× lower at baseline in the lines without PLEK2 | 0.049 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[CDCP1]] | B | CDCP1 activity raises ARHGAP29's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without CDCP1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[KRT15]] | B | KRT15 activity raises ARHGAP29's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without KRT15 | 0.062 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASAP2]] | B | ARHGAP29 activity raises ASAP2's level | lines that do not express ARHGAP29 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without ARHGAP29 | 0.049 | ⚠ within organs, on part of the lines; also absent: HTATIP2, CTSZ, TBILA |
| [[DCBLD2]] | B | ARHGAP29 activity raises DCBLD2's level | lines that do not express ARHGAP29 (10) vs lines expressing it (40) | 2.58× lower at baseline in the lines without ARHGAP29 | 0.068 | ⚠ within organs, on part of the lines; also absent: HTATIP2, CTSZ, TBILA |
| [[FLNB]] | B | ARHGAP29 activity raises FLNB's level | lines that do not express ARHGAP29 (10) vs lines expressing it (40) | 1.82× lower at baseline in the lines without ARHGAP29 | 0.085 | ⚠ within organs, on part of the lines; also absent: HTATIP2, CTSZ, TBILA |

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (15.9, 4.7); signed map (-0.9, 41.8). **Vector** length 139, 42.2% of its response variance represented; |z| ≥ 3 in 1,624 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +9.2 | +14.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +7.8 | +11.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +7.2 | +10.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +7.2 | +9.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +6.2 | +9.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -7.0 | -10.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -6.1 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.8 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.6 | -8.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.2 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -5.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.5 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.1 — chr1:94,148,988-94,275,068 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PARG1 |
| Gene groups (HGNC) | AH/BAR family Rho GTPase activating proteins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q52LW3](https://www.uniprot.org/uniprotkb/Q52LW3) (Rho GTPase-activating protein 29):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state. Has strong activity toward RHOA, and weaker activity toward RAC1 and CDC42. May act as a specific effector of RAP2A to regulate Rho. In concert with RASIP1, suppresses RhoA signaling and dampens ROCK and MYH9 activities in endothelial cells and plays an essential role in blood vessel tubulogenesis.

**Summary**, from NCBI Gene [9411](https://www.ncbi.nlm.nih.gov/gene/9411):

> Rap1 is a small GTPase that, through effectors, regulates Rho GTPase signaling. These effectors- Rasip1, Radil, and the protein encoded by this gene- translocate to the cell membrane, where they form a multiprotein complex. This complex is necessary for Rap1-induced inhibition of Rho signaling. Defects in this gene may be a cause of nonsyndromic cleft lip with or without cleft palate. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:30207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30207) · Entrez [9411](https://www.ncbi.nlm.nih.gov/gene/9411) · UniProt [Q52LW3](https://www.uniprot.org/uniprotkb/Q52LW3) · Ensembl [ENSG00000137962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137962)

## Data

Gene col 6101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6101); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6101]; `tensor/DDL_lfc|DDL_z.npy` [6101]; `embed/gene_vectors.npy` [6101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6101 or target_col == 6101). Every well: [[ARHGAP29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
