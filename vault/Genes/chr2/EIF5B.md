---
symbol: "EIF5B"
type: "gene"
col: 8159
ensembl_id: "ENSG00000158417"
name: "eukaryotic translation initiation factor 5B"
location: "2q11.2"
module: 29
arm: "-"
pooled_cpm: 294.7
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# EIF5B

*eukaryotic translation initiation factor 5B* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +8.9, q 2e-16, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.03× (z +7.6, q 9e-12, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.699× (z -3.8, q 0.061, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIFK]] (+0.72, fdr 7e-06), [[RBM25]] (+0.68, fdr 7e-06), [[ESF1]] (+0.65, fdr 7e-06); moves opposite to [[ITM2B]] (-0.67, fdr 7e-06), [[PGRMC1]] (-0.66, fdr 1e-05), [[SUMO3]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CD74]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.80×** | +8.9 | 2e-16 | 44/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +7.6 | 9e-12 | 46/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.04×** | +7.4 | 4e-11 | 47/48 (NCI-H1792, COLO 205, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.83×** | +6.5 | 1e-08 | 47/48 (NCI-H1792, H4, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.76×** | +5.9 | 5e-07 | 39/44 (SNU-423, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.7 | 1e-06 | 45/48 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +5.7 | 1e-06 | 41/48 (C32, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +5.7 | 1e-06 | 47/48 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.69×** | +5.7 | 1e-06 | 45/48 (SNU-423, H4, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.70×** | +5.5 | 2e-06 | 42/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.64×** | +5.3 | 5e-06 | 43/48 (COLO 205, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.61×** | +5.1 | 1e-05 | 39/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.71×** | +5.1 | 1e-05 | 40/49 (SNU-423, NCI-H1792, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **1.47×** | +4.2 | 0.001 | 43/48 (HT-29, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.1 | 0.002 | 37/48 (A549, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.004 | 37/49 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.051 | 27/48 (SNU-423, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.065 | 40/48 (C32, HT-29, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.67×** | +2.9 | 0.096 | 37/46 (C-33 A, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +2.9 | 0.096 | 31/48 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.699×** | -3.8 | 0.061 | 45/48 (J82, NCI-H23, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.784×** | -3.7 | 0.061 | 43/48 (BT-474, J82, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.726× | -3.4 | 0.11 | 41/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 285 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.72× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 197 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.7) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.93× (z +9.4) | — |
| [[A549 (line)]] | wt | 251 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.08× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 157 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 336 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 355 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 143 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +13.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.49× (z +9.2) | — |
| [[C32 (line)]] | wt | 197 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +16.7) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 201 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.61× (z +11.5) | — |
| [[H4 (line)]] | wt | 186 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.7) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 199 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 259 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +14.2) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.69× (z +11.5) | — |
| [[A498 (line)]] | wt | 331 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.9) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[BT-474 (line)]] | alt | 272 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.5) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[HEC-1-A (line)]] | alt | 367 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +8.9) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 188 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.1) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[LoVo (line)]] | wt | 323 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.3) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[LOX-IMVI (line)]] | wt | 296 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.94× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 413 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.68× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 211 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.7) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H460 (line)]] | wt | 301 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +8.9) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[Panc 03.27 (line)]] | alt | 275 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 327 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.2) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[SW480 (line)]] | alt | 377 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.69× (z +8.6) | — |
| [[A-172 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 326 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 307 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 376 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 291 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 345 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 194 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 204 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 338 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 187 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 312 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 355 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 233 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 512 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 284 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 369 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 377 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 325 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 307 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 403 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 364 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIFK]] | +0.72 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[RBM25]] | +0.68 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ESF1]] | +0.65 | +0.68 / +0.66 | both halves | 7e-06 | STRING 407 |
| [[ZC3H13]] | +0.65 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[CEBPZ]] | +0.64 | +0.65 / +0.66 | both halves | 7e-06 | STRING 630 |
| [[MAP7D3]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.63 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.63 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[KRI1]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SURF6]] | +0.60 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[NEMF]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2B]] | -0.67 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[PGRMC1]] | -0.66 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[NCSTN]] | -0.61 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[GNS]] | -0.61 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[ERMP1]] | -0.60 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[SCARB2]] | -0.60 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[VAMP1]] | -0.60 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.59 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[EPHX1]] | -0.59 | -0.27 / -0.55 | both halves | 3e-04 |  |
| [[HIPK1]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ITM2C]] | -0.58 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD74]] | B | CD74 activity lowers EIF5B's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.24× higher at baseline in the lines without CD74 | 0.091 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[SH3BGRL]] | C | SH3BGRL activity lowers EIF5B's level | lines that do not express SH3BGRL (4) vs lines expressing it (46) | 1.53× higher at baseline in the lines without SH3BGRL | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HMGN5, HIPK2, ATP10D |
| [[ABHD14B]] | C | ABHD14B's natural level weakens EIF5B's drug response | ABHD14B's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.08; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-39.6, -0.5); signed map (-1.8, -18.7). **Vector** length 95.4, 50.6% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +7.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +3.1 | +8.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.8 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.6 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | -4.4 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | -4.2 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:99,337,389-99,401,326 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IF2, KIAA0741, DKFZp434I036, FLJ10524 |
| Gene groups (HGNC) | Translational GTPases |
| Reactome | 4 pathways, smallest: GTP hydrolysis and joining of the 60S ribosomal subunit; Cap-dependent Translation Initiation; Eukaryotic Translation Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [O60841](https://www.uniprot.org/uniprotkb/O60841) (Eukaryotic translation initiation factor 5B):

> Plays a role in translation initiation. Ribosome-dependent GTPase that promotes the joining of the 60S ribosomal subunit to the pre-initiation complex to form the 80S initiation complex with the initiator methionine-tRNA in the P-site base paired to the start codon. Together with eIF1A (EIF1AX), actively orients the initiator methionine-tRNA in a conformation that allows 60S ribosomal subunit joining to form the 80S initiation complex. Is released after formation of the 80S initiation complex. …

**Summary**, from NCBI Gene [9669](https://www.ncbi.nlm.nih.gov/gene/9669):

> Accurate initiation of translation in eukaryotes is complex and requires many factors, some of which are composed of multiple subunits. The process is simpler in prokaryotes which have only three initiation factors (IF1, IF2, IF3). Two of these factors are conserved in eukaryotes: the homolog of IF1 is eIF1A and the homolog of IF2 is eIF5B. This gene encodes eIF5B. Factors eIF1A and eIF5B interact on the ribosome along with other initiation factors and GTP to position the initiation methionine …

**Accessions** — [HGNC:30793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30793) · Entrez [9669](https://www.ncbi.nlm.nih.gov/gene/9669) · UniProt [O60841](https://www.uniprot.org/uniprotkb/O60841) · Ensembl [ENSG00000158417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158417)

## Data

Gene col 8159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8159); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8159]; `tensor/DDL_lfc|DDL_z.npy` [8159]; `embed/gene_vectors.npy` [8159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8159 or target_col == 8159). Every well: [[EIF5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
