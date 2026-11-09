---
symbol: "PIGL"
type: "gene"
col: 2953
ensembl_id: "ENSG00000108474"
name: "phosphatidylinositol glycan anchor biosynthesis class L"
location: "17p11.2"
module: 1
arm: "+"
pooled_cpm: 44.01
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PIGL

*phosphatidylinositol glycan anchor biosynthesis class L* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.31× (z +6.2, q 2e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.663× (z -6.2, q 4e-07, down in 29 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.505× (z -5.8, q 2e-06, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JPX]] (+0.73, fdr 7e-06), [[ST7L]] (+0.64, fdr 7e-06), [[METTL2B]] (+0.64, fdr 7e-06); moves opposite to [[PCOLCE]] (-0.64, fdr 1e-05), [[MANBA]] (-0.60, fdr 1e-05), [[MOSPD3]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FRMPD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2953.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.2 | 2e-07 | 29/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 2e-07 | 31/47 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.3 | 2e-05 | 24/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +5.0 | 9e-05 | 18/40 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.5 | 6e-04 | 24/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.5 | 6e-04 | 24/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +4.4 | 1e-03 | 24/48 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.3 | 0.001 | 26/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.005 | 20/48 (NCI-H23, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.060 | 11/48 (A-172, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -6.2 | 4e-07 | 29/47 (SHP-77, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -5.8 | 2e-06 | 32/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -5.3 | 2e-05 | 31/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -4.5 | 8e-04 | 23/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.800×** | -3.6 | 0.037 | 19/48 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.807×** | -3.5 | 0.051 | 19/47 (HCT15, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | **0.817×** | -3.3 | 0.082 | 12/48 (C-33 A, HS-578T, …) | inconsistent across doses |  |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.818×** | -3.2 | 0.082 | 18/48 (C-33 A, NCI-H661, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.869× | -3.2 | 0.085 | 6/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.690×** | -3.1 | 0.097 | 16/42 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.825×** | -3.1 | 0.097 | 11/48 (PANC-1, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 76.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +18.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 31.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 54.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 59.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.6) |
| [[SW480 (line)]] | alt | 73.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.03× (z +8.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.0) |
| [[A498 (line)]] | wt | 78.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -9.5) |
| [[C-33 A (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -8.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[KATO III (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.452× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.316× (z -9.2) ⚠ toxic |
| [[A-172 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPX]] | +0.73 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[ST7L]] | +0.64 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[METTL2B]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ANAPC7]] | +0.62 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[GNL3L]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ITPA]] | +0.61 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.61 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SLC16A1-AS1]] | +0.61 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[DPH5-DT]] | +0.60 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[DNAJC11]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[ATXN10]] | +0.60 | +0.61 / +0.49 | both halves | 1e-05 | same gene group |
| [[GPATCH4]] | +0.60 | +0.63 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCOLCE]] | -0.64 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[MANBA]] | -0.60 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[MOSPD3]] | -0.59 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[APAF1]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[POGLUT2]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[ABHD17B]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MXI1]] | -0.55 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[EFNA4]] | -0.55 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[HERC3]] | -0.55 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[IDH2]] | -0.55 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[SCPEP1]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PAPSS1]] | -0.54 | -0.67 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMPD3]] | B | FRMPD3 activity lowers PIGL's level | lines that do not express FRMPD3 (18) vs lines expressing it (32) | 1.42× higher at baseline in the lines without FRMPD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: CACNG4, NSUN7, GYG2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (6.3, -22.7); signed map (4.1, -45.4). **Vector** length 104, 25.0% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +3.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +0.8 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Dihydroartemisinin (drug)]] 0.05 µM |  | +2.1 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | -3.2 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:16,217,191-16,351,797 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIG-L |
| Gene groups (HGNC) | Phosphatidylinositol glycan anchor biosynthesis; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2B2](https://www.uniprot.org/uniprotkb/Q9Y2B2) (N-acetylglucosaminyl-phosphatidylinositol de-N-acetylase):

> Catalyzes the second step of glycosylphosphatidylinositol (GPI) biosynthesis, which is the de-N-acetylation of N-acetylglucosaminyl-phosphatidylinositol.

**Summary**, from NCBI Gene [9487](https://www.ncbi.nlm.nih.gov/gene/9487):

> This gene encodes an enzyme that catalyzes the second step of glycosylphosphatidylinositol (GPI) biosynthesis, which is the de-N-acetylation of N-acetylglucosaminylphosphatidylinositol (GlcNAc-PI). Study of a similar rat enzyme suggests that this protein localizes to the endoplasmic reticulum. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8966](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8966) · Entrez [9487](https://www.ncbi.nlm.nih.gov/gene/9487) · UniProt [Q9Y2B2](https://www.uniprot.org/uniprotkb/Q9Y2B2) · Ensembl [ENSG00000108474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108474)

## Data

Gene col 2953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2953); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2953]; `tensor/DDL_lfc|DDL_z.npy` [2953]; `embed/gene_vectors.npy` [2953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2953 or target_col == 2953). Every well: [[PIGL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
