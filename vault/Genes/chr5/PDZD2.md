---
symbol: "PDZD2"
type: "gene"
col: 5446
ensembl_id: "ENSG00000133401"
name: "PDZ domain containing 2"
location: "5p13.3"
module: 98
arm: "+"
pooled_cpm: 21.62
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 6
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# PDZD2

*PDZ domain containing 2* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.08× (z +27.8, q 0e+00, up in 37 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.723× (z -5.7, q 8e-06, down in 18 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.753× (z -4.9, q 2e-04, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNB1]] (+0.61, fdr 1e-05), [[SAMSN1]] (+0.60, fdr 1e-05), [[TNS2]] (+0.60, fdr 2e-05); moves opposite to [[PDXP]] (-0.44, fdr 2e-04), [[PKIA]] (-0.43, fdr 1e-04), [[FOCAD]] (-0.43, fdr 3e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.08×** | +27.8 | 0e+00 | 37/45 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +21.6 | 0e+00 | 32/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.00×** | +18.5 | 0e+00 | 36/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +17.2 | 0e+00 | 19/24 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +17.0 | 0e+00 | 24/38 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +13.9 | 3e-42 | 20/31 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.66×** | +12.6 | 2e-34 | 36/48 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +9.0 | 2e-17 | 23/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.7 | 1e-12 | 21/48 (HOP62, SW1417, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.46×** | +6.7 | 2e-09 | 19/48 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.41×** | +6.0 | 1e-07 | 15/48 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.9 | 2e-07 | 20/48 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.9 | 2e-07 | 14/44 (AN3 CA, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.40×** | +5.8 | 2e-07 | 16/48 (HOP62, H4, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.42×** | +5.6 | 7e-07 | 16/46 (HOP62, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 9e-07 | 17/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +5.3 | 4e-06 | 18/48 (HOP62, H4, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 1e-05 | 19/48 (HOP62, H4, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5446.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.723×** | -5.7 | 8e-06 | 18/48 (H4, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.753×** | -4.9 | 2e-04 | 17/47 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.786×** | -4.2 | 0.005 | 13/48 (H4, RPMI-7951, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.801×** | -3.7 | 0.029 | 15/46 (C32, H4, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.677×** | -3.6 | 0.041 | 8/46 (Panc 03.27, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.817×** | -3.5 | 0.041 | 10/46 (C32, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.840× | -3.0 | 0.19 | 7/48 (HT-29, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 57.6 | 15 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 13.5× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0900× (z -9.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 29.5 | 15 | 0 | [[Dexamethasone (drug)]] 5 µM 17.5× (z +15.2) | — |
| [[SW 900 (line)]] | alt | 23.0 | 14 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.16× (z +16.2) | — |
| [[CFPAC-1 (line)]] | alt | 24.0 | 13 | 0 | [[Budesonide (drug)]] 5 µM 6.40× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 11.9 | 10 | 0 | [[Harringtonine (drug)]] 0.5 µM 9.76× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 6.66 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.8× (z +29.0) | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +25.4) | — |
| [[LoVo (line)]] | wt | 8.24 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 18.7× (z +15.2) | — |
| [[J82 (line)]] | alt | 25.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +19.0) | — |
| [[NCI-H460 (line)]] | wt | 6.97 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +10.8) | — |
| [[SW480 (line)]] | alt | 46.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -12.8) |
| [[A549 (line)]] | wt | 8.52 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 9.10 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.46× (z +11.6) | [[Nimesulide (drug)]] 5 µM 0.0793× (z -9.2) ⚠ toxic; unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 72.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +20.3) | — |
| [[Panc 03.27 (line)]] | alt | 79.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -10.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SHP-77 (line)]] | alt | 9.32 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.95× (z +10.2) | — |
| [[A-172 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0808× (z -12.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 7.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +11.7) | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0446× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 8.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 6.30 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.76× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 9.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +12.9) | — |
| [[RPMI-7951 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.140× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 8.16 | 0 | 1 | — | [[Ligustrazine (drug)]] 5 µM 0.0564× (z -8.6) |
| [[SW1417 (line)]] | alt | 34.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.53× (z +9.1) | — |
| [[A-427 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNB1]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SAMSN1]] | +0.60 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TNS2]] | +0.60 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[KLF9]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[EBI3]] | +0.57 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ABCA6]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CCND3]] | +0.57 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[UBE2E1]] | +0.57 | +0.33 / +0.49 | both halves | 1e-04 |  |
| [[TLR2]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SLC1A3]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[RIPOR2]] | +0.55 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CAV1]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXP]] | -0.44 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[PKIA]] | -0.43 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[FOCAD]] | -0.43 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[NGLY1]] | -0.43 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[FAM20B]] | -0.42 | -0.49 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises PDZD2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[SLC2A14]] | B | SLC2A14 activity raises PDZD2's level | lines that do not express SLC2A14 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without SLC2A14 | 0.076 | ⚠ within organs, on part of the lines; also absent: NPAS3, SLC2A3, HEY1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.7, 16.9); signed map (18.7, 30.1). **Vector** length 106, 24.7% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +17.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +27.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +12.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.2 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +7.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.4 | +5.3 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.3 | +5.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -5.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -3.5 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | PDZ domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:31,639,131-32,110,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0300; previously PDZK3 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

UniProt [O15018](https://www.uniprot.org/uniprotkb/O15018) carries no function annotation.

**Summary**, from NCBI Gene [23037](https://www.ncbi.nlm.nih.gov/gene/23037):

> The protein encoded by this gene contains six PDZ domains and shares sequence similarity with pro-interleukin-16 (pro-IL-16). Like pro-IL-16, the encoded protein localizes to the endoplasmic reticulum and is thought to be cleaved by a caspase to produce a secreted peptide containing two PDZ domains. In addition, this gene is upregulated in primary prostate tumors and may be involved in the early stages of prostate tumorigenesis. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:18486](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18486) · Entrez [23037](https://www.ncbi.nlm.nih.gov/gene/23037) · UniProt [O15018](https://www.uniprot.org/uniprotkb/O15018) · Ensembl [ENSG00000133401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133401)

## Data

Gene col 5446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5446); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5446]; `tensor/DDL_lfc|DDL_z.npy` [5446]; `embed/gene_vectors.npy` [5446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5446 or target_col == 5446). Every well: [[PDZD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDZD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
