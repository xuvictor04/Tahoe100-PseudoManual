---
symbol: "PTPRA"
type: "gene"
col: 5357
ensembl_id: "ENSG00000132670"
name: "protein tyrosine phosphatase receptor type A"
location: "20p13"
module: 204
arm: "+"
pooled_cpm: 169.85
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# PTPRA

*protein tyrosine phosphatase receptor type A* — 20p13

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 2.04×, NCI-H2030 1.74×, SHP-77 1.44×; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 1.55×; ⚠ cell-cycle shift, explains ~2% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 1.95×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.465× (z -33.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZYG11B]] (+0.66, fdr 1e-05), [[MTM1]] (+0.65, fdr 1e-05), [[HECTD4]] (+0.64, fdr 2e-05); moves opposite to [[PURB]] (-0.57, fdr 1e-05), [[ZNF655]] (-0.57, fdr 3e-05), [[NCR3LG1]] (-0.54, fdr 3e-05).
> It is in [[Module 204]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZFPM2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5357.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (LS 180 2.04×, NCI-H2030 1.74×, SHP-77 1.44×; ⚠ cell-cycle shift, explains ~29% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 1.55×; ⚠ cell-cycle shift, explains ~2% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 1.95×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +6.1 | 6e-07 | 19/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +5.9 | 8e-07 | 19/48 (RPMI-7951, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +5.8 | 1e-06 | 16/48 (RPMI-7951, J82, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +4.5 | 0.001 | 18/50 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.10× | +4.4 | 0.001 | 2/48 (LOX-IMVI, BT-474) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.10× | +4.3 | 0.002 | 5/48 (H4, A-172, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.10× | +4.1 | 0.003 | 6/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.09× | +3.7 | 0.013 | 2/50 (LOX-IMVI, MIA PaCa-2) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.17× | +3.7 | 0.014 | 9/48 (SW48, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.08× | +3.3 | 0.049 | 0/49 | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.06× | +3.1 | 0.10 | 0/48 | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.07× | +3.0 | 0.11 | 2/47 (H4, hTERT-HPNE) | rises with dose | low cells (technical?) |
| [[AZD-8055 (drug)]] 5 µM |  | 1.14× | +3.0 | 0.11 | 4/49 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5357.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.465×** | -33.7 | 0e+00 | 47/48 (C32, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -20.8 | 0e+00 | 37/44 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.484×** | -16.7 | 0e+00 | 40/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.786×** | -15.0 | 0e+00 | 27/48 (SNU-423, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.728×** | -12.9 | 3e-36 | 34/45 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.762×** | -11.9 | 7e-31 | 31/49 (RKO, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.758×** | -11.7 | 1e-29 | 30/48 (A549, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.770×** | -11.5 | 9e-29 | 27/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.777×** | -11.1 | 6e-27 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **0.795×** | -9.7 | 1e-20 | 27/47 (SNU-423, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.805×** | -9.5 | 9e-20 | 27/48 (HOP62, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.807×** | -9.4 | 2e-19 | 26/48 (A549, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.824×** | -8.5 | 6e-16 | 25/48 (NCI-H460, A-172, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.825×** | -8.5 | 1e-15 | 25/48 (NCI-H2347, C32, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.833×** | -7.7 | 5e-13 | 24/47 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.747×** | -6.7 | 6e-10 | 26/48 (SNU-1, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.883× | -5.1 | 1e-05 | 14/47 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.911× | -4.1 | 0.001 | 1/48 (SW48) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | 0.862× | -3.4 | 0.014 | 9/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | 0.928× | -3.3 | 0.021 | 5/48 (BT-474, SNU-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.934× | -3.0 | 0.054 | 7/48 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Resveratrol (drug)]] 0.5 µM |  | 0.936× | -2.9 | 0.070 | 1/49 (CHP-212) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.937× | -2.8 | 0.086 | 1/47 (hTERT-HPNE) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.938× | -2.8 | 0.090 | 2/48 (COLO 205, AN3 CA) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.938× | -2.8 | 0.092 | 6/48 (SW 1271, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5357. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 219 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -20.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.336× (z -19.9) |
| [[HOP62 (line)]] | alt | 233 | 0 | 10 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.312× (z -27.5) |
| [[NCI-H2347 (line)]] | alt | 191 | 0 | 10 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.455× (z -15.1) |
| [[C32 (line)]] | wt | 198 | 0 | 9 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.211× (z -28.0) |
| [[NCI-H460 (line)]] | wt | 172 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.499× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.583× (z -12.4) |
| [[A549 (line)]] | wt | 227 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -15.1) |
| [[SNU-423 (line)]] | alt | 188 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -23.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.497× (z -12.9) |
| [[HS-578T (line)]] | alt | 191 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.349× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 125 | 1 (1 ⚠) | 5 (4 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.102× (z -35.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 167 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.269× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 177 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -13.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.585× (z -9.7) |
| [[LoVo (line)]] | wt | 150 | 1 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.54× (z +9.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.418× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.569× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 187 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.423× (z -16.1) |
| [[PANC-1 (line)]] | alt | 179 | 0 | 5 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.270× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 256 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.369× (z -16.8) |
| [[SNU-1 (line)]] | wt | 219 | 0 | 4 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.203× (z -11.0) |
| [[SW480 (line)]] | alt | 207 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.450× (z -21.9) |
| [[A-427 (line)]] | wt | 111 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -20.2) |
| [[A498 (line)]] | wt | 71.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -14.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 195 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.377× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 188 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.463× (z -15.5) |
| [[J82 (line)]] | alt | 137 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -13.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.323× (z -10.6) |
| [[AN3 CA (line)]] | alt | 167 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.223× (z -13.8) |
| [[BT-474 (line)]] | alt | 170 | 0 | 2 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.221× (z -12.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.511× (z -10.3) |
| [[COLO 205 (line)]] | alt | 200 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.418× (z -13.4) |
| [[HCT15 (line)]] | alt | 188 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.403× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 275 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -11.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.384× (z -15.8) |
| [[KATO III (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.434× (z -15.2) |
| [[LS 180 (line)]] | wt | 135 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +17.5) ⚠ cell-cycle shift, explains ~29% of this change | [[Auranofin (drug)]] 5 µM 0.546× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 223 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.321× (z -21.3) |
| [[NCI-H1792 (line)]] | alt | 149 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.452× (z -12.1) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.354× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.365× (z -16.0) |
| [[RKO (line)]] | wt | 229 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -14.7) |
| [[SHP-77 (line)]] | alt | 205 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +10.5) ⚠ cell-cycle shift, explains ~2% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.564× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.278× (z -18.4) |
| [[SW 900 (line)]] | alt | 169 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.363× (z -16.6) |
| [[SW1417 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.456× (z -13.6) |
| [[SW48 (line)]] | wt | 171 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.317× (z -14.6) |
| [[H4 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.438× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[Hs 766T (line)]] | wt | 205 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.499× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 129 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 92.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 232 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5357), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZYG11B]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MTM1]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[HECTD4]] | +0.64 | +0.49 / +0.70 | both halves | 2e-05 |  |
| [[CNIH4]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TBC1D12]] | +0.62 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[RNF38]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.61 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[SEC24B]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[HEATR5B]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PHAF1]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ILKAP]] | +0.60 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PURB]] | -0.57 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.57 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[NCR3LG1]] | -0.54 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[ZNF628]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[NORAD]] | -0.51 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[PCF11]] | -0.51 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[ZFPM2-AS1]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[THOC6]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[KDM6B]] | -0.51 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[RABL3]] | -0.51 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[LINC00641]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[MIS12]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFPM2-AS1]] | B | ZFPM2-AS1 activity raises PTPRA's level | lines that do not express ZFPM2-AS1 (16) vs lines expressing it (34) | 1.18× lower at baseline in the lines without ZFPM2-AS1 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: MIR3142HG, FRMD4A, TLR6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.2, -21.0); signed map (-24.9, 5.4). **Vector** length 115, 31.8% of its response variance represented; |z| ≥ 3 in 1,192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.7 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.4 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | +1.9 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -12.9 | -33.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -12.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.7 | -16.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -20.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | -5.7 | -11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:2,873,420-3,039,076 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRP, HLPR, HPTPA, RPTPA; previously PTPRL2, PTPA |
| Gene groups (HGNC) | Protein tyrosine phosphatases receptor type |
| Reactome | 6 pathways, smallest: NCAM signaling for neurite out-growth; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P18433](https://www.uniprot.org/uniprotkb/P18433) (Receptor-type tyrosine-protein phosphatase alpha):

> Tyrosine protein phosphatase which is involved in integrin-mediated focal adhesion formation (By similarity). Following integrin engagement, specifically recruits BCAR3, BCAR1 and CRK to focal adhesions thereby promoting SRC-mediated phosphorylation of BRAC1 and the subsequent activation of PAK and small GTPase RAC1 and CDC42 (By similarity).

**Summary**, from NCBI Gene [5786](https://www.ncbi.nlm.nih.gov/gene/5786):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains an extracellular domain, a single transmembrane segment and two tandem intracytoplasmic catalytic domains, and thus represents a receptor-type PTP. This PTP has been shown to dephosphorylate and activate Src family …

**Accessions** — [HGNC:9664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9664) · Entrez [5786](https://www.ncbi.nlm.nih.gov/gene/5786) · UniProt [P18433](https://www.uniprot.org/uniprotkb/P18433) · Ensembl [ENSG00000132670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132670)

## Data

Gene col 5357: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5357); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5357, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5357]; `tensor/DDL_lfc|DDL_z.npy` [5357]; `embed/gene_vectors.npy` [5357]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5357 or target_col == 5357). Every well: [[PTPRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
