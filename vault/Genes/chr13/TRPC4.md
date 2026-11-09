---
symbol: "TRPC4"
type: "gene"
col: 5416
ensembl_id: "ENSG00000133107"
name: "transient receptor potential cation channel subfamily C member 4"
location: "13q13.3"
module: 121
arm: "+"
pooled_cpm: 16.64
n_lines_expressing: 18
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 12
direction_downstream: 23
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# TRPC4

*transient receptor potential cation channel subfamily C member 4* — 13q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.96× (z +12.7, q 5e-34, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +9.9, q 7e-21, up in 0 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.616× (z -5.4, q 3e-05, down in 8 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZEB2]] (+0.67, fdr 7e-06), [[GPR176]] (+0.64, fdr 1e-05), [[TEX41]] (+0.61, fdr 8e-06).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SCN3A]] → it (grade C ⚠); 23 go from it, the strongest it → [[FMN2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +12.7 | 5e-34 | 0/12 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.83×** | +10.0 | 5e-21 | 9/15 (NCI-H23, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +9.9 | 7e-21 | 0/13 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +8.2 | 4e-14 | 1/11 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +7.3 | 4e-11 | 0/10 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +5.8 | 8e-07 | 12/16 (NCI-H460, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +5.6 | 2e-06 | 5/16 (A498, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.50×** | +4.7 | 2e-04 | 8/15 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.6 | 3e-04 | 4/15 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.0 | 0.004 | 3/10 (NCI-H2030, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.005 | 4/15 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.005 | 4/16 (NCI-H2030, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.024 | 3/16 (NCI-H2030, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.024 | 4/16 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.036 | 0/15 | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.045 | 8/15 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.063 | 1/15 (SNU-423) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.44×** | +3.0 | 0.069 | 0/16 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.616×** | -5.4 | 3e-05 | 8/15 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.657×** | -4.9 | 3e-04 | 11/16 (hTERT-HPNE, NCI-H661, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.735×** | -3.6 | 0.052 | 9/16 (hTERT-HPNE, A498, …) | two highest doses | position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -3.6 | 0.052 | 1/16 (hTERT-HPNE) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.732×** | -3.4 | 0.076 | 0/16 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.076 | 2/16 (RPMI-7951, NCI-H661) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.753×** | -3.3 | 0.076 | 2/16 (A498, NCI-H460) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -3.3 | 0.076 | 6/16 (hTERT-HPNE, A-427, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.764× | -3.1 | 0.11 | 6/16 (J82, NCI-H23, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.768× | -3.1 | 0.12 | 10/16 (A-172, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.832× | -3.0 | 0.13 | 7/16 (NCI-H460, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 220 | 0 | 15 (11 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0838× (z -13.8) |
| [[A498 (line)]] | wt | 91.3 | 0 | 9 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 22.1 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 7.06× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 82.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -8.8) |
| [[J82 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 16.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.8× (z +20.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H661 (line)]] | alt | 84.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0523× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0710× (z -10.2) |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.105× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 5.51 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0765× (z -8.6) |
| [[A-172 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZEB2]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[GPR176]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[TEX41]] | +0.61 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[RBMS3]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ITGBL1]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP24]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MSR1]] | +0.57 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLC8A1]] | +0.57 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[STARD13]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[MYPN]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[LINC02492]] | +0.55 | +0.47 / +0.40 | both halves | 4e-05 |  |
| [[NGF]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCN3A]] | C | SCN3A activity raises TRPC4's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 5.65× lower at baseline in the lines without SCN3A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises TRPC4's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.75× lower at baseline in the lines without FMN2 | 0.004 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises TRPC4's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.83× lower at baseline in the lines without EPHA5 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[CDH10]] | C | CDH10 activity raises TRPC4's level | lines that do not express CDH10 (37) vs lines expressing it (13) | 5.03× lower at baseline in the lines without CDH10 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01035, FUT9, KCNH5; co-absent with the target |
| [[FAP]] | C | FAP activity raises TRPC4's level | lines that do not express FAP (25) vs lines expressing it (25) | 3.16× lower at baseline in the lines without FAP | 0.018 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |
| [[PSG5]] | C | PSG5 activity raises TRPC4's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 4.11× lower at baseline in the lines without PSG5 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486; co-absent with the target |
| [[INHBA]] | C | INHBA activity raises TRPC4's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.22× lower at baseline in the lines without INHBA | 0.065 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3; co-absent with the target |
| [[DMD]] | C | DMD activity raises TRPC4's level | lines that do not express DMD (18) vs lines expressing it (32) | 4.00× lower at baseline in the lines without DMD | 0.066 | ⚠ within organs, on part of the lines; also absent: KCTD16, NREP, PRKD1; maybe low, not absent; co-absent with the target |
| [[APBB1IP]] | C | APBB1IP activity raises TRPC4's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 5.56× lower at baseline in the lines without APBB1IP | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises TRPC4's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 2.15× lower at baseline in the lines without PRRX1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises TRPC4's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 4.85× lower at baseline in the lines without NETO1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises TRPC4's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.33× lower at baseline in the lines without MSC-AS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMN2]] | C | TRPC4 activity raises FMN2's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.76× lower at baseline in the lines without TRPC4 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[EPHA5]] | C | TRPC4 activity raises EPHA5's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 6.73× lower at baseline in the lines without TRPC4 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[SCN3A]] | C | TRPC4 activity raises SCN3A's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.46× lower at baseline in the lines without TRPC4 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[NALF1]] | C | TRPC4 activity raises NALF1's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.38× lower at baseline in the lines without TRPC4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[INHBA]] | C | TRPC4 activity raises INHBA's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 4.78× lower at baseline in the lines without TRPC4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[PDE3A]] | C | TRPC4 activity raises PDE3A's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.82× lower at baseline in the lines without TRPC4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[BNC2]] | C | TRPC4 activity raises BNC2's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.37× lower at baseline in the lines without TRPC4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[SLC8A1]] | C | TRPC4 activity raises SLC8A1's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 6.49× lower at baseline in the lines without TRPC4 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[CDH10]] | C | TRPC4 activity raises CDH10's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.38× lower at baseline in the lines without TRPC4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[FAP]] | C | TRPC4 activity raises FAP's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.61× lower at baseline in the lines without TRPC4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[ZNF804A]] | C | TRPC4 activity raises ZNF804A's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 6.68× lower at baseline in the lines without TRPC4 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[GREM1]] | C | TRPC4 activity raises GREM1's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 2.63× lower at baseline in the lines without TRPC4 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.1, 24.6); signed map (42.0, 25.5). **Vector** length 56.8, 16.2% of its response variance represented; |z| ≥ 3 in 483 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.9 | +10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +3.3 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily C member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.3 — chr13:37,632,063-37,869,802 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HTRP4, TRP4 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Transient receptor potential cation channel subfamily C |
| Reactome | 8 pathways, smallest: Role of second messengers in netrin-1 signaling; TRP channels; Netrin-1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBN4](https://www.uniprot.org/uniprotkb/Q9UBN4) (Short transient receptor potential channel 4):

> Forms a receptor-activated non-selective calcium permeant cation channel. Acts as a cell-cell contact-dependent endothelial calcium entry channel. Forms a homomeric ion channel or a heteromeric ion channel with TRPC1; the heteromeric ion channel has reduced calcium permeability compared to the homomeric channel. Also permeable to monovalent ions including sodium, lithium and cesium ions.; [Isoform Beta]: Forms a receptor-activated non-selective calcium permeant cation channel.

**Summary**, from NCBI Gene [7223](https://www.ncbi.nlm.nih.gov/gene/7223):

> This gene encodes a member of the canonical subfamily of transient receptor potential cation channels. The encoded protein forms a non-selective calcium-permeable cation channel that is activated by Gq-coupled receptors and tyrosine kinases, and plays a role in multiple processes including endothelial permeability, vasodilation, neurotransmitter release and cell proliferation. Single nucleotide polymorphisms in this gene may be associated with generalized epilepsy with photosensitivity. …

**Accessions** — [HGNC:12336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12336) · Entrez [7223](https://www.ncbi.nlm.nih.gov/gene/7223) · UniProt [Q9UBN4](https://www.uniprot.org/uniprotkb/Q9UBN4) · Ensembl [ENSG00000133107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133107)

## Data

Gene col 5416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5416); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5416]; `tensor/DDL_lfc|DDL_z.npy` [5416]; `embed/gene_vectors.npy` [5416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5416 or target_col == 5416). Every well: [[TRPC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
