---
symbol: "CLTCL1"
type: "gene"
col: 947
ensembl_id: "ENSG00000070371"
name: "clathrin heavy chain like 1"
location: "22q11.21"
module: 10
arm: "-"
pooled_cpm: 34.42
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 29
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 5
direction_downstream: 26
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CLTCL1

*clathrin heavy chain like 1* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.73× (z +19.3, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.352× (z -19.2, q 0e+00, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBX4]] (+0.69, fdr 1e-05), [[ASL]] (+0.69, fdr 1e-05), [[SNTA1]] (+0.67, fdr 1e-05); moves opposite to [[ANXA2R-AS1]] (-0.67, fdr 7e-05), [[IQCH-AS1]] (-0.66, fdr 3e-05), [[UFL1-AS1]] (-0.63, fdr 4e-04).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); 26 go from it, the strongest it → [[FBXL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +19.3 | 0e+00 | 44/45 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.52×** | +17.7 | 0e+00 | 44/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +17.3 | 0e+00 | 43/45 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +7.3 | 6e-11 | 29/45 (SW480, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +6.6 | 6e-09 | 23/45 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +5.3 | 1e-05 | 20/45 (RKO, SW480, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.63×** | +4.9 | 7e-05 | 19/44 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.29×** | +4.7 | 1e-04 | 12/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.8 | 0.010 | 13/45 (HOP62, SK-MEL-2, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.21×** | +3.7 | 0.010 | 12/45 (SW480, RKO, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.037 | 10/45 (SK-MEL-2, RKO, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.076 | 12/45 (SK-MEL-2, H4, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 947.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.352×** | -19.2 | 0e+00 | 40/45 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.398×** | -17.6 | 0e+00 | 37/45 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -16.7 | 0e+00 | 37/43 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.427×** | -16.2 | 0e+00 | 37/42 (A-172, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.209×** | -15.6 | 0e+00 | 44/45 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.274×** | -12.9 | 3e-36 | 39/44 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.500×** | -12.7 | 4e-35 | 33/42 (Hs 766T, J82, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.506×** | -12.0 | 2e-31 | 31/38 (MIA PaCa-2, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -11.8 | 3e-30 | 33/45 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.544×** | -11.6 | 2e-29 | 38/45 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.550×** | -11.4 | 2e-28 | 33/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.671×** | -10.7 | 4e-25 | 31/45 (A-172, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -10.6 | 1e-24 | 27/44 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.570×** | -10.3 | 2e-23 | 29/37 (LoVo, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.587×** | -10.1 | 1e-22 | 32/44 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -7.2 | 1e-11 | 29/45 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -7.2 | 2e-11 | 25/43 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.772×** | -7.0 | 1e-10 | 22/45 (SNU-423, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -6.8 | 3e-10 | 24/45 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -4.9 | 2e-05 | 22/45 (CFPAC-1, RPMI-7951, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.803×** | -4.2 | 7e-04 | 19/45 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.799×** | -4.0 | 0.001 | 15/44 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 75.1 | 0 | 15 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -16.8) |
| [[MIA PaCa-2 (line)]] | alt | 83.0 | 1 | 14 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0539× (z -17.4) |
| [[A-172 (line)]] | wt | 51.3 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -28.3) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0791× (z -23.9) |
| [[PANC-1 (line)]] | alt | 28.0 | 3 | 11 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.335× (z -11.5) |
| [[HOP62 (line)]] | alt | 60.1 | 0 | 13 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 22.7 | 3 | 10 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +12.2) | [[Harringtonine (drug)]] 0.5 µM 0.188× (z -16.2) |
| [[SNU-423 (line)]] | alt | 85.4 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -21.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.110× (z -19.5) |
| [[Hs 766T (line)]] | wt | 60.8 | 1 | 10 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.72× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.201× (z -13.8) |
| [[J82 (line)]] | alt | 34.9 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -15.3) |
| [[NCI-H1792 (line)]] | alt | 44.0 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0737× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.215× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 63.4 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 64.2 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.0) |
| [[LoVo (line)]] | wt | 27.9 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.364× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 1 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0980× (z -11.2) |
| [[SW480 (line)]] | alt | 18.7 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.60× (z +15.2) | [[Harringtonine (drug)]] 0.5 µM 0.339× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 42.9 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.52× (z +9.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -9.2) |
| [[A549 (line)]] | wt | 29.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.212× (z -12.8) |
| [[HCT15 (line)]] | alt | 44.3 | 0 | 5 (3 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0872× (z -11.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.180× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 30.8 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 46.1 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.37× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.119× (z -9.6) |
| [[SW1417 (line)]] | alt | 41.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.63× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.363× (z -9.0) |
| [[LS 180 (line)]] | wt | 24.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 34.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0994× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.153× (z -12.0) |
| [[SHP-77 (line)]] | alt | 56.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.5 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -11.1) |
| [[A498 (line)]] | wt | 28.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.195× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 23.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -10.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.194× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 14.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.15× (z +10.1) | — |
| [[RKO (line)]] | wt | 42.7 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.10× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.332× (z -8.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.205× (z -11.0) |
| [[SW 900 (line)]] | alt | 14.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.70× (z +8.5) | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.140× (z -9.6) |
| [[AN3 CA (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX4]] | +0.69 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ASL]] | +0.69 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SNTA1]] | +0.67 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PSMD9]] | +0.66 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[YIF1B]] | +0.65 | +0.36 / +0.43 | both halves | 1e-04 |  |
| [[METTL26]] | +0.64 | +0.36 / +0.38 | both halves | 1e-04 |  |
| [[MYO9B]] | +0.64 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[RRAS]] | +0.63 | +0.54 / +0.31 | both halves | 2e-04 |  |
| [[ANKRD27]] | +0.62 | +0.45 / +0.36 | both halves | 1e-04 |  |
| [[WRAP73]] | +0.62 | +0.29 / +0.39 | both halves | 2e-04 |  |
| [[LRRFIP1]] | +0.62 | +0.58 / +0.36 | both halves | 1e-04 |  |
| [[GNAI2]] | +0.62 | +0.47 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA2R-AS1]] | -0.67 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[IQCH-AS1]] | -0.66 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[UFL1-AS1]] | -0.63 | -0.49 / -0.24 | both halves | 4e-04 |  |
| [[LEKR1]] | -0.63 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[TAFA2]] | -0.63 | -0.46 / -0.29 | both halves | 2e-04 |  |
| [[DECR1]] | -0.62 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[AHI1-DT]] | -0.61 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[JADE2]] | -0.61 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CTBP1-DT]] | -0.61 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.61 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[ZFP91]] | -0.61 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[LINC00869-1]] | -0.60 | -0.31 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises CLTCL1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without STARD9 | 0.020 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[OSBPL6]] | B | OSBPL6 activity raises CLTCL1's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 1.91× lower at baseline in the lines without OSBPL6 | 0.037 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers CLTCL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SPIRE1]] | C | SPIRE1 activity raises CLTCL1's level | lines that do not express SPIRE1 (3) vs lines expressing it (47) | 3.90× lower at baseline in the lines without SPIRE1 | 0.034 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: NME4, CIBAR1, BMS1P23; co-absent with the target |
| [[SNTA1]] | C | SNTA1 activity raises CLTCL1's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.91× lower at baseline in the lines without SNTA1 | 0.098 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXL2]] | C | CLTCL1 activity raises FBXL2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 7.60× lower at baseline in the lines without CLTCL1 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[FERMT2]] | C | CLTCL1 activity raises FERMT2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 9.57× lower at baseline in the lines without CLTCL1 | 0.006 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[AP1M1]] | C | CLTCL1 activity raises AP1M1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 3.39× lower at baseline in the lines without CLTCL1 | 0.012 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[FAM13B]] | C | CLTCL1 activity raises FAM13B's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 1.62× lower at baseline in the lines without CLTCL1 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[WDR44]] | C | CLTCL1 activity weakens WDR44's drug response | lines that do not express CLTCL1 (3) vs lines expressing it (46) | the lines without CLTCL1 respond 1.33× as strongly (z diff -1.00); strongest at Ixazomib citrate 5 µM: 2.90x vs 1.34x (z diff -6.1) | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT; target measured in part of the lines; artifact flags |
| [[STARD9]] | C | CLTCL1 activity raises STARD9's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 5.56× lower at baseline in the lines without CLTCL1 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[VKORC1]] | C | CLTCL1 activity raises VKORC1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without CLTCL1 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[SIX4]] | C | CLTCL1 activity raises SIX4's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 4.13× lower at baseline in the lines without CLTCL1 | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[SNTA1]] | C | CLTCL1 activity raises SNTA1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 3.74× lower at baseline in the lines without CLTCL1 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT; co-absent with the target |
| [[MPP3]] | C | CLTCL1 activity raises MPP3's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 2.71× lower at baseline in the lines without CLTCL1 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[PATL2]] | C | CLTCL1 activity lowers PATL2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 2.80× higher at baseline in the lines without CLTCL1 | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[NMT2]] | C | CLTCL1 activity raises NMT2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without CLTCL1 | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.608). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.5, 3.0); signed map (-26.7, 16.9). **Vector** length 94.6, 25.5% of its response variance represented; |z| ≥ 3 in 1,410 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.1 | +17.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.0 | +19.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.9 | +17.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +0.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.4 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -4.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.8 | -10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.2 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -12.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -12.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | clathrin heavy chain like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,179,473-19,291,719 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLTD, CLH22, CHC22; previously CLTCL |
| Gene groups (HGNC) | Clathrin subunits |
| Reactome | 12 pathways, smallest: Formation of annular gap junctions; Gap junction degradation; Gap junction trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P53675](https://www.uniprot.org/uniprotkb/P53675) (Clathrin heavy chain 2):

> Clathrin is the major protein of the polyhedral coat of coated pits and vesicles. Two different adapter protein complexes link the clathrin lattice either to the plasma membrane or to the trans-Golgi network (By similarity).

**Summary**, from NCBI Gene [8218](https://www.ncbi.nlm.nih.gov/gene/8218):

> This gene is a member of the clathrin heavy chain family and encodes a major protein of the polyhedral coat of coated pits and vesicles. Chromosomal aberrations involving this gene are associated with meningioma, DiGeorge syndrome, and velo-cardio-facial syndrome. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2009]

**Accessions** — [HGNC:2093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2093) · Entrez [8218](https://www.ncbi.nlm.nih.gov/gene/8218) · UniProt [P53675](https://www.uniprot.org/uniprotkb/P53675) · Ensembl [ENSG00000070371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070371)

## Data

Gene col 947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 947); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 947]; `tensor/DDL_lfc|DDL_z.npy` [947]; `embed/gene_vectors.npy` [947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 947 or target_col == 947). Every well: [[CLTCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLTCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
