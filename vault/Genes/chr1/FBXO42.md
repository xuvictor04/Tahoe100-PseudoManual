---
symbol: "FBXO42"
type: "gene"
col: 443
ensembl_id: "ENSG00000037637"
name: "F-box protein 42"
location: "1p36.13"
module: 79
arm: "+"
pooled_cpm: 119.96
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 32
n_dd_up_clean: 10
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# FBXO42

*F-box protein 42* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.57× (z +7.0, q 2e-09, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.216× (z -22.5, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.662× (z -6.3, q 5e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6A]] (+0.75, fdr 7e-06), [[HDAC3]] (+0.75, fdr 7e-06), [[FAM162A]] (+0.73, fdr 7e-06); moves opposite to [[EIF4G1]] (-0.64, fdr 1e-05), [[TASOR]] (-0.62, fdr 1e-05), [[TRIP12]] (-0.62, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EFCAB3P1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +7.0 | 2e-09 | 38/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.7 | 6e-09 | 32/48 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.1 | 2e-07 | 35/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.5 | 0.001 | 26/49 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.004 | 26/48 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.007 | 32/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.012 | 26/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.025 | 21/48 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.54×** | +3.5 | 0.033 | 24/48 (A-172, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +3.2 | 0.068 | 23/48 (SW1417, RKO, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.25×** | +3.2 | 0.068 | 22/48 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.090 | 20/49 (A498, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.090 | 24/48 (NCI-H23, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.216×** | -22.5 | 0e+00 | 43/44 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.249×** | -19.3 | 0e+00 | 48/49 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.409×** | -12.6 | 2e-34 | 42/45 (RKO, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -6.3 | 5e-08 | 32/48 (SK-MEL-2, C32, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.677×** | -5.9 | 3e-07 | 41/48 (NCI-H2030, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.678×** | -5.7 | 1e-06 | 34/48 (NCI-H460, SK-MEL-2, …) | top dose only | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.693×** | -5.6 | 2e-06 | 40/48 (NCI-H2030, RPMI-7951, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.709×** | -5.0 | 3e-05 | 28/47 (C32, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.775×** | -4.9 | 6e-05 | 26/48 (C32, SNU-423, …) | two highest doses | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.733×** | -4.7 | 1e-04 | 35/49 (SW 900, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **0.736×** | -4.7 | 2e-04 | 31/48 (HT-29, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.740×** | -4.6 | 2e-04 | 33/49 (NCI-H2030, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.737×** | -4.5 | 3e-04 | 32/48 (C32, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.746×** | -4.5 | 3e-04 | 35/48 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.768×** | -4.0 | 0.002 | 30/49 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.748×** | -4.0 | 0.002 | 29/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.781×** | -3.8 | 0.005 | 28/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.784×** | -3.7 | 0.007 | 26/49 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.008 | 25/47 (Hs 766T, A498, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.788×** | -3.6 | 0.008 | 26/48 (RKO, HT-29, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.012 | 25/49 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.798×** | -3.4 | 0.015 | 23/48 (NCI-H2030, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 91.1 | 5 (3 ⚠) | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.90× (z +11.1) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.42× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0866× (z -26.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0647× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -9.2) |
| [[C32 (line)]] | wt | 208 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 141 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0583× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -10.3) |
| [[NCI-H1792 (line)]] | alt | 138 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.72× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 114 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 123 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -21.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 137 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -13.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 123 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -14.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 141 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -21.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 125 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.45× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -13.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 145 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -13.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 142 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -17.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 90.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -13.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 80.6 | 3 (2 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.77× (z +9.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 129 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -19.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 215 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -17.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -15.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -14.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 152 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -14.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 137 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 124 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -12.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 73.0 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 91.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -13.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 146 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0541× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 79.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -11.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -11.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -18.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -12.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 95.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0878× (z -20.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -19.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -12.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -15.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -10.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 85.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -15.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 95.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0754× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 99.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -17.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 81.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | +0.75 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.75 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.73 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[PDK1]] | +0.69 | +0.77 / +0.57 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | +0.68 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[PPP2R5B]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[PEX3]] | +0.68 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[NENF]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.68 | +0.71 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G1]] | -0.64 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[TASOR]] | -0.62 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.62 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.61 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SKIL]] | -0.60 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[PURB]] | -0.59 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[SRSF6]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[UTP20]] | -0.59 | -0.63 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFCAB3P1]] | C | EFCAB3P1 activity raises FBXO42's level | lines that do not express EFCAB3P1 (3) vs lines expressing it (47) | 1.60× lower at baseline in the lines without EFCAB3P1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FRZB, ENSG00000273184, CLEC2D; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.2, -16.7); signed map (-36.1, 23.1). **Vector** length 125, 46.2% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.56 to 5); *glycolysis* (hallmark, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +4.6 | +3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.9 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +0.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.3 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -7.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -4.1 | -5.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.5 | -5.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.4 | -3.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.2 | -4.7 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.7 | -4.0 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -2.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,246,840-16,352,480 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1332, Fbx42 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P3S6](https://www.uniprot.org/uniprotkb/Q6P3S6) (F-box only protein 42):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Required for bipolar spindle formation during mitosis. Recognizes p53/TP53 phosphorylated by CSN-associated kinase, promoting its polyubiquitination and proteasomal degradation. Positively regulates the Notch signaling pathway through 'Lys-63'-linked polyubiquitination of the transcriptional effector RBPJ, stabilizing its chromatin association and potentiating transcriptional activation of …

**Summary**, from NCBI Gene [54455](https://www.ncbi.nlm.nih.gov/gene/54455):

> Members of the F-box protein family, such as FBXO42, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (SKP1A; MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Dec 2010]

**Accessions** — [HGNC:29249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29249) · Entrez [54455](https://www.ncbi.nlm.nih.gov/gene/54455) · UniProt [Q6P3S6](https://www.uniprot.org/uniprotkb/Q6P3S6) · Ensembl [ENSG00000037637](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037637)

## Data

Gene col 443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 443); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 443]; `tensor/DDL_lfc|DDL_z.npy` [443]; `embed/gene_vectors.npy` [443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 443 or target_col == 443). Every well: [[FBXO42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
