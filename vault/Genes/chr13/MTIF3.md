---
symbol: "MTIF3"
type: "gene"
col: 4316
ensembl_id: "ENSG00000122033"
name: "mitochondrial translational initiation factor 3"
location: "13q12.2"
module: 24
arm: "+"
pooled_cpm: 37.04
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MTIF3

*mitochondrial translational initiation factor 3* — 13q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.41× (z +4.5, q 0.004, up in 25 of 46 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~26% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 2.35×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.458× (z -10.0, q 7e-21, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NKAP]] (+0.80, fdr 7e-06), [[ZNHIT3]] (+0.77, fdr 7e-06), [[RNF113A]] (+0.75, fdr 7e-06); moves opposite to [[VMA21]] (-0.73, fdr 7e-06), [[NUP188]] (-0.67, fdr 7e-06), [[PSME3]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APPAT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4316.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 2.35×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.41×** | +4.5 | 0.004 | 25/46 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4316.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -10.0 | 7e-21 | 41/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -9.5 | 6e-19 | 41/47 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.511×** | -8.6 | 1e-15 | 44/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -7.2 | 1e-10 | 36/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -6.1 | 1e-07 | 28/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.650×** | -5.5 | 3e-06 | 34/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.389×** | -5.2 | 2e-05 | 32/49 (Panc 03.27, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -4.8 | 9e-05 | 31/48 (HT-29, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.427×** | -4.7 | 2e-04 | 33/48 (HOP62, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.722×** | -3.8 | 0.007 | 19/42 (LoVo, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.724×** | -3.8 | 0.007 | 24/47 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.754×** | -3.3 | 0.040 | 19/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4316. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.8 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.322× (z -11.0) |
| [[A-172 (line)]] | wt | 43.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.4) |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.150× (z -12.1) |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.5) |
| [[J82 (line)]] | alt | 37.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -9.2) |
| [[KATO III (line)]] | alt | 46.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0908× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 34.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -14.7) |
| [[SNU-423 (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.1) |
| [[A-427 (line)]] | wt | 30.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -9.2) ⚠ toxic |
| [[A549 (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -8.9) |
| [[COLO 205 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 106 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.386× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -9.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -8.9) |
| [[LS 180 (line)]] | wt | 57.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 24.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 34.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.375× (z -8.8) |
| [[RKO (line)]] | wt | 41.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -8.5) |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0696× (z -9.4) ⚠ transcription drop; unreliable plate only |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -9.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4316), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | +0.80 | +0.68 / +0.86 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.77 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[RNF113A]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.73 | +0.62 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ZFAND2B]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.71 | +0.66 / +0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SUGP1]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[MED19]] | +0.70 | +0.56 / +0.74 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[C1orf35]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[LIN7B]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[RNF181]] | +0.69 | +0.51 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.73 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[NUP188]] | -0.67 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[PSME3]] | -0.66 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.65 | -0.42 / -0.72 | both halves | 4e-05 |  |
| [[HNRNPAB]] | -0.65 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.65 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.64 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[TARDBP]] | -0.64 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[HNRNPA3]] | -0.64 | -0.49 / -0.71 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.62 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.62 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[ARMC6]] | -0.62 | -0.55 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APPAT]] | B | APPAT activity raises MTIF3's level | lines that do not express APPAT (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without APPAT | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.763). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.6, -12.4); signed map (-15.8, -5.1). **Vector** length 91.9, 25.2% of its response variance represented; |z| ≥ 3 in 634 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.1 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.6 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.9 | +0.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.4 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial translational initiation factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.2 — chr13:27,435,643-27,450,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IF-3mt, IF3(mt) |
| Reactome | 3 pathways, smallest: Mitochondrial translation initiation; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2K0](https://www.uniprot.org/uniprotkb/Q9H2K0) (Translation initiation factor IF-3, mitochondrial):

> IF-3 binds to the 28S ribosomal subunit and shifts the equilibrium between 55S ribosomes and their 39S and 28S subunits in favor of the free subunits, thus enhancing the availability of 28S subunits on which protein synthesis initiation begins.

**Summary**, from NCBI Gene [219402](https://www.ncbi.nlm.nih.gov/gene/219402):

> This gene encodes a translation initiation factor that is involved in mitochondrial protein synthesis. Polymorphism in this gene is associated with the onset of Parkinson's disease. Alternate splicing results in multiple transcript variants. A pseudogene of this gene is found on chromosome 5. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:29788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29788) · Entrez [219402](https://www.ncbi.nlm.nih.gov/gene/219402) · UniProt [Q9H2K0](https://www.uniprot.org/uniprotkb/Q9H2K0) · Ensembl [ENSG00000122033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122033)

## Data

Gene col 4316: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4316); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4316, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4316]; `tensor/DDL_lfc|DDL_z.npy` [4316]; `embed/gene_vectors.npy` [4316]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4316 or target_col == 4316). Every well: [[MTIF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTIF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
