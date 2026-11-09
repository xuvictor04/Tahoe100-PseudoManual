---
symbol: "UBA3"
type: "gene"
col: 6923
ensembl_id: "ENSG00000144744"
name: "ubiquitin like modifier activating enzyme 3"
location: "3p14.1"
module: 198
arm: "+"
pooled_cpm: 58.94
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# UBA3

*ubiquitin like modifier activating enzyme 3* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.24× (z +6.7, q 1e-08, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.25× (z +5.0, q 1e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.759× (z -6.1, q 5e-07, down in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.436×, HOP62 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.266×); [[Thymopentin (drug)]] 5 µM in 1 line (SW 1271 0.0520×); [[Drospirenone (drug)]] 0.5 µM in 1 line (SW 1271 0.0651×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT8]] (+0.73, fdr 7e-06), [[DHX29]] (+0.69, fdr 7e-06), [[MRPL22]] (+0.66, fdr 7e-06); moves opposite to [[ETF1]] (-0.65, fdr 1e-05), [[FAM53A]] (-0.60, fdr 1e-05), [[FSCN2]] (-0.59, fdr 1e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.24×** | +6.7 | 1e-08 | 24/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +5.0 | 1e-04 | 25/48 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +5.0 | 1e-04 | 27/48 (Panc 03.27, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.6 | 6e-04 | 24/47 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.5 | 7e-04 | 22/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.23×** | +4.4 | 0.001 | 18/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +4.2 | 0.002 | 14/48 (NCI-H2347, hTERT-HPNE, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +4.2 | 0.002 | 13/48 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.20× | +4.0 | 0.004 | 23/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.20× | +4.0 | 0.004 | 18/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 15/48 (C32, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +3.4 | 0.030 | 14/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.042 | 16/47 (PANC-1, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.15× | +3.1 | 0.083 | 14/48 (BT-474, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6923.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H460 0.436×, HOP62 0.444×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.266×); [[Thymopentin (drug)]] 5 µM in 1 line (SW 1271 0.0520×); [[Drospirenone (drug)]] 0.5 µM in 1 line (SW 1271 0.0651×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.759×** | -6.1 | 5e-07 | 29/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -5.5 | 1e-05 | 0/49 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.865× | -3.1 | 0.39 | 19/42 (NCI-H460, HOP62, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 90.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.5) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SW 1271 (line)]] | alt | 49.8 | 0 | 2 | — | [[Thymopentin (drug)]] 5 µM 0.0520× (z -10.0) |
| [[A-427 (line)]] | wt | 37.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.01× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 77.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.7) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[HOP62 (line)]] | alt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.436× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +13.8) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[RKO (line)]] | wt | 75.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 60.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.388× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 66.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.266× (z -10.7) |
| [[A-172 (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 70.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT8]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[DHX29]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MRPL22]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[XPA]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[RWDD3]] | +0.63 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[NDUFB4]] | +0.63 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[ASB8]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 519 |
| [[METTL14]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PAPOLG]] | +0.62 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[AP3S2]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETF1]] | -0.65 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[FAM53A]] | -0.60 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[FSCN2]] | -0.59 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.59 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[SMG1P6]] | -0.58 | -0.46 / -0.64 | both halves | 2e-05 |  |
| [[MAPRE1]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZDHHC11]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[HCG18]] | -0.55 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[THOC6]] | -0.55 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[PPIEL]] | -0.55 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[BTBD19]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers UBA3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.0, -4.5); signed map (-21.8, -9.3). **Vector** length 91.0, 20.5% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.7 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.4 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.4 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -5.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.2 | -2.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like modifier activating enzyme 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:69,054,730-69,080,408 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hUba3, NAE2; previously UBE1C |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes |
| Reactome | 14 pathways, smallest: Dengue Virus Attachment and Entry; NIK-->noncanonical NF-kB signaling; Dectin-1 mediated noncanonical NF-kB signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBC4](https://www.uniprot.org/uniprotkb/Q8TBC4) (NEDD8-activating enzyme E1 catalytic subunit):

> Catalytic subunit of the dimeric UBA3-NAE1 E1 enzyme. E1 activates NEDD8 by first adenylating its C-terminal glycine residue with ATP, thereafter linking this residue to the side chain of the catalytic cysteine, yielding a NEDD8-UBA3 thioester and free AMP. E1 finally transfers NEDD8 to the catalytic cysteine of UBE2M. Down-regulates steroid receptor activity. Necessary for cell cycle progression.

**Summary**, from NCBI Gene [9039](https://www.ncbi.nlm.nih.gov/gene/9039):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E1 ubiquitin-activating enzyme family. The encoded enzyme associates with AppBp1, an amyloid beta precursor protein binding protein, to form a …

**Accessions** — [HGNC:12470](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12470) · Entrez [9039](https://www.ncbi.nlm.nih.gov/gene/9039) · UniProt [Q8TBC4](https://www.uniprot.org/uniprotkb/Q8TBC4) · Ensembl [ENSG00000144744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144744)

## Data

Gene col 6923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6923); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6923]; `tensor/DDL_lfc|DDL_z.npy` [6923]; `embed/gene_vectors.npy` [6923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6923 or target_col == 6923). Every well: [[UBA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
