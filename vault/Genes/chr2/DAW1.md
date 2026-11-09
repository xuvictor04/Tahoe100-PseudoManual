---
symbol: "DAW1"
type: "gene"
col: 4467
ensembl_id: "ENSG00000123977"
name: "dynein assembly factor with WD repeats 1"
location: "2q36.3"
module: 120
arm: "+"
pooled_cpm: 5.42
n_lines_expressing: 16
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# DAW1

*dynein assembly factor with WD repeats 1* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 6.02× (z +11.6, q 2e-28, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.02× (z +6.9, q 6e-10, up in 10 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.187×, NCI-H23 0.286×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.132×; ⚠ cell-cycle shift, explains ~59% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.0787×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (J82 0.0713×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCBE1]] (+0.62, fdr 7e-06), [[DLC1]] (+0.56, fdr 1e-05), [[PRKG1-AS1]] (+0.56, fdr 1e-05); moves opposite to [[ACOX1]] (-0.51, fdr 3e-05), [[MRPS6]] (-0.50, fdr 1e-04), [[SLC5A3]] (-0.49, fdr 1e-04).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[ELK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4467.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.02×** | +11.6 | 2e-28 | 3/6 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.46×** | +10.5 | 3e-23 | 1/7 (HOP62) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.04×** | +9.4 | 1e-18 | 0/4 | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +6.9 | 6e-10 | 10/13 (HOP62, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.3 | 1e-05 | 0/12 | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.13×** | +5.3 | 1e-05 | 5/13 (HOP62, A-172, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.2 | 1e-05 | 5/13 (A498, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.9 | 5e-05 | 1/9 (HOP62) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +4.9 | 7e-05 | 6/13 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.96×** | +4.7 | 2e-04 | 3/13 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.91×** | +4.5 | 3e-04 | 1/13 (HOP62) | all doses, flat |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.43×** | +4.5 | 3e-04 | 3/5 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.85×** | +4.3 | 8e-04 | 6/13 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 5/13 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **2.06×** | +3.6 | 0.012 | 4/11 (NCI-H460, A-427, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.64×** | +3.4 | 0.021 | 3/12 (NCI-H460, J82, …) | two highest doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.022 | 4/13 (HOP62, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.98×** | +3.4 | 0.022 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.077 | 0/13 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +2.9 | 0.081 | 2/13 (NCI-H460, HOP62) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.52×** | +2.9 | 0.081 | 4/13 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4467.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.187×, NCI-H23 0.286×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.132×; ⚠ cell-cycle shift, explains ~59% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.0787×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (J82 0.0713×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pimozide (drug)]] 5 µM |  | 0.643× | -3.1 | 0.36 | 1/13 (A-172) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.645× | -3.1 | 0.36 | 7/13 (J82, LOX-IMVI, …) | top dose only |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 0.645× | -3.1 | 0.36 | 2/13 (NCI-H460, SNU-423) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4467. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 30.5 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0787× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 61.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.84× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -20.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -16.9) |
| [[J82 (line)]] | alt | 6.94 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0713× (z -8.9) |
| [[A-172 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.967 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.834 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.667 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.496 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.506 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4467), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCBE1]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[DLC1]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PRKG1-AS1]] | +0.56 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[DDAH1]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LNCOG]] | +0.54 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[CCN1]] | +0.53 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[EPGN]] | +0.52 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[BDNF]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CCN2]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[LINC02742]] | +0.52 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[KCNG2]] | +0.51 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[WWC1]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOX1]] | -0.51 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[MRPS6]] | -0.50 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[SLC5A3]] | -0.49 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[LINC00310]] | -0.47 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[ATP6V1G1]] | -0.43 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[SYNRG]] | -0.42 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[EPB41]] | -0.41 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[MICU1]] | -0.41 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[OPTN]] | -0.41 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[UMAD1]] | -0.40 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[ZFYVE1]] | -0.40 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[IGFBP6]] | -0.39 | -0.40 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELK3]] | B | DAW1 activity raises ELK3's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 1.94× lower at baseline in the lines without DAW1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |
| [[HSF2BP]] | B | DAW1 activity raises HSF2BP's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 1.71× lower at baseline in the lines without DAW1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |
| [[ITPRIP]] | B | DAW1 activity raises ITPRIP's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 1.72× lower at baseline in the lines without DAW1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |
| [[SRGAP1]] | B | DAW1 activity raises SRGAP1's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without DAW1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |
| [[ODAD2]] | C | DAW1 activity raises ODAD2's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without DAW1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227; co-absent with the target |
| [[MARCHF4]] | C | DAW1 activity raises MARCHF4's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 4.80× lower at baseline in the lines without DAW1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227; co-absent with the target |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.0, 12.4); signed map (14.2, 40.2). **Vector** length 35.6, 9.39% of its response variance represented; |z| ≥ 3 in 335 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.1 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +2.8 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | dynein assembly factor with WD repeats 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:227,871,054-227,924,344 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25955, ODA16, DNAAF18; previously WDR69 |
| Gene groups (HGNC) | WD repeat domain containing; Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N136](https://www.uniprot.org/uniprotkb/Q8N136) (Dynein assembly factor with WD repeat domains 1):

> Required for axonemal dynein assembly and ciliary motility in ciliated organs, including Kupffer's vesicle, during embryogenesis. Facilitates the onset of robust cilia motility during development.

**Summary**, from NCBI Gene [164781](https://www.ncbi.nlm.nih.gov/gene/164781):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in protein polyubiquitination. Predicted to act upstream of with a positive effect on outer dynein arm assembly. Predicted to act upstream of or within with a positive effect on intraciliary transport. Predicted to act upstream of or within cerebrospinal fluid circulation; determination of left/right symmetry; and heart development. Predicted to be located in ciliary basal body. Predicted to be part …

**Accessions** — [HGNC:26383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26383) · Entrez [164781](https://www.ncbi.nlm.nih.gov/gene/164781) · UniProt [Q8N136](https://www.uniprot.org/uniprotkb/Q8N136) · Ensembl [ENSG00000123977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123977)

## Data

Gene col 4467: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4467); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4467, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4467]; `tensor/DDL_lfc|DDL_z.npy` [4467]; `embed/gene_vectors.npy` [4467]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4467 or target_col == 4467). Every well: [[DAW1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAW1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
