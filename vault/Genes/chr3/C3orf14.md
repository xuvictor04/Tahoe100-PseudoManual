---
symbol: "C3orf14"
type: "gene"
col: 3550
ensembl_id: "ENSG00000114405"
name: "centrosomal protein 15"
location: "3p14.2"
module: 17
arm: "+"
pooled_cpm: 8.0
n_lines_expressing: 38
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# C3orf14

*centrosomal protein 15* — 3p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.73× (z +12.7, q 2e-34, up in 12 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.42× (z +6.5, q 8e-09, up in 18 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.472× (z -5.2, q 1e-04, down in 13 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESD]] (+0.56, fdr 3e-05), [[COMMD8]] (+0.56, fdr 5e-05), [[SAAL1]] (+0.55, fdr 4e-05); moves opposite to [[MFNG]] (-0.52, fdr 2e-05), [[TRPV1]] (-0.48, fdr 0.002, ⚠ one half only (not replicated)), [[NPIPB11]] (-0.48, fdr 4e-04), [[TNXB]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PTPRG-AS1]] → it (grade C ⚠); 3 go from it, the strongest it → [[PTAR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3550.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +12.7 | 2e-34 | 12/14 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +8.6 | 3e-15 | 18/27 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.5 | 2e-11 | 20/28 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +6.5 | 8e-09 | 18/35 (SW1417, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.8 | 6e-07 | 10/19 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 5e-04 | 13/35 (HOP62, J82, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.4 | 9e-04 | 9/25 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.006 | 10/34 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.007 | 10/33 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.007 | 10/35 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.008 | 3/34 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.009 | 11/33 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.011 | 11/35 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.017 | 9/33 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.28×** | +3.2 | 0.044 | 7/35 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +3.1 | 0.068 | 2/35 (SW 900, J82) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.080 | 7/34 (NCI-H2347, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3550.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -5.2 | 1e-04 | 13/31 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -4.4 | 0.003 | 13/34 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.729×** | -4.1 | 0.005 | 10/34 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.729×** | -4.1 | 0.005 | 11/35 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.607×** | -3.4 | 0.069 | 14/33 (RPMI-7951, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.784× | -3.2 | 0.14 | 9/34 (J82, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fusidic acid (drug)]] 5 µM |  | 0.848× | -3.0 | 0.19 | 6/36 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3550. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.96 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0850× (z -9.2) |
| [[A-427 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 5.18 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0724× (z -9.1) |
| [[SW 900 (line)]] | alt | 5.19 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0874× (z -8.5) |
| [[A498 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.635 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.06 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3550), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESD]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[COMMD8]] | +0.56 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[SAAL1]] | +0.55 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[ASNSD1]] | +0.51 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[VRK2]] | +0.50 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[PIGB]] | +0.50 | +0.36 / +0.48 | both halves | 1e-04 |  |
| [[WDR11]] | +0.49 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[COMMD2]] | +0.49 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[MRPL16]] | +0.49 | +0.36 / +0.44 | both halves | 1e-04 |  |
| [[ACTR10]] | +0.49 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[HUS1]] | +0.49 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[TRAPPC11]] | +0.49 | +0.37 / +0.51 | both halves | 9e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFNG]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[TRPV1]] | -0.48 | -0.14 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[NPIPB11]] | -0.48 | -0.24 / -0.51 | both halves | 4e-04 |  |
| [[TNXB]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[COL20A1]] | -0.47 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[SLC23A3]] | -0.46 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[GAL3ST2]] | -0.45 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[CASTOR3P]] | -0.45 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[DMPK]] | -0.44 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[DNHD1]] | -0.44 | -0.16 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[ASIC4]] | -0.43 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ELL]] | -0.42 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[ZMIZ1-AS1]] | -0.42 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[UBAP1L]] | -0.42 | -0.22 / -0.46 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRG-AS1]] | C | PTPRG-AS1 activity raises C3orf14's level | lines that do not express PTPRG-AS1 (10) vs lines expressing it (40) | 4.33× lower at baseline in the lines without PTPRG-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: C3orf14, RECK, PCLO; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTAR1]] | B | C3orf14 activity raises PTAR1's level | lines that do not express C3orf14 (12) vs lines expressing it (38) | 1.29× lower at baseline in the lines without C3orf14 | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPRG-AS1, EVC, WIPF1; maybe low, not absent |
| [[PTPRG-AS1]] | C | C3orf14 activity raises PTPRG-AS1's level | lines that do not express C3orf14 (12) vs lines expressing it (38) | 3.73× lower at baseline in the lines without C3orf14 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTPRG-AS1, EVC, WIPF1; maybe low, not absent; co-absent with the target |
| [[MAP2]] | C | C3orf14 activity raises MAP2's level | lines that do not express C3orf14 (12) vs lines expressing it (38) | 3.96× lower at baseline in the lines without C3orf14 | 0.050 | ⚠ within organs, on part of the lines; also absent: PTPRG-AS1, EVC, WIPF1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.497). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.1, -1.7); signed map (5.8, -36.0). **Vector** length 46.0, 6.81% of its response variance represented; |z| ≥ 3 in 621 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +8.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.2 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +3.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -0.8 | -0.7 |
|  | [[Lucanthone (drug)]] 5 µM |  | -0.8 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.2 — chr3:62,319,015-62,336,213 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HT021; previously C3orf14 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBI5](https://www.uniprot.org/uniprotkb/Q9HBI5) (Centrosomal protein 15):

> May play a role in ciliary assembly.

**Summary**, from NCBI Gene [57415](https://www.ncbi.nlm.nih.gov/gene/57415):

> Predicted to be located in cilium. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25024](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25024) · Entrez [57415](https://www.ncbi.nlm.nih.gov/gene/57415) · UniProt [Q9HBI5](https://www.uniprot.org/uniprotkb/Q9HBI5) · Ensembl [ENSG00000114405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114405)

## Data

Gene col 3550: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3550); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3550, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3550]; `tensor/DDL_lfc|DDL_z.npy` [3550]; `embed/gene_vectors.npy` [3550]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3550 or target_col == 3550). Every well: [[C3orf14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
