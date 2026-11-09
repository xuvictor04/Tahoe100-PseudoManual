---
symbol: "TEAD2"
type: "gene"
col: 1073
ensembl_id: "ENSG00000074219"
name: "TEA domain transcription factor 2"
location: "19q13.33"
module: 163
arm: "+"
pooled_cpm: 6.57
n_lines_expressing: 41
n_dd_up: 3
n_dd_down: 16
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# TEAD2

*TEA domain transcription factor 2* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +9.4, q 2e-18, up in 17 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxycycline (monohydrate) (drug)]] 5 µM: 1.36× (z +3.6, q 0.068, up in 2 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.346× (z -18.2, q 0e+00, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC6A16]] (+0.68, fdr 1e-05, ⚠ same locus), [[AMFR]] (+0.57, fdr 2e-05), [[SENP3]] (+0.56, fdr 2e-05), [[GATA2-AS1]] (+0.55, fdr 3e-05); moves opposite to [[SCFD1]] (-0.52, fdr 1e-04), [[BCL10]] (-0.50, fdr 2e-04), [[PTER]] (-0.50, fdr 3e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SIRPA]] → it (grade B ⚠); 8 go from it, the strongest it → [[CTSZ]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.19×** | +9.4 | 2e-18 | 17/26 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.5 | 1e-05 | 9/16 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.068 | 2/37 (NCI-H2030, Hs 766T) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.34× | +3.2 | 0.14 | 4/34 (hTERT-HPNE, AN3 CA, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.22× | +3.2 | 0.14 | 4/38 (A498, Hs 766T, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.31× | +3.2 | 0.14 | 11/36 (NCI-H2030, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.31× | +3.1 | 0.14 | 7/37 (SK-MEL-2, PANC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.346×** | -18.2 | 0e+00 | 35/36 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.236×** | -17.4 | 0e+00 | 32/33 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.406×** | -10.5 | 2e-23 | 26/37 (AN3 CA, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.465×** | -9.3 | 3e-18 | 24/38 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.476×** | -9.0 | 3e-17 | 26/38 (AN3 CA, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.496×** | -8.5 | 2e-15 | 21/37 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -7.0 | 3e-10 | 23/38 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.602×** | -6.1 | 6e-08 | 21/38 (A-172, AN3 CA, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.670×** | -4.5 | 4e-04 | 12/34 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.537×** | -3.9 | 0.005 | 9/36 (SK-MEL-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.547×** | -3.8 | 0.007 | 9/37 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.043 | 9/38 (A-172, C32, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -3.3 | 0.043 | 10/36 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.764×** | -3.3 | 0.044 | 10/38 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -3.1 | 0.079 | 12/38 (SW480, SK-MEL-2, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.624×** | -3.0 | 0.098 | 9/38 (AN3 CA, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.783×** | -3.0 | 0.098 | 6/37 (AN3 CA, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 64.6 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0816× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Verteporfin (drug)]] 5 µM 0.0846× (z -11.2) |
| [[BT-474 (line)]] | alt | 8.99 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -9.4) |
| [[HT-29 (line)]] | alt | 5.74 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0650× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0411× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 8.15 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0834× (z -20.1) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -14.4) |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0812× (z -18.6) |
| [[HS-578T (line)]] | alt | 9.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0373× (z -15.7) |
| [[SW480 (line)]] | alt | 7.86 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0638× (z -17.0) |
| [[C32 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.126× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 3.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -8.5) |
| [[KATO III (line)]] | alt | 3.99 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0774× (z -8.6) |
| [[LS 180 (line)]] | wt | 2.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0620× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 6.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0467× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 7.85 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0692× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 8.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -8.7) |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.0) |
| [[A-427 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.902 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.682 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.569 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.620 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC6A16]] | +0.68 | +0.70 / +0.55 | both halves | 1e-05 | ⚠ same locus (15.4 kb, same strand: neighbours can correlate without regulation) |
| [[AMFR]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[SENP3]] | +0.56 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[GATA2-AS1]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SELENON]] | +0.55 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[MFSD14B]] | +0.55 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MSI1]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[B4GALNT4]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.54 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MLLT1]] | +0.53 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[AKT1]] | +0.53 | +0.56 / +0.50 | both halves | 1e-05 | pathway: Regulation of T cell activation by CD28 family |
| [[TLE5]] | +0.52 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[UBE2G1]] | +0.51 | +0.66 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCFD1]] | -0.52 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[BCL10]] | -0.50 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[PTER]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DIS3]] | -0.47 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[GOLGB1]] | -0.47 | -0.59 / -0.25 | both halves | 4e-04 |  |
| [[H3-3B]] | -0.47 | -0.59 / -0.26 | both halves | 4e-04 |  |
| [[LYSMD3]] | -0.47 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[AGGF1]] | -0.46 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[CEP63]] | -0.46 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[ZNF622]] | -0.46 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ZNF674]] | -0.46 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[LINC01473]] | -0.46 | -0.51 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRPA]] | B | SIRPA activity raises TEAD2's level | lines that do not express SIRPA (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without SIRPA | 0.012 | ⚠ within organs, on part of the lines; also absent: EID2B, LIX1L, FHL1 |
| [[MSI1]] | B | MSI1 activity raises TEAD2's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.83× lower at baseline in the lines without MSI1 | 0.062 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[SLC6A16]] | C | SLC6A16 activity raises TEAD2's level | lines that do not express SLC6A16 (11) vs lines expressing it (39) | 3.65× lower at baseline in the lines without SLC6A16 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSZ]] | B | TEAD2 activity raises CTSZ's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without TEAD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| cells under [[Penfluridol (drug)]] 5 µM | B | TEAD2 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express TEAD2 (9) vs lines expressing it (39) | the lines without TEAD2: 1.18× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| [[GLB1]] | B | TEAD2 activity raises GLB1's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.24× lower at baseline in the lines without TEAD2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| [[MBOAT7]] | B | TEAD2 activity raises MBOAT7's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.32× lower at baseline in the lines without TEAD2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | B | TEAD2 activity lowers the cells' numbers under Riluzole hydrochloride 0.05 µM (makes them more sensitive) | lines that do not express TEAD2 (9) vs lines expressing it (39) | the lines without TEAD2: 1.13× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | B | TEAD2 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TEAD2 (9) vs lines expressing it (39) | the lines without TEAD2: 1.15× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| [[PLCG1]] | B | TEAD2 activity raises PLCG1's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without TEAD2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| [[SLC6A16]] | C | TEAD2 activity raises SLC6A16's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 3.89× lower at baseline in the lines without TEAD2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17; co-absent with the target |

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, -15.4); signed map (-40.9, -26.3). **Vector** length 64.3, 11.5% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +9.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -17.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -18.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -4.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TEA domain transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,340,595-49,362,457 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TEF-4, ETF, TEF4 |
| Gene groups (HGNC) | TEA domain transcription factors |
| Reactome | 10 pathways, smallest: RUNX3 regulates YAP1-mediated transcription; Formation of axial mesoderm; YAP1- and WWTR1 (TAZ)-stimulated gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15562](https://www.uniprot.org/uniprotkb/Q15562) (Transcriptional enhancer factor TEF-4):

> Transcription factor which plays a key role in the Hippo signaling pathway, a pathway involved in organ size control and tumor suppression by restricting proliferation and promoting apoptosis. The core of this pathway is composed of a kinase cascade wherein MST1/MST2, in complex with its regulatory protein SAV1, phosphorylates and activates LATS1/2 in complex with its regulatory protein MOB1, which in turn phosphorylates and inactivates YAP1 oncoprotein and WWTR1/TAZ. Acts by mediating gene …

**Summary**, from NCBI Gene [8463](https://www.ncbi.nlm.nih.gov/gene/8463):

> Enables several functions, including DNA-binding transcription factor activity; disordered domain specific binding activity; and transcription coactivator binding activity. Involved in hippo signaling; positive regulation of DNA-templated transcription; and protein-containing complex assembly. Located in nucleoplasm. Part of TEAD-YAP complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11715) · Entrez [8463](https://www.ncbi.nlm.nih.gov/gene/8463) · UniProt [Q15562](https://www.uniprot.org/uniprotkb/Q15562) · Ensembl [ENSG00000074219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074219)

## Data

Gene col 1073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1073); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1073]; `tensor/DDL_lfc|DDL_z.npy` [1073]; `embed/gene_vectors.npy` [1073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1073 or target_col == 1073). Every well: [[TEAD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEAD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
