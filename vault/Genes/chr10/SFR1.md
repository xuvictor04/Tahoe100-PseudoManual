---
symbol: "SFR1"
type: "gene"
col: 7974
ensembl_id: "ENSG00000156384"
name: "SWI5 dependent homologous recombination repair protein 1"
location: "10q25.1"
module: 158
arm: "+"
pooled_cpm: 8.05
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# SFR1

*SWI5 dependent homologous recombination repair protein 1* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.44× (z +14.4, q 4e-44, up in 30 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.669× (z -4.6, q 0.002, down in 20 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.0680×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.132×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLDA1]] (+0.64, fdr 1e-05), [[SAV1]] (+0.64, fdr 7e-06), [[BCL10]] (+0.62, fdr 1e-05); moves opposite to [[NDUFAF7]] (-0.61, fdr 1e-05), [[DCUN1D5]] (-0.60, fdr 1e-05), [[C8orf76]] (-0.59, fdr 1e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[COL17A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.44×** | +14.4 | 4e-44 | 30/39 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.49×** | +10.0 | 5e-21 | 32/45 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +8.7 | 7e-16 | 30/41 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +8.1 | 1e-13 | 31/46 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.75×** | +6.3 | 3e-08 | 11/28 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.76×** | +6.2 | 6e-08 | 6/14 (A549, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.71×** | +6.1 | 9e-08 | 22/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.9 | 3e-07 | 18/47 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.6 | 2e-06 | 12/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.59×** | +5.3 | 7e-06 | 16/47 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.57×** | +4.7 | 1e-04 | 11/22 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.5 | 3e-04 | 15/45 (SW1417, NCI-H2347, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.1 | 0.002 | 12/37 (SNU-423, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.002 | 12/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.43×** | +4.0 | 0.002 | 12/46 (A498, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.7 | 0.008 | 13/43 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.029 | 5/44 (MIA PaCa-2, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.055 | 4/43 (hTERT-HPNE, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (LS 180 0.0680×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.132×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -4.6 | 0.002 | 20/46 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.786×** | -3.9 | 0.023 | 15/45 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.716×** | -3.8 | 0.023 | 18/40 (LS 180, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.720×** | -3.6 | 0.049 | 18/42 (MIA PaCa-2, SW48, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.755× | -3.2 | 0.13 | 17/47 (SHP-77, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.757× | -3.2 | 0.13 | 11/46 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 0.762× | -3.1 | 0.14 | 7/41 (J82, HCT15, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 14.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +11.9) | — |
| [[A-172 (line)]] | wt | 4.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +11.0) | — |
| [[A498 (line)]] | wt | 4.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 22.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 5.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +11.6) | — |
| [[LoVo (line)]] | wt | 9.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 4.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 8.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0680× (z -11.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 5.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +13.3) | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDA1]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SAV1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[BCL10]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[SOX9]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ICAM2]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ZNF217]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ARL14]] | +0.59 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[NAB1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[LINC00460]] | +0.58 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[GALE]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[IER3]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | -0.61 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[DCUN1D5]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.59 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.59 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[PGS1]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[GAPVD1]] | -0.58 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ATPAF2]] | -0.57 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[ADPGK]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[GLB1]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[MZT2A]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[EIF4ENIF1]] | -0.56 | -0.46 / -0.65 | both halves | 2e-05 |  |
| [[DCUN1D2]] | -0.56 | -0.65 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL17A1]] | B | COL17A1 activity raises SFR1's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without COL17A1 | 0.037 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[SHH]] | B | SHH activity raises SFR1's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without SHH | 0.048 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[PSMB5]] | B | PSMB5 activity raises SFR1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EHF]] | B | EHF activity raises SFR1's level | lines that do not express EHF (27) vs lines expressing it (23) | 1.68× lower at baseline in the lines without EHF | 0.059 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[CYP3A5]] | B | CYP3A5 activity raises SFR1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 1.60× lower at baseline in the lines without CYP3A5 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[AGPAT4]] | C | AGPAT4's natural level strengthens SFR1's drug response | AGPAT4's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.71, reverse -0.09; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.3, 2.6); signed map (6.7, 23.6). **Vector** length 85.3, 17.0% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +14.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +4.1 |
|  | [[Thymol (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.5 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.9 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SWI5 dependent homologous recombination repair protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,122,058-104,126,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEI5, bA373N18.1, FLJ41960; previously C10orf78, MEIR5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XK3](https://www.uniprot.org/uniprotkb/Q86XK3) (Swi5-dependent recombination DNA repair protein 1 homolog):

> Component of the SWI5-SFR1 complex, a complex required for double-strand break repair via homologous recombination. Acts as a transcriptional modulator for ESR1.

**Summary**, from NCBI Gene [119392](https://www.ncbi.nlm.nih.gov/gene/119392):

> Enables transcription coactivator activity. Involved in cellular response to estrogen stimulus; double-strand break repair via homologous recombination; and positive regulation of DNA-templated transcription. Located in nucleolus and nucleoplasm. Part of Swi5-Sfr1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29574) · Entrez [119392](https://www.ncbi.nlm.nih.gov/gene/119392) · UniProt [Q86XK3](https://www.uniprot.org/uniprotkb/Q86XK3) · Ensembl [ENSG00000156384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156384)

## Data

Gene col 7974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7974); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7974]; `tensor/DDL_lfc|DDL_z.npy` [7974]; `embed/gene_vectors.npy` [7974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7974 or target_col == 7974). Every well: [[SFR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
