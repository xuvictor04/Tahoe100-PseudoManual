---
symbol: "DZIP1"
type: "gene"
col: 5618
ensembl_id: "ENSG00000134874"
name: "DAZ interacting zinc finger protein 1"
location: "13q32.1"
module: 82
arm: "+"
pooled_cpm: 14.16
n_lines_expressing: 27
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# DZIP1

*DAZ interacting zinc finger protein 1* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.22× (z +17.9, q 0e+00, up in 11 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.18× (z +17.5, q 0e+00, up in 10 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.390×, SHP-77 0.398×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0540×; ⚠ cell-cycle shift, explains ~72% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0595×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.243×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP16]] (+0.58, fdr 1e-05), [[PDGFD]] (+0.52, fdr 2e-05), [[HMCN1]] (+0.51, fdr 1e-05); moves opposite to [[EMP3]] (-0.44, fdr 6e-05), [[ZNF846]] (-0.41, fdr 2e-04), [[ING2]] (-0.41, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SPTBN2]] → it (grade B ⚠); 3 go from it, the strongest it → [[MMP16]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +17.9 | 0e+00 | 11/18 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.18×** | +17.5 | 0e+00 | 10/25 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +16.9 | 0e+00 | 15/23 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.63×** | +15.4 | 0e+00 | 21/25 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.83×** | +13.7 | 2e-40 | 10/19 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.13×** | +12.1 | 1e-31 | 19/25 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.80×** | +9.4 | 4e-19 | 18/25 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +9.2 | 4e-18 | 11/25 (hTERT-HPNE, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.54×** | +6.7 | 2e-09 | 8/25 (NCI-H460, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +6.6 | 2e-09 | 18/25 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +6.6 | 2e-09 | 8/25 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.5 | 3e-09 | 13/25 (HOP62, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +6.2 | 2e-08 | 10/23 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +5.3 | 4e-06 | 9/25 (A-172, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.3 | 5e-06 | 4/18 (NCI-H2347, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +5.2 | 7e-06 | 14/25 (PANC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.5 | 2e-04 | 4/25 (A549, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +4.3 | 4e-04 | 6/25 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 1e-03 | 7/25 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.003 | 7/24 (J82, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.038 | 0/25 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.053 | 7/25 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5618.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.390×, SHP-77 0.398×); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0540×; ⚠ cell-cycle shift, explains ~72% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (AN3 CA 0.0595×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.243×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.845× | -3.8 | 0.081 | 3/25 (PANC-1, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.656× | -3.5 | 0.12 | 13/25 (SHP-77, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 0.669× | -3.4 | 0.12 | 9/25 (AN3 CA, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.813× | -3.3 | 0.12 | 11/25 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.815× | -3.3 | 0.12 | 10/25 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.820× | -3.2 | 0.15 | 13/24 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.816× | -3.1 | 0.15 | 9/24 (NCI-H661, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 27.4 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.45× (z +14.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Digitoxin (drug)]] 0.5 µM 0.390× (z -9.1) |
| [[A-427 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 89.6 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0595× (z -12.5) |
| [[HOP62 (line)]] | alt | 30.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +13.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 44.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -9.5) |
| [[A-172 (line)]] | wt | 51.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.270× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 63.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.221× (z -11.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 27.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 68.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0540× (z -13.9) ⚠ cell-cycle shift, explains ~72% of this change |
| [[hTERT-HPNE (line)]] | wt | 44.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +12.2) | — |
| [[J82 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.52 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP16]] | +0.58 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PDGFD]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[HMCN1]] | +0.51 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[SUGCT]] | +0.51 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ANGPT1]] | +0.50 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SLC6A15]] | +0.50 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[HS6ST2]] | +0.49 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[ST6GALNAC3]] | +0.48 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[TMEM108]] | +0.47 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MED12L]] | +0.47 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[EMB]] | +0.47 | +0.26 / +0.54 | both halves | 4e-04 |  |
| [[AADAT]] | +0.46 | +0.40 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMP3]] | -0.44 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[ZNF846]] | -0.41 | -0.30 / -0.41 | both halves | 2e-04 | same gene group |
| [[ING2]] | -0.41 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[FBXL12]] | -0.39 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[RNASE4]] | -0.39 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTBN2]] | B | SPTBN2 activity lowers DZIP1's level | lines that do not express SPTBN2 (9) vs lines expressing it (41) | 2.14× higher at baseline in the lines without SPTBN2 | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC88C, HID1, ASS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DZIP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MMP16]] | C | MMP16 activity raises DZIP1's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 4.84× lower at baseline in the lines without MMP16 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP16]] | C | DZIP1 activity raises MMP16's level | lines that do not express DZIP1 (23) vs lines expressing it (27) | 5.58× lower at baseline in the lines without DZIP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: BVES, LAYN, GLIS1; co-absent with the target |
| [[SYNM]] | C | DZIP1 activity raises SYNM's level | lines that do not express DZIP1 (23) vs lines expressing it (27) | 3.03× lower at baseline in the lines without DZIP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: BVES, LAYN, GLIS1; co-absent with the target |
| [[ANGPT1]] | C | DZIP1 activity raises ANGPT1's level | lines that do not express DZIP1 (23) vs lines expressing it (27) | 3.17× lower at baseline in the lines without DZIP1 | 0.098 | ⚠ within organs, on part of the lines; also absent: BVES, LAYN, GLIS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.312). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.8, 36.2); signed map (38.2, 33.6). **Vector** length 56.0, 13.1% of its response variance represented; |z| ≥ 3 in 557 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +17.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +13.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.9 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.0 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.5 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | DAZ interacting zinc finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:95,578,202-95,644,706 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0996, DZIP |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Centriolar satellite proteins |
| Reactome | 2 pathways, smallest: Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YF9](https://www.uniprot.org/uniprotkb/Q86YF9) (Cilium assembly protein DZIP1):

> Molecular adapter that recruits protein complexes required for cilium assembly and function to the cilium basal body. At the exit of mitosis, localizes to the basal body and ciliary base of the forming primary cilium where it recruits and activates RAB8A to direct vesicle-mediated transport of proteins to the cilium (By similarity). Also recruits the BBSome, a complex involved in cilium biogenesis, by bridging it to PCM1 at the centriolar satellites of the cilium. It is also required for the …

**Summary**, from NCBI Gene [22873](https://www.ncbi.nlm.nih.gov/gene/22873):

> Enables BBSome binding activity and molecular adaptor activity. Involved in cilium organization; heart development; and protein-containing complex localization to centriolar satellite. Located in cytosol; microtubule organizing center; and nucleoplasm. Implicated in mitral valve prolapse and spermatogenic failure 47. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20908](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20908) · Entrez [22873](https://www.ncbi.nlm.nih.gov/gene/22873) · UniProt [Q86YF9](https://www.uniprot.org/uniprotkb/Q86YF9) · Ensembl [ENSG00000134874](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134874)

## Data

Gene col 5618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5618); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5618]; `tensor/DDL_lfc|DDL_z.npy` [5618]; `embed/gene_vectors.npy` [5618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5618 or target_col == 5618). Every well: [[DZIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DZIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
