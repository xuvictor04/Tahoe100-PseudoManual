---
symbol: "PJA2"
type: "gene"
col: 12758
ensembl_id: "ENSG00000198961"
name: "praja ring finger ubiquitin ligase 2"
location: "5q21.3"
module: 5
arm: "-"
pooled_cpm: 250.67
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PJA2

*praja ring finger ubiquitin ligase 2* — 5q21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.596× (z -13.4, q 4e-38, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUCO]] (+0.78, fdr 7e-06), [[ARL3]] (+0.77, fdr 1e-05), [[GMCL1]] (+0.70, fdr 2e-05); moves opposite to [[DHX37]] (-0.75, fdr 7e-06), [[UTP20]] (-0.74, fdr 7e-06), [[ZNF124]] (-0.73, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.23× | +3.7 | 0.10 | 24/49 (NCI-H2030, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 1.43× | +3.6 | 0.10 | 27/49 (C32, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.26× | +3.2 | 0.29 | 24/48 (SW 900, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -13.4 | 4e-38 | 43/49 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.515×** | -12.1 | 5e-31 | 45/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.547×** | -11.0 | 1e-25 | 39/44 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.622×** | -9.0 | 4e-17 | 40/49 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.739×** | -7.9 | 2e-13 | 41/48 (HS-578T, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -7.7 | 2e-12 | 38/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -7.5 | 5e-12 | 31/48 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.675×** | -7.4 | 8e-12 | 31/48 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.697×** | -6.8 | 6e-10 | 39/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -5.9 | 2e-07 | 33/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.721×** | -5.7 | 5e-07 | 33/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.765×** | -4.9 | 5e-05 | 29/50 (NCI-H460, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -4.7 | 1e-04 | 33/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.775×** | -4.5 | 2e-04 | 34/47 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.645×** | -4.3 | 5e-04 | 36/48 (NCI-H460, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.795×** | -4.3 | 5e-04 | 31/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.806×** | -3.9 | 0.003 | 26/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.750×** | -3.9 | 0.003 | 32/48 (RPMI-7951, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.824×** | -3.6 | 0.007 | 27/48 (LS 180, RPMI-7951, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.701×** | -3.5 | 0.011 | 25/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.020 | 22/48 (HT-29, C32, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.842× | -3.2 | 0.027 | 21/48 (SW 1088, BT-474, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 426 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -23.2) |
| [[NCI-H460 (line)]] | wt | 389 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -18.7) |
| [[C32 (line)]] | wt | 357 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -15.7) |
| [[HS-578T (line)]] | alt | 408 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 319 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -20.1) |
| [[NCI-H2347 (line)]] | alt | 496 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -13.9) |
| [[SW 900 (line)]] | alt | 283 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 327 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -16.4) |
| [[HOP62 (line)]] | alt | 330 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -16.9) |
| [[AN3 CA (line)]] | alt | 274 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -10.5) |
| [[H4 (line)]] | wt | 298 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 295 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 249 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 213 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.253× (z -10.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.9) |
| [[PANC-1 (line)]] | alt | 181 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 346 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.5) |
| [[A-172 (line)]] | wt | 275 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -13.5) |
| [[A-427 (line)]] | wt | 235 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.452× (z -11.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 308 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -8.9) |
| [[KATO III (line)]] | alt | 129 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 277 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -12.4) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 199 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 177 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -18.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 235 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -11.2) |
| [[SW480 (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.486× (z -9.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.5) |
| [[A549 (line)]] | wt | 205 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -12.5) |
| [[CHP-212 (line)]] | wt | 237 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.3) |
| [[COLO 205 (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.370× (z -8.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 179 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.0) |
| [[Hs 766T (line)]] | wt | 336 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 222 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.456× (z -9.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 299 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -11.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 319 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -16.8) |
| [[SW 1088 (line)]] | alt | 366 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -8.5) |
| [[SW 1271 (line)]] | alt | 351 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -8.5) |
| [[A498 (line)]] | wt | 238 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 156 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUCO]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[ARL3]] | +0.77 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.70 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[TTC3]] | +0.70 | +0.72 / +0.53 | both halves | 1e-05 | same gene group |
| [[MXI1]] | +0.68 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[YIF1B]] | +0.68 | +0.70 / +0.29 | both halves | 2e-04 |  |
| [[LMAN1]] | +0.68 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[ANG]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[MINDY2]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.67 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[RAB3A]] | +0.67 | +0.57 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX37]] | -0.75 | -0.74 / -0.65 | both halves | 7e-06 |  |
| [[UTP20]] | -0.74 | -0.75 / -0.59 | both halves | 7e-06 |  |
| [[ZNF124]] | -0.73 | -0.76 / -0.53 | both halves | 1e-05 |  |
| [[NOP56]] | -0.72 | -0.81 / -0.59 | both halves | 7e-06 |  |
| [[ITPA]] | -0.72 | -0.75 / -0.46 | both halves | 2e-05 |  |
| [[E2F3]] | -0.69 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.68 | -0.73 / -0.57 | both halves | 8e-06 |  |
| [[AVEN]] | -0.67 | -0.67 / -0.43 | both halves | 3e-05 |  |
| [[PRRC2B]] | -0.67 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[GABPB1]] | -0.65 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[DNAJC11]] | -0.65 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[METTL8]] | -0.65 | -0.65 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PJA2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[METTL8]] | C | METTL8's natural level weakens PJA2's drug response | METTL8's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.61, reverse +0.11; direction not clear | 0.088 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (1.9, -31.3); signed map (-33.2, 16.2). **Vector** length 143, 53.3% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +8.7 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.6 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.7 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +7.1 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.8 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +0.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.7 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.0 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -6.7 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.7 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.5 | -12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -7.9 |
|  | [[EX229 (drug)]] 5 µM |  | -4.9 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.2 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | praja ring finger ubiquitin ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q21.3 — chr5:109,334,713-109,409,974 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0438, Neurodap1, PRAJA2; previously RNF131 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O43164](https://www.uniprot.org/uniprotkb/O43164) (E3 ubiquitin-protein ligase Praja-2):

> Has E2-dependent E3 ubiquitin-protein ligase activity. Responsible for ubiquitination of cAMP-dependent protein kinase type I and type II-alpha/beta regulatory subunits and for targeting them for proteasomal degradation. Essential for PKA-mediated long-term memory processes. Through the ubiquitination of MFHAS1, positively regulates the TLR2 signaling pathway that leads to the activation of the downstream p38 and JNK MAP kinases and promotes the polarization of macrophages toward the …

**Summary**, from NCBI Gene [9867](https://www.ncbi.nlm.nih.gov/gene/9867):

> Enables cAMP-dependent protein kinase inhibitor activity and ubiquitin protein ligase activity. Involved in several processes, including positive regulation of signal transduction; proteasome-mediated ubiquitin-dependent protein catabolic process; and regulation of macrophage activation. Located in centriolar satellite; cytosol; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17481) · Entrez [9867](https://www.ncbi.nlm.nih.gov/gene/9867) · UniProt [O43164](https://www.uniprot.org/uniprotkb/O43164) · Ensembl [ENSG00000198961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198961)

## Data

Gene col 12758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12758); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12758]; `tensor/DDL_lfc|DDL_z.npy` [12758]; `embed/gene_vectors.npy` [12758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12758 or target_col == 12758). Every well: [[PJA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PJA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
