---
symbol: "PLEKHA8"
type: "gene"
col: 2721
ensembl_id: "ENSG00000106086"
name: "pleckstrin homology domain containing A8"
location: "7p14.3"
module: 134
arm: "+"
pooled_cpm: 87.84
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# PLEKHA8

*pleckstrin homology domain containing A8* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.29× (z +7.1, q 7e-10, up in 29 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.416× (z -24.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRB2]] (+0.74, fdr 7e-06), [[HDAC3]] (+0.72, fdr 7e-06), [[TPD52]] (+0.71, fdr 7e-06); moves opposite to [[LARP7]] (-0.68, fdr 7e-06), [[LINC00174]] (-0.66, fdr 1e-05), [[ZNF554]] (-0.66, fdr 9e-06).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +7.1 | 7e-10 | 29/49 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +6.4 | 5e-08 | 36/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +6.3 | 5e-08 | 35/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +5.7 | 1e-06 | 39/49 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +5.5 | 5e-06 | 36/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.20×** | +3.6 | 0.025 | 20/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.19× | +3.3 | 0.087 | 19/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.0 | 0.18 | 15/49 (A-172, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.416×** | -24.3 | 0e+00 | 47/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.482×** | -14.3 | 5e-44 | 45/48 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.472×** | -14.2 | 3e-43 | 44/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -12.4 | 4e-33 | 37/44 (SW 900, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.635×** | -8.9 | 6e-17 | 37/49 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.715×** | -6.1 | 1e-07 | 31/45 (SW 900, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.747×** | -5.7 | 9e-07 | 35/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.765×** | -5.2 | 1e-05 | 30/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -4.8 | 1e-04 | 27/47 (C32, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -4.8 | 1e-04 | 26/47 (C32, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.797×** | -4.3 | 1e-03 | 25/48 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.844× | -3.3 | 0.041 | 22/48 (CHP-212, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | 0.844× | -3.3 | 0.041 | 21/48 (C32, AsPC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.888× | -3.3 | 0.041 | 6/48 (C32, LoVo, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.735×** | -3.2 | 0.060 | 17/49 (SHP-77, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 117 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -27.8) |
| [[NCI-H460 (line)]] | wt | 98.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -32.5) |
| [[A549 (line)]] | wt | 75.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -17.3) |
| [[SW 900 (line)]] | alt | 95.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.297× (z -18.0) |
| [[A498 (line)]] | wt | 104 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.417× (z -10.3) |
| [[PANC-1 (line)]] | alt | 91.0 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.52× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -16.5) |
| [[A-172 (line)]] | wt | 111 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -24.8) |
| [[AsPC-1 (line)]] | alt | 65.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -17.3) |
| [[HS-578T (line)]] | alt | 73.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -21.3) |
| [[J82 (line)]] | alt | 72.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -20.4) |
| [[RKO (line)]] | wt | 90.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -17.3) |
| [[HepG2_C3A (line)]] | wt | 83.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.4) |
| [[HOP62 (line)]] | alt | 70.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 73.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 86.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -27.1) |
| [[NCI-H1573 (line)]] | alt | 38.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.8) |
| [[NCI-H1792 (line)]] | alt | 78.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -18.9) |
| [[NCI-H2030 (line)]] | alt | 74.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 127 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -11.0) |
| [[SW1417 (line)]] | alt | 84.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -11.7) |
| [[AN3 CA (line)]] | alt | 181 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -12.4) |
| [[COLO 205 (line)]] | alt | 63.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.2) |
| [[HT-29 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -12.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 107 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 56.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 64.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 94.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.0) |
| [[SNU-1 (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 78.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -17.2) |
| [[A-427 (line)]] | wt | 97.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -9.9) |
| [[BT-474 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 43.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -16.8) |
| [[CHP-212 (line)]] | wt | 72.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0785× (z -13.6) |
| [[H4 (line)]] | wt | 103 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 90.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 46.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -8.9) |
| [[NCI-H596 (line)]] | alt | 84.3 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.169× (z -10.1) |
| [[C-33 A (line)]] | alt | 130 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 96.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB2]] | +0.74 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[TPD52]] | +0.71 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[TENT4A]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[KIAA1958]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[BMT2]] | +0.67 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[PDXP]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[LNPK]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ALKBH5]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[WASF3]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[UBTD1]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ATRN]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | -0.68 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[LINC00174]] | -0.66 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[ZNF554]] | -0.66 | -0.65 / -0.57 | both halves | 9e-06 |  |
| [[ZNF776]] | -0.65 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[SRSF6]] | -0.65 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[CHTOP]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.63 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[FKRP]] | -0.63 | -0.72 / -0.41 | both halves | 4e-05 |  |
| [[ZNF518A]] | -0.63 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[SLC9A8]] | -0.62 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[THG1L]] | -0.62 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[TRMT13]] | -0.61 | -0.67 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PLEKHA8's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.4, -16.9); signed map (-39.6, 23.5). **Vector** length 120, 36.5% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +7.0 | +6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.6 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.8 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -13.7 | -24.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.5 | -14.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.9 | -14.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | +0.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,027,404-30,130,483 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAPP2, MGC3358 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Glycolipid transfer protein family |
| Reactome | 6 pathways, smallest: Glycosphingolipid transport; Synthesis of PIPs at the plasma membrane; PI Metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JA3](https://www.uniprot.org/uniprotkb/Q96JA3) (Pleckstrin homology domain-containing family A member 8):

> Mediates the non-vesicular transport of glucosylceramide (GlcCer) from the trans-Golgi network (TGN) to the plasma membrane, playing a pivotal role in the synthesis of complex glycosphingolipids; binding of both phosphatidylinositol 4-phosphate (PIP) and ARF1 are essential for this GlcCer transfer ability. Also functions as a cargo transport protein required for apical transport from the Golgi complex, including transport of AQP2 from the TGN to sites of AQP2 phosphorylation. Additionally …

**Summary**, from NCBI Gene [84725](https://www.ncbi.nlm.nih.gov/gene/84725):

> Enables several functions, including cerebroside transfer activity; phosphatidylinositol-4-phosphate binding activity; and small GTPase binding activity. Involved in ER to Golgi ceramide transport and globoside biosynthetic process. Located in nucleoplasm and trans-Golgi network. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30037) · Entrez [84725](https://www.ncbi.nlm.nih.gov/gene/84725) · UniProt [Q96JA3](https://www.uniprot.org/uniprotkb/Q96JA3) · Ensembl [ENSG00000106086](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106086)

## Data

Gene col 2721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2721); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2721]; `tensor/DDL_lfc|DDL_z.npy` [2721]; `embed/gene_vectors.npy` [2721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2721 or target_col == 2721). Every well: [[PLEKHA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
