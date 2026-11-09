---
symbol: "VEGFB"
type: "gene"
col: 10395
ensembl_id: "ENSG00000173511"
name: "vascular endothelial growth factor B"
location: "11q13.1"
module: 24
arm: "+"
pooled_cpm: 20.2
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# VEGFB

*vascular endothelial growth factor B* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.59× (z +4.0, q 0.029, up in 21 of 40 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.324× (z -10.4, q 2e-22, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNNM2]] (+0.72, fdr 7e-06), [[SIRT2]] (+0.71, fdr 7e-06), [[RAB40C]] (+0.70, fdr 7e-06); moves opposite to [[PSME3]] (-0.71, fdr 7e-06), [[CCT7]] (-0.70, fdr 7e-06), [[ABCF2]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.0 | 0.029 | 21/40 (C32, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.95× | +3.2 | 0.29 | 18/45 (NCI-H1573, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.40× | +3.2 | 0.29 | 19/47 (A-427, HS-578T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.324×** | -10.4 | 2e-22 | 42/47 (A-427, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -8.2 | 9e-14 | 35/47 (CFPAC-1, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.451×** | -7.3 | 4e-11 | 41/48 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -6.6 | 4e-09 | 33/47 (NCI-H1792, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.488×** | -6.6 | 5e-09 | 35/48 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.621×** | -6.2 | 6e-08 | 33/47 (SNU-423, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.525×** | -5.9 | 2e-07 | 39/48 (SNU-423, A-427, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.526×** | -5.7 | 9e-07 | 33/47 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.544×** | -5.6 | 1e-06 | 32/47 (LS 180, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.580×** | -5.0 | 3e-05 | 35/48 (SNU-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.564×** | -5.0 | 3e-05 | 34/48 (H4, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.712×** | -4.4 | 5e-04 | 21/48 (SW480, A-427, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.713×** | -4.4 | 5e-04 | 30/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.640×** | -4.1 | 0.002 | 31/47 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.647×** | -4.0 | 0.002 | 28/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.751×** | -3.7 | 0.007 | 25/48 (SW1417, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.421×** | -3.6 | 0.012 | 26/48 (SNU-423, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.429×** | -3.5 | 0.014 | 24/45 (BT-474, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.674×** | -3.4 | 0.018 | 24/47 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.680×** | -3.3 | 0.028 | 15/47 (NCI-H2030, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.703×** | -3.2 | 0.030 | 21/48 (BT-474, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.033 | 17/47 (SNU-423, SW48, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.696×** | -3.1 | 0.048 | 10/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 20.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0750× (z -9.6) |
| [[SNU-423 (line)]] | alt | 35.5 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[A-427 (line)]] | wt | 26.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0997× (z -14.0) |
| [[AN3 CA (line)]] | alt | 25.5 | 0 | 2 | — | [[Dihydroartemisinin (drug)]] 0.05 µM 0.0528× (z -10.2) |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 20.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -10.4) |
| [[PANC-1 (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.2) |
| [[H4 (line)]] | wt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -10.5) |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.4) |
| [[J82 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.240× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[LoVo (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 22.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.2) |
| [[A-172 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM2]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[SIRT2]] | +0.71 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ATP5MC2]] | +0.69 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.68 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[SAP30]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[NME3]] | +0.67 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MZT2B]] | +0.66 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | +0.65 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[CBFA2T2]] | +0.65 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SAT2]] | +0.65 | +0.51 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3]] | -0.71 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[CCT7]] | -0.70 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.65 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.63 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CCT5]] | -0.63 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[MOB1A]] | -0.62 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[DARS2]] | -0.62 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[LIN7C]] | -0.61 | -0.56 / -0.67 | both halves | 1e-05 |  |
| [[TOR1A]] | -0.61 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[SF3B4]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ELK4]] | -0.60 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-22.3, -31.3); signed map (-27.7, 11.4). **Vector** length 76.2, 19.5% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.2 | -7.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.1 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.0 | -6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -2.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | +0.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | vascular endothelial growth factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,234,584-64,239,264 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VEGFL; previously VRF |
| Gene groups (HGNC) | VEGF family |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 8 pathways, smallest: VEGF binds to VEGFR leading to receptor dimerization; VEGF ligand-receptor interactions; Signaling by VEGF |
| Matched by | ensembl_id |

**Function**, from UniProt [P49765](https://www.uniprot.org/uniprotkb/P49765) (Vascular endothelial growth factor B):

> Growth factor for endothelial cells. VEGF-B167 binds heparin and neuropilin-1 whereas the binding to neuropilin-1 of VEGF-B186 is regulated by proteolysis.

**Summary**, from NCBI Gene [7423](https://www.ncbi.nlm.nih.gov/gene/7423):

> This gene encodes a member of the PDGF (platelet-derived growth factor)/VEGF (vascular endothelial growth factor) family. The VEGF family members regulate the formation of blood vessels and are involved in endothelial cell physiology. This member is a ligand for VEGFR-1 (vascular endothelial growth factor receptor 1) and NRP-1 (neuropilin-1). Studies in mice showed that this gene was co-expressed with nuclear-encoded mitochondrial genes and the encoded protein specifically controlled …

**Accessions** — [HGNC:12681](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12681) · Entrez [7423](https://www.ncbi.nlm.nih.gov/gene/7423) · UniProt [P49765](https://www.uniprot.org/uniprotkb/P49765) · Ensembl [ENSG00000173511](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173511)

## Data

Gene col 10395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10395); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10395]; `tensor/DDL_lfc|DDL_z.npy` [10395]; `embed/gene_vectors.npy` [10395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10395 or target_col == 10395). Every well: [[VEGFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VEGFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
