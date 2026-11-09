---
symbol: "TMEM101"
type: "gene"
col: 1680
ensembl_id: "ENSG00000091947"
name: "transmembrane protein 101"
location: "17q21.31"
module: 111
arm: "+"
pooled_cpm: 14.18
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# TMEM101

*transmembrane protein 101* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.39× (z +4.4, q 0.007, up in 17 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.52× (z +4.2, q 0.008, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.581× (z -7.5, q 3e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL32]] (+0.73, fdr 7e-06), [[NGDN]] (+0.68, fdr 1e-05), [[SMIM26]] (+0.66, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[NKAP]] (+0.66, fdr 1e-05); moves opposite to [[CDC42]] (-0.70, fdr 1e-05), [[YWHAZ]] (-0.65, fdr 1e-05), [[CORO1C]] (-0.65, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RNF135]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.4 | 0.007 | 17/43 (SW480, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.008 | 18/46 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.9 | 0.016 | 18/46 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.6 | 0.046 | 1/48 (BT-474) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.099 | 9/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.26× | +3.3 | 0.10 | 11/44 (LS 180, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.17 | 6/48 (LoVo, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.581×** | -7.5 | 3e-11 | 35/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.708×** | -6.8 | 4e-09 | 32/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -6.7 | 5e-09 | 35/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -6.6 | 7e-09 | 26/44 (LOX-IMVI, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.631×** | -6.4 | 2e-08 | 25/47 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.673×** | -5.5 | 4e-06 | 23/47 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.503×** | -5.0 | 5e-05 | 17/48 (SNU-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.702×** | -4.9 | 7e-05 | 22/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.530×** | -4.6 | 3e-04 | 20/48 (A-427, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.730×** | -4.4 | 8e-04 | 19/39 (RPMI-7951, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.679×** | -4.3 | 0.001 | 15/33 (KATO III, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.742×** | -4.0 | 0.003 | 12/26 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -3.8 | 0.006 | 16/40 (NCI-H460, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.038 | 18/46 (SHP-77, SW48, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.803×** | -3.0 | 0.093 | 8/47 (LS 180, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0751× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 8.54 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -9.0) |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -12.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -10.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -15.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL32]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[NGDN]] | +0.68 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.66 | +0.58 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[NKAP]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.65 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.65 | +0.46 / +0.75 | both halves | 2e-05 |  |
| [[NOXRED1]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[COG7]] | +0.64 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[ZRSR2]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[WDR83OS]] ⚠ | +0.64 | +0.57 / +0.67 | both halves | 9e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PCGF1]] ⚠ | +0.63 | +0.47 / +0.73 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KBTBD4]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[NDUFS3]] | +0.63 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[COA6]] | +0.63 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[C16orf91]] | +0.62 | +0.41 / +0.72 | both halves | 4e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42]] | -0.70 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.65 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[MYH9]] | -0.64 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.63 | -0.46 / -0.70 | both halves | 3e-05 |  |
| [[GNG12]] | -0.63 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[ACTR3]] | -0.63 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.59 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[EPB41L2]] | -0.59 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CHML]] | -0.58 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[ARL6IP6]] | -0.58 | -0.37 / -0.55 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF135]] | B | RNF135 activity lowers TMEM101's level | lines that do not express RNF135 (6) vs lines expressing it (44) | 1.03× higher at baseline in the lines without RNF135 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000291063, TMEM54, ENSG00000266865; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction -0.704). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.9, -18.1); signed map (-6.2, -5.1). **Vector** length 72.4, 13.6% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.7 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -6.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 101 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,011,188-44,023,946 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4251, FLJ23987 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IK0](https://www.uniprot.org/uniprotkb/Q96IK0) (Transmembrane protein 101):

> May activate NF-kappa-B signaling pathways.

**Summary**, from NCBI Gene [84336](https://www.ncbi.nlm.nih.gov/gene/84336):

> Involved in positive regulation of canonical NF-kappaB signal transduction. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28653](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28653) · Entrez [84336](https://www.ncbi.nlm.nih.gov/gene/84336) · UniProt [Q96IK0](https://www.uniprot.org/uniprotkb/Q96IK0) · Ensembl [ENSG00000091947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091947)

## Data

Gene col 1680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1680); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1680]; `tensor/DDL_lfc|DDL_z.npy` [1680]; `embed/gene_vectors.npy` [1680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1680 or target_col == 1680). Every well: [[TMEM101 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM101.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
