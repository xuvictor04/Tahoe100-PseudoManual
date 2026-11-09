---
symbol: "METAP2"
type: "gene"
col: 3194
ensembl_id: "ENSG00000111142"
name: "methionyl aminopeptidase 2"
location: "12q22"
module: 11
arm: "+"
pooled_cpm: 138.77
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# METAP2

*methionyl aminopeptidase 2* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +8.7, q 1e-15, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~70% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.67× (z +7.7, q 3e-12, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.476×; ⚠ cell-cycle shift, explains ~3% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSL1D1]] (+0.62, fdr 1e-05), [[NPM1]] (+0.59, fdr 2e-05), [[DDX27]] (+0.56, fdr 1e-05); moves opposite to [[PRKACA]] (-0.62, fdr 7e-06), [[LSM4]] (-0.59, fdr 2e-05), [[CALM3]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RBM25]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.50×** | +8.7 | 1e-15 | 36/48 (AsPC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.7 | 3e-12 | 40/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +7.0 | 5e-10 | 44/48 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +6.4 | 3e-08 | 44/49 (COLO 205, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.52×** | +6.3 | 3e-08 | 40/49 (A498, A549, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.52×** | +6.2 | 7e-08 | 39/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +5.9 | 2e-07 | 41/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.44×** | +5.5 | 3e-06 | 42/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +5.0 | 3e-05 | 37/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.9 | 5e-05 | 37/48 (SW480, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.41×** | +4.8 | 9e-05 | 32/45 (A498, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.38×** | +4.7 | 1e-04 | 26/44 (A498, A549, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.37×** | +4.6 | 2e-04 | 36/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.35×** | +4.6 | 2e-04 | 32/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.33×** | +4.4 | 4e-04 | 27/48 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +4.1 | 0.001 | 34/48 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.002 | 28/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.003 | 36/47 (NCI-H23, NCI-H460, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.003 | 32/47 (NCI-H460, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.003 | 35/48 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.003 | 34/48 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.023 | 26/48 (NCI-H460, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.026 | 29/48 (SK-MEL-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.21×** | +2.9 | 0.069 | 21/48 (HT-29, C32, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.073 | 24/48 (MIA PaCa-2, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3194.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.476×; ⚠ cell-cycle shift, explains ~3% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 0.806× | -3.1 | 0.85 | 26/47 (RKO, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 172 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +12.8) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[A498 (line)]] | wt | 85.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.7) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 163 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.9) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.11× (z +9.0) | — |
| [[A549 (line)]] | wt | 157 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H1573 (line)]] | alt | 113 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +14.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 145 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.9) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 129 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +10.4) | — |
| [[C32 (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.9) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 78.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.8) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.14× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 117 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.2) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +8.7) | — |
| [[KATO III (line)]] | alt | 93.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.6) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 131 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.4) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[SW 900 (line)]] | alt | 128 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +9.6) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +10.4) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[CHP-212 (line)]] | wt | 200 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -8.9) ⚠ cell-cycle shift, explains ~3% of this change |
| [[HS-578T (line)]] | alt | 86.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.6) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[HT-29 (line)]] | alt | 99.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.6) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[LoVo (line)]] | wt | 170 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.33× (z +9.0) ⚠ toxic; cell-cycle shift, explains ~44% of this change | — |
| [[SNU-423 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.2) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[A-172 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 182 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 144 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 203 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 205 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 168 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 211 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 161 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSL1D1]] | +0.62 | +0.67 / +0.56 | both halves | 1e-05 | STRING 515 |
| [[NPM1]] | +0.59 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[DDX27]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MTIF2]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SNW1]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[UBE3A]] | +0.54 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[EIF3E]] | +0.54 | +0.41 / +0.60 | both halves | 4e-05 | STRING 446 |
| [[EIF3A]] | +0.53 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[REXO4]] | +0.53 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[MRPL21]] | +0.53 | +0.60 / +0.43 | both halves | 3e-05 | STRING 694 |
| [[DNAJC2]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[CEP290]] | +0.52 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKACA]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[LSM4]] | -0.59 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[CALM3]] | -0.50 | -0.65 / -0.28 | both halves | 3e-04 |  |
| [[PPIC]] | -0.50 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[CDK2]] | -0.49 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[CKS1B]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[NAXE]] | -0.45 | -0.51 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[AP2A1]] | -0.43 | -0.61 / -0.28 | both halves | 3e-04 |  |
| [[SKA2]] | -0.43 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM25]] | C | RBM25's natural level weakens METAP2's drug response | RBM25's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.17; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.357). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-24.2, -40.8); signed map (-2.2, -17.8). **Vector** length 78.7, 25.8% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.5 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +7.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.3 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +5.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -4.8 | +4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -4.7 | +4.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[Riluzole hydrochloride (drug)]] 0.05 µM |  | -1.3 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.3 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.2 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | methionyl aminopeptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:95,473,520-95,515,839 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MNPEP, p67, MAP2 |
| Gene groups (HGNC) | Aminopeptidases; M24 metallopeptidase family |
| Reactome | 4 pathways, smallest: Inactivation, recovery and regulation of the phototransduction cascade; The phototransduction cascade; Visual phototransduction |
| Matched by | ensembl_id |

**Function**, from UniProt [P50579](https://www.uniprot.org/uniprotkb/P50579) (Methionine aminopeptidase 2):

> Cotranslationally removes the N-terminal methionine from nascent proteins. The N-terminal methionine is often cleaved when the second residue in the primary sequence is small and uncharged (Met-Ala-, Cys, Gly, Pro, Ser, Thr, or Val). The catalytic activity of human METAP2 toward Met-Val peptides is consistently two orders of magnitude higher than that of METAP1, suggesting that it is responsible for processing proteins containing N-terminal Met-Val and Met-Thr sequences in vivo.; Protects …

**Summary**, from NCBI Gene [10988](https://www.ncbi.nlm.nih.gov/gene/10988):

> The protein encoded by this gene is a member of the methionyl aminopeptidase family. The encoded protein functions both by protecting the alpha subunit of eukaryotic initiation factor 2 from inhibitory phosphorylation and by removing the amino-terminal methionine residue from nascent proteins. Increased expression of this gene is associated with various forms of cancer, and the anti-cancer drugs fumagillin and ovalicin inhibit the protein by irreversibly binding to its active site. Inhibitors …

**Accessions** — [HGNC:16672](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16672) · Entrez [10988](https://www.ncbi.nlm.nih.gov/gene/10988) · UniProt [P50579](https://www.uniprot.org/uniprotkb/P50579) · Ensembl [ENSG00000111142](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111142)

## Data

Gene col 3194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3194); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3194]; `tensor/DDL_lfc|DDL_z.npy` [3194]; `embed/gene_vectors.npy` [3194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3194 or target_col == 3194). Every well: [[METAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
