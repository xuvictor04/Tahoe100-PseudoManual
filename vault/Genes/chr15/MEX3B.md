---
symbol: "MEX3B"
type: "gene"
col: 11410
ensembl_id: "ENSG00000183496"
name: "mex-3 RNA binding family member B"
location: "15q25.2"
module: 59
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 46
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# MEX3B

*mex-3 RNA binding family member B* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.69× (z +15.3, q 0e+00, up in 22 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.707× (z -3.8, q 0.081, down in 18 of 29 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.127×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0489×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.178×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCORL1]] (+0.56, fdr 1e-05), [[CITED2]] (+0.56, fdr 2e-05), [[TENT5C]] (+0.54, fdr 1e-05); moves opposite to [[TIMM23B]] (-0.56, fdr 1e-05), [[TYW1]] (-0.55, fdr 4e-05), [[TIMM23B-AGAP6]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OVOL1]] → it (grade B ⚠); 3 go from it, the strongest it → [[DLX2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +15.3 | 0e+00 | 22/35 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +8.3 | 4e-14 | 20/43 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +7.4 | 2e-11 | 20/42 (SW1417, LoVo, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.2 | 1e-10 | 14/31 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.8 | 9e-10 | 1/5 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +6.5 | 9e-09 | 21/42 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +6.4 | 1e-08 | 15/36 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +6.1 | 1e-07 | 13/32 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +6.0 | 2e-07 | 6/41 (J82, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.7 | 8e-07 | 9/19 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +5.4 | 3e-06 | 19/43 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.2 | 8e-06 | 10/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +5.0 | 3e-05 | 15/42 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.8 | 6e-05 | 2/22 (PANC-1, SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.7 | 9e-05 | 8/24 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 9/31 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.003 | 14/43 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.92×** | +3.7 | 0.006 | 0/28 | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.015 | 5/32 (HT-29, BT-474, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11410.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.127×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0489×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.178×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.707×** | -3.8 | 0.081 | 18/29 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.737× | -3.3 | 0.19 | 10/43 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | 0.746× | -3.2 | 0.19 | 8/34 (C32, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -3.2 | 0.19 | 11/44 (LoVo, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 49.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -12.1) |
| [[J82 (line)]] | alt | 10.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 5.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 9.18 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.102× (z -8.5) |
| [[SHP-77 (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0998× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.292 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCORL1]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CITED2]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TENT5C]] | +0.54 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CACNA2D2]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TP53INP2]] | +0.54 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[BMF]] | +0.52 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[VASN]] | +0.52 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MYLIP]] | +0.51 | +0.46 / +0.60 | both halves | 2e-05 | same gene group |
| [[BCL2L11]] | +0.51 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[RAB33B]] | +0.51 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[TBC1D9]] | +0.51 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[DLX2]] | +0.51 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TYW1]] | -0.55 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TIMM23B-AGAP6]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ATR]] | -0.53 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[AAGAB]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[LARS2]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[NOL10]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ERCC8]] | -0.50 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[MEF2B]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[IPO11]] | -0.49 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[STX16-NPEPL1]] | -0.48 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[PIK3R4]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OVOL1]] | B | OVOL1 activity lowers MEX3B's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.10× higher at baseline in the lines without OVOL1 | 0.083 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX2]] | C | MEX3B activity raises DLX2's level | lines that do not express MEX3B (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without MEX3B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIF17, DPF1, CNTNAP1; its own permutation p |
| [[BCOR]] | C | MEX3B activity raises BCOR's level | lines that do not express MEX3B (4) vs lines expressing it (46) | 1.69× lower at baseline in the lines without MEX3B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIF17, DPF1, CNTNAP1; its own permutation p |
| [[BCORL1]] | C | MEX3B activity raises BCORL1's level | lines that do not express MEX3B (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without MEX3B | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIF17, DPF1, CNTNAP1; its own permutation p |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (29.9, -30.9); signed map (-0.5, 16.3). **Vector** length 55.1, 7.29% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +15.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +7.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.4 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mex-3 RNA binding family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,041,778-82,046,119 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434J0617, RNF195; previously RKHD3 |
| Gene groups (HGNC) | Ring finger proteins; Mex-3 RNA binding family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN04](https://www.uniprot.org/uniprotkb/Q6ZN04) (RNA-binding protein MEX3B):

> RNA-binding protein. May be involved in post-transcriptional regulatory mechanisms.

**Summary**, from NCBI Gene [84206](https://www.ncbi.nlm.nih.gov/gene/84206):

> This gene encodes an RNA-binding phosphoprotein that is part of the MEX3 (muscle excess 3) family of translational regulators. The encoded protein contains N-terminal nuclear export and nuclear localization signals and is exported from the cytoplasm to the nucleus. The protein binds to RNA via two KH domains and also colocalizes with MEX3A, Dcp1A decapping factor and Argonaute proteins within P (processing) bodies. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:25297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25297) · Entrez [84206](https://www.ncbi.nlm.nih.gov/gene/84206) · UniProt [Q6ZN04](https://www.uniprot.org/uniprotkb/Q6ZN04) · Ensembl [ENSG00000183496](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183496)

## Data

Gene col 11410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11410); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11410]; `tensor/DDL_lfc|DDL_z.npy` [11410]; `embed/gene_vectors.npy` [11410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11410 or target_col == 11410). Every well: [[MEX3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEX3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
