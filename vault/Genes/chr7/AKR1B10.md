---
symbol: "AKR1B10"
type: "gene"
col: 12524
ensembl_id: "ENSG00000198074"
name: "aldo-keto reductase family 1 member B10"
location: "7q33"
module: 44
arm: "+"
pooled_cpm: 19.66
n_lines_expressing: 9
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 24
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# AKR1B10

*aldo-keto reductase family 1 member B10* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 13.8× (z +17.2, q 0e+00, up in 7 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.13× (z +4.9, q 1e-04, up in 4 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.0687×, NCI-H460 0.0845×, HT-29 0.0927×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0762×, HT-29 0.0912×); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.129×, LS 180 0.0729×); [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.113×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH3A1]] (+0.69, fdr 1e-05), [[ALDH1A1]] (+0.56, fdr 3e-05), [[NQO1]] (+0.55, fdr 2e-05); moves opposite to [[DLK2]] (-0.44, fdr 3e-04), [[RRAGC]] (-0.42, fdr 8e-05), [[NBPF10]] (-0.41, fdr 8e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[AKR1C3]] → it (grade B ⚠); 24 go from it, the strongest it → [[SLC7A11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **13.8×** | +17.2 | 0e+00 | 7/7 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **10.8×** | +14.9 | 0e+00 | 6/6 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.41×** | +10.2 | 4e-22 | 6/6 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +4.9 | 1e-04 | 4/7 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.7 | 4e-04 | 2/7 (A549, LS 180) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.48×** | +4.3 | 0.002 | 1/4 (A549) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.91×** | +4.1 | 0.004 | 4/7 (A549, CFPAC-1, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.74×** | +3.6 | 0.021 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.73×** | +3.6 | 0.021 | 0/7 | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.021 | 3/7 (A549, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +3.4 | 0.030 | 2/7 (KATO III, CFPAC-1) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.045 | 2/7 (A549, CFPAC-1) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.045 | 1/7 (A549) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.42×** | +3.3 | 0.045 | 6/7 (A498, KATO III, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.15×** | +3.2 | 0.045 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.045 | 2/7 (A498, A549) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.68×** | +3.2 | 0.045 | 3/7 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.1 | 0.063 | 2/7 (LS 180, A549) | top dose only | cell-cycle shift (explains ~22% here) |
| [[AZD-7648 (drug)]] 5 µM |  | **2.35×** | +2.9 | 0.096 | 3/7 (A498, A549, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12524.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.0687×, NCI-H460 0.0845×, HT-29 0.0927×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (KATO III 0.0762×, HT-29 0.0912×); [[Panobinostat (drug)]] 5 µM in 2 lines (KATO III 0.129×, LS 180 0.0729×); [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.569× | -3.4 | 0.36 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 29.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0687× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0762× (z -11.2) |
| [[A549 (line)]] | wt | 85.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 25.6× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 76.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 11.3× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0845× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0906× (z -8.7) |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0912× (z -8.6) |
| [[A498 (line)]] | wt | 276 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 5.77 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0729× (z -8.6) |
| [[A-172 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 14 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3A1]] | +0.69 | +0.75 / +0.54 | both halves | 1e-05 | STRING 717 |
| [[ALDH1A1]] | +0.56 | +0.44 / +0.47 | both halves | 3e-05 | STRING 437 |
| [[NQO1]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 | STRING 630 |
| [[CYP4F11]] | +0.53 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GPX2]] | +0.53 | +0.58 / +0.37 | both halves | 8e-05 | STRING 650 |
| [[SCARA5]] | +0.52 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[PGD]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[LINC00824]] | +0.50 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[SLC7A11]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[ITPK1]] | +0.49 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[UGT1A1]] | +0.49 | +0.57 / +0.32 | both halves | 2e-04 |  |
| [[LINC02474]] | +0.48 | +0.54 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLK2]] | -0.44 | -0.41 / -0.27 | both halves | 3e-04 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[RRAGC]] | -0.42 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[NBPF10]] | -0.41 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[HIC2]] | -0.41 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[ADPRS]] | -0.41 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[NAGK]] | -0.41 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[ZC2HC1A]] | -0.40 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[NBPF14]] | -0.40 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[DNAAF9]] | -0.40 | -0.45 / -0.16 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 2, C 15. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | AKR1C3 activity raises AKR1B10's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.32× lower at baseline in the lines without AKR1C3 | 0.026 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[NMRAL2P]] | B | NMRAL2P activity raises AKR1B10's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without NMRAL2P | 0.086 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[ALDH1A1]] | C | ALDH1A1 activity raises AKR1B10's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 3.94× lower at baseline in the lines without ALDH1A1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises AKR1B10's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 3.29× lower at baseline in the lines without GLP2R | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises AKR1B10's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 2.53× lower at baseline in the lines without GCNT3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises AKR1B10's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.93× lower at baseline in the lines without CYP4F11 | 0.012 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[TM4SF4]] | C | TM4SF4 activity raises AKR1B10's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 2.75× lower at baseline in the lines without TM4SF4 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[SPP1]] | C | SPP1 activity raises AKR1B10's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.70× lower at baseline in the lines without SPP1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |
| [[ALDH3A1]] | C | ALDH3A1 activity raises AKR1B10's level | lines that do not express ALDH3A1 (36) vs lines expressing it (14) | 2.54× lower at baseline in the lines without ALDH3A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1; co-absent with the target |
| [[AKR1C1]] | C | AKR1C1 activity raises AKR1B10's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 2.34× lower at baseline in the lines without AKR1C1 | 0.018 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU; co-absent with the target |
| [[GDA]] | C | GDA activity raises AKR1B10's level | lines that do not express GDA (35) vs lines expressing it (15) | 2.91× lower at baseline in the lines without GDA | 0.020 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[SLC19A3]] | C | SLC19A3 activity raises AKR1B10's level | lines that do not express SLC19A3 (36) vs lines expressing it (14) | 3.44× lower at baseline in the lines without SLC19A3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, MTND1P23, LINC00824; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 3, C 21. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC7A11]] | B | AKR1B10 activity raises SLC7A11's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.79× lower at baseline in the lines without AKR1B10 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[AKR1C3]] | B | AKR1B10 activity raises AKR1C3's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 4.33× lower at baseline in the lines without AKR1B10 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[PGD]] | B | AKR1B10 activity raises PGD's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 1.83× lower at baseline in the lines without AKR1B10 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[TM4SF4]] | C | AKR1B10 activity raises TM4SF4's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 3.71× lower at baseline in the lines without AKR1B10 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[MUC5B]] | C | AKR1B10 activity raises MUC5B's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 4.15× lower at baseline in the lines without AKR1B10 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[GDA]] | C | AKR1B10 activity raises GDA's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 5.60× lower at baseline in the lines without AKR1B10 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[GLP2R]] | C | AKR1B10 activity raises GLP2R's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.22× lower at baseline in the lines without AKR1B10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[ALPK2]] | C | AKR1B10 activity raises ALPK2's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 1.94× lower at baseline in the lines without AKR1B10 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[GCNT3]] | C | AKR1B10 activity raises GCNT3's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 5.46× lower at baseline in the lines without AKR1B10 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[TBXT]] | C | AKR1B10 activity raises TBXT's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.56× lower at baseline in the lines without AKR1B10 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[SCARA5]] | C | AKR1B10 activity raises SCARA5's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.09× lower at baseline in the lines without AKR1B10 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[LINC03000]] | C | AKR1B10 activity raises LINC03000's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.53× lower at baseline in the lines without AKR1B10 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.389). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 40.6); signed map (47.7, 44.9). **Vector** length 31.5, 11.9% of its response variance represented; |z| ≥ 3 in 197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +17.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +1.9 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.8 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.8 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -1.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -0.7 | -0.4 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -2.5 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -0.6 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.6 | +0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 1 member B10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:134,527,567-134,541,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AKR1B12, ARL-1, HIS, ARL1, HSI, ALDRLn; previously AKR1B11 |
| Gene groups (HGNC) | Aldo-keto reductases |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 5 pathways, smallest: Retinoid metabolism and transport; Metabolism of fat-soluble vitamins; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [O60218](https://www.uniprot.org/uniprotkb/O60218) (Aldo-keto reductase family 1 member B10):

> NADPH-dependent aldo-keto reductase that catalyzes the reduction of a broad range of carbonyl-containing compounds to their corresponding alcohols. Displays strong enzymatic activity toward all-trans-retinal, 9-cis-retinal, and 13-cis-retinal. Plays a critical role in detoxifying dietary and lipid-derived unsaturated carbonyls, such as crotonaldehyde, 4-hydroxynonenal, trans-2-hexenal, trans-2,4-hexadienal and their glutathione-conjugates carbonyls (GS-carbonyls). Displays enzymatic activity …

**Summary**, from NCBI Gene [57016](https://www.ncbi.nlm.nih.gov/gene/57016):

> This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. This member can efficiently reduce aliphatic and aromatic aldehydes, and it is less active on hexoses. It is highly expressed in adrenal gland, small intestine, and colon, and may play an important role in liver carcinogenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:382) · Entrez [57016](https://www.ncbi.nlm.nih.gov/gene/57016) · UniProt [O60218](https://www.uniprot.org/uniprotkb/O60218) · Ensembl [ENSG00000198074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198074)

## Data

Gene col 12524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12524); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12524]; `tensor/DDL_lfc|DDL_z.npy` [12524]; `embed/gene_vectors.npy` [12524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12524 or target_col == 12524). Every well: [[AKR1B10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR1B10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
