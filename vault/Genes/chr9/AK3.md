---
symbol: "AK3"
type: "gene"
col: 7225
ensembl_id: "ENSG00000147853"
name: "adenylate kinase 3"
location: "9p24.1"
module: 29
arm: "+"
pooled_cpm: 48.72
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# AK3

*adenylate kinase 3* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.05× (z +20.5, q 0e+00, up in 38 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.35× (z +8.6, q 9e-16, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.706× (z -9.9, q 2e-20, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP46]] (+0.64, fdr 9e-06), [[CHPT1]] (+0.63, fdr 1e-05), [[PAXBP1]] (+0.59, fdr 2e-05); moves opposite to [[ARID3B]] (-0.53, fdr 3e-05), [[FAM131A]] (-0.52, fdr 1e-04), [[STX1A]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7225.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +20.5 | 0e+00 | 38/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +17.3 | 0e+00 | 34/39 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +13.1 | 8e-37 | 32/44 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +8.6 | 9e-16 | 27/47 (A498, A-172, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +8.6 | 1e-15 | 21/48 (HT-29, J82, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +8.5 | 2e-15 | 27/48 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +6.8 | 7e-10 | 23/46 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +6.1 | 6e-08 | 23/47 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.20×** | +5.3 | 8e-06 | 21/47 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +5.1 | 2e-05 | 19/46 (A549, HOP62, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +5.0 | 2e-05 | 17/47 (LOX-IMVI, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +4.8 | 7e-05 | 10/48 (A498, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.18× | +4.6 | 2e-04 | 15/48 (A549, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +4.5 | 3e-04 | 14/46 (KATO III, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +4.4 | 3e-04 | 14/47 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +4.3 | 6e-04 | 8/48 (AsPC-1, SW1417, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.17× | +4.1 | 0.002 | 15/46 (HS-578T, A-172, …) | all doses, flat |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.10× | +3.7 | 0.006 | 9/48 (A549, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.6 | 0.008 | 8/49 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.5 | 0.009 | 5/48 (HepG2/C3A, LOX-IMVI, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.11× | +3.5 | 0.010 | 5/48 (A549, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.13× | +3.4 | 0.015 | 11/48 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 1.12× | +3.3 | 0.021 | 5/48 (LOX-IMVI, NCI-H2030, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.023 | 11/47 (A-172, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.038 | 5/48 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7225.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.706×** | -9.9 | 2e-20 | 27/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.744×** | -8.4 | 8e-15 | 26/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -8.2 | 3e-14 | 1/49 (RPMI-7951) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.827×** | -5.4 | 8e-06 | 19/48 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.860× | -4.1 | 0.004 | 19/48 (COLO 205, AN3 CA, …) | rises with dose | composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.785×** | -3.6 | 0.028 | 9/48 (SW480, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.920× | -3.4 | 0.061 | 5/48 (HS-578T, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.890× | -3.3 | 0.062 | 13/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Gallic acid (drug)]] 5 µM |  | 0.926× | -3.1 | 0.12 | 2/48 (NCI-H1792, H4) | rises with dose |  |
| [[Naproxen (drug)]] 0.05 µM |  | 0.891× | -3.1 | 0.13 | 9/47 (CHP-212, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7225. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 116 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.303× (z -17.0) |
| [[SW480 (line)]] | alt | 91.8 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.361× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 38.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -12.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.425× (z -10.4) |
| [[RKO (line)]] | wt | 102 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -13.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.468× (z -9.9) |
| [[COLO 205 (line)]] | alt | 53.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[HOP62 (line)]] | alt | 35.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 30.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -10.4) |
| [[SW1417 (line)]] | alt | 70.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +10.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -12.6) |
| [[A498 (line)]] | wt | 57.6 | 1 | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.16× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -10.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[CFPAC-1 (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 41.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.31× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 59.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 59.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -10.8) |
| [[KATO III (line)]] | alt | 82.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.440× (z -9.8) |
| [[LoVo (line)]] | wt | 108 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -13.4) |
| [[PANC-1 (line)]] | alt | 19.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 38.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[A-427 (line)]] | wt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.51× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 55.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -10.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[CHP-212 (line)]] | wt | 67.9 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.153× (z -9.9) |
| [[HCT15 (line)]] | alt | 62.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +8.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +10.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[LOX-IMVI (line)]] | wt | 46.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 60.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 56.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.344× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7225), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP46]] | +0.64 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[CHPT1]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PAXBP1]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[VSIG10]] | +0.58 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[PON2]] | +0.58 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[PHACTR2]] | +0.57 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[DERA]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PLBD1]] | +0.55 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[SETD7]] | +0.54 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[RHOBTB3]] | +0.54 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CIAO2A]] | +0.54 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PLXNB1]] | +0.54 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3B]] | -0.53 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[FAM131A]] | -0.52 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[STX1A]] | -0.51 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[NAGK]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[PDLIM7]] | -0.51 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SPATA2L]] | -0.51 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[SAP30BP]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[ATG101]] | -0.50 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[PTGS1]] | -0.50 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[RASA3]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[GNAI3]] | -0.49 | -0.49 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[ARL4C]] | -0.49 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[RIN1]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises AK3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PITX1]] | B | PITX1 activity raises AK3's level | lines that do not express PITX1 (10) vs lines expressing it (40) | 1.62× lower at baseline in the lines without PITX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: MNX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-12.4, 14.7); signed map (-19.5, -28.6). **Vector** length 101, 22.7% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +20.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +5.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +13.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | +5.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.6 | +2.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -9.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | -2.4 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.4 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:4,709,556-4,742,043 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AKL3L1; previously AK6, AK3L1 |
| Gene groups (HGNC) | Adenylate kinases |
| Hallmark sets | DNA_REPAIR, GLYCOLYSIS |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIJ7](https://www.uniprot.org/uniprotkb/Q9UIJ7) (GTP:AMP phosphotransferase AK3, mitochondrial):

> Mitochondrial adenylate kinase with a specific GTP:AMP phosphotransferase activity. Could also use ITP as phosphate donor. Its physiological function is to recycle GTP into GDP which is necessary for the TCA cycle in the mitochondrial matrix (Probable).

**Summary**, from NCBI Gene [50808](https://www.ncbi.nlm.nih.gov/gene/50808):

> The protein encoded by this gene is a GTP:ATP phosphotransferase that is found in the mitochondrial matrix. Several transcript variants encoding a few different isoforms have been found for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:17376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17376) · Entrez [50808](https://www.ncbi.nlm.nih.gov/gene/50808) · UniProt [Q9UIJ7](https://www.uniprot.org/uniprotkb/Q9UIJ7) · Ensembl [ENSG00000147853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147853)

## Data

Gene col 7225: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7225); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7225, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7225]; `tensor/DDL_lfc|DDL_z.npy` [7225]; `embed/gene_vectors.npy` [7225]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7225 or target_col == 7225). Every well: [[AK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
