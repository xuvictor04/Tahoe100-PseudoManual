---
symbol: "C3orf38"
type: "gene"
col: 10989
ensembl_id: "ENSG00000179021"
name: "chromosome 3 open reading frame 38"
location: "3p11.1"
module: 23
arm: "+"
pooled_cpm: 28.38
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# C3orf38

*chromosome 3 open reading frame 38* — 3p11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +19.2, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.681× (z -8.7, q 3e-15, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM: 0.845× (z -3.8, q 0.010, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW1417 0.251×, A-172 0.269×, HEC-1-A 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (NCI-H2347 0.102×; ⚠ toxic); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.109×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.121×); [[Capmatinib (drug)]] 5 µM in 1 line (HCT15 0.0779×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A1]] (+0.80, fdr 7e-06), [[N4BP2L1]] (+0.78, fdr 7e-06), [[THAP2]] (+0.78, fdr 7e-06); moves opposite to [[DGKD]] (-0.69, fdr 1e-05), [[ARHGAP8]] (-0.68, fdr 4e-05), [[GMDS]] (-0.67, fdr 1e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ZFP30]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10989.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +19.2 | 0e+00 | 41/47 (A549, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +17.6 | 0e+00 | 41/48 (HS-578T, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +15.7 | 0e+00 | 42/47 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.26×** | +13.9 | 8e-42 | 44/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +13.0 | 2e-36 | 41/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +12.5 | 5e-34 | 36/46 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +9.4 | 4e-19 | 26/48 (HEC-1-A, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +9.3 | 2e-18 | 33/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +6.9 | 4e-10 | 28/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.9 | 2e-07 | 22/48 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.3 | 9e-04 | 17/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 18/47 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.002 | 8/48 (LoVo, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.002 | 17/48 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.011 | 16/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.022 | 17/48 (RKO, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10989.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW1417 0.251×, A-172 0.269×, HEC-1-A 0.342×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.131×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (NCI-H2347 0.102×; ⚠ toxic); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.109×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.121×); [[Capmatinib (drug)]] 5 µM in 1 line (HCT15 0.0779×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.681×** | -8.7 | 3e-15 | 33/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.695×** | -7.9 | 8e-13 | 19/38 (SW1417, A-172, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -6.8 | 3e-09 | 25/48 (HEC-1-A, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.757×** | -6.3 | 5e-08 | 26/48 (RPMI-7951, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.767×** | -6.0 | 3e-07 | 20/42 (AN3 CA, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.806×** | -4.9 | 1e-04 | 19/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.7 | 2e-04 | 1/48 (SW48) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.845× | -3.8 | 0.010 | 16/48 (HCT15, HOP62, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.052 | 6/47 (HEC-1-A, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.10 | 2/48 (HEC-1-A, PANC-1) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.908× | -3.1 | 0.10 | 10/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.873× | -3.1 | 0.10 | 12/48 (Panc 03.27, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10989. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.8 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 43.1 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 17.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.2) | — |
| [[A549 (line)]] | wt | 24.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 19.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 37.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 50.0 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.109× (z -11.5) |
| [[KATO III (line)]] | alt | 27.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.28× (z +9.2) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[LOX-IMVI (line)]] | wt | 26.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 37.8 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.72× (z +10.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.1) | — |
| [[SW480 (line)]] | alt | 35.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.10× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 35.7 | 0 | 1 | — | [[Capmatinib (drug)]] 5 µM 0.0779× (z -9.2) |
| [[HOP62 (line)]] | alt | 29.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +12.3) | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.5) | — |
| [[J82 (line)]] | alt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.102× (z -15.1) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 20.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.48× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 46.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.7) | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10989), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A1]] | +0.80 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.78 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[THAP2]] | +0.78 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[MAIP1]] | +0.77 | +0.79 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHF2]] | +0.75 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[ATE1OSP]] | +0.74 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[FAM200A]] | +0.74 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[METTL6]] | +0.73 | +0.77 / +0.35 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | +0.73 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[RBM48]] | +0.73 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.72 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[CCDC59]] | +0.72 | +0.73 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKD]] | -0.69 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ARHGAP8]] | -0.68 | -0.69 / -0.41 | both halves | 4e-05 |  |
| [[GMDS]] | -0.67 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.66 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[TBCD]] | -0.64 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[APMAP]] | -0.64 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[AHCY]] | -0.64 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[RSU1]] | -0.64 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[TBC1D16]] | -0.63 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[NPHP4]] | -0.63 | -0.60 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFP30]] | B | ZFP30 activity raises C3orf38's level | lines that do not express ZFP30 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without ZFP30 | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF420, ZNF461 |
| [[ZNF675]] | B | ZNF675 activity raises C3orf38's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.41× lower at baseline in the lines without ZNF675 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[HDAC6]] | B | HDAC6 activity raises C3orf38's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers C3orf38's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DCP1B]] | C | DCP1B activity raises C3orf38's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without DCP1B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.785). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (0.9, 16.7); signed map (23.7, -12.3). **Vector** length 97.6, 21.7% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.1 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +15.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +19.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +2.6 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.7 | -6.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.2 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.7 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -4.3 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 3 open reading frame 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p11.1 — chr3:88,149,959-88,168,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26717 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JPI3](https://www.uniprot.org/uniprotkb/Q5JPI3) (Uncharacterized protein C3orf38):

> May be involved in apoptosis regulation.

**Summary**, from NCBI Gene [285237](https://www.ncbi.nlm.nih.gov/gene/285237):

> Involved in positive regulation of apoptotic process. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28384) · Entrez [285237](https://www.ncbi.nlm.nih.gov/gene/285237) · UniProt [Q5JPI3](https://www.uniprot.org/uniprotkb/Q5JPI3) · Ensembl [ENSG00000179021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179021)

## Data

Gene col 10989: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10989); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10989, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10989]; `tensor/DDL_lfc|DDL_z.npy` [10989]; `embed/gene_vectors.npy` [10989]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10989 or target_col == 10989). Every well: [[C3orf38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
