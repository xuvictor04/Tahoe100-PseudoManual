---
symbol: "AMDHD2"
type: "gene"
col: 8475
ensembl_id: "ENSG00000162066"
name: "amidohydrolase domain containing 2"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# AMDHD2

*amidohydrolase domain containing 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.16× (z +12.6, q 2e-33, up in 32 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.613× (z -8.1, q 4e-13, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UAP1L1]] (+0.69, fdr 7e-06), [[PLXNA3]] (+0.66, fdr 9e-06), [[FAM50A]] (+0.62, fdr 1e-05); moves opposite to [[ANGEL2]] (-0.54, fdr 5e-05), [[ACTL6A]] (-0.54, fdr 1e-05), [[PAPOLG]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZDHHC11B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SDHAF4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +12.6 | 2e-33 | 32/40 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +10.1 | 3e-21 | 41/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.30×** | +9.6 | 2e-19 | 33/45 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +8.9 | 7e-17 | 31/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +8.0 | 1e-13 | 5/10 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +6.4 | 2e-08 | 25/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +5.4 | 5e-06 | 19/46 (KATO III, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.1 | 2e-05 | 7/17 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.4 | 7e-04 | 11/39 (NCI-H1573, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.2 | 0.002 | 5/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.007 | 16/46 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.5 | 0.020 | 10/28 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.063 | 9/43 (SNU-423, PANC-1, …) | two highest doses | position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.067 | 13/43 (NCI-H1792, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.073 | 7/41 (HOP62, HCT15, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.098 | 8/42 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8475.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.613×** | -8.1 | 4e-13 | 27/42 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.009 | 16/41 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.059 | 10/46 (NCI-H23, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.755× | -3.3 | 0.14 | 10/44 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.827× | -3.2 | 0.17 | 12/45 (NCI-H2347, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 6.84 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 11.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +11.3) | [[AZD2858 (drug)]] 0.5 µM 0.114× (z -8.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 5.21 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.0861× (z -10.0) |
| [[A-172 (line)]] | wt | 8.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +10.4) | — |
| [[A549 (line)]] | wt | 3.55 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0639× (z -9.0) |
| [[BT-474 (line)]] | alt | 4.37 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0552× (z -9.1) |
| [[C-33 A (line)]] | alt | 5.75 | 0 | 1 | — | [[Fingolimod (hydrochloride) (drug)]] 0.5 µM 0.0512× (z -9.1) |
| [[COLO 205 (line)]] | alt | 7.98 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0788× (z -8.9) |
| [[HCT15 (line)]] | alt | 9.45 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0800× (z -9.6) |
| [[Hs 766T (line)]] | wt | 8.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.13 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 4.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 4.57 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0961× (z -8.6) |
| [[RKO (line)]] | wt | 6.55 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0867× (z -9.1) |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -8.6) |
| [[A-427 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UAP1L1]] | +0.69 | +0.73 / +0.65 | both halves | 7e-06 | STRING 440 |
| [[PLXNA3]] | +0.66 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[FAM50A]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[APBB3]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CTNS]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ATP6V0D1]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PIP4P1]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MFSD12]] | +0.57 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[GET4]] | +0.56 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[DVL2]] | +0.55 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CACFD1]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL2]] | -0.54 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ACTL6A]] | -0.54 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[PAPOLG]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[BIVM]] | -0.49 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SDHAF4]] | -0.48 | -0.43 / -0.32 | both halves | 1e-04 |  |
| [[POC1B-AS1]] | -0.48 | -0.24 / -0.40 | both halves | 4e-04 |  |
| [[RMI1]] | -0.47 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[TMEM68]] | -0.46 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[LEMD3]] | -0.46 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[GSTCD]] | -0.44 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[ASH2L]] | -0.44 | -0.38 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZDHHC11B]] | B | ZDHHC11B activity raises AMDHD2's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without ZDHHC11B | 0.070 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SDHAF4]] | C | AMDHD2's natural level weakens SDHAF4's drug response | AMDHD2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.15; direction not clear | 0.092 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.474). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (12.6, -3.1); signed map (-5.2, 21.6). **Vector** length 70.7, 10.9% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +12.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | amidohydrolase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,520,357-2,531,422 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-14 |
| Reactome | 4 pathways, smallest: Synthesis of UDP-N-acetyl-glucosamine; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y303](https://www.uniprot.org/uniprotkb/Q9Y303) (N-acetylglucosamine-6-phosphate deacetylase):

> Hydrolyzes the N-glycolyl group from N-glycolylglucosamine 6-phosphate (GlcNGc-6-P) in the N-glycolylneuraminic acid (Neu5Gc) degradation pathway. Although human is not able to catalyze formation of Neu5Gc due to the inactive CMAHP enzyme, Neu5Gc is present in food and must be degraded.

**Summary**, from NCBI Gene [51005](https://www.ncbi.nlm.nih.gov/gene/51005):

> Enables N-acetylglucosamine-6-phosphate deacetylase activity. Involved in negative regulation of UDP-N-acetylglucosamine biosynthetic process. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24262) · Entrez [51005](https://www.ncbi.nlm.nih.gov/gene/51005) · UniProt [Q9Y303](https://www.uniprot.org/uniprotkb/Q9Y303) · Ensembl [ENSG00000162066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162066)

## Data

Gene col 8475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8475); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8475]; `tensor/DDL_lfc|DDL_z.npy` [8475]; `embed/gene_vectors.npy` [8475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8475 or target_col == 8475). Every well: [[AMDHD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMDHD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
