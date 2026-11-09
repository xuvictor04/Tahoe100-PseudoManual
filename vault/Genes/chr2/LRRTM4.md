---
symbol: "LRRTM4"
type: "gene"
col: 10695
ensembl_id: "ENSG00000176204"
name: "leucine rich repeat transmembrane neuronal 4"
location: "2p12"
module: 27
arm: "+"
pooled_cpm: 41.62
n_lines_expressing: 17
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 12
direction_downstream: 26
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# LRRTM4

*leucine rich repeat transmembrane neuronal 4* — 2p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +16.4, q 0e+00, up in 1 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.579× (z -7.5, q 5e-11, down in 12 of 15 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LNCAROD]] (+0.63, fdr 1e-05), [[PHYHIPL]] (+0.58, fdr 2e-05), [[NIHCOLE]] (+0.53, fdr 3e-05); moves opposite to [[GDPGP1]] (-0.42, fdr 6e-05), [[MAP3K5]] (-0.39, fdr 2e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SLC30A10]] → it (grade B ⚠); 26 go from it, the strongest it → [[GRIK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +16.4 | 0e+00 | 1/15 (NCI-H1792) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +10.2 | 6e-22 | 0/16 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.81×** | +8.1 | 7e-14 | 1/15 (C32) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.2 | 1e-10 | 0/15 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.2 | 5e-08 | 0/16 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.2 | 2e-05 | 2/15 (NCI-H1792, HepG2/C3A) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.7 | 2e-04 | 6/15 (C32, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.6 | 3e-04 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +4.4 | 6e-04 | 0/16 | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.004 | 8/15 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.007 | 1/15 (NCI-H661) | rises with dose | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.8 | 0.007 | 4/15 (SW480, LS 180, …) | top dose only | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.007 | 9/16 (A-172, SHP-77, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 5/16 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.011 | 8/15 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.012 | 4/15 (C32, SW480, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.020 | 0/15 | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.075 | 3/15 (C32, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10695.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.579×** | -7.5 | 5e-11 | 12/15 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.598×** | -7.0 | 6e-10 | 14/15 (H4, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.624×** | -6.2 | 1e-07 | 14/15 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.670×** | -5.5 | 6e-06 | 10/15 (A-172, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.681×** | -5.2 | 3e-05 | 10/15 (H4, A-172, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.686×** | -5.1 | 3e-05 | 13/15 (HepG2/C3A, H4, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -5.0 | 6e-05 | 12/15 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.532×** | -4.5 | 5e-04 | 11/15 (LS 180, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -4.0 | 0.005 | 6/15 (A-427, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.755×** | -3.8 | 0.007 | 14/15 (H4, HepG2/C3A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.757×** | -3.8 | 0.007 | 10/15 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.922× | -3.8 | 0.007 | 1/16 (SK-MEL-2) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.754×** | -3.7 | 0.010 | 3/15 (A-172, C32, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.045 | 10/15 (KATO III, H4, …) | rises with dose | plate-row cell shift |
| [[Brivudine (drug)]] 5 µM |  | **0.645×** | -3.1 | 0.067 | 8/16 (A-427, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.855× | -3.0 | 0.092 | 4/16 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -3.0 | 0.093 | 1/15 (LS 180) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 521 | 0 | 22 (15 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0196× (z -28.8) |
| [[KATO III (line)]] | alt | 176 | 0 | 17 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.00412× (z -40.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0252× (z -28.5) |
| [[H4 (line)]] | wt | 96.3 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0921× (z -19.6) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.0815× (z -14.4) |
| [[A-172 (line)]] | wt | 103 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0414× (z -27.3) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0623× (z -16.8) |
| [[A-427 (line)]] | wt | 689 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.3) |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0464× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0892× (z -13.1) |
| [[SW480 (line)]] | alt | 38.9 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0565× (z -18.5) |
| [[C32 (line)]] | wt | 79.5 | 4 | 0 | [[Cobimetinib (drug)]] 0.5 µM 9.23× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 51.8 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0153× (z -22.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0583× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0736× (z -15.4) |
| [[NCI-H1792 (line)]] | alt | 27.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0552× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.153× (z -8.9) |
| [[SHP-77 (line)]] | alt | 105 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0913× (z -16.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.191× (z -11.5) |
| [[A498 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.19 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.95 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNCAROD]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[PHYHIPL]] | +0.58 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[NIHCOLE]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[GABRA3]] | +0.53 | +0.51 / +0.60 | both halves | 1e-05 | pathway: Neuronal System |
| [[HS3ST5]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PEG3]] | +0.53 | +0.41 / +0.43 | both halves | 4e-05 | **novel candidate** |
| [[MIR3667HG]] | +0.53 | +0.39 / +0.62 | both halves | 5e-05 |  |
| [[JAKMIP2]] | +0.49 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[MKX]] | +0.48 | +0.35 / +0.41 | both halves | 1e-04 |  |
| [[C1QTNF7-AS1]] | +0.48 | +0.25 / +0.57 | both halves | 4e-04 |  |
| [[RMST]] | +0.48 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[APOB]] | +0.47 | +0.38 / +0.25 | both halves | 4e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDPGP1]] | -0.42 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[MAP3K5]] | -0.39 | -0.30 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC30A10]] | B | SLC30A10 activity raises LRRTM4's level | lines that do not express SLC30A10 (22) vs lines expressing it (28) | 2.55× lower at baseline in the lines without SLC30A10 | 0.054 | ⚠ within organs, on part of the lines; also absent: PKHD1, LINC00698, LINC02147; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers LRRTM4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[GABRA3]] | C | GABRA3 activity raises LRRTM4's level | lines that do not express GABRA3 (26) vs lines expressing it (24) | 4.24× lower at baseline in the lines without GABRA3 | 0.001 | ⚠ within organs, on part of the lines; also absent: MAGEA3-DT, MKRN3, LRRTM4; co-absent with the target |
| [[MKRN3]] | C | MKRN3 activity raises LRRTM4's level | lines that do not express MKRN3 (23) vs lines expressing it (27) | 4.79× lower at baseline in the lines without MKRN3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GABRA3, LRRTM4, MAGEA3-DT; co-absent with the target |
| [[MAGEA3-DT]] | C | MAGEA3-DT activity raises LRRTM4's level | lines that do not express MAGEA3-DT (29) vs lines expressing it (21) | 4.43× lower at baseline in the lines without MAGEA3-DT | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRA3, LINC00648, LINC00470; co-absent with the target |
| [[FAM95A]] | C | FAM95A activity raises LRRTM4's level | lines that do not express FAM95A (38) vs lines expressing it (12) | 5.12× lower at baseline in the lines without FAM95A | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises LRRTM4's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 3.36× lower at baseline in the lines without AXIN2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity raises LRRTM4's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 3.77× lower at baseline in the lines without GABRG2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[LINC02058]] | C | LINC02058 activity raises LRRTM4's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 2.17× lower at baseline in the lines without LINC02058 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent; co-absent with the target |
| [[JAKMIP2]] | C | JAKMIP2 activity raises LRRTM4's level | lines that do not express JAKMIP2 (29) vs lines expressing it (21) | 2.45× lower at baseline in the lines without JAKMIP2 | 0.051 | ⚠ within organs, on part of the lines; also absent: MARCHF1, KCNH5, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises LRRTM4's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.67× lower at baseline in the lines without LGR5 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises LRRTM4's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.06× lower at baseline in the lines without CSMD3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 8, C 18. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIK2]] | B | LRRTM4 activity raises GRIK2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 3.15× lower at baseline in the lines without LRRTM4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[NPAS3]] | B | LRRTM4 activity strengthens NPAS3's drug response | lines that do not express LRRTM4 (22) vs lines expressing it (11) | the lines without LRRTM4 respond 1.48× as strongly (z diff -0.85); strongest at Panobinostat 0.5 µM: 0.62x vs 0.32x (z diff +3.6) | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; target measured in part of the lines; both ways; artifact flags |
| [[SORBS2]] | B | LRRTM4 activity raises SORBS2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.69× lower at baseline in the lines without LRRTM4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[PCDH9]] | B | LRRTM4 activity raises PCDH9's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without LRRTM4 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[GRM7]] | B | LRRTM4 activity raises GRM7's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.14× lower at baseline in the lines without LRRTM4 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[PSD2]] | B | LRRTM4 activity raises PSD2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without LRRTM4 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[TNFRSF19]] | B | LRRTM4 activity raises TNFRSF19's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.53× lower at baseline in the lines without LRRTM4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[PDK4-AS1]] | B | LRRTM4 activity raises PDK4-AS1's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 1.33× lower at baseline in the lines without LRRTM4 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973 |
| [[MKRN3]] | C | LRRTM4 activity raises MKRN3's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 6.77× lower at baseline in the lines without LRRTM4 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; co-absent with the target |
| [[GABRG2]] | C | LRRTM4 activity raises GABRG2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.89× lower at baseline in the lines without LRRTM4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; co-absent with the target |
| [[AXIN2]] | C | LRRTM4 activity raises AXIN2's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.88× lower at baseline in the lines without LRRTM4 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; co-absent with the target |
| [[CSMD3]] | C | LRRTM4 activity raises CSMD3's level | lines that do not express LRRTM4 (33) vs lines expressing it (17) | 2.44× lower at baseline in the lines without LRRTM4 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000227088, ENSG00000249174, ENSG00000248973; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.6, 42.8); signed map (64.8, 19.4). **Vector** length 69.4, 21.4% of its response variance represented; |z| ≥ 3 in 601 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.3 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +4.5 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.5 | -7.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat transmembrane neuronal 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p12 — chr2:76,747,685-77,593,319 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12568 |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VH4](https://www.uniprot.org/uniprotkb/Q86VH4) (Leucine-rich repeat transmembrane neuronal protein 4):

> May play a role in the development and maintenance of the vertebrate nervous system. Exhibits strong synaptogenic activity, restricted to excitatory presynaptic differentiation (By similarity).

**Summary**, from NCBI Gene [80059](https://www.ncbi.nlm.nih.gov/gene/80059):

> Predicted to enable heparan sulfate proteoglycan binding activity and signaling receptor activity. Predicted to be involved in positive regulation of synapse assembly. Predicted to act upstream of or within AMPA glutamate receptor clustering and regulation of presynaptic membrane organization. Predicted to be located in postsynaptic membrane. Predicted to be part of AMPA glutamate receptor complex. Predicted to be active in several cellular components, including GABA-ergic synapse; …

**Accessions** — [HGNC:19411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19411) · Entrez [80059](https://www.ncbi.nlm.nih.gov/gene/80059) · UniProt [Q86VH4](https://www.uniprot.org/uniprotkb/Q86VH4) · Ensembl [ENSG00000176204](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176204)

## Data

Gene col 10695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10695); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10695]; `tensor/DDL_lfc|DDL_z.npy` [10695]; `embed/gene_vectors.npy` [10695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10695 or target_col == 10695). Every well: [[LRRTM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRTM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
