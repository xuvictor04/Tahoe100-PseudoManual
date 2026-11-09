---
symbol: "ACAA1"
type: "gene"
col: 696
ensembl_id: "ENSG00000060971"
name: "acetyl-CoA acyltransferase 1"
location: "3p22.2"
module: 2
arm: "+"
pooled_cpm: 16.45
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ACAA1

*acetyl-CoA acyltransferase 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.00× (z +20.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.750× (z -5.3, q 5e-05, down in 18 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.775× (z -4.7, q 6e-04, down in 14 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUP]] (+0.56, fdr 4e-05), [[CORO1B]] (+0.56, fdr 4e-05), [[ARSA]] (+0.52, fdr 1e-04); moves opposite to [[NPRL3]] (-0.48, fdr 4e-05), [[NSUN4]] (-0.47, fdr 2e-04), [[FBXO10]] (-0.46, fdr 4e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IRF6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +20.3 | 0e+00 | 45/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +18.2 | 0e+00 | 40/44 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.63×** | +17.9 | 0e+00 | 46/47 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +16.5 | 0e+00 | 41/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.81×** | +11.0 | 3e-26 | 23/37 (PANC-1, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.70×** | +9.5 | 2e-19 | 20/30 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +9.5 | 2e-19 | 33/48 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.66×** | +8.6 | 4e-16 | 17/33 (Panc 03.27, SW1417, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +8.2 | 1e-14 | 29/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +8.2 | 1e-14 | 22/46 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +6.3 | 1e-08 | 20/41 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.39×** | +5.9 | 2e-07 | 21/41 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 16/48 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +5.0 | 2e-05 | 14/48 (SW1417, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +4.5 | 2e-04 | 16/48 (RKO, SW480, …) | top dose only | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.59×** | +4.5 | 2e-04 | 8/42 (A549, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 12/48 (LS 180, SW1417, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.004 | 13/47 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.009 | 9/43 (HCT15, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.068 | 3/43 (SW1417, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.072 | 4/48 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.750×** | -5.3 | 5e-05 | 18/46 (SNU-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.775×** | -4.7 | 6e-04 | 14/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.793×** | -4.3 | 0.003 | 11/47 (SW 900, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.820×** | -3.7 | 0.033 | 11/47 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.824×** | -3.5 | 0.061 | 11/47 (AN3 CA, SW48, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.843× | -3.2 | 0.15 | 1/48 (Panc 03.27) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 22.9 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +14.0) | — |
| [[SW480 (line)]] | alt | 18.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.4) | — |
| [[A549 (line)]] | wt | 12.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.15 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0681× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 22.4 | 1 | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.97× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.1) |
| [[A498 (line)]] | wt | 9.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 8.96 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 29.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 26.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.8) | — |
| [[RKO (line)]] | wt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +10.2) | — |
| [[SW1417 (line)]] | alt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[A-172 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUP]] | +0.56 | +0.43 / +0.56 | both halves | 4e-05 |  |
| [[CORO1B]] | +0.56 | +0.47 / +0.40 | both halves | 4e-05 |  |
| [[ARSA]] | +0.52 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[PITPNM1]] | +0.52 | +0.35 / +0.46 | both halves | 1e-04 |  |
| [[DAG1]] | +0.52 | +0.36 / +0.51 | both halves | 1e-04 |  |
| [[IRF6]] | +0.51 | +0.37 / +0.40 | both halves | 8e-05 |  |
| [[MTMR11]] | +0.50 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[PORCN]] | +0.50 | +0.38 / +0.40 | both halves | 6e-05 |  |
| [[ANO8]] | +0.50 | +0.40 / +0.38 | both halves | 6e-05 |  |
| [[ROGDI]] | +0.50 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[SSH3]] | +0.49 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[GTPBP1]] | +0.49 | +0.35 / +0.44 | both halves | 1e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPRL3]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[NSUN4]] | -0.47 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[FBXO10]] | -0.46 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[TTC27]] | -0.45 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[SCMH1]] | -0.45 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[METTL8]] | -0.44 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[ZNF785]] | -0.42 | -0.26 / -0.40 | both halves | 4e-04 |  |
| [[MRPL45P2]] | -0.42 | -0.14 / -0.44 | ⚠ not reproduced | 0.002 |  |
| [[MTRFR]] | -0.42 | -0.27 / -0.28 | both halves | 3e-04 |  |
| [[MLH3]] | -0.42 | -0.27 / -0.34 | both halves | 3e-04 |  |
| [[TTC17]] | -0.42 | -0.41 / -0.25 | both halves | 4e-04 |  |
| [[GCFC2]] | -0.42 | -0.17 / -0.30 | ⚠ not reproduced | 0.001 |  |
| [[PIGL]] | -0.41 | -0.20 / -0.45 | both halves | 7e-04 |  |
| [[TIMM9]] | -0.41 | -0.33 / -0.31 | both halves | 2e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF6]] | B | IRF6 activity raises ACAA1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 1.70× lower at baseline in the lines without IRF6 | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TOP2A]] | B | TOP2A activity lowers ACAA1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MISP]] | B | MISP activity raises ACAA1's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without MISP | 0.034 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[JUP]] | B | JUP activity raises ACAA1's level | lines that do not express JUP (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without JUP | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[LGALS3BP]] | B | LGALS3BP activity raises ACAA1's level | lines that do not express LGALS3BP (7) vs lines expressing it (43) | 1.22× lower at baseline in the lines without LGALS3BP | 0.056 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.407). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (11.9, -47.6); signed map (-25.1, 2.1). **Vector** length 61.4, 9.22% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +4.8 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.7 | +8.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.4 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +18.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +0.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.3 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | acetyl-CoA acyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:38,103,129-38,137,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Lnc-Myd88 |
| Gene groups (HGNC) | Acyltransferases |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM, UV_RESPONSE_UP, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 11 pathways, smallest: TYSND1 cleaves peroxisomal proteins; Beta-oxidation of very long chain fatty acids; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P09110](https://www.uniprot.org/uniprotkb/P09110) (3-ketoacyl-CoA thiolase, peroxisomal):

> Responsible for the thiolytic cleavage of straight chain 3-keto fatty acyl-CoAs (3-oxoacyl-CoAs). Plays an important role in fatty acid peroxisomal beta-oxidation. Catalyzes the cleavage of medium, long, and very long straight chain 3-oxoacyl-CoAs. May play a role in peroxisomal beta-oxidation step in polyunsaturated fatty acids (PUFAs) biosynthesis. Possibly regulates systemic levels of docosahexaenoic acid (DHA, C22:6n-3) through a process involving endoplasmic reticulum desaturation and …

**Summary**, from NCBI Gene [30](https://www.ncbi.nlm.nih.gov/gene/30):

> This gene encodes an enzyme operative in the beta-oxidation system of the peroxisomes. Deficiency of this enzyme leads to pseudo-Zellweger syndrome. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:82](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:82) · Entrez [30](https://www.ncbi.nlm.nih.gov/gene/30) · UniProt [P09110](https://www.uniprot.org/uniprotkb/P09110) · Ensembl [ENSG00000060971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060971)

## Data

Gene col 696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 696); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 696]; `tensor/DDL_lfc|DDL_z.npy` [696]; `embed/gene_vectors.npy` [696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 696 or target_col == 696). Every well: [[ACAA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
