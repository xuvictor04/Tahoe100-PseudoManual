---
symbol: "COP1-DT"
type: "gene"
col: 14057
ensembl_id: "ENSG00000236021"
name: "COP1 divergent transcript"
location: "1q25.2"
module: 133
arm: "+"
pooled_cpm: 13.0
n_lines_expressing: 37
n_dd_up: 38
n_dd_down: 4
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# COP1-DT

*COP1 divergent transcript* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.44× (z +17.7, q 0e+00, up in 23 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.594× (z -5.3, q 6e-05, down in 18 of 32 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (H4 0.0125×, NCI-H460 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.0928×, H4 0.0516×; ⚠ cell-cycle shift, explains ~41% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.110×, NCI-H460 0.175×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.0996×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.156×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPPA2]] (+0.90, fdr 7e-06, ⚠ same locus), [[VLDLR-AS1]] (+0.71, fdr 7e-06), [[TTTY14]] (+0.68, fdr 7e-06), [[LURAP1L-AS1]] (+0.64, fdr 1e-05); moves opposite to [[MED14]] (-0.53, fdr 3e-05), [[THEM6]] (-0.49, fdr 2e-04), [[ACO1]] (-0.48, fdr 2e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PAPPA2]] → it (grade B ⚠); 11 go from it, the strongest it → [[PAPPA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14057.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +17.7 | 0e+00 | 23/30 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.44×** | +15.1 | 0e+00 | 29/31 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.70×** | +9.3 | 3e-18 | 2/9 (HOP62, LOX-IMVI) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +9.1 | 1e-17 | 15/30 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +8.4 | 4e-15 | 3/8 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +6.6 | 5e-09 | 15/29 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +6.6 | 5e-09 | 8/18 (HEC-1-A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +6.4 | 9e-09 | 13/27 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.86×** | +6.3 | 2e-08 | 18/33 (hTERT-HPNE, SW 900, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.79×** | +5.9 | 2e-07 | 16/30 (LOX-IMVI, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.51×** | +5.8 | 3e-07 | 15/35 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.7 | 6e-07 | 12/34 (HEC-1-A, A498, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.41×** | +4.9 | 4e-05 | 12/35 (LOX-IMVI, hTERT-HPNE, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.8 | 6e-05 | 14/28 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +4.8 | 6e-05 | 14/31 (LOX-IMVI, SHP-77, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.61×** | +4.8 | 6e-05 | 15/33 (LOX-IMVI, RPMI-7951, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.35×** | +4.2 | 8e-04 | 14/34 (NCI-H460, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 9e-04 | 10/30 (LoVo, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14057.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 10 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (H4 0.0125×, NCI-H460 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H460 0.0928×, H4 0.0516×; ⚠ cell-cycle shift, explains ~41% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (A-427 0.110×, NCI-H460 0.175×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.0996×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.156×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.594×** | -5.3 | 6e-05 | 18/32 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.606×** | -5.1 | 9e-05 | 14/34 (NCI-H460, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.621×** | -4.9 | 2e-04 | 15/32 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.709×** | -3.4 | 0.096 | 10/34 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Pemetrexed (drug)]] 5 µM |  | 0.716× | -3.3 | 0.11 | 7/28 (HCT15, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14057. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 134 | 0 | 14 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0928× (z -14.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -10.6) |
| [[H4 (line)]] | wt | 111 | 0 | 13 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0125× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 20.8 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.42× (z +10.1) | — |
| [[A-172 (line)]] | wt | 4.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.79× (z +8.6) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -11.5) |
| [[A498 (line)]] | wt | 3.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 4.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.12× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 4.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 4.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.60× (z +10.7) | — |
| [[LoVo (line)]] | wt | 5.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 8.36 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0768× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14057), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPPA2]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | ⚠ same locus (15.3 kb, same strand: neighbours can correlate without regulation) |
| [[VLDLR-AS1]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[TTTY14]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[LURAP1L-AS1]] | +0.64 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[OSCAR]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LINC00616]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[CLIP1]] | +0.59 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[LINC02398]] | +0.57 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[NXPH1]] | +0.56 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[LINC02306]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CFAP54]] | +0.56 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[LINC02755]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[LINC01684]] | +0.55 | +0.59 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED14]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[THEM6]] | -0.49 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[ACO1]] | -0.48 | -0.42 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPPA2]] | B | PAPPA2 activity raises COP1-DT's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.86× lower at baseline in the lines without PAPPA2 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers COP1-DT's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.7% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[LINC01684]] | B | LINC01684 activity raises COP1-DT's level | lines that do not express LINC01684 (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without LINC01684 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IRAG2, COL3A1, LINC01592; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers COP1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01257]] | B | LINC01257 activity raises COP1-DT's level | lines that do not express LINC01257 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without LINC01257 | 0.092 | ⚠ within organs, on part of the lines; also absent: MIR3667HG, LINC01446, NAA11; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPPA2]] | B | COP1-DT activity raises PAPPA2's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 2.44× lower at baseline in the lines without COP1-DT | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[USP38-DT]] | B | COP1-DT activity raises USP38-DT's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without COP1-DT | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[LINC00534]] | B | COP1-DT activity raises LINC00534's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without COP1-DT | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[ANO3]] | B | COP1-DT activity raises ANO3's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without COP1-DT | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[DLG2]] | B | COP1-DT activity raises DLG2's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without COP1-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[PKN2-AS1]] | B | COP1-DT activity raises PKN2-AS1's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without COP1-DT | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[LY96]] | B | COP1-DT activity raises LY96's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 2.27× lower at baseline in the lines without COP1-DT | 0.078 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[H2AZ1-DT]] | B | COP1-DT activity raises H2AZ1-DT's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without COP1-DT | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[INTS6-AS1]] | B | COP1-DT activity raises INTS6-AS1's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.26× lower at baseline in the lines without COP1-DT | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[LINC00393]] | B | COP1-DT activity raises LINC00393's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.37× lower at baseline in the lines without COP1-DT | 0.091 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[LINC02398]] | C | COP1-DT activity raises LINC02398's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without COP1-DT | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.4, 23.8); signed map (24.7, 4.0). **Vector** length 75.8, 16.4% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.0 | +15.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +17.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +4.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | +0.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | COP1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q25.2 — chr1:176,207,646-176,447,919 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55666) · Entrez [121832809](https://www.ncbi.nlm.nih.gov/gene/121832809) · Ensembl [ENSG00000236021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236021)

## Data

Gene col 14057: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14057); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14057, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14057]; `tensor/DDL_lfc|DDL_z.npy` [14057]; `embed/gene_vectors.npy` [14057]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14057 or target_col == 14057). Every well: [[COP1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COP1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
