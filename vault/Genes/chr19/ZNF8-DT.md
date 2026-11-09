---
symbol: "ZNF8-DT"
type: "gene"
col: 15601
ensembl_id: "ENSG00000268516"
name: "ZNF8 divergent transcript"
location: "19q13.43"
module: 103
arm: "+"
pooled_cpm: 11.7
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# ZNF8-DT

*ZNF8 divergent transcript* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.28× (z +6.1, q 7e-07, up in 17 of 48 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.540× (z -15.1, q 0e+00, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF404]] (+0.64, fdr 7e-06), [[TMEM134]] (+0.62, fdr 7e-06), [[GUK1]] (+0.61, fdr 7e-06); moves opposite to [[GSPT1]] (-0.57, fdr 1e-05), [[MYO5C]] (-0.57, fdr 2e-05), [[DENND2D]] (-0.55, fdr 4e-05).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MPP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15601.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +6.1 | 7e-07 | 17/48 (LS 180, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.28×** | +4.4 | 0.003 | 8/43 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.21× | +3.3 | 0.12 | 6/40 (SW 900, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.28× | +3.3 | 0.12 | 4/41 (PANC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.21× | +3.3 | 0.12 | 12/39 (NCI-H2347, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.29× | +3.2 | 0.13 | 6/41 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimitespib (drug)]] 5 µM |  | 1.40× | +3.1 | 0.17 | 4/33 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15601.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.540×** | -15.1 | 0e+00 | 36/46 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.507×** | -11.8 | 1e-29 | 35/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.504×** | -11.5 | 4e-28 | 28/46 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.514×** | -11.1 | 1e-26 | 23/40 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.586×** | -9.3 | 2e-18 | 29/45 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.602×** | -8.8 | 1e-16 | 32/47 (LOX-IMVI, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.641×** | -7.7 | 9e-13 | 23/47 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.712×** | -5.9 | 3e-07 | 19/46 (NCI-H2030, SW 900, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.715×** | -5.8 | 4e-07 | 21/44 (SNU-423, C-33 A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.730×** | -5.5 | 3e-06 | 15/48 (NCI-H1792, C32, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.743×** | -5.2 | 1e-05 | 16/48 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.573×** | -5.1 | 2e-05 | 13/46 (A-172, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.752×** | -4.9 | 3e-05 | 17/46 (H4, CHP-212, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.767×** | -4.6 | 2e-04 | 14/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.764×** | -4.4 | 4e-04 | 14/47 (PANC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -4.2 | 9e-04 | 9/43 (hTERT-HPNE, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.674×** | -3.6 | 0.011 | 7/47 (NCI-H1792, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.834× | -3.1 | 0.047 | 2/48 (NCI-H460, A-172) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15601. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 23.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0583× (z -15.8) |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.172× (z -10.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 15.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 8.16 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.167× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 31.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0597× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 9.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.5) |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.398× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.0) |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -10.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -9.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -8.9) |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0686× (z -8.6) |
| [[C32 (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.1) |
| [[H4 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0870× (z -8.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.9) |
| [[LS 180 (line)]] | wt | 8.80 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0993× (z -8.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 7.99 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0550× (z -13.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 6.52 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0978× (z -8.7) ⚠ toxic; unreliable plate only |
| [[SHP-77 (line)]] | alt | 6.91 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.109× (z -9.0) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 4.29 | 0 | 1 | — | [[Tolmetin (drug)]] 5 µM 0.0659× (z -9.1) |
| [[A498 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15601), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF404]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TMEM134]] | +0.62 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[GUK1]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[LZTS2]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[LINC03047]] | +0.60 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SLC35E3]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RNF122]] | +0.57 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[C4orf47]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[EPOR]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[UPK1A-AS1]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[LINC02256]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PPFIA4]] | +0.56 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT1]] | -0.57 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[MYO5C]] | -0.57 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DENND2D]] | -0.55 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[TJP1]] | -0.55 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PKP4]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[POU5F1B]] | -0.51 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[PTPRK]] | -0.50 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SYK]] | -0.50 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[CDC42BPA]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[XRCC5]] | -0.49 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[FAT1]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[WWC3]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP2]] | B | MPP2 activity raises ZNF8-DT's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without MPP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[ANXA3]] | B | ANXA3 activity lowers ZNF8-DT's level | lines that do not express ANXA3 (24) vs lines expressing it (26) | 1.74× higher at baseline in the lines without ANXA3 | 0.040 | ⚠ within organs, on part of the lines; also absent: RNF223, P2RY2, C6orf132 |
| [[SYK]] | B | SYK activity lowers ZNF8-DT's level | lines that do not express SYK (30) vs lines expressing it (20) | 1.77× higher at baseline in the lines without SYK | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.8, -5.0); signed map (-30.6, 29.5). **Vector** length 62.0, 9.14% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.5 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +2.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.0 | -11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | -1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.2 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.0 | -15.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -11.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -1.4 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ZNF8 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.43 — chr19:58,257,270-58,278,830 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55280) · Entrez [105372482](https://www.ncbi.nlm.nih.gov/gene/105372482) · Ensembl [ENSG00000268516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268516)

## Data

Gene col 15601: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15601); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15601, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15601]; `tensor/DDL_lfc|DDL_z.npy` [15601]; `embed/gene_vectors.npy` [15601]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15601 or target_col == 15601). Every well: [[ZNF8-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF8-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
