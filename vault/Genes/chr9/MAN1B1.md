---
symbol: "MAN1B1"
type: "gene"
col: 10806
ensembl_id: "ENSG00000177239"
name: "mannosidase alpha class 1B member 1"
location: "9q34.3"
module: 2
arm: "+"
pooled_cpm: 22.88
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MAN1B1

*mannosidase alpha class 1B member 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.66× (z +8.5, q 1e-14, up in 22 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.45× (z +4.6, q 8e-04, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.436× (z -14.3, q 8e-44, down in 43 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.481× (z -12.6, q 5e-34, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCA2]] (+0.68, fdr 7e-06), [[GLT8D1]] (+0.65, fdr 7e-06), [[PRPF8]] (+0.65, fdr 7e-06); moves opposite to [[ERVK3-1]] (-0.56, fdr 1e-05), [[DDX52]] (-0.53, fdr 1e-05), [[MTHFD2L]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CERCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.5 | 1e-14 | 22/32 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.2 | 9e-14 | 26/42 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 8e-04 | 18/46 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Simotinib (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.094 | 9/47 (RPMI-7951, HS-578T, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.094 | 4/48 (A-427, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Furosemide (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.094 | 8/48 (SNU-423, A498, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.1 | 0.15 | 3/48 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.28× | +3.0 | 0.17 | 9/45 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -14.3 | 8e-44 | 43/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -12.6 | 5e-34 | 35/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.496×** | -12.1 | 3e-31 | 38/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.509×** | -11.2 | 6e-27 | 38/47 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.543×** | -10.5 | 7e-24 | 40/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.557×** | -10.1 | 7e-22 | 38/48 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.558×** | -10.0 | 7e-22 | 39/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.707×** | -8.4 | 3e-15 | 27/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.652×** | -7.0 | 2e-10 | 25/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -6.6 | 2e-09 | 27/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.712×** | -5.8 | 3e-07 | 25/48 (HOP62, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -5.8 | 3e-07 | 23/46 (C-33 A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.793×** | -5.6 | 8e-07 | 27/48 (A-427, J82, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -5.2 | 8e-06 | 21/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.583×** | -4.9 | 4e-05 | 16/42 (MIA PaCa-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.712×** | -4.2 | 1e-03 | 13/48 (CHP-212, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -4.1 | 0.001 | 16/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.780×** | -3.9 | 0.002 | 15/47 (A549, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.826×** | -3.3 | 0.028 | 17/48 (BT-474, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 28.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.206× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -12.8) |
| [[H4 (line)]] | wt | 28.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0853× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 21.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -17.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0939× (z -17.0) |
| [[A-172 (line)]] | wt | 63.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.408× (z -9.2) |
| [[A498 (line)]] | wt | 36.8 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.383× (z -10.5) |
| [[A549 (line)]] | wt | 21.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 31.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -10.5) |
| [[SW480 (line)]] | alt | 19.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -9.4) |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -11.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 17.2 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.105× (z -10.3) |
| [[Hs 766T (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -12.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 38.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -8.5) |
| [[SW48 (line)]] | wt | 30.7 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0728× (z -12.8) |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCA2]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[GLT8D1]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[STT3A]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation; STRING 573 |
| [[INTS11]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GANAB]] | +0.62 | +0.54 / +0.68 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation; STRING 955 |
| [[CERCAM]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PLOD1]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[FAM234A]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[IDH3G]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MAPK3]] | +0.61 | +0.63 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK3-1]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[DDX52]] | -0.53 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[MTHFD2L]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[PSMA4]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERCAM]] | B | CERCAM activity raises MAN1B1's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without CERCAM | 0.090 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-18.5, -22.0); signed map (-50.6, -12.4). **Vector** length 80.6, 15.7% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +8.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -2.8 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.0 |
|  | [[Lopinavir (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Salicylic acid (drug)]] 5 µM |  | +1.6 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.5 | -10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 1B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,086,857-137,109,189 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MANA-ER, MRT15, ERManI, ERMan1 |
| Gene groups (HGNC) | Mannosidases alpha class 1 |
| Reactome | 13 pathways, smallest: Diseases associated with N-glycosylation of proteins; ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKM7](https://www.uniprot.org/uniprotkb/Q9UKM7) (Endoplasmic reticulum mannosyl-oligosaccharide 1,2-alpha-mannosidase):

> Involved in glycoprotein quality control targeting of misfolded glycoproteins for degradation. It primarily trims a single alpha-1,2-linked mannose residue from Man(9)GlcNAc(2) to produce Man(8)GlcNAc(2), but at high enzyme concentrations, as found in the ER quality control compartment (ERQC), it further trims the carbohydrates to Man(5-6)GlcNAc(2).

**Summary**, from NCBI Gene [11253](https://www.ncbi.nlm.nih.gov/gene/11253):

> This gene encodes an enzyme belonging to the glycosyl hydrolase 47 family. This enzyme functions in N-glycan biosynthesis, and is a class I alpha-1,2-mannosidase that specifically converts Man9GlcNAc to Man8GlcNAc isomer B. It is required for N-glycan trimming to Man5-6GlcNAc2 in the endoplasmic-reticulum-associated degradation pathway. Mutations in this gene cause autosomal-recessive intellectual disability. Alternative splicing results in multiple transcript variants. A related pseudogene has …

**Accessions** — [HGNC:6823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6823) · Entrez [11253](https://www.ncbi.nlm.nih.gov/gene/11253) · UniProt [Q9UKM7](https://www.uniprot.org/uniprotkb/Q9UKM7) · Ensembl [ENSG00000177239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177239)

## Data

Gene col 10806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10806); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10806]; `tensor/DDL_lfc|DDL_z.npy` [10806]; `embed/gene_vectors.npy` [10806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10806 or target_col == 10806). Every well: [[MAN1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
