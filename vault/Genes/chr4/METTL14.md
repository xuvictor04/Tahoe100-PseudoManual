---
symbol: "METTL14"
type: "gene"
col: 6986
ensembl_id: "ENSG00000145388"
name: "methyltransferase 14, N6-adenosine-methyltransferase non-catalytic subunit"
location: "4q26"
module: 17
arm: "+"
pooled_cpm: 42.15
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# METTL14

*methyltransferase 14, N6-adenosine-methyltransferase non-catalytic subunit* — 4q26

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +13.9, q 2e-41, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.389× (z -16.8, q 0e+00, down in 36 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.812× (z -3.9, q 0.016, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF14]] (+0.73, fdr 7e-06), [[CWC15]] (+0.72, fdr 7e-06), [[ASB8]] (+0.72, fdr 7e-06); moves opposite to [[GATAD2A]] (-0.58, fdr 7e-06), [[TTL]] (-0.58, fdr 1e-05), [[DDX5]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → cells under [[Almonertinib (mesylate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +13.9 | 2e-41 | 40/48 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.63×** | +12.5 | 2e-33 | 45/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +9.4 | 8e-19 | 44/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +9.1 | 1e-17 | 47/48 (RKO, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +9.0 | 2e-17 | 36/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +8.1 | 4e-14 | 43/48 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.5 | 6e-09 | 27/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +6.5 | 8e-09 | 32/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +5.9 | 2e-07 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +5.5 | 3e-06 | 30/48 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +5.2 | 1e-05 | 23/48 (LoVo, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.2 | 1e-05 | 27/48 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +5.0 | 3e-05 | 25/48 (A-427, A549, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **1.21×** | +3.5 | 0.020 | 19/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +3.4 | 0.027 | 18/48 (SW480, PANC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.041 | 8/48 (HT-29, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.389×** | -16.8 | 0e+00 | 36/41 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.516×** | -12.3 | 4e-32 | 37/47 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.570×** | -9.6 | 1e-19 | 31/44 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.812×** | -3.9 | 0.016 | 17/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.822×** | -3.6 | 0.032 | 17/48 (H4, HCT15, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.837× | -3.3 | 0.086 | 11/48 (SW 1088, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -3.2 | 0.086 | 17/48 (NCI-H2347, A549, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.2 | 0.086 | 14/48 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.787×** | -3.2 | 0.086 | 15/47 (AN3 CA, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.843× | -3.2 | 0.086 | 18/47 (SNU-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | 0.840× | -3.1 | 0.086 | 13/47 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.846× | -3.1 | 0.086 | 17/48 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.792×** | -3.1 | 0.086 | 17/48 (COLO 205, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.794×** | -3.1 | 0.090 | 18/48 (A-427, HS-578T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.850× | -3.0 | 0.090 | 12/48 (AsPC-1, LS 180, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.850× | -3.0 | 0.090 | 12/47 (NCI-H1573, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.5 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.33× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 80.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -19.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 58.9 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.236× (z -11.3) |
| [[A498 (line)]] | wt | 52.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 66.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -10.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 53.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -18.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 47.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0503× (z -28.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 49.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.6) | — |
| [[A-427 (line)]] | wt | 49.7 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.92× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -16.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 71.1 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 5 µM 0.284× (z -9.6) |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 37.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -12.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 38.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -20.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 55.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.4) | — |
| [[SW48 (line)]] | wt | 48.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.91× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -12.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 37.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.0) | — |
| [[C32 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -11.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0931× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 37.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +13.5) | — |
| [[SNU-423 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF14]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CWC15]] | +0.72 | +0.72 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ASB8]] | +0.72 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[MRPL22]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[HEATR6]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[RNF20]] | +0.69 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[FAM133B]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[MRPL44]] | +0.68 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[NDUFS4]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[SECISBP2L]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.58 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[TTL]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[DDX5]] | -0.58 | -0.46 / -0.59 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 412 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Almonertinib (mesylate) (drug)]] 5 µM | C | METTL14's natural level lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | METTL14's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.360 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | C | METTL14's natural level raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | METTL14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.361 over the table, 0.089 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | METTL14's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | METTL14's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.2, -3.7); signed map (-22.4, -10.9). **Vector** length 89.5, 22.0% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.8 | +5.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.9 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.4 | +12.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -3.5 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 14, N6-adenosine-methyltransferase non-catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:118,685,392-118,715,433 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1627 |
| Gene groups (HGNC) | m6A methyltransferase complex; 7BS N6-adenosine DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 2 pathways, smallest: Processing of Capped Intron-Containing Pre-mRNA; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCE5](https://www.uniprot.org/uniprotkb/Q9HCE5) (N(6)-adenosine-methyltransferase non-catalytic subunit METTL14):

> The METTL3-METTL14 heterodimer forms a N6-methyltransferase complex that methylates adenosine residues at the N(6) position of some mRNAs and regulates the circadian clock, differentiation of embryonic stem cells and cortical neurogenesis. In the heterodimer formed with METTL3, METTL14 constitutes the RNA-binding scaffold that recognizes the substrate rather than the catalytic core. N6-methyladenosine (m6A), which takes place at the 5'-[AG]GAC-3' consensus sites of some mRNAs, plays a role in …

**Summary**, from NCBI Gene [57721](https://www.ncbi.nlm.nih.gov/gene/57721):

> Enables mRNA binding activity and mRNA m(6)A methyltransferase activity. Involved in mRNA modification; mRNA splicing, via spliceosome; and mRNA stabilization. Located in nucleoplasm. Part of RNA N6-methyladenosine methyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29330](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29330) · Entrez [57721](https://www.ncbi.nlm.nih.gov/gene/57721) · UniProt [Q9HCE5](https://www.uniprot.org/uniprotkb/Q9HCE5) · Ensembl [ENSG00000145388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145388)

## Data

Gene col 6986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6986); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6986]; `tensor/DDL_lfc|DDL_z.npy` [6986]; `embed/gene_vectors.npy` [6986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6986 or target_col == 6986). Every well: [[METTL14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
