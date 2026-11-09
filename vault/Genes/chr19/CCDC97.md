---
symbol: "CCDC97"
type: "gene"
col: 6591
ensembl_id: "ENSG00000142039"
name: "coiled-coil domain containing 97"
location: "19q13.2"
module: 38
arm: "+"
pooled_cpm: 23.21
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CCDC97

*coiled-coil domain containing 97* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +11.2, q 2e-26, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.658× (z -7.4, q 1e-10, down in 17 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.819× (z -4.8, q 2e-04, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM23]] (+0.67, fdr 7e-06), [[YJU2]] (+0.66, fdr 1e-05), [[THUMPD3-AS1]] (+0.64, fdr 1e-05); moves opposite to [[SETD3]] (-0.57, fdr 1e-05), [[METAP1]] (-0.56, fdr 1e-05), [[DCUN1D4]] (-0.55, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +11.2 | 2e-26 | 37/47 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +11.1 | 4e-26 | 38/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +7.9 | 4e-13 | 35/48 (LoVo, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +7.4 | 2e-11 | 28/47 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +7.3 | 3e-11 | 27/44 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 4e-09 | 26/47 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +5.6 | 2e-06 | 21/45 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 14/47 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +4.0 | 0.004 | 21/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.6 | 0.016 | 12/40 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.20×** | +3.3 | 0.046 | 16/46 (NCI-H460, KATO III, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.11 | 7/48 (RKO, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -7.4 | 1e-10 | 17/35 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.718×** | -6.1 | 4e-07 | 24/43 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.739×** | -5.3 | 2e-05 | 26/46 (SNU-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.819×** | -4.8 | 2e-04 | 17/48 (HEC-1-A, BT-474, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.616×** | -4.6 | 4e-04 | 14/48 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.789×** | -4.3 | 0.001 | 18/48 (BT-474, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -4.1 | 0.003 | 16/47 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.821×** | -3.6 | 0.021 | 12/46 (HEC-1-A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.046 | 15/47 (COLO 205, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.872× | -3.3 | 0.046 | 10/48 (SW480, PANC-1, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.880× | -3.1 | 0.089 | 8/48 (NCI-H1573, Panc 03.27, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 0.841× | -3.1 | 0.11 | 11/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 24.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -13.6) |
| [[A549 (line)]] | wt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -11.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 25.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -15.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 23.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 31.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.4) | — |
| [[A-172 (line)]] | wt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.146× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +16.2) | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.161× (z -8.6) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 23.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.183× (z -9.4) |
| [[HS-578T (line)]] | alt | 20.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +8.8) | — |
| [[KATO III (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -9.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0748× (z -18.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 19.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -12.2) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0699× (z -20.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[YJU2]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[THUMPD3-AS1]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[RBM10]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PILRA]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[LRRC23]] | +0.62 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ARL9]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[GARIN1A]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[ZNF830]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[MYOCOS]] | +0.61 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[ZNF546]] | +0.61 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.57 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[METAP1]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[DCUN1D4]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[DPY19L1]] | -0.54 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[EPS15]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[RPS18]] | -0.53 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[CPSF6]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[ATP5F1C]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[FAR1]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[RPA1]] | -0.52 | -0.46 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CCDC97's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CCDC97's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.0, -18.1); signed map (10.7, 13.5). **Vector** length 83.1, 15.7% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.6 | +11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +6.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.5 | -3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.6 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.0 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 97 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,310,172-41,324,873 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40267, MGC20255 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F63](https://www.uniprot.org/uniprotkb/Q96F63) (Coiled-coil domain-containing protein 97):

> May play a role pre-mRNA splicing through the association with the splicing factor SF3B complex which is involved in branch-site recognition.

**Summary**, from NCBI Gene [90324](https://www.ncbi.nlm.nih.gov/gene/90324):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28289) · Entrez [90324](https://www.ncbi.nlm.nih.gov/gene/90324) · UniProt [Q96F63](https://www.uniprot.org/uniprotkb/Q96F63) · Ensembl [ENSG00000142039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142039)

## Data

Gene col 6591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6591); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6591]; `tensor/DDL_lfc|DDL_z.npy` [6591]; `embed/gene_vectors.npy` [6591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6591 or target_col == 6591). Every well: [[CCDC97 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC97.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
