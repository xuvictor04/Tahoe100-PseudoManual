---
symbol: "A2MP1"
type: "gene"
col: 14974
ensembl_id: "ENSG00000256069"
name: "PZP alpha-2-macroglobulin like 2, pseudogene"
location: ""
module: 58
arm: "+"
pooled_cpm: 6.29
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# A2MP1

*PZP alpha-2-macroglobulin like 2, pseudogene*

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.28× (z +7.7, q 6e-12, up in 23 of 27 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Bendamustine (drug)]] 5 µM: 1.65× (z +3.5, q 0.040, up in 17 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (hTERT-HPNE 130×, BT-474 39.6×, J82 10.6×, SNU-423 15.6×, …; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Budesonide (drug)]] 5 µM: 0.586× (z -3.8, q 0.047, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.199×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.120×); [[Trifluridine (drug)]] 0.5 µM in 1 line (SHP-77 0.0605×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pentagastrin (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0576×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW 900 0.0750×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTMAP2]] (+0.74, fdr 7e-06, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[PTMAP5]] (+0.74, fdr 7e-06), [[PTMA]] (+0.72, fdr 7e-06), [[BCL2L14]] (+0.66, fdr 7e-06); moves opposite to [[STX16]] (-0.55, fdr 3e-05), [[IKBKG]] (-0.54, fdr 3e-05), [[LZTR1]] (-0.54, fdr 3e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TESK2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (hTERT-HPNE 130×, BT-474 39.6×, J82 10.6×, SNU-423 15.6×, …; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.28×** | +7.7 | 6e-12 | 23/27 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.62×** | +6.6 | 9e-09 | 8/11 (LS 180, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.91×** | +4.7 | 6e-04 | 22/40 (NCI-H460, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.93×** | +4.4 | 0.002 | 11/16 (J82, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.52×** | +4.3 | 0.002 | 15/41 (hTERT-HPNE, BT-474, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.73×** | +3.9 | 0.007 | 17/33 (A-172, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Bendamustine (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.040 | 17/41 (SW480, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.199×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.120×); [[Trifluridine (drug)]] 0.5 µM in 1 line (SHP-77 0.0605×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pentagastrin (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0576×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW 900 0.0750×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | **0.586×** | -3.8 | 0.047 | 20/47 (SW 1271, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.581×** | -3.7 | 0.047 | 20/43 (J82, LS 180, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.598×** | -3.7 | 0.047 | 17/42 (LS 180, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.724× | -3.3 | 0.16 | 15/47 (hTERT-HPNE, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 16.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -9.5) |
| [[BT-474 (line)]] | alt | 6.02 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 39.6× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HS-578T (line)]] | alt | 4.16 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 4.01 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 130× (z +17.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 3.73 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 4.04 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0576× (z -9.0) |
| [[SHP-77 (line)]] | alt | 6.69 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0605× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 3.47 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 6.41 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0750× (z -8.6) |
| [[A-172 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMAP2]] ⚠ | +0.74 | +0.59 / +0.83 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PTMAP5]] | +0.74 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[PTMA]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[BCL2L14]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[IGFBP2]] | +0.58 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[TESK2]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[NMU]] | +0.57 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[LCORL]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[KMT2E]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[RFX2]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[HMGB1P5]] ⚠ | +0.55 | +0.44 / +0.56 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CXXC5]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SLC35B2]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CD70]] | +0.54 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX16]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[IKBKG]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[LZTR1]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ABCF2]] | -0.53 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[GPN1]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[PSMD12]] | -0.52 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PEX26]] | -0.50 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SNX19]] | -0.50 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[ELAC2]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[SLC35F6]] | -0.50 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[HERC2P9-1]] | -0.50 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[TOP3B]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TESK2]] | C | TESK2 activity lowers A2MP1's level | lines that do not express TESK2 (3) vs lines expressing it (46) | 1.90× higher at baseline in the lines without TESK2 | 0.092 | ⚠ few lines (3 vs 46); across organs; also absent: SYNPO2, SLC9A3, SFXN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.387). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-55.4, -16.5); signed map (-39.1, 16.4). **Vector** length 54.8, 8.90% of its response variance represented; |z| ≥ 3 in 625 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +2.7 | +4.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.5 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | PZP alpha-2-macroglobulin like 2, pseudogene |
| Locus type | pseudogene |
| Location | — chr12:9,229,376-9,275,817 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously A2MP1 |
| Gene groups (HGNC) | Alpha-2-macroglobulin family; Unitary pseudogenes |
| Matched by | prev_symbol |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56245) · Entrez [124903067](https://www.ncbi.nlm.nih.gov/gene/124903067) · Ensembl [ENSG00000256069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256069)

## Data

Gene col 14974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14974); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14974]; `tensor/DDL_lfc|DDL_z.npy` [14974]; `embed/gene_vectors.npy` [14974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14974 or target_col == 14974). Every well: [[A2MP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/A2MP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
