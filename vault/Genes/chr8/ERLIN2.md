---
symbol: "ERLIN2"
type: "gene"
col: 7189
ensembl_id: "ENSG00000147475"
name: "ER lipid raft associated 2"
location: "8p11.23"
module: 25
arm: "+"
pooled_cpm: 19.62
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ERLIN2

*ER lipid raft associated 2* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.25× (z +18.0, q 0e+00, up in 39 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +9.3, q 2e-18, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.565× (z -8.7, q 2e-15, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DR1]] (+0.75, fdr 7e-06), [[PRKAR1A]] (+0.73, fdr 7e-06), [[LIN7C]] (+0.70, fdr 1e-05); moves opposite to [[RPP21]] (-0.71, fdr 7e-06), [[RPL36AL]] (-0.68, fdr 1e-04, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[CAMLG]] (-0.67, fdr 1e-05), [[SNHG7]] (-0.66, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +18.0 | 0e+00 | 39/41 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.40×** | +17.9 | 0e+00 | 33/34 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +14.9 | 0e+00 | 29/35 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +9.3 | 2e-18 | 34/47 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +5.0 | 6e-05 | 22/48 (KATO III, LoVo, …) | rises with dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +5.0 | 6e-05 | 19/47 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +3.7 | 0.021 | 11/47 (Hs 766T, SNU-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.28×** | +3.6 | 0.021 | 16/47 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.049 | 9/48 (HS-578T, HepG2/C3A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +3.3 | 0.051 | 8/47 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.3 | 0.051 | 16/48 (KATO III, HS-578T, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.16× | +3.3 | 0.051 | 8/48 (NCI-H2347, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +3.2 | 0.052 | 17/46 (HS-578T, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +3.2 | 0.064 | 10/45 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.22×** | +3.0 | 0.089 | 11/48 (SW480, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.090 | 13/48 (KATO III, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7189.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.565×** | -8.7 | 2e-15 | 36/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.571×** | -8.5 | 4e-15 | 33/48 (LS 180, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -6.2 | 1e-07 | 30/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.655×** | -6.1 | 2e-07 | 29/47 (J82, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.532×** | -5.0 | 6e-05 | 19/38 (Panc 03.27, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.764×** | -4.1 | 0.004 | 20/46 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -4.0 | 0.005 | 18/46 (NCI-H23, H4, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.706×** | -3.8 | 0.011 | 12/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.786×** | -3.7 | 0.016 | 14/48 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.672×** | -3.2 | 0.089 | 7/46 (Hs 766T, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 22.5 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.71× (z +9.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.244× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.369× (z -9.9) |
| [[LS 180 (line)]] | wt | 30.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +11.7) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.321× (z -9.5) |
| [[A498 (line)]] | wt | 21.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 27.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.32× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 27.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 25.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +10.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 36.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +13.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 17.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.62× (z +13.3) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.302× (z -8.8) |
| [[A549 (line)]] | wt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.31× (z +13.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.82× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.40× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 7.68 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0794× (z -10.7) |
| [[H4 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.36× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.105× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0712× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0823× (z -8.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 8.02 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.299× (z -8.5) |
| [[SHP-77 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DR1]] | +0.75 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[PRKAR1A]] | +0.73 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.70 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.70 | +0.45 / +0.76 | both halves | 3e-05 |  |
| [[EMC1]] | +0.70 | +0.48 / +0.75 | both halves | 2e-05 | STRING 513 |
| [[BTBD1]] | +0.69 | +0.38 / +0.75 | both halves | 6e-05 |  |
| [[MOB1A]] | +0.69 | +0.43 / +0.73 | both halves | 4e-05 |  |
| [[ALG10B]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[MBTPS2]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[GNS]] | +0.67 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[DHFR]] | +0.67 | +0.32 / +0.68 | both halves | 2e-04 |  |
| [[TUG1]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP21]] | -0.71 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | -0.68 | -0.36 / -0.72 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CAMLG]] | -0.67 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.66 | -0.38 / -0.66 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL18]] ⚠ | -0.66 | -0.41 / -0.66 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | -0.66 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[ARID3A]] | -0.65 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[RPL36]] | -0.64 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[LIN7B]] | -0.64 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[RASSF7]] | -0.63 | -0.38 / -0.67 | both halves | 6e-05 |  |
| [[BAHD1]] | -0.63 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ARL8A]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[SNHG6]] | -0.61 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[ATP5MJ]] | -0.61 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[POLR2I]] | -0.61 | -0.40 / -0.57 | both halves | 5e-05 | pathway: Signaling by FGFR in disease |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERLIN2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises ERLIN2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.2, -22.0); signed map (-16.9, -37.8). **Vector** length 91.2, 19.7% of its response variance represented; |z| ≥ 3 in 992 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +17.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.4 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -3.2 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.6 | +2.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.4 | -8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.8 | -6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -8.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | ER lipid raft associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:37,736,601-37,758,422 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NET32, Erlin-2; previously C8orf2, SPFH2, SPG18 |
| Reactome | 16 pathways, smallest: Signaling by plasma membrane FGFR1 fusions; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [O94905](https://www.uniprot.org/uniprotkb/O94905) (Erlin-2):

> Component of the ERLIN1/ERLIN2 complex which mediates the endoplasmic reticulum-associated degradation (ERAD) of inositol 1,4,5-trisphosphate receptors (IP3Rs) such as ITPR1. Promotes sterol-accelerated ERAD of HMGCR probably implicating an AMFR/gp78-containing ubiquitin ligase complex. Involved in regulation of cellular cholesterol homeostasis by regulation the SREBP signaling pathway. May promote ER retention of the SCAP-SREBF complex.

**Summary**, from NCBI Gene [11160](https://www.ncbi.nlm.nih.gov/gene/11160):

> This gene encodes a member of the SPFH domain-containing family of lipid raft-associated proteins. The encoded protein is localized to lipid rafts of the endoplasmic reticulum and plays a critical role in inositol 1,4,5-trisphosphate (IP3) signaling by mediating ER-associated degradation of activated IP3 receptors. Mutations in this gene are a cause of spastic paraplegia-18 (SPG18). Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided …

**Accessions** — [HGNC:1356](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1356) · Entrez [11160](https://www.ncbi.nlm.nih.gov/gene/11160) · UniProt [O94905](https://www.uniprot.org/uniprotkb/O94905) · Ensembl [ENSG00000147475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147475)

## Data

Gene col 7189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7189); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7189]; `tensor/DDL_lfc|DDL_z.npy` [7189]; `embed/gene_vectors.npy` [7189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7189 or target_col == 7189). Every well: [[ERLIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERLIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
