---
symbol: "COMMD8"
type: "gene"
col: 9737
ensembl_id: "ENSG00000169019"
name: "COMM domain containing 8"
location: "4p12"
module: 17
arm: "+"
pooled_cpm: 9.81
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# COMMD8

*COMM domain containing 8* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.63× (z +13.9, q 5e-41, up in 15 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +4.9, q 9e-05, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.542× (z -5.8, q 5e-06, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C12orf29]] (+0.67, fdr 7e-06), [[IFTAP]] (+0.66, fdr 1e-05), [[NBN]] (+0.66, fdr 1e-05); moves opposite to [[TMEM11-DT]] (-0.65, fdr 2e-05), [[DRD4]] (-0.65, fdr 7e-06), [[TNXB]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[KIAA0408]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.63×** | +13.9 | 5e-41 | 15/15 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.32×** | +13.8 | 1e-40 | 31/33 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +9.3 | 4e-18 | 23/26 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.75×** | +5.3 | 2e-05 | 29/47 (HT-29, A498, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.9 | 9e-05 | 23/48 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.62×** | +4.4 | 0.001 | 23/46 (A-172, NCI-H1573, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.58×** | +4.3 | 0.001 | 20/39 (SW480, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +4.3 | 0.001 | 24/46 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.001 | 23/47 (CFPAC-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.008 | 16/47 (NCI-H1792, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.5 | 0.024 | 17/38 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.44×** | +3.4 | 0.029 | 17/47 (A498, HT-29, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.29×** | +3.4 | 0.033 | 12/48 (C32, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.061 | 16/47 (C32, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.40×** | +3.2 | 0.061 | 16/47 (SW 900, NCI-H1792, …) | all doses, flat |  |
| [[Arbutin (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.079 | 12/45 (A549, COLO 205, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +3.0 | 0.079 | 12/47 (NCI-H1573, HOP62, …) | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.83×** | +3.0 | 0.089 | 4/37 (A498, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -5.8 | 5e-06 | 30/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.587×** | -5.0 | 1e-04 | 27/47 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.590×** | -5.0 | 1e-04 | 26/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -4.6 | 5e-04 | 22/46 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 14.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.44× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 8.79 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.71× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 11.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Digitoxin (drug)]] 5 µM 0.136× (z -12.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.01 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 21.5 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.377× (z -8.7) |
| [[A549 (line)]] | wt | 7.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.77× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 8.88 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.08× (z +8.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 10.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.26× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 6.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.87× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf29]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 | STRING 486 |
| [[IFTAP]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[NBN]] | +0.66 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[KLHL9]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 | pathway: Neddylation; STRING 515 |
| [[MRPL40]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[DLD]] | +0.65 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[GMFB]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.64 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CDC73]] | +0.64 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[MOCS2]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.65 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[DRD4]] | -0.65 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[TNXB]] | -0.64 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[PITPNA]] | -0.63 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[NPIPB11]] | -0.62 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[TRPV1]] | -0.61 | -0.24 / -0.64 | both halves | 5e-04 |  |
| [[SPG7]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ING5]] | -0.59 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[MROH1]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[UBAP1L]] | -0.58 | -0.18 / -0.66 | ⚠ one half (not replicated) | 9e-04 |  |
| [[TTLL3]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[MARK4]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[ZNF394]] | -0.57 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA0408]] | B | KIAA0408 activity raises COMMD8's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 1.24× lower at baseline in the lines without KIAA0408 | 0.035 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1 |
| [[SOGA3]] | B | SOGA3 activity raises COMMD8's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.26× lower at baseline in the lines without SOGA3 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[MAP9]] | B | MAP9 activity raises COMMD8's level | lines that do not express MAP9 (17) vs lines expressing it (33) | 1.24× lower at baseline in the lines without MAP9 | 0.089 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, RNF150, BVES; its own permutation p |
| [[AMOT]] | B | AMOT activity raises COMMD8's level | lines that do not express AMOT (12) vs lines expressing it (38) | 1.33× lower at baseline in the lines without AMOT | 0.099 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-19.8, 0.1); signed map (5.8, -36.0). **Vector** length 63.0, 11.4% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.3 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.0 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.8 | +13.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -0.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.6 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:47,450,787-47,463,702 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20502 |
| Gene groups (HGNC) | COMM domain containing; CCC complex |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX08](https://www.uniprot.org/uniprotkb/Q9NX08) (COMM domain-containing protein 8):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. May down-regulate activation of NF-kappa-B.

**Summary**, from NCBI Gene [54951](https://www.ncbi.nlm.nih.gov/gene/54951):

> The protein encoded by this gene binds coiled-coil domain-containing protein 22 (CCDC22), and this complex can regulate the turnover of I-kappa-B and the activation of NF-kappa-B. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:26036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26036) · Entrez [54951](https://www.ncbi.nlm.nih.gov/gene/54951) · UniProt [Q9NX08](https://www.uniprot.org/uniprotkb/Q9NX08) · Ensembl [ENSG00000169019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169019)

## Data

Gene col 9737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9737); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9737]; `tensor/DDL_lfc|DDL_z.npy` [9737]; `embed/gene_vectors.npy` [9737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9737 or target_col == 9737). Every well: [[COMMD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
