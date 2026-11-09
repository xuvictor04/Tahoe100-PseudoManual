---
symbol: "FLACC1"
type: "gene"
col: 7913
ensembl_id: "ENSG00000155749"
name: "flagellum associated containing coiled-coil domains 1"
location: "2q33.1"
module: 39
arm: "+"
pooled_cpm: 11.32
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# FLACC1

*flagellum associated containing coiled-coil domains 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Filgotinib (drug)]] 5 µM: 1.89× (z +5.4, q 4e-05, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.137× (z -16.7, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKDD1B]] (+0.81, fdr 7e-06), [[SLC22A14]] (+0.80, fdr 7e-06), [[CDKL4]] (+0.80, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NEK10]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Filgotinib (drug)]] 5 µM |  | **1.89×** | +5.4 | 4e-05 | 31/47 (NCI-H460, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.024 | 21/43 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.024 | 19/47 (A498, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.47× | +3.1 | 0.27 | 16/40 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.137×** | -16.7 | 0e+00 | 45/47 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.234×** | -12.2 | 6e-32 | 38/43 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.270×** | -11.0 | 6e-26 | 41/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.276×** | -10.8 | 3e-25 | 41/46 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.348×** | -8.5 | 1e-15 | 29/39 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.225×** | -6.6 | 5e-09 | 35/47 (RPMI-7951, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.267×** | -5.8 | 5e-07 | 29/43 (LOX-IMVI, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.517×** | -5.3 | 7e-06 | 29/46 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.505×** | -5.2 | 2e-05 | 21/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.584×** | -4.5 | 3e-04 | 23/46 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.588×** | -4.5 | 4e-04 | 23/46 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.574×** | -4.2 | 0.001 | 22/47 (H4, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.414×** | -3.9 | 0.004 | 18/41 (C32, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.647×** | -3.7 | 0.010 | 16/43 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -3.5 | 0.015 | 18/36 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.668×** | -3.2 | 0.047 | 15/46 (C32, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.682×** | -3.1 | 0.065 | 18/45 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.671×** | -3.0 | 0.079 | 19/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.692×** | -3.0 | 0.081 | 8/47 (SK-MEL-2, LS 180, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.2 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0704× (z -13.5) |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0457× (z -14.3) |
| [[LoVo (line)]] | wt | 10.8 | 0 | 5 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0399× (z -16.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.116× (z -11.7) |
| [[H4 (line)]] | wt | 18.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0370× (z -11.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0531× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0303× (z -15.5) |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0761× (z -13.4) |
| [[A549 (line)]] | wt | 8.74 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0891× (z -11.4) |
| [[J82 (line)]] | alt | 19.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0647× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0782× (z -10.8) |
| [[SW480 (line)]] | alt | 9.00 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -11.0) |
| [[A-172 (line)]] | wt | 14.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0436× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0389× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -11.0) |
| [[HS-578T (line)]] | alt | 17.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0960× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0775× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -9.8) |
| [[SNU-423 (line)]] | alt | 8.98 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0775× (z -10.4) |
| [[A-427 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.140× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 9.07 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0446× (z -11.8) |
| [[C32 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0544× (z -11.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 6.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0372× (z -12.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 8.10 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 7.32 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0486× (z -11.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0367× (z -12.4) |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0727× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKDD1B]] | +0.81 | +0.85 / +0.79 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.80 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GARIN1A]] | +0.77 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.74 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.73 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.73 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.73 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[GCNA]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK10]] | B | NEK10 activity raises FLACC1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without NEK10 | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[WNT5B]] | B | WNT5B activity raises FLACC1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 1.50× lower at baseline in the lines without WNT5B | 0.048 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[ACOT12]] | B | ACOT12 activity raises FLACC1's level | lines that do not express ACOT12 (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without ACOT12 | 0.050 | ⚠ within organs, on part of the lines; also absent: SSBP2, TBC1D32, SOX12; maybe low, not absent |
| [[CFAP161]] | B | CFAP161 activity raises FLACC1's level | lines that do not express CFAP161 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without CFAP161 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRB1; maybe low, not absent; its own permutation p |
| [[LINC02133]] | C | LINC02133 activity raises FLACC1's level | lines that do not express LINC02133 (4) vs lines expressing it (46) | 1.94× lower at baseline in the lines without LINC02133 | 0.056 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LYG1, RBM44, TRIM72; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | FLACC1's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | FLACC1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.5, -14.6); signed map (16.7, 8.4). **Vector** length 83.9, 18.9% of its response variance represented; |z| ≥ 3 in 1,175 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.8 |
| fall | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.9 | -3.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.8 | -12.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -16.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -10.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | flagellum associated containing coiled-coil domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,288,271-201,357,398 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ALS2CR12 |
| Matched by | ensembl_id |

UniProt [Q96Q35](https://www.uniprot.org/uniprotkb/Q96Q35) carries no function annotation.

**Summary**, from NCBI Gene [130540](https://www.ncbi.nlm.nih.gov/gene/130540):

> Predicted to be located in cytoplasmic vesicle; outer dense fiber; and sperm fibrous sheath. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14439) · Entrez [130540](https://www.ncbi.nlm.nih.gov/gene/130540) · UniProt [Q96Q35](https://www.uniprot.org/uniprotkb/Q96Q35) · Ensembl [ENSG00000155749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155749)

## Data

Gene col 7913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7913); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7913]; `tensor/DDL_lfc|DDL_z.npy` [7913]; `embed/gene_vectors.npy` [7913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7913 or target_col == 7913). Every well: [[FLACC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FLACC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
