---
symbol: "LZTFL1"
type: "gene"
col: 8788
ensembl_id: "ENSG00000163818"
name: "leucine zipper transcription factor like 1"
location: "3p21.31"
module: 127
arm: "+"
pooled_cpm: 21.76
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# LZTFL1

*leucine zipper transcription factor like 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.55× (z +6.6, q 2e-08, up in 15 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.51× (z +6.5, q 2e-08, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.641× (z -7.0, q 1e-09, down in 37 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 0.697× (z -5.7, q 3e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX19]] (+0.52, fdr 3e-05), [[BAG6]] (+0.50, fdr 1e-04), [[GNS]] (+0.50, fdr 4e-05); moves opposite to [[PAQR7]] (-0.50, fdr 6e-05), [[HDAC7]] (-0.48, fdr 5e-05), [[ACTR3B]] (-0.47, fdr 1e-04).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.6 | 2e-08 | 15/32 (Hs 766T, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +6.5 | 2e-08 | 26/48 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +5.5 | 5e-06 | 29/48 (LS 180, H4, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +5.5 | 5e-06 | 24/48 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +5.0 | 7e-05 | 23/48 (SW1417, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.25×** | +4.9 | 9e-05 | 20/48 (NCI-H460, J82, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.1 | 0.003 | 14/37 (SK-MEL-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.28×** | +3.9 | 0.006 | 17/48 (PANC-1, LS 180, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.3 | 0.071 | 17/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -7.0 | 1e-09 | 37/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.697×** | -5.7 | 3e-06 | 27/48 (A549, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.691×** | -5.4 | 1e-05 | 23/46 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.798×** | -5.0 | 6e-05 | 22/48 (SK-MEL-2, LoVo, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.675×** | -4.4 | 0.001 | 15/48 (PANC-1, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.536×** | -4.4 | 0.001 | 14/44 (SK-MEL-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.827×** | -4.3 | 0.002 | 21/47 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.772×** | -4.1 | 0.003 | 22/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.784×** | -3.9 | 0.007 | 16/48 (A549, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.022 | 18/48 (HEC-1-A, AN3 CA, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.733×** | -3.5 | 0.022 | 9/48 (HT-29, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.856× | -3.5 | 0.022 | 14/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.037 | 15/48 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.815×** | -3.1 | 0.073 | 15/47 (H4, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.353× (z -8.5) |
| [[LS 180 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.267× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~16% of this change |
| [[NCI-H1792 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.5) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 31.2 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0540× (z -9.5) |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -8.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW48 (line)]] | wt | 27.1 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.101× (z -10.5) |
| [[A-172 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX19]] | +0.52 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[BAG6]] | +0.50 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[GNS]] | +0.50 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[HDLBP]] | +0.50 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[GOLM2]] | +0.49 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[DNAH7]] | +0.49 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[EIF2AK1]] | +0.49 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[RNF213-AS1]] | +0.48 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[DNAL1]] | +0.48 | +0.24 / +0.52 | both halves | 4e-04 |  |
| [[KIF9]] | +0.48 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[NELFE]] | +0.47 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[UBFD1]] | +0.47 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR7]] | -0.50 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[HDAC7]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ACTR3B]] | -0.47 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[ZNF786]] | -0.46 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[FBXO45]] | -0.45 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ENDOG]] | -0.45 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[MTG2]] | -0.45 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[ZNF398]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[LSM8]] | -0.44 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[CSTF3-DT]] | -0.44 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[MEMO1]] | -0.44 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[NLRX1]] | -0.44 | -0.45 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers LZTFL1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.303). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, -18.5); signed map (-30.0, -34.5). **Vector** length 87.4, 17.2% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.9 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.9 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.7 | +2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.4 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -5.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper transcription factor like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,823,316-45,916,042 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BBS17 |
| Reactome | 5 pathways, smallest: BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ48](https://www.uniprot.org/uniprotkb/Q9NQ48) (Leucine zipper transcription factor-like protein 1):

> Regulates ciliary localization of the BBSome complex. Together with the BBSome complex, controls SMO ciliary trafficking and contributes to the sonic hedgehog (SHH) pathway regulation. May play a role in neurite outgrowth. May have tumor suppressor function.

**Summary**, from NCBI Gene [54585](https://www.ncbi.nlm.nih.gov/gene/54585):

> This gene encodes a ubiquitously expressed protein that localizes to the cytoplasm. This protein interacts with Bardet-Biedl Syndrome (BBS) proteins and, through its interaction with BBS protein complexes, regulates protein trafficking to the ciliary membrane. Nonsense mutations in this gene cause a form of Bardet-Biedl Syndrome; a ciliopathy characterized in part by polydactyly, obesity, cognitive impairment, hypogonadism, and kidney failure. This gene may also function as a tumor suppressor; …

**Accessions** — [HGNC:6741](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6741) · Entrez [54585](https://www.ncbi.nlm.nih.gov/gene/54585) · UniProt [Q9NQ48](https://www.uniprot.org/uniprotkb/Q9NQ48) · Ensembl [ENSG00000163818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163818)

## Data

Gene col 8788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8788); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8788]; `tensor/DDL_lfc|DDL_z.npy` [8788]; `embed/gene_vectors.npy` [8788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8788 or target_col == 8788). Every well: [[LZTFL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LZTFL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
