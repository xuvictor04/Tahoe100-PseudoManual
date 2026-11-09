---
symbol: "MICA"
type: "gene"
col: 12882
ensembl_id: "ENSG00000204520"
name: "MHC class I polypeptide-related sequence A"
location: "6p21.33"
module: 1
arm: "-"
pooled_cpm: 27.49
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 15
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MICA

*MHC class I polypeptide-related sequence A* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.92× (z +16.4, q 0e+00, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.654× (z -7.6, q 2e-11, down in 23 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.704× (z -5.5, q 5e-06, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNASE2]] (+0.60, fdr 1e-05), [[SCPEP1]] (+0.60, fdr 1e-05), [[RUSC1]] (+0.59, fdr 1e-05); moves opposite to [[JPX]] (-0.66, fdr 1e-05), [[DDX10]] (-0.61, fdr 9e-06), [[GNL3L]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HLA-F-AS1]] → it (grade B ⚠); 15 go from it, the strongest it → cells under [[Glycyrrhizic acid (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12882.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +16.4 | 0e+00 | 40/45 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +10.6 | 6e-24 | 30/45 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +10.0 | 3e-21 | 33/45 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +8.8 | 2e-16 | 32/45 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.0 | 3e-07 | 27/45 (SW480, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.8 | 6e-07 | 20/44 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +5.7 | 1e-06 | 21/45 (RKO, J82, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.5 | 3e-06 | 24/45 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.24×** | +5.3 | 8e-06 | 21/45 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 3e-05 | 21/45 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.21×** | +4.7 | 2e-04 | 17/45 (AsPC-1, SNU-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.5 | 3e-04 | 18/43 (LS 180, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Berbamine (drug)]] 5 µM |  | 1.20× | +4.5 | 4e-04 | 14/45 (NCI-H2030, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.4 | 5e-04 | 22/45 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.23×** | +4.3 | 7e-04 | 19/45 (AsPC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.27×** | +4.2 | 0.001 | 16/45 (AsPC-1, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12882.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.654×** | -7.6 | 2e-11 | 23/42 (A-172, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.691×** | -5.8 | 2e-06 | 21/34 (MIA PaCa-2, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.709×** | -5.7 | 3e-06 | 19/38 (H4, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.704×** | -5.5 | 5e-06 | 23/45 (NCI-H2347, SW 1271, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.783×** | -4.4 | 0.001 | 22/45 (hTERT-HPNE, J82, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.866× | -3.6 | 0.026 | 14/45 (KATO III, SW 1088, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | 0.871× | -3.5 | 0.038 | 12/45 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.826×** | -3.4 | 0.042 | 11/45 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.827×** | -3.4 | 0.042 | 14/45 (Hs 766T, C32, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.879× | -3.3 | 0.062 | 14/45 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.840× | -3.1 | 0.095 | 9/45 (LoVo, Panc 03.27, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12882. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 55.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -16.7) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 44.7 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -11.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 47.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -11.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.58× (z +10.6) ⚠ position not correctable | [[Dinaciclib (drug)]] 5 µM 0.0691× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 31.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 22.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +8.8) | — |
| [[SW480 (line)]] | alt | 14.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 28.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.5) | — |
| [[C32 (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +9.9) | — |
| [[H4 (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -9.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0886× (z -12.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -10.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 47.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 34.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 22.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 23.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 37.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -12.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12882), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNASE2]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SCPEP1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[RUSC1]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[IL17RC]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[CPEB3]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MICB]] | +0.58 | +0.41 / +0.64 | both halves | 4e-05 | same gene group; pathway: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; STRING 918 |
| [[RHEBL1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[MGST3]] | +0.57 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[HSD17B7P2]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[RABAC1]] | +0.56 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[LAPTM4A]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JPX]] | -0.66 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[DDX10]] | -0.61 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[GNL3L]] | -0.60 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[NOP14]] | -0.59 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[RGS5]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[ZBTB38]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[MPHOSPH6]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SMARCA4]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[DOCK1]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[COMMD10]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[ABCE1]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F-AS1]] | B | HLA-F-AS1 activity raises MICA's level | lines that do not express HLA-F-AS1 (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without HLA-F-AS1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LRP1, STRIP2, SH2D4B; maybe low, not absent |
| [[MICB]] | B | MICB activity raises MICA's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without MICB | 0.095 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Glycyrrhizic acid (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Glycyrrhizic acid 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.50× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.45× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.48× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.42× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[IQ 1 (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.69× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.66× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.75× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Lidocaine (hydrochloride) (drug)]] 0.05 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.64× the cells of the other lines | 0.053 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Tolcapone (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Naproxen (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.77× the cells of the other lines | 0.066 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.22× the cells of the other lines | 0.070 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| cells under [[Salicylic acid (drug)]] 5 µM | C | [[ENSG00000288587]], [[KDELR3]], MICA, [[POLD4]], [[PPP1R14B-AS1]] activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.21× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-1.8, -37.9); signed map (-40.6, 12.7). **Vector** length 99.1, 22.7% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +16.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | MHC class I polypeptide-related sequence A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,399,784-31,415,315 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PERB11.1 |
| Gene groups (HGNC) | C1-set domain containing; MIC family |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q29983](https://www.uniprot.org/uniprotkb/Q29983) (MHC class I polypeptide-related sequence A):

> Widely expressed membrane-bound protein which acts as a ligand to stimulate an activating receptor KLRK1/NKG2D, expressed on the surface of essentially all human natural killer (NK), gammadelta T and CD8 alphabeta T-cells. Up-regulated in stressed conditions, such as viral and bacterial infections or DNA damage response, serves as signal of cellular stress, and engagement of KLRK1/NKG2D by MICA triggers NK-cells resulting in a range of immune effector functions, such as cytotoxicity and …

**Summary**, from NCBI Gene [100507436](https://www.ncbi.nlm.nih.gov/gene/100507436):

> This gene encodes the highly polymorphic major histocompatability complex class I chain-related protein A. The protein product is expressed on the cell surface, although unlike canonical class I molecules it does not seem to associate with beta-2-microglobulin. It is a ligand for the NKG2-D type II integral membrane protein receptor. The protein functions as a stress-induced antigen that is broadly recognized by intestinal epithelial gamma delta T cells. Variations in this gene have been …

**Accessions** — [HGNC:7090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7090) · Entrez [100507436](https://www.ncbi.nlm.nih.gov/gene/100507436) · UniProt [Q29983](https://www.uniprot.org/uniprotkb/Q29983) · Ensembl [ENSG00000204520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204520)

## Data

Gene col 12882: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12882); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12882, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12882]; `tensor/DDL_lfc|DDL_z.npy` [12882]; `embed/gene_vectors.npy` [12882]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12882 or target_col == 12882). Every well: [[MICA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
