---
symbol: "PTDSS1"
type: "gene"
col: 7984
ensembl_id: "ENSG00000156471"
name: "phosphatidylserine synthase 1"
location: "8q22.1"
module: 12
arm: "-"
pooled_cpm: 36.43
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 10
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PTDSS1

*phosphatidylserine synthase 1* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.41× (z +21.4, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 0.770× (z -4.5, q 0.003, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPS2]] (+0.68, fdr 7e-06), [[TXNDC5]] (+0.66, fdr 1e-05), [[TFRC]] (+0.64, fdr 7e-06); moves opposite to [[RAB9A]] (-0.64, fdr 1e-05), [[PIGBOS1]] (-0.64, fdr 3e-05), [[ZNF226]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +21.4 | 0e+00 | 45/48 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.56×** | +16.2 | 0e+00 | 43/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.38×** | +14.9 | 0e+00 | 43/48 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.20×** | +13.0 | 1e-36 | 37/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.13×** | +12.5 | 1e-33 | 40/48 (HOP62, HS-578T, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **2.11×** | +12.4 | 4e-33 | 28/39 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.09×** | +10.3 | 6e-23 | 40/48 (NCI-H2030, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +10.3 | 8e-23 | 36/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **1.80×** | +10.1 | 3e-22 | 36/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +9.3 | 7e-19 | 41/48 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.52×** | +7.2 | 4e-11 | 31/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.3 | 1e-08 | 32/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.41×** | +5.9 | 2e-07 | 28/48 (NCI-H2030, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.7 | 5e-07 | 24/47 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.35×** | +5.1 | 1e-05 | 23/48 (LS 180, SW480, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.002 | 15/48 (LS 180, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.006 | 11/48 (NCI-H2030, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.008 | 15/48 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.010 | 16/47 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.012 | 12/47 (HOP62, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.014 | 13/48 (NCI-H460, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.017 | 10/48 (NCI-H460, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.019 | 8/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.025 | 6/48 (NCI-H460, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.033 | 13/47 (AsPC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.050 | 8/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.770×** | -4.5 | 0.003 | 22/47 (SW 900, SNU-1, …) | two highest doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.773×** | -4.4 | 0.003 | 22/48 (RKO, A498, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.796×** | -3.8 | 0.031 | 18/47 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.865× | -3.5 | 0.042 | 10/48 (A498, NCI-H1573, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.861× | -3.5 | 0.042 | 10/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.817×** | -3.5 | 0.042 | 12/48 (A498, RKO, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -3.5 | 0.042 | 10/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.045 | 15/47 (RKO, HepG2/C3A, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.690×** | -3.3 | 0.053 | 8/48 (HOP62, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.065 | 11/48 (A-172, C32, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.077 | 16/47 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.879× | -3.1 | 0.082 | 12/48 (HEC-1-A, A498, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.779×** | -3.1 | 0.095 | 10/48 (LS 180, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.838× | -3.0 | 0.095 | 15/47 (NCI-H661, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 32.1 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +14.7) | — |
| [[HS-578T (line)]] | alt | 50.5 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 23.2 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 27.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +15.4) | — |
| [[PANC-1 (line)]] | alt | 31.1 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +15.0) | — |
| [[AsPC-1 (line)]] | alt | 23.0 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.31× (z +12.1) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 48.9 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +14.5) | — |
| [[LoVo (line)]] | wt | 23.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.8) | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.17× (z +12.9) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[A-172 (line)]] | wt | 23.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.8) | — |
| [[LOX-IMVI (line)]] | wt | 56.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 23.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | — |
| [[SW 900 (line)]] | alt | 26.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +10.1) | — |
| [[A549 (line)]] | wt | 27.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +9.9) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[C32 (line)]] | wt | 78.4 | 2 (2 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +9.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 50.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 30.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 42.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SW1417 (line)]] | alt | 34.8 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.3) | — |
| [[A-427 (line)]] | wt | 21.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +9.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[BT-474 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[Hs 766T (line)]] | wt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 31.2 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.218× (z -9.0) |
| [[KATO III (line)]] | alt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | — |
| [[LS 180 (line)]] | wt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +13.7) | — |
| [[RKO (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 32.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 49.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 27.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.2) | — |
| [[SW48 (line)]] | wt | 45.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SW480 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS2]] | +0.68 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TFRC]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ACLY]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SMYD2]] | +0.63 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[PAICS]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[BPNT2]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[PGRMC1]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[BUD23]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MYH10]] | +0.58 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[SIGMAR1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DPAGT1]] | +0.57 | +0.39 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB9A]] | -0.64 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.64 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[ZNF226]] | -0.63 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[COIL]] | -0.62 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[SEC62]] | -0.61 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[SRSF11]] ⚠ | -0.61 | -0.54 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PPIG]] | -0.61 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.60 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.59 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[CHURC1]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SAT2]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.58 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[FRG1]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTDSS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.6, 1.6); signed map (-47.1, 25.4). **Vector** length 100, 26.9% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.2 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.5 | +12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +21.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | +5.0 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +5.0 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +10.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.7 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylserine synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:96,261,902-96,336,995 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0024, PSSA, PSS1 |
| Reactome | 3 pathways, smallest: Glycerophospholipid biosynthesis; Phospholipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [P48651](https://www.uniprot.org/uniprotkb/P48651) (Phosphatidylserine synthase 1):

> Catalyzes a base-exchange reaction in which the polar head group of phosphatidylethanolamine (PE) or phosphatidylcholine (PC) is replaced by L-serine. Catalyzes mainly the conversion of phosphatidylcholine. Also converts, in vitro and to a lesser extent, phosphatidylethanolamine.

**Summary**, from NCBI Gene [9791](https://www.ncbi.nlm.nih.gov/gene/9791):

> The protein encoded by this gene catalyzes the formation of phosphatidylserine from either phosphatidylcholine or phosphatidylethanolamine. Phosphatidylserine localizes to the mitochondria-associated membrane of the endoplasmic reticulum, where it serves a structural role as well as a signaling role. Defects in this gene are a cause of Lenz-Majewski hyperostotic dwarfism. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:9587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9587) · Entrez [9791](https://www.ncbi.nlm.nih.gov/gene/9791) · UniProt [P48651](https://www.uniprot.org/uniprotkb/P48651) · Ensembl [ENSG00000156471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156471)

## Data

Gene col 7984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7984); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7984]; `tensor/DDL_lfc|DDL_z.npy` [7984]; `embed/gene_vectors.npy` [7984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7984 or target_col == 7984). Every well: [[PTDSS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTDSS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
