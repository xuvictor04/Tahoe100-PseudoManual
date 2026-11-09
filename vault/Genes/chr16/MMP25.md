---
symbol: "MMP25"
type: "gene"
col: 176
ensembl_id: "ENSG00000008516"
name: "matrix metallopeptidase 25"
location: "16p13.3"
module: 47
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 47
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/047", "written"]
generated_by: "tahoemap"
---

# MMP25

*matrix metallopeptidase 25* — 16p13.3

> [!summary] In one line
> MMP25 encodes MT6-MMP, or leukolysin, a GPI-anchored membrane-type matrix metalloproteinase whose expression is essentially confined to the leukocyte lineage.

## What it is

MMP25 was cloned from leukocytes and found, across a panel of tissues, in peripheral blood leukocytes and almost nowhere else. It carries the standard metalloproteinase architecture but is tethered to the outer face of the plasma membrane by a glycosylphosphatidylinositol anchor rather than a transmembrane helix, a feature it shares only with MT4-MMP (MMP17) among the membrane-type enzymes. In resting neutrophils the protein sits in specific and gelatinase granules, secretory vesicles and the plasma membrane, and is mobilised to the surface on stimulation. It degrades matrix substrates in vitro and has been reported to activate progelatinase A at the cell surface. The gene lies at 16p13.3.

## What is uncertain

The first problem is whether the transcript is really there. A gene this restricted to neutrophils should read near zero in pooled epithelial and mesenchymal cancer lines, so a usable signal is as plausibly ambient RNA or low-level ectopic transcription as genuine expression. Nothing links MMP25 to p53 or to membrane repair, and its reported tumour roles rest on few studies.

## References

- Pei, 1999, Cell Research — cloned leukolysin/MMP25 and showed its expression is restricted to the leukocyte lineage.
- Kang et al., 2001, Journal of Biological Chemistry — localised leukolysin to neutrophil granule compartments and showed its mobilisation on stimulation.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 20.8× (z +24.6, q 0e+00, up in 27 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH2D4B]] (+0.81, fdr 7e-06), [[GRIK5]] (+0.80, fdr 7e-06), [[THOC6]] (+0.78, fdr 7e-06, ⚠ same locus), [[CHADL]] (+0.77, fdr 7e-06); moves opposite to [[CRYZL1]] (-0.63, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01250]] → it (grade B ⚠); 10 go from it, the strongest it → [[ALPK3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **20.8×** | +24.6 | 0e+00 | 27/29 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **10.7×** | +13.6 | 1e-39 | 25/27 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.36×** | +8.5 | 5e-15 | 23/34 (SW480, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +7.0 | 5e-10 | 16/29 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +6.2 | 6e-08 | 2/3 (A498, HOP62) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +5.4 | 5e-06 | 0/4 | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.49×** | +5.1 | 3e-05 | 19/35 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.13×** | +4.4 | 9e-04 | 5/13 (AsPC-1, PANC-1, …) | all doses, flat | composition shift |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.77×** | +3.3 | 0.062 | 3/23 (PANC-1, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.642× | -3.5 | 0.22 | 13/42 (SW480, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.564× | -3.3 | 0.32 | 16/43 (SNU-423, NCI-H1573, …) | top dose only | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.567× | -3.0 | 0.40 | 6/34 (SW480, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 2.09 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 125× (z +11.0) | — |
| [[LoVo (line)]] | wt | 2.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 70.6× (z +17.4) | — |
| [[NCI-H1573 (line)]] | alt | 4.72 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.1× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 69.2× (z +15.4) | — |
| [[A-172 (line)]] | wt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 1.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.2× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 4.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.3× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 3.38 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.2× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 4.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +8.6) | — |
| [[KATO III (line)]] | alt | 2.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 6.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 0.718 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.0× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 1.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.4× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 1.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.9× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 1.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.8× (z +8.9) | — |
| [[SW480 (line)]] | alt | 4.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +11.3) | — |
| [[A-427 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.802 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.692 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.657 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH2D4B]] | +0.81 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.80 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[THOC6]] | +0.78 | +0.78 / +0.75 | both halves | 7e-06 | ⚠ same locus (18.3 kb, same strand: neighbours can correlate without regulation) |
| [[CHADL]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.77 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[PPIEL-1]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ZNF34]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[MPP4]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.76 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ZDHHC11]] | +0.75 | +0.71 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | -0.63 | -0.58 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01250]] | B | LINC01250 activity raises MMP25's level | lines that do not express LINC01250 (10) vs lines expressing it (40) | 1.83× lower at baseline in the lines without LINC01250 | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises MMP25's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without LINC00334 | 0.067 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[EFNA2]] | B | EFNA2 activity raises MMP25's level | lines that do not express EFNA2 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without EFNA2 | 0.097 | ⚠ within organs, on part of the lines; also absent: TFR2, USP43, BTG3-AS1; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALPK3]] | C | MMP25 activity lowers ALPK3's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 3.53× higher at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent; its own permutation p |
| [[PHEX]] | C | MMP25 activity raises PHEX's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 2.14× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |
| [[SLC22A1]] | C | MMP25 activity raises SLC22A1's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent; its own permutation p |
| [[MPP4]] | C | MMP25 activity raises MPP4's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent; co-absent with the target |
| [[USP50]] | C | MMP25 activity raises USP50's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.57× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |
| [[NLGN3]] | C | MMP25 activity raises NLGN3's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |
| [[ALDH8A1]] | C | MMP25 activity raises ALDH8A1's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.48× lower at baseline in the lines without MMP25 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent; its own permutation p |
| [[GARIN1A]] | C | MMP25 activity raises GARIN1A's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.96× lower at baseline in the lines without MMP25 | 0.091 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |
| [[SLC9A5]] | C | MMP25 activity raises SLC9A5's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.32× lower at baseline in the lines without MMP25 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |
| [[MSS51]] | C | MMP25 activity raises MSS51's level | lines that do not express MMP25 (3) vs lines expressing it (47) | 1.58× lower at baseline in the lines without MMP25 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000250842, MPP4, KDELR3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.3, -12.9); signed map (19.7, 10.9). **Vector** length 72.7, 13.4% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +24.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +13.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +5.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -0.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.8 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,046,062-3,060,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MT6-MMP; previously MMPL1, MMP20 |
| Gene groups (HGNC) | M10 matrix metallopeptidases |
| Reactome | 5 pathways, smallest: Activation of Matrix Metalloproteinases; Degradation of the extracellular matrix; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPA2](https://www.uniprot.org/uniprotkb/Q9NPA2) (Matrix metalloproteinase-25):

> May activate progelatinase A.

**Summary**, from NCBI Gene [64386](https://www.ncbi.nlm.nih.gov/gene/64386):

> Proteins of the matrix metalloproteinase (MMP) family are involved in the breakdown of extracellular matrix in normal physiological processes, such as embryonic development, reproduction, and tissue remodeling, as well as in disease processes, such as arthritis and metastasis. Most MMPs are secreted as inactive proproteins which are activated when cleaved by extracellular proteinases. However, the protein encoded by this gene is a member of the membrane-type MMP (MT-MMP) subfamily, attached to …

**Accessions** — [HGNC:14246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14246) · Entrez [64386](https://www.ncbi.nlm.nih.gov/gene/64386) · UniProt [Q9NPA2](https://www.uniprot.org/uniprotkb/Q9NPA2) · Ensembl [ENSG00000008516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008516)

## Data

Gene col 176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 176); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 176]; `tensor/DDL_lfc|DDL_z.npy` [176]; `embed/gene_vectors.npy` [176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 176 or target_col == 176). Every well: [[MMP25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MMP25.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
