---
symbol: "STPG1"
type: "gene"
col: 8
ensembl_id: "ENSG00000001460"
name: "sperm tail PG-rich repeat containing 1"
location: "1p36.11"
module: 221
arm: "+"
pooled_cpm: 10.31
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# STPG1

*sperm tail PG-rich repeat containing 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +8.6, q 6e-15, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.638× (z -6.6, q 3e-08, down in 18 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0458×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0766×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.115×; ⚠ cell-cycle shift, explains ~2% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2Q2P1]] (+0.59, fdr 5e-05), [[ZSCAN2]] (+0.58, fdr 1e-05), [[RWDD3]] (+0.55, fdr 3e-05); moves opposite to [[CFAP44]] (-0.54, fdr 4e-05), [[RALY]] (-0.53, fdr 1e-05), [[STAU1]] (-0.52, fdr 3e-05).
> It is in [[Module 221]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC00511]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +8.6 | 6e-15 | 25/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.4 | 5e-08 | 22/40 (CFPAC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 3e-07 | 22/44 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.8 | 7e-07 | 18/45 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +5.8 | 1e-06 | 19/46 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +5.6 | 3e-06 | 19/46 (HT-29, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 2e-05 | 15/46 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 2e-05 | 17/45 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.27×** | +4.8 | 1e-04 | 20/45 (RKO, LoVo, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.5 | 4e-04 | 15/43 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +4.4 | 6e-04 | 12/44 (LoVo, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.4 | 6e-04 | 16/46 (LS 180, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.002 | 6/47 (C-33 A, HCT15, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 14/46 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.002 | 9/45 (A-427, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.002 | 10/46 (HOP62, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.003 | 17/46 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.006 | 11/46 (C-33 A, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H460 0.0458×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0766×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.115×; ⚠ cell-cycle shift, explains ~2% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -6.6 | 3e-08 | 18/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.716×** | -4.9 | 3e-04 | 17/43 (NCI-H460, KATO III, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -4.3 | 0.003 | 12/44 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.2 | 0.17 | 1/47 (hTERT-HPNE) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | 0.799× | -3.2 | 0.17 | 12/41 (PANC-1, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0458× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[A-427 (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 8.73 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0791× (z -8.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LoVo (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -8.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -10.4) ⚠ cell-cycle shift, explains ~2% of this change |
| [[A-172 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2Q2P1]] | +0.59 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[ZSCAN2]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[IAH1]] | +0.54 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[BBS7]] | +0.53 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ZNF449]] | +0.53 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[LINC01012]] | +0.52 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | +0.52 | +0.59 / +0.37 | both halves | 9e-05 |  |
| [[NLRX1]] | +0.52 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[PFDN4]] | +0.51 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[AGO4]] | +0.50 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[UBA3]] | +0.49 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP44]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[RALY]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[STAU1]] | -0.52 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[EGR3]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[SCART1]] | -0.49 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[LINC00511]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ZDHHC11]] | -0.48 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[NUP98]] | -0.47 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[C5AR1]] | -0.46 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[IVNS1ABP]] | -0.44 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[PTBP1]] | -0.44 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[RAPGEF6]] | -0.44 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00511]] | B | LINC00511 activity strengthens STPG1's drug response | lines that do not express LINC00511 (11) vs lines expressing it (36) | the lines without LINC00511 respond 0.53× as strongly (z diff +0.71); strongest at Panobinostat 0.5 µM: 0.95x vs 1.47x (z diff +2.0) | 0.089 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18; target measured in part of the lines; artifact flags |
| [[OCIAD2]] | B | OCIAD2 activity lowers STPG1's level | lines that do not express OCIAD2 (10) vs lines expressing it (40) | 1.37× higher at baseline in the lines without OCIAD2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CDCP1, STAMBPL1, SLCO4A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.8, -2.7); signed map (-31.9, -5.4). **Vector** length 63.6, 9.95% of its response variance represented; |z| ≥ 3 in 847 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +6.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.5 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -2.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Cinacalcet (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | sperm tail PG-rich repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,356,999-24,416,934 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33340, MAPO2; previously C1orf201 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TH74](https://www.uniprot.org/uniprotkb/Q5TH74) (O(6)-methylguanine-induced apoptosis 2):

> May positively contribute to the induction of apoptosis triggered by O(6)-methylguanine.

**Summary**, from NCBI Gene [90529](https://www.ncbi.nlm.nih.gov/gene/90529):

> Involved in positive regulation of apoptotic process and positive regulation of mitochondrial membrane permeability involved in apoptotic process. Predicted to be located in mitochondrion and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28070) · Entrez [90529](https://www.ncbi.nlm.nih.gov/gene/90529) · UniProt [Q5TH74](https://www.uniprot.org/uniprotkb/Q5TH74) · Ensembl [ENSG00000001460](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001460)

## Data

Gene col 8: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8]; `tensor/DDL_lfc|DDL_z.npy` [8]; `embed/gene_vectors.npy` [8]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8 or target_col == 8). Every well: [[STPG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STPG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
