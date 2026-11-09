---
symbol: "ABCD4"
type: "gene"
col: 4100
ensembl_id: "ENSG00000119688"
name: "ATP binding cassette subfamily D member 4"
location: "14q24.3"
module: 30
arm: "+"
pooled_cpm: 33.95
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ABCD4

*ATP binding cassette subfamily D member 4* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.39× (z +7.9, q 1e-12, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.48× (z +6.7, q 7e-09, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.546× (z -9.9, q 4e-20, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMBR1L]] (+0.77, fdr 7e-06), [[CRYZL1]] (+0.74, fdr 7e-06), [[KLHL7]] (+0.70, fdr 7e-06); moves opposite to [[TMEM185B]] (-0.65, fdr 1e-05), [[PURB]] (-0.64, fdr 2e-05), [[EIF4G1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.39×** | +7.9 | 1e-12 | 38/48 (RKO, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +6.7 | 7e-09 | 31/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +6.1 | 2e-07 | 29/48 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.40×** | +5.6 | 3e-06 | 30/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +3.9 | 0.012 | 15/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.050 | 13/47 (NCI-H2347, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.091 | 11/48 (PANC-1, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.12 | 18/48 (A498, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.546×** | -9.9 | 4e-20 | 35/48 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.677×** | -9.3 | 3e-18 | 32/47 (HCT15, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.577×** | -9.3 | 3e-18 | 27/44 (Panc 03.27, NCI-H2030, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.575×** | -8.6 | 1e-15 | 27/42 (MIA PaCa-2, HCT15, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -8.4 | 6e-15 | 35/48 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -8.0 | 2e-13 | 11/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -6.6 | 4e-09 | 31/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.669×** | -6.5 | 5e-09 | 20/38 (NCI-H1792, KATO III, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.556×** | -5.2 | 1e-05 | 30/49 (NCI-H1573, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -5.1 | 2e-05 | 26/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.734×** | -5.0 | 2e-05 | 29/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.765×** | -4.5 | 3e-04 | 25/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.774×** | -4.3 | 6e-04 | 24/47 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.9 | 0.005 | 20/47 (COLO 205, BT-474, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.820×** | -3.4 | 0.029 | 16/48 (SHP-77, SW 900, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.870× | -3.3 | 0.031 | 14/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.697×** | -3.2 | 0.047 | 10/47 (MIA PaCa-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.069 | 7/48 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 47.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -11.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 53.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.348× (z -9.1) |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.252× (z -8.8) |
| [[HCT15 (line)]] | alt | 68.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -14.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LoVo (line)]] | wt | 30.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.35× (z +10.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 41.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.340× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 50.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 20.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 30.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HS-578T (line)]] | alt | 21.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 38.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 2 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0643× (z -9.1) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Trimetrexate (drug)]] 0.5 µM 0.0646× (z -9.1) |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.105× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.204× (z -9.5) |
| [[H4 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0992× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~62% of this change |
| [[HOP62 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.379× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~78% of this change |
| [[KATO III (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -11.7) |
| [[LS 180 (line)]] | wt | 37.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 26.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -11.8) |
| [[RKO (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -9.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -11.4) |
| [[SNU-423 (line)]] | alt | 38.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -10.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 43.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0615× (z -8.8) |
| [[SW480 (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1L]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.74 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[UBE4B]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[CC2D1A]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RUFY2]] | +0.68 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.68 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[MGST3]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[DPY30]] | +0.66 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.66 | +0.69 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM185B]] | -0.65 | -0.74 / -0.56 | both halves | 1e-05 |  |
| [[PURB]] | -0.64 | -0.77 / -0.47 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.64 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[CYREN]] | -0.62 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[TRIM44]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[TASOR]] | -0.61 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[FAT1]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[THOC6]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[SKIL]] | -0.59 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[LEKR1]] | -0.59 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[OMA1]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers ABCD4's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.6, -12.2); signed map (-32.8, -3.8). **Vector** length 109, 26.7% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.8 | +7.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.0 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.8 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +3.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.3 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.1 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -3.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.7 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily D member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,285,269-74,303,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMP69, P70R, EST352188; previously PXMP1L |
| Gene groups (HGNC) | ATP binding cassette subfamily D |
| Reactome | 10 pathways, smallest: Uptake of dietary cobalamins into enterocytes; Transport of RCbl within the body; Defects in cobalamin (B12) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14678](https://www.uniprot.org/uniprotkb/O14678) (Lysosomal cobalamin transporter ABCD4):

> Lysosomal membrane protein that transports cobalamin (Vitamin B12) from the lysosomal lumen to the cytosol in an ATP-dependent manner. Targeted by LMBRD1 lysosomal chaperone from the endoplasmic reticulum to the lysosomal membrane. Then forms a complex with lysosomal chaperone LMBRD1 and cytosolic MMACHC to transport cobalamin across the lysosomal membrane.

**Summary**, from NCBI Gene [5826](https://www.ncbi.nlm.nih.gov/gene/5826):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ALD subfamily, which is involved in peroxisomal import of fatty acids and/or fatty acyl-CoAs in the organelle. All known peroxisomal ABC transporters are half transporters …

**Accessions** — [HGNC:68](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:68) · Entrez [5826](https://www.ncbi.nlm.nih.gov/gene/5826) · UniProt [O14678](https://www.uniprot.org/uniprotkb/O14678) · Ensembl [ENSG00000119688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119688)

## Data

Gene col 4100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4100); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4100]; `tensor/DDL_lfc|DDL_z.npy` [4100]; `embed/gene_vectors.npy` [4100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4100 or target_col == 4100). Every well: [[ABCD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
