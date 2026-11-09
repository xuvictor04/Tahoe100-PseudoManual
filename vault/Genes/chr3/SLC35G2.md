---
symbol: "SLC35G2"
type: "gene"
col: 9723
ensembl_id: "ENSG00000168917"
name: "solute carrier family 35 member G2"
location: "3q22.3"
module: 7
arm: "+"
pooled_cpm: 23.42
n_lines_expressing: 38
n_dd_up: 3
n_dd_down: 24
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SLC35G2

*solute carrier family 35 member G2* — 3q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.27× (z +5.3, q 6e-05, up in 15 of 36 measured lines) ⚠ cell-cycle shift, explains ~72% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.18× (z +3.7, q 0.057, up in 8 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.407× (z -14.0, q 5e-42, down in 32 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF594]] (+0.64, fdr 1e-05), [[ZC3HC1]] (+0.64, fdr 1e-05), [[ZNF75A]] (+0.62, fdr 1e-05); moves opposite to [[EFNA3]] (-0.57, fdr 5e-05), [[PDK1]] (-0.54, fdr 2e-05), [[MGAT4A]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WIPF1]] → it (grade B ⚠); 3 go from it, the strongest it → [[TBCD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.27×** | +5.3 | 6e-05 | 15/36 (NCI-H2347, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.057 | 8/36 (NCI-H460, A549, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.26×** | +3.6 | 0.058 | 14/36 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.065 | 13/35 (SW480, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.23 | 5/36 (MIA PaCa-2, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9723.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.407×** | -14.0 | 5e-42 | 32/36 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.414×** | -13.8 | 8e-41 | 30/36 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.456×** | -12.3 | 3e-32 | 29/36 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.591×** | -7.9 | 4e-13 | 22/33 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.613×** | -7.1 | 2e-10 | 18/30 (A549, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.643×** | -6.9 | 5e-10 | 21/33 (SHP-77, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.665×** | -6.4 | 2e-08 | 22/36 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.687×** | -5.9 | 3e-07 | 20/34 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.692×** | -5.8 | 5e-07 | 21/36 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **0.686×** | -5.7 | 8e-07 | 16/27 (MIA PaCa-2, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.717×** | -5.2 | 1e-05 | 18/36 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.730×** | -4.9 | 4e-05 | 17/35 (SW1417, NCI-H2030, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.566×** | -4.7 | 1e-04 | 16/36 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **0.760×** | -4.3 | 7e-04 | 14/34 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.754×** | -4.2 | 9e-04 | 17/33 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.737×** | -3.4 | 0.019 | 11/35 (CHP-212, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.667×** | -3.3 | 0.026 | 9/34 (PANC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.027 | 9/35 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.027 | 13/36 (SW 1088, PANC-1, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.679×** | -3.2 | 0.039 | 12/34 (SW 900, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.775×** | -2.8 | 0.098 | 10/33 (PANC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 50.7 | 0 | 10 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.144× (z -15.0) |
| [[HOP62 (line)]] | alt | 54.0 | 0 | 6 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0777× (z -12.3) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.358× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -17.0) |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.238× (z -13.3) |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -13.8) |
| [[A549 (line)]] | wt | 30.4 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0921× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.261× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 29.7 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SW480 (line)]] | alt | 50.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -17.9) |
| [[SNU-423 (line)]] | alt | 26.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -13.3) |
| [[SW 900 (line)]] | alt | 43.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -12.5) |
| [[A-172 (line)]] | wt | 41.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.326× (z -8.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.349× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[NCI-H2347 (line)]] | alt | 35.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 34.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -10.7) |
| [[PANC-1 (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.424× (z -9.5) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -8.9) |
| [[A-427 (line)]] | wt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -11.4) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[A498 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF594]] | +0.64 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ZC3HC1]] | +0.64 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZNF75A]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ZNF189]] | +0.62 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ZNF407-AS1]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[ZNF585B]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[KRR1]] | +0.59 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[CARD6]] | +0.59 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[ZNF302]] | +0.58 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[RPL7L1]] | +0.58 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TACO1]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ZNF629]] | +0.58 | +0.47 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNA3]] | -0.57 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PDK1]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MGAT4A]] | -0.54 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[EFNA4]] | -0.54 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[TPD52]] | -0.54 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[MPP1]] | -0.53 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[TRAF7]] | -0.53 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[PDK3]] | -0.53 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[CALR]] | -0.52 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[RALGAPA2]] | -0.52 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[SUN1]] | -0.52 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[GPI]] | -0.52 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WIPF1]] | B | WIPF1 activity raises SLC35G2's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 3.49× lower at baseline in the lines without WIPF1 | 0.018 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBCD]] | B | SLC35G2 activity lowers TBCD's level | lines that do not express SLC35G2 (12) vs lines expressing it (38) | 1.56× higher at baseline in the lines without SLC35G2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SMARCA1, LARP6, ZSCAN12 |
| [[SLC16A6]] | B | SLC35G2 activity raises SLC16A6's level | lines that do not express SLC35G2 (12) vs lines expressing it (38) | 2.23× lower at baseline in the lines without SLC35G2 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SMARCA1, LARP6, ZSCAN12 |
| [[PRRX2]] | C | SLC35G2 activity raises PRRX2's level | lines that do not express SLC35G2 (12) vs lines expressing it (38) | 3.05× lower at baseline in the lines without SLC35G2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SMARCA1, LARP6, ZSCAN12; co-absent with the target |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-39.9, 8.0); signed map (-2.4, -15.5). **Vector** length 73.9, 15.8% of its response variance represented; |z| ≥ 3 in 787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +4.3 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +1.5 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.7 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +3.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.4 | -13.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -14.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -12.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | -2.5 | -4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member G2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.3 — chr3:136,818,647-136,855,888 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3295, DKFZp564K2464; previously TMEM22 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

UniProt [Q8TBE7](https://www.uniprot.org/uniprotkb/Q8TBE7) carries no function annotation.

**Summary**, from NCBI Gene [80723](https://www.ncbi.nlm.nih.gov/gene/80723):

> Located in Golgi apparatus; plasma membrane; and synaptic vesicle membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28480) · Entrez [80723](https://www.ncbi.nlm.nih.gov/gene/80723) · UniProt [Q8TBE7](https://www.uniprot.org/uniprotkb/Q8TBE7) · Ensembl [ENSG00000168917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168917)

## Data

Gene col 9723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9723); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9723]; `tensor/DDL_lfc|DDL_z.npy` [9723]; `embed/gene_vectors.npy` [9723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9723 or target_col == 9723). Every well: [[SLC35G2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35G2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
