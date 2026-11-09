---
symbol: "HARS2"
type: "gene"
col: 3413
ensembl_id: "ENSG00000112855"
name: "histidyl-tRNA synthetase 2, mitochondrial"
location: "5q31.3"
module: 17
arm: "+"
pooled_cpm: 16.29
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# HARS2

*histidyl-tRNA synthetase 2, mitochondrial* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.65× (z +13.5, q 8e-39, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.645× (z -12.4, q 1e-32, down in 33 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.224×, A-427 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.188×, RPMI-7951 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.388×, NCI-H460 0.507×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (AsPC-1 0.174×); [[Pimozide (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS33B]] (+0.75, fdr 7e-06), [[DMAP1]] (+0.72, fdr 7e-06), [[ABCF3]] (+0.71, fdr 7e-06); moves opposite to [[IGF2BP3]] (-0.58, fdr 3e-05), [[PSMD6-AS2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.65×** | +13.5 | 8e-39 | 41/48 (SW480, A-427, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.07×** | +11.7 | 3e-29 | 35/46 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +10.2 | 3e-22 | 9/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +6.8 | 1e-09 | 19/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +6.8 | 1e-09 | 21/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 3e-07 | 17/48 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +5.8 | 7e-07 | 19/48 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.3 | 9e-06 | 15/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +5.1 | 2e-05 | 19/48 (NCI-H1573, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.9 | 6e-05 | 15/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +4.4 | 7e-04 | 13/47 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.9 | 0.004 | 11/43 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.035 | 2/47 (LS 180, LoVo) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.2 | 0.056 | 13/48 (NCI-H2030, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.0 | 0.10 | 6/48 (RKO, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3413.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.224×, A-427 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (HEC-1-A 0.188×, RPMI-7951 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-172 0.388×, NCI-H460 0.507×); [[Oxaprozin (drug)]] 0.5 µM in 1 line (AsPC-1 0.174×); [[Pimozide (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.645×** | -12.4 | 1e-32 | 33/46 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.868× | -4.0 | 0.015 | 16/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.833×** | -3.5 | 0.075 | 13/48 (SNU-1, NCI-H460, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.852× | -3.2 | 0.18 | 2/48 (LOX-IMVI, PANC-1) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.851× | -3.1 | 0.20 | 14/47 (A-172, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 22.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 2 (1 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.185× (z -8.9) |
| [[SW480 (line)]] | alt | 18.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.36× (z +9.8) | — |
| [[A-172 (line)]] | wt | 18.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.174× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.105× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[NCI-H460 (line)]] | wt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -9.0) |
| [[A498 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS33B]] | +0.75 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[DMAP1]] | +0.72 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ABCF3]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 | STRING 660 |
| [[RNF25]] | +0.70 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[TBC1D13]] | +0.69 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.69 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[BBS5]] | +0.68 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ZNF205]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[RNF20]] | +0.68 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ESS2]] | +0.67 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[PLRG1]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[VTA1]] | +0.66 | +0.67 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGF2BP3]] | -0.58 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[PSMD6-AS2]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HARS2's level | compounds that target TOP2A: 2 of 5 lower it (Epirubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.1, -2.9); signed map (-23.0, -17.7). **Vector** length 76.0, 13.0% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +11.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.8 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -3.5 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | histidyl-tRNA synthetase 2, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,691,430-140,699,305 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HO3, HARSR; previously HARSL |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 3 pathways, smallest: Mitochondrial tRNA aminoacylation; tRNA Aminoacylation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P49590](https://www.uniprot.org/uniprotkb/P49590) (Histidine--tRNA ligase, mitochondrial):

> Mitochondrial aminoacyl-tRNA synthetase that catalyzes the ATP-dependent ligation of histidine to the 3'-end of its cognate tRNA, via the formation of an aminoacyl-adenylate intermediate (His-AMP).

**Summary**, from NCBI Gene [23438](https://www.ncbi.nlm.nih.gov/gene/23438):

> Aminoacyl-tRNA synthetases are a class of enzymes that charge tRNAs with their cognate amino acids. The protein encoded by this gene is an enzyme belonging to the class II family of aminoacyl-tRNA synthetases. Functioning in the synthesis of histidyl-transfer RNA, the enzyme plays an accessory role in the regulation of protein biosynthesis. The gene is located in a head-to-head orientation with HARS on chromosome five, where the homologous genes likely share a bidirectional promoter. Mutations …

**Accessions** — [HGNC:4817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4817) · Entrez [23438](https://www.ncbi.nlm.nih.gov/gene/23438) · UniProt [P49590](https://www.uniprot.org/uniprotkb/P49590) · Ensembl [ENSG00000112855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112855)

## Data

Gene col 3413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3413); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3413]; `tensor/DDL_lfc|DDL_z.npy` [3413]; `embed/gene_vectors.npy` [3413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3413 or target_col == 3413). Every well: [[HARS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HARS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
