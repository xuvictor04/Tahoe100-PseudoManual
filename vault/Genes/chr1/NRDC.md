---
symbol: "NRDC"
type: "gene"
col: 1226
ensembl_id: "ENSG00000078618"
name: "nardilysin convertase"
location: "1p32.3"
module: 51
arm: "+"
pooled_cpm: 162.6
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NRDC

*nardilysin convertase* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.85× (z +15.1, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.33× (z +7.0, q 3e-10, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.748× (z -7.1, q 7e-10, down in 27 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H1573 0.364×, HepG2/C3A 0.303×, PANC-1 0.604×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 2 lines (Panc 03.27 0.103×, NCI-H1573 0.263×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 0.415×, PANC-1 0.594×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW 1088 0.0817×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMARCA5]] (+0.55, fdr 2e-05), [[DNAJC8]] (+0.53, fdr 1e-05), [[ATF6]] (+0.51, fdr 1e-05); moves opposite to [[LSM11]] (-0.50, fdr 2e-05), [[RBM38]] (-0.50, fdr 1e-04), [[FAM110A]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +15.1 | 0e+00 | 45/49 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +14.7 | 0e+00 | 35/44 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +7.7 | 2e-12 | 34/45 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +7.0 | 3e-10 | 36/48 (HEC-1-A, COLO 205, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.25×** | +5.5 | 4e-06 | 27/48 (Hs 766T, J82, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +5.4 | 7e-06 | 28/49 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.24×** | +5.4 | 7e-06 | 28/48 (Hs 766T, J82, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +5.1 | 2e-05 | 25/47 (KATO III, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | **1.20×** | +4.3 | 0.001 | 24/48 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 5 µM |  | 1.13× | +4.2 | 0.002 | 6/49 (C-33 A, KATO III, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.13× | +4.2 | 0.002 | 10/48 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.19× | +4.1 | 0.002 | 21/48 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.9 | 0.004 | 20/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.8 | 0.006 | 9/49 (NCI-H23, SK-MEL-2, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | 1.17× | +3.8 | 0.006 | 21/47 (COLO 205, HEC-1-A, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.6 | 0.012 | 8/48 (MIA PaCa-2, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.020 | 13/47 (A549, Hs 766T, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.2 | 0.036 | 12/49 (NCI-H23, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.044 | 11/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.048 | 13/48 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.065 | 19/48 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.09× | +2.9 | 0.073 | 2/48 (SW1417, H4) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.13× | +2.9 | 0.074 | 7/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1226.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H1573 0.364×, HepG2/C3A 0.303×, PANC-1 0.604×; ⚠ toxic; transcription drop); [[Lonafarnib (drug)]] 5 µM in 2 lines (Panc 03.27 0.103×, NCI-H1573 0.263×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 0.415×, PANC-1 0.594×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bendamustine (drug)]] 5 µM in 1 line (SW 1088 0.0817×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.748×** | -7.1 | 7e-10 | 27/48 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.680×** | -4.9 | 2e-04 | 24/38 (Panc 03.27, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -4.3 | 0.003 | 14/48 (PANC-1, J82, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -4.2 | 0.005 | 21/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.892× | -4.0 | 0.009 | 18/48 (NCI-H1573, NCI-H1792, …) | top dose only | composition shift |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.900× | -3.6 | 0.025 | 1/49 (AsPC-1) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.864× | -3.4 | 0.046 | 22/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.908× | -3.4 | 0.057 | 9/49 (C-33 A, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.3 | 0.067 | 17/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.877× | -3.2 | 0.070 | 11/49 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.882× | -3.1 | 0.11 | 7/49 (A-427, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 192 | 1 (1 ⚠) | 6 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.364× (z -13.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 228 | 2 (2 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +14.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.594× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 126 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.16× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 136 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.69× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 198 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +11.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 182 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +15.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 130 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +15.5) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.608× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 206 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +12.9) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.302× (z -9.2) ⚠ toxic |
| [[A549 (line)]] | wt | 133 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 150 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +15.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 222 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +12.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 165 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.00× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 125 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.18× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -9.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H2030 (line)]] | alt | 178 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +12.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 143 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +10.1) ⚠ toxic; transcription drop | [[Lonafarnib (drug)]] 5 µM 0.103× (z -15.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 152 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 151 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +10.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 235 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -9.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[NCI-H23 (line)]] | alt | 277 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.72× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.451× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 185 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +13.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 174 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 165 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.491× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -12.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.622× (z -8.7) ⚠ cell-cycle shift, explains ~21% of this change |
| [[LoVo (line)]] | wt | 232 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -9.1) ⚠ cell-cycle shift, explains ~21% of this change |
| [[LOX-IMVI (line)]] | wt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.86× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 150 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.26× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 181 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0817× (z -12.6) |
| [[SW 900 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +10.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 244 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA5]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[DNAJC8]] | +0.53 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ATF6]] | +0.51 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[HNRNPC]] | +0.50 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[ATRX]] | +0.50 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[HECTD1]] | +0.50 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[HUWE1]] | +0.49 | +0.34 / +0.57 | both halves | 1e-04 | same gene group |
| [[GOLM2]] | +0.48 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[UGGT1]] | +0.48 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[IDE]] | +0.48 | +0.43 / +0.55 | both halves | 3e-05 | same gene group |
| [[BRCC3]] | +0.47 | +0.49 / +0.43 | both halves | 4e-05 |  |
| [[WNK1]] | +0.47 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM11]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[RBM38]] | -0.50 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[FAM110A]] | -0.48 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[TNFRSF11A]] | -0.47 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[ACADS]] | -0.45 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[CNNM4]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 | same gene group |
| [[CYB561D1]] | -0.45 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[POLR1H]] | -0.44 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[RCE1]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[CEP68]] | -0.44 | -0.21 / -0.49 | both halves | 7e-04 |  |
| [[MIR17HG]] | -0.43 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[AFMID]] | -0.43 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers NRDC's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.209). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-22.5, 9.6); signed map (19.2, -39.6). **Vector** length 128, 38.6% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.9 | +7.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | +4.6 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +2.8 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.5 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -9.1 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -6.3 | -4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -4.1 | -1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -4.1 | -1.0 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -3.2 | -2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | nardilysin convertase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:51,789,191-51,878,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hNRD1, hNRD2; previously NRD1 |
| Gene groups (HGNC) | M16 metallopeptidases; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O43847](https://www.uniprot.org/uniprotkb/O43847) (Nardilysin):

> Cleaves peptide substrates on the N-terminus of arginine residues in dibasic pairs. Is a critical activator of BACE1- and ADAM17-mediated pro-neuregulin ectodomain shedding, involved in the positive regulation of axonal maturation and myelination. Required for proper functioning of 2-oxoglutarate dehydrogenase (OGDH) (By similarity).

**Summary**, from NCBI Gene [4898](https://www.ncbi.nlm.nih.gov/gene/4898):

> This gene encodes a zinc-dependent endopeptidase that cleaves peptide substrates at the N-terminus of arginine residues in dibasic moieties and is a member of the peptidase M16 family. This protein interacts with heparin-binding EGF-like growth factor and plays a role in cell migration and proliferation. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:7995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7995) · Entrez [4898](https://www.ncbi.nlm.nih.gov/gene/4898) · UniProt [O43847](https://www.uniprot.org/uniprotkb/O43847) · Ensembl [ENSG00000078618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078618)

## Data

Gene col 1226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1226); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1226]; `tensor/DDL_lfc|DDL_z.npy` [1226]; `embed/gene_vectors.npy` [1226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1226 or target_col == 1226). Every well: [[NRDC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRDC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
