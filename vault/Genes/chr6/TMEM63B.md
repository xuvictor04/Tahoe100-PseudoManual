---
symbol: "TMEM63B"
type: "gene"
col: 5988
ensembl_id: "ENSG00000137216"
name: "transmembrane protein 63B"
location: "6p21.1"
module: 14
arm: "+"
pooled_cpm: 33.77
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 4
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TMEM63B

*transmembrane protein 63B* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.53× (z +11.3, q 7e-27, up in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (J82 5.18×, HOP62 3.57×, Panc 03.27 3.82×, CFPAC-1 3.86×, …); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 5.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 4.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.718× (z -6.4, q 9e-08, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD40]] (+0.55, fdr 2e-05), [[NTN1]] (+0.55, fdr 4e-05), [[TTYH3]] (+0.53, fdr 1e-05); moves opposite to [[CCT2]] (-0.48, fdr 3e-05), [[COMMD10]] (-0.46, fdr 4e-05), [[MAK16]] (-0.45, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DRAM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 14 lines (J82 5.18×, HOP62 3.57×, Panc 03.27 3.82×, CFPAC-1 3.86×, …); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 5.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 4.53×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +11.3 | 7e-27 | 27/47 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.2 | 6e-05 | 23/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.3 | 0.003 | 23/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.11 | 19/48 (BT-474, SNU-423, …) | rises with dose | composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.17 | 7/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5988.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.718×** | -6.4 | 9e-08 | 25/48 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -6.2 | 2e-07 | 26/47 (LOX-IMVI, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.809×** | -4.1 | 0.007 | 18/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.822×** | -3.8 | 0.021 | 16/48 (AN3 CA, LOX-IMVI, …) | inconsistent across doses |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.839× | -3.4 | 0.076 | 10/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.844× | -3.3 | 0.092 | 10/48 (HCT15, SHP-77, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.834× | -3.3 | 0.093 | 17/47 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.15 | 12/47 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.857× | -3.0 | 0.17 | 5/48 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 44.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -15.1) |
| [[BT-474 (line)]] | alt | 25.0 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.40× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 16.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -13.6) |
| [[H4 (line)]] | wt | 56.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.6) | [[Docetaxel (drug)]] 0.05 µM 0.233× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 43.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +18.9) | — |
| [[J82 (line)]] | alt | 28.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +20.0) | — |
| [[LS 180 (line)]] | wt | 45.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 34.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 66.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +17.5) | — |
| [[A-172 (line)]] | wt | 55.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.6) | — |
| [[A498 (line)]] | wt | 49.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 48.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +17.0) | — |
| [[CHP-212 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.103× (z -8.9) ⚠ cell-cycle shift, explains ~6% of this change |
| [[HCT15 (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 32.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +16.2) | — |
| [[LoVo (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.0) | — |
| [[SNU-423 (line)]] | alt | 53.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.5) | — |
| [[A-427 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD40]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[NTN1]] | +0.55 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[TTYH3]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[STARD10]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[NINJ1]] | +0.53 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ADORA2A]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DTX2]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[TNFRSF9]] | +0.52 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[UBE2Z]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[MAN2B1]] | +0.52 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[TMCC2]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[TYK2]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT2]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[COMMD10]] | -0.46 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MAK16]] | -0.45 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[NAA15]] | -0.44 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[CCT5]] | -0.44 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[EEFSEC]] | -0.44 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[TRMT6]] | -0.44 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[TCERG1]] | -0.44 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[HEATR1]] | -0.43 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[PUDP]] | -0.43 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[PUM3]] | -0.43 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DRAM1]] | B | DRAM1 activity raises TMEM63B's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without DRAM1 | 0.049 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[FGF11]] | B | FGF11 activity lowers TMEM63B's level | lines that do not express FGF11 (9) vs lines expressing it (41) | 1.53× higher at baseline in the lines without FGF11 | 0.074 | ⚠ within organs, on part of the lines; also absent: C9orf64, CYB5A |
| [[NINJ1]] | B | NINJ1 activity strengthens TMEM63B's drug response | lines that do not express NINJ1 (5) vs lines expressing it (43) | the lines without NINJ1 respond 0.58× as strongly (z diff +0.68); strongest at Homoharringtonine 5 µM: 0.41x vs 1.48x (z diff +10.8) | 0.093 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[TMCC2]] | B | TMCC2 activity raises TMEM63B's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without TMCC2 | 0.098 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, 1.9); signed map (43.3, 10.1). **Vector** length 103, 22.8% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.3 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.9 | -3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 63B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,126,914-44,155,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434P0531, dJ421H19.2; previously C6orf110 |
| Gene groups (HGNC) | TMEM63 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T3F8](https://www.uniprot.org/uniprotkb/Q5T3F8) (Mechanosensitive cation channel TMEM63B):

> Mechanosensitive cation channel with low conductance and high activation threshold. Osmosensitive cation channel preferentially activated by hypotonic stress. Also acts as a phospholipid scramblase in response to changes in membrane structure: upon changes in membrane curvature and thickness, alters its conformation and translocates phospholipids, such as phosphatidylcholine and sphingomyelin, thereby controlling plasma membrane lipid distribution. Forms a heterodimer with SLC19A2, which …

**Summary**, from NCBI Gene [55362](https://www.ncbi.nlm.nih.gov/gene/55362):

> Enables calcium-activated cation channel activity; mechanosensitive monoatomic cation channel activity; and phospholipid scramblase activity. Predicted to be involved in several processes, including drinking behavior; intestinal stem cell homeostasis; and surfactant secretion. Located in actin cytoskeleton and bounding membrane of organelle. Is active in plasma membrane. Implicated in developmental and epileptic encephalopathy and developmental and epileptic encephalopathy 118. [provided by …

**Accessions** — [HGNC:17735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17735) · Entrez [55362](https://www.ncbi.nlm.nih.gov/gene/55362) · UniProt [Q5T3F8](https://www.uniprot.org/uniprotkb/Q5T3F8) · Ensembl [ENSG00000137216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137216)

## Data

Gene col 5988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5988); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5988]; `tensor/DDL_lfc|DDL_z.npy` [5988]; `embed/gene_vectors.npy` [5988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5988 or target_col == 5988). Every well: [[TMEM63B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM63B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
