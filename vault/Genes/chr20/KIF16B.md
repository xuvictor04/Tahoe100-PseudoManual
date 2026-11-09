---
symbol: "KIF16B"
type: "gene"
col: 1575
ensembl_id: "ENSG00000089177"
name: "kinesin family member 16B"
location: "20p12.1"
module: 41
arm: "+"
pooled_cpm: 167.24
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 37
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# KIF16B

*kinesin family member 16B* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.32× (z +5.3, q 6e-05, up in 31 of 46 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.25× (z +4.5, q 0.002, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (21 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.367× (z -28.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM167B]] (+0.58, fdr 1e-05), [[UFSP2]] (+0.56, fdr 3e-05), [[EMC2]] (+0.55, fdr 5e-05); moves opposite to [[MOSMO]] (-0.55, fdr 3e-05), [[E2F3]] (-0.49, fdr 1e-04), [[ARHGAP31]] (-0.49, fdr 6e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1575.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.32×** | +5.3 | 6e-05 | 31/46 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +4.5 | 0.002 | 27/46 (NCI-H460, LoVo, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.005 | 24/46 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.23×** | +4.1 | 0.006 | 31/49 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.027 | 22/49 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.040 | 21/46 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.076 | 19/48 (LoVo, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.076 | 19/47 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.2 | 0.086 | 16/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.097 | 11/47 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.11 | 13/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 24 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1575.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.367×** | -28.5 | 0e+00 | 47/48 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.417×** | -16.9 | 0e+00 | 45/46 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.434×** | -16.1 | 0e+00 | 38/43 (NCI-H23, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.484×** | -14.0 | 2e-42 | 45/47 (HOP62, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.502×** | -13.9 | 1e-41 | 38/48 (COLO 205, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.495×** | -13.1 | 4e-37 | 36/44 (RKO, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.571×** | -10.8 | 2e-25 | 42/49 (A-172, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.602×** | -10.2 | 1e-22 | 36/47 (A-172, LoVo, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.710×** | -9.8 | 1e-20 | 39/47 (A-172, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.629×** | -9.3 | 6e-19 | 42/47 (SNU-423, COLO 205, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.722×** | -9.3 | 8e-19 | 28/47 (HS-578T, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.637×** | -9.1 | 5e-18 | 38/47 (LoVo, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.639×** | -9.0 | 8e-18 | 43/47 (KATO III, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.641×** | -9.0 | 1e-17 | 31/47 (LOX-IMVI, LS 180, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.435×** | -8.8 | 7e-17 | 42/48 (A-172, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -7.1 | 5e-11 | 33/47 (RPMI-7951, SW48, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.793×** | -6.6 | 1e-09 | 25/47 (A549, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -5.9 | 7e-08 | 32/47 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.753×** | -5.7 | 2e-07 | 29/47 (SNU-423, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.754×** | -5.7 | 3e-07 | 35/47 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.631×** | -4.9 | 2e-05 | 30/47 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.809×** | -4.3 | 4e-04 | 24/47 (SW 900, HT-29, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **0.682×** | -4.0 | 0.001 | 25/45 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.868× | -4.0 | 0.001 | 12/47 (A549, NCI-H1792, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.876× | -3.8 | 0.003 | 17/48 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.003 | 22/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.747×** | -3.8 | 0.003 | 26/47 (LS 180, HCT15, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1575. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 229 | 15 (2 ⚠) | 10 (9 ⚠) | [[Trametinib (drug)]] 5 µM 3.13× (z +14.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 2.75× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -18.5) |
| [[A-172 (line)]] | wt | 147 | 0 | 18 (14 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.160× (z -19.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -18.5) |
| [[LOX-IMVI (line)]] | wt | 144 | 0 | 18 (16 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -22.0) |
| [[A549 (line)]] | wt | 289 | 0 | 16 (13 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -25.2) |
| [[CFPAC-1 (line)]] | alt | 193 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -22.5) |
| [[Hs 766T (line)]] | wt | 352 | 0 | 12 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -27.5) |
| [[LS 180 (line)]] | wt | 262 | 0 | 12 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -21.7) |
| [[SNU-423 (line)]] | alt | 115 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -16.2) |
| [[A498 (line)]] | wt | 189 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -22.0) |
| [[HS-578T (line)]] | alt | 151 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -22.8) |
| [[COLO 205 (line)]] | alt | 434 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -22.5) |
| [[KATO III (line)]] | alt | 345 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -23.5) |
| [[LoVo (line)]] | wt | 325 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -21.4) |
| [[RPMI-7951 (line)]] | alt | 185 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.0) |
| [[SW 900 (line)]] | alt | 187 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -19.8) |
| [[HT-29 (line)]] | alt | 177 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -20.2) |
| [[SW48 (line)]] | wt | 170 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -14.1) |
| [[J82 (line)]] | alt | 58.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -15.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.2) |
| [[PANC-1 (line)]] | alt | 188 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -19.6) |
| [[SW480 (line)]] | alt | 201 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 120 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 126 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -25.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.6) |
| [[AsPC-1 (line)]] | alt | 233 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -18.4) |
| [[HOP62 (line)]] | alt | 91.1 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -18.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -17.4) |
| [[A-427 (line)]] | wt | 94.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HCT15 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 93.2 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -12.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -16.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 72.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -8.8) |
| [[RKO (line)]] | wt | 161 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0823× (z -26.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -12.5) |
| [[SNU-1 (line)]] | wt | 153 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -13.4) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.1000× (z -13.0) |
| [[SW1417 (line)]] | alt | 114 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -18.6) |
| [[C-33 A (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[C32 (line)]] | wt | 80.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 99.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 76.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 71.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -10.1) |
| [[SHP-77 (line)]] | alt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.5) |
| [[SW 1088 (line)]] | alt | 218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -10.7) |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1575), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM167B]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[UFSP2]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[EMC2]] | +0.55 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[GOLGA4]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[EPB41]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[GOLGA2]] | +0.53 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[TUBB2B]] | +0.53 | +0.36 / +0.35 | both halves | 1e-04 | pathway: COPI-dependent Golgi-to-ER retrograde traffic |
| [[TMF1]] | +0.53 | +0.56 / +0.46 | both halves | 3e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[TTC3]] | +0.52 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[NBEAL1]] | +0.52 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[STAM2]] | +0.52 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[FAM114A1]] | +0.49 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSMO]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[E2F3]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[ARHGAP31]] | -0.49 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[PHC2-AS1]] | -0.48 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[MSANTD2]] | -0.48 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[CCND1]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TOR1A]] | -0.47 | -0.48 / -0.24 | both halves | 5e-04 |  |
| [[HMGA2]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SPRED1]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SPRY4-AS1]] | -0.47 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[KIAA1549L]] | -0.47 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[CLP1]] | -0.47 | -0.43 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KIF16B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF718]] | B | ZNF718 activity raises KIF16B's level | lines that do not express ZNF718 (13) vs lines expressing it (37) | 1.45× lower at baseline in the lines without ZNF718 | 0.083 | ⚠ within organs, on part of the lines; also absent: ZNF876P, GALNT12, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.395). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.3, -39.8); signed map (-51.6, 17.4). **Vector** length 95.4, 33.1% of its response variance represented; |z| ≥ 3 in 1,706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.7 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.6 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.3 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.2 | +1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.1 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.3 | -16.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -9.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -8.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -5.2 | -14.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -4.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.5 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 16B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:16,272,104-16,573,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20135, dJ971B4.1, SNX23; previously C20orf23 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96L93](https://www.uniprot.org/uniprotkb/Q96L93) (Kinesin-like protein KIF16B):

> Plus end-directed microtubule-dependent motor protein involved in endosome transport and receptor recycling and degradation. Regulates the plus end motility of early endosomes and the balance between recycling and degradation of receptors such as EGF receptor (EGFR) and FGF receptor (FGFR). Regulates the Golgi to endosome transport of FGFR-containing vesicles during early development, a key process for developing basement membrane and epiblast and primitive endoderm lineages during early …

**Summary**, from NCBI Gene [55614](https://www.ncbi.nlm.nih.gov/gene/55614):

> The protein encoded by this gene is a kinesin-like protein that may be involved in intracellular trafficking. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:15869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15869) · Entrez [55614](https://www.ncbi.nlm.nih.gov/gene/55614) · UniProt [Q96L93](https://www.uniprot.org/uniprotkb/Q96L93) · Ensembl [ENSG00000089177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089177)

## Data

Gene col 1575: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1575); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1575, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1575]; `tensor/DDL_lfc|DDL_z.npy` [1575]; `embed/gene_vectors.npy` [1575]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1575 or target_col == 1575). Every well: [[KIF16B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF16B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
