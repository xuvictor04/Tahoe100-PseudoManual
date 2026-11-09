---
symbol: "ACTR1A"
type: "gene"
col: 6127
ensembl_id: "ENSG00000138107"
name: "actin related protein 1A"
location: "10q24.32"
module: 72
arm: "+"
pooled_cpm: 26.05
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ACTR1A

*actin related protein 1A* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.15× (z +15.0, q 0e+00, up in 30 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.68× (z +10.6, q 8e-24, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.791× (z -6.8, q 5e-09, down in 23 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.797× (z -4.7, q 4e-04, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.200×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.391×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP5]] (+0.69, fdr 7e-06), [[ABCB8]] (+0.63, fdr 1e-05), [[PSMD1]] (+0.62, fdr 7e-06); moves opposite to [[ZNF330]] (-0.54, fdr 3e-05), [[AFMID]] (-0.52, fdr 1e-05), [[GOLGA4]] (-0.51, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HEG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +15.0 | 0e+00 | 30/35 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +13.6 | 7e-40 | 37/42 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +10.6 | 8e-24 | 37/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +10.2 | 2e-22 | 31/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +9.9 | 5e-21 | 36/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +9.9 | 5e-21 | 42/48 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +7.4 | 1e-11 | 32/47 (LoVo, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.8 | 5e-07 | 19/47 (CFPAC-1, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.18× | +4.7 | 2e-04 | 20/47 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.27×** | +4.6 | 2e-04 | 21/47 (PANC-1, C-33 A, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.4 | 5e-04 | 11/48 (HEC-1-A, H4, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.24×** | +4.3 | 8e-04 | 16/48 (CFPAC-1, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.24×** | +4.2 | 0.001 | 20/46 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.23×** | +4.1 | 0.002 | 16/46 (HS-578T, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +4.0 | 0.002 | 19/48 (A498, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.054 | 4/48 (PANC-1, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.0 | 0.060 | 10/48 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.060 | 10/47 (HOP62, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6127.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (Hs 766T 0.200×; ⚠ cell-cycle shift, explains ~29% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (LOX-IMVI 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.391×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.791×** | -6.8 | 5e-09 | 23/48 (Hs 766T, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.787×** | -4.9 | 2e-04 | 25/48 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -4.8 | 3e-04 | 22/48 (LOX-IMVI, J82, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.797×** | -4.7 | 4e-04 | 19/48 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.847× | -3.4 | 0.068 | 7/48 (SW 1088, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.862× | -3.1 | 0.21 | 3/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 35.8 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +9.6) ⚠ cell-cycle shift, explains ~77% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 26.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 39.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -9.0) |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.200× (z -16.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +9.3) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP5]] | +0.69 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[ABCB8]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[PSMD1]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 | pathway: G2/M Transition |
| [[MAPK9]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PSMD11]] | +0.61 | +0.57 / +0.66 | both halves | 1e-05 | pathway: G2/M Transition |
| [[DBNL]] | +0.60 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[KLC2]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins; STRING 608 |
| [[EXT2]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[TALDO1]] | +0.58 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[PSMD2]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 | pathway: G2/M Transition |
| [[PCNX3]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[USP39]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF330]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[AFMID]] | -0.52 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[GOLGA4]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[SNHG8]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RPAIN]] | -0.50 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SNHG7]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[MITD1]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TCAF1]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[POLR1H]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEG1]] | B | HEG1 activity raises ACTR1A's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without HEG1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.435). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.5, -13.0); signed map (-29.6, -30.3). **Vector** length 94.4, 20.3% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.8 | +9.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.1 | +10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.6 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +15.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.5 | -6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.2 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -4.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.0 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,461,881-102,502,712 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARP1, Arp1A |
| Gene groups (HGNC) | Dynactin subunits; Actin related proteins |
| Reactome | 34 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Loss of Nlp from mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [P61163](https://www.uniprot.org/uniprotkb/P61163) (Alpha-centractin):

> Part of the ACTR1A/ACTB filament around which the dynactin complex is built. The dynactin multiprotein complex activates the molecular motor dynein for ultra-processive transport along microtubules.

**Summary**, from NCBI Gene [10121](https://www.ncbi.nlm.nih.gov/gene/10121):

> This gene encodes a 42.6 kD subunit of dynactin, a macromolecular complex consisting of 10-11 subunits ranging in size from 22 to 150 kD. Dynactin binds to both microtubules and cytoplasmic dynein. It is involved in a diverse array of cellular functions, including ER-to-Golgi transport, the centripetal movement of lysosomes and endosomes, spindle formation, chromosome movement, nuclear positioning, and axonogenesis. This subunit is present in 8-13 copies per dynactin molecule, and is the most …

**Accessions** — [HGNC:167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:167) · Entrez [10121](https://www.ncbi.nlm.nih.gov/gene/10121) · UniProt [P61163](https://www.uniprot.org/uniprotkb/P61163) · Ensembl [ENSG00000138107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138107)

## Data

Gene col 6127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6127); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6127]; `tensor/DDL_lfc|DDL_z.npy` [6127]; `embed/gene_vectors.npy` [6127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6127 or target_col == 6127). Every well: [[ACTR1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
