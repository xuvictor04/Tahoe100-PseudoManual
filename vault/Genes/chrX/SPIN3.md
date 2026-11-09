---
symbol: "SPIN3"
type: "gene"
col: 12842
ensembl_id: "ENSG00000204271"
name: "spindlin family member 3"
location: "Xp11.21"
module: 4
arm: "+"
pooled_cpm: 16.82
n_lines_expressing: 46
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SPIN3

*spindlin family member 3* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.65× (z +9.6, q 5e-19, up in 36 of 44 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.56× (z +6.0, q 4e-07, up in 29 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.454× (z -10.8, q 2e-24, down in 32 of 44 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.664× (z -8.0, q 4e-13, down in 29 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00665]] (+0.60, fdr 1e-05), [[TRMT11]] (+0.59, fdr 2e-05), [[C5orf63]] (+0.59, fdr 1e-05); moves opposite to [[DDT]] (-0.52, fdr 1e-05), [[CDKL5]] (-0.52, fdr 1e-04), [[WDR44]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF527]] → it (grade C ⚠); 2 go from it, the strongest it → [[TTC14]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.65×** | +9.6 | 5e-19 | 36/44 (SNU-423, HOP62, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +6.0 | 4e-07 | 29/44 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.6 | 3e-06 | 27/44 (A498, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.39×** | +4.5 | 0.001 | 16/43 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.1 | 0.004 | 2/44 (NCI-H23, SW 1088) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.004 | 17/43 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.006 | 12/43 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +3.9 | 0.006 | 17/43 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.8 | 0.009 | 12/38 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.012 | 20/44 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.033 | 8/44 (SNU-423, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.035 | 18/44 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.040 | 10/43 (HT-29, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.454×** | -10.8 | 2e-24 | 32/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.507×** | -9.3 | 4e-18 | 29/42 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -8.0 | 4e-13 | 29/43 (Hs 766T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.640×** | -6.1 | 1e-07 | 26/42 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.696×** | -5.0 | 7e-05 | 22/43 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.696×** | -4.7 | 2e-04 | 22/44 (COLO 205, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.723×** | -4.5 | 6e-04 | 21/43 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -4.0 | 0.005 | 21/43 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.835× | -3.5 | 0.026 | 15/44 (COLO 205, PANC-1, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.770×** | -3.4 | 0.039 | 12/43 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.784×** | -3.2 | 0.071 | 16/43 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.800×** | -3.1 | 0.099 | 9/43 (SW 1271, LS 180, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.6 | 0 | 6 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0867× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0730× (z -12.8) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H1573 (line)]] | alt | 17.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 14.4 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.100× (z -10.9) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW480 (line)]] | alt | 33.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -10.5) ⚠ cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 15.0 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.128× (z -8.5) |
| [[HOP62 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.230× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 20.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -15.5) |
| [[HS-578T (line)]] | alt | 7.80 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.114× (z -10.1) |
| [[HT-29 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[SHP-77 (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.49× (z +8.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[SW1417 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00665]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[TRMT11]] | +0.59 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[C5orf63]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MRPL3]] | +0.59 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[RABGGTB]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PGGT1B]] | +0.56 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[ZNF589]] | +0.56 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[RRN3P1]] | +0.56 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ZNF780B]] | +0.55 | +0.43 / +0.66 | both halves | 4e-05 |  |
| [[ZNF283]] | +0.55 | +0.33 / +0.67 | both halves | 1e-04 |  |
| [[COG8]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TIGD1]] | +0.54 | +0.31 / +0.66 | both halves | 2e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDT]] | -0.52 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CDKL5]] | -0.52 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[WDR44]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PRADC1]] | -0.50 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[OST4]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.49 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[TOM1L2]] | -0.49 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[ORMDL2]] | -0.48 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[NUMB]] | -0.48 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PKNOX1]] | -0.48 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[EMSY]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[ZNF324]] | -0.47 | -0.09 / -0.53 | ⚠ one half (not replicated) | 0.003 |  |
| [[SELENOK]] | -0.46 | -0.25 / -0.49 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF527]] | C | ZNF527 activity raises SPIN3's level | lines that do not express ZNF527 (3) vs lines expressing it (47) | 3.91× lower at baseline in the lines without ZNF527 | 0.011 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC14]] | C | SPIN3 activity raises TTC14's level | lines that do not express SPIN3 (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without SPIN3 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IRAK2, EXO5, ZNF567; its own permutation p |
| [[RMDN2]] | C | SPIN3 activity raises RMDN2's level | lines that do not express SPIN3 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without SPIN3 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IRAK2, EXO5, ZNF567; its own permutation p |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.425). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.4, 3.4); signed map (7.4, -41.1). **Vector** length 69.4, 12.6% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.7 | +9.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +3.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.4 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -1.9 | -9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | spindlin family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:56,818,298-56,995,827 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TDRD27 |
| Gene groups (HGNC) | Tudor domain containing; Spindlin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JUX0](https://www.uniprot.org/uniprotkb/Q5JUX0) (Spindlin-3):

> Exhibits H3K4me3-binding activity.

**Summary**, from NCBI Gene [169981](https://www.ncbi.nlm.nih.gov/gene/169981):

> Enables histone H3K4me3 reader activity. Predicted to be involved in regulation of DNA-templated transcription. Predicted to be active in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27272) · Entrez [169981](https://www.ncbi.nlm.nih.gov/gene/169981) · UniProt [Q5JUX0](https://www.uniprot.org/uniprotkb/Q5JUX0) · Ensembl [ENSG00000204271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204271)

## Data

Gene col 12842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12842); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12842]; `tensor/DDL_lfc|DDL_z.npy` [12842]; `embed/gene_vectors.npy` [12842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12842 or target_col == 12842). Every well: [[SPIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
