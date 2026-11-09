---
symbol: "SLC31A2"
type: "gene"
col: 5923
ensembl_id: "ENSG00000136867"
name: "solute carrier family 31 member 2"
location: "9q32"
module: 16
arm: "+"
pooled_cpm: 3.28
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SLC31A2

*solute carrier family 31 member 2* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.84× (z +21.8, q 0e+00, up in 33 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.0716×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (LoVo 0.0782×); [[Busulfan (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0615×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UAP1L1]] (+0.70, fdr 7e-06), [[BTN2A2]] (+0.68, fdr 7e-06), [[NECAP2]] (+0.66, fdr 7e-06); moves opposite to [[SETD3]] (-0.64, fdr 7e-06), [[TTC13]] (-0.60, fdr 2e-05), [[STRAP]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC02154]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.84×** | +21.8 | 0e+00 | 33/36 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.66×** | +12.2 | 9e-32 | 34/42 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.75×** | +9.9 | 9e-21 | 26/37 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.0 | 3e-07 | 1/6 (PANC-1) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +5.9 | 4e-07 | 5/8 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +5.9 | 4e-07 | 21/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +5.7 | 1e-06 | 14/45 (SW480, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +5.5 | 3e-06 | 15/46 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +5.1 | 2e-05 | 15/45 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +5.1 | 2e-05 | 13/43 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.9 | 4e-05 | 18/42 (SW480, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.7 | 1e-04 | 6/18 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +4.6 | 1e-04 | 17/46 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.78×** | +4.0 | 0.002 | 7/17 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.51×** | +4.0 | 0.002 | 4/19 (PANC-1, HEC-1-A, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.003 | 6/37 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.003 | 13/45 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.006 | 12/44 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.007 | 6/46 (J82, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5923.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (NCI-H460 0.0716×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (LoVo 0.0782×); [[Busulfan (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0615×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.770× | -3.6 | 0.16 | 11/45 (NCI-H460, NCI-H2347, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.734× | -3.0 | 0.65 | 4/46 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.49 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +14.4) | — |
| [[NCI-H460 (line)]] | wt | 3.25 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +11.1) | [[Pimozide (drug)]] 0.05 µM 0.0716× (z -11.0) |
| [[A-172 (line)]] | wt | 3.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +13.9) | — |
| [[Hs 766T (line)]] | wt | 5.45 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +8.6) | [[Rapamycin (drug)]] 0.5 µM 0.0841× (z -9.0) |
| [[J82 (line)]] | alt | 5.41 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +16.4) | — |
| [[LoVo (line)]] | wt | 3.67 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +8.7) | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0782× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 3.00 | 0 | 2 | — | [[Busulfan (drug)]] 0.5 µM 0.0615× (z -9.2) |
| [[PANC-1 (line)]] | alt | 2.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +14.5) | — |
| [[SNU-423 (line)]] | alt | 4.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +13.2) | — |
| [[A549 (line)]] | wt | 2.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 3.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 5.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +12.9) | — |
| [[Panc 03.27 (line)]] | alt | 4.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +11.1) | — |
| [[RPMI-7951 (line)]] | alt | 4.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +8.5) | — |
| [[A-427 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UAP1L1]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[BTN2A2]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[NECAP2]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CDK3]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[DEDD]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ZNF554]] | +0.64 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[SLC2A6]] | +0.63 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[DLX2]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[C11orf96]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ZSCAN18]] | +0.62 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[CCDC102A]] | +0.62 | +0.66 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.64 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[TTC13]] | -0.60 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[STRAP]] | -0.60 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[MFN1]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[DPAGT1]] | -0.60 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[WRNIP1]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[MLEC]] | -0.59 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[MTRR]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.58 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[BPNT2]] | -0.58 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ACTL6A]] | -0.58 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TXNDC5]] | -0.56 | -0.58 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02154]] | B | LINC02154 activity weakens SLC31A2's drug response | lines that do not express LINC02154 (36) vs lines expressing it (11) | the lines without LINC02154 respond 0.82× as strongly (z diff +0.38); strongest at Panobinostat 0.5 µM: 1.90x vs 1.03x (z diff -1.9) | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530; target measured in part of the lines; both ways; artifact flags |
| [[SLC2A6]] | B | SLC2A6 activity raises SLC31A2's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 1.36× lower at baseline in the lines without SLC2A6 | 0.066 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[LINC02154]] | B | LINC02154 activity raises SLC31A2's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 1.18× lower at baseline in the lines without LINC02154 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530 |
| [[SLC2A6]] | B | SLC2A6 activity strengthens SLC31A2's drug response | lines that do not express SLC2A6 (6) vs lines expressing it (41) | the lines without SLC2A6 respond 0.67× as strongly (z diff +0.96); strongest at Homoharringtonine 5 µM: 2.05x vs 5.66x (z diff +4.3) | 0.093 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CEP112]] | C | CEP112 activity raises SLC31A2's level | lines that do not express CEP112 (3) vs lines expressing it (47) | 1.66× lower at baseline in the lines without CEP112 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: P3H1, SH2B3, VAT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.462). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (19.7, 6.8); signed map (4.7, -10.1). **Vector** length 56.8, 7.77% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +21.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +9.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.1 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 31 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,150,976-113,164,140 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hCTR2, CTR2; previously COPT2 |
| Gene groups (HGNC) | Solute carrier family 31 |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [O15432](https://www.uniprot.org/uniprotkb/O15432) (Protein SLC31A2):

> Does not function as a copper(1+) importer in vivo (By similarity). However, in vitro functions as a low-affinity copper(1+) importer. Regulator of SLC31A1 which facilitates the cleavage of the SLC31A1 ecto-domain or which stabilizes the truncated form of SLC31A1 (Truncated CTR1 form), thereby drives the SLC31A1 truncated form-dependent endosomal copper export and modulates the copper and cisplatin accumulation via SLC31A1 (By similarity).

**Summary**, from NCBI Gene [1318](https://www.ncbi.nlm.nih.gov/gene/1318):

> Enables copper ion transmembrane transporter activity. Involved in copper ion import. Located in late endosome membrane; lysosomal membrane; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11017) · Entrez [1318](https://www.ncbi.nlm.nih.gov/gene/1318) · UniProt [O15432](https://www.uniprot.org/uniprotkb/O15432) · Ensembl [ENSG00000136867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136867)

## Data

Gene col 5923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5923); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5923]; `tensor/DDL_lfc|DDL_z.npy` [5923]; `embed/gene_vectors.npy` [5923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5923 or target_col == 5923). Every well: [[SLC31A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC31A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
