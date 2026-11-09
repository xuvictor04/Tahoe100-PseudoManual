---
symbol: "XRCC5"
type: "gene"
col: 1245
ensembl_id: "ENSG00000079246"
name: "X-ray repair cross complementing 5"
location: "2q35"
module: 4
arm: "+"
pooled_cpm: 265.45
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# XRCC5

*X-ray repair cross complementing 5* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +23.0, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.35× (z +11.6, q 6e-29, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.805× (z -8.5, q 8e-15, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKDC]] (+0.79, fdr 7e-06), [[NUP155]] (+0.79, fdr 7e-06), [[SUPT16H]] (+0.74, fdr 7e-06); moves opposite to [[VPS37D]] (-0.72, fdr 1e-05), [[SAT2]] (-0.72, fdr 7e-06), [[CNNM4]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KREMEN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.29×** | +23.0 | 0e+00 | 49/49 (A549, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.34×** | +21.4 | 0e+00 | 42/44 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.78×** | +14.8 | 0e+00 | 44/45 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.35×** | +11.6 | 6e-29 | 39/49 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.42×** | +9.7 | 4e-20 | 41/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +9.5 | 1e-19 | 38/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +9.3 | 1e-18 | 42/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.41×** | +8.6 | 5e-16 | 37/47 (LoVo, Hs 766T, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.30×** | +7.2 | 5e-11 | 32/48 (NCI-H1573, NCI-H2030, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +6.2 | 3e-08 | 29/48 (LoVo, SHP-77, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +5.9 | 2e-07 | 25/48 (NCI-H1792, A549, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.22×** | +5.6 | 1e-06 | 25/48 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 3e-05 | 26/38 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.9 | 4e-05 | 21/48 (LoVo, HOP62, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.41×** | +4.6 | 1e-04 | 31/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 32/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.36×** | +4.2 | 8e-04 | 25/48 (C32, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.003 | 20/48 (MIA PaCa-2, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.10× | +3.7 | 0.004 | 1/48 (HCT15) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.008 | 18/47 (LOX-IMVI, SW1417, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.14× | +3.6 | 0.008 | 8/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.5 | 0.008 | 9/48 (SW1417, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +3.4 | 0.013 | 17/48 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.027 | 5/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.030 | 15/48 (NCI-H2030, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -8.5 | 8e-15 | 31/49 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.776×** | -7.1 | 4e-10 | 29/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.779×** | -6.9 | 7e-10 | 29/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -6.9 | 1e-09 | 22/48 (SW1417, SW480, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.798×** | -6.3 | 3e-08 | 29/48 (AsPC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 0.856× | -6.1 | 8e-08 | 17/48 (H4, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -5.6 | 2e-06 | 15/48 (Panc 03.27, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.820×** | -5.5 | 2e-06 | 24/49 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -5.0 | 4e-05 | 22/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.845× | -4.7 | 1e-04 | 21/48 (NCI-H2030, RKO, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.791×** | -4.6 | 2e-04 | 29/48 (CHP-212, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.854× | -4.4 | 5e-04 | 21/48 (SW48, A-172, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.895× | -4.4 | 5e-04 | 7/48 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.899× | -4.2 | 0.001 | 3/48 (A-172, C-33 A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.742×** | -4.1 | 0.002 | 26/49 (A-427, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.872× | -3.8 | 0.004 | 13/48 (A-427, AN3 CA, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.917× | -3.4 | 0.024 | 4/48 (NCI-H23, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.902× | -3.2 | 0.035 | 7/49 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.893× | -3.2 | 0.041 | 9/47 (LOX-IMVI, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Roxadustat (drug)]] 0.05 µM |  | 0.886× | -3.1 | 0.046 | 10/47 (HepG2/C3A, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 211 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.47× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 149 | 9 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 211 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.89× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 342 | 5 (5 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 5 µM 0.545× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 512 | 6 (6 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +13.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Belinostat (drug)]] 5 µM 0.612× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 194 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.03× (z +8.5) | — |
| [[J82 (line)]] | alt | 207 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Belinostat (drug)]] 5 µM 0.550× (z -9.9) |
| [[KATO III (line)]] | alt | 219 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.86× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.579× (z -9.3) |
| [[LS 180 (line)]] | wt | 233 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.81× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 297 | 1 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 0.5 µM 0.515× (z -12.2) |
| [[COLO 205 (line)]] | alt | 168 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.15× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 187 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.19× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 311 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 1.90× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 287 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +12.5) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H460 (line)]] | wt | 312 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.80× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 226 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW1417 (line)]] | alt | 327 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 1.55× (z +8.6) | — |
| [[SW480 (line)]] | alt | 380 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.656× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 240 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 176 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 241 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[H4 (line)]] | wt | 251 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Selinexor (drug)]] 5 µM 0.574× (z -9.3) ⚠ cell-cycle shift, explains ~86% of this change |
| [[HEC-1-A (line)]] | alt | 252 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.649× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 159 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 199 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 243 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 186 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H23 (line)]] | alt | 399 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Belinostat (drug)]] 5 µM 0.604× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 206 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[Panc 03.27 (line)]] | alt | 197 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.588× (z -8.7) |
| [[RKO (line)]] | wt | 368 | 3 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 3.04× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 265 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SHP-77 (line)]] | alt | 365 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.64× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 252 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 208 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 273 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 301 | 2 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.85× (z +10.2) ⚠ unreliable plate only | — |
| [[HCT15 (line)]] | alt | 246 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW48 (line)]] | wt | 278 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2122 (line)]] | alt | 228 | 0 | 1 | — | [[Berbamine (dihydrochloride) (drug)]] 0.5 µM 0.0594× (z -8.6) |
| [[AN3 CA (line)]] | alt | 310 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 366 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 259 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 327 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 238 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | +0.79 | +0.78 / +0.84 | both halves | 7e-06 | pathway: Cytosolic sensors of pathogen-associated DNA; STRING 999 |
| [[NUP155]] | +0.79 | +0.75 / +0.78 | both halves | 7e-06 | pathway: HIV Infection |
| [[SUPT16H]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 | pathway: HIV Infection; STRING 665 |
| [[TMX3]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[IPO5]] | +0.69 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[MACROH2A1]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 | STRING 514 |
| [[CAPRIN1]] | +0.67 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[PTPN11]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[DARS2]] | +0.67 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[LAS1L]] | +0.66 | +0.64 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37D]] | -0.72 | -0.56 / -0.73 | both halves | 1e-05 | pathway: HIV Infection |
| [[SAT2]] | -0.72 | -0.73 / -0.71 | both halves | 7e-06 |  |
| [[CNNM4]] | -0.71 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.69 | -0.53 / -0.76 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.67 | -0.57 / -0.69 | both halves | 1e-05 |  |
| [[BLVRB]] | -0.67 | -0.54 / -0.72 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[SNHG9]] | -0.66 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[ZFAND2B]] | -0.65 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.65 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[SNHG7]] | -0.65 | -0.61 / -0.70 | both halves | 7e-06 |  |
| [[BRI3]] | -0.65 | -0.57 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KREMEN2]] | B | KREMEN2 activity raises XRCC5's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without KREMEN2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[TEC]] | B | TEC activity lowers XRCC5's level | lines that do not express TEC (8) vs lines expressing it (42) | 1.09× higher at baseline in the lines without TEC | 0.060 | ⚠ within organs, on part of the lines; also absent: TXK; maybe low, not absent; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises XRCC5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises XRCC5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PIK3IP1]] | B | PIK3IP1 activity lowers XRCC5's level | lines that do not express PIK3IP1 (8) vs lines expressing it (42) | 1.12× higher at baseline in the lines without PIK3IP1 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MIR193BHG]] | C | MIR193BHG activity lowers XRCC5's level | lines that do not express MIR193BHG (4) vs lines expressing it (46) | 1.41× higher at baseline in the lines without MIR193BHG | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FLVCR2, NINJ1, ZNF845; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.7, -32.5); signed map (-13.8, -44.7). **Vector** length 126, 45.2% of its response variance represented; |z| ≥ 3 in 1,540 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +5.8 | +23.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.7 | +21.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.3 | +14.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +9.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.2 | +3.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +4.0 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.2 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -6.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -6.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | -4.2 | -3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.2 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.0 | -4.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | X-ray repair cross complementing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:216,107,464-216,206,303 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KU80, KARP-1, Ku86, KUB2 |
| Gene groups (HGNC) | DNA-(apurinic or apyrimidinic site) lyases |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 14 pathways, smallest: 2-LTR circle formation; Integration of provirus; IRF3-mediated induction of type I IFN |
| Matched by | ensembl_id |

**Function**, from UniProt [P13010](https://www.uniprot.org/uniprotkb/P13010) (DNA repair protein Ku80):

> DNA-binding protein critical for the DNA damage response, specifically in repairing double-strand breaks (DSBs) via the classical non-homologous end joining (NHEJ) pathway. It forms a heterodimer with XRCC6 (Ku70), creating the Ku70:Ku80 heterodimer (Ku complex), which serves as a DNA end-binding complex. It primarily binds DSBs and recruits essential repair factors, assembling the core long-range NHEJ complex to facilitate the alignment and ligation of broken DNA ends. This pathway ensures the …

**Summary**, from NCBI Gene [7520](https://www.ncbi.nlm.nih.gov/gene/7520):

> The protein encoded by this gene is the 80-kilodalton subunit of the Ku heterodimer protein which is also known as ATP-dependant DNA helicase II or DNA repair protein XRCC5. Ku is the DNA-binding component of the DNA-dependent protein kinase, and it functions together with the DNA ligase IV-XRCC4 complex in the repair of DNA double-strand break by non-homologous end joining and the completion of V(D)J recombination events. This gene functionally complements Chinese hamster xrs-6, a mutant …

**Accessions** — [HGNC:12833](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12833) · Entrez [7520](https://www.ncbi.nlm.nih.gov/gene/7520) · UniProt [P13010](https://www.uniprot.org/uniprotkb/P13010) · Ensembl [ENSG00000079246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079246)

## Data

Gene col 1245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1245); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1245]; `tensor/DDL_lfc|DDL_z.npy` [1245]; `embed/gene_vectors.npy` [1245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1245 or target_col == 1245). Every well: [[XRCC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRCC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
