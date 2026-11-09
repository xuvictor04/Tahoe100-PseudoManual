---
symbol: "PCGF6"
type: "gene"
col: 7972
ensembl_id: "ENSG00000156374"
name: "polycomb group ring finger 6"
location: "10q24.33"
module: 36
arm: "+"
pooled_cpm: 18.67
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PCGF6

*polycomb group ring finger 6* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.72× (z +8.7, q 2e-15, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Omeprazole (drug)]] 0.05 µM: 0.785× (z -3.9, q 0.065, down in 7 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.127×, AN3 CA 0.237×, NCI-H460 0.488×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 0.181×, SHP-77 0.237×, NCI-H1792 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0851×, A-427 0.177×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.0715×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.112×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARGP1]] (+0.69, fdr 7e-06), [[NDUFAF5]] (+0.69, fdr 7e-06), [[CDK5RAP1]] (+0.67, fdr 7e-06); moves opposite to [[SDCBP]] (-0.61, fdr 7e-06), [[LINC00910]] (-0.59, fdr 1e-05), [[ATF3]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADCY3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZFYVE9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.72×** | +8.7 | 2e-15 | 34/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.58×** | +7.9 | 7e-13 | 32/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +7.6 | 4e-12 | 33/47 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +7.4 | 2e-11 | 28/46 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.3 | 2e-11 | 27/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.50×** | +6.5 | 7e-09 | 28/47 (SW480, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 3e-05 | 24/46 (CFPAC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.33×** | +4.6 | 3e-04 | 21/46 (SW480, PANC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.5 | 4e-04 | 18/41 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.32×** | +4.4 | 6e-04 | 21/47 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +4.4 | 6e-04 | 16/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.31×** | +4.4 | 6e-04 | 17/46 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.29×** | +3.9 | 0.004 | 17/45 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 17/48 (PANC-1, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.26×** | +3.7 | 0.008 | 12/46 (SW480, LS 180, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.010 | 10/47 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.046 | 5/43 (SW 900, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.059 | 9/48 (NCI-H2347, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.067 | 1/48 (hTERT-HPNE) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.078 | 14/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +2.9 | 0.083 | 5/46 (PANC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SNU-1 0.127×, AN3 CA 0.237×, NCI-H460 0.488×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 0.181×, SHP-77 0.237×, NCI-H1792 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (Panc 03.27 0.0851×, A-427 0.177×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.0715×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (HCT15 0.112×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Omeprazole (drug)]] 0.05 µM |  | **0.785×** | -3.9 | 0.065 | 7/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.4 | 0.17 | 3/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.863× | -3.3 | 0.17 | 12/48 (Hs 766T, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 30.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0715× (z -12.2) |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.112× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0851× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.62× (z +8.7) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARGP1]] | +0.69 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[NDUFAF5]] | +0.69 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[MANEAL]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[ORC5]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[NAA16]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SIMC1]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC17]] | +0.62 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[FGD1]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[LIN9]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.61 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[LINC00910]] | -0.59 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[ATF3]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[TEX14]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[HEXIM1]] | -0.55 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[SPDYA]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MED29]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TSPAN31]] | -0.53 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ARL5B]] | -0.53 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[FOSB]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[IQCN]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MAGT1]] | -0.52 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises PCGF6's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.20× lower at baseline in the lines without ADCY3 | 0.069 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[FGD1]] | B | FGD1 activity raises PCGF6's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without FGD1 | 0.081 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZFYVE9]] | C | PCGF6's natural level strengthens ZFYVE9's drug response | PCGF6's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.03; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-21.4, -2.2); signed map (-26.1, -17.9). **Vector** length 93.6, 20.4% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.4 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.2 | +8.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.4 | +7.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.4 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +6.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +0.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.2 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -1.7 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.8 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | polycomb group ring finger 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,302,796-103,351,144 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MBLR; previously RNF134 |
| Gene groups (HGNC) | Ring finger proteins; Polycomb group ring fingers |
| Reactome | 1 pathways, smallest: Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYE7](https://www.uniprot.org/uniprotkb/Q9BYE7) (Polycomb group RING finger protein 6):

> Transcriptional repressor. May modulate the levels of histone H3K4Me3 by activating KDM5D histone demethylase. Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its …

**Summary**, from NCBI Gene [84108](https://www.ncbi.nlm.nih.gov/gene/84108):

> The protein encoded by this gene contains a RING finger motif, which is most closely related to those of polycomb group (PcG) proteins RNF110/MEL-18 and BMI1. PcG proteins are known to form protein complexes and function as transcription repressors. This protein has been shown to interact with some PcG proteins and act as a transcription repressor. The activity of this protein is found to be regulated by cell cycle dependent phosphorylation. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:21156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21156) · Entrez [84108](https://www.ncbi.nlm.nih.gov/gene/84108) · UniProt [Q9BYE7](https://www.uniprot.org/uniprotkb/Q9BYE7) · Ensembl [ENSG00000156374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156374)

## Data

Gene col 7972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7972); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7972]; `tensor/DDL_lfc|DDL_z.npy` [7972]; `embed/gene_vectors.npy` [7972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7972 or target_col == 7972). Every well: [[PCGF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCGF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
