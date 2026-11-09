---
symbol: "COPB1"
type: "gene"
col: 4946
ensembl_id: "ENSG00000129083"
name: "coat protein complex I subunit beta 1"
location: "11p15.2"
module: 56
arm: "+"
pooled_cpm: 270.66
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# COPB1

*coat protein complex I subunit beta 1* — 11p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.73× (z +5.6, q 1e-05, up in 35 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (A498 2.65×); [[Salicylic acid (drug)]] 0.5 µM in 1 line (NCI-H596 4.13×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 2.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.609× (z -13.5, q 1e-38, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM263]] (+0.86, fdr 7e-06), [[SEC31A]] (+0.86, fdr 7e-06), [[COPA]] (+0.85, fdr 7e-06); moves opposite to [[TET3]] (-0.62, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4946.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (A498 2.65×); [[Salicylic acid (drug)]] 0.5 µM in 1 line (NCI-H596 4.13×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 2.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +5.6 | 1e-05 | 35/49 (A498, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.011 | 27/48 (A-427, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 1.38× | +3.4 | 0.13 | 26/48 (HS-578T, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.3 | 0.13 | 7/48 (HT-29, SW480, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.13 | 8/49 (C32, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -13.5 | 1e-38 | 42/49 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -9.6 | 3e-19 | 43/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.666×** | -8.0 | 3e-13 | 36/48 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -8.0 | 3e-13 | 29/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.671×** | -7.6 | 5e-12 | 39/47 (HT-29, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.664×** | -7.4 | 9e-12 | 32/45 (Panc 03.27, AsPC-1, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.769×** | -7.2 | 4e-11 | 40/48 (J82, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.693×** | -7.2 | 4e-11 | 36/48 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.706×** | -6.8 | 5e-10 | 35/48 (A498, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.711×** | -6.4 | 7e-09 | 41/48 (LoVo, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -6.1 | 6e-08 | 34/48 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -5.7 | 5e-07 | 36/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.752×** | -5.4 | 3e-06 | 32/48 (A498, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.769×** | -5.2 | 1e-05 | 36/48 (A-172, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.771×** | -5.1 | 1e-05 | 28/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.836× | -3.5 | 0.013 | 22/49 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.843× | -3.4 | 0.021 | 20/48 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.057 | 19/47 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 0.894× | -3.0 | 0.058 | 7/48 (HOP62, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 410 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.490× (z -15.7) |
| [[H4 (line)]] | wt | 576 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.290× (z -14.1) |
| [[A-172 (line)]] | wt | 352 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -19.0) |
| [[hTERT-HPNE (line)]] | wt | 332 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -14.8) |
| [[A498 (line)]] | wt | 477 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.65× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -22.9) |
| [[Hs 766T (line)]] | wt | 425 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.345× (z -13.3) |
| [[J82 (line)]] | alt | 396 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 360 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -22.4) |
| [[CFPAC-1 (line)]] | alt | 195 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -12.2) |
| [[HS-578T (line)]] | alt | 329 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 292 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.316× (z -15.2) |
| [[SNU-423 (line)]] | alt | 290 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -17.6) |
| [[HOP62 (line)]] | alt | 333 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -12.7) |
| [[HT-29 (line)]] | alt | 318 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 242 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[LoVo (line)]] | wt | 299 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.4) |
| [[SW1417 (line)]] | alt | 316 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -12.4) |
| [[HCT15 (line)]] | alt | 460 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -9.8) |
| [[HepG2_C3A (line)]] | wt | 189 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.426× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -8.6) |
| [[KATO III (line)]] | alt | 203 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.371× (z -10.9) |
| [[NCI-H596 (line)]] | alt | 249 | 1 | 1 | [[Salicylic acid (drug)]] 0.5 µM 4.13× (z +10.0) | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.261× (z -9.8) |
| [[SNU-1 (line)]] | wt | 274 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.455× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[A549 (line)]] | wt | 339 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -17.5) |
| [[AN3 CA (line)]] | alt | 204 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.7) |
| [[BT-474 (line)]] | alt | 207 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.598× (z -9.5) |
| [[C32 (line)]] | wt | 173 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 268 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 179 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 339 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 87.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 189 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.491× (z -8.5) |
| [[SW 900 (line)]] | alt | 144 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.486× (z -8.5) |
| [[SW480 (line)]] | alt | 248 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.471× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 159 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 173 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 259 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 218 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 387 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 283 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM263]] | +0.86 | +0.85 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SEC31A]] | +0.86 | +0.90 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 678 |
| [[COPA]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 999 |
| [[SEC24D]] | +0.84 | +0.88 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 659 |
| [[COG6]] | +0.84 | +0.86 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 404 |
| [[TBC1D23]] | +0.82 | +0.84 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[SEC23A]] | +0.81 | +0.83 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 607 |
| [[SRP54]] | +0.79 | +0.83 / +0.72 | both halves | 7e-06 | STRING 681 |
| [[KDELR2]] | +0.79 | +0.84 / +0.71 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 921 |
| [[PRRC1]] | +0.79 | +0.84 / +0.70 | both halves | 7e-06 | STRING 415 |
| [[ACBD3]] | +0.79 | +0.87 / +0.65 | both halves | 7e-06 |  |
| [[GFPT1]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TET3]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises COPB1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PTP4A3]] | B | PTP4A3 activity lowers COPB1's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.43× higher at baseline in the lines without PTP4A3 | 0.084 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[TMEM39A]] | C | TMEM39A's natural level strengthens COPB1's drug response | TMEM39A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.23; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.900). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -33.5); signed map (-51.2, 10.6). **Vector** length 139, 53.7% of its response variance represented; |z| ≥ 3 in 1,244 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *COPII-mediated vesicle transport* (reactome, mean cos +0.75 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.69 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.78 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +0.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.7 | -7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.1 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +2.7 | +2.8 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -8.0 | -4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.3 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.3 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -2.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.0 | -6.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.7 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -7.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.3 | -3.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.2 — chr11:14,443,440-14,500,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously COPB |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Coat protein complex I |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 11 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P53618](https://www.uniprot.org/uniprotkb/P53618) (Coatomer subunit beta):

> The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. Coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins. In mammals, the coatomer can only be recruited by membranes associated to ADP-ribosylation …

**Summary**, from NCBI Gene [1315](https://www.ncbi.nlm.nih.gov/gene/1315):

> This gene encodes a protein subunit of the coatomer complex associated with non-clathrin coated vesicles. The coatomer complex, also known as the coat protein complex 1, forms in the cytoplasm and is recruited to the Golgi by activated guanosine triphosphatases. Once at the Golgi membrane, the coatomer complex may assist in the movement of protein and lipid components back to the endoplasmic reticulum. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:2231](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2231) · Entrez [1315](https://www.ncbi.nlm.nih.gov/gene/1315) · UniProt [P53618](https://www.uniprot.org/uniprotkb/P53618) · Ensembl [ENSG00000129083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129083)

## Data

Gene col 4946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4946); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4946]; `tensor/DDL_lfc|DDL_z.npy` [4946]; `embed/gene_vectors.npy` [4946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4946 or target_col == 4946). Every well: [[COPB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
