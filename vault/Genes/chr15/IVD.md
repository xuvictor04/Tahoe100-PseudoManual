---
symbol: "IVD"
type: "gene"
col: 4934
ensembl_id: "ENSG00000128928"
name: "isovaleryl-CoA dehydrogenase"
location: "15q15.1"
module: 67
arm: "+"
pooled_cpm: 31.9
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# IVD

*isovaleryl-CoA dehydrogenase* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.36× (z +5.8, q 5e-06, up in 21 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.18× (z +4.5, q 8e-04, up in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 6.20×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 3.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.634× (z -9.0, q 2e-16, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RCCD1]] (+0.55, fdr 2e-05), [[NIF3L1]] (+0.52, fdr 2e-04), [[HSPA14]] (+0.52, fdr 6e-05); moves opposite to [[SH3GL2]] (-0.52, fdr 1e-04), [[RPS6KA6]] (-0.49, fdr 2e-04), [[ELOVL7]] (-0.49, fdr 2e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDLIM3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4934.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 6.20×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 3.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.36×** | +5.8 | 5e-06 | 21/38 (NCI-H1792, C-33 A, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +5.5 | 1e-05 | 22/47 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +5.3 | 2e-05 | 25/47 (NCI-H23, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.29×** | +5.0 | 8e-05 | 21/43 (KATO III, NCI-H1792, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.5 | 8e-04 | 19/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.25×** | +4.4 | 1e-03 | 17/46 (NCI-H460, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.15× | +3.9 | 0.009 | 15/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.017 | 17/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.19× | +3.4 | 0.037 | 16/48 (LoVo, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.4 | 0.038 | 15/48 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | 1.20× | +3.4 | 0.038 | 19/46 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.18× | +3.3 | 0.047 | 15/48 (LoVo, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.17× | +3.0 | 0.11 | 19/48 (SW480, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -9.0 | 2e-16 | 32/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.460×** | -8.0 | 4e-13 | 39/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.775×** | -7.1 | 3e-10 | 25/48 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -6.6 | 4e-09 | 27/48 (PANC-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.733×** | -5.9 | 5e-07 | 24/47 (A-172, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.734×** | -5.9 | 5e-07 | 26/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -5.3 | 9e-06 | 25/48 (PANC-1, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -5.1 | 2e-05 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.784×** | -4.8 | 1e-04 | 22/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.793×** | -4.6 | 3e-04 | 22/47 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.826×** | -3.8 | 0.009 | 18/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.698×** | -3.7 | 0.010 | 18/47 (Hs 766T, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.829×** | -3.7 | 0.010 | 20/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -3.0 | 0.099 | 18/48 (NCI-H460, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 42.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -18.1) |
| [[NCI-H460 (line)]] | wt | 32.9 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -11.6) |
| [[J82 (line)]] | alt | 34.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.316× (z -9.9) |
| [[SNU-1 (line)]] | wt | 64.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 9.55 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.136× (z -9.5) |
| [[A-172 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.308× (z -9.8) ⚠ toxic |
| [[C32 (line)]] | wt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.9) |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0749× (z -8.5) |
| [[HT-29 (line)]] | alt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -9.5) |
| [[KATO III (line)]] | alt | 42.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +13.1) | — |
| [[RKO (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.240× (z -9.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 49.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.6) |
| [[A-427 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCCD1]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[NIF3L1]] | +0.52 | +0.29 / +0.57 | both halves | 2e-04 |  |
| [[HSPA14]] | +0.52 | +0.38 / +0.51 | both halves | 6e-05 |  |
| [[ANKRD16]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[DTYMK]] | +0.51 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[EXOSC7]] | +0.51 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[ANAPC1]] | +0.51 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[PAK6]] | +0.50 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SCLY]] | +0.50 | +0.45 / +0.54 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |
| [[OIP5]] | +0.49 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[DNAAF10]] | +0.49 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[LIN9]] | +0.49 | +0.41 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3GL2]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[RPS6KA6]] | -0.49 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[ELOVL7]] | -0.49 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[RHOB]] | -0.46 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[ACHE]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PDLIM3]] | -0.45 | -0.29 / -0.38 | both halves | 3e-04 |  |
| [[CD2AP]] | -0.45 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[KIDINS220]] | -0.45 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[KLF5]] | -0.45 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[TPPP]] | -0.44 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[PLCL1]] | -0.44 | -0.17 / -0.42 | ⚠ not reproduced | 0.001 |  |
| [[TUBB2A]] | -0.44 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[PPL]] | -0.44 | -0.25 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDLIM3]] | B | PDLIM3 activity lowers IVD's level | lines that do not express PDLIM3 (18) vs lines expressing it (32) | 1.08× higher at baseline in the lines without PDLIM3 | 0.080 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, SOX5, PTX3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.379). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.7, -40.3); signed map (-40.0, -38.9). **Vector** length 71.5, 12.7% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.2 | +5.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.1 | +3.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~20% of this change | +1.9 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +1.6 | +5.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +0.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.2 | +2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.2 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.4 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -5.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | isovaleryl-CoA dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,405,485-40,435,947 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACAD2, IVDH |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Reactome | 4 pathways, smallest: Diseases of branched-chain amino acid catabolism; Branched-chain amino acid catabolism; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P26440](https://www.uniprot.org/uniprotkb/P26440) (Isovaleryl-CoA dehydrogenase, mitochondrial):

> A mitochondrial matrix enzyme that catalyzes the third step in leucine catabolism, where isovaleryl-CoA (3-methylbutanoyl-CoA) is metabolized to 3-methylbut-2-enoyl-CoA. To a lesser extent, it also participates in the first step in fatty acid beta-oxidation, in which it catalyzes the proR-proR stereospecific alpha,beta-dehydrogenation of other saturated short-chain acyl-CoA thioesters such as pentanoyl-CoA, hexanoyl-CoA and butanoyl-CoA, using the electron transfer flavoprotein (ETF) as their …

**Summary**, from NCBI Gene [3712](https://www.ncbi.nlm.nih.gov/gene/3712):

> Isovaleryl-CoA dehydrogenase (IVD) is a mitochondrial matrix enzyme that catalyzes the third step in leucine catabolism. The genetic deficiency of IVD results in an accumulation of isovaleric acid, which is toxic to the central nervous system and leads to isovaleric acidemia. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:6186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6186) · Entrez [3712](https://www.ncbi.nlm.nih.gov/gene/3712) · UniProt [P26440](https://www.uniprot.org/uniprotkb/P26440) · Ensembl [ENSG00000128928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128928)

## Data

Gene col 4934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4934); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4934]; `tensor/DDL_lfc|DDL_z.npy` [4934]; `embed/gene_vectors.npy` [4934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4934 or target_col == 4934). Every well: [[IVD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IVD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
