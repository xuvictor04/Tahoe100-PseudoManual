---
symbol: "DYNC2H1"
type: "gene"
col: 11904
ensembl_id: "ENSG00000187240"
name: "dynein cytoplasmic 2 heavy chain 1"
location: "11q22.3"
module: 17
arm: "+"
pooled_cpm: 75.4
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 35
n_dd_up_clean: 16
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 20
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DYNC2H1

*dynein cytoplasmic 2 heavy chain 1* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +10.9, q 6e-25, up in 30 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.583× (z -12.9, q 2e-35, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIXDC1]] (+0.66, fdr 1e-05), [[SPATA6]] (+0.63, fdr 4e-05), [[BBS5]] (+0.63, fdr 4e-05); moves opposite to [[TLNRD1]] (-0.61, fdr 1e-05), [[GCNT4]] (-0.58, fdr 4e-05), [[LINC01829]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CCNYL2]], [[CCNYL2-1]] → it (grade B ⚠); 20 go from it, the strongest it → [[NPHP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +10.9 | 6e-25 | 30/40 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +9.8 | 5e-20 | 30/40 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +9.3 | 3e-18 | 29/40 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.35×** | +7.2 | 1e-10 | 28/40 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +6.6 | 6e-09 | 31/40 (A498, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +6.3 | 3e-08 | 24/40 (HT-29, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +5.6 | 1e-06 | 33/41 (HT-29, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.34×** | +4.9 | 6e-05 | 27/40 (RKO, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 4e-04 | 23/40 (RPMI-7951, A-427, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.75×** | +4.5 | 4e-04 | 23/41 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 5e-04 | 20/40 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.39×** | +4.3 | 7e-04 | 22/41 (NCI-H1573, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.30×** | +3.9 | 0.004 | 19/42 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 18/40 (SW480, HT-29, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.005 | 22/39 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.006 | 20/42 (HEC-1-A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.006 | 16/40 (hTERT-HPNE, NCI-H1792, …) | all doses, flat |  |
| [[Afatinib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.008 | 12/41 (PANC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.583×** | -12.9 | 2e-35 | 34/40 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.561×** | -9.8 | 4e-20 | 33/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -9.7 | 5e-20 | 30/39 (LOX-IMVI, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.586×** | -9.0 | 2e-17 | 36/40 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.586×** | -8.7 | 4e-16 | 33/40 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.610×** | -8.4 | 6e-15 | 32/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.611×** | -8.3 | 6e-15 | 29/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.622×** | -8.0 | 8e-14 | 30/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.631×** | -7.8 | 5e-13 | 30/41 (C-33 A, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.636×** | -7.1 | 9e-11 | 28/38 (C-33 A, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -7.0 | 2e-10 | 29/42 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.748×** | -6.9 | 2e-10 | 29/41 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.664×** | -6.9 | 2e-10 | 29/40 (CFPAC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.695×** | -6.1 | 3e-08 | 30/40 (RKO, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.697×** | -6.1 | 4e-08 | 31/40 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -5.6 | 6e-07 | 25/40 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -5.4 | 3e-06 | 25/40 (CFPAC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.731×** | -5.3 | 4e-06 | 26/39 (MIA PaCa-2, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.2 | 7e-06 | 23/40 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.761×** | -4.4 | 2e-04 | 25/39 (H4, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.705×** | -4.2 | 6e-04 | 23/40 (CFPAC-1, NCI-H1792, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.840× | -4.2 | 7e-04 | 16/41 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.841× | -4.1 | 7e-04 | 16/40 (SK-MEL-2, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 123 | 3 | 15 (13 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.257× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.421× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 107 | 2 | 13 (9 ⚠) | [[Belinostat (drug)]] 5 µM 2.03× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 14 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -14.5) |
| [[HT-29 (line)]] | alt | 39.2 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.73× (z +12.9) | [[Digitoxin (drug)]] 5 µM 0.191× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-423 (line)]] | alt | 91.4 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -14.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -12.6) |
| [[SW480 (line)]] | alt | 31.8 | 2 | 5 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.70× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -11.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 185 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -11.6) |
| [[C32 (line)]] | wt | 100 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -15.2) |
| [[C-33 A (line)]] | alt | 247 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -24.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -9.3) |
| [[H4 (line)]] | wt | 134 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 46.0 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.84× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -9.4) |
| [[RKO (line)]] | wt | 172 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -14.3) |
| [[SW1417 (line)]] | alt | 33.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 341 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 148 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 61.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.217× (z -11.4) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.319× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 29.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 56.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A549 (line)]] | wt | 99.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.8) |
| [[AN3 CA (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0826× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -9.1) |
| [[Hs 766T (line)]] | wt | 53.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.32× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.325× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 181 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 86.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 25.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.80× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.254× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 1271 (line)]] | alt | 261 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -9.3) |
| [[A-427 (line)]] | wt | 58.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 34.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 65.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -11.5) |
| [[SHP-77 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 78.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIXDC1]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SPATA6]] | +0.63 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[BBS5]] | +0.63 | +0.43 / +0.66 | both halves | 4e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 424 |
| [[EHMT2]] | +0.61 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[IRAK1BP1]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[TTC26]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 411 |
| [[SKIC3]] | +0.60 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[TBC1D19]] | +0.59 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[NPHP1]] | +0.59 | +0.44 / +0.47 | both halves | 3e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 437 |
| [[IFTAP]] | +0.59 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZC4H2]] | +0.58 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[POT1]] | +0.57 | +0.37 / +0.55 | both halves | 8e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | -0.61 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[GCNT4]] | -0.58 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[LINC01829]] | -0.56 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SAP30L-AS1]] | -0.55 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[QRICH2]] | -0.54 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[SLC20A2]] | -0.54 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MAP3K14-AS1]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.53 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[SIAH2-AS1]] | -0.53 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[LINC01588]] | -0.53 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[NACC2]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SMUG1]] | -0.53 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCNYL2]], [[CCNYL2-1]] | B | CCNYL2, CCNYL2-1 activity raises DYNC2H1's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 2.55× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent genes |
| [[TOP2A]] | B | TOP2A activity raises DYNC2H1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANK2]] | B | ANK2 activity raises DYNC2H1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.98× lower at baseline in the lines without ANK2 | 0.051 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[DMXL2]] | C | DMXL2 activity raises DYNC2H1's level | lines that do not express DMXL2 (3) vs lines expressing it (47) | 5.83× lower at baseline in the lines without DMXL2 | 0.060 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: PPP2R3A, CCDC102A, ENSG00000250264 |
| [[TBC1D19]] | C | TBC1D19 activity raises DYNC2H1's level | lines that do not express TBC1D19 (4) vs lines expressing it (46) | 6.48× lower at baseline in the lines without TBC1D19 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 17, C 3. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPHP1]] | B | DYNC2H1 activity raises NPHP1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.86× lower at baseline in the lines without DYNC2H1 | 0.009 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[TTC26]] | B | DYNC2H1 activity raises TTC26's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without DYNC2H1 | 0.010 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[UBE2R2-AS1]] | B | DYNC2H1 activity lowers UBE2R2-AS1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.20× higher at baseline in the lines without DYNC2H1 | 0.010 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[TMEM67]] | B | DYNC2H1 activity raises TMEM67's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 3.47× lower at baseline in the lines without DYNC2H1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[POT1]] | B | DYNC2H1 activity raises POT1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without DYNC2H1 | 0.032 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[IFT172]] | B | DYNC2H1 activity raises IFT172's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.84× lower at baseline in the lines without DYNC2H1 | 0.034 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[ODF2L]] | B | DYNC2H1 activity raises ODF2L's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without DYNC2H1 | 0.036 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[TUBG2]] | B | DYNC2H1 activity raises TUBG2's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without DYNC2H1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[ARL6]] | B | DYNC2H1 activity raises ARL6's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 3.33× lower at baseline in the lines without DYNC2H1 | 0.057 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[UBE2R2-AS1]] | B | DYNC2H1 activity strengthens UBE2R2-AS1's drug response | lines that do not express DYNC2H1 (8) vs lines expressing it (39) | the lines without DYNC2H1 respond 0.35× as strongly (z diff +1.98); strongest at Dinaciclib 0.5 µM: 0.69x vs 2.54x (z diff +5.5) | 0.058 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798; target measured in part of the lines; artifact flags |
| [[HNRNPDL]] | B | DYNC2H1 activity weakens HNRNPDL's drug response | lines that do not express DYNC2H1 (8) vs lines expressing it (41) | the lines without DYNC2H1 respond 1.26× as strongly (z diff -1.01); strongest at Ouabain (Octahydrate) 5 µM: 2.41x vs 1.63x (z diff -3.1) | 0.068 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798; target measured in part of the lines; artifact flags |
| [[TLNRD1]] | B | DYNC2H1 activity lowers TLNRD1's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 1.61× higher at baseline in the lines without DYNC2H1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.0, -0.8); signed map (-26.7, -11.0). **Vector** length 106, 32.6% of its response variance represented; |z| ≥ 3 in 1,371 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.8 | +7.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +9.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +4.4 | +4.9 |
|  | [[NG25 (drug)]] 5 µM |  | +4.3 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | +5.6 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.4 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -9.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.6 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | dynein cytoplasmic 2 heavy chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:103,109,410-103,479,863 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hdhc11, DHC2, DHC1b, DYH1B; previously DNCH2 |
| Gene groups (HGNC) | Dynein 2 complex subunits; Dynein heavy chains |
| Reactome | 6 pathways, smallest: Intraflagellar transport; Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCM8](https://www.uniprot.org/uniprotkb/Q8NCM8) (Cytoplasmic dynein 2 heavy chain 1):

> May function as a motor for intraflagellar retrograde transport. Functions in cilia biogenesis. May play a role in transport between endoplasmic reticulum and Golgi or organization of the Golgi in cells (By similarity).

**Summary**, from NCBI Gene [79659](https://www.ncbi.nlm.nih.gov/gene/79659):

> This gene encodes a large cytoplasmic dynein protein that is involved in retrograde transport in the cilium and has a role in intraflagellar transport, a process required for ciliary/flagellar assembly. Mutations in this gene cause a heterogeneous spectrum of conditions related to altered primary cilium function and often involve polydactyly, abnormal skeletogenesis, and polycystic kidneys. Alternative splicing results in multiple transcript variants encoding distinct proteins. [provided by …

**Accessions** — [HGNC:2962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2962) · Entrez [79659](https://www.ncbi.nlm.nih.gov/gene/79659) · UniProt [Q8NCM8](https://www.uniprot.org/uniprotkb/Q8NCM8) · Ensembl [ENSG00000187240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187240)

## Data

Gene col 11904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11904); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11904]; `tensor/DDL_lfc|DDL_z.npy` [11904]; `embed/gene_vectors.npy` [11904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11904 or target_col == 11904). Every well: [[DYNC2H1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC2H1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
