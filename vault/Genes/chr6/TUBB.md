---
symbol: "TUBB"
type: "gene"
col: 12160
ensembl_id: "ENSG00000196230"
name: "tubulin beta class I"
location: "6p21.33"
module: 6
arm: "+"
pooled_cpm: 167.49
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 29
n_dd_up_clean: 8
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TUBB

*tubulin beta class I* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.34× (z +11.1, q 1e-25, up in 46 of 47 measured lines) ⚠ transcription drop. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.80× (z +10.8, q 8e-25, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.406× (z -16.5, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBA1B]] (+0.74, fdr 7e-06), [[FANCG]] (+0.70, fdr 1e-05), [[RBBP7]] (+0.69, fdr 7e-06); moves opposite to [[TERF2IP]] (-0.64, fdr 1e-05), [[GATAD1]] (-0.62, fdr 7e-06), [[CROCCP2-1]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.34×** | +11.1 | 1e-25 | 46/47 (PANC-1, LOX-IMVI, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 5 µM |  | **1.80×** | +10.8 | 8e-25 | 47/47 (C32, hTERT-HPNE, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.11×** | +9.7 | 6e-20 | 43/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.87×** | +7.8 | 6e-13 | 36/44 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.5 µM |  | **1.74×** | +7.2 | 7e-11 | 47/48 (NCI-H1792, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.53×** | +5.1 | 3e-05 | 32/45 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.40×** | +4.2 | 0.002 | 31/46 (C32, RPMI-7951, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.23×** | +3.8 | 0.009 | 26/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.029 | 33/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.032 | 29/47 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.042 | 21/47 (RKO, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.2 | 0.053 | 0/49 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.2 | 0.053 | 26/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.28×** | +3.2 | 0.053 | 28/47 (HOP62, H4, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.19× | +3.2 | 0.053 | 22/47 (SW480, HOP62, …) | top dose only |  |
| [[Triclosan (drug)]] 5 µM |  | 1.19× | +3.2 | 0.053 | 22/48 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.057 | 27/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.065 | 28/47 (C32, NCI-H1792, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.067 | 23/47 (HepG2/C3A, AsPC-1, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +2.9 | 0.091 | 23/47 (NCI-H1792, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.406×** | -16.5 | 0e+00 | 44/47 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -10.8 | 6e-25 | 45/47 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -9.8 | 2e-20 | 42/48 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.516×** | -8.3 | 2e-14 | 41/47 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.579×** | -7.1 | 2e-10 | 44/47 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.598×** | -6.7 | 2e-09 | 42/47 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.602×** | -6.6 | 4e-09 | 42/47 (HEC-1-A, LoVo, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | **0.605×** | -6.2 | 5e-08 | 37/47 (HEC-1-A, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.634×** | -5.9 | 2e-07 | 34/47 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.650×** | -5.6 | 1e-06 | 37/48 (HEC-1-A, C-33 A, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.668×** | -5.2 | 9e-06 | 40/46 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.754×** | -5.2 | 1e-05 | 31/47 (A-427, LS 180, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.673×** | -5.1 | 1e-05 | 32/47 (J82, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -5.0 | 3e-05 | 34/47 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.685×** | -4.9 | 3e-05 | 31/46 (NCI-H2030, C-33 A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.693×** | -4.8 | 6e-05 | 36/47 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.681×** | -4.6 | 1e-04 | 35/47 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.001 | 26/47 (SW48, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 183 | 2 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 1.90× (z +8.9) | [[Mebendazole (drug)]] 5 µM 0.305× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 213 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.0) |
| [[J82 (line)]] | alt | 374 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.435× (z -10.4) |
| [[BT-474 (line)]] | alt | 161 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.4) |
| [[C-33 A (line)]] | alt | 215 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -20.5) |
| [[LS 180 (line)]] | wt | 150 | 1 (1 ⚠) | 5 (1 ⚠) | [[Docetaxel (drug)]] 0.05 µM 2.83× (z +8.6) ⚠ transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 120 | 2 (1 ⚠) | 4 | [[Docetaxel (drug)]] 5 µM 2.02× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -15.3) |
| [[A498 (line)]] | wt | 187 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.4) |
| [[H4 (line)]] | wt | 283 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -17.1) |
| [[LoVo (line)]] | wt | 101 | 2 (1 ⚠) | 3 | [[Docetaxel (drug)]] 0.05 µM 2.90× (z +9.4) ⚠ transcription drop · without an alert: [[Docetaxel (drug)]] 5 µM 2.07× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 215 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -16.9) |
| [[PANC-1 (line)]] | alt | 172 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.04× (z +10.2) | — |
| [[RKO (line)]] | wt | 123 | 2 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.09× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 151 | 3 (2 ⚠) | 2 | [[Docetaxel (drug)]] 5 µM 2.56× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.2) |
| [[SW 900 (line)]] | alt | 99.7 | 2 (1 ⚠) | 3 | [[Docetaxel (drug)]] 0.05 µM 3.44× (z +10.6) ⚠ transcription drop · without an alert: [[Docetaxel (drug)]] 5 µM 2.07× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -10.4) |
| [[A-427 (line)]] | wt | 194 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.5) |
| [[A549 (line)]] | wt | 150 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 241 | 1 | 3 | [[Docetaxel (drug)]] 5 µM 1.79× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.7) |
| [[HT-29 (line)]] | alt | 87.8 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.26× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.5) |
| [[SNU-1 (line)]] | wt | 161 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -16.2) |
| [[SW48 (line)]] | wt | 231 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -10.8) |
| [[SW480 (line)]] | alt | 180 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -19.7) |
| [[A-172 (line)]] | wt | 210 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -13.3) |
| [[AN3 CA (line)]] | alt | 376 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 97.9 | 1 (1 ⚠) | 2 | [[Docetaxel (drug)]] 0.05 µM 2.44× (z +8.9) ⚠ transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -15.6) |
| [[C32 (line)]] | wt | 84.6 | 3 (2 ⚠) | 0 | [[Docetaxel (drug)]] 5 µM 3.49× (z +12.2) | — |
| [[HCT15 (line)]] | alt | 185 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.6) |
| [[HepG2_C3A (line)]] | wt | 131 | 2 (1 ⚠) | 1 | [[Docetaxel (drug)]] 5 µM 2.42× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.9) |
| [[HOP62 (line)]] | alt | 229 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -15.6) |
| [[KATO III (line)]] | alt | 131 | 1 (1 ⚠) | 2 | [[Docetaxel (drug)]] 0.05 µM 2.93× (z +10.2) ⚠ transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 159 | 2 (1 ⚠) | 1 | [[Docetaxel (drug)]] 0.05 µM 3.28× (z +11.0) ⚠ transcription drop · without an alert: [[Docetaxel (drug)]] 5 µM 2.31× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 82.3 | 3 (1 ⚠) | 0 | [[Docetaxel (drug)]] 5 µM 2.73× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 179 | 2 (1 ⚠) | 1 (1 ⚠) | [[Docetaxel (drug)]] 5 µM 2.46× (z +10.9) | [[Daptomycin (drug)]] 0.05 µM 0.354× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 157 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 150 | 1 | 2 | [[Docetaxel (drug)]] 5 µM 1.90× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 201 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -14.4) |
| [[SNU-423 (line)]] | alt | 302 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 1.95× (z +9.6) | — |
| [[CHP-212 (line)]] | wt | 148 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 170 | 1 | 1 | [[Docetaxel (drug)]] 5 µM 2.50× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.8) |
| [[SW1417 (line)]] | alt | 124 | 1 (1 ⚠) | 1 | [[Docetaxel (drug)]] 0.05 µM 2.53× (z +10.0) ⚠ transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -13.3) |
| [[Hs 766T (line)]] | wt | 157 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 170 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBA1B]] | +0.74 | +0.75 / +0.76 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 999 |
| [[FANCG]] | +0.70 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[RBBP7]] | +0.69 | +0.70 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MAD2L1]] | +0.68 | +0.74 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 573 |
| [[TUBG1]] | +0.68 | +0.76 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 629 |
| [[NCAPG2]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[CS]] | +0.67 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[PRKDC]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RFC5]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[PARP1]] | +0.65 | +0.57 / +0.44 | both halves | 3e-05 | STRING 423 |
| [[NCAPD3]] | +0.65 | +0.71 / +0.46 | both halves | 2e-05 |  |
| [[NONO]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 | STRING 595 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.64 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.60 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[SEC62]] | -0.60 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[RPS27L]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[EIF3J-DT]] | -0.59 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[GADD45A]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[WHAMM]] | -0.58 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[XPC]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[WBP4]] | -0.57 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[FAM98C]] | -0.57 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ATE1OSP]] | -0.57 | -0.62 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises TUBB's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without TCF19 | 0.010 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[PBK]] | C | PBK activity raises TUBB's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without PBK | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CRTAP]] | C | CRTAP activity raises TUBB's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without CRTAP | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[MCM3]] | C | MCM3 activity raises TUBB's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[MELK]] | C | MELK activity raises TUBB's level | lines that do not express MELK (3) vs lines expressing it (47) | 1.84× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises TUBB's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[PLP2]] | C | PLP2 activity raises TUBB's level | lines that do not express PLP2 (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without PLP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: OTULINL, C12orf75; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.4, -40.8); signed map (-30.3, -42.8). **Vector** length 116, 38.0% of its response variance represented; |z| ≥ 3 in 1,592 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective pyroptosis* (reactome, mean cos +0.51 to 7); *Diseases of programmed cell death* (reactome, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | -5.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | -5.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +4.2 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.5 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -10.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.5 | -0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -16.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.7 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -0.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.6 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin beta class I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,717,435-30,725,538 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OK/SW-cl.56, MGC16435, M40, Tubb5 |
| Gene groups (HGNC) | Tubulin beta family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 22 pathways, smallest: Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome; AURKA Activation by TPX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P07437](https://www.uniprot.org/uniprotkb/P07437) (Tubulin beta chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [203068](https://www.ncbi.nlm.nih.gov/gene/203068):

> This gene encodes a beta tubulin protein. This protein forms a dimer with alpha tubulin and acts as a structural component of microtubules. Mutations in this gene cause cortical dysplasia, complex, with other brain malformations 6. Alternative splicing results in multiple splice variants. There are multiple pseudogenes for this gene on chromosomes 1, 6, 7, 8, 9, and 13. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:20778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20778) · Entrez [203068](https://www.ncbi.nlm.nih.gov/gene/203068) · UniProt [P07437](https://www.uniprot.org/uniprotkb/P07437) · Ensembl [ENSG00000196230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196230)

## Data

Gene col 12160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12160); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12160]; `tensor/DDL_lfc|DDL_z.npy` [12160]; `embed/gene_vectors.npy` [12160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12160 or target_col == 12160). Every well: [[TUBB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
