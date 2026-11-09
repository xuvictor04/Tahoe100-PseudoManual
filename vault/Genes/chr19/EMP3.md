---
symbol: "EMP3"
type: "gene"
col: 6610
ensembl_id: "ENSG00000142227"
name: "epithelial membrane protein 3 (MAM blood group)"
location: "19q13.33"
module: 95
arm: "+"
pooled_cpm: 45.7
n_lines_expressing: 41
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# EMP3

*epithelial membrane protein 3 (MAM blood group)* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.32× (z +6.6, q 2e-08, up in 32 of 37 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 2.64×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.62×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.211× (z -12.2, q 2e-31, down in 38 of 39 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WBP4]] (+0.63, fdr 1e-05), [[TCEAL3]] (+0.60, fdr 2e-05), [[UNK]] (+0.59, fdr 2e-05); moves opposite to [[WASF3]] (-0.65, fdr 1e-05), [[MCOLN2]] (-0.56, fdr 1e-05), [[TRAP1]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 7 go from it, the strongest it → [[LRCH3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6610.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 2.64×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 3.62×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.32×** | +6.6 | 2e-08 | 32/37 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +4.4 | 0.003 | 23/31 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.70×** | +4.2 | 0.006 | 22/39 (PANC-1, C32, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.56×** | +3.5 | 0.061 | 24/39 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.49× | +3.2 | 0.13 | 19/39 (C32, NCI-H2030, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.53× | +3.1 | 0.13 | 21/34 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.50× | +3.1 | 0.13 | 20/38 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 1.47× | +3.1 | 0.13 | 21/39 (NCI-H2030, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.49× | +3.1 | 0.13 | 18/36 (J82, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.47× | +3.0 | 0.13 | 22/39 (C32, A-427, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.211×** | -12.2 | 2e-31 | 38/39 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.230×** | -11.5 | 3e-28 | 39/39 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.252×** | -10.8 | 6e-25 | 39/39 (HS-578T, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.389×** | -7.4 | 2e-11 | 34/39 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.452×** | -6.2 | 6e-08 | 35/39 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.235×** | -5.3 | 1e-05 | 35/39 (HS-578T, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.629×** | -3.6 | 0.024 | 27/39 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.632×** | -3.6 | 0.024 | 26/39 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.648× | -3.1 | 0.11 | 32/39 (SW 1088, A549, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.650× | -3.1 | 0.11 | 27/39 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.648× | -3.0 | 0.11 | 21/39 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.760× | -3.0 | 0.11 | 21/39 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.679× | -3.0 | 0.11 | 22/39 (HS-578T, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 57.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.152× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 68.9 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -11.4) |
| [[H4 (line)]] | wt | 91.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0756× (z -12.6) |
| [[HOP62 (line)]] | alt | 47.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0998× (z -13.3) |
| [[HS-578T (line)]] | alt | 97.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0845× (z -16.1) |
| [[hTERT-HPNE (line)]] | wt | 88.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -11.0) |
| [[PANC-1 (line)]] | alt | 36.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.234× (z -9.6) |
| [[SNU-1 (line)]] | wt | 154 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 72.9 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.202× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 85.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 78.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 56.0 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.142× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 52.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -11.7) |
| [[SW 900 (line)]] | alt | 78.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -9.5) |
| [[SW480 (line)]] | alt | 31.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.160× (z -11.9) |
| [[C32 (line)]] | wt | 66.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 64.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 94.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -10.9) |
| [[A-427 (line)]] | wt | 34.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -12.5) |
| [[A549 (line)]] | wt | 74.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 30.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.206× (z -8.9) |
| [[Hs 766T (line)]] | wt | 48.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -10.5) |
| [[SNU-423 (line)]] | alt | 31.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.160× (z -9.4) |
| [[SW 1088 (line)]] | alt | 116 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0889× (z -8.6) |
| [[A498 (line)]] | wt | 86.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP4]] | +0.63 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TCEAL3]] | +0.60 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[UNK]] | +0.59 | +0.49 / +0.52 | both halves | 2e-05 |  |
| [[PLA2G4C]] | +0.59 | +0.56 / +0.38 | both halves | 6e-05 |  |
| [[S100A3]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LINC02307]] | +0.57 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[LRCH3]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[NUTM2E]] | +0.57 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[NPHS1]] | +0.57 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[MAP3K20-AS1]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[THAP2]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TCEAL4]] | +0.56 | +0.52 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.65 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[MCOLN2]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[TRAP1]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[JAM3]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TCOF1]] | -0.56 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[FBXW2]] | -0.56 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[WDR5]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[STRAP]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PTGES2]] | -0.55 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[PARP1]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[SKP2]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.53 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EMP3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FMNL1-DT]] | B | FMNL1-DT activity raises EMP3's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 2.02× lower at baseline in the lines without FMNL1-DT | 0.089 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRCH3]] | B | EMP3 activity raises LRCH3's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without EMP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[TRNAU1AP]] | B | EMP3 activity raises TRNAU1AP's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without EMP3 | 0.061 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[SAMD4A-AS1]] | B | EMP3 activity raises SAMD4A-AS1's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.25× lower at baseline in the lines without EMP3 | 0.062 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[APLF]] | B | EMP3 activity raises APLF's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 2.07× lower at baseline in the lines without EMP3 | 0.067 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[CAVIN1]] | B | EMP3 activity raises CAVIN1's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 4.73× lower at baseline in the lines without EMP3 | 0.088 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[CYP20A1]] | B | EMP3 activity raises CYP20A1's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without EMP3 | 0.099 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[RAB34]] | C | EMP3 activity raises RAB34's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 7.15× lower at baseline in the lines without EMP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17; co-absent with the target |

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (17.8, 9.0); signed map (20.4, -13.3). **Vector** length 93.2, 33.8% of its response variance represented; |z| ≥ 3 in 702 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.9 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | -0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | -1.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -2.2 | -3.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -5.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | epithelial membrane protein 3 (MAM blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,321,509-48,330,553 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YMP |
| Gene groups (HGNC) | Blood group antigens |
| Hallmark sets | INFLAMMATORY_RESPONSE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [P54852](https://www.uniprot.org/uniprotkb/P54852) (Epithelial membrane protein 3):

> Probably involved in cell proliferation and cell-cell interactions.

**Summary**, from NCBI Gene [2014](https://www.ncbi.nlm.nih.gov/gene/2014):

> The protein encoded by this gene belongs to the PMP-22/EMP/MP20 family of proteins. The protein contains four transmembrane domains and two N-linked glycosylation sites. It is thought to be involved in cell proliferation, cell-cell interactions and function as a tumor suppressor. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:3335](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3335) · Entrez [2014](https://www.ncbi.nlm.nih.gov/gene/2014) · UniProt [P54852](https://www.uniprot.org/uniprotkb/P54852) · Ensembl [ENSG00000142227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142227)

## Data

Gene col 6610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6610); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6610]; `tensor/DDL_lfc|DDL_z.npy` [6610]; `embed/gene_vectors.npy` [6610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6610 or target_col == 6610). Every well: [[EMP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
