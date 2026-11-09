---
symbol: "ICA1"
type: "gene"
col: 30
ensembl_id: "ENSG00000003147"
name: "islet cell autoantigen 1"
location: "7p21.3"
module: 8
arm: "+"
pooled_cpm: 49.32
n_lines_expressing: 30
n_dd_up: 13
n_dd_down: 31
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 25
direction_downstream: 15
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ICA1

*islet cell autoantigen 1* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.61× (z +8.7, q 1e-15, up in 26 of 29 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.57× (z +8.3, q 4e-14, up in 13 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.460× (z -20.0, q 0e+00, down in 26 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAAH2]] (+0.65, fdr 7e-06), [[TMEM125]] (+0.60, fdr 7e-06), [[LINC02253]] (+0.57, fdr 1e-05); moves opposite to [[MLXIP]] (-0.50, fdr 1e-05), [[NAV1]] (-0.49, fdr 4e-05), [[TSHZ3]] (-0.49, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[TPD52L1]] → it (grade B ⚠); 15 go from it, the strongest it → [[TPD52L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 30.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.61×** | +8.7 | 1e-15 | 26/29 (NCI-H460, SW1417, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +8.3 | 4e-14 | 13/29 (A-172, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.53×** | +7.8 | 1e-12 | 20/28 (A-427, SW1417, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.52×** | +7.6 | 4e-12 | 20/28 (NCI-H460, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.1 | 1e-07 | 11/28 (A-172, NCI-H23, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +5.2 | 1e-05 | 13/28 (A-427, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.6 | 3e-04 | 9/28 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.29×** | +4.2 | 0.002 | 17/30 (SW480, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.7 | 0.013 | 11/28 (BT-474, A-427, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.46×** | +3.6 | 0.017 | 9/29 (SW480, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.017 | 9/29 (A549, Panc 03.27, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.21×** | +3.3 | 0.049 | 7/28 (A-427, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.061 | 11/28 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.061 | 10/28 (SW480, SW48, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.082 | 5/28 (SW480, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.082 | 8/28 (LoVo, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.082 | 5/28 (COLO 205, A-172, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.082 | 6/28 (NCI-H2030, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.0 | 0.092 | 3/28 (A-427, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 23 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 30.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.460×** | -20.0 | 0e+00 | 26/29 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.373×** | -17.9 | 0e+00 | 28/28 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.513×** | -17.2 | 0e+00 | 23/28 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.395×** | -16.9 | 0e+00 | 27/28 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -12.1 | 8e-32 | 28/29 (KATO III, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.493×** | -11.7 | 1e-29 | 27/28 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.534×** | -11.4 | 3e-28 | 23/28 (KATO III, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.536×** | -11.4 | 5e-28 | 26/28 (SW480, BT-474, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.323×** | -10.8 | 3e-25 | 26/28 (Panc 03.27, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.523×** | -10.7 | 4e-25 | 25/28 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.555×** | -10.3 | 4e-23 | 24/28 (NCI-H23, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.540×** | -10.2 | 1e-22 | 26/28 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.573×** | -10.1 | 2e-22 | 24/28 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -8.7 | 2e-16 | 20/28 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.720×** | -8.4 | 1e-15 | 23/28 (BT-474, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -5.7 | 3e-07 | 17/28 (NCI-H460, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.779×** | -4.3 | 5e-04 | 12/28 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.769×** | -3.4 | 0.014 | 6/28 (NCI-H460, A549, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.021 | 14/28 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.837× | -3.1 | 0.036 | 2/28 (NCI-H2030, SHP-77) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.889× | -3.0 | 0.045 | 7/29 (Hs 766T, A549, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | 0.890× | -3.0 | 0.049 | 7/28 (Hs 766T, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.802×** | -2.9 | 0.070 | 8/29 (RKO, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.748×** | -2.8 | 0.086 | 8/28 (NCI-H460, RKO, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 30. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.7 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -18.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.321× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -13.5) |
| [[SW480 (line)]] | alt | 57.5 | 0 | 12 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -17.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.235× (z -15.9) |
| [[KATO III (line)]] | alt | 191 | 0 | 11 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -19.2) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -19.1) |
| [[LoVo (line)]] | wt | 153 | 0 | 11 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 74.7 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -16.8) |
| [[SW48 (line)]] | wt | 139 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.6) |
| [[COLO 205 (line)]] | alt | 133 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0703× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.8) |
| [[HT-29 (line)]] | alt | 175 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -17.1) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -15.3) |
| [[LS 180 (line)]] | wt | 178 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -15.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 134 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -22.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -18.9) |
| [[SW1417 (line)]] | alt | 49.7 | 0 | 7 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0849× (z -19.7) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -14.2) |
| [[A549 (line)]] | wt | 21.1 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[BT-474 (line)]] | alt | 142 | 0 | 6 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.467× (z -12.1) |
| [[SW 900 (line)]] | alt | 34.7 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 43.9 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -12.8) |
| [[HCT15 (line)]] | alt | 97.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -10.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -10.1) |
| [[A-427 (line)]] | wt | 62.7 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.07× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -16.1) |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0917× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[NCI-H2030 (line)]] | alt | 24.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.5) |
| [[SHP-77 (line)]] | alt | 84.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.93 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.05 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 70.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 30), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAH2]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TMEM125]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[LINC02253]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[NSUN7]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[MFSD6]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ESRP1]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MYO5C]] | +0.53 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[PRSS16]] | +0.52 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[PIP5K1B]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[OCLN]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[COL16A1]] | +0.51 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ANK3]] | +0.51 | +0.54 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLXIP]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[NAV1]] | -0.49 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[TSHZ3]] | -0.49 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[TSHZ3-AS1]] | -0.48 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[LOXL2]] | -0.48 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NUMBL]] | -0.48 | -0.43 / -0.49 | both halves | 4e-05 |  |
| [[IQCJ-SCHIP1]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ATP8B3]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TGFB1]] | -0.46 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[DENND2A]] | -0.46 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[FAM20C]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[LINC01615]] | -0.44 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 8, C 17. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPD52L1]] | B | TPD52L1 activity raises ICA1's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 3.32× lower at baseline in the lines without TPD52L1 | 0.004 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| [[FAAH2]] | B | FAAH2 activity raises ICA1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.51× lower at baseline in the lines without FAAH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[FAM83B]] | B | FAM83B activity raises ICA1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.65× lower at baseline in the lines without FAM83B | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[SLC28A3]] | B | SLC28A3 activity raises ICA1's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 2.04× lower at baseline in the lines without SLC28A3 | 0.036 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[INAVA]] | B | INAVA activity raises ICA1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.75× lower at baseline in the lines without INAVA | 0.061 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[FUT3]] | B | FUT3 activity raises ICA1's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 2.60× lower at baseline in the lines without FUT3 | 0.088 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[LINC03040]] | B | LINC03040 activity raises ICA1's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.55× lower at baseline in the lines without LINC03040 | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[NSUN7]] | B | NSUN7 activity raises ICA1's level | lines that do not express NSUN7 (22) vs lines expressing it (28) | 2.39× lower at baseline in the lines without NSUN7 | 0.094 | ⚠ within organs, on part of the lines; also absent: NEBL, KIF1A, FRMPD3; maybe low, not absent |
| [[LINC02967]] | C | LINC02967 activity raises ICA1's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 5.44× lower at baseline in the lines without LINC02967 | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[TMEM125]] | C | TMEM125 activity raises ICA1's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.52× lower at baseline in the lines without TMEM125 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14; co-absent with the target |
| [[ENPP4]] | C | ENPP4 activity raises ICA1's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 4.22× lower at baseline in the lines without ENPP4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises ICA1's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 4.33× lower at baseline in the lines without TTC22 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 9, C 6. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPD52L1]] | B | ICA1 activity raises TPD52L1's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without ICA1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[MFSD6]] | B | ICA1 activity raises MFSD6's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 2.26× lower at baseline in the lines without ICA1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[SLC44A3]] | B | ICA1 activity raises SLC44A3's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 2.16× lower at baseline in the lines without ICA1 | 0.029 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[GOLPH3L]] | B | ICA1 activity raises GOLPH3L's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without ICA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[MIR3936HG]] | B | ICA1 activity raises MIR3936HG's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without ICA1 | 0.066 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[HAX1]] | B | ICA1 activity raises HAX1's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without ICA1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[TSHZ3-AS1]] | B | ICA1 activity lowers TSHZ3-AS1's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.99× higher at baseline in the lines without ICA1 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[STK32A]] | B | ICA1 activity raises STK32A's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.41× lower at baseline in the lines without ICA1 | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | ICA1 activity raises the cells' numbers under Sodium Salicylate 0.5 µM (protects the cells) | lines that do not express ICA1 (20) vs lines expressing it (28) | the lines without ICA1: 0.86× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[KRT80]] | C | ICA1 activity raises KRT80's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without ICA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656; co-absent with the target |
| [[SAMD12]] | C | ICA1 activity raises SAMD12's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 3.61× lower at baseline in the lines without ICA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656; co-absent with the target |
| [[ENPP4]] | C | ICA1 activity raises ENPP4's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 3.21× lower at baseline in the lines without ICA1 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.7, 54.9); signed map (56.3, 5.0). **Vector** length 96.6, 29.1% of its response variance represented; |z| ≥ 3 in 945 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | -1.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +0.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -10.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.9 | -11.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -8.4 |

## What is on record

|  |  |
|---|---|
| Name | islet cell autoantigen 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:8,113,184-8,262,687 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ICAp69, ICA69 |
| Gene groups (HGNC) | AH domain containing |
| Hallmark sets | PROTEIN_SECRETION, UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05084](https://www.uniprot.org/uniprotkb/Q05084) (Islet cell autoantigen 1):

> May play a role in neurotransmitter secretion.

**Summary**, from NCBI Gene [3382](https://www.ncbi.nlm.nih.gov/gene/3382):

> This gene encodes a protein with an arfaptin homology domain that is found both in the cytosol and as membrane-bound form on the Golgi complex and immature secretory granules. This protein is believed to be an autoantigen in insulin-dependent diabetes mellitus and primary Sjogren's syndrome. Several transcript variants encoding two different isoforms have been found for this gene. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:5343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5343) · Entrez [3382](https://www.ncbi.nlm.nih.gov/gene/3382) · UniProt [Q05084](https://www.uniprot.org/uniprotkb/Q05084) · Ensembl [ENSG00000003147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003147)

## Data

Gene col 30: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 30); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 30, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 30]; `tensor/DDL_lfc|DDL_z.npy` [30]; `embed/gene_vectors.npy` [30]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 30 or target_col == 30). Every well: [[ICA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
