---
symbol: "EML4"
type: "gene"
col: 6823
ensembl_id: "ENSG00000143924"
name: "EMAP like 4"
location: "2p21"
module: 23
arm: "-"
pooled_cpm: 204.55
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# EML4

*EMAP like 4* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.25× (z +26.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.789× (z -11.0, q 3e-25, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TESC]] (+0.66, fdr 1e-05), [[GMDS]] (+0.63, fdr 2e-05), [[PRAG1]] (+0.59, fdr 1e-05); moves opposite to [[CCDC59]] (-0.65, fdr 1e-05), [[RAB21]] (-0.62, fdr 6e-05), [[VPS39]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EEPD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +26.4 | 0e+00 | 46/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +23.3 | 0e+00 | 46/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +21.6 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +15.0 | 0e+00 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.47×** | +12.6 | 3e-34 | 42/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +12.1 | 7e-32 | 43/48 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +11.8 | 2e-30 | 28/48 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +11.8 | 4e-30 | 42/49 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +11.1 | 5e-27 | 33/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +10.1 | 4e-22 | 34/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +10.0 | 7e-22 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +9.3 | 5e-19 | 33/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.30×** | +8.1 | 2e-14 | 32/47 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.27×** | +7.7 | 7e-13 | 34/48 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.26×** | +7.3 | 9e-12 | 26/48 (NCI-H460, AsPC-1, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +7.2 | 2e-11 | 33/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +6.8 | 5e-10 | 26/49 (HT-29, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.012 | 19/48 (SNU-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.052 | 10/48 (NCI-H460, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.054 | 11/48 (NCI-H2347, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.19× | +2.9 | 0.090 | 11/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.789×** | -11.0 | 3e-25 | 28/49 (SNU-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.802×** | -10.2 | 6e-22 | 27/48 (A-427, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.735×** | -9.7 | 6e-20 | 28/47 (SNU-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.763×** | -8.8 | 1e-16 | 27/49 (SNU-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.781×** | -8.8 | 2e-16 | 31/50 (A-172, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -8.7 | 2e-16 | 26/44 (SNU-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.805×** | -8.4 | 3e-15 | 35/48 (A-427, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.796×** | -7.5 | 6e-12 | 30/49 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.801×** | -7.3 | 2e-11 | 27/48 (SW1417, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.838× | -6.8 | 5e-10 | 20/48 (A-427, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.842× | -6.6 | 3e-09 | 21/49 (A-427, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.827×** | -6.0 | 1e-07 | 22/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.838× | -5.8 | 3e-07 | 22/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.851× | -5.1 | 1e-05 | 19/47 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.857× | -5.1 | 2e-05 | 22/48 (HepG2/C3A, SNU-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.860× | -4.9 | 3e-05 | 14/47 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.909× | -4.4 | 3e-04 | 15/48 (A-172, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.868× | -4.3 | 6e-04 | 16/48 (HOP62, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.913× | -4.2 | 8e-04 | 8/48 (HOP62, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.791×** | -4.0 | 0.002 | 11/50 (A-427, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | 0.889× | -3.9 | 0.003 | 8/48 (HOP62, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 140 | 17 (12 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +24.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +24.0) | — |
| [[PANC-1 (line)]] | alt | 194 | 12 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +19.8) | — |
| [[NCI-H2347 (line)]] | alt | 216 | 5 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +11.7) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.491× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 578 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 303 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +22.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.546× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 199 | 9 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 20.1× (z +24.4) | — |
| [[SNU-1 (line)]] | wt | 1,011 | 3 (1 ⚠) | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.99× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.0715× (z -33.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -22.0) |
| [[SW480 (line)]] | alt | 235 | 8 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +14.8) | [[Dinaciclib (drug)]] 0.5 µM 0.636× (z -9.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 392 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -17.8) |
| [[Hs 766T (line)]] | wt | 65.2 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +13.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 227 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.45× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -13.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 109 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 338 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.0) |
| [[HOP62 (line)]] | alt | 108 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +12.6) | — |
| [[NCI-H1573 (line)]] | alt | 95.6 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.6) | — |
| [[RKO (line)]] | wt | 171 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 114 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.60× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 143 | 0 | 5 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.535× (z -11.6) |
| [[A-427 (line)]] | wt | 256 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +14.4) | [[Selinexor (drug)]] 5 µM 0.615× (z -11.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.645× (z -9.2) |
| [[A549 (line)]] | wt | 265 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 206 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -10.1) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 179 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -14.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 210 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -10.1) |
| [[AN3 CA (line)]] | alt | 258 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.17× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -9.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 151 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +14.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.594× (z -9.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 216 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +12.0) | — |
| [[LoVo (line)]] | wt | 134 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.90× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 182 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.57× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 107 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.98× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 162 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.87× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 91.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +14.9) | — |
| [[HT-29 (line)]] | alt | 301 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -13.1) |
| [[J82 (line)]] | alt | 105 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 144 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +15.8) | — |
| [[LS 180 (line)]] | wt | 137 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 174 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.31× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 136 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +14.8) | — |
| [[C32 (line)]] | wt | 74.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.8) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.23× (z +8.8) | — |
| [[H4 (line)]] | wt | 118 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +8.6) | — |
| [[NCI-H23 (line)]] | alt | 674 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -14.3) |
| [[C-33 A (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -11.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 84.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.4) | — |
| [[SW48 (line)]] | wt | 145 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.459× (z -8.5) |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 240 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESC]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[GMDS]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PRAG1]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[HIVEP3]] | +0.59 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SLC20A1]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ARHGAP26]] | +0.58 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[TIAM1]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SPATA13]] | +0.56 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[FAM3C]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[UXS1]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[MAP3K14]] | +0.56 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[MED14]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC59]] | -0.65 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[RAB21]] | -0.62 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[VPS39]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[SUPT7L]] | -0.60 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[MAIP1]] | -0.58 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[TAS2R4]] | -0.58 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[ZFHX2-AS1]] | -0.58 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.57 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[PSMC2]] | -0.57 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[KLRA1P]] | -0.57 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[C3orf38]] | -0.57 | -0.47 / -0.36 | both halves | 9e-05 |  |
| [[ATE1OSP]] | -0.56 | -0.47 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEPD1]] | B | EEPD1 activity raises EML4's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without EEPD1 | 0.038 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-0.4, 17.0); signed map (1.5, 42.3). **Vector** length 125, 40.1% of its response variance represented; |z| ≥ 3 in 1,653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +11.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +8.1 | +12.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.9 | +21.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.3 | +26.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.3 | +23.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +7.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +0.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.9 | +1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.8 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.0 | -9.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -7.5 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | -7.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.5 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -7.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.6 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | EMAP like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:42,169,353-42,332,548 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ROPP120, ELP120; previously C2orf2 |
| Gene groups (HGNC) | WD repeat domain containing; EMAP like |
| Reactome | 9 pathways, smallest: ALK mutants bind TKIs; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC35](https://www.uniprot.org/uniprotkb/Q9HC35) (Echinoderm microtubule-associated protein-like 4):

> Essential for the formation and stability of microtubules (MTs). Required for the organization of the mitotic spindle and for the proper attachment of kinetochores to MTs. Promotes the recruitment of NUDC to the mitotic spindle for mitotic progression.

**Summary**, from NCBI Gene [27436](https://www.ncbi.nlm.nih.gov/gene/27436):

> This gene is a member of the echinoderm microtubule associated protein-like family. The encoded WD-repeat protein may be involved in microtubule formation. Abnormal fusion of parts of this gene with portions of the anaplastic lymphoma receptor tyrosine kinase gene, which generates EML4-ALK fusion transcripts, is one of the primary mutations associated with non-small cell lung cancer. Alternative splicing of this gene results in two transcript variants. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:1316](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1316) · Entrez [27436](https://www.ncbi.nlm.nih.gov/gene/27436) · UniProt [Q9HC35](https://www.uniprot.org/uniprotkb/Q9HC35) · Ensembl [ENSG00000143924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143924)

## Data

Gene col 6823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6823); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6823]; `tensor/DDL_lfc|DDL_z.npy` [6823]; `embed/gene_vectors.npy` [6823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6823 or target_col == 6823). Every well: [[EML4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EML4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
