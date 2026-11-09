---
symbol: "KLF3-AS1"
type: "gene"
col: 13781
ensembl_id: "ENSG00000231160"
name: "KLF3 antisense RNA 1"
location: "4p14"
module: 15
arm: "+"
pooled_cpm: 4.41
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 23
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# KLF3-AS1

*KLF3 antisense RNA 1* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.29× (z +20.1, q 0e+00, up in 34 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.350× (z -10.5, q 3e-23, down in 32 of 45 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.464× (z -7.7, q 2e-12, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPESP1]] (+0.78, fdr 1e-05), [[HLA-DMA]] (+0.75, fdr 7e-06), [[INTS6-AS1]] (+0.74, fdr 1e-05); moves opposite to [[NAA40]] (-0.61, fdr 7e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.29×** | +20.1 | 0e+00 | 34/36 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +9.3 | 3e-18 | 20/32 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.2 | 1e-10 | 3/10 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.4 | 3e-08 | 21/37 (NCI-H460, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.47×** | +5.2 | 2e-05 | 14/45 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.1 | 3e-05 | 9/38 (SNU-1, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.64×** | +4.6 | 3e-04 | 2/13 (AsPC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.6 | 3e-04 | 3/19 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +4.3 | 9e-04 | 13/43 (A498, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 10/43 (H4, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.011 | 11/43 (NCI-H460, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.43×** | +3.6 | 0.016 | 7/37 (H4, BT-474, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.030 | 9/30 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.063 | 9/45 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.074 | 4/44 (KATO III, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.074 | 13/42 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.080 | 5/44 (LS 180, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13781.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.350×** | -10.5 | 3e-23 | 32/45 (SW480, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.392×** | -9.4 | 1e-18 | 27/45 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.395×** | -9.3 | 2e-18 | 29/45 (SW480, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.464×** | -7.7 | 2e-12 | 25/44 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.534×** | -6.3 | 4e-08 | 22/45 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.571×** | -5.6 | 2e-06 | 19/45 (SW480, LoVo, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.610×** | -4.9 | 6e-05 | 21/45 (KATO III, SW480, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.409×** | -4.7 | 2e-04 | 15/41 (H4, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.627×** | -4.7 | 2e-04 | 16/43 (SW480, H4, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.616×** | -4.7 | 2e-04 | 14/42 (SW480, A549, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.716×** | -4.6 | 2e-04 | 19/37 (AsPC-1, SW480, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.618×** | -4.6 | 2e-04 | 20/40 (Hs 766T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.649×** | -4.3 | 7e-04 | 13/45 (SW480, LoVo, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.661×** | -4.1 | 0.001 | 19/42 (H4, BT-474, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.651×** | -4.1 | 0.002 | 12/41 (A498, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.521×** | -3.4 | 0.021 | 7/40 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.530×** | -3.3 | 0.025 | 7/38 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.658×** | -3.0 | 0.076 | 6/45 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.569×** | -3.0 | 0.080 | 7/31 (SNU-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.80 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.2 | 0 | 10 (7 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0306× (z -20.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.138× (z -11.5) |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0207× (z -14.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0348× (z -12.0) |
| [[A549 (line)]] | wt | 7.30 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -10.4) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.0762× (z -9.5) |
| [[H4 (line)]] | wt | 21.1 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0287× (z -13.3) |
| [[BT-474 (line)]] | alt | 9.60 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0200× (z -14.6) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0883× (z -9.1) |
| [[SW48 (line)]] | wt | 9.93 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0416× (z -9.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 3.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +10.6) | — |
| [[A498 (line)]] | wt | 3.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +12.6) | — |
| [[AsPC-1 (line)]] | alt | 9.47 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -11.5) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HEC-1-A (line)]] | alt | 1.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 2.97 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 0.05 µM 0.0414× (z -9.9) |
| [[HS-578T (line)]] | alt | 4.87 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0295× (z -11.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[KATO III (line)]] | alt | 5.42 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0474× (z -11.0) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H23 (line)]] | alt | 3.86 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0618× (z -8.5) |
| [[PANC-1 (line)]] | alt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.72× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0533× (z -9.8) |
| [[A-427 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPESP1]] | +0.78 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[HLA-DMA]] | +0.75 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.74 | +0.51 / +0.62 | both halves | 1e-05 | same gene group |
| [[SEC24B-AS1]] | +0.72 | +0.53 / +0.57 | both halves | 1e-05 | same gene group |
| [[SPATA1]] | +0.72 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PRANCR]] | +0.71 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.69 | +0.54 / +0.50 | both halves | 1e-05 | same gene group |
| [[CCNO-DT]] | +0.69 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[H2AZ1-DT]] | +0.69 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.69 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[DICER1-AS1]] | +0.69 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[CHD1-DT]] | +0.68 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.61 | -0.37 / -0.54 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLF3-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PARP11]] | C | PARP11 activity raises KLF3-AS1's level | lines that do not express PARP11 (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without PARP11 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: NECAB2, FAT3, ENSG00000205890; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.9, 21.1); signed map (27.9, -5.9). **Vector** length 75.1, 13.2% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.8 | +20.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -4.0 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -3.7 | -9.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.4 | -9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -5.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | KLF3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p14 — chr4:38,602,438-38,664,926 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ13197 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25796](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25796) · Entrez [79667](https://www.ncbi.nlm.nih.gov/gene/79667) · Ensembl [ENSG00000231160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231160)

## Data

Gene col 13781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13781); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13781]; `tensor/DDL_lfc|DDL_z.npy` [13781]; `embed/gene_vectors.npy` [13781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13781 or target_col == 13781). Every well: [[KLF3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
