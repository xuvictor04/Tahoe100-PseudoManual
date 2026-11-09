---
symbol: "TMEM232"
type: "gene"
col: 11872
ensembl_id: "ENSG00000186952"
name: "transmembrane protein 232"
location: "5q22.1"
module: 10
arm: "+"
pooled_cpm: 7.3
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 9
n_dd_up_clean: 37
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TMEM232

*transmembrane protein 232* — 5q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.55× (z +13.4, q 2e-38, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.340× (z -8.1, q 3e-13, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO38-DT]] (+0.78, fdr 7e-06), [[STPG2]] (+0.76, fdr 7e-06), [[PDCL3P4]] (+0.75, fdr 7e-06); moves opposite to [[CCDC134]] (-0.67, fdr 2e-05), [[FAM118A]] (-0.61, fdr 3e-05), [[L2HGDH]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02360]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.55×** | +13.4 | 2e-38 | 40/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.42×** | +13.0 | 3e-36 | 32/40 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.32×** | +9.0 | 5e-17 | 43/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.79×** | +7.7 | 2e-12 | 28/38 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +6.2 | 8e-08 | 32/46 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.79×** | +6.1 | 8e-08 | 25/47 (HEC-1-A, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +6.0 | 1e-07 | 5/15 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +5.6 | 1e-06 | 29/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +4.8 | 9e-05 | 19/38 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +4.8 | 1e-04 | 10/29 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.87×** | +4.7 | 1e-04 | 25/46 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.86×** | +4.6 | 2e-04 | 18/46 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +4.3 | 6e-04 | 22/46 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.006 | 15/39 (SK-MEL-2, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.007 | 11/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.57×** | +3.7 | 0.008 | 14/45 (A498, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.009 | 17/47 (SW480, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.340×** | -8.1 | 3e-13 | 32/47 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.420×** | -6.5 | 2e-08 | 27/46 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.437×** | -6.2 | 1e-07 | 25/36 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.475×** | -5.6 | 3e-06 | 25/45 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.487×** | -5.4 | 7e-06 | 28/46 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.487×** | -4.4 | 9e-04 | 19/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.561×** | -4.4 | 0.001 | 22/47 (SW1417, SHP-77, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.554×** | -4.2 | 0.002 | 24/45 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.582×** | -4.1 | 0.003 | 15/46 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.451× | -3.1 | 0.10 | 12/40 (COLO 205, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.665× | -3.1 | 0.11 | 16/45 (HT-29, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0785× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0723× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 3.24 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +10.3) | [[Nimesulide (drug)]] 5 µM 0.0763× (z -8.8) ⚠ toxic; unreliable plate only |
| [[LoVo (line)]] | wt | 7.56 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0964× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0953× (z -9.4) ⚠ toxic |
| [[HCT15 (line)]] | alt | 3.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 3.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 7.24 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0817× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 7.45 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0896× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 5.19 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0853× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 4.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 4.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.96× (z +10.4) | — |
| [[SW480 (line)]] | alt | 9.85 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.160× (z -9.1) |
| [[A-172 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.78 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO38-DT]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[STPG2]] | +0.76 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[PDCL3P4]] | +0.75 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[LEKR1]] | +0.75 | +0.83 / +0.59 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.74 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[FSIP2-AS1]] | +0.73 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[CAPN3]] | +0.73 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[EFCAB6]] | +0.70 | +0.81 / +0.47 | both halves | 2e-05 |  |
| [[ZRANB2-DT]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[LINC01252]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.69 | +0.81 / +0.51 | both halves | 1e-05 |  |
| [[LINC00240]] | +0.69 | +0.80 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC134]] | -0.67 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[FAM118A]] | -0.61 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[L2HGDH]] | -0.60 | -0.54 / -0.42 | both halves | 4e-05 | same gene group |
| [[KLHL8]] | -0.60 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02360]] | B | LINC02360 activity raises TMEM232's level | lines that do not express LINC02360 (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without LINC02360 | 8e-04 | ⚠ within organs, on part of the lines; also absent: MAGEB2, LINC01905, AJAP1 |
| [[MIR583HG]] | B | MIR583HG activity raises TMEM232's level | lines that do not express MIR583HG (10) vs lines expressing it (40) | 1.97× lower at baseline in the lines without MIR583HG | 0.040 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RGS17, GNAI1, KLF12; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TMEM232's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises TMEM232's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01905]] | B | LINC01905 activity raises TMEM232's level | lines that do not express LINC01905 (35) vs lines expressing it (15) | 1.67× lower at baseline in the lines without LINC01905 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000267327, ENSG00000267284, SLC25A24P1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.746). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.5, 15.5); signed map (28.5, -10.6). **Vector** length 74.9, 14.9% of its response variance represented; |z| ≥ 3 in 1,114 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.1 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.5 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | +6.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 232 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.1 — chr5:110,289,233-110,738,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ43080 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [C9JQI7](https://www.uniprot.org/uniprotkb/C9JQI7) (Transmembrane protein 232):

> Plays a critical role for male fertility and sperm motility by regulating sperm cytoplasm removal and maintaining axoneme integrity.

**Summary**, from NCBI Gene [642987](https://www.ncbi.nlm.nih.gov/gene/642987):

> Predicted to be involved in flagellated sperm motility and spermatid cytoplasm removal during spermiation of flagellated sperm. Predicted to act upstream of or within maintenance of protein complex location. Predicted to be located in membrane. Predicted to be active in outer dense fiber. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37270) · Entrez [642987](https://www.ncbi.nlm.nih.gov/gene/642987) · UniProt [C9JQI7](https://www.uniprot.org/uniprotkb/C9JQI7) · Ensembl [ENSG00000186952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186952)

## Data

Gene col 11872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11872); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11872]; `tensor/DDL_lfc|DDL_z.npy` [11872]; `embed/gene_vectors.npy` [11872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11872 or target_col == 11872). Every well: [[TMEM232 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM232.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
