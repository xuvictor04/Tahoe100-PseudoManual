---
symbol: "EIF4G2"
type: "gene"
col: 3128
ensembl_id: "ENSG00000110321"
name: "eukaryotic translation initiation factor 4 gamma 2"
location: "11p15.4"
module: 3
arm: "-"
pooled_cpm: 383.45
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# EIF4G2

*eukaryotic translation initiation factor 4 gamma 2* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.20× (z +25.2, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +12.1, q 1e-31, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.537× (z -10.9, q 4e-25, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUG1]] (+0.82, fdr 7e-06), [[HNRNPK]] (+0.75, fdr 7e-06), [[MOB1A]] (+0.75, fdr 7e-06); moves opposite to [[ATP5MJ]] (-0.79, fdr 7e-06), [[ANAPC11]] (-0.75, fdr 1e-05), [[LAMTOR5]] (-0.73, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.20×** | +25.2 | 0e+00 | 49/49 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.95×** | +23.2 | 0e+00 | 44/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.07×** | +18.1 | 0e+00 | 46/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +17.1 | 0e+00 | 44/45 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +12.1 | 1e-31 | 45/49 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +10.4 | 3e-23 | 45/48 (A498, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.72×** | +9.2 | 3e-18 | 43/48 (COLO 205, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.65×** | +8.8 | 1e-16 | 43/48 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.8 | 1e-16 | 48/50 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.7 | 9e-13 | 39/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +7.2 | 4e-11 | 44/47 (COLO 205, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +7.1 | 8e-11 | 43/49 (PANC-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +6.6 | 1e-09 | 36/48 (HEC-1-A, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.5 | 4e-09 | 40/48 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.1 | 4e-08 | 38/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.3 | 4e-06 | 35/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 4e-04 | 38/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.001 | 35/48 (BT-474, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.013 | 27/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.028 | 24/48 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.029 | 27/48 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.20× | +3.0 | 0.046 | 22/47 (HT-29, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.537×** | -10.9 | 4e-25 | 45/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.545×** | -10.7 | 3e-24 | 45/48 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.556×** | -10.3 | 9e-23 | 46/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.596×** | -9.1 | 1e-17 | 46/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.664×** | -7.2 | 6e-11 | 45/48 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.514×** | -6.1 | 8e-08 | 45/49 (KATO III, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -5.5 | 4e-06 | 30/48 (A-427, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.781×** | -4.4 | 8e-04 | 35/49 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.707×** | -4.4 | 8e-04 | 41/48 (HepG2/C3A, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **0.743×** | -3.7 | 0.010 | 43/50 (SNU-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.041 | 26/48 (HCT15, HS-578T, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.835× | -3.0 | 0.12 | 23/49 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.835× | -3.0 | 0.12 | 20/49 (LOX-IMVI, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 483 | 11 (9 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +23.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.439× (z -11.1) |
| [[C32 (line)]] | wt | 281 | 10 (5 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +22.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +15.4) | [[Panobinostat (drug)]] 5 µM 0.347× (z -14.1) |
| [[LoVo (line)]] | wt | 372 | 11 (10 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +24.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.53× (z +14.2) | [[Belinostat (drug)]] 5 µM 0.534× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 325 | 9 (6 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.55× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.349× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 240 | 9 (9 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +22.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.505× (z -9.6) |
| [[A-172 (line)]] | wt | 380 | 8 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.492× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 302 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +20.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +13.8) | — |
| [[HOP62 (line)]] | alt | 344 | 7 (5 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +22.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 309 | 10 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +15.2) | [[Belinostat (drug)]] 5 µM 0.455× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 334 | 9 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +27.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +15.1) | [[Panobinostat (drug)]] 0.5 µM 0.510× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 246 | 6 (4 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +17.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -13.3) |
| [[SNU-423 (line)]] | alt | 379 | 10 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.65× (z +20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 342 | 6 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +24.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +11.8) | [[Belinostat (drug)]] 5 µM 0.387× (z -11.7) |
| [[H4 (line)]] | wt | 474 | 5 (5 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +16.8) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.416× (z -9.8) |
| [[HS-578T (line)]] | alt | 323 | 9 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.38× (z +21.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 354 | 6 (5 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +17.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.387× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 463 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +20.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.81× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.452× (z -12.0) |
| [[SW 900 (line)]] | alt | 157 | 6 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +21.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.482× (z -9.2) |
| [[A-427 (line)]] | wt | 360 | 4 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +21.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.342× (z -14.7) |
| [[A498 (line)]] | wt | 325 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +23.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.04× (z +15.8) | — |
| [[KATO III (line)]] | alt | 267 | 6 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +22.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.496× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 454 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 470 | 5 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +16.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.489× (z -9.5) |
| [[PANC-1 (line)]] | alt | 702 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +21.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.38× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 307 | 7 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.24× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.9) | [[Belinostat (drug)]] 5 µM 0.510× (z -9.0) |
| [[A549 (line)]] | wt | 502 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +22.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.01× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.437× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 274 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.14× (z +23.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.8) | — |
| [[NCI-H2347 (line)]] | alt | 571 | 6 (4 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +16.4) | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -11.5) |
| [[SW48 (line)]] | wt | 424 | 5 (5 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +16.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.426× (z -10.5) |
| [[C-33 A (line)]] | alt | 399 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +16.7) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.409× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 357 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +10.2) | [[Belinostat (drug)]] 0.5 µM 0.526× (z -8.6) |
| [[Hs 766T (line)]] | wt | 354 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.87× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 448 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +22.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +13.4) | — |
| [[NCI-H2030 (line)]] | alt | 283 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 320 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +19.2) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.325× (z -13.3) |
| [[RKO (line)]] | wt | 312 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 475 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +18.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +10.8) | — |
| [[J82 (line)]] | alt | 525 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.23× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 318 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 162 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +18.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.486× (z -8.5) |
| [[BT-474 (line)]] | alt | 371 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.3) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -11.9) |
| [[AN3 CA (line)]] | alt | 460 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +13.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 222 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +16.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 598 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +18.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.506× (z -8.5) |
| [[SNU-1 (line)]] | wt | 355 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +17.3) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 391 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 322 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.20× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2122 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 330 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | +0.82 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[HNRNPK]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 | STRING 632 |
| [[MOB1A]] | +0.75 | +0.61 / +0.79 | both halves | 7e-06 |  |
| [[PRKAR1A]] | +0.73 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[NXT2]] | +0.73 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[SCRN1]] | +0.73 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[CRPPA]] | +0.72 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[DDX6]] | +0.72 | +0.50 / +0.64 | both halves | 1e-05 | STRING 466 |
| [[TWF1]] | +0.72 | +0.66 / +0.79 | both halves | 7e-06 |  |
| [[NCOA4]] | +0.72 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[DDX3X]] | +0.71 | +0.63 / +0.64 | both halves | 7e-06 | STRING 773 |
| [[ZMPSTE24]] | +0.69 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | -0.79 | -0.66 / -0.72 | both halves | 7e-06 |  |
| [[ANAPC11]] | -0.75 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.73 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[RPS21]] | -0.73 | -0.70 / -0.66 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[RBIS]] | -0.73 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[RPL36]] | -0.72 | -0.65 / -0.72 | both halves | 7e-06 |  |
| [[ELOB]] | -0.72 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[TMEM120B]] | -0.72 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[RPS26]] | -0.71 | -0.40 / -0.70 | both halves | 5e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[ARID3A]] | -0.71 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[CAMLG]] | -0.71 | -0.58 / -0.68 | both halves | 8e-06 |  |
| [[SDHAP2]] | -0.71 | -0.67 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EIF4G2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises EIF4G2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises EIF4G2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.1, -22.4); signed map (17.3, -33.3). **Vector** length 149, 64.2% of its response variance represented; |z| ≥ 3 in 1,621 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Polyadenylation* (reactome, mean cos +0.50 to 11); *Dengue Virus-Host Interactions* (reactome, mean cos +0.54 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +11.3 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +10.4 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.9 | +6.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.5 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +4.4 | +2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.2 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -10.6 | -10.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -9.9 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -9.0 | -9.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.8 | -10.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.3 | -10.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -6.8 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.8 | -6.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.5 | -2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.5 | -1.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -4.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4 gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:10,797,050-10,808,940 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAP5, NAT1, p97 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; MIF4G domain containing proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 7 pathways, smallest: ISG15 antiviral mechanism; Dengue Virus Genome Translation and Replication; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P78344](https://www.uniprot.org/uniprotkb/P78344) (Eukaryotic translation initiation factor 4 gamma 2):

> Appears to play a role in the switch from cap-dependent to IRES-mediated translation during mitosis, apoptosis and viral infection. Cleaved by some caspases and viral proteases.

**Summary**, from NCBI Gene [1982](https://www.ncbi.nlm.nih.gov/gene/1982):

> Translation initiation is mediated by specific recognition of the cap structure by eukaryotic translation initiation factor 4F (eIF4F), which is a cap binding protein complex that consists of three subunits: eIF4A, eIF4E and eIF4G. The protein encoded by this gene shares similarity with the C-terminal region of eIF4G that contains the binding sites for eIF4A and eIF3; eIF4G, in addition, contains a binding site for eIF4E at the N-terminus. Unlike eIF4G, which supports cap-dependent and …

**Accessions** — [HGNC:3297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3297) · Entrez [1982](https://www.ncbi.nlm.nih.gov/gene/1982) · UniProt [P78344](https://www.uniprot.org/uniprotkb/P78344) · Ensembl [ENSG00000110321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110321)

## Data

Gene col 3128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3128); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3128]; `tensor/DDL_lfc|DDL_z.npy` [3128]; `embed/gene_vectors.npy` [3128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3128 or target_col == 3128). Every well: [[EIF4G2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4G2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
