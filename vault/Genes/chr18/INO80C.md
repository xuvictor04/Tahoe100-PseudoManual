---
symbol: "INO80C"
type: "gene"
col: 7718
ensembl_id: "ENSG00000153391"
name: "INO80 complex subunit C"
location: "18q12.2"
module: 109
arm: "+"
pooled_cpm: 18.04
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# INO80C

*INO80 complex subunit C* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 1.44× (z +8.1, q 4e-13, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.594× (z -7.7, q 6e-12, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFNB2]] (+0.56, fdr 1e-05), [[LIPG]] (+0.56, fdr 1e-05), [[LDLR]] (+0.56, fdr 1e-05); moves opposite to [[TTC9C]] (-0.57, fdr 1e-05), [[GAPVD1]] (-0.53, fdr 4e-05), [[CNNM2]] (-0.51, fdr 2e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **1.44×** | +8.1 | 4e-13 | 29/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.39×** | +7.3 | 8e-11 | 28/48 (HOP62, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.5 | 0.001 | 14/48 (Hs 766T, Panc 03.27, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.004 | 15/47 (LOX-IMVI, HOP62, …) | two highest doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.8 | 0.016 | 10/29 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.027 | 9/47 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.037 | 12/46 (NCI-H460, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.072 | 14/47 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.2 | 0.092 | 10/47 (A498, HT-29, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +3.2 | 0.092 | 18/43 (A-427, J82, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.098 | 17/47 (AsPC-1, NCI-H2347, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.100 | 11/47 (LOX-IMVI, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +3.0 | 0.100 | 14/33 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.100 | 9/48 (SW480, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -7.7 | 6e-12 | 28/47 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.639×** | -6.9 | 1e-09 | 29/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -6.5 | 2e-08 | 25/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -5.4 | 6e-06 | 20/46 (A-427, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -5.4 | 6e-06 | 22/47 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.728×** | -4.9 | 9e-05 | 22/45 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.730×** | -4.9 | 1e-04 | 22/46 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.754×** | -4.4 | 9e-04 | 14/47 (AsPC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.759×** | -4.3 | 0.001 | 19/47 (NCI-H1792, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.770×** | -4.0 | 0.003 | 19/47 (LS 180, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.793×** | -3.6 | 0.018 | 17/47 (LS 180, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.045 | 15/47 (hTERT-HPNE, SW48, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.809×** | -3.3 | 0.047 | 14/40 (CFPAC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.802×** | -3.1 | 0.068 | 14/47 (SW480, RKO, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.1 | 0.073 | 12/48 (RKO, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.822×** | -3.0 | 0.093 | 13/47 (NCI-H1792, RKO, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.872× | -3.0 | 0.095 | 10/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 8.92 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.70× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -12.5) |
| [[A-427 (line)]] | wt | 15.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 9.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0927× (z -8.7) ⚠ cell-cycle shift, explains ~1% of this change |
| [[LS 180 (line)]] | wt | 43.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.573× (z -10.2) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 10.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.197× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~3% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -8.6) |
| [[SW 900 (line)]] | alt | 6.94 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0942× (z -9.0) |
| [[A-172 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFNB2]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[LIPG]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LDLR]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[LINC01204]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TMC7]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SERPINB8]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TRIB1]] | +0.54 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[OGDH]] | +0.54 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[GALNT1]] | +0.53 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[F2RL1]] | +0.53 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[CD58]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[LINC00460]] | +0.52 | +0.43 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9C]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[GAPVD1]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CNNM2]] | -0.51 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CRAMP1]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[BRWD1]] | -0.50 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[GID8]] | -0.50 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[HINFP]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[FHIP2A]] | -0.48 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[MAX]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 | STRING 900 |
| [[CDAN1]] | -0.45 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[KDM3A]] | -0.45 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[AGAP3]] | -0.45 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA2]] | B | CA2 activity raises INO80C's level | lines that do not express CA2 (27) vs lines expressing it (23) | 1.43× lower at baseline in the lines without CA2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4 |
| [[TOP2A]] | B | TOP2A activity raises INO80C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, -14.6); signed map (1.2, 40.7). **Vector** length 94.2, 19.4% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.5 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | +4.1 | +0.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.5 | +7.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.0 | +8.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | INO80 complex subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:35,452,230-35,497,979 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38183, hIes6, IES6; previously C18orf37 |
| Gene groups (HGNC) | INO80 complex subunits |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PI98](https://www.uniprot.org/uniprotkb/Q6PI98) (INO80 complex subunit C):

> Proposed core component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair.

**Summary**, from NCBI Gene [125476](https://www.ncbi.nlm.nih.gov/gene/125476):

> Involved in several processes, including positive regulation of DNA-templated transcription; regulation of DNA metabolic process; and regulation of chromosome organization. Located in fibrillar center and nucleoplasm. Part of Ino80 complex and MLL1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26994) · Entrez [125476](https://www.ncbi.nlm.nih.gov/gene/125476) · UniProt [Q6PI98](https://www.uniprot.org/uniprotkb/Q6PI98) · Ensembl [ENSG00000153391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153391)

## Data

Gene col 7718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7718); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7718]; `tensor/DDL_lfc|DDL_z.npy` [7718]; `embed/gene_vectors.npy` [7718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7718 or target_col == 7718). Every well: [[INO80C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INO80C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
