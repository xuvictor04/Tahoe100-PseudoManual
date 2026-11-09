---
symbol: "C2orf49"
type: "gene"
col: 5794
ensembl_id: "ENSG00000135974"
name: "tRNA splicing ligase complex subunit 2"
location: "2q12.2"
module: 119
arm: "+"
pooled_cpm: 38.25
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# C2orf49

*tRNA splicing ligase complex subunit 2* — 2q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.45× (z +8.4, q 4e-14, up in 29 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 0.314×, SHP-77 0.240×, NCI-H2030 0.328×, NCI-H1792 0.345×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.479×, C32 0.490×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.261×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.373×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL14]] (+0.64, fdr 7e-06), [[SLC4A1AP]] (+0.62, fdr 9e-06), [[RAMAC]] (+0.61, fdr 1e-05); moves opposite to [[TTL]] (-0.51, fdr 3e-05), [[LRP8]] (-0.49, fdr 4e-05), [[NPIPB4]] (-0.49, fdr 3e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF292]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +8.4 | 4e-14 | 29/48 (LoVo, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +7.9 | 7e-13 | 2/48 (MIA PaCa-2, HOP62) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +7.9 | 7e-13 | 30/48 (A498, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +7.0 | 4e-10 | 27/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.9 | 5e-07 | 22/47 (A-427, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 1e-05 | 22/48 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +5.0 | 5e-05 | 25/47 (LOX-IMVI, SW48, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.25×** | +4.6 | 2e-04 | 20/43 (NCI-H460, SW480, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +4.3 | 0.001 | 16/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +3.9 | 0.005 | 19/48 (LOX-IMVI, BT-474, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.19× | +3.8 | 0.007 | 13/48 (H4, A498, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.17× | +3.5 | 0.022 | 12/48 (A498, A-427, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.17× | +3.4 | 0.025 | 13/48 (SW480, PANC-1, …) | top dose only | composition shift |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.055 | 6/48 (SW48, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.15× | +3.1 | 0.083 | 4/48 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.0 | 0.087 | 7/48 (A498, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5794.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 0.314×, SHP-77 0.240×, NCI-H2030 0.328×, NCI-H1792 0.345×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.479×, C32 0.490×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.261×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (C32 0.373×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.836× | -3.9 | 0.047 | 18/47 (C32, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.845× | -3.7 | 0.047 | 16/39 (HEC-1-A, SHP-77, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.850× | -3.7 | 0.047 | 16/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.896× | -3.5 | 0.058 | 10/48 (SW1417, SW 1088, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.863× | -3.2 | 0.15 | 6/48 (SW480, A-172, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.870× | -3.1 | 0.16 | 7/48 (HepG2/C3A, NCI-H460, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 46.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -8.6) |
| [[A-427 (line)]] | wt | 28.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 40.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.261× (z -11.1) |
| [[SW480 (line)]] | alt | 48.0 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HEC-1-A (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 51.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -8.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-172 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL14]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 | STRING 463 |
| [[SLC4A1AP]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[RAMAC]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MED6]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZNF12]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SECISBP2L]] | +0.59 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[ATG14]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[USP30]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ZNF576]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MRPL44]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[VIRMA]] | +0.56 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CRNKL1]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.51 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[LRP8]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[NPIPB4]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[HNRNPAB]] | -0.49 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[SMG1P3]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[SLFNL1-AS1]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[RANGAP1]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PKP4]] | -0.48 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[ASAP2]] | -0.48 | -0.40 / -0.48 | both halves | 4e-05 |  |
| [[UGGT2]] | -0.47 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CYFIP1]] | -0.47 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF292]] | C | ZNF292's natural level weakens C2orf49's drug response | ZNF292's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.07; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.524). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.6, 5.0); signed map (-11.2, -12.5). **Vector** length 76.5, 14.2% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.1 | +7.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.3 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +8.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.1 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.1 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -2.7 | -3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | -1.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing ligase complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.2 — chr2:105,337,532-105,349,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5509, asw; previously C2orf49 |
| Gene groups (HGNC) | tRNA splicing ligase complex |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVC5](https://www.uniprot.org/uniprotkb/Q9BVC5) (tRNA splicing ligase complex subunit 2):

> Accessory subunit of the tRNA-splicing ligase complex that acts by directly joining spliced tRNA halves to mature-sized tRNAs by incorporating the precursor-derived splice junction phosphate into the mature tRNA as a canonical 3',5'-phosphodiester. May act as an RNA ligase with broad substrate specificity and may function toward other RNAs.

**Summary**, from NCBI Gene [79074](https://www.ncbi.nlm.nih.gov/gene/79074):

> Predicted to be involved in tRNA splicing, via endonucleolytic cleavage and ligation. Located in nucleoplasm. Part of tRNA-splicing ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28772) · Entrez [79074](https://www.ncbi.nlm.nih.gov/gene/79074) · UniProt [Q9BVC5](https://www.uniprot.org/uniprotkb/Q9BVC5) · Ensembl [ENSG00000135974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135974)

## Data

Gene col 5794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5794); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5794]; `tensor/DDL_lfc|DDL_z.npy` [5794]; `embed/gene_vectors.npy` [5794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5794 or target_col == 5794). Every well: [[C2orf49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2orf49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
