---
symbol: "TMEM94"
type: "gene"
col: 10859
ensembl_id: "ENSG00000177728"
name: "transmembrane protein 94"
location: "17q25.1"
module: 178
arm: "+"
pooled_cpm: 21.5
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# TMEM94

*transmembrane protein 94* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.22× (z +4.5, q 0.004, up in 19 of 48 measured lines) ⚠ cell-cycle shift, explains ~92% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.28× (z +4.0, q 0.014, up in 12 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.391× (z -14.9, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.476× (z -11.8, q 4e-30, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED24]] (+0.71, fdr 7e-06), [[METTL22]] (+0.66, fdr 7e-06), [[ZNF224]] (+0.63, fdr 1e-05); moves opposite to [[ATP8B5P-1]] (-0.65, fdr 7e-06), [[TNFRSF12A]] (-0.59, fdr 1e-05), [[PITPNB]] (-0.58, fdr 3e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10859.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.22×** | +4.5 | 0.004 | 19/48 (RPMI-7951, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.28×** | +4.3 | 0.006 | 17/48 (A-427, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.014 | 12/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.014 | 12/47 (SW480, A-427, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.7 | 0.021 | 12/48 (RKO, hTERT-HPNE, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.17× | +3.5 | 0.037 | 9/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | 1.15× | +3.3 | 0.092 | 10/48 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.096 | 9/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.096 | 10/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.21×** | +3.1 | 0.096 | 12/48 (A-427, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10859.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.391×** | -14.9 | 0e+00 | 46/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.413×** | -14.1 | 2e-42 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.537×** | -14.0 | 3e-42 | 35/47 (NCI-H460, LS 180, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.468×** | -12.1 | 2e-31 | 43/47 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.476×** | -11.8 | 4e-30 | 38/47 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.549×** | -9.2 | 4e-18 | 34/48 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.588×** | -8.4 | 3e-15 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.610×** | -7.5 | 3e-12 | 29/47 (HOP62, NCI-H1792, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -6.4 | 8e-09 | 24/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.668×** | -6.4 | 9e-09 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.676×** | -6.2 | 3e-08 | 26/46 (SNU-1, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.688×** | -5.9 | 1e-07 | 27/47 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.694×** | -5.8 | 3e-07 | 30/47 (C32, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -5.4 | 2e-06 | 26/48 (Hs 766T, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -4.9 | 4e-05 | 5/48 (RKO, LS 180, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.794×** | -3.5 | 0.016 | 13/48 (AN3 CA, NCI-H460, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.671×** | -3.3 | 0.027 | 12/46 (LOX-IMVI, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -3.0 | 0.059 | 14/48 (CFPAC-1, C32, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.827×** | -3.0 | 0.064 | 10/48 (A498, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10859. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.7 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -16.3) |
| [[HOP62 (line)]] | alt | 30.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -9.1) |
| [[LoVo (line)]] | wt | 24.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H1792 (line)]] | alt | 30.0 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -10.1) |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 20.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -10.9) |
| [[A-427 (line)]] | wt | 24.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 36.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.175× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -10.5) |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 27.6 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HCT15 (line)]] | alt | 31.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0603× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.343× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -12.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0916× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -9.3) |
| [[SW48 (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0941× (z -9.1) |
| [[A498 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10859), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED24]] | +0.71 | +0.61 / +0.72 | both halves | 7e-06 | same gene group |
| [[METTL22]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZNF224]] | +0.63 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[CIAO2A]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[USP30]] | +0.62 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[DRAM2]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[TIAL1]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[DDRGK1]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[LYSMD1]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[PMS2]] | +0.59 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[SMPDL3A]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[SGSM2]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP8B5P-1]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | -0.59 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[PITPNB]] | -0.58 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[BACH1]] | -0.58 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MYL12A]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[CCDC57]] | -0.56 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ATG7]] | -0.54 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RABGAP1L]] | -0.54 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[AREG]] | -0.54 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[BLZF2P]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SLC4A7]] | -0.53 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.1, -18.1); signed map (-29.5, -19.3). **Vector** length 84.4, 17.7% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +5.8 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -11.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.2 | -14.9 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -2.1 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.1 | -14.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -3.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.0 | -2.2 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 94 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,441,159-75,500,452 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ERMA; previously KIAA0195 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12767](https://www.uniprot.org/uniprotkb/Q12767) (Transmembrane protein 94):

> Could function in the uptake of Mg(2+) from the cytosol into the endoplasmic reticulum and regulate intracellular Mg(2+) homeostasis.

**Summary**, from NCBI Gene [9772](https://www.ncbi.nlm.nih.gov/gene/9772):

> Enables P-type magnesium transporter activity. Involved in magnesium ion transport from cytosol to endoplasmic reticulum. Located in nucleoplasm. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28983) · Entrez [9772](https://www.ncbi.nlm.nih.gov/gene/9772) · UniProt [Q12767](https://www.uniprot.org/uniprotkb/Q12767) · Ensembl [ENSG00000177728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177728)

## Data

Gene col 10859: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10859); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10859, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10859]; `tensor/DDL_lfc|DDL_z.npy` [10859]; `embed/gene_vectors.npy` [10859]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10859 or target_col == 10859). Every well: [[TMEM94 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM94.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
