---
symbol: "XIST"
type: "gene"
col: 13715
ensembl_id: "ENSG00000229807"
name: "X inactive specific transcript"
location: "Xq13.2"
module: 31
arm: "+"
pooled_cpm: 42.31
n_lines_expressing: 7
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# XIST

*X inactive specific transcript* — Xq13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.31× (z +12.0, q 2e-30, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Docetaxel (Trihydrate) (drug)]] 0.5 µM: 1.84× (z +5.0, q 9e-05, up in 0 of 5 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.847× (z -4.9, q 5e-04, down in 1 of 6 measured lines) ⚠ position not correctable. The strongest without an alert is [[Artesunate (drug)]] 0.5 µM: 0.637× (z -3.7, q 0.052, down in 0 of 5 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO5B]] (+0.55, fdr 3e-05), [[CYP4F11]] (+0.51, fdr 4e-05), [[ADGRF4]] (+0.51, fdr 3e-05); moves opposite to [[C8orf58]] (-0.42, fdr 3e-04), [[DOP1A]] (-0.38, fdr 3e-04), [[LINC01118]] (-0.38, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[OR51B5]] → it (grade B ⚠); 8 go from it, the strongest it → [[B4GALNT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.31×** | +12.0 | 2e-30 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.10×** | +11.1 | 3e-26 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +8.4 | 1e-14 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.84×** | +5.0 | 9e-05 | 0/5 | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +4.8 | 1e-04 | 0/5 | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.28×** | +4.8 | 1e-04 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.7 | 2e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.4 | 9e-04 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +3.9 | 0.005 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.94×** | +3.9 | 0.006 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.54×** | +3.5 | 0.023 | 0/5 | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.5 | 0.026 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.029 | 1/5 (SW48) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.74×** | +3.2 | 0.052 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.47×** | +3.1 | 0.064 | 0/5 | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +3.1 | 0.069 | 3/5 (A498, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.070 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.080 | 3/5 (HT-29, A498, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.67×** | +3.0 | 0.087 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.098 | 0/5 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.847× | -4.9 | 5e-04 | 1/6 (NCI-H2122) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.637×** | -3.7 | 0.052 | 0/5 | inconsistent across doses | position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.626×** | -3.6 | 0.064 | 0/5 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.647× | -3.3 | 0.12 | 0/5 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 306 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 628 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO5B]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CYP4F11]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[ADGRF4]] | +0.51 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[DAPP1]] | +0.51 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[HKDC1]] | +0.49 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[GALNT3]] | +0.45 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[KCNK1]] | +0.44 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[PREX2]] | +0.44 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[SEL1L3]] | +0.44 | +0.43 / +0.37 | both halves | 8e-05 |  |
| [[SLC10A7]] | +0.43 | +0.42 / +0.22 | both halves | 6e-04 |  |
| [[TACSTD2]] | +0.43 | +0.44 / +0.31 | both halves | 2e-04 |  |
| [[SH3RF2]] | +0.43 | +0.39 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C8orf58]] | -0.42 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[DOP1A]] | -0.38 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[LINC01118]] | -0.38 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[SOCS5]] | -0.37 | -0.27 / -0.28 | both halves | 3e-04 |  |
| [[MFSD4B]] | -0.36 | -0.45 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[WASHC3]] | -0.35 | -0.44 / -0.22 | both halves | 6e-04 |  |
| [[SPACA9]] | -0.35 | -0.34 / -0.26 | both halves | 3e-04 |  |
| [[CEP85L]] | -0.35 | -0.38 / -0.21 | both halves | 6e-04 |  |
| [[SIRT3]] | -0.35 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[DRC3]] | -0.34 | -0.28 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OR51B5]] | B | OR51B5 activity lowers XIST's level | lines that do not express OR51B5 (16) vs lines expressing it (34) | 2.25× higher at baseline in the lines without OR51B5 | 0.094 | ⚠ within organs, on part of the lines; also absent: HBG2, ENSG00000287231, EPS8L1; maybe low, not absent |
| [[SFTPA2]] | C | SFTPA2 activity raises XIST's level | lines that do not express SFTPA2 (46) vs lines expressing it (4) | 8.50× lower at baseline in the lines without SFTPA2 | 0.083 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT1]] | B | XIST activity lowers B4GALNT1's level | lines that do not express XIST (43) vs lines expressing it (7) | 1.74× higher at baseline in the lines without XIST | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20 |
| [[SAMD12]] | B | XIST activity raises SAMD12's level | lines that do not express XIST (43) vs lines expressing it (7) | 3.05× lower at baseline in the lines without XIST | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20 |
| [[PLEKHA6]] | B | XIST activity raises PLEKHA6's level | lines that do not express XIST (43) vs lines expressing it (7) | 3.06× lower at baseline in the lines without XIST | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20 |
| [[SFTPA2]] | C | XIST activity raises SFTPA2's level | lines that do not express XIST (43) vs lines expressing it (7) | 2.25× lower at baseline in the lines without XIST | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20; co-absent with the target |
| [[RNF39]] | C | XIST activity raises RNF39's level | lines that do not express XIST (43) vs lines expressing it (7) | 1.96× lower at baseline in the lines without XIST | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20; co-absent with the target |
| [[MUC4]] | C | XIST activity raises MUC4's level | lines that do not express XIST (43) vs lines expressing it (7) | 1.41× lower at baseline in the lines without XIST | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20; co-absent with the target |
| [[DAPP1]] | C | XIST activity raises DAPP1's level | lines that do not express XIST (43) vs lines expressing it (7) | 3.25× lower at baseline in the lines without XIST | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20; co-absent with the target |
| [[MMP7]] | C | XIST activity raises MMP7's level | lines that do not express XIST (43) vs lines expressing it (7) | 3.24× lower at baseline in the lines without XIST | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.268). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.1, 59.0); signed map (55.2, 6.8). **Vector** length 15.2, 4.46% of its response variance represented; |z| ≥ 3 in 111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.8 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.7 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +0.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.5 | +1.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.4 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.4 | +0.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.6 | -0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.4 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.3 | -0.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.3 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | X inactive specific transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq13.2 — chrX:73,820,649-73,852,723 (-) |
| Ensembl biotype | lncRNA |
| Also known as | NCRNA00001, DXS1089, swd66, LINC00001; previously DXS399E |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [7503](https://www.ncbi.nlm.nih.gov/gene/7503):

> X inactivation is an early developmental process in mammalian females that transcriptionally silences one of the pair of X chromosomes, thus providing dosage equivalence between males and females. The process is regulated by several factors, including a region of chromosome X called the X inactivation center (XIC). The XIC comprises several non-coding and protein-coding genes, and this gene was the first non-coding gene identified within the XIC. This gene is expressed exclusively from the XIC …

**Accessions** — [HGNC:12810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12810) · Entrez [7503](https://www.ncbi.nlm.nih.gov/gene/7503) · Ensembl [ENSG00000229807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229807)

## Data

Gene col 13715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13715); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13715]; `tensor/DDL_lfc|DDL_z.npy` [13715]; `embed/gene_vectors.npy` [13715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13715 or target_col == 13715). Every well: [[XIST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XIST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
