---
symbol: "SCUBE1"
type: "gene"
col: 8242
ensembl_id: "ENSG00000159307"
name: "signal peptide, CUB domain and EGF like domain containing 1"
location: "22q13.2"
module: 19
arm: "+"
pooled_cpm: 4.2
n_lines_expressing: 22
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 24
direction_downstream: 8
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SCUBE1

*signal peptide, CUB domain and EGF like domain containing 1* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +9.9, q 4e-20, up in 2 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.541× (z -4.5, q 0.004, down in 8 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0946×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.0878×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0755×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H460 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.243×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC5D]] (+0.74, fdr 7e-06), [[PLAC4]] (+0.71, fdr 7e-06), [[PAK3]] (+0.69, fdr 1e-05); moves opposite to [[DGKH]] (-0.49, fdr 1e-04), [[NEXN]] (-0.49, fdr 2e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[PDE10A]] → it (grade B ⚠); 8 go from it, the strongest it → [[SFRP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +9.9 | 4e-20 | 2/14 (PANC-1, A549) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.86×** | +9.8 | 5e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.35×** | +9.1 | 2e-17 | 14/18 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.71×** | +7.5 | 1e-11 | 13/18 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +6.9 | 7e-10 | 2/11 (PANC-1, NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +6.8 | 7e-10 | 12/17 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +5.8 | 6e-07 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.66×** | +5.2 | 1e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +4.8 | 1e-04 | 10/18 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.88×** | +4.7 | 1e-04 | 11/18 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.07×** | +4.4 | 5e-04 | 0/5 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.22×** | +4.3 | 9e-04 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.8 | 0.007 | 3/15 (SNU-423, NCI-H460, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +3.7 | 0.008 | 9/16 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.66×** | +3.5 | 0.018 | 0/14 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.035 | 1/14 (SW 900) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.049 | 5/16 (NCI-H460, HOP62, …) | two highest doses | low cells (technical?) |
| [[Menadione (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.050 | 2/15 (NCI-H460, NCI-H1792) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.086 | 0/13 | top dose only | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.48×** | +2.9 | 0.096 | 0/16 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8242.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0946×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.0878×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.0755×; ⚠ toxic; transcription drop); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (NCI-H460 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.243×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.541×** | -4.5 | 0.004 | 8/15 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.609× | -3.5 | 0.10 | 4/18 (NCI-H460, SNU-1, …) | all doses, flat |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.619× | -3.4 | 0.10 | 0/18 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.650× | -3.3 | 0.10 | 5/18 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.703× | -3.3 | 0.10 | 5/17 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.652× | -3.3 | 0.10 | 7/18 (NCI-H460, HOP62, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.657× | -3.2 | 0.10 | 2/16 (NCI-H460, SHP-77) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.659× | -3.2 | 0.10 | 9/17 (HOP62, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.746× | -3.1 | 0.12 | 5/18 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.674× | -3.0 | 0.15 | 5/18 (NCI-H460, SHP-77, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 33.5 | 0 | 11 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0946× (z -11.7) |
| [[SHP-77 (line)]] | alt | 54.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0755× (z -11.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0845× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.745 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.554 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC5D]] | +0.74 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PLAC4]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PAK3]] | +0.69 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[CNTN1]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SLITRK4]] | +0.68 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[NCKAP5-AS2]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 | pathway: Degradation of the extracellular matrix |
| [[SERPIND1]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RADIL]] | +0.65 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CTNND2]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[SPOCK1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SGIP1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKH]] | -0.49 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[NEXN]] | -0.49 | -0.50 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 4, C 20. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE10A]] | B | PDE10A activity raises SCUBE1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without PDE10A | 0.056 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[PLAC4]] | B | PLAC4 activity raises SCUBE1's level | lines that do not express PLAC4 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without PLAC4 | 0.070 | ⚠ within organs, on part of the lines; also absent: FAM3B, TXNIP, SNCAIP; maybe low, not absent |
| [[ISM2]] | B | ISM2 activity raises SCUBE1's level | lines that do not express ISM2 (9) vs lines expressing it (41) | 1.07× lower at baseline in the lines without ISM2 | 0.085 | ⚠ within organs, on part of the lines; also absent: DYSF, CSRP2, LINC02609; maybe low, not absent |
| [[TENM1]] | B | TENM1 activity raises SCUBE1's level | lines that do not express TENM1 (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without TENM1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, MIR4307HG |
| [[DPP10]] | C | DPP10 activity raises SCUBE1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.54× lower at baseline in the lines without DPP10 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises SCUBE1's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.01× lower at baseline in the lines without KCNE4 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[NEFM]] | C | NEFM activity raises SCUBE1's level | lines that do not express NEFM (35) vs lines expressing it (15) | 3.72× lower at baseline in the lines without NEFM | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, GTF2I-AS1, LINC03000; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises SCUBE1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.84× lower at baseline in the lines without SCARA5 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[ANGPTL2]] | C | ANGPTL2 activity raises SCUBE1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.70× lower at baseline in the lines without ANGPTL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent; co-absent with the target |
| [[RARB]] | C | RARB activity raises SCUBE1's level | lines that do not express RARB (28) vs lines expressing it (22) | 2.71× lower at baseline in the lines without RARB | 0.031 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises SCUBE1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 3.34× lower at baseline in the lines without FENDRR | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises SCUBE1's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without NCKAP5-AS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFRP1]] | C | SCUBE1 activity raises SFRP1's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 4.55× lower at baseline in the lines without SCUBE1 | 0.023 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[MEG3]] | C | SCUBE1 activity raises MEG3's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 3.97× lower at baseline in the lines without SCUBE1 | 0.052 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[PCBP3]] | C | SCUBE1 activity raises PCBP3's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 3.18× lower at baseline in the lines without SCUBE1 | 0.057 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[CRTAC1]] | C | SCUBE1 activity raises CRTAC1's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without SCUBE1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[KCNE4]] | C | SCUBE1 activity raises KCNE4's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 3.16× lower at baseline in the lines without SCUBE1 | 0.068 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[TRPV2]] | C | SCUBE1 activity raises TRPV2's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 1.67× lower at baseline in the lines without SCUBE1 | 0.091 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[PDE7B]] | C | SCUBE1 activity raises PDE7B's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without SCUBE1 | 0.092 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |
| [[KCNK3]] | C | SCUBE1 activity raises KCNK3's level | lines that do not express SCUBE1 (28) vs lines expressing it (22) | 1.75× lower at baseline in the lines without SCUBE1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NPFFR2, MEG3, GREM1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.8, 34.8); signed map (41.5, 45.2). **Vector** length 52.4, 13.8% of its response variance represented; |z| ≥ 3 in 536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.5 | +1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | signal peptide, CUB domain and EGF like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:43,197,280-43,343,372 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | APICAL_SURFACE |
| Reactome | 2 pathways, smallest: Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWY4](https://www.uniprot.org/uniprotkb/Q8IWY4) (Signal peptide, CUB and EGF-like domain-containing protein 1):

> Could function as an adhesive molecule and its matrix bound and soluble fragments may play a critical role in vascular biology.

**Summary**, from NCBI Gene [80274](https://www.ncbi.nlm.nih.gov/gene/80274):

> This gene encodes a cell surface glycoprotein that is a member of the SCUBE (signal peptide, CUB domain, EGF (epidermal growth factor)-like protein) family. Family members have an amino-terminal signal peptide, nine copies of EGF-like repeats and a CUB domain at the carboxyl terminus. This protein is expressed in platelets and endothelial cells and may play an important role in vascular biology. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:13441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13441) · Entrez [80274](https://www.ncbi.nlm.nih.gov/gene/80274) · UniProt [Q8IWY4](https://www.uniprot.org/uniprotkb/Q8IWY4) · Ensembl [ENSG00000159307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159307)

## Data

Gene col 8242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8242); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8242]; `tensor/DDL_lfc|DDL_z.npy` [8242]; `embed/gene_vectors.npy` [8242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8242 or target_col == 8242). Every well: [[SCUBE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCUBE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
