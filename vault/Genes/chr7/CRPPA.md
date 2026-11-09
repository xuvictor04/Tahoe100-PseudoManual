---
symbol: "CRPPA"
type: "gene"
col: 13236
ensembl_id: "ENSG00000214960"
name: "CDP-L-ribitol pyrophosphorylase A"
location: "7p21.2"
module: 124
arm: "+"
pooled_cpm: 12.45
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# CRPPA

*CDP-L-ribitol pyrophosphorylase A* — 7p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +14.9, q 0e+00, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.367× (z -12.2, q 1e-31, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AVEN]] (+0.77, fdr 7e-06), [[EFCAB2]] (+0.77, fdr 1e-05), [[ARSB]] (+0.76, fdr 1e-05); moves opposite to [[SLC27A1]] (-0.71, fdr 1e-04), [[MAST3]] (-0.69, fdr 3e-05), [[YIF1B]] (-0.68, fdr 5e-05).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[SIAH2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +14.9 | 0e+00 | 33/39 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.9 | 1e-12 | 28/43 (LoVo, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +7.5 | 8e-12 | 16/22 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.9 | 6e-10 | 27/38 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.4 | 2e-08 | 20/40 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.7 | 9e-07 | 19/32 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +5.4 | 5e-06 | 21/41 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.2 | 2e-05 | 12/27 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +4.8 | 1e-04 | 19/40 (PANC-1, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.003 | 17/41 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.003 | 11/41 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.009 | 12/43 (HT-29, SW 900, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.24×** | +3.7 | 0.009 | 18/43 (LoVo, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Demeclocycline (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.062 | 8/43 (CFPAC-1, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.367×** | -12.2 | 1e-31 | 31/43 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.373×** | -12.0 | 6e-31 | 37/42 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.430×** | -10.3 | 1e-22 | 36/43 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.505×** | -8.4 | 9e-15 | 33/43 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.649×** | -7.5 | 9e-12 | 24/41 (NCI-H1792, HOP62, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.547×** | -7.4 | 1e-11 | 27/38 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.596×** | -6.1 | 9e-08 | 20/41 (SNU-1, NCI-H1792, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.402×** | -5.8 | 4e-07 | 21/42 (LS 180, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -4.1 | 0.002 | 15/42 (SNU-1, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.731×** | -3.8 | 0.007 | 14/42 (HOP62, SHP-77, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.553×** | -3.8 | 0.007 | 12/39 (SW480, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -3.8 | 0.007 | 15/42 (LoVo, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -3.7 | 0.010 | 16/42 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.748×** | -3.6 | 0.015 | 15/40 (SK-MEL-2, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.753×** | -3.5 | 0.019 | 11/43 (HOP62, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.756×** | -3.4 | 0.022 | 10/42 (SNU-423, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.024 | 15/42 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 19.7 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +11.9) | [[Digitoxin (drug)]] 5 µM 0.115× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.234× (z -8.5) |
| [[SNU-1 (line)]] | wt | 249 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.234× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -14.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.164× (z -10.6) |
| [[SW480 (line)]] | alt | 14.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 9.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -12.0) ⚠ cell-cycle shift, explains ~60% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.75 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0685× (z -8.5) |
| [[LoVo (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 6.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0885× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[NCI-H460 (line)]] | wt | 7.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +10.2) | — |
| [[A-172 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | +0.77 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[EFCAB2]] | +0.77 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ARSB]] | +0.76 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.75 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SLC25A21]] | +0.75 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ADCK1]] | +0.74 | +0.66 / +0.31 | both halves | 2e-04 |  |
| [[PBLD]] | +0.74 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[EPM2A]] | +0.73 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[EIF4G2]] | +0.72 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SPRY3]] | +0.72 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[MYLK4]] | +0.71 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.55 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.71 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[MAST3]] | -0.69 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[YIF1B]] | -0.68 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[RNF41]] | -0.68 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TTC38]] | -0.68 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[ETHE1]] | -0.68 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[PIGH]] | -0.67 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[KLHL26]] | -0.67 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[RRAS]] | -0.67 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[FCHO1]] | -0.65 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[RAB3A]] | -0.65 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[TMEM256]] | -0.65 | -0.47 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CRPPA's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIAH2-AS1]] | B | CRPPA activity lowers SIAH2-AS1's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.66× higher at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[SLC39A10]] | B | CRPPA activity raises SLC39A10's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.62× lower at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[RASSF1]] | B | CRPPA activity raises RASSF1's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[TMEM202-AS1]] | B | CRPPA activity lowers TMEM202-AS1's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.46× higher at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[METTL26]] | B | CRPPA activity raises METTL26's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[LINC00571]] | B | CRPPA activity lowers LINC00571's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 2.92× higher at baseline in the lines without CRPPA | 0.068 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent |
| [[GAS2]] | B | CRPPA activity lowers GAS2's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 2.34× higher at baseline in the lines without CRPPA | 0.089 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[TULP4]] | B | CRPPA activity raises TULP4's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without CRPPA | 0.098 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.804). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.9, 8.6); signed map (23.7, -28.7). **Vector** length 90.0, 19.2% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.8 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +4.0 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -12.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.6 | -10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -5.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | CDP-L-ribitol pyrophosphorylase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.2 — chr7:16,087,525-16,502,504 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hCG_1745121, IspD, Nip; previously ISPD |
| Reactome | 3 pathways, smallest: Matriglycan biosynthesis on DAG1; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [A4D126](https://www.uniprot.org/uniprotkb/A4D126) (D-ribitol-5-phosphate cytidylyltransferase):

> Cytidylyltransferase required for protein O-linked mannosylation. Catalyzes the formation of CDP-ribitol nucleotide sugar from D-ribitol 5-phosphate. CDP-ribitol is a substrate of FKTN during the biosynthesis of the phosphorylated O-mannosyl trisaccharide (N-acetylgalactosamine-beta-3-N-acetylglucosamine-beta-4-(phosphate-6-)mannose), a carbohydrate structure present in alpha-dystroglycan (DAG1), which is required for binding laminin G-like domain-containing extracellular proteins with high …

**Summary**, from NCBI Gene [729920](https://www.ncbi.nlm.nih.gov/gene/729920):

> This gene encodes a 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase-like protein. Mutations in this gene are the cause of Walker-Warburg syndrome. Alternate splicing results in multiple transcript variants. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:37276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37276) · Entrez [729920](https://www.ncbi.nlm.nih.gov/gene/729920) · UniProt [A4D126](https://www.uniprot.org/uniprotkb/A4D126) · Ensembl [ENSG00000214960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214960)

## Data

Gene col 13236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13236); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13236]; `tensor/DDL_lfc|DDL_z.npy` [13236]; `embed/gene_vectors.npy` [13236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13236 or target_col == 13236). Every well: [[CRPPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRPPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
