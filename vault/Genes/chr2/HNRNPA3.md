---
symbol: "HNRNPA3"
type: "gene"
col: 9907
ensembl_id: "ENSG00000170144"
name: "heterogeneous nuclear ribonucleoprotein A3"
location: "2q31.2"
module: 20
arm: "+"
pooled_cpm: 168.64
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# HNRNPA3

*heterogeneous nuclear ribonucleoprotein A3* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.40× (z +23.3, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.02× (z +13.3, q 3e-38, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.770× (z -7.1, q 8e-10, down in 33 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHFR]] (+0.75, fdr 7e-06), [[DHX15]] (+0.72, fdr 7e-06), [[FKBP9]] (+0.71, fdr 7e-06); moves opposite to [[MED19]] (-0.76, fdr 7e-06), [[NKAP]] (-0.73, fdr 7e-06), [[TRAPPC2B]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RHOD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9907.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.40×** | +23.3 | 0e+00 | 48/49 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +21.9 | 0e+00 | 43/44 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +19.9 | 0e+00 | 45/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +13.3 | 3e-38 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.51×** | +12.5 | 1e-33 | 47/49 (RPMI-7951, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +11.2 | 2e-27 | 43/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +9.6 | 8e-20 | 43/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +8.5 | 2e-15 | 38/48 (HT-29, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +8.2 | 2e-14 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +7.6 | 1e-12 | 41/48 (RPMI-7951, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.42×** | +6.4 | 9e-09 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +6.3 | 2e-08 | 27/38 (A-172, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 1e-04 | 39/48 (HCT15, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.005 | 24/48 (A498, A549, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.006 | 26/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.039 | 5/48 (J82, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.082 | 19/48 (HT-29, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9907.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -7.1 | 8e-10 | 33/49 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.712×** | -6.5 | 2e-08 | 36/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.712×** | -6.5 | 2e-08 | 36/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.713×** | -6.2 | 8e-08 | 40/48 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -5.8 | 7e-07 | 41/48 (LOX-IMVI, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.763×** | -5.2 | 2e-05 | 35/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.9 | 0.006 | 20/48 (SW480, C-33 A, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.825×** | -3.7 | 0.016 | 24/48 (C-33 A, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | 0.732× | -3.1 | 0.11 | 20/49 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9907. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 217 | 11 (7 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +20.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 177 | 10 (8 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +21.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.48× (z +21.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.7) |
| [[KATO III (line)]] | alt | 138 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.97× (z +17.8) | — |
| [[NCI-H1573 (line)]] | alt | 206 | 9 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.75× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.60× (z +16.1) | — |
| [[A-172 (line)]] | wt | 135 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.63× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 146 | 8 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +17.4) | — |
| [[NCI-H1792 (line)]] | alt | 82.9 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 206 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +15.1) | — |
| [[SW 900 (line)]] | alt | 142 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 174 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -8.7) |
| [[HT-29 (line)]] | alt | 147 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.44× (z +11.3) | — |
| [[J82 (line)]] | alt | 164 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +17.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.543× (z -8.7) |
| [[LoVo (line)]] | wt | 132 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +23.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.96× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 168 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.02× (z +20.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[C32 (line)]] | wt | 125 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.51× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 201 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.78× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 157 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 109 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.76× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 130 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 187 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.72× (z +11.1) | — |
| [[SK-MEL-2 (line)]] | alt | 134 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.87× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.19× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 104 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.2) | — |
| [[A-427 (line)]] | wt | 194 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 177 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.36× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 227 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.5) |
| [[H4 (line)]] | wt | 153 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 220 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +16.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 201 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.74× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 146 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.31× (z +8.7) | — |
| [[A549 (line)]] | wt | 173 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.75× (z +17.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 170 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +11.8) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 131 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +12.1) | — |
| [[HepG2_C3A (line)]] | wt | 169 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 131 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +15.2) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 170 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +19.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 142 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 169 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +13.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +9.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 171 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 273 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +14.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 150 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.56× (z +10.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 145 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +18.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 237 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.27× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 206 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.56× (z +10.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9907), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHFR]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[DHX15]] | +0.72 | +0.70 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[FKBP9]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[MAT2A]] | +0.70 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SRSF1]] | +0.70 | +0.46 / +0.81 | both halves | 2e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 918 |
| [[IPO5]] | +0.70 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[HNRNPM]] | +0.69 | +0.48 / +0.78 | both halves | 2e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 935 |
| [[RPSA]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[CPSF6]] | +0.69 | +0.55 / +0.71 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 428 |
| [[RBBP7]] | +0.68 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.67 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TARDBP]] | +0.66 | +0.48 / +0.72 | both halves | 2e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 919 |

## Genes that move opposite

*53 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED19]] | -0.76 | -0.67 / -0.75 | both halves | 7e-06 |  |
| [[NKAP]] | -0.73 | -0.69 / -0.73 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[TRAPPC2B]] | -0.71 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.70 | -0.64 / -0.69 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPP21]] | -0.69 | -0.44 / -0.78 | both halves | 3e-05 |  |
| [[ZNF593]] | -0.68 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.68 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[DYNLL1]] | -0.67 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[RNF181]] | -0.67 | -0.44 / -0.71 | both halves | 3e-05 |  |
| [[ING2]] | -0.67 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.66 | -0.59 / -0.76 | both halves | 7e-06 |  |
| [[YIF1A]] | -0.65 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[KRTCAP2]] | -0.65 | -0.51 / -0.71 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOD]] | B | RHOD activity raises HNRNPA3's level | lines that do not express RHOD (15) vs lines expressing it (35) | 1.19× lower at baseline in the lines without RHOD | 0.068 | ⚠ within organs, on part of the lines; also absent: EPHA2, LINC00857, TFCP2L1 |
| [[HDAC6]] | B | HDAC6 activity raises HNRNPA3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CBR3]] | B | CBR3 activity lowers HNRNPA3's level | lines that do not express CBR3 (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without CBR3 | 0.089 | ⚠ within organs, on part of the lines; also absent: MYO10, CDKL5, KLF2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.4, -27.8); signed map (-20.9, -43.5). **Vector** length 113, 41.1% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.51 to 11); *GTP hydrolysis and joining of the 60S ribosomal subunit* (reactome, mean cos +0.51 to 11); *Eukaryotic Translation Elongation* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.4 | +19.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | +23.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.9 | +21.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +12.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +7.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.6 | +0.1 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +2.5 | +2.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | +0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.5 | -1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.8 | +0.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.7 | -0.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:177,212,694-177,223,959 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HNRPA3 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes; Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P51991](https://www.uniprot.org/uniprotkb/P51991) (Heterogeneous nuclear ribonucleoprotein A3):

> Plays a role in cytoplasmic trafficking of RNA. Binds to the cis-acting response element, A2RE. May be involved in pre-mRNA splicing.

**Summary**, from NCBI Gene [220988](https://www.ncbi.nlm.nih.gov/gene/220988):

> Enables RNA binding activity. Predicted to be involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24941) · Entrez [220988](https://www.ncbi.nlm.nih.gov/gene/220988) · UniProt [P51991](https://www.uniprot.org/uniprotkb/P51991) · Ensembl [ENSG00000170144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170144)

## Data

Gene col 9907: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9907); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9907, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9907]; `tensor/DDL_lfc|DDL_z.npy` [9907]; `embed/gene_vectors.npy` [9907]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9907 or target_col == 9907). Every well: [[HNRNPA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
