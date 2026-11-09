---
symbol: "RAD51D"
type: "gene"
col: 11670
ensembl_id: "ENSG00000185379"
name: "RAD51 paralog D"
location: "17q12"
module: 4
arm: "+"
pooled_cpm: 16.3
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RAD51D

*RAD51 paralog D* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +7.4, q 9e-11, up in 13 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.41× (z +4.7, q 3e-04, up in 17 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.462× (z -15.5, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCERG1]] (+0.76, fdr 7e-06), [[POGK]] (+0.72, fdr 7e-06), [[NAA15]] (+0.71, fdr 7e-06); moves opposite to [[ZNHIT1]] (-0.68, fdr 1e-05), [[AAMDC]] (-0.66, fdr 1e-05), [[NARF]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); 2 go from it, the strongest it → [[P4HA1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.4 | 9e-11 | 13/22 (NCI-H1792, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.5 | 9e-06 | 15/37 (NCI-H1792, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +5.5 | 9e-06 | 18/46 (PANC-1, SW480, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.0 | 6e-05 | 20/46 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.41×** | +4.7 | 3e-04 | 17/45 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.067 | 11/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.067 | 12/46 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.067 | 14/46 (NCI-H460, A549, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.067 | 9/46 (HS-578T, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11670.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.462×** | -15.5 | 0e+00 | 39/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.401×** | -13.0 | 5e-36 | 41/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.413×** | -12.5 | 8e-34 | 36/45 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -11.4 | 4e-28 | 35/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.514×** | -9.4 | 4e-19 | 34/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.580×** | -7.7 | 1e-12 | 24/46 (SW480, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.629×** | -6.6 | 4e-09 | 23/46 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -6.5 | 4e-09 | 26/45 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -5.4 | 5e-06 | 27/46 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.768×** | -5.3 | 7e-06 | 24/45 (MIA PaCa-2, A498, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.710×** | -4.8 | 7e-05 | 21/46 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.659×** | -4.4 | 5e-04 | 17/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.565×** | -4.2 | 0.001 | 15/42 (SW48, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.742×** | -4.1 | 0.002 | 16/44 (SW1417, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.580×** | -4.0 | 0.002 | 11/46 (A-427, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -4.0 | 0.003 | 19/46 (RKO, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -3.8 | 0.005 | 17/47 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.3 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0867× (z -22.4) |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -17.9) |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -17.4) |
| [[RKO (line)]] | wt | 21.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0487× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -12.5) |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.5) |
| [[J82 (line)]] | alt | 20.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.235× (z -11.0) |
| [[A-427 (line)]] | wt | 30.7 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -13.5) |
| [[A498 (line)]] | wt | 20.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.6) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -13.3) |
| [[LoVo (line)]] | wt | 17.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 5.90 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0865× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -9.2) |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0865× (z -12.3) |
| [[C32 (line)]] | wt | 8.35 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0774× (z -9.8) |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0767× (z -9.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -9.5) |
| [[Hs 766T (line)]] | wt | 6.67 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -10.1) |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.123× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 8.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.122× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -8.9) ⚠ cell-cycle shift, explains ~98% of this change |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -9.2) |
| [[SNU-423 (line)]] | alt | 12.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0880× (z -11.6) |
| [[SW48 (line)]] | wt | 21.1 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -9.1) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCERG1]] | +0.76 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[POGK]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[NAA15]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[FKTN]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[NAA25]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[COA7]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.67 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[MRPL3]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[MAK16]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT1]] | -0.68 | -0.70 / -0.56 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.66 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[NARF]] | -0.66 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[NDUFA2]] | -0.62 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[WBP1]] | -0.61 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[OST4]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[SAP30-DT]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TESK2]] | -0.59 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[P4HA1]] | -0.59 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[YPEL5]] | -0.59 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.58 | -0.39 / -0.56 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises RAD51D's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without TERT | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[TOP2A]] | B | TOP2A activity raises RAD51D's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAXC]] | B | FAXC activity raises RAD51D's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.47× lower at baseline in the lines without FAXC | 0.037 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[MVB12B]] | B | MVB12B activity raises RAD51D's level | lines that do not express MVB12B (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without MVB12B | 0.037 | ⚠ within organs, on part of the lines; co-occurs with SMAD4; also absent: PDE5A, TSEN2, TYMSOS; maybe low, not absent |
| [[FAXC]] | B | FAXC activity strengthens RAD51D's drug response | lines that do not express FAXC (11) vs lines expressing it (36) | the lines without FAXC respond 0.78× as strongly (z diff +1.16); strongest at Digitoxin 5 µM: 0.43x vs 0.33x (z diff +2.4) | 0.055 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P4HA1]] | C | RAD51D's natural level weakens P4HA1's drug response | RAD51D's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.40; direction not clear | 0.012 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TADA2A]] | C | RAD51D's natural level strengthens TADA2A's drug response | RAD51D's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.29; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.0, -38.5); signed map (-0.3, -41.3). **Vector** length 90.4, 20.0% of its response variance represented; |z| ≥ 3 in 964 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.5 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +1.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.5 | -15.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -13.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -12.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -4.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RAD51 paralog D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,092,221-35,121,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | R51H3, Trad, HsTRAD; previously RAD51L3 |
| Gene groups (HGNC) | RAD51 paralogs |
| Reactome | 20 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [O75771](https://www.uniprot.org/uniprotkb/O75771) (DNA repair protein RAD51 homolog 4):

> Involved in the homologous recombination repair (HRR) pathway of double-stranded DNA breaks arising during DNA replication or induced by DNA-damaging agents. Bind to single-stranded DNA (ssDNA) and has DNA-dependent ATPase activity. Part of the RAD51 paralog protein complex BCDX2 which acts in the BRCA1-BRCA2-dependent HR pathway. Upon DNA damage, BCDX2 acts downstream of BRCA2 recruitment and upstream of RAD51 recruitment. BCDX2 binds predominantly to the intersection of the four duplex arms …

**Summary**, from NCBI Gene [5892](https://www.ncbi.nlm.nih.gov/gene/5892):

> The protein encoded by this gene is a member of the RAD51 protein family. RAD51 family members are highly similar to bacterial RecA and Saccharomyces cerevisiae Rad51, which are known to be involved in the homologous recombination and repair of DNA. This protein forms a complex with several other members of the RAD51 family, including RAD51L1, RAD51L2, and XRCC2. The protein complex formed with this protein has been shown to catalyze homologous pairing between single- and double-stranded DNA, …

**Accessions** — [HGNC:9823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9823) · Entrez [5892](https://www.ncbi.nlm.nih.gov/gene/5892) · UniProt [O75771](https://www.uniprot.org/uniprotkb/O75771) · Ensembl [ENSG00000185379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185379)

## Data

Gene col 11670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11670); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11670]; `tensor/DDL_lfc|DDL_z.npy` [11670]; `embed/gene_vectors.npy` [11670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11670 or target_col == 11670). Every well: [[RAD51D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD51D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
