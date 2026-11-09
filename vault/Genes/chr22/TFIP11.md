---
symbol: "TFIP11"
type: "gene"
col: 1871
ensembl_id: "ENSG00000100109"
name: "tuftelin interacting protein 11"
location: "22q12.1"
module: 107
arm: "+"
pooled_cpm: 24.12
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# TFIP11

*tuftelin interacting protein 11* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 6.91× (z +17.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.423× (z -15.1, q 0e+00, down in 36 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.784× (z -6.1, q 3e-07, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF622]] (+0.69, fdr 7e-06), [[SCNM1]] (+0.69, fdr 7e-06), [[ESS2]] (+0.68, fdr 7e-06); moves opposite to [[IGF2BP3]] (-0.56, fdr 3e-05), [[REEP3]] (-0.53, fdr 3e-05), [[GLS]] (-0.51, fdr 3e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[POLR2C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.91×** | +17.7 | 0e+00 | 46/48 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.01×** | +10.1 | 1e-21 | 32/46 (SW480, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +8.0 | 2e-13 | 35/48 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.8 | 8e-13 | 29/46 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +7.5 | 5e-12 | 27/48 (SK-MEL-2, RKO, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +6.3 | 2e-08 | 29/48 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +5.0 | 4e-05 | 21/47 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +4.8 | 1e-04 | 20/48 (SK-MEL-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.7 | 2e-04 | 15/48 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 8e-04 | 18/48 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.3 | 8e-04 | 18/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.18× | +4.1 | 0.002 | 15/48 (C32, SW480, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.038 | 11/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.064 | 8/47 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.0 | 0.089 | 9/48 (Hs 766T, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1871.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.423×** | -15.1 | 0e+00 | 36/41 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.491×** | -12.0 | 9e-31 | 27/35 (Panc 03.27, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -6.1 | 3e-07 | 30/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.748×** | -4.7 | 3e-04 | 18/37 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.779×** | -4.4 | 0.001 | 22/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.810×** | -3.7 | 0.020 | 12/48 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.830×** | -3.3 | 0.088 | 5/48 (BT-474, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 67.2 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -22.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 31.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.15× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -16.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 41.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.11× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 23.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 28.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 14.7× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -8.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 20.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.5× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 15.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.31× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -16.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.00× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -8.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -9.4) |
| [[A498 (line)]] | wt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -10.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -15.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -9.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 21.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 21.8× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.109× (z -14.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 14.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.7× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0526× (z -23.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 15.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.5× (z +8.9) | — |
| [[RKO (line)]] | wt | 24.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.6× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -9.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.06× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF622]] | +0.69 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[SCNM1]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ESS2]] | +0.68 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[SDE2]] | +0.67 | +0.58 / +0.61 | both halves | 8e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 620 |
| [[VIRMA]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[MRPL10]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[TMEM11]] | +0.65 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZNF576]] | +0.65 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[ZNF581]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ZNF350]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[EIF4E2]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[GCC1]] | +0.64 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGF2BP3]] | -0.56 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[REEP3]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[GLS]] | -0.51 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[ATP1B3]] | -0.51 | -0.58 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TFIP11's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLR2C]] | C | TFIP11's natural level weakens POLR2C's drug response | TFIP11's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.08; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.0, -7.1); signed map (-12.1, -10.0). **Vector** length 81.1, 16.0% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +17.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +4.3 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.0 | -4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | tuftelin interacting protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:26,491,225-26,512,505 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIP39, DKFZP434B194, Spp382 |
| Gene groups (HGNC) | G-patch domain containing; Spliceosomal B complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBB9](https://www.uniprot.org/uniprotkb/Q9UBB9) (Tuftelin-interacting protein 11):

> Involved in pre-mRNA splicing, specifically in spliceosome disassembly during late-stage splicing events. Intron turnover seems to proceed through reactions in two lariat-intron associated complexes termed Intron Large (IL) and Intron Small (IS). In cooperation with DHX15 seems to mediate the transition of the U2, U5 and U6 snRNP-containing IL complex to the snRNP-free IS complex leading to efficient debranching and turnover of excised introns. May play a role in the differentiation of …

**Summary**, from NCBI Gene [24144](https://www.ncbi.nlm.nih.gov/gene/24144):

> This gene encodes a protein component of the spliceosome that promotes the release of the lariat-intron during late-stage splicing through the recruitment of a pre-mRNA splicing factor called DEAH-box helicase 15. The encoded protein contains a G-patch domain, a hallmark of RNA-processing proteins, that binds DEAH-box helicase 15. This protein contains an atypical nuclear localization sequence as well as a nuclear speckle-targeting sequence, enabling it to localize to distinct speckled regions …

**Accessions** — [HGNC:17165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17165) · Entrez [24144](https://www.ncbi.nlm.nih.gov/gene/24144) · UniProt [Q9UBB9](https://www.uniprot.org/uniprotkb/Q9UBB9) · Ensembl [ENSG00000100109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100109)

## Data

Gene col 1871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1871); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1871]; `tensor/DDL_lfc|DDL_z.npy` [1871]; `embed/gene_vectors.npy` [1871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1871 or target_col == 1871). Every well: [[TFIP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFIP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
