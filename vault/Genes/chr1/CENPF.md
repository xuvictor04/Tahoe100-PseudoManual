---
symbol: "CENPF"
type: "gene"
col: 3946
ensembl_id: "ENSG00000117724"
name: "centromere protein F"
location: "1q41"
module: 22
arm: "+"
pooled_cpm: 355.0
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 26
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CENPF

*centromere protein F* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +14.1, q 3e-42, up in 36 of 46 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.38× (z +4.0, q 0.003, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (17 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.470× (z -12.9, q 2e-35, down in 45 of 46 measured lines) ⚠ cell-cycle shift, explains ~80% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.613× (z -6.0, q 2e-07, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPE]] (+0.94, fdr 7e-06), [[DLGAP5]] (+0.93, fdr 7e-06), [[ASPM]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.27×** | +14.1 | 3e-42 | 36/46 (NCI-H2347, NCI-H2030, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **2.49×** | +10.9 | 5e-25 | 42/46 (NCI-H2347, PANC-1, …) | rises with dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **3.43×** | +8.0 | 3e-13 | 41/45 (J82, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.51×** | +7.2 | 9e-11 | 42/46 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.74×** | +6.9 | 7e-10 | 41/46 (HT-29, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.62×** | +6.0 | 2e-07 | 30/46 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.58×** | +5.6 | 1e-06 | 31/46 (hTERT-HPNE, PANC-1, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.43×** | +4.5 | 6e-04 | 35/46 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.43×** | +4.4 | 6e-04 | 26/46 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.003 | 30/46 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.34×** | +3.6 | 0.014 | 23/45 (A549, LoVo, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.016 | 23/46 (HT-29, NCI-H2347, …) | all doses, flat |  |
| [[Thymol (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.016 | 23/46 (NCI-H460, SW 900, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.4 | 0.025 | 25/46 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +3.4 | 0.027 | 22/46 (KATO III, hTERT-HPNE, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.027 | 27/46 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.045 | 21/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.048 | 24/46 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.050 | 24/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.060 | 23/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.078 | 24/46 (MIA PaCa-2, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.470×** | -12.9 | 2e-35 | 45/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.641×** | -7.6 | 7e-12 | 29/47 (A498, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.552×** | -7.3 | 6e-11 | 37/46 (C32, SW48, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.504×** | -7.2 | 8e-11 | 44/46 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.556×** | -6.9 | 4e-10 | 42/46 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.481×** | -6.2 | 4e-08 | 36/46 (C32, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -6.0 | 2e-07 | 32/46 (SHP-77, A-427, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.630×** | -5.7 | 1e-06 | 40/46 (SW48, SNU-1, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.729×** | -5.5 | 3e-06 | 30/46 (A498, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -5.0 | 3e-05 | 31/46 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.672×** | -4.9 | 5e-05 | 37/46 (SNU-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **0.664×** | -4.8 | 6e-05 | 30/45 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.632×** | -4.8 | 6e-05 | 30/46 (A498, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | **0.476×** | -4.8 | 7e-05 | 34/43 (C32, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.685×** | -4.6 | 1e-04 | 36/47 (HT-29, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.713×** | -4.1 | 0.001 | 26/46 (C32, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.713×** | -3.7 | 0.006 | 27/45 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.805×** | -3.7 | 0.006 | 24/46 (RKO, HCT15, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.743×** | -3.3 | 0.029 | 21/46 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.608×** | -3.2 | 0.034 | 25/46 (SW48, A549, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.619×** | -3.1 | 0.049 | 24/46 (BT-474, A498, …) | top dose only | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.776×** | -3.0 | 0.052 | 22/46 (NCI-H460, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -3.0 | 0.059 | 24/46 (A-427, C32, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +1.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 760 | 1 (1 ⚠) | 12 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.218× (z -16.7) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.364× (z -11.2) |
| [[SW48 (line)]] | wt | 419 | 0 | 9 (5 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.339× (z -11.2) |
| [[A-172 (line)]] | wt | 482 | 2 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.271× (z -15.5) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.390× (z -11.3) |
| [[A498 (line)]] | wt | 423 | 0 | 8 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.154× (z -24.0) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.380× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 292 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.206× (z -17.5) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.387× (z -10.7) |
| [[H4 (line)]] | wt | 439 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.159× (z -16.3) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.303× (z -10.7) |
| [[KATO III (line)]] | alt | 200 | 6 (6 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.21× (z +11.3) ⚠ cell-cycle shift, explains ~88% of this change | — |
| [[LS 180 (line)]] | wt | 275 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.141× (z -16.8) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.286× (z -10.9) |
| [[A549 (line)]] | wt | 279 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +20.2) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.446× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 230 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.340× (z -10.7) ⚠ cell-cycle shift, explains ~80% of this change |
| [[A-427 (line)]] | wt | 417 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.199× (z -20.2) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.262× (z -17.1) |
| [[HOP62 (line)]] | alt | 531 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.397× (z -12.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[NCI-H2347 (line)]] | alt | 270 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +29.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 741 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.285× (z -11.0) |
| [[SNU-1 (line)]] | wt | 363 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 181 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.428× (z -9.1) ⚠ cell-cycle shift, explains ~80% of this change |
| [[HS-578T (line)]] | alt | 219 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.381× (z -9.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[LoVo (line)]] | wt | 188 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.403× (z -10.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[NCI-H2030 (line)]] | alt | 279 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +22.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 363 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.318× (z -13.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[Panc 03.27 (line)]] | alt | 253 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +20.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.326× (z -13.0) ⚠ cell-cycle shift, explains ~80% of this change |
| [[PANC-1 (line)]] | alt | 556 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +18.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 327 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +16.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.505× (z -9.0) ⚠ cell-cycle shift, explains ~80% of this change |
| [[HT-29 (line)]] | alt | 299 | 1 (1 ⚠) | 1 (1 ⚠) | [[Docetaxel (drug)]] 0.05 µM 3.53× (z +9.3) ⚠ transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.351× (z -10.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[J82 (line)]] | alt | 497 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 331 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.84× (z +9.3) ⚠ cell-cycle shift, explains ~88% of this change | [[Selinexor (drug)]] 5 µM 0.455× (z -10.1) ⚠ cell-cycle shift, explains ~80% of this change |
| [[RKO (line)]] | wt | 298 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +18.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 403 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +15.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 232 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 395 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.376× (z -8.9) ⚠ cell-cycle shift, explains ~80% of this change |
| [[MIA PaCa-2 (line)]] | alt | 521 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.406× (z -8.9) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SNU-423 (line)]] | alt | 310 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 468 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 808 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 72.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 518 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 447 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 281 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 240 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 541 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 578 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 470 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPE]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[DLGAP5]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 976 |
| [[ASPM]] | +0.92 | +0.93 / +0.94 | both halves | 7e-06 | STRING 987 |
| [[TOP2A]] | +0.92 | +0.93 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 974 |
| [[MKI67]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 979 |
| [[CKAP2]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | STRING 934 |
| [[NDC80]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 987 |
| [[CCNB1]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 988 |
| [[DEPDC1]] | +0.90 | +0.92 / +0.92 | both halves | 7e-06 | STRING 844 |
| [[TPX2]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 954 |
| [[KIF23]] | +0.90 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 930 |
| [[KIF4A]] | +0.89 | +0.91 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 879 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CENPF's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.97× lower at baseline in the lines without PIMREG | 0.001 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[HYLS1]] | B | HYLS1 activity raises CENPF's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without HYLS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CENPF's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.61× lower at baseline in the lines without AURKB | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises CENPF's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.62× lower at baseline in the lines without PBK | 0.009 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[NDC80]] | C | NDC80 activity raises CENPF's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.23× lower at baseline in the lines without NDC80 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[SKA3]] | C | SKA3 activity raises CENPF's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.78× lower at baseline in the lines without SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises CENPF's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.21× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises CENPF's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises CENPF's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CENPF's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.80× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.925). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.0, -56.5); signed map (-50.4, -43.6). **Vector** length 187, 80.8% of its response variance represented; |z| ≥ 3 in 1,598 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.71 to 46); *Cyclin A/B1/B2 associated events during G2/M transition* (reactome, mean cos +0.74 to 12); *AURKA Activation by TPX2* (reactome, mean cos +0.69 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +10.3 | +14.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +8.6 | +10.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +7.4 | +8.0 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +7.3 | +7.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +6.3 | +6.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.4 | +3.6 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.8 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.5 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.3 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -10.5 | -12.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | -9.1 | -4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | -9.0 | -6.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.9 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -8.8 | -7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -6.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -6.4 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -4.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.2 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -4.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:214,603,185-214,664,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hcp-1 |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 20 pathways, smallest: Polo-like kinase mediated events; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores |
| Matched by | ensembl_id |

**Function**, from UniProt [P49454](https://www.uniprot.org/uniprotkb/P49454) (Centromere protein F):

> Required for kinetochore function and chromosome segregation in mitosis. Required for kinetochore localization of dynein, LIS1, NDE1 and NDEL1. Regulates recycling of the plasma membrane by acting as a link between recycling vesicles and the microtubule network though its association with STX4 and SNAP25. Acts as a potential inhibitor of pocket protein-mediated cellular processes during development by regulating the activity of RB proteins during cell division and proliferation. May play a …

**Summary**, from NCBI Gene [1063](https://www.ncbi.nlm.nih.gov/gene/1063):

> This gene encodes a protein that associates with the centromere-kinetochore complex. The protein is a component of the nuclear matrix during the G2 phase of interphase. In late G2 the protein associates with the kinetochore and maintains this association through early anaphase. It localizes to the spindle midzone and the intracellular bridge in late anaphase and telophase, respectively, and is thought to be subsequently degraded. The localization of this protein suggests that it may play a role …

**Accessions** — [HGNC:1857](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1857) · Entrez [1063](https://www.ncbi.nlm.nih.gov/gene/1063) · UniProt [P49454](https://www.uniprot.org/uniprotkb/P49454) · Ensembl [ENSG00000117724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117724)

## Data

Gene col 3946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3946); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3946]; `tensor/DDL_lfc|DDL_z.npy` [3946]; `embed/gene_vectors.npy` [3946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3946 or target_col == 3946). Every well: [[CENPF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
