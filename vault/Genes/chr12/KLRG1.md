---
symbol: "KLRG1"
type: "gene"
col: 6275
ensembl_id: "ENSG00000139187"
name: "killer cell lectin like receptor G1"
location: "12p13.31"
module: 9
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# KLRG1

*killer cell lectin like receptor G1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.16× (z +10.7, q 1e-23, up in 23 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Hesperidin (drug)]] 0.05 µM: 0.499× (z -4.8, q 7e-04, down in 8 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.141×; ⚠ cell-cycle shift, would explain all of this change); [[Piroxicam (drug)]] 0.5 µM in 1 line (C-33 A 0.0607×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPS8-DT]] (+0.55, fdr 2e-05), [[LINC01524]] (+0.55, fdr 1e-05), [[DISC1FP1]] (+0.50, fdr 3e-05); moves opposite to [[INTS8]] (-0.48, fdr 3e-04), [[MRPL49]] (-0.48, fdr 1e-04), [[NEDD1]] (-0.46, fdr 7e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 8 go from it, the strongest it → [[COPS8-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.16×** | +10.7 | 1e-23 | 23/28 (LoVo, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.00×** | +10.4 | 1e-22 | 31/37 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +10.2 | 5e-22 | 15/24 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.30×** | +8.9 | 6e-17 | 30/36 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.35×** | +8.8 | 1e-16 | 29/36 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.23×** | +8.2 | 3e-14 | 27/37 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +7.8 | 5e-13 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +6.1 | 8e-08 | 17/36 (LoVo, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **2.17×** | +5.6 | 1e-06 | 10/21 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +5.6 | 1e-06 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.06×** | +5.4 | 4e-06 | 19/37 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.1 | 2e-05 | 9/37 (A-427, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +4.8 | 8e-05 | 8/28 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +4.7 | 1e-04 | 1/7 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.81×** | +4.3 | 6e-04 | 11/30 (KATO III, A-427, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.75×** | +3.9 | 0.003 | 10/28 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.006 | 6/35 (A-427, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.59×** | +3.7 | 0.006 | 4/28 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6275.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.141×; ⚠ cell-cycle shift, would explain all of this change); [[Piroxicam (drug)]] 0.5 µM in 1 line (C-33 A 0.0607×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hesperidin (drug)]] 0.05 µM |  | **0.499×** | -4.8 | 7e-04 | 8/27 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.658× | -3.1 | 0.64 | 9/30 (LS 180, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 7.65 | 0 | 1 | — | [[Piroxicam (drug)]] 0.5 µM 0.0607× (z -9.1) |
| [[A-172 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.893 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.992 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.719 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8-DT]] | +0.55 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[LINC01524]] | +0.55 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DISC1FP1]] | +0.50 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[C16orf95]] | +0.49 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ID2-AS1]] | +0.49 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[CELF1]] | +0.48 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[LINC01320]] | +0.48 | +0.46 / +0.36 | both halves | 1e-04 |  |
| [[RERG]] | +0.48 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[KSR2]] | +0.47 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[KIF6]] | +0.47 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[DMXL1-DT]] | +0.47 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[PKIB]] | +0.46 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS8]] | -0.48 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[MRPL49]] | -0.48 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[NEDD1]] | -0.46 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ARMC1]] | -0.45 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[SCOC]] | -0.44 | -0.31 / -0.27 | both halves | 3e-04 |  |
| [[ZWILCH]] | -0.43 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[BTBD10]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TEP1]] | -0.43 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ZFYVE16]] | -0.42 | -0.11 / -0.58 | ⚠ one half (not replicated) | 0.002 |  |
| [[ACTR1B]] | -0.42 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[RNF34]] | -0.41 | -0.26 / -0.35 | both halves | 4e-04 |  |
| [[TAF15]] | -0.41 | -0.24 / -0.34 | both halves | 4e-04 |  |
| [[MED20]] | -0.41 | -0.30 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COPS8-DT]] | B | KLRG1 activity raises COPS8-DT's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without KLRG1 | 0.027 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[RPAP2]] | B | KLRG1 activity raises RPAP2's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without KLRG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[C16orf95]] | B | KLRG1 activity raises C16orf95's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.70× lower at baseline in the lines without KLRG1 | 0.041 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[MMACHC]] | B | KLRG1 activity raises MMACHC's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.31× lower at baseline in the lines without KLRG1 | 0.042 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[SYT9-AS1]] | B | KLRG1 activity raises SYT9-AS1's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without KLRG1 | 0.055 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[SEMA6A-AS1]] | B | KLRG1 activity raises SEMA6A-AS1's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without KLRG1 | 0.084 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[TMC3-AS1]] | B | KLRG1 activity raises TMC3-AS1's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without KLRG1 | 0.085 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |
| [[ZNF232-AS1]] | B | KLRG1 activity raises ZNF232-AS1's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without KLRG1 | 0.090 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.353). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.3, 28.4); signed map (36.8, 16.4). **Vector** length 42.8, 6.12% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +4.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.3 |
|  | [[Cytarabine (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | killer cell lectin like receptor G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:8,950,044-9,010,760 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAFA, 2F1, MAFA-L, CLEC15A |
| Gene groups (HGNC) | Killer cell lectin like receptors; C-type lectin domain containing |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E93](https://www.uniprot.org/uniprotkb/Q96E93) (Killer cell lectin-like receptor subfamily G member 1):

> Plays an inhibitory role on natural killer (NK) cells and T-cell functions upon binding to their non-MHC ligands. May mediate missing self recognition by binding to a highly conserved site on classical cadherins, enabling it to monitor expression of E-cadherin/CDH1, N-cadherin/CDH2 and R-cadherin/CDH4 on target cells.

**Summary**, from NCBI Gene [10219](https://www.ncbi.nlm.nih.gov/gene/10219):

> Natural killer (NK) cells are lymphocytes that can mediate lysis of certain tumor cells and virus-infected cells without previous activation. They can also regulate specific humoral and cell-mediated immunity. The protein encoded by this gene belongs to the killer cell lectin-like receptor (KLR) family, which is a group of transmembrane proteins preferentially expressed in NK cells. Studies in mice suggested that the expression of this gene may be regulated by MHC class I molecules. [provided …

**Accessions** — [HGNC:6380](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6380) · Entrez [10219](https://www.ncbi.nlm.nih.gov/gene/10219) · UniProt [Q96E93](https://www.uniprot.org/uniprotkb/Q96E93) · Ensembl [ENSG00000139187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139187)

## Data

Gene col 6275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6275); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6275]; `tensor/DDL_lfc|DDL_z.npy` [6275]; `embed/gene_vectors.npy` [6275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6275 or target_col == 6275). Every well: [[KLRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
