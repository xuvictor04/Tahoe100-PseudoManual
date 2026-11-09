---
symbol: "BAIAP2"
type: "gene"
col: 10657
ensembl_id: "ENSG00000175866"
name: "BAR/IMD domain containing adaptor protein 2"
location: "17q25.3"
module: 129
arm: "+"
pooled_cpm: 46.98
n_lines_expressing: 49
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# BAIAP2

*BAR/IMD domain containing adaptor protein 2* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 8.54× (z +28.2, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOSB]] (+0.58, fdr 1e-05), [[TUBB3]] (+0.56, fdr 1e-05), [[LASP1]] (+0.55, fdr 3e-05); moves opposite to [[ZNF567]] (-0.60, fdr 1e-05), [[ZNF16]] (-0.57, fdr 1e-05), [[ZNF329]] (-0.56, fdr 1e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10657.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **8.54×** | +28.2 | 0e+00 | 47/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.75×** | +24.6 | 0e+00 | 46/48 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.23×** | +21.8 | 0e+00 | 43/46 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.52×** | +18.6 | 0e+00 | 47/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.74×** | +17.3 | 0e+00 | 47/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.01×** | +14.5 | 1e-45 | 45/47 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +13.2 | 1e-37 | 42/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.69×** | +13.0 | 8e-37 | 45/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +10.8 | 1e-25 | 38/47 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +10.4 | 2e-23 | 40/46 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +9.8 | 5e-21 | 37/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +9.8 | 5e-21 | 38/46 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +9.3 | 8e-19 | 39/46 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.69×** | +6.9 | 3e-10 | 34/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.76×** | +6.2 | 3e-08 | 31/47 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.1 | 5e-08 | 22/47 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +6.0 | 6e-08 | 32/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10657.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Berbamine (drug)]] 0.05 µM |  | 0.754× | -3.3 | 0.55 | 11/47 (CHP-212, NCI-H2347, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.794× | -3.1 | 0.58 | 13/47 (NCI-H2347, HS-578T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10657. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.2 | 20 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 16.4× (z +20.2) | — |
| [[SW480 (line)]] | alt | 61.8 | 10 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 16.1× (z +26.1) | — |
| [[HEC-1-A (line)]] | alt | 77.3 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +19.0) | — |
| [[HS-578T (line)]] | alt | 23.5 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 22.7× (z +17.1) | — |
| [[LoVo (line)]] | wt | 21.9 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.61× (z +16.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 54.7 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +17.1) | — |
| [[SW48 (line)]] | wt | 58.3 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 16.8× (z +16.9) | — |
| [[AsPC-1 (line)]] | alt | 46.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +17.2) | — |
| [[HOP62 (line)]] | alt | 110 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +21.8) | — |
| [[KATO III (line)]] | alt | 78.5 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.21× (z +18.9) | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 9.25× (z +16.9) | — |
| [[LS 180 (line)]] | wt | 25.4 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +18.8) | — |
| [[NCI-H1573 (line)]] | alt | 15.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.69× (z +16.4) | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 12.7× (z +17.3) | — |
| [[A-427 (line)]] | wt | 19.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.48× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 20.4× (z +15.5) | — |
| [[SNU-423 (line)]] | alt | 34.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.31× (z +14.5) | — |
| [[A-172 (line)]] | wt | 67.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +12.5) | — |
| [[A498 (line)]] | wt | 53.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +33.2) | — |
| [[A549 (line)]] | wt | 17.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +18.1) | — |
| [[H4 (line)]] | wt | 50.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +13.9) | — |
| [[HCT15 (line)]] | alt | 71.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +16.0) | — |
| [[Hs 766T (line)]] | wt | 26.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.61× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 84.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +13.3) | — |
| [[SNU-1 (line)]] | wt | 20.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +11.8) | — |
| [[C-33 A (line)]] | alt | 22.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.68× (z +12.6) | — |
| [[C32 (line)]] | wt | 47.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.99× (z +15.0) | — |
| [[CFPAC-1 (line)]] | alt | 75.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 88.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.76× (z +14.3) | — |
| [[J82 (line)]] | alt | 21.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.93× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 75.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.64× (z +12.1) | — |
| [[RKO (line)]] | wt | 30.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +14.2) | — |
| [[SHP-77 (line)]] | alt | 24.1 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 14.8× (z +13.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 7.30× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 73.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 33.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 72.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.84× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 84.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 31.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 61.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.45× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10657), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOSB]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TUBB3]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[LASP1]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 | same gene group |
| [[VAMP1]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[NXF1]] | +0.54 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[MICALL2]] | +0.54 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SKI]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[NOTCH1]] | +0.52 | +0.53 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[PITRM1]] | +0.50 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[INPP5A]] | +0.50 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[ZFP36]] | +0.49 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[FOS]] | +0.49 | +0.46 / +0.56 | both halves | 2e-05 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF567]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[ZNF16]] | -0.57 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[ZNF329]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NDUFAF5]] | -0.55 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ZNF45]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[VPS54]] | -0.52 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[DHX57]] | -0.52 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[IRAK1BP1]] | -0.52 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ZNF133]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ATAD1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[ZNF639]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PRDM4]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BAIAP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC03046]] | B | LINC03046 activity lowers BAIAP2's level | lines that do not express LINC03046 (38) vs lines expressing it (12) | 1.60× higher at baseline in the lines without LINC03046 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, LINC00824, LINC01205 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction -0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.7, -2.6); signed map (2.1, 19.7). **Vector** length 96.9, 29.3% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.2 | +14.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.5 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +24.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.4 | +3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | +2.4 | +1.6 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.2 | +0.4 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.7 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.7 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.4 | +0.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -2.4 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | BAR/IMD domain containing adaptor protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,035,122-81,117,434 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BAP2, IRSp53, WAML |
| Gene groups (HGNC) | I-BAR domain containing; SH3 domain containing |
| Hallmark sets | APICAL_JUNCTION, P53_PATHWAY |
| Reactome | 19 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQB8](https://www.uniprot.org/uniprotkb/Q9UQB8) (BAR/IMD domain-containing adapter protein 2):

> Adapter protein that links membrane-bound small G proteins to cytoplasmic effector proteins. Necessary for CDC42-mediated reorganization of the actin cytoskeleton and for RAC1-mediated membrane ruffling. Involved in the regulation of the actin cytoskeleton by WASF family members and the Arp2/3 complex. Plays a role in neurite growth, neuronal differentiation and neuronal migration. Acts syngeristically with ENAH to promote filipodia formation. Plays a role in the reorganization of the actin …

**Summary**, from NCBI Gene [10458](https://www.ncbi.nlm.nih.gov/gene/10458):

> The protein encoded by this gene has been identified as a brain-specific angiogenesis inhibitor (BAI1)-binding protein. This adaptor protein links membrane bound G-proteins to cytoplasmic effector proteins. This protein functions as an insulin receptor tyrosine kinase substrate and suggests a role for insulin in the central nervous system. It also associates with a downstream effector of Rho small G proteins, which is associated with the formation of stress fibers and cytokinesis. This protein …

**Accessions** — [HGNC:947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:947) · Entrez [10458](https://www.ncbi.nlm.nih.gov/gene/10458) · UniProt [Q9UQB8](https://www.uniprot.org/uniprotkb/Q9UQB8) · Ensembl [ENSG00000175866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175866)

## Data

Gene col 10657: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10657); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10657, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10657]; `tensor/DDL_lfc|DDL_z.npy` [10657]; `embed/gene_vectors.npy` [10657]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10657 or target_col == 10657). Every well: [[BAIAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAIAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
