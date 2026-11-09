---
symbol: "CYP4V2"
type: "gene"
col: 6996
ensembl_id: "ENSG00000145476"
name: "cytochrome P450 family 4 subfamily V member 2"
location: "4q35.1-q35.2"
module: 10
arm: "+"
pooled_cpm: 7.16
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CYP4V2

*cytochrome P450 family 4 subfamily V member 2* — 4q35.1-q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +11.1, q 1e-25, up in 24 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.84× (z +8.7, q 4e-16, up in 31 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.280× (z -12.9, q 3e-35, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RXYLT1]] (+0.68, fdr 5e-05), [[LINC00667]] (+0.67, fdr 2e-05), [[UFL1-AS1]] (+0.66, fdr 2e-05); moves opposite to [[ATP5MJ]] (-0.63, fdr 2e-05), [[COX6C]] (-0.62, fdr 2e-05), [[COX6A1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +11.1 | 1e-25 | 24/30 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +10.1 | 1e-21 | 10/12 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.7 | 4e-16 | 31/42 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.53×** | +8.7 | 4e-16 | 17/19 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +5.3 | 2e-05 | 23/45 (CFPAC-1, SW480, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.2 | 2e-05 | 21/40 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +5.0 | 4e-05 | 21/45 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.60×** | +4.8 | 1e-04 | 13/43 (LoVo, A-172, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.10×** | +3.9 | 0.005 | 11/45 (A-172, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.006 | 11/45 (A498, LoVo, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.021 | 12/43 (Panc 03.27, A498, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.022 | 8/45 (A-172, NCI-H1573, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.038 | 11/42 (NCI-H2030, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.038 | 13/42 (Hs 766T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.3 | 0.038 | 6/46 (AsPC-1, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.061 | 7/46 (HOP62, A498, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.071 | 10/45 (RPMI-7951, A549, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.073 | 8/43 (NCI-H460, NCI-H1573, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.280×** | -12.9 | 3e-35 | 40/44 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.390×** | -9.0 | 6e-17 | 34/43 (H4, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.450×** | -8.1 | 1e-13 | 30/43 (A-427, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.462×** | -7.8 | 7e-13 | 34/44 (SK-MEL-2, KATO III, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.466×** | -7.7 | 1e-12 | 30/46 (SNU-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.546×** | -6.1 | 9e-08 | 20/44 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.563×** | -5.8 | 5e-07 | 22/43 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.609×** | -5.0 | 4e-05 | 21/45 (H4, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.531×** | -4.6 | 3e-04 | 12/45 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.482×** | -3.9 | 0.006 | 9/22 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -3.5 | 0.025 | 15/45 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.739× | -3.1 | 0.10 | 14/46 (SW480, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 8.90 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0407× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.140× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 8.49 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.97× (z +9.3) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.212× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 7.07 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0835× (z -8.6) |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0463× (z -11.0) |
| [[HOP62 (line)]] | alt | 7.30 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HT-29 (line)]] | alt | 3.61 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0324× (z -11.7) |
| [[J82 (line)]] | alt | 5.16 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0919× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[KATO III (line)]] | alt | 10.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.138× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 5.25 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0750× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 7.58 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.156× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0492× (z -13.4) |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0653× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 4.01 | 0 | 1 | — | [[Fluvoxamine (drug)]] 0.05 µM 0.0521× (z -8.9) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RXYLT1]] | +0.68 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[LINC00667]] | +0.67 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[UFL1-AS1]] | +0.66 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[TMEM147-AS1]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ADCK1]] | +0.64 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[BDNF-AS]] | +0.63 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[HDHD2]] | +0.63 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[MAD2L1-DT]] | +0.62 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[LINC00412]] | +0.62 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[RBM26-AS1]] | +0.62 | +0.66 / +0.36 | both halves | 9e-05 |  |
| [[RAP2C-AS1]] | +0.62 | +0.66 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | -0.63 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[COX6C]] | -0.62 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.60 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LAMTOR5]] | -0.59 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CLTCL1]] | -0.59 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[BLVRB]] | -0.59 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[POLR2J]] ⚠ | -0.59 | -0.32 / -0.42 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RASSF7]] | -0.58 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[VRK3]] | -0.57 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[ANAPC11]] | -0.56 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ACTR6]] | -0.56 | -0.49 / -0.37 | both halves | 9e-05 |  |
| [[ABCB9]] | -0.56 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[RNF181]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises CYP4V2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.6, 14.8); signed map (27.9, -30.2). **Vector** length 77.7, 14.2% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -12.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -7.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.5 | -9.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | -5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 4 subfamily V member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1-q35.2 — chr4:186,191,567-186,213,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYP4AH1 |
| Gene groups (HGNC) | Cytochrome P450 family 4 |
| Reactome | 7 pathways, smallest: The canonical retinoid cycle in rods (twilight vision); Endogenous sterols; Cytochrome P450 - arranged by substrate type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZWL3](https://www.uniprot.org/uniprotkb/Q6ZWL3) (Cytochrome P450 4V2):

> A cytochrome P450 monooxygenase involved in fatty acid metabolism in the eye. Catalyzes the omega-hydroxylation of polyunsaturated fatty acids (PUFAs) docosahexaenoate (DHA) and its precursor eicosapentaenoate (EPA), and may contribute to the homeostasis of these retinal PUFAs. Omega hydroxylates saturated fatty acids such as laurate, myristate and palmitate, the catalytic efficiency decreasing in the following order: myristate > laurate > palmitate (C14>C12>C16). Mechanistically, uses …

**Summary**, from NCBI Gene [285440](https://www.ncbi.nlm.nih.gov/gene/285440):

> This gene encodes a member of the cytochrome P450 hemethiolate protein superfamily which are involved in oxidizing various substrates in the metabolic pathway. It is implicated in the metabolism of fatty acid precursors into n-3 polyunsaturated fatty acids. Mutations in this gene result in Bietti crystalline corneoretinal dystrophy. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23198) · Entrez [285440](https://www.ncbi.nlm.nih.gov/gene/285440) · UniProt [Q6ZWL3](https://www.uniprot.org/uniprotkb/Q6ZWL3) · Ensembl [ENSG00000145476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145476)

## Data

Gene col 6996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6996); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6996]; `tensor/DDL_lfc|DDL_z.npy` [6996]; `embed/gene_vectors.npy` [6996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6996 or target_col == 6996). Every well: [[CYP4V2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP4V2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
