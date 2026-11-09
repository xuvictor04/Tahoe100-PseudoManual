---
symbol: "SPHK2"
type: "gene"
col: 721
ensembl_id: "ENSG00000063176"
name: "sphingosine kinase 2"
location: "19q13.33"
module: 36
arm: "+"
pooled_cpm: 9.15
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# SPHK2

*sphingosine kinase 2* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.86× (z +11.6, q 2e-28, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.583× (z -14.3, q 9e-44, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.706× (z -6.5, q 1e-08, down in 15 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAFIP]] (+0.59, fdr 2e-05), [[POP1]] (+0.59, fdr 2e-05), [[JRK]] (+0.58, fdr 1e-05); moves opposite to [[TXNDC16]] (-0.51, fdr 2e-05), [[TMEM14C]] (-0.50, fdr 3e-05), [[CCDC148]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +11.6 | 2e-28 | 32/45 (SW480, A498, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.079 | 1/44 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +3.5 | 0.079 | 3/47 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.21× | +3.3 | 0.13 | 6/42 (SK-MEL-2, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.19× | +3.3 | 0.13 | 1/47 (A549) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +3.1 | 0.17 | 5/43 (SW1417, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.583×** | -14.3 | 9e-44 | 37/47 (LS 180, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -7.1 | 4e-10 | 19/38 (HCT15, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.706×** | -6.5 | 1e-08 | 15/43 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.796×** | -6.1 | 2e-07 | 19/44 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -6.0 | 2e-07 | 20/44 (SW1417, J82, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -5.6 | 2e-06 | 13/47 (SW 1271, C32, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -5.4 | 4e-06 | 17/43 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.755×** | -5.3 | 9e-06 | 17/47 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -4.6 | 3e-04 | 13/47 (HS-578T, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.797×** | -4.1 | 0.002 | 9/18 (HOP62, A498, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.808×** | -4.0 | 0.003 | 17/43 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.821×** | -3.6 | 0.018 | 15/46 (SNU-1, A-427, …) | rises with dose | composition shift |
| [[Decitabine (drug)]] 0.05 µM |  | **0.823×** | -3.4 | 0.032 | 8/43 (BT-474, H4, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | 0.837× | -3.3 | 0.034 | 6/44 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.07 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.126× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.109× (z -8.8) |
| [[A-427 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -10.0) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0534× (z -15.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 5.36 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 7.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 5.46 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0989× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -9.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SHP-77 (line)]] | alt | 7.85 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0951× (z -9.1) |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0746× (z -10.1) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A498 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFIP]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[POP1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[JRK]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[EARS2]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[GTF3C3]] | +0.57 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[DNAJC17]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[DFFA]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ZNF169]] | +0.54 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[NUDC]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[SLC25A17]] | +0.54 | +0.25 / +0.58 | both halves | 4e-04 |  |
| [[C7orf50]] | +0.54 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[TMEM161A]] | +0.54 | +0.55 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC16]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TMEM14C]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[CCDC148]] | -0.50 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[HIVEP2]] | -0.49 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[EEA1]] | -0.49 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ACTR1B]] | -0.49 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[NBPF26]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[TAPT1]] | -0.49 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[APLF]] | -0.49 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[FBXO48]] | -0.47 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[UACA]] | -0.47 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[LNX2]] | -0.47 | -0.43 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SPHK2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF512]] | C | ZNF512 activity lowers SPHK2's level | lines that do not express ZNF512 (3) vs lines expressing it (47) | 1.95× higher at baseline in the lines without ZNF512 | 0.009 | ⚠ few lines (3 vs 47); across organs; co-occurs with MSH6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-29.4, -7.4); signed map (-15.2, -20.1). **Vector** length 52.9, 6.19% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.7 | +11.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.4 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.2 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.8 | -14.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -3.0 | -3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -4.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.1 | -2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.1 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | sphingosine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,619,291-48,630,717 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sphingosine kinase family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRA0](https://www.uniprot.org/uniprotkb/Q9NRA0) (Sphingosine kinase 2):

> Catalyzes the phosphorylation of sphingosine to form sphingosine-1-phosphate (SPP), a lipid mediator with both intra- and extracellular functions. Also acts on D-erythro-dihydrosphingosine, D-erythro-sphingosine and L-threo-dihydrosphingosine. Binds phosphoinositides. In contrast to prosurvival SPHK1, has a positive effect on intracellular ceramide levels, inhibits cells growth and enhances apoptosis. In mitochondria, is important for cytochrome-c oxidase assembly and mitochondrial respiration. …

**Summary**, from NCBI Gene [56848](https://www.ncbi.nlm.nih.gov/gene/56848):

> This gene encodes one of two sphingosine kinase isozymes that catalyze the phosphorylation of sphingosine into sphingosine 1-phosphate. Sphingosine 1-phosphate mediates many cellular processes including migration, proliferation and apoptosis, and also plays a role in several types of cancer by promoting angiogenesis and tumorigenesis. The encoded protein may play a role in breast cancer proliferation and chemoresistance. Alternatively spliced transcript variants encoding multiple isoforms have …

**Accessions** — [HGNC:18859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18859) · Entrez [56848](https://www.ncbi.nlm.nih.gov/gene/56848) · UniProt [Q9NRA0](https://www.uniprot.org/uniprotkb/Q9NRA0) · Ensembl [ENSG00000063176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063176)

## Data

Gene col 721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 721); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 721]; `tensor/DDL_lfc|DDL_z.npy` [721]; `embed/gene_vectors.npy` [721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 721 or target_col == 721). Every well: [[SPHK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPHK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
