---
symbol: "CPNE3"
type: "gene"
col: 1436
ensembl_id: "ENSG00000085719"
name: "copine 3"
location: "8q21.3"
module: 29
arm: "+"
pooled_cpm: 94.27
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CPNE3

*copine 3* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.34× (z +15.8, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.39× (z +8.6, q 8e-16, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.534× (z -11.6, q 2e-28, down in 43 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.585× (z -9.9, q 1e-20, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS35]] (+0.72, fdr 7e-06), [[BLTP1]] (+0.63, fdr 1e-05), [[KIAA1191]] (+0.61, fdr 7e-06); moves opposite to [[LINC00106]] (-0.56, fdr 3e-05), [[ASMTL-AS1]] (-0.50, fdr 4e-05), [[PPP6R2]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +15.8 | 0e+00 | 47/49 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +13.7 | 5e-40 | 40/43 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +8.8 | 3e-16 | 40/45 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.6 | 8e-16 | 36/49 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.5 | 1e-08 | 29/48 (AsPC-1, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 2e-08 | 31/48 (LOX-IMVI, A498, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.9 | 3e-07 | 30/48 (LOX-IMVI, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.6 | 2e-06 | 31/50 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.31×** | +5.1 | 3e-05 | 29/48 (LOX-IMVI, SW1417, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.56×** | +4.3 | 0.001 | 33/47 (RKO, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 28/48 (Hs 766T, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +3.7 | 0.009 | 24/48 (HT-29, A-172, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.062 | 21/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -11.6 | 2e-28 | 43/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -9.9 | 1e-20 | 42/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.593×** | -9.7 | 8e-20 | 47/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -9.3 | 3e-18 | 44/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.428×** | -8.2 | 3e-14 | 44/49 (RKO, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.785×** | -6.3 | 3e-08 | 25/48 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -6.0 | 1e-07 | 38/48 (HOP62, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.855× | -4.1 | 0.003 | 19/48 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.796×** | -4.0 | 0.003 | 23/48 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.804×** | -4.0 | 0.003 | 23/48 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.817×** | -3.7 | 0.010 | 25/47 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.835× | -3.2 | 0.063 | 20/47 (SW480, hTERT-HPNE, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.1 | 0.091 | 18/48 (HOP62, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 113 | 1 (1 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +8.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.302× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -13.9) |
| [[SW480 (line)]] | alt | 86.8 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +14.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.439× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 127 | 2 (1 ⚠) | 5 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.45× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -14.9) |
| [[J82 (line)]] | alt | 80.1 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +8.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.262× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -12.7) |
| [[PANC-1 (line)]] | alt | 77.9 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.87× (z +13.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.346× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.430× (z -11.3) |
| [[SNU-423 (line)]] | alt | 111 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.87× (z +13.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -13.6) |
| [[LS 180 (line)]] | wt | 79.9 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.6) | [[TAK-901 (drug)]] 5 µM 0.208× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 83.9 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.98× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.7) |
| [[Hs 766T (line)]] | wt | 97.1 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.34× (z +9.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.327× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.558× (z -9.3) |
| [[HT-29 (line)]] | alt | 50.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 122 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.379× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.448× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 141 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +9.4) | — |
| [[RKO (line)]] | wt | 203 | 2 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +10.5) | [[TAK-901 (drug)]] 5 µM 0.238× (z -9.5) |
| [[A549 (line)]] | wt | 93.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.7) | — |
| [[C32 (line)]] | wt | 101 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.384× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.400× (z -10.0) |
| [[HS-578T (line)]] | alt | 140 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -12.3) |
| [[LoVo (line)]] | wt | 78.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 71.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +11.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.246× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 108 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 77.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.05 µM 0.447× (z -10.0) |
| [[SW 900 (line)]] | alt | 63.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +9.4) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.381× (z -8.9) |
| [[A-427 (line)]] | wt | 86.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +12.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 170 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +12.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 123 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.6) | — |
| [[H4 (line)]] | wt | 85.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.373× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 68.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +13.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 80.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +10.9) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 91.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -11.1) |
| [[SHP-77 (line)]] | alt | 110 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 60.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 68.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 92.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 95.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +11.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 85.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.199× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 146 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 69.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 97.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -15.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 98.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.138× (z -9.2) |
| [[SW 1088 (line)]] | alt | 93.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0872× (z -9.5) |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[BLTP1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[KIAA1191]] | +0.61 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[APPL1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TPGS2]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PCYOX1]] | +0.59 | +0.43 / +0.67 | both halves | 4e-05 |  |
| [[STYX]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[QARS1]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[VAMP3]] | +0.56 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[CRYZ]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[IQGAP1]] | +0.56 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[EIF2AK1]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00106]] | -0.56 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ASMTL-AS1]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PPP6R2]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[OPA3]] | -0.47 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CUEDC1]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[IWS1]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[NDUFS6]] | -0.46 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TMEM229B]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[ALYREF]] | -0.45 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[FBXL18]] | -0.44 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[TEX22]] | -0.44 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[EIF4E]] | -0.44 | -0.24 / -0.52 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPNE3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.335). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.2, -18.0); signed map (-22.6, -31.5). **Vector** length 110, 34.1% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.3 | +6.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.8 | +4.1 |
|  | [[NG25 (drug)]] 5 µM |  | +4.2 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.1 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.6 | +1.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.2 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +1.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | +2.5 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.0 | -4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -8.4 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.5 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -11.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.4 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | copine 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:86,514,435-86,561,498 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Copines |
| Reactome | 5 pathways, smallest: Glycerophospholipid biosynthesis; Phospholipid metabolism; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75131](https://www.uniprot.org/uniprotkb/O75131) (Copine-3):

> Calcium-dependent phospholipid-binding protein that plays a role in ERBB2-mediated tumor cell migration in response to growth factor heregulin stimulation.

**Summary**, from NCBI Gene [8895](https://www.ncbi.nlm.nih.gov/gene/8895):

> Calcium-dependent membrane-binding proteins may regulate molecular events at the interface of the cell membrane and cytoplasm. This gene encodes a protein which contains two type II C2 domains in the amino-terminus and an A domain-like sequence in the carboxy-terminus. The A domain mediates interactions between integrins and extracellular ligands. [provided by RefSeq, Aug 2008]

**Accessions** — [HGNC:2316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2316) · Entrez [8895](https://www.ncbi.nlm.nih.gov/gene/8895) · UniProt [O75131](https://www.uniprot.org/uniprotkb/O75131) · Ensembl [ENSG00000085719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085719)

## Data

Gene col 1436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1436); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1436]; `tensor/DDL_lfc|DDL_z.npy` [1436]; `embed/gene_vectors.npy` [1436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1436 or target_col == 1436). Every well: [[CPNE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
