---
symbol: "SCAND2P"
type: "gene"
col: 10743
ensembl_id: "ENSG00000176700"
name: "SCAN domain containing 2 pseudogene"
location: "15q25.2"
module: 103
arm: "+"
pooled_cpm: 6.84
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# SCAND2P

*SCAN domain containing 2 pseudogene* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.23× (z +9.5, q 8e-19, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.539× (z -9.3, q 1e-17, down in 27 of 35 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.626× (z -7.3, q 5e-11, down in 21 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 11 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H1792 0.0263×, J82 0.124×, LOX-IMVI 0.0845×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.120×; ⚠ cell-cycle shift, explains ~78% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.0422×; ⚠ cell-cycle shift, explains ~29% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0734×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.140×); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.112×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM45A]] (+0.56, fdr 1e-05), [[DDX41]] (+0.55, fdr 1e-05), [[DPCD]] (+0.55, fdr 1e-05); moves opposite to [[SMC6]] (-0.46, fdr 5e-05), [[EFR3A]] (-0.45, fdr 1e-04), [[PEAK1]] (-0.44, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DPYSL4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.23×** | +9.5 | 8e-19 | 30/46 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +6.3 | 1e-07 | 18/41 (HOP62, A-172, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +4.5 | 0.002 | 10/44 (SW480, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.018 | 11/44 (SNU-423, HOP62, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.24× | +3.3 | 0.12 | 10/43 (C-33 A, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10743.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 11 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H1792 0.0263×, J82 0.124×, LOX-IMVI 0.0845×; ⚠ toxic); [[Homoharringtonine (drug)]] 5 µM in 1 line (C32 0.120×; ⚠ cell-cycle shift, explains ~78% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.0422×; ⚠ cell-cycle shift, explains ~29% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0734×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.140×); [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.539×** | -9.3 | 1e-17 | 27/35 (NCI-H1792, J82, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.560×** | -9.0 | 4e-17 | 31/44 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -7.3 | 5e-11 | 21/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.654×** | -6.6 | 5e-09 | 21/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.678×** | -5.8 | 6e-07 | 17/44 (MIA PaCa-2, C32, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.769×** | -5.8 | 6e-07 | 17/42 (C32, CFPAC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.731×** | -4.9 | 9e-05 | 20/45 (hTERT-HPNE, C-33 A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.737×** | -4.5 | 5e-04 | 17/42 (C32, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.783×** | -3.8 | 0.009 | 13/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.778×** | -3.8 | 0.009 | 5/12 (NCI-H1792, SNU-423, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.816×** | -3.2 | 0.078 | 14/45 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 18.9 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.140× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 19.8 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0263× (z -18.7) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 6.24 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0977× (z -9.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.112× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -9.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 5.86 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.167× (z -8.5) |
| [[HOP62 (line)]] | alt | 6.88 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 28.5× (z +9.0) | — |
| [[J82 (line)]] | alt | 7.34 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -10.0) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 5.88 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0845× (z -9.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 6.77 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0886× (z -10.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H1573 (line)]] | alt | 6.90 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0734× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 3.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0846× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.99 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -8.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 7.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -9.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -8.6) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 6.54 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.113× (z -8.6) |
| [[SW1417 (line)]] | alt | 4.15 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0802× (z -9.6) ⚠ toxic; unreliable plate only |
| [[A-172 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM45A]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DDX41]] | +0.55 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[DPCD]] | +0.55 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[NIM1K]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[TCAF2]] | +0.54 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[ING4]] | +0.53 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[GYS1]] | +0.53 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TRMU]] | +0.52 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[ZNF8-DT]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ISY1]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PPP6C]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[ZNF808]] | +0.52 | +0.61 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC6]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[EFR3A]] | -0.45 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[PEAK1]] | -0.44 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPYSL4]] | B | DPYSL4 activity raises SCAND2P's level | lines that do not express DPYSL4 (24) vs lines expressing it (26) | 1.36× lower at baseline in the lines without DPYSL4 | 0.047 | ⚠ within organs, on part of the lines; also absent: TWIST2, ZIC1, MICU3 |
| [[NRN1]] | B | NRN1 activity raises SCAND2P's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.30× lower at baseline in the lines without NRN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.4, -21.6); signed map (-40.7, 26.4). **Vector** length 63.4, 9.00% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | +1.7 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +0.4 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +0.9 | +0.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.0 | -6.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | SCAN domain containing 2 pseudogene |
| Locus type | pseudogene |
| Location | 15q25.2 — chr15:84,631,963-84,642,066 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously SCAND2 |
| Matched by | ensembl_id |

UniProt [Q9GZW5](https://www.uniprot.org/uniprotkb/Q9GZW5) carries no function annotation.

**Summary**, from NCBI Gene [54581](https://www.ncbi.nlm.nih.gov/gene/54581):

> Predicted to enable DNA-binding transcription factor activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10567) · Entrez [54581](https://www.ncbi.nlm.nih.gov/gene/54581) · UniProt [Q9GZW5](https://www.uniprot.org/uniprotkb/Q9GZW5) · Ensembl [ENSG00000176700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176700)

## Data

Gene col 10743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10743); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10743]; `tensor/DDL_lfc|DDL_z.npy` [10743]; `embed/gene_vectors.npy` [10743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10743 or target_col == 10743). Every well: [[SCAND2P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAND2P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
