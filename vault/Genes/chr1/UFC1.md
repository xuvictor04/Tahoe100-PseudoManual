---
symbol: "UFC1"
type: "gene"
col: 6700
ensembl_id: "ENSG00000143222"
name: "ubiquitin-fold modifier conjugating enzyme 1"
location: "1q23.3"
module: 23
arm: "+"
pooled_cpm: 27.97
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# UFC1

*ubiquitin-fold modifier conjugating enzyme 1* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +9.3, q 1e-17, up in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.54× (z +4.4, q 0.001, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HEC-1-A 5.43×, LoVo 4.02×, A-427 4.98×, PANC-1 3.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 5.07×, PANC-1 3.03×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.28×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.379× (z -10.0, q 7e-21, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAZAP2]] (+0.72, fdr 1e-05), [[GIPC2]] (+0.71, fdr 1e-05), [[KMT2E-AS1]] (+0.69, fdr 1e-05); moves opposite to [[PPM1G]] (-0.62, fdr 1e-05), [[TUBG1]] (-0.59, fdr 3e-05), [[EHD4]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6700.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (HEC-1-A 5.43×, LoVo 4.02×, A-427 4.98×, PANC-1 3.10×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A-172 5.07×, PANC-1 3.03×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 3.28×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.3 | 1e-17 | 41/44 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +8.9 | 2e-16 | 29/33 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +6.1 | 1e-07 | 35/39 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +6.1 | 1e-07 | 38/46 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.4 | 0.001 | 30/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.41×** | +3.5 | 0.041 | 25/45 (RPMI-7951, C32, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.65× | +3.0 | 0.19 | 19/45 (LOX-IMVI, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6700.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.379×** | -10.0 | 7e-21 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.401×** | -9.4 | 1e-18 | 45/47 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.402×** | -9.4 | 1e-18 | 45/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.452×** | -8.2 | 4e-14 | 46/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.365×** | -5.4 | 6e-06 | 37/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.619×** | -5.0 | 7e-05 | 33/46 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.717×** | -4.6 | 3e-04 | 30/48 (C32, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6700. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 33.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.268× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -10.9) |
| [[SW480 (line)]] | alt | 24.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.9) |
| [[A-172 (line)]] | wt | 17.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 23.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.217× (z -9.8) |
| [[A-427 (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0805× (z -8.9) |
| [[C32 (line)]] | wt | 55.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -8.9) |
| [[COLO 205 (line)]] | alt | 37.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 22.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 36.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 39.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6700), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAZAP2]] | +0.72 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[GIPC2]] | +0.71 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[KMT2E-AS1]] | +0.69 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GPRASP3]] | +0.66 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[C1orf43]] | +0.65 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[N4BP2L1]] | +0.64 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[C11orf71]] | +0.63 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[BORCS7]] | +0.63 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[TSC1]] | +0.62 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[BORCS7-ASMT]] | +0.62 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[HPS1]] | +0.62 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[GTF2IRD2]] | +0.62 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1G]] | -0.62 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[TUBG1]] | -0.59 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[EHD4]] | -0.58 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[ZBED4]] | -0.56 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[CORO1C]] | -0.56 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[EML4]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NUP93]] | -0.55 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[GPRIN1]] | -0.55 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[MICAL2]] | -0.54 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TTLL12]] | -0.54 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[STUB1]] | -0.54 | -0.48 / -0.09 | ⚠ not reproduced | 0.003 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UFC1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UFC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.9, 22.6); signed map (19.9, -10.3). **Vector** length 73.8, 18.7% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | -0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +0.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -9.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.2 | -5.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin-fold modifier conjugating enzyme 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,152,776-161,158,856 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC155 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3C8](https://www.uniprot.org/uniprotkb/Q9Y3C8) (Ubiquitin-fold modifier-conjugating enzyme 1):

> E2-like enzyme which specifically catalyzes the second step in ufmylation. Accepts the ubiquitin-like modifier UFM1 from the E1 enzyme UBA5 and forms an intermediate with UFM1 via a thioester linkage. Ufmylation is involved in various processes, such as ribosome recycling, response to DNA damage, interferon response or reticulophagy (also called ER-phagy).

**Summary**, from NCBI Gene [51506](https://www.ncbi.nlm.nih.gov/gene/51506):

> UFC1 is an E2-like conjugating enzyme for ubiquitin-fold modifier-1 (UFM1; MIM 610553) (Komatsu et al., 2004 [PubMed 15071506]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26941](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26941) · Entrez [51506](https://www.ncbi.nlm.nih.gov/gene/51506) · UniProt [Q9Y3C8](https://www.uniprot.org/uniprotkb/Q9Y3C8) · Ensembl [ENSG00000143222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143222)

## Data

Gene col 6700: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6700); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6700, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6700]; `tensor/DDL_lfc|DDL_z.npy` [6700]; `embed/gene_vectors.npy` [6700]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6700 or target_col == 6700). Every well: [[UFC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UFC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
