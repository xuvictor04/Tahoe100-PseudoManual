---
symbol: "FAM227B"
type: "gene"
col: 9271
ensembl_id: "ENSG00000166262"
name: "family with sequence similarity 227 member B"
location: "15q21.2"
module: 10
arm: "+"
pooled_cpm: 10.66
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 19
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# FAM227B

*family with sequence similarity 227 member B* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +7.5, q 4e-11, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.417× (z -9.2, q 2e-17, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPH6-DT]] (+0.75, fdr 7e-06), [[LINC00240]] (+0.74, fdr 1e-05), [[AHI1-DT]] (+0.74, fdr 1e-05); moves opposite to [[LPCAT1]] (-0.65, fdr 4e-05), [[ARHGAP8]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FSIP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.5 | 4e-11 | 30/44 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.56×** | +6.6 | 9e-09 | 31/48 (LS 180, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.9 | 6e-07 | 23/36 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +5.6 | 3e-06 | 27/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.5 | 5e-06 | 12/21 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 7e-04 | 22/47 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.4 | 8e-04 | 20/46 (A498, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +4.4 | 8e-04 | 12/27 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.003 | 18/46 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.66×** | +3.8 | 0.006 | 8/45 (SW480, Hs 766T, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.006 | 13/48 (SW480, LS 180, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.006 | 16/46 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.028 | 17/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.84×** | +3.4 | 0.031 | 4/47 (HEC-1-A, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.041 | 12/47 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.060 | 14/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.417×** | -9.2 | 2e-17 | 39/47 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.420×** | -9.1 | 2e-17 | 33/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.451×** | -8.4 | 1e-14 | 37/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.504×** | -7.2 | 9e-11 | 36/45 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -6.7 | 3e-09 | 27/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.547×** | -6.3 | 2e-08 | 27/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.566×** | -6.0 | 2e-07 | 27/47 (HCT15, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.595×** | -4.6 | 2e-04 | 19/48 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.671×** | -4.2 | 0.002 | 19/48 (NCI-H2030, AN3 CA, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.475×** | -4.1 | 0.002 | 17/46 (RKO, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.669×** | -4.0 | 0.004 | 16/46 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.590×** | -3.9 | 0.004 | 15/48 (RKO, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.710×** | -3.6 | 0.015 | 14/48 (HOP62, CHP-212, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -3.4 | 0.025 | 16/43 (hTERT-HPNE, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.723×** | -3.4 | 0.026 | 17/47 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.805×** | -3.2 | 0.046 | 17/48 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.579×** | -3.0 | 0.082 | 11/43 (SNU-1, SW48, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 22.4 | 0 | 4 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0974× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~52% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.136× (z -11.6) |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0726× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -9.8) |
| [[PANC-1 (line)]] | alt | 9.86 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -9.8) |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.151× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0853× (z -8.7) |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0472× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 14.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -9.5) |
| [[RKO (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.121× (z -9.3) |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0506× (z -9.1) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH6-DT]] | +0.75 | +0.81 / +0.58 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.74 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.74 | +0.79 / +0.53 | both halves | 1e-05 |  |
| [[BDNF-AS]] | +0.74 | +0.83 / +0.48 | both halves | 2e-05 |  |
| [[TMEM9B-AS1]] | +0.73 | +0.77 / +0.46 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.73 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[KLHDC1]] | +0.72 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[APPBP2-DT]] | +0.71 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[F8]] | +0.71 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[UNC79]] | +0.71 | +0.80 / +0.51 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.70 | +0.77 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LPCAT1]] | -0.65 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[ARHGAP8]] | -0.61 | -0.66 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2]] | B | FSIP2 activity raises FAM227B's level | lines that do not express FSIP2 (26) vs lines expressing it (24) | 1.28× lower at baseline in the lines without FSIP2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000286797, NPFFR2, GRIA2; maybe low, not absent |
| [[CLEC2D]] | C | CLEC2D activity raises FAM227B's level | lines that do not express CLEC2D (3) vs lines expressing it (47) | 2.13× lower at baseline in the lines without CLEC2D | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: IMPG2, GSTM2, ENSG00000286952; maybe low, not absent; its own permutation p |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises FAM227B's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |
| [[LRRIQ3]] | C | LRRIQ3 activity raises FAM227B's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without LRRIQ3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent; its own permutation p |
| [[NR1D2]] | C | NR1D2's natural level weakens FAM227B's drug response | NR1D2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.43; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.806). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.8, 18.2); signed map (30.7, -9.4). **Vector** length 71.0, 13.4% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -8.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -4.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 227 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:49,326,962-49,620,929 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32800; previously C15orf33 |
| Matched by | ensembl_id |

UniProt [Q96M60](https://www.uniprot.org/uniprotkb/Q96M60) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26543) · Entrez [196951](https://www.ncbi.nlm.nih.gov/gene/196951) · UniProt [Q96M60](https://www.uniprot.org/uniprotkb/Q96M60) · Ensembl [ENSG00000166262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166262)

## Data

Gene col 9271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9271); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9271]; `tensor/DDL_lfc|DDL_z.npy` [9271]; `embed/gene_vectors.npy` [9271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9271 or target_col == 9271). Every well: [[FAM227B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM227B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
