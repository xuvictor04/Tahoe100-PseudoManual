---
symbol: "CKMT2-AS1"
type: "gene"
col: 14498
ensembl_id: "ENSG00000247572"
name: "CKMT2 antisense RNA 1"
location: "5q14.1"
module: 15
arm: "+"
pooled_cpm: 41.84
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 18
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CKMT2-AS1

*CKMT2 antisense RNA 1* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +11.6, q 2e-28, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.519× (z -9.5, q 2e-18, down in 35 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.557× (z -8.5, q 6e-15, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM12]] (+0.63, fdr 1e-05), [[ANKRD17-DT]] (+0.63, fdr 1e-05), [[KDM4D]] (+0.60, fdr 3e-05); moves opposite to [[NDRG3]] (-0.60, fdr 5e-05), [[SMARCD3]] (-0.59, fdr 1e-04), [[MPP1]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +11.6 | 2e-28 | 41/48 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.20×** | +11.4 | 7e-28 | 44/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +10.1 | 2e-21 | 44/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +9.4 | 5e-19 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +8.8 | 2e-16 | 42/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +8.2 | 2e-14 | 29/48 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.7 | 1e-12 | 33/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.9 | 4e-10 | 35/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.3 | 2e-08 | 30/48 (LoVo, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +5.6 | 1e-06 | 32/48 (CFPAC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 7e-05 | 28/48 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.8 | 7e-05 | 31/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.26×** | +4.7 | 9e-05 | 29/48 (CFPAC-1, LoVo, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 5e-04 | 26/48 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.001 | 25/48 (MIA PaCa-2, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.018 | 23/48 (LS 180, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.519×** | -9.5 | 2e-18 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.557×** | -8.5 | 6e-15 | 33/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -8.4 | 6e-15 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.579×** | -7.9 | 4e-13 | 37/48 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.615×** | -7.0 | 3e-10 | 39/48 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.612×** | -6.6 | 5e-09 | 27/43 (LoVo, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.698×** | -5.2 | 2e-05 | 29/46 (J82, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.713×** | -4.7 | 2e-04 | 23/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.726×** | -4.6 | 2e-04 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.545×** | -4.6 | 3e-04 | 20/35 (LOX-IMVI, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -3.7 | 0.009 | 23/48 (HEC-1-A, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.704×** | -3.6 | 0.014 | 14/48 (A-427, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.791×** | -3.2 | 0.050 | 15/48 (BT-474, PANC-1, …) | top dose only | plate-row cell shift |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.794×** | -3.2 | 0.057 | 13/48 (SW 1088, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.8 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.204× (z -13.8) |
| [[SW480 (line)]] | alt | 50.9 | 4 | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +12.6) | [[Digitoxin (drug)]] 0.5 µM 0.370× (z -11.4) |
| [[A498 (line)]] | wt | 33.6 | 1 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -11.4) |
| [[HT-29 (line)]] | alt | 31.3 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +14.0) | [[Digitoxin (drug)]] 5 µM 0.288× (z -9.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 47.2 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.1) | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.366× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 64.3 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -14.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 31.7 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.8) | [[Lonafarnib (drug)]] 5 µM 0.102× (z -9.4) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 56.6 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.250× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 51.1 | 2 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +11.8) | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -15.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 48.2 | 1 | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.355× (z -8.5) |
| [[SHP-77 (line)]] | alt | 61.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[C-33 A (line)]] | alt | 52.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 43.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.4) | [[Ixazomib citrate (drug)]] 5 µM 0.200× (z -10.7) |
| [[HOP62 (line)]] | alt | 52.1 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +13.7) | — |
| [[J82 (line)]] | alt | 49.4 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -8.7) |
| [[KATO III (line)]] | alt | 29.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 44.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.356× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 24.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.222× (z -10.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 30.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.109× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[A-427 (line)]] | wt | 74.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 38.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.127× (z -8.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[COLO 205 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.138× (z -11.1) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.205× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -11.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 33.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 82.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.6) | — |
| [[SW 1271 (line)]] | alt | 81.3 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0890× (z -9.9) |
| [[SW 900 (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -9.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.8) | — |
| [[A-172 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | +0.63 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[KDM4D]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | +0.59 | +0.73 / +0.42 | both halves | 4e-05 | same gene group |
| [[NIFK-AS1]] | +0.58 | +0.69 / +0.43 | both halves | 3e-05 | same gene group |
| [[TMEM187]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[PDCD7]] | +0.57 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[TRAPPC12]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[DNAAF10]] | +0.56 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[TMEM186]] | +0.56 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[STYXL1]] | +0.56 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[DNASE1]] | +0.55 | +0.64 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | -0.60 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[SMARCD3]] | -0.59 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[MPP1]] | -0.58 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[CLSTN1]] | -0.58 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[CERS6]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[HPSE]] | -0.54 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[CAT]] | -0.53 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[HDAC1]] | -0.51 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[FOXO6]] | -0.51 | -0.26 / -0.35 | both halves | 4e-04 |  |
| [[BCAM]] | -0.51 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[CREG1]] | -0.51 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[HSD17B4]] | -0.51 | -0.36 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CKMT2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC16A1-AS1]] | B | SLC16A1-AS1 activity raises CKMT2-AS1's level | lines that do not express SLC16A1-AS1 (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without SLC16A1-AS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: P3H4, SLC16A1, DUSP19 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.438). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.1, 18.3); signed map (19.4, -7.2). **Vector** length 81.9, 20.7% of its response variance represented; |z| ≥ 3 in 1,166 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.6 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +6.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +10.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.7 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | -4.8 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -7.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | CKMT2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q14.1 — chr5:81,201,341-81,301,565 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48997) · Entrez [100131067](https://www.ncbi.nlm.nih.gov/gene/100131067) · Ensembl [ENSG00000247572](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247572)

## Data

Gene col 14498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14498); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14498]; `tensor/DDL_lfc|DDL_z.npy` [14498]; `embed/gene_vectors.npy` [14498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14498 or target_col == 14498). Every well: [[CKMT2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CKMT2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
