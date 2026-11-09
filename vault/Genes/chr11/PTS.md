---
symbol: "PTS"
type: "gene"
col: 7464
ensembl_id: "ENSG00000150787"
name: "6-pyruvoyltetrahydropterin synthase"
location: "11q23.1"
module: 15
arm: "+"
pooled_cpm: 46.11
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PTS

*6-pyruvoyltetrahydropterin synthase* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +15.6, q 0e+00, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.770× (z -6.2, q 3e-07, down in 20 of 41 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H1792 0.346×, PANC-1 0.455×, SNU-423 0.419×, Panc 03.27 0.380×, …; ⚠ cell-cycle shift, explains ~54% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.0390×, HEC-1-A 0.302×, NCI-H2030 0.466×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.121×, HepG2/C3A 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (CHP-212 0.122×); [[venetoclax (drug)]] 5 µM in 1 line (COLO 205 0.0906×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA1]] (+0.62, fdr 6e-05), [[ZNF418]] (+0.59, fdr 2e-05), [[CAPN10-DT]] (+0.58, fdr 1e-05); moves opposite to [[AKAP11]] (-0.47, fdr 3e-05), [[SERBP1]] (-0.46, fdr 1e-04), [[CPT1A]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Volasertib (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7464.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +15.6 | 0e+00 | 37/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.24×** | +5.1 | 1e-04 | 23/47 (NCI-H2347, Hs 766T, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.7 | 0.039 | 14/35 (SNU-423, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.4 | 0.065 | 7/48 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.4 | 0.065 | 13/48 (KATO III, SW480, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.065 | 8/48 (A498, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.065 | 12/49 (A498, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.14× | +3.0 | 0.17 | 10/48 (SK-MEL-2, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7464.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (NCI-H1792 0.346×, PANC-1 0.455×, SNU-423 0.419×, Panc 03.27 0.380×, …; ⚠ cell-cycle shift, explains ~54% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.0390×, HEC-1-A 0.302×, NCI-H2030 0.466×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SNU-1 0.121×, HepG2/C3A 0.236×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (CHP-212 0.122×); [[venetoclax (drug)]] 5 µM in 1 line (COLO 205 0.0906×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.770×** | -6.2 | 3e-07 | 20/41 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.862× | -5.2 | 7e-05 | 24/48 (NCI-H1792, PANC-1, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7464. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 44.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.302× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 64.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.466× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 32.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[PANC-1 (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -14.0) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SHP-77 (line)]] | alt | 58.2 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +9.5) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0998× (z -16.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 41.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.122× (z -10.4) |
| [[COLO 205 (line)]] | alt | 35.0 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0906× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 62.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[LS 180 (line)]] | wt | 95.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0390× (z -27.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 50.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.8) ⚠ cell-cycle shift, explains ~54% of this change |
| [[NCI-H23 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.467× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 47.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.618× (z -9.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SNU-1 (line)]] | wt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -10.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 55.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +14.1) | — |
| [[A-172 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 100.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7464), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA1]] | +0.62 | +0.38 / +0.65 | both halves | 6e-05 |  |
| [[ZNF418]] | +0.59 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[CAPN10-DT]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[MIR762HG]] | +0.56 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[CDC20-DT]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[WDR20]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[GLUD1P3]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SPAG7]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[SOS2]] | +0.55 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ANKUB1]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[UBOX5-AS1]] | +0.54 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[CCT6P3-1]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.47 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.46 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[CPT1A]] | -0.45 | -0.33 / -0.37 | both halves | 1e-04 | pathway: HALLMARK_FATTY_ACID_METABOLISM |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Volasertib (drug)]] 0.5 µM | C | PTS's natural level raises the cells' numbers under Volasertib 0.5 µM (protects the cells) | PTS's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.291 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | PTS's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | PTS's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.483 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.6, 23.2); signed map (3.0, -0.2). **Vector** length 92.9, 19.4% of its response variance represented; |z| ≥ 3 in 708 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +15.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | +6.2 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +1.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.1 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.7 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.5 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Tofacitinib (drug)]] 0.05 µM |  | -1.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | 6-pyruvoyltetrahydropterin synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:112,226,367-112,269,955 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTPS |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Hallmark sets | FATTY_ACID_METABOLISM, XENOBIOTIC_METABOLISM |
| Reactome | 3 pathways, smallest: Tetrahydrobiopterin (BH4) synthesis, recycling, salvage and regulation; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03393](https://www.uniprot.org/uniprotkb/Q03393) (6-pyruvoyl tetrahydrobiopterin synthase):

> Involved in the biosynthesis of tetrahydrobiopterin, an essential cofactor of aromatic amino acid hydroxylases. Catalyzes the transformation of 7,8-dihydroneopterin triphosphate into 6-pyruvoyl tetrahydropterin.

**Summary**, from NCBI Gene [5805](https://www.ncbi.nlm.nih.gov/gene/5805):

> The enzyme encoded by this gene catalyzes the elimination of inorganic triphosphate from dihydroneopterin triphosphate, which is the second and irreversible step in the biosynthesis of tetrahydrobiopterin from GTP. Tetrahydrobiopterin, also known as BH(4), is an essential cofactor and regulator of various enzyme activities, including enzymes involved in serotonin biosynthesis and NO synthase activity. Mutations in this gene result in hyperphenylalaninemia. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:9689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9689) · Entrez [5805](https://www.ncbi.nlm.nih.gov/gene/5805) · UniProt [Q03393](https://www.uniprot.org/uniprotkb/Q03393) · Ensembl [ENSG00000150787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150787)

## Data

Gene col 7464: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7464); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7464, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7464]; `tensor/DDL_lfc|DDL_z.npy` [7464]; `embed/gene_vectors.npy` [7464]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7464 or target_col == 7464). Every well: [[PTS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
