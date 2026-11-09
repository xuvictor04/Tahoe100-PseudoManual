---
symbol: "SLC22A20P"
type: "gene"
col: 12474
ensembl_id: "ENSG00000197847"
name: "solute carrier family 22 member 20, pseudogene"
location: "11q13.1"
module: 38
arm: "+"
pooled_cpm: 11.67
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# SLC22A20P

*solute carrier family 22 member 20, pseudogene* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.93× (z +6.2, q 2e-07, up in 6 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.49× (z +4.1, q 0.009, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -13.0, q 8e-36, down in 32 of 41 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.437× (z -8.3, q 9e-15, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSANTD1]] (+0.76, fdr 7e-06), [[RAPSN]] (+0.72, fdr 7e-06), [[SLC23A3]] (+0.71, fdr 7e-06); moves opposite to [[TRAPPC11]] (-0.55, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MROH3P]] → it (grade B ⚠); 3 go from it, the strongest it → [[LINC00672]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +6.2 | 2e-07 | 6/18 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.7 | 9e-04 | 4/45 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.009 | 14/44 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.034 | 9/44 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Lucanthone (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.075 | 5/43 (NCI-H2030, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.401×** | -13.0 | 8e-36 | 32/41 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.323×** | -11.4 | 2e-27 | 32/39 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.319×** | -10.8 | 5e-25 | 34/43 (HEC-1-A, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.342×** | -10.8 | 5e-25 | 34/44 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.437×** | -8.3 | 9e-15 | 36/43 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.442×** | -8.2 | 2e-14 | 32/43 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.468×** | -7.6 | 2e-12 | 26/40 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.472×** | -7.5 | 3e-12 | 31/43 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.484×** | -7.3 | 2e-11 | 28/44 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.282×** | -6.7 | 2e-09 | 27/40 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.561×** | -5.8 | 3e-07 | 22/42 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.557×** | -5.5 | 1e-06 | 22/36 (LoVo, COLO 205, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.561×** | -5.5 | 2e-06 | 26/40 (H4, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.594×** | -5.2 | 7e-06 | 21/42 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.626×** | -4.7 | 1e-04 | 22/42 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Bexarotene (drug)]] 5 µM |  | **0.672×** | -4.0 | 0.002 | 11/44 (hTERT-HPNE, NCI-H1792, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.759×** | -3.9 | 0.003 | 16/43 (HEC-1-A, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -3.8 | 0.004 | 16/44 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -3.5 | 0.012 | 14/40 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.535×** | -3.3 | 0.028 | 11/42 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.049 | 15/44 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.806×** | -3.0 | 0.054 | 9/43 (LoVo, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 54.0 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -19.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0994× (z -18.0) |
| [[BT-474 (line)]] | alt | 36.0 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0392× (z -18.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -11.9) |
| [[SW480 (line)]] | alt | 17.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0400× (z -15.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0953× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0629× (z -17.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.136× (z -9.0) |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -14.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.187× (z -9.3) |
| [[A549 (line)]] | wt | 10.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -15.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.143× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 21.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -15.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -8.9) |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0829× (z -12.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 12.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0452× (z -11.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Verteporfin (drug)]] 5 µM 0.0784× (z -8.5) |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -12.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 18.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -17.6) ⚠ cell-cycle shift, explains ~47% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0626× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 5.15 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0294× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0834× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0730× (z -13.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 11.6 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0579× (z -11.6) |
| [[KATO III (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 6.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0909× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.2) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H460 (line)]] | wt | 4.79 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 3.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0399× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 5.91 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0823× (z -8.5) |
| [[A498 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD1]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[RAPSN]] | +0.72 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SLC23A3]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ATP2A1]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.70 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[QRICH2]] | +0.68 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[CHADL]] | +0.68 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[TMEM236]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[UBE2F-SCLY]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[OIT3]] | +0.68 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[LINC00672]] | +0.67 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC11]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH3P]] | B | MROH3P activity raises SLC22A20P's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without MROH3P | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[LSMEM2]] | B | LSMEM2 activity raises SLC22A20P's level | lines that do not express LSMEM2 (8) vs lines expressing it (42) | 2.06× lower at baseline in the lines without LSMEM2 | 0.005 | ⚠ within organs, on part of the lines; also absent: PLEKHA2, ATL1, ENSG00000283573; maybe low, not absent |
| [[TNNT2]] | B | TNNT2 activity raises SLC22A20P's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without TNNT2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[MFNG]] | B | MFNG activity raises SLC22A20P's level | lines that do not express MFNG (12) vs lines expressing it (38) | 1.96× lower at baseline in the lines without MFNG | 0.070 | ⚠ within organs, on part of the lines; also absent: CARD10, EPS8L2, KRT8 |
| [[MROH3P]] | B | MROH3P activity strengthens SLC22A20P's drug response | lines that do not express MROH3P (25) vs lines expressing it (19) | the lines without MROH3P respond 0.67× as strongly (z diff +1.41); strongest at Homoharringtonine 5 µM: 0.44x vs 0.26x (z diff +3.4) | 0.072 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3; target measured in part of the lines; artifact flags |
| [[LMO7DN]] | B | LMO7DN activity raises SLC22A20P's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without LMO7DN | 0.089 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |
| [[MELTF]] | B | MELTF activity raises SLC22A20P's level | lines that do not express MELTF (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without MELTF | 0.089 | ⚠ within organs, on part of the lines; also absent: EPHX2, ACCS; maybe low, not absent; its own permutation p |
| [[SPTBN5]] | C | SPTBN5 activity raises SLC22A20P's level | lines that do not express SPTBN5 (3) vs lines expressing it (47) | 2.51× lower at baseline in the lines without SPTBN5 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with SMAD3; also absent: UACA, MYH16, PER3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SMBD1P]] | C | SMBD1P activity raises SLC22A20P's level | lines that do not express SMBD1P (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without SMBD1P | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRP1, SPTBN5, DDIT4; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00672]] | C | SLC22A20P activity raises LINC00672's level | lines that do not express SLC22A20P (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without SLC22A20P | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CDC42EP1, PLEKHG5, MYH16; maybe low, not absent; its own permutation p |
| [[CDKL4]] | C | SLC22A20P activity raises CDKL4's level | lines that do not express SLC22A20P (3) vs lines expressing it (47) | 1.75× lower at baseline in the lines without SLC22A20P | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CDC42EP1, PLEKHG5, MYH16; maybe low, not absent |
| [[INPP5E]] | C | SLC22A20P activity lowers INPP5E's level | lines that do not express SLC22A20P (3) vs lines expressing it (47) | 1.30× higher at baseline in the lines without SLC22A20P | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CDC42EP1, PLEKHG5, MYH16; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.0, -16.1); signed map (13.0, 9.8). **Vector** length 93.9, 21.8% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.3 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | -0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +1.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -4.1 | -10.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -3.6 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -7.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.2 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -5.5 |
|  | [[Bexarotene (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 22 member 20, pseudogene |
| Locus type | pseudogene |
| Location | 11q13.1 — chr11:65,213,873-65,242,086 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | Oat6, FLJ16331; previously SLC22A20 |
| Gene groups (HGNC) | Solute carrier family 22; Unitary pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NK97](https://www.uniprot.org/uniprotkb/A6NK97) (Solute carrier family 22 member 20):

> Organic anion transporter that mediates the uptake of estrone sulfate. Inhibited by probenecid, propionate, 2-methylbutyrate, 3-methylbutyrate, benzoate, heptanoate and 2-ethylhaxanoate. May act as an odorant transporter (By similarity).

**Summary**, from NCBI Gene [440044](https://www.ncbi.nlm.nih.gov/gene/440044):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in organic anion transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29867) · Entrez [440044](https://www.ncbi.nlm.nih.gov/gene/440044) · UniProt [A6NK97](https://www.uniprot.org/uniprotkb/A6NK97) · Ensembl [ENSG00000197847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197847)

## Data

Gene col 12474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12474); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12474]; `tensor/DDL_lfc|DDL_z.npy` [12474]; `embed/gene_vectors.npy` [12474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12474 or target_col == 12474). Every well: [[SLC22A20P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC22A20P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
