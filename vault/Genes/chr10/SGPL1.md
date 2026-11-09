---
symbol: "SGPL1"
type: "gene"
col: 9263
ensembl_id: "ENSG00000166224"
name: "sphingosine-1-phosphate lyase 1"
location: "10q22.1"
module: 25
arm: "+"
pooled_cpm: 51.18
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# SGPL1

*sphingosine-1-phosphate lyase 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.48× (z +6.6, q 2e-08, up in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 1.16× (z +3.6, q 0.046, up in 13 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 3.44×, NCI-H1573 3.34×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.732× (z -7.5, q 4e-11, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OCRL]] (+0.70, fdr 1e-05), [[DBN1]] (+0.66, fdr 2e-05), [[DCTN1]] (+0.66, fdr 2e-05); moves opposite to [[SEC61G]] (-0.68, fdr 4e-05), [[FUT11]] (-0.67, fdr 3e-05), [[NUDT22]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9263.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 3.44×, NCI-H1573 3.34×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.6 | 2e-08 | 36/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +6.2 | 1e-07 | 25/39 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.4 | 0.002 | 22/44 (BT-474, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.6 | 0.046 | 13/48 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.066 | 16/49 (A-172, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.066 | 18/48 (C-33 A, SW 900, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.1 | 0.13 | 15/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.21× | +3.1 | 0.13 | 19/48 (LS 180, MIA PaCa-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.21× | +3.1 | 0.13 | 10/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.13 | 14/48 (AN3 CA, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9263.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -7.5 | 4e-11 | 33/48 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.721×** | -5.4 | 2e-05 | 28/47 (SW480, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.730×** | -5.3 | 2e-05 | 30/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.760×** | -4.7 | 5e-04 | 25/48 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.762×** | -4.4 | 0.001 | 26/49 (SW480, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.786×** | -4.1 | 0.004 | 21/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.801×** | -3.8 | 0.013 | 26/48 (A549, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 5 µM |  | **0.813×** | -3.4 | 0.051 | 20/48 (LS 180, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.834× | -3.1 | 0.13 | 14/48 (A-172, A549, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 49.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 34.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.34× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 66.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -11.5) |
| [[A-427 (line)]] | wt | 69.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.375× (z -9.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 73.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[C-33 A (line)]] | alt | 70.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -15.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 35.1 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0695× (z -10.6) |
| [[COLO 205 (line)]] | alt | 37.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.2) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 36.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.404× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 55.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 77.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCRL]] | +0.70 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[DBN1]] | +0.66 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[DCTN1]] | +0.66 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[GMFB]] | +0.65 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[NCKAP1]] | +0.65 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.64 | +0.34 / +0.71 | both halves | 1e-04 |  |
| [[LPGAT1]] | +0.63 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[FECH]] | +0.62 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[KLC2]] | +0.61 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.61 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[FAM199X]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61G]] | -0.68 | -0.42 / -0.75 | both halves | 4e-05 |  |
| [[FUT11]] | -0.67 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[NUDT22]] | -0.64 | -0.34 / -0.74 | both halves | 1e-04 |  |
| [[IMP3]] | -0.62 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[PRKRIP1]] | -0.62 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[COX7A2]] ⚠ | -0.62 | -0.47 / -0.65 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM258]] | -0.61 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[SELENOH]] | -0.59 | -0.35 / -0.64 | both halves | 1e-04 |  |
| [[COX6B1]] | -0.59 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.59 | -0.38 / -0.63 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAMTOR5]] | -0.59 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[WSB1]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[C4orf3]] | -0.58 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[RNMT]] | -0.57 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SGPL1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises SGPL1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.4, -19.2); signed map (-14.8, -38.0). **Vector** length 99.0, 24.0% of its response variance represented; |z| ≥ 3 in 743 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +4.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.6 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.8 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.8 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -5.3 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.4 | -3.4 |
|  | [[Silodosin (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | sphingosine-1-phosphate lyase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,815,905-70,895,816 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPL |
| Gene groups (HGNC) | Aldehyde lyases |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O95470](https://www.uniprot.org/uniprotkb/O95470) (Sphingosine-1-phosphate lyase 1):

> Cleaves phosphorylated sphingoid bases (PSBs), such as sphingosine-1-phosphate, into fatty aldehydes and phosphoethanolamine. Elevates stress-induced ceramide production and apoptosis. Required for global lipid homeostasis in liver and cholesterol homeostasis in fibroblasts. Involved in the regulation of pro-inflammatory response and neutrophil trafficking. Modulates neuronal autophagy via phosphoethanolamine production which regulates accumulation of aggregate-prone proteins such as APP (By …

**Summary**, from NCBI Gene [8879](https://www.ncbi.nlm.nih.gov/gene/8879):

> Enables sphinganine-1-phosphate aldolase activity. Involved in apoptotic signaling pathway; fatty acid metabolic process; and sphingolipid metabolic process. Located in endoplasmic reticulum. Implicated in RENI syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10817) · Entrez [8879](https://www.ncbi.nlm.nih.gov/gene/8879) · UniProt [O95470](https://www.uniprot.org/uniprotkb/O95470) · Ensembl [ENSG00000166224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166224)

## Data

Gene col 9263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9263); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9263]; `tensor/DDL_lfc|DDL_z.npy` [9263]; `embed/gene_vectors.npy` [9263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9263 or target_col == 9263). Every well: [[SGPL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SGPL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
