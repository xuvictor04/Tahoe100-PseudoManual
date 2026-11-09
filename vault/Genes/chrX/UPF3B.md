---
symbol: "UPF3B"
type: "gene"
col: 4603
ensembl_id: "ENSG00000125351"
name: "UPF3B regulator of nonsense mediated mRNA decay"
location: "Xq24"
module: 20
arm: "-"
pooled_cpm: 88.06
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# UPF3B

*UPF3B regulator of nonsense mediated mRNA decay* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.67× (z +23.7, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.226×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIB]] (+0.71, fdr 7e-06), [[PPIG]] (+0.70, fdr 7e-06), [[BDP1]] (+0.68, fdr 1e-05); moves opposite to [[FKBP1A]] (-0.69, fdr 7e-06), [[COLGALT1]] (-0.68, fdr 7e-06), [[SLC25A39]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PODXL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.67×** | +23.7 | 0e+00 | 48/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.67×** | +16.1 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.84×** | +13.5 | 5e-39 | 48/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.20×** | +10.2 | 3e-22 | 46/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.44×** | +9.8 | 1e-20 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.15×** | +9.5 | 2e-19 | 39/43 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.30×** | +9.1 | 5e-18 | 43/49 (SW480, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.63×** | +6.3 | 2e-08 | 37/48 (PANC-1, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.63×** | +6.3 | 2e-08 | 41/48 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.60×** | +6.1 | 7e-08 | 42/48 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +6.0 | 8e-08 | 41/47 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.64×** | +5.9 | 1e-07 | 30/45 (RKO, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +5.8 | 2e-07 | 39/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.59×** | +5.6 | 1e-06 | 37/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.42×** | +4.5 | 3e-04 | 32/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 4e-04 | 36/48 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 5e-04 | 30/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.004 | 32/48 (HT-29, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4603.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[TAK-901 (drug)]] 0.05 µM in 1 line (SW48 0.226×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.585× | -3.6 | 0.17 | 29/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.770× | -3.1 | 0.53 | 25/48 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 164 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +36.3) | — |
| [[NCI-H460 (line)]] | wt | 94.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +22.3) | — |
| [[A-427 (line)]] | wt | 86.7 | 5 | 0 | [[Harringtonine (drug)]] 5 µM 4.18× (z +13.9) | — |
| [[A549 (line)]] | wt | 101 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +24.3) | — |
| [[HEC-1-A (line)]] | alt | 67.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +22.0) | — |
| [[LS 180 (line)]] | wt | 62.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 123 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.6) | — |
| [[A498 (line)]] | wt | 93.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +23.7) | — |
| [[J82 (line)]] | alt | 111 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.50× (z +20.7) | — |
| [[KATO III (line)]] | alt | 92.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.3) | — |
| [[LoVo (line)]] | wt | 49.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 56.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.16× (z +27.5) | — |
| [[NCI-H2347 (line)]] | alt | 67.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +19.3) | — |
| [[SW48 (line)]] | wt | 77.5 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +13.5) | [[TAK-901 (drug)]] 0.05 µM 0.226× (z -8.9) |
| [[SW480 (line)]] | alt | 159 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.1) | — |
| [[A-172 (line)]] | wt | 38.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +19.4) | — |
| [[AsPC-1 (line)]] | alt | 59.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +23.6) | — |
| [[HOP62 (line)]] | alt | 73.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +17.5) | — |
| [[HS-578T (line)]] | alt | 52.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.4) | — |
| [[HT-29 (line)]] | alt | 85.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +16.8) | — |
| [[NCI-H1573 (line)]] | alt | 78.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +19.0) | — |
| [[NCI-H23 (line)]] | alt | 124 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 99.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +16.8) | — |
| [[RKO (line)]] | wt | 70.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +16.2) | — |
| [[SNU-1 (line)]] | wt | 62.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +13.9) | — |
| [[SW1417 (line)]] | alt | 107 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 39.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 68.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +18.1) | — |
| [[H4 (line)]] | wt | 65.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +15.8) | — |
| [[HCT15 (line)]] | alt | 103 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 94.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +14.4) | — |
| [[hTERT-HPNE (line)]] | wt | 53.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.34× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 56.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.3) | — |
| [[NCI-H1792 (line)]] | alt | 51.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 51.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +16.8) | — |
| [[SNU-423 (line)]] | alt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +20.1) | — |
| [[SW 900 (line)]] | alt | 48.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 167 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.9) | — |
| [[C32 (line)]] | wt | 43.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 165 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIB]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[PPIG]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 857 |
| [[BDP1]] | +0.68 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[CHMP4A]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[WBP4]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CCAR1]] | +0.67 | +0.78 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SEC62]] | +0.65 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[SNRNP27]] | +0.65 | +0.71 / +0.52 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SCAF11]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[WHAMM]] | +0.65 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[SRSF11]] ⚠ | +0.65 | +0.68 / +0.59 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 911; ⚠ in the vector space only through flagged drug-doses |
| [[GATAD1]] | +0.64 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FNBP4]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP1A]] | -0.69 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[COLGALT1]] | -0.68 | -0.73 / -0.64 | both halves | 7e-06 |  |
| [[SLC25A39]] | -0.66 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[MDH2]] | -0.64 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[NUTF2]] | -0.64 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[ARHGEF7]] | -0.64 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[ATP5F1B]] | -0.63 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[PHB1]] | -0.62 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[EIF3H]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.59 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ZDHHC3]] | -0.58 | -0.65 / -0.46 | both halves | 3e-05 |  |
| [[MATN3]] | -0.58 | -0.45 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PODXL2]] | B | PODXL2 activity raises UPF3B's level | lines that do not express PODXL2 (14) vs lines expressing it (36) | 1.26× lower at baseline in the lines without PODXL2 | 0.037 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.3, 1.7); signed map (2.2, -15.1). **Vector** length 106, 37.8% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.4 | +16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.0 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +23.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.0 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +1.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.1 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.6 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | +0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | UPF3B regulator of nonsense mediated mRNA decay |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,834,022-119,852,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RENT3B, UPF3X, HUPF3B, MRX82; previously MRX62, UPF3BP1, UPF3BP2, UPF3BP3 |
| Gene groups (HGNC) | DECID complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 13 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZI7](https://www.uniprot.org/uniprotkb/Q9BZI7) (Regulator of nonsense transcripts 3B):

> Involved in nonsense-mediated decay (NMD) of mRNAs containing premature stop codons by associating with the nuclear exon junction complex (EJC) and serving as link between the EJC core and NMD machinery. Recruits UPF2 at the cytoplasmic side of the nuclear envelope and the subsequent formation of an UPF1-UPF2-UPF3 surveillance complex (including UPF1 bound to release factors at the stalled ribosome) is believed to activate NMD. In cooperation with UPF2 stimulates both ATPase and RNA helicase …

**Summary**, from NCBI Gene [65109](https://www.ncbi.nlm.nih.gov/gene/65109):

> This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. The encoded protein is one of two functional homologs to yeast Upf3p. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons. This protein binds to the …

**Accessions** — [HGNC:20439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20439) · Entrez [65109](https://www.ncbi.nlm.nih.gov/gene/65109) · UniProt [Q9BZI7](https://www.uniprot.org/uniprotkb/Q9BZI7) · Ensembl [ENSG00000125351](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125351)

## Data

Gene col 4603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4603); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4603]; `tensor/DDL_lfc|DDL_z.npy` [4603]; `embed/gene_vectors.npy` [4603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4603 or target_col == 4603). Every well: [[UPF3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPF3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
