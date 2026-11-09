---
symbol: "ALDH1B1"
type: "gene"
col: 5971
ensembl_id: "ENSG00000137124"
name: "aldehyde dehydrogenase 1 family member B1"
location: "9p13.1"
module: 5
arm: "+"
pooled_cpm: 5.87
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ALDH1B1

*aldehyde dehydrogenase 1 family member B1* — 9p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.69× (z +9.7, q 2e-19, up in 20 of 24 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.57× (z +6.5, q 1e-08, up in 18 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.629× (z -6.7, q 2e-08, down in 25 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN4]] (+0.74, fdr 7e-06), [[RRS1]] (+0.72, fdr 7e-06), [[DCTPP1]] (+0.72, fdr 7e-06); moves opposite to [[CEP57]] (-0.58, fdr 1e-05), [[C12orf57]] (-0.55, fdr 2e-05), [[EOGT-DT]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMARCA2]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLC35B4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5971.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +9.7 | 2e-19 | 20/24 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.91×** | +6.6 | 1e-08 | 26/43 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +6.5 | 1e-08 | 18/43 (A549, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.82×** | +6.1 | 2e-07 | 23/43 (A-172, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.1 | 3e-05 | 16/42 (A549, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.61×** | +4.8 | 1e-04 | 18/43 (A-172, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.57×** | +4.6 | 4e-04 | 16/43 (SW 900, A-172, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +4.4 | 8e-04 | 16/40 (NCI-H2030, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.55×** | +4.3 | 0.001 | 3/7 (SW480, A498, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.49×** | +4.0 | 0.003 | 8/43 (SW 900, A498, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.14×** | +4.0 | 0.003 | 10/34 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **2.11×** | +4.0 | 0.003 | 5/26 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.006 | 7/42 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.007 | 11/44 (A549, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.7 | 0.009 | 5/27 (HCT15, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.022 | 12/32 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 5 µM |  | **1.86×** | +3.3 | 0.029 | 3/26 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.029 | 2/33 (SW480, NCI-H2347) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.037 | 8/43 (Panc 03.27, Hs 766T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.090 | 8/35 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.33×** | +2.9 | 0.092 | 2/42 (H4, A-427) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.095 | 10/42 (NCI-H460, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.629×** | -6.7 | 2e-08 | 25/38 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -4.8 | 5e-04 | 17/43 (NCI-H23, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.732×** | -4.5 | 0.001 | 20/43 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.647×** | -4.4 | 0.001 | 15/43 (C32, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -4.2 | 0.003 | 14/43 (SW 900, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.677×** | -3.8 | 0.013 | 17/38 (HCT15, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | **0.793×** | -3.3 | 0.069 | 10/43 (SW 900, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.738× | -3.1 | 0.14 | 5/43 (KATO III, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0487× (z -18.3) |
| [[RKO (line)]] | wt | 14.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0524× (z -13.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.126× (z -13.6) |
| [[A-172 (line)]] | wt | 3.51 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0536× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 6.82 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.141× (z -8.8) |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.0) |
| [[LoVo (line)]] | wt | 7.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 3.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -8.6) |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0807× (z -10.7) |
| [[SW48 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -8.5) |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN4]] | +0.74 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[RRS1]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[DCTPP1]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NME1]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[BYSL]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[LYAR]] | +0.68 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[RRP1]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NOP16]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[DHX33]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TBRG4]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[PINX1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP57]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[C12orf57]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[EOGT-DT]] | -0.55 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[KLC4]] | -0.54 | -0.62 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA2]] | B | SMARCA2 activity lowers ALDH1B1's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.78× higher at baseline in the lines without SMARCA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35B4]] | C | ALDH1B1 activity raises SLC35B4's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[RCL1]] | C | ALDH1B1 activity raises RCL1's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.62× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[CHCHD4]] | C | ALDH1B1 activity raises CHCHD4's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.15× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[SIGMAR1]] | C | ALDH1B1 activity raises SIGMAR1's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[NAT10]] | C | ALDH1B1 activity raises NAT10's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[IMP4]] | C | ALDH1B1 activity raises IMP4's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |
| [[DDX31]] | C | ALDH1B1 activity raises DDX31's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without ALDH1B1 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent |
| [[DHX33]] | C | ALDH1B1 activity raises DHX33's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without ALDH1B1 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent |
| [[CEP57]] | C | ALDH1B1 activity raises CEP57's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.37× lower at baseline in the lines without ALDH1B1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.4, -39.0); signed map (-4.7, -48.7). **Vector** length 70.5, 13.0% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.56 to 13); *ribosome biogenesis* (control, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +6.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +9.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -6.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.9 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 1 family member B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.1 — chr9:38,392,702-38,398,661 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALDHX; previously ALDH5 |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Reactome | 4 pathways, smallest: Ethanol oxidation; Phase I - Functionalization of compounds; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P30837](https://www.uniprot.org/uniprotkb/P30837) (Aldehyde dehydrogenase family 1 member B1, mitochondrial):

> Broad specificity, mitochondrial aldehyde dehydrogenase that could play a role in the detoxification of alcohol-derived acetaldehyde and other aldehydes. Shows an absolute preference for NAD(+) as no activity is detected with NADP(+). Has a high affinity and catalytic efficiency toward aliphatic medium-chain saturated aldehydes relative to short-chain and aromatic aldehydes in vitro. Also capable of metabolizing products of lipid peroxidation, namely 4-hydroxynon-2-enal(4-HNE) and malonaldehyde …

**Summary**, from NCBI Gene [219](https://www.ncbi.nlm.nih.gov/gene/219):

> This protein belongs to the aldehyde dehydrogenases family of proteins. Aldehyde dehydrogenase is the second enzyme of the major oxidative pathway of alcohol metabolism. This gene does not contain introns in the coding sequence. The variation of this locus may affect the development of alcohol-related problems. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:407) · Entrez [219](https://www.ncbi.nlm.nih.gov/gene/219) · UniProt [P30837](https://www.uniprot.org/uniprotkb/P30837) · Ensembl [ENSG00000137124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137124)

## Data

Gene col 5971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5971); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5971]; `tensor/DDL_lfc|DDL_z.npy` [5971]; `embed/gene_vectors.npy` [5971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5971 or target_col == 5971). Every well: [[ALDH1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
