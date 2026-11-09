---
symbol: "UBE2Q2P1"
type: "gene"
col: 12093
ensembl_id: "ENSG00000189136"
name: "UBE2Q2 pseudogene 1"
location: "15q25.2"
module: 221
arm: "+"
pooled_cpm: 21.77
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# UBE2Q2P1

*UBE2Q2 pseudogene 1* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.05 µM: 1.42× (z +4.5, q 0.003, up in 14 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -15.6, q 0e+00, down in 34 of 45 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 0.478× (z -5.6, q 2e-06, down in 22 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2Q2P1-1]] (+0.72, fdr 7e-06, ⚠ same locus), [[RUFY2]] (+0.64, fdr 1e-05), [[UBE2Q2]] (+0.60, fdr 7e-06), [[IAH1]] (+0.60, fdr 1e-05); moves opposite to [[NUP98]] (-0.53, fdr 9e-05), [[PPP1R10]] (-0.49, fdr 5e-05), [[HNRNPF]] (-0.48, fdr 2e-05).
> It is in [[Module 221]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ATP6V0D2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.42×** | +4.5 | 0.003 | 14/46 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +4.4 | 0.003 | 18/46 (LoVo, A498, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.34×** | +4.3 | 0.003 | 22/46 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.34×** | +4.2 | 0.005 | 18/45 (RPMI-7951, hTERT-HPNE, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.005 | 16/45 (CFPAC-1, HOP62, …) | two highest doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.36×** | +3.9 | 0.008 | 10/46 (SW480, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.011 | 8/46 (A549, NCI-H2347, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.31×** | +3.7 | 0.015 | 17/46 (A498, H4, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.015 | 16/45 (RPMI-7951, H4, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.020 | 15/43 (A549, RKO, …) | two highest doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.030 | 10/45 (C-33 A, BT-474, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.030 | 11/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.3 | 0.040 | 18/46 (LoVo, Panc 03.27, …) | two highest doses | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.040 | 10/46 (CFPAC-1, LOX-IMVI, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.093 | 6/46 (BT-474, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.438×** | -15.6 | 0e+00 | 34/45 (hTERT-HPNE, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.450×** | -11.6 | 8e-29 | 35/46 (A549, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.519×** | -9.6 | 2e-19 | 35/46 (A549, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.561×** | -8.1 | 7e-14 | 27/46 (A-172, NCI-H1792, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.675×** | -5.7 | 1e-06 | 24/46 (A-172, CFPAC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.478×** | -5.6 | 2e-06 | 22/43 (MIA PaCa-2, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.496×** | -5.3 | 7e-06 | 25/46 (hTERT-HPNE, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -5.3 | 7e-06 | 20/44 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.710×** | -5.0 | 4e-05 | 22/46 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~80% of this change | **0.724×** | -4.5 | 3e-04 | 19/43 (C32, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.786×** | -4.5 | 3e-04 | 22/45 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.733×** | -4.4 | 6e-04 | 19/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.799×** | -4.2 | 0.001 | 21/46 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.625×** | -3.6 | 0.014 | 19/45 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **0.630×** | -3.5 | 0.015 | 15/41 (SW 900, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.778×** | -3.5 | 0.015 | 13/45 (NCI-H2347, C32, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.649×** | -3.3 | 0.032 | 13/43 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.774×** | -3.2 | 0.038 | 12/46 (SW 1088, Hs 766T, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 0.854× | -3.0 | 0.066 | 8/46 (NCI-H1573, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.672×** | -3.0 | 0.066 | 10/45 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.853× | -3.0 | 0.081 | 17/46 (NCI-H2347, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -15.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -10.7) |
| [[A549 (line)]] | wt | 60.2 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -12.0) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 40.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -14.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C32 (line)]] | wt | 19.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -11.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 46.9 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HOP62 (line)]] | alt | 22.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -11.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -16.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[HI-TOPK-032 (drug)]] 5 µM 0.0348× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 37.6 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.335× (z -9.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[H4 (line)]] | wt | 26.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -15.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -18.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 28.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A498 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -10.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RKO (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0817× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2P1-1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RUFY2]] | +0.64 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[UBE2Q2]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[IAH1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[STPG1]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[SVIL-AS1-1]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[KATNAL1]] | +0.56 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FAM219B]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[NDFIP1]] | +0.56 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[APBB1]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[BVES]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ECHDC3]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CDS2]] | +0.55 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP98]] | -0.53 | -0.37 / -0.58 | both halves | 9e-05 |  |
| [[PPP1R10]] | -0.49 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[HNRNPF]] | -0.48 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[SEMA4A]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[SLC12A2]] | -0.47 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[HES1]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SLC30A7]] | -0.47 | -0.41 / -0.40 | both halves | 4e-05 |  |
| [[TNFRSF21]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[SYS1-DBNDD2]] | -0.47 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[NR4A1]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[NR4A3]] | -0.46 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[CFAP44]] | -0.46 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0D2]] | B | ATP6V0D2 activity raises UBE2Q2P1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.54× lower at baseline in the lines without ATP6V0D2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[TBKBP1]] | B | TBKBP1 activity raises UBE2Q2P1's level | lines that do not express TBKBP1 (5) vs lines expressing it (45) | 3.26× lower at baseline in the lines without TBKBP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CSRP2, PHC1, DNAJC18; its own permutation p |
| [[MYO5A]] | B | MYO5A activity raises UBE2Q2P1's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without MYO5A | 0.065 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2 |
| [[KATNAL1]] | B | KATNAL1 activity raises UBE2Q2P1's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.21× lower at baseline in the lines without KATNAL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[FSD1L]] | C | FSD1L activity raises UBE2Q2P1's level | lines that do not express FSD1L (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without FSD1L | 0.016 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[SYS1-DBNDD2]] | C | SYS1-DBNDD2's natural level weakens UBE2Q2P1's drug response | SYS1-DBNDD2's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.70, reverse +0.16; direction not clear | 0.021 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NT5C3B]] | C | NT5C3B's natural level strengthens UBE2Q2P1's drug response | NT5C3B's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.11; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[KIF5A]] | C | KIF5A activity raises UBE2Q2P1's level | lines that do not express KIF5A (4) vs lines expressing it (46) | 2.16× lower at baseline in the lines without KIF5A | 0.098 | ⚠ few lines (4 vs 46); across organs; also absent: ZDHHC1, ALPK3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.5, -2.8); signed map (-32.2, -4.6). **Vector** length 94.7, 22.2% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.4 | +4.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +2.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -3.9 | -5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.3 | -15.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.9 | -8.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | UBE2Q2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 15q25.2 — chr15:84,526,781-84,570,700 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | FLJ43276; previously UBE2QP1 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:37439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37439) · Entrez [388165](https://www.ncbi.nlm.nih.gov/gene/388165) · Ensembl [ENSG00000189136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189136)

## Data

Gene col 12093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12093); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12093]; `tensor/DDL_lfc|DDL_z.npy` [12093]; `embed/gene_vectors.npy` [12093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12093 or target_col == 12093). Every well: [[UBE2Q2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Q2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
