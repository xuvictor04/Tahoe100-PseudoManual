---
symbol: "PRIMPOL"
type: "gene"
col: 8924
ensembl_id: "ENSG00000164306"
name: "primase and DNA directed polymerase"
location: "4q35.1"
module: 6
arm: "+"
pooled_cpm: 18.76
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 30
n_dd_up_clean: 7
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PRIMPOL

*primase and DNA directed polymerase* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +6.8, q 4e-09, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.412× (z -13.9, q 4e-41, down in 35 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.531× (z -9.9, q 7e-21, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMI1]] (+0.74, fdr 7e-06), [[BRCA1]] (+0.72, fdr 7e-06), [[KNTC1]] (+0.68, fdr 7e-06); moves opposite to [[MFSD12]] (-0.56, fdr 3e-05), [[ABAT]] (-0.55, fdr 6e-05), [[PEDS1]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC171]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.8 | 4e-09 | 27/46 (Panc 03.27, BT-474, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +6.1 | 4e-07 | 24/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +5.4 | 1e-05 | 19/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 0.003 | 12/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +4.1 | 0.004 | 13/47 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.004 | 13/47 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.25×** | +3.6 | 0.030 | 13/47 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.068 | 6/48 (HS-578T, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.068 | 9/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.22× | +3.1 | 0.11 | 3/48 (SW 1088, KATO III, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.22× | +3.0 | 0.14 | 14/48 (SW480, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -13.9 | 4e-41 | 35/46 (LS 180, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.605×** | -11.1 | 3e-26 | 32/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -9.9 | 7e-21 | 33/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -9.6 | 7e-20 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.587×** | -8.3 | 8e-15 | 30/46 (SHP-77, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -8.2 | 2e-14 | 31/48 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -7.4 | 9e-12 | 24/45 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.606×** | -7.4 | 9e-12 | 30/48 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.640×** | -7.0 | 2e-10 | 25/46 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.656×** | -6.6 | 2e-09 | 27/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.658×** | -6.6 | 3e-09 | 28/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.658×** | -6.5 | 3e-09 | 29/48 (RKO, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.689×** | -5.8 | 3e-07 | 23/48 (AN3 CA, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.684×** | -5.7 | 4e-07 | 25/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.520×** | -5.3 | 3e-06 | 19/37 (LS 180, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.719×** | -5.1 | 9e-06 | 20/48 (SW480, C-33 A, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -5.1 | 1e-05 | 21/45 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -4.9 | 2e-05 | 21/48 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.738×** | -4.8 | 6e-05 | 21/48 (J82, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.564×** | -4.7 | 8e-05 | 20/48 (PANC-1, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.757×** | -4.4 | 4e-04 | 14/46 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.295× (z -12.1) |
| [[SW480 (line)]] | alt | 23.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.278× (z -12.1) |
| [[J82 (line)]] | alt | 23.5 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.192× (z -11.9) |
| [[LS 180 (line)]] | wt | 15.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0384× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 28.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -13.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 31.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 17.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -10.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0482× (z -10.0) |
| [[H4 (line)]] | wt | 22.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -13.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0309× (z -19.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 16.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -8.5) |
| [[LoVo (line)]] | wt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -13.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.118× (z -12.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0681× (z -9.9) |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -10.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMI1]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 | STRING 542 |
| [[BRCA1]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 | STRING 483 |
| [[KNTC1]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[DYRK4]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GSTCD]] | +0.66 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[CENPH]] | +0.65 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[VRK1]] | +0.65 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[C1orf112]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[FANCD2]] | +0.64 | +0.60 / +0.71 | both halves | 7e-06 | STRING 469 |
| [[UBL7-DT]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[XNDC1N]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RAD51AP1]] | +0.63 | +0.53 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD12]] | -0.56 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ABAT]] | -0.55 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[PEDS1]] | -0.52 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[DLGAP4]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CLIP2]] | -0.52 | -0.49 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC171]] | C | CCDC171 activity raises PRIMPOL's level | lines that do not express CCDC171 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without CCDC171 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.6, -46.1); signed map (-41.1, -48.0). **Vector** length 75.9, 15.1% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *EML4 and NUDC in mitotic spindle formation* (reactome, mean cos +0.50 to 13); *Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal* (reactome, mean cos +0.52 to 12); *Amplification of signal from the kinetochores* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +4.3 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.4 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | -3.3 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | primase and DNA directed polymerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:184,649,667-184,694,963 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33167; previously CCDC111 |
| Gene groups (HGNC) | DNA polymerases; DNA primases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LW4](https://www.uniprot.org/uniprotkb/Q96LW4) (DNA-directed primase/polymerase protein):

> DNA primase and DNA polymerase required to tolerate replication-stalling lesions by bypassing them. Required to facilitate mitochondrial and nuclear replication fork progression by initiating de novo DNA synthesis using dNTPs and acting as an error-prone DNA polymerase able to bypass certain DNA lesions. Shows a high capacity to tolerate DNA damage lesions such as 8oxoG and abasic sites in DNA. Provides different translesion synthesis alternatives when DNA replication is stalled: able to …

**Summary**, from NCBI Gene [201973](https://www.ncbi.nlm.nih.gov/gene/201973):

> This gene encodes a DNA primase-polymerase that belongs to a superfamily of archaeao-eukaryotic primases. Members of this family have primase activity, catalyzing the synthesis of short RNA primers that serve as starting points for DNA synthesis, as well as DNA polymerase activity. The encoded protein facilitates DNA damage tolerance by mediating uninterrupted fork progression after UV irradiation and reinitiating DNA synthesis. An allelic variant in this gene is associated with myopia 22. …

**Accessions** — [HGNC:26575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26575) · Entrez [201973](https://www.ncbi.nlm.nih.gov/gene/201973) · UniProt [Q96LW4](https://www.uniprot.org/uniprotkb/Q96LW4) · Ensembl [ENSG00000164306](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164306)

## Data

Gene col 8924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8924); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8924]; `tensor/DDL_lfc|DDL_z.npy` [8924]; `embed/gene_vectors.npy` [8924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8924 or target_col == 8924). Every well: [[PRIMPOL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRIMPOL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
