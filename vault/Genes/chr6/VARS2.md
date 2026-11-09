---
symbol: "VARS2"
type: "gene"
col: 6010
ensembl_id: "ENSG00000137411"
name: "valyl-tRNA synthetase 2, mitochondrial"
location: "6p21.33"
module: 96
arm: "+"
pooled_cpm: 8.92
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# VARS2

*valyl-tRNA synthetase 2, mitochondrial* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +8.5, q 1e-14, up in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.57× (z +5.1, q 4e-05, up in 16 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.658× (z -5.3, q 7e-05, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0781×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.139×; ⚠ cell-cycle shift, explains ~0% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 0.138×); [[Pemetrexed (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0677×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RHOT2]] (+0.57, fdr 1e-05), [[SLC4A2]] (+0.57, fdr 2e-05), [[BCS1L]] (+0.55, fdr 1e-05); moves opposite to [[FTL]] (-0.58, fdr 1e-05), [[TAX1BP1]] (-0.51, fdr 2e-05), [[RPLP1]] (-0.50, fdr 5e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.5 | 1e-14 | 23/35 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.9 | 1e-09 | 7/14 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +5.9 | 8e-07 | 12/22 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.6 | 3e-06 | 10/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.57×** | +5.1 | 4e-05 | 16/44 (LoVo, HepG2/C3A, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +4.9 | 8e-05 | 14/39 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.64×** | +4.4 | 8e-04 | 10/36 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.001 | 12/41 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.3 | 0.001 | 15/24 (A498, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +4.1 | 0.002 | 11/47 (RKO, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.005 | 11/44 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.84×** | +3.8 | 0.007 | 6/40 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.010 | 13/47 (RKO, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.5 | 0.022 | 16/37 (NCI-H1573, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.031 | 11/45 (NCI-H2347, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.061 | 4/44 (SW1417, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.069 | 4/36 (MIA PaCa-2, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.082 | 11/40 (A-172, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6010.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0781×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.139×; ⚠ cell-cycle shift, explains ~0% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (SNU-1 0.138×); [[Pemetrexed (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0677×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.658×** | -5.3 | 7e-05 | 24/47 (KATO III, LS 180, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -4.6 | 0.001 | 18/44 (AN3 CA, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.765× | -3.4 | 0.11 | 15/47 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.767× | -3.4 | 0.11 | 18/47 (HepG2/C3A, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.780× | -3.2 | 0.18 | 10/46 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 5.10 | 0 | 1 | — | [[Pemetrexed (drug)]] 0.05 µM 0.0677× (z -8.5) |
| [[J82 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.01 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0781× (z -9.6) |
| [[SNU-1 (line)]] | wt | 7.32 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.138× (z -8.9) |
| [[A-172 (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOT2]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SLC4A2]] | +0.57 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[BCS1L]] | +0.55 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ULK3]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[WDR74]] | +0.53 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[WIZ]] | +0.53 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[UBA1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CTBP1]] | +0.53 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[ATP13A1]] | +0.53 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[TRIM28]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[CTDNEP1]] | +0.52 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[SDR39U1]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTL]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[TAX1BP1]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[RPLP1]] | -0.50 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[RPL39]] | -0.50 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[SPCS1]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[SRP14]] | -0.46 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[PSMA7]] | -0.46 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[UBA52]] | -0.46 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[RPS12]] | -0.45 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[GSTP1]] | -0.45 | -0.29 / -0.39 | both halves | 2e-04 |  |
| [[ATP5PD]] | -0.44 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[SELENOK]] | -0.43 | -0.25 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises VARS2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.5, -44.3); signed map (4.6, -7.3). **Vector** length 55.9, 7.57% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +8.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.8 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +4.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.6 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.4 | -0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Afatinib (drug)]] 0.05 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | valyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,914,205-30,926,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434L1435, KIAA1885, G7a; previously VARS2L, VARSL |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class I |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5ST30](https://www.uniprot.org/uniprotkb/Q5ST30) (Valine--tRNA ligase, mitochondrial):

> Catalyzes the attachment of valine to tRNA(Val) in a two-step reaction: valine is first activated by ATP to form Val-AMP and then transferred to the acceptor end of tRNA(Val).

**Summary**, from NCBI Gene [57176](https://www.ncbi.nlm.nih.gov/gene/57176):

> This gene encodes a mitochondrial aminoacyl-tRNA synthetase, which catalyzes the attachment of valine to tRNA(Val) for mitochondrial translation. Mutations in this gene cause combined oxidative phosphorylation deficiency-20, and are also associated with early-onset mitochondrial encephalopathies. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Aug 2014]

**Accessions** — [HGNC:21642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21642) · Entrez [57176](https://www.ncbi.nlm.nih.gov/gene/57176) · UniProt [Q5ST30](https://www.uniprot.org/uniprotkb/Q5ST30) · Ensembl [ENSG00000137411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137411)

## Data

Gene col 6010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6010); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6010]; `tensor/DDL_lfc|DDL_z.npy` [6010]; `embed/gene_vectors.npy` [6010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6010 or target_col == 6010). Every well: [[VARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
