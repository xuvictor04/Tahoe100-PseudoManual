---
symbol: "SEMA3A"
type: "gene"
col: 1104
ensembl_id: "ENSG00000075213"
name: "semaphorin 3A"
location: "7q21.11"
module: 81
arm: "+"
pooled_cpm: 300.45
n_lines_expressing: 31
n_dd_up: 7
n_dd_down: 44
n_dd_up_clean: 6
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# SEMA3A

*semaphorin 3A* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.63× (z +7.1, q 6e-10, up in 11 of 29 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +5.5, q 1e-05, up in 10 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.349× (z -16.0, q 0e+00, down in 28 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRDM8]] (+0.66, fdr 7e-06), [[SERPIND1]] (+0.65, fdr 1e-05), [[PLAU]] (+0.63, fdr 7e-06); moves opposite to [[TSC22D3]] (-0.56, fdr 1e-05), [[ACSL1]] (-0.54, fdr 1e-05), [[MAP3K6]] (-0.49, fdr 4e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IER3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SERPINE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +7.1 | 6e-10 | 11/29 (SNU-423, SW 900, …) | rises with dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.5 | 1e-05 | 10/29 (SW1417, SNU-423, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.037 | 12/30 (A549, SW 900, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.037 | 18/29 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.041 | 11/29 (RKO, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.044 | 11/30 (SK-MEL-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.057 | 7/29 (A549, AsPC-1, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.17 | 9/29 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.17 | 8/30 (NCI-H2347, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 9 with an alert ⚠; shown: the 15 strongest. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.349×** | -16.0 | 0e+00 | 28/29 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.369×** | -15.1 | 0e+00 | 29/29 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.491×** | -10.8 | 9e-25 | 27/29 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.512×** | -10.1 | 7e-22 | 24/29 (SW480, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -8.0 | 2e-13 | 24/30 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.725×** | -6.9 | 5e-10 | 19/29 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -6.3 | 3e-08 | 23/29 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.655×** | -6.2 | 3e-08 | 18/31 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.669×** | -6.1 | 7e-08 | 16/29 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.687×** | -5.7 | 7e-07 | 16/29 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.773×** | -5.5 | 2e-06 | 18/29 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.698×** | -5.5 | 2e-06 | 16/29 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.701×** | -5.4 | 3e-06 | 17/29 (NCI-H1792, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.704×** | -5.3 | 5e-06 | 19/29 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.709×** | -5.2 | 7e-06 | 18/29 (H4, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 518 | 0 | 21 (2 ⚠) | — | [[Dexamethasone (drug)]] 5 µM 0.146× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 374 | 0 | 20 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.156× (z -12.7) |
| [[SW480 (line)]] | alt | 579 | 0 | 15 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0419× (z -28.9) |
| [[NCI-H460 (line)]] | wt | 876 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -20.6) |
| [[NCI-H1573 (line)]] | alt | 162 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -22.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.257× (z -12.9) |
| [[RKO (line)]] | wt | 1,382 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -26.2) |
| [[C32 (line)]] | wt | 277 | 0 | 11 | — | [[Radotinib (drug)]] 5 µM 0.173× (z -13.8) |
| [[A-427 (line)]] | wt | 3,226 | 0 | 9 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.176× (z -18.0) |
| [[LoVo (line)]] | wt | 168 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 267 | 0 | 9 | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -12.3) |
| [[SNU-423 (line)]] | alt | 170 | 2 (2 ⚠) | 7 | [[Harringtonine (drug)]] 5 µM 4.12× (z +11.9) ⚠ cell-cycle shift, explains ~28% of this change | [[Budesonide (drug)]] 0.05 µM 0.315× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 560 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.116× (z -21.1) |
| [[Hs 766T (line)]] | wt | 87.9 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dexamethasone (drug)]] 0.05 µM 0.260× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 945 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0819× (z -26.2) |
| [[NCI-H2030 (line)]] | alt | 296 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -15.1) |
| [[SNU-1 (line)]] | wt | 298 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.214× (z -12.1) |
| [[A549 (line)]] | wt | 88.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 0.363× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 385 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -18.4) |
| [[SW 900 (line)]] | alt | 173 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -9.6) |
| [[SW1417 (line)]] | alt | 85.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.4) |
| [[C-33 A (line)]] | alt | 115 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -11.2) |
| [[NCI-H661 (line)]] | alt | 758 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 90.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.99× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 82.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -9.0) |
| [[A-172 (line)]] | wt | 52.2 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 30.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 45.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 40.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 44.4 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 74.7 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 40.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 68.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 52.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 34.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 70.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 311 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 67.4 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 59.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 261 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM8]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SERPIND1]] | +0.65 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[PLAU]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[FST]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[NCEH1]] | +0.60 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[LINC00973]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CD274]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[AADAC]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PKIA]] | +0.58 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[LINC00472]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PHLDA1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ACSL1]] | -0.54 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[MAP3K6]] | -0.49 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[GLUL]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ALDH2]] | -0.48 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[SCARB1]] | -0.47 | -0.46 / -0.43 | both halves | 4e-05 |  |
| [[MAOA]] | -0.47 | -0.52 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IER3]] | B | IER3 activity lowers SEMA3A's level | lines that do not express IER3 (5) vs lines expressing it (45) | 5.89× higher at baseline in the lines without IER3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[SEMA3D]] | C | SEMA3D activity raises SEMA3A's level | lines that do not express SEMA3D (31) vs lines expressing it (19) | 4.18× lower at baseline in the lines without SEMA3D | 0.001 | ⚠ within organs, on part of the lines; also absent: COL3A1, HS3ST3A1, THY1; co-absent with the target |
| [[SYNJ2]] | C | SYNJ2 activity lowers SEMA3A's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 5.73× higher at baseline in the lines without SYNJ2 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE2]] | B | SEMA3A activity raises SERPINE2's level | lines that do not express SEMA3A (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without SEMA3A | 0.097 | ⚠ within organs, on part of the lines; also absent: PRRX2, SEMA3D, CD5L |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.9, 15.3); signed map (18.5, 52.6). **Vector** length 125, 36.9% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.0 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +5.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.1 | +3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +2.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.2 | -6.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.7 | -6.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.5 | -6.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.5 | -4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.4 | -5.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:83,955,777-84,492,724 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SEMA1, SemD, coll-1, Hsema-I; previously SEMAD |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Semaphorins |
| Reactome | 6 pathways, smallest: SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; CRMPs in Sema3A signaling; Sema3A PAK dependent Axon repulsion |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14563](https://www.uniprot.org/uniprotkb/Q14563) (Semaphorin-3A):

> Involved in the development of the olfactory system and in neuronal control of puberty. Induces the collapse and paralysis of neuronal growth cones. Could serve as a ligand that guides specific growth cones by a motility-inhibiting mechanism. Binds to the complex neuropilin-1/plexin-1.

**Summary**, from NCBI Gene [10371](https://www.ncbi.nlm.nih.gov/gene/10371):

> This gene is a member of the semaphorin family and encodes a protein with an Ig-like C2-type (immunoglobulin-like) domain, a PSI domain and a Sema domain. This secreted protein can function as either a chemorepulsive agent, inhibiting axonal outgrowth, or as a chemoattractive agent, stimulating the growth of apical dendrites. In both cases, the protein is vital for normal neuronal pattern development. Increased expression of this protein is associated with schizophrenia and is seen in a variety …

**Accessions** — [HGNC:10723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10723) · Entrez [10371](https://www.ncbi.nlm.nih.gov/gene/10371) · UniProt [Q14563](https://www.uniprot.org/uniprotkb/Q14563) · Ensembl [ENSG00000075213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075213)

## Data

Gene col 1104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1104); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1104]; `tensor/DDL_lfc|DDL_z.npy` [1104]; `embed/gene_vectors.npy` [1104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1104 or target_col == 1104). Every well: [[SEMA3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
