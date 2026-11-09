---
symbol: "MESD"
type: "gene"
col: 3955
ensembl_id: "ENSG00000117899"
name: "mesoderm development LRP chaperone"
location: "15q25.1"
module: 49
arm: "+"
pooled_cpm: 60.6
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# MESD

*mesoderm development LRP chaperone* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.56× (z +10.3, q 6e-22, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +7.9, q 7e-13, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.453× (z -13.3, q 7e-38, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYDGF]] (+0.59, fdr 1e-05), [[SPCS2]] (+0.58, fdr 2e-05), [[FKBP11]] (+0.57, fdr 1e-05); moves opposite to [[NAPRT]] (-0.57, fdr 4e-05), [[KLF11]] (-0.54, fdr 3e-05), [[PEX1]] (-0.53, fdr 3e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.56×** | +10.3 | 6e-22 | 45/49 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.7 | 9e-20 | 37/42 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.9 | 7e-13 | 39/49 (SW1417, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +7.1 | 2e-10 | 42/47 (NCI-H1573, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +6.2 | 8e-08 | 29/45 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.5 | 5e-04 | 32/48 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.5 | 5e-04 | 29/49 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +4.1 | 0.003 | 35/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.081 | 28/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.21×** | +3.2 | 0.081 | 17/48 (PANC-1, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.453×** | -13.3 | 7e-38 | 47/48 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.623×** | -5.6 | 5e-06 | 37/47 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.659×** | -4.8 | 3e-04 | 35/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.480×** | -4.6 | 7e-04 | 32/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.495×** | -4.4 | 0.001 | 39/49 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.738×** | -3.5 | 0.046 | 30/49 (RKO, J82, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.748×** | -3.4 | 0.046 | 28/48 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 58.0 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -9.8) |
| [[A-172 (line)]] | wt | 47.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.10× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.9) |
| [[A498 (line)]] | wt | 67.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -12.3) |
| [[A549 (line)]] | wt | 68.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.8) |
| [[C32 (line)]] | wt | 49.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 86.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.2) |
| [[HOP62 (line)]] | alt | 71.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.5) |
| [[SW1417 (line)]] | alt | 53.0 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.8) |
| [[H4 (line)]] | wt | 82.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -12.6) |
| [[HS-578T (line)]] | alt | 45.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.326× (z -8.9) |
| [[KATO III (line)]] | alt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 45.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 37.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 66.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.1) |
| [[A-427 (line)]] | wt | 37.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -25.7) |
| [[AsPC-1 (line)]] | alt | 35.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.1) |
| [[BT-474 (line)]] | alt | 46.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -8.6) |
| [[COLO 205 (line)]] | alt | 94.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 75.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.1) |
| [[Hs 766T (line)]] | wt | 44.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 62.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -11.4) |
| [[J82 (line)]] | alt | 60.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -10.3) |
| [[LoVo (line)]] | wt | 80.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 70.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.69× (z +8.5) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 62.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 73.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 59.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 50.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.4) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 80.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.1) |
| [[SW480 (line)]] | alt | 61.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.1) |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 84.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYDGF]] | +0.59 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[SPCS2]] | +0.58 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[FKBP11]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GLUD1P3]] | +0.55 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | +0.53 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[PCGF3-AS1]] | +0.53 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[WDR20]] | +0.53 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[SSR4]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[C9orf153]] | +0.52 | +0.40 / +0.50 | both halves | 4e-05 |  |
| [[CCDC168]] | +0.52 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[KDELR1]] | +0.51 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ARL17A]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPRT]] | -0.57 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[KLF11]] | -0.54 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PEX1]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZNF772]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[DGAT2]] | -0.50 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[ZSCAN12]] | -0.49 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SRSF3]] | -0.49 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[CCDC113]] | -0.49 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[BHLHE41]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[MIF4GD]] | -0.48 | -0.52 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[NUDT12]] | -0.47 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[VEZF1]] | -0.47 | -0.37 / -0.58 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MESD's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TP53]] | C | TP53 activity weakens MESD's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 1.12× as strongly (z diff -0.70); strongest at Idarubicin (hydrochloride) 5 µM: 1.66x vs 1.30x (z diff -2.9) | 0.406 over the table, 0.018 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.343). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.0, 17.7); signed map (-45.2, 10.6). **Vector** length 73.4, 19.5% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | -0.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.5 | +1.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.4 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.9 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.5 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | mesoderm development LRP chaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:80,946,289-80,989,828 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0081, BOCA; previously MESDC2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14696](https://www.uniprot.org/uniprotkb/Q14696) (LRP chaperone MESD):

> Chaperone specifically assisting the folding of beta-propeller/EGF modules within the family of low-density lipoprotein receptors (LDLRs). Acts as a modulator of the Wnt pathway through chaperoning the coreceptors of the canonical Wnt pathway, LRP5 and LRP6, to the plasma membrane. Essential for specification of embryonic polarity and mesoderm induction. Plays an essential role in neuromuscular junction (NMJ) formation by promoting cell-surface expression of LRP4 (By similarity). May regulate …

**Summary**, from NCBI Gene [23184](https://www.ncbi.nlm.nih.gov/gene/23184):

> Predicted to enable low-density lipoprotein particle receptor binding activity. Involved in ossification and protein folding. Located in cytosol; endoplasmic reticulum; and nuclear body. Implicated in osteogenesis imperfecta type 20. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13520) · Entrez [23184](https://www.ncbi.nlm.nih.gov/gene/23184) · UniProt [Q14696](https://www.uniprot.org/uniprotkb/Q14696) · Ensembl [ENSG00000117899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117899)

## Data

Gene col 3955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3955); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3955]; `tensor/DDL_lfc|DDL_z.npy` [3955]; `embed/gene_vectors.npy` [3955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3955 or target_col == 3955). Every well: [[MESD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MESD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
