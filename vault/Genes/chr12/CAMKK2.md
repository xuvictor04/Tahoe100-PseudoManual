---
symbol: "CAMKK2"
type: "gene"
col: 3182
ensembl_id: "ENSG00000110931"
name: "calcium/calmodulin dependent protein kinase kinase 2"
location: "12q24.31"
module: 18
arm: "+"
pooled_cpm: 29.09
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CAMKK2

*calcium/calmodulin dependent protein kinase kinase 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Neratinib (drug)]] 5 µM: 1.19× (z +4.1, q 0.008, up in 9 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 2.44×; ⚠ cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.504× (z -22.1, q 0e+00, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.469× (z -16.6, q 0e+00, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VKORC1L1]] (+0.66, fdr 7e-06), [[ZDHHC8]] (+0.61, fdr 2e-05), [[NTAQ1]] (+0.61, fdr 1e-05); moves opposite to [[ATP7A]] (-0.58, fdr 1e-05), [[MBD5]] (-0.56, fdr 2e-05), [[KDM5A]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADCY3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MPP3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3182.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-423 2.44×; ⚠ cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (drug)]] 5 µM |  | 1.19× | +4.1 | 0.008 | 9/48 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.20×** | +4.0 | 0.008 | 15/47 (NCI-H1792, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.0 | 0.008 | 16/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.0 | 0.008 | 13/48 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.9 | 0.010 | 12/47 (HOP62, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.023 | 4/48 (J82, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.504×** | -22.1 | 0e+00 | 33/47 (LoVo, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -16.6 | 0e+00 | 35/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.286×** | -14.9 | 0e+00 | 46/48 (LoVo, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.589×** | -12.1 | 2e-31 | 35/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -10.9 | 1e-25 | 28/47 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.489×** | -8.5 | 1e-15 | 30/47 (LS 180, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -8.0 | 7e-14 | 26/48 (A549, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.716×** | -7.4 | 1e-11 | 28/48 (HT-29, NCI-H23, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.730×** | -7.2 | 5e-11 | 30/48 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -6.1 | 7e-08 | 27/48 (LoVo, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.774×** | -5.8 | 3e-07 | 24/48 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -5.8 | 4e-07 | 14/48 (A-172, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.779×** | -5.7 | 6e-07 | 25/48 (A498, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.844× | -5.4 | 2e-06 | 22/47 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -5.4 | 3e-06 | 24/48 (HOP62, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.787×** | -5.1 | 1e-05 | 22/48 (HS-578T, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.837× | -4.0 | 0.001 | 21/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.844× | -3.6 | 0.009 | 15/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.014 | 8/48 (SHP-77, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 30.7 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.250× (z -13.9) |
| [[A549 (line)]] | wt | 39.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -18.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.344× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 41.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.331× (z -12.3) |
| [[A-172 (line)]] | wt | 40.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -24.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.326× (z -16.4) |
| [[A-427 (line)]] | wt | 34.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -19.4) |
| [[SW480 (line)]] | alt | 23.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.162× (z -9.1) |
| [[A498 (line)]] | wt | 47.7 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.205× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 34.4 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -13.5) ⚠ cell-cycle shift, explains ~18% of this change |
| [[LOX-IMVI (line)]] | wt | 24.5 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -13.7) |
| [[SW1417 (line)]] | alt | 23.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.294× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.299× (z -11.3) |
| [[KATO III (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[LS 180 (line)]] | wt | 25.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.209× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.336× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.332× (z -8.7) |
| [[RKO (line)]] | wt | 30.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -9.7) |
| [[SW48 (line)]] | wt | 41.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.227× (z -8.8) |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 25.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.273× (z -17.3) |
| [[HS-578T (line)]] | alt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.369× (z -9.0) |
| [[J82 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -14.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.119× (z -9.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.61 | +0.49 / +0.70 | both halves | 2e-05 |  |
| [[NTAQ1]] | +0.61 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PEMT]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ZNF767P-1]] | +0.58 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[PACS2]] | +0.57 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ZMYND19]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[ZNF598]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[TELO2]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PRELID3A]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[NT5M]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP7A]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[MBD5]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[KDM5A]] | -0.56 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[TTC30A]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TET2]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ZNF429]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PHF3]] | -0.51 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CSNK1A1]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[EID1]] | -0.50 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SF3B1]] | -0.50 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[UBA6-DT]] | -0.50 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.49 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises CAMKK2's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without ADCY3 | 0.032 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP3]] | C | CAMKK2's natural level strengthens MPP3's drug response | CAMKK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.25; direction not clear | 0.093 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.6, -28.2); signed map (-44.0, -16.0). **Vector** length 84.6, 17.3% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +0.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +1.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +0.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.9 | -14.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -3.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,237,675-121,298,308 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAMKK, KIAA0787, CAMKKB, MGC15254 |
| Gene groups (HGNC) | Calcium/calmodulin dependent protein kinase kinase family |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 20 pathways, smallest: Activation of RAC1 downstream of NMDARs; CREB1 phosphorylation through the activation of CaMKII/CaMKK/CaMKIV cascasde; CaMK IV-mediated phosphorylation of CREB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RR4](https://www.uniprot.org/uniprotkb/Q96RR4) (Calcium/calmodulin-dependent protein kinase kinase 2):

> Calcium/calmodulin-dependent protein kinase belonging to a proposed calcium-triggered signaling cascade involved in a number of cellular processes. Isoform 1, isoform 2 and isoform 3 phosphorylate CAMK1 and CAMK4. Isoform 3 phosphorylates CAMK1D. Isoform 4, isoform 5 and isoform 6 lacking part of the calmodulin-binding domain are inactive. Efficiently phosphorylates 5'-AMP-activated protein kinase (AMPK) trimer, including that consisting of PRKAA1, PRKAB1 and PRKAG1. This phosphorylation is …

**Summary**, from NCBI Gene [10645](https://www.ncbi.nlm.nih.gov/gene/10645):

> The product of this gene belongs to the Serine/Threonine protein kinase family, and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. The major isoform of this gene plays a role in the calcium/calmodulin-dependent (CaM) kinase cascade by phosphorylating the downstream kinases CaMK1 and CaMK4. Protein products of this gene also phosphorylate AMP-activated protein kinase (AMPK). This gene has its strongest expression in the brain and influences signalling cascades involved with …

**Accessions** — [HGNC:1470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1470) · Entrez [10645](https://www.ncbi.nlm.nih.gov/gene/10645) · UniProt [Q96RR4](https://www.uniprot.org/uniprotkb/Q96RR4) · Ensembl [ENSG00000110931](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110931)

## Data

Gene col 3182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3182); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3182]; `tensor/DDL_lfc|DDL_z.npy` [3182]; `embed/gene_vectors.npy` [3182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3182 or target_col == 3182). Every well: [[CAMKK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMKK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
