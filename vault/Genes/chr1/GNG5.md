---
symbol: "GNG5"
type: "gene"
col: 10455
ensembl_id: "ENSG00000174021"
name: "G protein subunit gamma 5"
location: "1p22.3"
module: 25
arm: "-"
pooled_cpm: 43.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GNG5

*G protein subunit gamma 5* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.99× (z +8.4, q 3e-14, up in 42 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 3.80×, SW480 3.42×, NCI-H460 4.02×, AsPC-1 2.94×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (NCI-H460 4.91×, PANC-1 3.23×, SW480 3.09×, AsPC-1 2.75×; ⚠ cell-cycle shift, explains ~42% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 2.70×, NCI-H460 3.23×; ⚠ cell-cycle shift, explains ~31% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.473× (z -9.2, q 2e-17, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERVK3-1]] (+0.60, fdr 4e-05), [[ATP6V0C]] (+0.54, fdr 4e-05), [[EIF1B]] (+0.54, fdr 3e-05); moves opposite to [[USP5]] (-0.55, fdr 7e-05), [[RANBP3]] (-0.52, fdr 5e-05), [[TRMU]] (-0.51, fdr 4e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10455.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 4 lines (PANC-1 3.80×, SW480 3.42×, NCI-H460 4.02×, AsPC-1 2.94×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 4 lines (NCI-H460 4.91×, PANC-1 3.23×, SW480 3.09×, AsPC-1 2.75×; ⚠ cell-cycle shift, explains ~42% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (SW480 2.70×, NCI-H460 3.23×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.99×** | +8.4 | 3e-14 | 42/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.77×** | +6.0 | 4e-07 | 35/46 (PANC-1, A-427, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.63×** | +6.0 | 4e-07 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.54×** | +5.2 | 2e-05 | 33/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.54×** | +5.1 | 4e-05 | 29/47 (PANC-1, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +4.7 | 3e-04 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.39×** | +3.7 | 0.017 | 24/44 (PANC-1, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.31×** | +3.3 | 0.051 | 23/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.33×** | +3.3 | 0.051 | 21/38 (Hs 766T, NCI-H1792, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.3 | 0.051 | 21/45 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.473×** | -9.2 | 2e-17 | 43/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.582×** | -6.7 | 8e-09 | 40/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.628×** | -5.7 | 2e-06 | 37/48 (AsPC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -4.7 | 4e-04 | 31/47 (LS 180, SW48, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.709×** | -4.2 | 0.003 | 31/48 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -3.9 | 0.011 | 29/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.590×** | -3.4 | 0.056 | 28/48 (AsPC-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -3.1 | 0.13 | 24/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.773× | -3.1 | 0.13 | 23/48 (AN3 CA, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.13 | 21/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.7 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +12.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[AsPC-1 (line)]] | alt | 61.6 | 2 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.94× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.281× (z -12.0) |
| [[PANC-1 (line)]] | alt | 80.7 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.80× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW480 (line)]] | alt | 38.3 | 3 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.42× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.393× (z -8.9) |
| [[HS-578T (line)]] | alt | 60.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.307× (z -11.1) |
| [[AN3 CA (line)]] | alt | 53.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -9.1) |
| [[H4 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.157× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~86% of this change |
| [[LS 180 (line)]] | wt | 46.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 39.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 34.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -8.5) |
| [[A-172 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK3-1]] | +0.60 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[ATP6V0C]] | +0.54 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[EIF1B]] | +0.54 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[TUBB2A]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 | pathway: Chaperonin-mediated protein folding |
| [[SERTAD1]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[SHOC2]] | +0.52 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[LRCH3]] | +0.51 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[NOP10]] ⚠ | +0.50 | +0.48 / +0.53 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SS18L2]] | +0.50 | +0.28 / +0.41 | both halves | 3e-04 |  |
| [[BRAF]] | +0.50 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[FAM241A]] | +0.49 | +0.52 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[S100A11]] | +0.49 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PEAK1]] | +0.49 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[DYNLL1]] | +0.48 | +0.26 / +0.47 | both halves | 4e-04 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP5]] | -0.55 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[RANBP3]] | -0.52 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TRMU]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[GFM2]] | -0.50 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[SNRNP200]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[NUDC]] | -0.49 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[XPO7]] | -0.49 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[DDX54]] | -0.48 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[ELAVL1]] | -0.48 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[XRCC6]] | -0.48 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[TCOF1]] | -0.48 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[PRPF8]] | -0.47 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GNG5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.273). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-11.5, -47.6); signed map (-8.0, 7.9). **Vector** length 64.7, 14.8% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.8 | +6.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.7 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.2 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.0 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.5 | +4.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.4 | +1.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +0.7 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +0.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.1 | +2.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -1.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.3 — chr1:84,498,323-84,506,581 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits gamma |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [P63218](https://www.uniprot.org/uniprotkb/P63218) (Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-5):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems. The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction.

**Summary**, from NCBI Gene [2787](https://www.ncbi.nlm.nih.gov/gene/2787):

> G proteins are trimeric (alpha-beta-gamma) membrane-associated proteins that regulate flow of information from cell surface receptors to a variety of internal metabolic effectors. Interaction of a G protein with its activated receptor promotes exchange of GTP for GDP that is bound to the alpha subunit. The alpha-GTP complex dissociates from the beta-gamma heterodimer so that the subunits, in turn, may interact with and regulate effector molecules (Gilman, 1987 [PubMed 3113327]; summary by Ahmad …

**Accessions** — [HGNC:4408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4408) · Entrez [2787](https://www.ncbi.nlm.nih.gov/gene/2787) · UniProt [P63218](https://www.uniprot.org/uniprotkb/P63218) · Ensembl [ENSG00000174021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174021)

## Data

Gene col 10455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10455); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10455]; `tensor/DDL_lfc|DDL_z.npy` [10455]; `embed/gene_vectors.npy` [10455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10455 or target_col == 10455). Every well: [[GNG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
