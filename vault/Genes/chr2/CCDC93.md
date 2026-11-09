---
symbol: "CCDC93"
type: "gene"
col: 4635
ensembl_id: "ENSG00000125633"
name: "CCC complex scaffolding subunit CCDC93"
location: "2q14.1"
module: 3
arm: "+"
pooled_cpm: 118.06
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CCDC93

*CCC complex scaffolding subunit CCDC93* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +11.9, q 7e-30, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.453× (z -14.0, q 1e-41, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.862× (z -3.8, q 0.015, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (A-427 0.145×, MIA PaCa-2 0.166×, Hs 766T 0.157×, A549 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 0.341×, SNU-1 0.189×, A498 0.381×, NCI-H2347 0.389×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.553×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM65]] (+0.55, fdr 1e-05), [[HEBP1]] (+0.53, fdr 1e-05), [[DGKE]] (+0.53, fdr 3e-05); moves opposite to [[MCRS1]] (-0.50, fdr 1e-05), [[DCAF1]] (-0.49, fdr 1e-04), [[ZNF268]] (-0.48, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +11.9 | 7e-30 | 36/48 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +10.1 | 1e-21 | 45/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +8.8 | 2e-16 | 44/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +7.6 | 5e-12 | 36/48 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +7.2 | 5e-11 | 36/48 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +6.2 | 6e-08 | 37/49 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 28/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.1 | 0.004 | 25/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +4.0 | 0.004 | 24/48 (J82, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.006 | 26/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.011 | 24/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.037 | 25/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.059 | 19/48 (RKO, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.076 | 20/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.1 | 0.079 | 17/47 (SNU-1, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.0 | 0.095 | 8/49 (CFPAC-1, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4635.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (A-427 0.145×, MIA PaCa-2 0.166×, Hs 766T 0.157×, A549 0.214×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 0.341×, SNU-1 0.189×, A498 0.381×, NCI-H2347 0.389×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.553×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.453×** | -14.0 | 1e-41 | 40/44 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.484×** | -13.3 | 7e-38 | 46/49 (HEC-1-A, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.574×** | -9.4 | 1e-18 | 37/45 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -6.6 | 7e-09 | 35/47 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -3.8 | 0.015 | 17/48 (A549, A-172, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.833×** | -3.3 | 0.078 | 22/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.843× | -3.1 | 0.15 | 19/47 (HOP62, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 81.7 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 111 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -10.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 148 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -12.0) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 241 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -15.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 181 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 111 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -12.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 73.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +25.2) | — |
| [[SNU-423 (line)]] | alt | 176 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -12.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 147 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -16.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 99.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -20.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 127 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +13.7) | — |
| [[SHP-77 (line)]] | alt | 99.1 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 60.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -21.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 137 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -13.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.04× (z +10.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.0) | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 98.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -12.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 104 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 60.8 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -13.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 114 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.553× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 90.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +21.2) | — |
| [[SNU-1 (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -14.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.234× (z -13.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 83.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.266× (z -10.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -18.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 93.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.431× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -9.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -12.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.514× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 95.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM65]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HEBP1]] | +0.53 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[DGKE]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[LDAF1]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TRIM33]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CIB2]] | +0.49 | +0.39 / +0.37 | both halves | 8e-05 |  |
| [[CERT1]] | +0.49 | +0.61 / +0.37 | both halves | 8e-05 |  |
| [[CCDC82]] | +0.48 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[LACTB]] | +0.48 | +0.34 / +0.44 | both halves | 1e-04 |  |
| [[HEBP2]] | +0.47 | +0.54 / +0.36 | both halves | 1e-04 |  |
| [[TBC1D12]] | +0.47 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[NAP1L1]] | +0.47 | +0.44 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCRS1]] | -0.50 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[DCAF1]] | -0.49 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[ZNF268]] | -0.48 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RBM4]] | -0.47 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ERH]] | -0.46 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[EPC2]] | -0.46 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[MAGED1]] | -0.45 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[NOL6]] | -0.45 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[SARS2]] | -0.44 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[SRSF6]] | -0.44 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ZNF644]] | -0.43 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[EDC3]] | -0.43 | -0.33 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.300). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-11.1, -1.5); signed map (-21.1, 14.8). **Vector** length 73.3, 19.3% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | -14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | -13.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.6 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +3.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.4 | +2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.4 | +6.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | +0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.0 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.9 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -1.2 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | CCC complex scaffolding subunit CCDC93 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:117,915,478-118,014,133 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10996 |
| Gene groups (HGNC) | CCC complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q567U6](https://www.uniprot.org/uniprotkb/Q567U6) (Coiled-coil domain-containing protein 93):

> Component of the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of composed of the CCC subcomplex and the retriever subcomplex. Component of the CCC complex, which is involved in the regulation of endosomal recycling of surface proteins, including integrins, signaling receptor and channels. The CCC complex associates with SNX17, retriever and WASH complexes to prevent lysosomal degradation and promote cell surface recycling …

**Summary**, from NCBI Gene [54520](https://www.ncbi.nlm.nih.gov/gene/54520):

> Involved in Golgi to plasma membrane transport and endocytic recycling. Located in plasma membrane. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25611) · Entrez [54520](https://www.ncbi.nlm.nih.gov/gene/54520) · UniProt [Q567U6](https://www.uniprot.org/uniprotkb/Q567U6) · Ensembl [ENSG00000125633](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125633)

## Data

Gene col 4635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4635); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4635]; `tensor/DDL_lfc|DDL_z.npy` [4635]; `embed/gene_vectors.npy` [4635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4635 or target_col == 4635). Every well: [[CCDC93 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC93.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
