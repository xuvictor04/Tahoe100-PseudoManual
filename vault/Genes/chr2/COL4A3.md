---
symbol: "COL4A3"
type: "gene"
col: 9740
ensembl_id: "ENSG00000169031"
name: "collagen type IV alpha 3 chain"
location: "2q36.3"
module: 19
arm: "+"
pooled_cpm: 17.28
n_lines_expressing: 21
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# COL4A3

*collagen type IV alpha 3 chain* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.78× (z +16.5, q 0e+00, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.490× (z -7.8, q 4e-12, down in 15 of 18 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A4]] (+0.90, fdr 7e-06, ⚠ same locus), [[UNC5D]] (+0.56, fdr 3e-05), [[FAM124A]] (+0.55, fdr 2e-05), [[EBF2]] (+0.54, fdr 1e-05); moves opposite to [[DGLUCY]] (-0.44, fdr 1e-04), [[NR0B1]] (-0.42, fdr 3e-04), [[AOPEP]] (-0.40, fdr 5e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[DIO3OS]] → it (grade B ⚠); 11 go from it, the strongest it → [[ITGA2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.78×** | +16.5 | 0e+00 | 16/19 (NCI-H1573, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.73×** | +11.5 | 5e-28 | 16/18 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +11.1 | 3e-26 | 4/18 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.54×** | +10.6 | 4e-24 | 1/13 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +9.6 | 9e-20 | 1/11 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +4.9 | 1e-04 | 1/12 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.52×** | +4.8 | 1e-04 | 12/18 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.6 | 4e-04 | 8/18 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.002 | 6/18 (A-172, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.037 | 5/18 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.075 | 1/18 (A-172) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.30× | +3.0 | 0.12 | 4/18 (A549, NCI-H1573, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.490×** | -7.8 | 4e-12 | 15/18 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -7.5 | 2e-11 | 16/18 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.615×** | -5.5 | 7e-06 | 9/18 (NCI-H460, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.629×** | -5.3 | 2e-05 | 15/18 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.644×** | -5.0 | 8e-05 | 9/18 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.677×** | -4.4 | 0.001 | 17/18 (NCI-H460, NCI-H1573, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.688×** | -4.2 | 0.002 | 14/19 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.717×** | -3.8 | 0.012 | 12/17 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.804×** | -3.5 | 0.032 | 17/18 (A549, HEC-1-A, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.7 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -22.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0829× (z -18.1) |
| [[HEC-1-A (line)]] | alt | 141 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -25.1) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -15.8) |
| [[A549 (line)]] | wt | 81.7 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0497× (z -28.8) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0675× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 42.6 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.54× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -10.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0586× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -12.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0635× (z -12.4) |
| [[SW480 (line)]] | alt | 9.18 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -11.3) |
| [[A-172 (line)]] | wt | 13.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[LoVo (line)]] | wt | 10.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -10.8) |
| [[A-427 (line)]] | wt | 5.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0781× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.89 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A4]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | same gene group; pathway: Anchoring fibril formation; STRING 995; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[UNC5D]] | +0.56 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[FAM124A]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[EBF2]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TMEM170B]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LRRC63]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[SSPOP]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SLITRK4]] | +0.52 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[ST6GAL2]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[KIAA0319]] | +0.51 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[EYA2]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CACNA2D3]] | +0.50 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[SPANXA2-OT1]] | +0.50 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGLUCY]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[NR0B1]] | -0.42 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[AOPEP]] | -0.40 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 6, C 9. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIO3OS]] | B | DIO3OS activity raises COL4A3's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.04× lower at baseline in the lines without DIO3OS | 0.032 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |
| [[EBF2]] | B | EBF2 activity raises COL4A3's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without EBF2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[NR2E3]] | B | NR2E3 activity raises COL4A3's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without NR2E3 | 0.060 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[FAM124A]] | B | FAM124A activity raises COL4A3's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without FAM124A | 0.079 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1 |
| [[SSPOP]] | B | SSPOP activity raises COL4A3's level | lines that do not express SSPOP (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without SSPOP | 0.083 | ⚠ within organs, on part of the lines; also absent: SPDYE10, LRRC4B, AP3B2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers COL4A3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[COL4A4]] | C | COL4A4 activity raises COL4A3's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 5.04× lower at baseline in the lines without COL4A4 | 1e-04 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A; co-absent with the target |
| [[RADIL]] | C | RADIL activity raises COL4A3's level | lines that do not express RADIL (21) vs lines expressing it (29) | 3.10× lower at baseline in the lines without RADIL | 0.012 | ⚠ within organs, on part of the lines; also absent: ZYG11A, OLFM1, JAKMIP1; maybe low, not absent; co-absent with the target |
| [[NR0B1]] | C | NR0B1 activity raises COL4A3's level | lines that do not express NR0B1 (38) vs lines expressing it (12) | 4.33× lower at baseline in the lines without NR0B1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, CDH19, TBXT; co-absent with the target |
| [[CDH19]] | C | CDH19 activity raises COL4A3's level | lines that do not express CDH19 (40) vs lines expressing it (10) | 3.84× lower at baseline in the lines without CDH19 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, TBXT, LINC01425; co-absent with the target |
| [[SLAIN1]] | C | SLAIN1 activity raises COL4A3's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.56× lower at baseline in the lines without SLAIN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2; co-absent with the target |
| [[NRXN3]] | C | NRXN3 activity raises COL4A3's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 2.13× lower at baseline in the lines without NRXN3 | 0.069 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2B]] | B | COL4A3 activity raises ITGA2B's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without COL4A3 | 0.015 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[GALNT16]] | B | COL4A3 activity raises GALNT16's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without COL4A3 | 0.022 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[FAM124A]] | B | COL4A3 activity raises FAM124A's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.11× lower at baseline in the lines without COL4A3 | 0.027 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[EBF2]] | B | COL4A3 activity raises EBF2's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 1.78× lower at baseline in the lines without COL4A3 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[COL4A4]] | C | COL4A3 activity raises COL4A4's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 5.32× lower at baseline in the lines without COL4A3 | 1e-04 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[PRKAA2]] | C | COL4A3 activity raises PRKAA2's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 3.18× lower at baseline in the lines without COL4A3 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[EPB41L4A]] | C | COL4A3 activity raises EPB41L4A's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 3.24× lower at baseline in the lines without COL4A3 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[HORMAD1]] | C | COL4A3 activity raises HORMAD1's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without COL4A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[LGSN]] | C | COL4A3 activity raises LGSN's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.66× lower at baseline in the lines without COL4A3 | 0.035 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[LRRC63]] | C | COL4A3 activity raises LRRC63's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without COL4A3 | 0.039 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |
| [[SLAIN1]] | C | COL4A3 activity raises SLAIN1's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without COL4A3 | 0.088 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.464). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.8, 39.4); signed map (39.7, 47.3). **Vector** length 72.8, 23.9% of its response variance represented; |z| ≥ 3 in 584 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +16.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +10.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.3 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -7.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.2 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | collagen type IV alpha 3 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:227,164,624-227,314,792 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Network forming collagens |
| Reactome | 24 pathways, smallest: Anchoring fibril formation; Crosslinking of collagen fibrils; Fibronectin matrix formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01955](https://www.uniprot.org/uniprotkb/Q01955) (Collagen alpha-3(IV) chain):

> Type IV collagen is the major structural component of glomerular basement membranes (GBM), forming a 'chicken-wire' meshwork together with laminins, proteoglycans and entactin/nidogen.; Tumstatin, a cleavage fragment corresponding to the collagen alpha 3(IV) NC1 domain, possesses both anti-angiogenic and anti-tumor cell activity; these two anti-tumor properties may be regulated via RGD-independent ITGB3-mediated mechanisms.

**Summary**, from NCBI Gene [1285](https://www.ncbi.nlm.nih.gov/gene/1285):

> Type IV collagen, the major structural component of basement membranes, is a multimeric protein composed of 3 alpha subunits. These subunits are encoded by 6 different genes, alpha 1 through alpha 6, each of which can form a triple helix structure with 2 other subunits to form type IV collagen. This gene encodes alpha 3. In the Goodpasture syndrome, autoantibodies bind to the collagen molecules in the basement membranes of alveoli and glomeruli. The epitopes that elicit these autoantibodies are …

**Accessions** — [HGNC:2204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2204) · Entrez [1285](https://www.ncbi.nlm.nih.gov/gene/1285) · UniProt [Q01955](https://www.uniprot.org/uniprotkb/Q01955) · Ensembl [ENSG00000169031](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169031)

## Data

Gene col 9740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9740); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9740]; `tensor/DDL_lfc|DDL_z.npy` [9740]; `embed/gene_vectors.npy` [9740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9740 or target_col == 9740). Every well: [[COL4A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL4A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
