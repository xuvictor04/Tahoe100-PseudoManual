---
symbol: "SPHK1"
type: "gene"
col: 10691
ensembl_id: "ENSG00000176170"
name: "sphingosine kinase 1"
location: "17q25.1"
module: 80
arm: "+"
pooled_cpm: 11.91
n_lines_expressing: 38
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# SPHK1

*sphingosine kinase 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.52× (z +14.9, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.511× (z -4.7, q 0.001, down in 19 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCNT4]] (+0.68, fdr 1e-05), [[LPXN]] (+0.68, fdr 3e-05), [[ZNF341-AS1]] (+0.67, fdr 2e-05); moves opposite to [[NUDT21]] (-0.65, fdr 1e-05), [[TMEM245]] (-0.64, fdr 3e-05), [[STRAP]] (-0.64, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ADTRP]] → it (grade B ⚠); 13 go from it, the strongest it → [[FOXD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10691.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.52×** | +14.9 | 0e+00 | 30/33 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.28×** | +14.3 | 3e-44 | 28/35 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **5.87×** | +11.2 | 5e-27 | 30/35 (SNU-423, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.68×** | +10.8 | 7e-25 | 29/32 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.91×** | +9.5 | 2e-19 | 32/35 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.45×** | +8.6 | 6e-16 | 31/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.00×** | +7.7 | 2e-12 | 18/26 (LoVo, A498, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +6.2 | 4e-08 | 31/32 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.42×** | +6.2 | 5e-08 | 27/33 (NCI-H460, SK-MEL-2, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +5.3 | 6e-06 | 23/33 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.25×** | +5.2 | 1e-05 | 20/25 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.04×** | +5.0 | 3e-05 | 24/35 (NCI-H460, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.96×** | +4.3 | 8e-04 | 10/15 (A498, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.96×** | +4.3 | 8e-04 | 19/32 (NCI-H460, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.77×** | +4.0 | 0.003 | 18/36 (NCI-H2347, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.006 | 17/36 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.21×** | +3.2 | 0.037 | 8/32 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.065 | 17/35 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.07×** | +3.0 | 0.086 | 14/33 (HS-578T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **2.04×** | +2.9 | 0.093 | 6/33 (J82, NCI-H23, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.511×** | -4.7 | 0.001 | 19/35 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.535×** | -4.4 | 0.003 | 24/35 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -4.1 | 0.007 | 22/35 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.553×** | -3.7 | 0.032 | 15/36 (NCI-H2347, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.30 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +11.4) | — |
| [[A498 (line)]] | wt | 32.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +16.6) | — |
| [[HOP62 (line)]] | alt | 16.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 16.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 7.42 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 19.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +17.3) | — |
| [[A-172 (line)]] | wt | 28.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +12.4) | — |
| [[A549 (line)]] | wt | 7.14 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 50.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +11.7) | — |
| [[RKO (line)]] | wt | 54.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 26.3 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 7.66× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +12.3) | — |
| [[HepG2_C3A (line)]] | wt | 39.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 6.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.01× (z +10.3) | — |
| [[J82 (line)]] | alt | 16.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[LoVo (line)]] | wt | 6.66 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.99× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 3.20 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 3.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +8.9) | — |
| [[AsPC-1 (line)]] | alt | 3.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +9.5) | — |
| [[C32 (line)]] | wt | 4.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 3.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.10× (z +9.6) | — |
| [[A-427 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT4]] | +0.68 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[LPXN]] | +0.68 | +0.73 / +0.46 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | +0.67 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[MSX1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CDK6-AS1]] | +0.66 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[PPP1R12A-AS2]] | +0.62 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[ENO3]] | +0.62 | +0.66 / +0.35 | both halves | 1e-04 | pathway: HALLMARK_MYOGENESIS |
| [[NEPRO-AS1]] | +0.62 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[NEK8]] | +0.61 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[MZF1-AS1]] | +0.61 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[FJX1]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BCL10-AS1]] | +0.61 | +0.54 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | -0.65 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TMEM245]] | -0.64 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[STRAP]] | -0.64 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[SKP2]] | -0.63 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ELP1]] | -0.63 | -0.48 / -0.58 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[POT1]] | -0.62 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[GUSBP1]] | -0.61 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[CBX1]] | -0.60 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[NDRG3]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[RPA1]] | -0.59 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[PLA2G12A]] | -0.59 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ANAPC5]] | -0.58 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADTRP]] | B | ADTRP activity raises SPHK1's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.48× lower at baseline in the lines without ADTRP | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2 |
| [[ROBO4]] | B | ROBO4 activity raises SPHK1's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without ROBO4 | 0.016 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[TOP2A]] | B | TOP2A activity lowers SPHK1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises SPHK1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NKX3-1]] | B | NKX3-1 activity raises SPHK1's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 2.56× lower at baseline in the lines without NKX3-1 | 0.063 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[GCNT4]] | B | GCNT4 activity raises SPHK1's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 2.18× lower at baseline in the lines without GCNT4 | 0.066 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SOCS2]] | B | SOCS2 activity raises SPHK1's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without SOCS2 | 0.077 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[ARHGAP31]] | B | ARHGAP31 activity raises SPHK1's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without ARHGAP31 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXD1]] | B | SPHK1 activity raises FOXD1's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 3.07× lower at baseline in the lines without SPHK1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[GJC1]] | B | SPHK1 activity raises GJC1's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 2.78× lower at baseline in the lines without SPHK1 | 0.019 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[HOMER3]] | B | SPHK1 activity raises HOMER3's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.66× lower at baseline in the lines without SPHK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[ARHGAP31]] | B | SPHK1 activity raises ARHGAP31's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 3.51× lower at baseline in the lines without SPHK1 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[UPP1]] | B | SPHK1 activity raises UPP1's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 2.72× lower at baseline in the lines without SPHK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[C12orf50]] | B | SPHK1 activity raises C12orf50's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without SPHK1 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[SOX11]] | B | SPHK1 activity lowers SOX11's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.47× higher at baseline in the lines without SPHK1 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[SOCS2]] | B | SPHK1 activity raises SOCS2's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without SPHK1 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[TRAF3]] | B | SPHK1 activity raises TRAF3's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.28× lower at baseline in the lines without SPHK1 | 0.055 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[STRAP]] | B | SPHK1 activity raises STRAP's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.20× lower at baseline in the lines without SPHK1 | 0.057 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[ANGPT2]] | B | SPHK1 activity lowers ANGPT2's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.31× higher at baseline in the lines without SPHK1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[FMNL3]] | B | SPHK1 activity raises FMNL3's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without SPHK1 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.4, -2.6); signed map (21.0, -5.2). **Vector** length 90.5, 25.8% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.4 | +14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.3 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.8 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -4.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.7 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | sphingosine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,376,584-76,387,860 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPHK |
| Gene groups (HGNC) | Sphingosine kinase family |
| Hallmark sets | INFLAMMATORY_RESPONSE, MYOGENESIS, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 17 pathways, smallest: VEGFR2 mediated cell proliferation; Sphingolipid de novo biosynthesis; Association of TriC/CCT with target proteins during biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYA1](https://www.uniprot.org/uniprotkb/Q9NYA1) (Sphingosine kinase 1):

> Catalyzes the phosphorylation of sphingosine to form sphingosine 1-phosphate (SPP), a lipid mediator with both intra- and extracellular functions. Also acts on D-erythro-sphingosine and to a lesser extent sphinganine, but not other lipids, such as D,L-threo-dihydrosphingosine, N,N-dimethylsphingosine, diacylglycerol, ceramide, or phosphatidylinositol. In contrast to pro-apoptotic SPHK2, has a negative effect on intracellular ceramide levels, enhances cell growth and inhibits apoptosis. Involved …

**Summary**, from NCBI Gene [8877](https://www.ncbi.nlm.nih.gov/gene/8877):

> The protein encoded by this gene catalyzes the phosphorylation of sphingosine to form sphingosine-1-phosphate (S1P), a lipid mediator with both intra- and extracellular functions. Intracellularly, S1P regulates proliferation and survival, and extracellularly, it is a ligand for cell surface G protein-coupled receptors. This protein, and its product S1P, play a key role in TNF-alpha signaling and the NF-kappa-B activation pathway important in inflammatory, antiapoptotic, and immune processes. …

**Accessions** — [HGNC:11240](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11240) · Entrez [8877](https://www.ncbi.nlm.nih.gov/gene/8877) · UniProt [Q9NYA1](https://www.uniprot.org/uniprotkb/Q9NYA1) · Ensembl [ENSG00000176170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176170)

## Data

Gene col 10691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10691); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10691]; `tensor/DDL_lfc|DDL_z.npy` [10691]; `embed/gene_vectors.npy` [10691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10691 or target_col == 10691). Every well: [[SPHK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPHK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
