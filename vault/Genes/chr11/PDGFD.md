---
symbol: "PDGFD"
type: "gene"
col: 10036
ensembl_id: "ENSG00000170962"
name: "platelet derived growth factor D"
location: "11q22.3"
module: 9
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 28
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PDGFD

*platelet derived growth factor D* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 6.14× (z +20.7, q 0e+00, up in 22 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.675× (z -4.5, q 0.004, down in 10 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (A-172 0.0662×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.254×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUCY1B1]] (+0.66, fdr 7e-06), [[TMEM108]] (+0.65, fdr 9e-06), [[KHDRBS2]] (+0.64, fdr 9e-06); moves opposite to [[DZANK1]] (-0.49, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPP1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[GPM6A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10036.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **6.14×** | +20.7 | 0e+00 | 22/22 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.85×** | +13.7 | 2e-40 | 3/5 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.13×** | +13.0 | 2e-36 | 8/19 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.35×** | +11.9 | 2e-30 | 19/20 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.23×** | +11.7 | 3e-29 | 22/23 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.97×** | +11.1 | 9e-27 | 7/15 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.38×** | +9.8 | 6e-21 | 22/24 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.33×** | +9.7 | 2e-20 | 19/22 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.04×** | +9.0 | 2e-17 | 18/22 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +8.1 | 4e-14 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.03×** | +8.1 | 4e-14 | 10/22 (NCI-H2347, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +6.4 | 8e-09 | 9/18 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **2.04×** | +5.5 | 1e-06 | 6/11 (A498, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.98×** | +5.5 | 1e-06 | 3/20 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.92×** | +5.0 | 2e-05 | 9/19 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.72×** | +4.2 | 7e-04 | 12/20 (NCI-H2347, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +4.1 | 0.001 | 5/17 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 7/23 (A-172, J82, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.002 | 8/21 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10036.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (A-172 0.0662×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.254×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.675×** | -4.5 | 0.004 | 10/23 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.877× | -3.8 | 0.035 | 7/25 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.601×** | -3.7 | 0.035 | 0/24 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.683× | -3.1 | 0.25 | 4/18 (SHP-77, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.671× | -3.1 | 0.25 | 0/21 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10036. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 4.86 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 12.9× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 2.76 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 8.68× (z +9.6) | [[Penfluridol (drug)]] 0.5 µM 0.0565× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 8.75 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 8.04× (z +13.8) | — |
| [[A-172 (line)]] | wt | 5.25 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0662× (z -9.5) |
| [[BT-474 (line)]] | alt | 7.19 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0685× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[J82 (line)]] | alt | 2.71 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.68× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.07× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 3.71 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.1× (z +9.5) | — |
| [[A-427 (line)]] | wt | 0.940 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.797 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.412 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.434 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.429 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10036), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUCY1B1]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[TMEM108]] | +0.65 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[KHDRBS2]] | +0.64 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[ANOS1]] | +0.64 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[VAV3]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GRIA2]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TEX15]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ESRRG]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[ASXL3]] | +0.61 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[MMP16]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[GABRA2]] | +0.60 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[KCNH7]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | -0.49 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPP1]] | C | SPP1 activity raises PDGFD's level | lines that do not express SPP1 (35) vs lines expressing it (15) | 2.18× lower at baseline in the lines without SPP1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01320, MAGEB2, FGG; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPM6A]] | B | PDGFD activity raises GPM6A's level | lines that do not express PDGFD (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without PDGFD | 0.093 | ⚠ within organs, on part of the lines; also absent: LRRC63, ZFHX4, FGF14; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.6, 35.8); signed map (38.7, 34.2). **Vector** length 50.3, 11.3% of its response variance represented; |z| ≥ 3 in 611 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +20.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +11.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | platelet derived growth factor D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:103,907,189-104,164,379 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCDGF-B, MSTP036, IEGF |
| Gene groups (HGNC) | PDGF family ligands |
| Reactome | 2 pathways, smallest: Signaling by PDGF; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZP0](https://www.uniprot.org/uniprotkb/Q9GZP0) (Platelet-derived growth factor D):

> Growth factor that plays an essential role in the regulation of embryonic development, cell proliferation, cell migration, survival and chemotaxis. Potent mitogen for cells of mesenchymal origin. Plays an important role in wound healing. Induces macrophage recruitment, increased interstitial pressure, and blood vessel maturation during angiogenesis. Can initiate events that lead to a mesangial proliferative glomerulonephritis, including influx of monocytes and macrophages and production of …

**Summary**, from NCBI Gene [80310](https://www.ncbi.nlm.nih.gov/gene/80310):

> The protein encoded by this gene is a member of the platelet-derived growth factor family. The four members of this family are mitogenic factors for cells of mesenchymal origin and are characterized by a core motif of eight cysteines, seven of which are found in this factor. This gene product only forms homodimers and, therefore, does not dimerize with the other three family members. It differs from alpha and beta members of this family in having an unusual N-terminal domain, the CUB domain. …

**Accessions** — [HGNC:30620](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30620) · Entrez [80310](https://www.ncbi.nlm.nih.gov/gene/80310) · UniProt [Q9GZP0](https://www.uniprot.org/uniprotkb/Q9GZP0) · Ensembl [ENSG00000170962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170962)

## Data

Gene col 10036: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10036); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10036, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10036]; `tensor/DDL_lfc|DDL_z.npy` [10036]; `embed/gene_vectors.npy` [10036]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10036 or target_col == 10036). Every well: [[PDGFD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDGFD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
