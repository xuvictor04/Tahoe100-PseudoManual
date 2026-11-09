---
symbol: "ZNF816-ZNF321P"
type: "gene"
col: 13311
ensembl_id: "ENSG00000221874"
name: "ZNF816-ZNF321P readthrough"
location: "19q13.41"
module: 25
arm: "-"
pooled_cpm: 16.71
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ZNF816-ZNF321P

*ZNF816-ZNF321P readthrough* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.88× (z +8.4, q 2e-14, up in 29 of 35 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +4.3, q 0.003, up in 18 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 13.7×, H4 6.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.487× (z -9.9, q 2e-20, down in 33 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAT1]] (+0.68, fdr 3e-05), [[DTX2P1-UPK3BP1-PMS2P11]] (+0.63, fdr 1e-05), [[EIF3CL]] (+0.60, fdr 1e-05); moves opposite to [[DYNC1H1]] (-0.61, fdr 2e-05), [[SCRN1]] (-0.58, fdr 2e-05), [[AP2M1]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF600]] → it (grade C ⚠); 4 go from it, the strongest it → [[DYNC1H1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13311.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C32 13.7×, H4 6.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +8.4 | 2e-14 | 29/35 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.6 | 6e-06 | 1/42 (COLO 205) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.003 | 18/40 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.007 | 14/41 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.40× | +3.3 | 0.10 | 10/37 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.18× | +3.3 | 0.10 | 14/42 (PANC-1, HOP62, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.26× | +3.2 | 0.11 | 12/41 (SW 900, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.487×** | -9.9 | 2e-20 | 33/42 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.482×** | -9.7 | 9e-20 | 30/40 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -6.6 | 8e-09 | 25/41 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.738×** | -5.9 | 4e-07 | 21/40 (A-172, RKO, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -5.9 | 4e-07 | 20/35 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -5.8 | 5e-07 | 19/28 (KATO III, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -5.2 | 2e-05 | 24/41 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -4.9 | 7e-05 | 20/40 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.526×** | -4.6 | 2e-04 | 19/42 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.771×** | -3.6 | 0.019 | 18/40 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.765×** | -3.6 | 0.019 | 15/40 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Gefitinib (drug)]] 5 µM |  | **0.774×** | -3.5 | 0.020 | 12/42 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.787×** | -3.3 | 0.040 | 18/35 (PANC-1, NCI-H2347, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.788×** | -3.3 | 0.040 | 11/42 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.789×** | -3.3 | 0.041 | 18/40 (NCI-H1792, SW480, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.642×** | -3.2 | 0.048 | 11/37 (CFPAC-1, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 38.0 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.222× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 15.8 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -11.4) ⚠ toxic |
| [[A-427 (line)]] | wt | 18.7 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0970× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -11.8) |
| [[A-172 (line)]] | wt | 24.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -12.4) ⚠ cell-cycle shift, explains ~45% of this change |
| [[H4 (line)]] | wt | 34.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Harringtonine (drug)]] 5 µM 0.187× (z -9.1) |
| [[KATO III (line)]] | alt | 41.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.1000× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 8.60 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0790× (z -8.6) |
| [[C32 (line)]] | wt | 9.05 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.7× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[COLO 205 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 5.23 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.107× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0834× (z -10.3) ⚠ toxic |
| [[A498 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAT1]] | +0.68 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[EIF3CL]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PHLDB3]] | +0.58 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CCZ1P1]] | +0.58 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[ZNF500]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[IL17RA]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[FBXL12]] | +0.56 | +0.37 / +0.62 | both halves | 9e-05 |  |
| [[CCDC12]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[MFSD14CP]] | +0.55 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[NCBP2AS2]] | +0.54 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[C19orf25]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1H1]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[SCRN1]] | -0.58 | -0.46 / -0.60 | both halves | 2e-05 |  |
| [[AP2M1]] | -0.58 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[HUWE1]] | -0.57 | -0.35 / -0.62 | both halves | 1e-04 |  |
| [[WWC3]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ZNF664]] | -0.56 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[TWF1]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FLII]] | -0.55 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[HNRNPK]] | -0.55 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[SLC35F6]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[BBS10]] | -0.53 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[DST]] | -0.53 | -0.33 / -0.61 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF600]] | C | ZNF600 activity raises ZNF816-ZNF321P's level | lines that do not express ZNF600 (9) vs lines expressing it (41) | 2.94× lower at baseline in the lines without ZNF600 | 0.002 | ⚠ within organs, on part of the lines; also absent: ZNF320, ZNF28, ZNF468; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC1H1]] | B | ZNF816-ZNF321P activity lowers DYNC1H1's level | lines that do not express ZNF816-ZNF321P (6) vs lines expressing it (44) | 1.37× higher at baseline in the lines without ZNF816-ZNF321P | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[AXIN1]] | B | ZNF816-ZNF321P activity lowers AXIN1's level | lines that do not express ZNF816-ZNF321P (6) vs lines expressing it (44) | 1.38× higher at baseline in the lines without ZNF816-ZNF321P | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[FBXL12]] | B | ZNF816-ZNF321P activity raises FBXL12's level | lines that do not express ZNF816-ZNF321P (6) vs lines expressing it (44) | 1.26× lower at baseline in the lines without ZNF816-ZNF321P | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |
| [[ZNF600]] | C | ZNF816-ZNF321P activity raises ZNF600's level | lines that do not express ZNF816-ZNF321P (6) vs lines expressing it (44) | 4.02× lower at baseline in the lines without ZNF816-ZNF321P | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701; co-absent with the target |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.8, -19.7); signed map (-39.0, 5.5). **Vector** length 77.1, 15.1% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.2 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.0 | +1.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -9.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.4 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ZNF816-ZNF321P readthrough |
| Locus type | readthrough (other) |
| Location | 19q13.41 — chr19:52,928,475-52,962,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ZNF816-ZNF321 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100529240](https://www.ncbi.nlm.nih.gov/gene/100529240):

> This locus represents naturally occurring read-through transcription between the zinc finger protein 816 (ZNF816) gene and the zinc finger protein 321 (ZNF321) pseudogene on chromosome 19. The read-through transcript encodes a KRAB domain-containing protein that shares sequence identity with the upstream gene product, but it contains a distinct C-terminus encoded by exon structure from the downstream pseudogene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:38879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38879) · Entrez [100529240](https://www.ncbi.nlm.nih.gov/gene/100529240) · Ensembl [ENSG00000221874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221874)

## Data

Gene col 13311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13311); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13311]; `tensor/DDL_lfc|DDL_z.npy` [13311]; `embed/gene_vectors.npy` [13311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13311 or target_col == 13311). Every well: [[ZNF816-ZNF321P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF816-ZNF321P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
