---
symbol: "TCEA2"
type: "gene"
col: 10149
ensembl_id: "ENSG00000171703"
name: "transcription elongation factor A2"
location: "20q13.33"
module: 21
arm: "+"
pooled_cpm: 11.89
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TCEA2

*transcription elongation factor A2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.88× (z +24.0, q 0e+00, up in 31 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.55× (z +5.4, q 7e-06, up in 22 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.437× (z -10.3, q 3e-22, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KNDC1]] (+0.62, fdr 1e-05), [[CCDC183]] (+0.61, fdr 5e-05), [[ANO8]] (+0.58, fdr 2e-05); moves opposite to [[CCDC137]] (-0.48, fdr 3e-04), [[KIAA1586]] (-0.45, fdr 5e-05), [[TRMT5]] (-0.45, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[JPH3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10149.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.88×** | +24.0 | 0e+00 | 31/31 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.16×** | +23.5 | 0e+00 | 19/21 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.16×** | +16.4 | 0e+00 | 27/27 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +5.4 | 7e-06 | 22/42 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 3e-04 | 20/42 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.002 | 14/41 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.7 | 0.018 | 15/36 (CFPAC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.018 | 11/39 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.024 | 7/42 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.029 | 10/38 (A549, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.033 | 12/40 (SW480, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.042 | 5/40 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.3 | 0.049 | 12/34 (MIA PaCa-2, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.057 | 9/35 (NCI-H460, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -10.3 | 3e-22 | 27/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.658×** | -7.4 | 4e-11 | 23/40 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.561×** | -7.2 | 8e-11 | 26/40 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -7.2 | 8e-11 | 26/39 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.563×** | -6.9 | 6e-10 | 25/40 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -6.8 | 1e-09 | 21/41 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -6.6 | 2e-09 | 23/41 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.606×** | -6.3 | 3e-08 | 19/40 (SNU-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -6.0 | 1e-07 | 20/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.760×** | -3.4 | 0.032 | 16/41 (SNU-1, LOX-IMVI, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.075 | 13/41 (A-172, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 10.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 17.1× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -10.9) |
| [[SW480 (line)]] | alt | 11.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 11.4× (z +16.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -9.2) |
| [[A498 (line)]] | wt | 12.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.22× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 12.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.17× (z +11.3) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -8.6) ⚠ cell-cycle shift, explains ~2% of this change |
| [[NCI-H460 (line)]] | wt | 7.46 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.88× (z +11.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 14.5× (z +13.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.160× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -13.0) |
| [[A-172 (line)]] | wt | 28.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 43.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.6× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 7.96 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.293× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 11.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.5× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 11.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 10.6× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -11.6) |
| [[A-427 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -12.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 7.14 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.10× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 13.4 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0673× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 7.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.15× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 28.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.230× (z -10.8) |
| [[SHP-77 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.3× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -8.5) |
| [[SNU-1 (line)]] | wt | 8.54 | 0 | 1 | — | [[Celecoxib (drug)]] 0.05 µM 0.0625× (z -8.6) |
| [[SNU-423 (line)]] | alt | 8.14 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0707× (z -9.4) |
| [[A549 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KNDC1]] | +0.62 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[CCDC183]] | +0.61 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[ANO8]] | +0.58 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[TMEM219]] | +0.57 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[CFL1P1-1]] | +0.57 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MORF4L1]] | +0.56 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[MAP3K12]] | +0.55 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[ZC3H3]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[PALM]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[GSTM2]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PDZD4]] | +0.53 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[MYO1F]] | +0.53 | +0.51 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC137]] | -0.48 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[KIAA1586]] | -0.45 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[TRMT5]] | -0.45 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[NIP7]] | -0.43 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[CMTR2]] | -0.43 | -0.31 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JPH3]] | B | JPH3 activity raises TCEA2's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without JPH3 | 0.030 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.351). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.2, 28.4); signed map (-28.8, -2.7). **Vector** length 70.5, 13.1% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +23.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +24.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | transcription elongation factor A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:64,049,836-64,072,347 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15560](https://www.uniprot.org/uniprotkb/Q15560) (Transcription elongation factor A protein 2):

> Necessary for efficient RNA polymerase II transcription elongation past template-encoded arresting sites. The arresting sites in DNA have the property of trapping a certain fraction of elongating RNA polymerases that pass through, resulting in locked ternary complexes. Cleavage of the nascent transcript by S-II allows the resumption of elongation from the new 3'-terminus.

**Summary**, from NCBI Gene [6919](https://www.ncbi.nlm.nih.gov/gene/6919):

> The protein encoded by this gene is found in the nucleus, where it functions as an SII class transcription elongation factor. Elongation factors in this class are responsible for releasing RNA polymerase II ternary complexes from transcriptional arrest at template-encoded arresting sites. The encoded protein has been shown to interact with general transcription factor IIB, a basal transcription factor. Two transcript variants encoding different isoforms have been found for this gene. [provided …

**Accessions** — [HGNC:11614](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11614) · Entrez [6919](https://www.ncbi.nlm.nih.gov/gene/6919) · UniProt [Q15560](https://www.uniprot.org/uniprotkb/Q15560) · Ensembl [ENSG00000171703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171703)

## Data

Gene col 10149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10149); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10149]; `tensor/DDL_lfc|DDL_z.npy` [10149]; `embed/gene_vectors.npy` [10149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10149 or target_col == 10149). Every well: [[TCEA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCEA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
