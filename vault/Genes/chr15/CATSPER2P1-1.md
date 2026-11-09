---
symbol: "CATSPER2P1-1"
type: "gene"
col: 16555
ensembl_id: "ENSG00000291053"
name: ""
location: ""
module: 15
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CATSPER2P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.65× (z +16.6, q 0e+00, up in 26 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.368× (z -9.1, q 7e-17, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPER2P1]] (+0.85, fdr 7e-06, ⚠ same locus), [[BRPF3-AS1]] (+0.68, fdr 1e-05), [[COPZ2]] (+0.67, fdr 5e-05), [[KAZALD1]] (+0.67, fdr 7e-06); moves opposite to [[H2AX]] (-0.51, fdr 2e-04), [[IPO9]] (-0.50, fdr 1e-04), [[INTS7]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RDM1P5]] → it (grade B ⚠); 3 go from it, the strongest it → [[CATSPER2P1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +16.6 | 0e+00 | 26/28 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +9.6 | 2e-19 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +7.6 | 5e-12 | 1/4 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.6 | 3e-06 | 5/11 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.0 | 7e-05 | 5/46 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.0 | 7e-05 | 8/24 (HEC-1-A, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.9 | 0.007 | 6/33 (SW1417, KATO III, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.76×** | +3.7 | 0.017 | 3/19 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.60× | +3.1 | 0.14 | 1/26 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.368×** | -9.1 | 7e-17 | 29/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.404×** | -8.2 | 6e-14 | 25/41 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.541×** | -7.9 | 6e-13 | 20/31 (J82, NCI-H23, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -7.0 | 5e-10 | 14/19 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.475×** | -6.7 | 2e-09 | 17/38 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -6.5 | 6e-09 | 19/27 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.473×** | -6.4 | 1e-08 | 23/40 (NCI-H23, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.595×** | -4.7 | 2e-04 | 14/37 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.607×** | -4.5 | 4e-04 | 12/43 (A-427, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.631×** | -4.2 | 0.002 | 12/43 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.632×** | -4.2 | 0.002 | 13/42 (HS-578T, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.643×** | -4.0 | 0.003 | 12/43 (NCI-H1573, LoVo, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.434×** | -4.0 | 0.003 | 11/26 (NCI-H1573, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -3.9 | 0.004 | 10/36 (J82, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.010 | 13/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.669×** | -3.4 | 0.020 | 9/40 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.505×** | -3.2 | 0.040 | 6/37 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 6.35 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 9.19 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0986× (z -11.3) |
| [[A498 (line)]] | wt | 1.92 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0612× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 3.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0366× (z -11.8) |
| [[J82 (line)]] | alt | 2.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0664× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 4.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0895× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0713× (z -11.7) |
| [[A-172 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.851 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.701 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPER2P1]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[BRPF3-AS1]] | +0.68 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[COPZ2]] | +0.67 | +0.40 / +0.76 | both halves | 5e-05 |  |
| [[KAZALD1]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[CDNF]] | +0.65 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[SCAMP5]] | +0.64 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[CCNO-DT]] | +0.63 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[RHCE]] | +0.63 | +0.38 / +0.74 | both halves | 6e-05 |  |
| [[PJVK]] | +0.63 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[DNAJC3-DT]] | +0.60 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[UPK2]] | +0.60 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[DDX59-AS1]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.60 | +0.44 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H2AX]] | -0.51 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[IPO9]] | -0.50 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[INTS7]] | -0.50 | -0.26 / -0.60 | both halves | 3e-04 |  |
| [[MPHOSPH6]] | -0.50 | -0.27 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDM1P5]] | B | RDM1P5 activity raises CATSPER2P1-1's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.57× lower at baseline in the lines without RDM1P5 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[CATSPER2P1]] | C | CATSPER2P1's natural level strengthens CATSPER2P1-1's drug response | CATSPER2P1's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.71; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CATSPER2P1]] | C | CATSPER2P1-1's natural level strengthens CATSPER2P1's drug response | CATSPER2P1-1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.76; direction not clear | 0.019 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[BRPF3-AS1]] | C | CATSPER2P1-1's natural level strengthens BRPF3-AS1's drug response | CATSPER2P1-1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.42; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | CATSPER2P1-1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | CATSPER2P1-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.412 over the table, 0.050 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.579). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.5, 23.6); signed map (33.7, -4.5). **Vector** length 44.7, 5.34% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +16.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +0.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.0 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -9.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -4.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -6.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -0.7 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.1 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -3.2 |

## What is on record

> [!warning] No registry record
> CATSPER2P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16555); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16555]; `tensor/DDL_lfc|DDL_z.npy` [16555]; `embed/gene_vectors.npy` [16555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16555 or target_col == 16555). Every well: [[CATSPER2P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CATSPER2P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
