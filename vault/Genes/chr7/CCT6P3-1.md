---
symbol: "CCT6P3-1"
type: "gene"
col: 16517
ensembl_id: "ENSG00000290860"
name: ""
location: ""
module: 15
arm: "+"
pooled_cpm: 25.34
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CCT6P3-1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.298× (z -16.3, q 0e+00, down in 42 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.635× (z -6.1, q 9e-08, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFSD14CP]] (+0.74, fdr 7e-06), [[SMG1P5]] (+0.71, fdr 7e-06), [[SDHAP4-1]] (+0.70, fdr 7e-06); moves opposite to [[ZC3H11A]] (-0.66, fdr 1e-05), [[VEZF1]] (-0.61, fdr 1e-05), [[ZNF474]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APOBEC3A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.298×** | -16.3 | 0e+00 | 42/42 (A-172, KATO III, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.513×** | -12.7 | 2e-34 | 41/47 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.390×** | -11.7 | 2e-29 | 31/39 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.418×** | -11.3 | 3e-27 | 32/34 (J82, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.601×** | -6.8 | 9e-10 | 37/45 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -6.1 | 9e-08 | 32/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.624×** | -6.1 | 9e-08 | 33/48 (PANC-1, HS-578T, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -5.9 | 2e-07 | 29/47 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -5.6 | 1e-06 | 27/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.7 | 0.015 | 4/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -3.5 | 0.020 | 14/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -3.2 | 0.055 | 18/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **0.789×** | -3.2 | 0.062 | 18/46 (SW48, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.793×** | -3.1 | 0.077 | 19/48 (HS-578T, A498, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -3.0 | 0.091 | 13/48 (A-172, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 28.1 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0499× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -13.5) |
| [[HS-578T (line)]] | alt | 27.9 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -10.1) |
| [[PANC-1 (line)]] | alt | 45.0 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 18.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0734× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2347 (line)]] | alt | 29.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 30.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A549 (line)]] | wt | 25.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 34.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0908× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H1792 (line)]] | alt | 30.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -15.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.234× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 30.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 27.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 33.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -13.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[C32 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[CFPAC-1 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HepG2_C3A (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0927× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.9) ⚠ cell-cycle shift, explains ~40% of this change |
| [[HT-29 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[KATO III (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0581× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 30.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.425× (z -9.0) |
| [[SW480 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD14CP]] | +0.74 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[SMG1P5]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[UBE2G1]] | +0.69 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.68 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[E4F1]] | +0.67 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[EIF4ENIF1]] | +0.66 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[RNF38]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[STARD3]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZNF500]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TRPC4AP]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H11A]] | -0.66 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.61 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ZNF474]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ATP7A]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[SYNE1]] | -0.60 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[DARS1]] | -0.60 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPK]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPH2]] | -0.59 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.58 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[ZNF462]] | -0.57 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[SF3B1]] | -0.56 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[YWHAE]] | -0.56 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOBEC3A]] | B | APOBEC3A activity raises CCT6P3-1's level | lines that do not express APOBEC3A (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without APOBEC3A | 0.093 | ⚠ within organs, on part of the lines; also absent: PBX4, CTSV, APOBEC3B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.7, -5.6); signed map (-41.7, -0.3). **Vector** length 80.7, 16.3% of its response variance represented; |z| ≥ 3 in 932 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +0.7 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | +1.5 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -7.5 | -12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -5.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -4.6 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.5 | -16.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -4.2 | -11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

> [!warning] No registry record
> CCT6P3-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16517); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16517]; `tensor/DDL_lfc|DDL_z.npy` [16517]; `embed/gene_vectors.npy` [16517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16517 or target_col == 16517). Every well: [[CCT6P3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT6P3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
