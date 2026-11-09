---
symbol: "GCAT"
type: "gene"
col: 1872
ensembl_id: "ENSG00000100116"
name: "glycine C-acetyltransferase"
location: "22q13.1"
module: 4
arm: "-"
pooled_cpm: 10.2
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GCAT

*glycine C-acetyltransferase* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +15.7, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.673× (z -4.5, q 0.004, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MINDY2]] (+0.67, fdr 1e-05), [[ING1]] (+0.66, fdr 7e-06), [[DDX50]] (+0.62, fdr 7e-06); moves opposite to [[LARP4]] (-0.65, fdr 1e-05), [[ARPP19]] (-0.64, fdr 7e-06), [[NAA50]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +15.7 | 0e+00 | 37/44 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.27×** | +13.5 | 4e-39 | 42/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.69×** | +11.3 | 3e-27 | 40/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.54×** | +10.6 | 3e-24 | 37/45 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.9 | 9e-17 | 30/39 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.23×** | +8.8 | 2e-16 | 32/43 (SW480, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +6.4 | 1e-08 | 23/45 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.00×** | +4.1 | 0.002 | 9/39 (AsPC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.38×** | +3.7 | 0.014 | 19/43 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +3.2 | 0.065 | 10/46 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.33×** | +3.1 | 0.088 | 2/18 (NCI-H2030, MIA PaCa-2) | top dose only | composition shift |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.089 | 6/46 (MIA PaCa-2, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -4.5 | 0.004 | 20/45 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.769×** | -4.2 | 0.009 | 15/46 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.514×** | -4.0 | 0.014 | 16/43 (NCI-H23, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.709×** | -3.7 | 0.031 | 16/43 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.549×** | -3.6 | 0.041 | 13/40 (KATO III, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.731×** | -3.4 | 0.074 | 10/46 (LS 180, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.752×** | -3.2 | 0.097 | 7/46 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.820×** | -3.2 | 0.098 | 12/46 (H4, Panc 03.27, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.758× | -3.0 | 0.15 | 11/43 (BT-474, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.763× | -3.0 | 0.15 | 11/46 (NCI-H1573, HS-578T, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.12 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +13.1) | — |
| [[KATO III (line)]] | alt | 17.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +9.8) | — |
| [[A498 (line)]] | wt | 11.3 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.313× (z -10.1) |
| [[LS 180 (line)]] | wt | 28.3 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.174× (z -9.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.200× (z -9.2) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -8.9) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 1 | — | [[Erlotinib (drug)]] 0.5 µM 0.0523× (z -8.7) |
| [[COLO 205 (line)]] | alt | 7.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.0× (z +14.0) | — |
| [[J82 (line)]] | alt | 9.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change |
| [[LOX-IMVI (line)]] | wt | 9.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 9.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 7.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 5.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 7.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY2]] | +0.67 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ING1]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DDX50]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[BCL2L12]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ASL]] | +0.60 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[INAFM1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ESCO1]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[NOSIP]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[METTL23]] | +0.56 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DCXR]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[RGP1]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[KATNA1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP4]] | -0.65 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ARPP19]] | -0.64 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[NAA50]] | -0.62 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[PSMB2]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[RAD23B]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[TMX3]] | -0.56 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[NCKAP1]] | -0.56 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LARP1]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[PPP2CA]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[UBE2L3]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises GCAT's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.8, -30.2); signed map (-25.1, 15.8). **Vector** length 82.8, 16.4% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +15.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.1 | +8.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +13.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.0 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.4 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | glycine C-acetyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,807,905-37,817,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KBL |
| Gene groups (HGNC) | Acyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75600](https://www.uniprot.org/uniprotkb/O75600) (2-amino-3-ketobutyrate coenzyme A ligase, mitochondrial):

> Pyridoxal phosphate (PLP) dependent enzyme, which catalyzes the cleavage of 2-amino-3-oxobutanoate to glycine and acetyl-CoA.

**Summary**, from NCBI Gene [23464](https://www.ncbi.nlm.nih.gov/gene/23464):

> The degradation of L-threonine to glycine consists of a two-step biochemical pathway involving the enzymes L-threonine dehydrogenase and 2-amino-3-ketobutyrate coenzyme A ligase. L-Threonine is first converted into 2-amino-3-ketobutyrate by L-threonine dehydrogenase. This gene encodes the second enzyme in this pathway, which then catalyzes the reaction between 2-amino-3-ketobutyrate and coenzyme A to form glycine and acetyl-CoA. The encoded enzyme is considered a class II …

**Accessions** — [HGNC:4188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4188) · Entrez [23464](https://www.ncbi.nlm.nih.gov/gene/23464) · UniProt [O75600](https://www.uniprot.org/uniprotkb/O75600) · Ensembl [ENSG00000100116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100116)

## Data

Gene col 1872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1872); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1872]; `tensor/DDL_lfc|DDL_z.npy` [1872]; `embed/gene_vectors.npy` [1872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1872 or target_col == 1872). Every well: [[GCAT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCAT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
