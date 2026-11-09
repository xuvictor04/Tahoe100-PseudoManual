---
symbol: "CLN6"
type: "gene"
col: 4938
ensembl_id: "ENSG00000128973"
name: "CLN6 transmembrane ER protein"
location: "15q23"
module: 18
arm: "+"
pooled_cpm: 17.38
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CLN6

*CLN6 transmembrane ER protein* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +12.9, q 4e-35, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.639× (z -4.2, q 0.013, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.256×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.212×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.356×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CALML4]] (+0.69, fdr 7e-06, ⚠ same locus), [[CDCA7]] (+0.64, fdr 7e-06), [[CAD]] (+0.62, fdr 7e-06), [[XYLB]] (+0.60, fdr 1e-05); moves opposite to [[TAX1BP1]] (-0.55, fdr 2e-05), [[COPB2]] (-0.55, fdr 1e-05), [[OTUD5]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 20 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +12.9 | 4e-35 | 32/47 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +12.7 | 2e-34 | 37/47 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +11.6 | 1e-28 | 38/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.91×** | +11.3 | 3e-27 | 18/29 (KATO III, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.82×** | +10.9 | 2e-25 | 33/46 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.70×** | +9.7 | 4e-20 | 28/38 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.69×** | +9.5 | 3e-19 | 29/48 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.62×** | +8.1 | 4e-14 | 16/33 (A549, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.54×** | +7.9 | 2e-13 | 30/47 (PANC-1, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.57×** | +7.9 | 2e-13 | 25/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.50×** | +7.3 | 2e-11 | 25/48 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +6.9 | 2e-10 | 28/47 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.47×** | +6.7 | 1e-09 | 23/45 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.44×** | +6.6 | 2e-09 | 23/47 (SW1417, LOX-IMVI, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.79×** | +5.5 | 1e-06 | 20/47 (NCI-H460, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.78×** | +5.5 | 1e-06 | 18/46 (HT-29, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +5.1 | 8e-06 | 12/45 (SW1417, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.65×** | +4.8 | 5e-05 | 14/46 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 8e-05 | 16/48 (SW1417, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +4.5 | 1e-04 | 17/47 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.28×** | +4.4 | 2e-04 | 12/45 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 7e-04 | 8/48 (NCI-H460, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +4.1 | 7e-04 | 10/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.001 | 7/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.002 | 6/47 (NCI-H460, A549, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.256×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 0.212×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.356×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.639×** | -4.2 | 0.013 | 16/48 (SNU-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.678×** | -3.7 | 0.067 | 12/45 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.827× | -3.4 | 0.11 | 11/47 (SW480, HEC-1-A, …) | two highest doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.1 | 0.20 | 2/48 (HOP62, MIA PaCa-2) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.888× | -3.0 | 0.20 | 5/48 (A-427, A-172, …) | top dose only |  |
| [[RMC-6236 (drug)]] 5 µM |  | 0.727× | -3.0 | 0.20 | 6/47 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 26.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.7) | — |
| [[A-172 (line)]] | wt | 13.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 19.3 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.76× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.11× (z +10.3) | — |
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 16.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +13.3) | — |
| [[NCI-H460 (line)]] | wt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 30.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +14.6) | — |
| [[A-427 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALML4]] | +0.69 | +0.65 / +0.74 | both halves | 7e-06 | STRING 733; ⚠ same locus (0.9 kb, same strand: neighbours can correlate without regulation) |
| [[CDCA7]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CAD]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[XYLB]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CENPM]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TUBGCP4]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PFAS]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[DDX11]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[FOXRED2]] | +0.56 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[JPH1]] | +0.55 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ADAT2]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[POLE2]] | +0.54 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[RBFA]] | +0.54 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAX1BP1]] | -0.55 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[COPB2]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[OTUD5]] | -0.55 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TCP11L2]] | -0.55 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[BUD31]] | -0.54 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[SERINC1]] | -0.54 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[CCDC186]] | -0.53 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[YIPF3]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SYF2]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SPTY2D1]] | -0.52 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CLK3]] | -0.52 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[SLU7]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises CLN6's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.20× lower at baseline in the lines without ADCY3 | 0.019 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[CDC25A]] | B | CDC25A activity raises CLN6's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without CDC25A | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises CLN6's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without CDCA7 | 0.062 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[CENPM]] | C | CENPM activity raises CLN6's level | lines that do not express CENPM (3) vs lines expressing it (47) | 1.86× lower at baseline in the lines without CENPM | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises CLN6's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 1.60× lower at baseline in the lines without E2F1, MCM3 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.4, -50.2); signed map (-3.3, -57.4). **Vector** length 87.6, 18.5% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +11.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.7 | +10.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +12.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.5 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +4.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -2.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | CLN6 transmembrane ER protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:68,206,992-68,257,211 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20561, HsT18960, nclf |
| Hallmark sets | PEROXISOME, GLYCOLYSIS |
| Matched by | ensembl_id |

UniProt [Q9NWW5](https://www.uniprot.org/uniprotkb/Q9NWW5) carries no function annotation.

**Summary**, from NCBI Gene [54982](https://www.ncbi.nlm.nih.gov/gene/54982):

> This gene is one of eight which have been associated with neuronal ceroid lipofuscinoses (NCL). Also referred to as Batten disease, NCL comprises a class of autosomal recessive, neurodegenerative disorders affecting children. The genes responsible likely encode proteins involved in the degradation of post-translationally modified proteins in lysosomes. The primary defect in NCL disorders is thought to be associated with lysosomal storage function. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:2077](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2077) · Entrez [54982](https://www.ncbi.nlm.nih.gov/gene/54982) · UniProt [Q9NWW5](https://www.uniprot.org/uniprotkb/Q9NWW5) · Ensembl [ENSG00000128973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128973)

## Data

Gene col 4938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4938); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4938]; `tensor/DDL_lfc|DDL_z.npy` [4938]; `embed/gene_vectors.npy` [4938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4938 or target_col == 4938). Every well: [[CLN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
