---
symbol: "NEDD4"
type: "gene"
col: 928
ensembl_id: "ENSG00000069869"
name: "NEDD4 E3 ubiquitin protein ligase"
location: "15q21.3"
module: 28
arm: "+"
pooled_cpm: 147.03
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NEDD4

*NEDD4 E3 ubiquitin protein ligase* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +36.6, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.459× (z -24.6, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD50]] (+0.66, fdr 1e-05), [[ZC3H12C]] (+0.59, fdr 1e-05), [[OCIAD1]] (+0.57, fdr 3e-05); moves opposite to [[NFATC3]] (-0.58, fdr 1e-05), [[TIMM10B]] (-0.56, fdr 2e-05), [[SDHAP4]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 928.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +36.6 | 0e+00 | 40/47 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +20.2 | 0e+00 | 42/47 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +14.6 | 0e+00 | 40/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +7.7 | 2e-12 | 22/47 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +5.9 | 3e-07 | 22/46 (A498, COLO 205, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +5.9 | 3e-07 | 20/47 (A498, A-172, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.11× | +4.8 | 1e-04 | 12/47 (LS 180, SW480, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +4.8 | 1e-04 | 19/48 (AN3 CA, HS-578T, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +4.7 | 2e-04 | 16/47 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.31×** | +4.4 | 6e-04 | 22/48 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +4.3 | 8e-04 | 15/48 (A498, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.14× | +4.2 | 0.001 | 17/48 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +3.8 | 0.007 | 7/47 (BT-474, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.12× | +3.7 | 0.008 | 13/47 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.12× | +3.6 | 0.012 | 10/46 (COLO 205, A498, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.12× | +3.6 | 0.012 | 11/48 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.076 | 5/47 (CFPAC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.091 | 5/47 (HS-578T, HEC-1-A, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 928.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.459×** | -24.6 | 0e+00 | 46/47 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -23.1 | 0e+00 | 46/48 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.514×** | -19.5 | 0e+00 | 43/47 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -16.4 | 0e+00 | 40/47 (A549, J82, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -9.9 | 3e-21 | 30/47 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.734×** | -9.4 | 7e-19 | 33/47 (C32, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.745×** | -8.9 | 5e-17 | 30/46 (H4, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.765×** | -8.1 | 3e-14 | 27/49 (H4, LOX-IMVI, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.794×** | -7.3 | 2e-11 | 29/47 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.824×** | -5.6 | 1e-06 | 23/47 (C32, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.837× | -5.3 | 7e-06 | 23/47 (H4, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | 0.855× | -4.9 | 4e-05 | 21/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.814×** | -4.6 | 2e-04 | 16/46 (Hs 766T, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.867× | -4.5 | 3e-04 | 19/47 (H4, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.788×** | -3.9 | 0.003 | 16/44 (A549, H4, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.916× | -3.9 | 0.004 | 13/47 (A549, COLO 205, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.900× | -3.3 | 0.030 | 8/47 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.5 µM |  | 0.904× | -3.2 | 0.045 | 3/47 (HCT15, SHP-77, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.936× | -2.9 | 0.087 | 1/48 (SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 928. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 450 | 3 | 11 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -30.6) |
| [[NCI-H460 (line)]] | wt | 166 | 8 (3 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -17.4) |
| [[PANC-1 (line)]] | alt | 152 | 2 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.84× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.370× (z -18.2) |
| [[A498 (line)]] | wt | 288 | 4 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.51× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -17.9) |
| [[H4 (line)]] | wt | 387 | 1 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -17.3) |
| [[J82 (line)]] | alt | 148 | 5 (3 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +26.0) | [[Panobinostat (drug)]] 5 µM 0.379× (z -15.0) |
| [[RKO (line)]] | wt | 157 | 1 (1 ⚠) | 7 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.98× (z +8.5) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.360× (z -13.1) |
| [[HS-578T (line)]] | alt | 72.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +23.0) | — |
| [[hTERT-HPNE (line)]] | wt | 203 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.262× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 415 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -19.9) |
| [[SNU-423 (line)]] | alt | 162 | 3 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +22.4) | [[Panobinostat (drug)]] 5 µM 0.296× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 119 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +27.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -13.1) |
| [[C32 (line)]] | wt | 244 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -17.7) |
| [[COLO 205 (line)]] | alt | 143 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +17.9) | [[Panobinostat (drug)]] 5 µM 0.298× (z -13.4) |
| [[LS 180 (line)]] | wt | 95.8 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.393× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 123 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 286 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.00× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -11.4) |
| [[SW480 (line)]] | alt | 102 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.513× (z -11.5) |
| [[A-172 (line)]] | wt | 235 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +16.9) | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 208 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +21.6) | [[Panobinostat (drug)]] 5 µM 0.503× (z -9.7) |
| [[HOP62 (line)]] | alt | 84.1 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +23.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.9) |
| [[A-427 (line)]] | wt | 70.6 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +20.9) | [[Panobinostat (drug)]] 5 µM 0.430× (z -10.6) |
| [[HT-29 (line)]] | alt | 127 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +21.1) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 54.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +20.5) | [[Belinostat (drug)]] 5 µM 0.430× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 81.3 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +29.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H2347 (line)]] | alt | 65.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +21.5) | — |
| [[Panc 03.27 (line)]] | alt | 96.4 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +24.6) | [[Panobinostat (drug)]] 5 µM 0.472× (z -8.6) |
| [[Hs 766T (line)]] | wt | 59.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 213 | 3 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.63× (z +10.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.54× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 121 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.99× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.72× (z +9.5) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -9.2) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW 1271 (line)]] | alt | 590 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -15.0) |
| [[SW1417 (line)]] | alt | 110 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -14.8) |
| [[BT-474 (line)]] | alt | 59.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +22.6) | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 78.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 80.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +19.5) | — |
| [[LoVo (line)]] | wt | 96.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +16.0) | — |
| [[SHP-77 (line)]] | alt | 58.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.106× (z -11.7) ⚠ toxic |
| [[SW 900 (line)]] | alt | 76.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.0) | — |
| [[AN3 CA (line)]] | alt | 99.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +12.1) | — |
| [[C-33 A (line)]] | alt | 131 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -9.8) |
| [[SW 1088 (line)]] | alt | 228 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0692× (z -12.4) |
| [[CHP-212 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 928), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD50]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ZC3H12C]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[OCIAD1]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[LACTB2]] | +0.55 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[OXTR]] | +0.55 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[DARS1]] | +0.55 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[SYNE1]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CCDC25]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[EBI3]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PTX3]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RBMS3]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[DZIP3]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFATC3]] | -0.58 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[SDHAP4]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CAPN10]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CCT6P3-1]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TUSC2]] | -0.54 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ATPAF2]] | -0.54 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[UBE2G1]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SAP130]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[SDHA]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[GUCD1]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 | STRING 458 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NEDD4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (25.3, 9.8); signed map (16.7, -9.7). **Vector** length 121, 33.6% of its response variance represented; |z| ≥ 3 in 1,479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +12.6 | +36.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +12.4 | +20.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.0 | +14.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +5.8 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +7.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.5 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.9 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -23.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.4 | -9.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -5.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -24.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -19.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -1.5 |
|  | [[8-Hydroxyquinoline (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Arbutin (drug)]] 0.5 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | NEDD4 E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:55,826,922-55,993,660 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0093, MGC176705, NEDD4-1, RPF1 |
| Gene groups (HGNC) | Nedd4 family E3 ubiquitin protein ligases |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 15 pathways, smallest: Downregulation of ERBB4 signaling; Regulation of PTEN localization; Signaling by ERBB4 |
| Matched by | ensembl_id |

**Function**, from UniProt [P46934](https://www.uniprot.org/uniprotkb/P46934) (E3 ubiquitin-protein ligase NEDD4):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Specifically ubiquitinates 'Lys-63' in target proteins. Involved in the pathway leading to the degradation of VEGFR-2/KDFR, independently of its ubiquitin-ligase activity. Monoubiquitinates IGF1R at multiple sites, thus leading to receptor internalization and degradation in lysosomes (By similarity). …

**Summary**, from NCBI Gene [4734](https://www.ncbi.nlm.nih.gov/gene/4734):

> This gene is the founding member of the NEDD4 family of HECT ubiquitin ligases that function in the ubiquitin proteasome system of protein degradation. The encoded protein contains an N-terminal calcium and phospholipid binding C2 domain followed by multiple tryptophan-rich WW domains and, a C-terminal HECT ubiquitin ligase catalytic domain. It plays critical role in the regulation of a number of membrane receptors, endocytic machinery components and the tumor suppressor PTEN. [provided by …

**Accessions** — [HGNC:7727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7727) · Entrez [4734](https://www.ncbi.nlm.nih.gov/gene/4734) · UniProt [P46934](https://www.uniprot.org/uniprotkb/P46934) · Ensembl [ENSG00000069869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069869)

## Data

Gene col 928: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 928); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 928, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 928]; `tensor/DDL_lfc|DDL_z.npy` [928]; `embed/gene_vectors.npy` [928]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 928 or target_col == 928). Every well: [[NEDD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEDD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
