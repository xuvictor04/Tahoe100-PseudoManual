---
symbol: "FBN1"
type: "gene"
col: 9246
ensembl_id: "ENSG00000166147"
name: "fibrillin 1"
location: "15q21.1"
module: 66
arm: "+"
pooled_cpm: 80.84
n_lines_expressing: 22
n_dd_up: 26
n_dd_down: 17
n_dd_up_clean: 23
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 53
direction_downstream: 61
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# FBN1

*fibrillin 1* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.31× (z +13.1, q 3e-36, up in 8 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +6.5, q 1e-08, up in 5 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.418× (z -13.1, q 1e-36, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL1A2]] (+0.72, fdr 7e-06), [[ARHGEF6]] (+0.68, fdr 7e-06), [[PDGFRB]] (+0.68, fdr 7e-06); moves opposite to [[GSTO2]] (-0.45, fdr 9e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[NOXA1]] → it (grade B ⚠); 61 go from it, the strongest it → [[SMPD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +13.1 | 3e-36 | 8/20 (HOP62, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +12.4 | 7e-33 | 6/15 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +8.5 | 5e-15 | 4/15 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.5 | 1e-08 | 5/22 (LOX-IMVI, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.50×** | +6.3 | 3e-08 | 13/21 (NCI-H460, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.48×** | +6.2 | 4e-08 | 14/22 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 5e-07 | 11/20 (NCI-H460, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 4e-05 | 11/20 (NCI-H460, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.6 | 3e-04 | 6/20 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.4 | 6e-04 | 11/20 (NCI-H460, H4, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +4.3 | 8e-04 | 7/21 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.3 | 8e-04 | 4/21 (NCI-H460, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 1e-03 | 11/19 (NCI-H460, H4, …) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.32×** | +4.0 | 0.002 | 10/20 (J82, NCI-H1792, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.0 | 0.003 | 13/19 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 9/21 (NCI-H460, H4, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.004 | 12/20 (NCI-H460, H4, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.005 | 2/20 (NCI-H460, SNU-1) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.418×** | -13.1 | 1e-36 | 17/20 (COLO 205, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -11.3 | 3e-27 | 15/20 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.600×** | -11.3 | 3e-27 | 17/20 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.499×** | -10.9 | 3e-25 | 15/20 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -5.6 | 2e-06 | 15/20 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.740×** | -4.7 | 2e-04 | 10/20 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.748×** | -4.5 | 4e-04 | 6/20 (C32, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.584×** | -4.4 | 8e-04 | 6/20 (COLO 205, SW 1271, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -4.4 | 9e-04 | 7/20 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.775×** | -4.0 | 0.004 | 9/20 (NCI-H1792, J82, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.006 | 15/20 (SW 900, hTERT-HPNE, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.784×** | -3.8 | 0.007 | 12/20 (NCI-H1792, J82, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.852× | -3.6 | 0.017 | 10/21 (H4, A-172, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.805×** | -3.4 | 0.029 | 11/20 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.686×** | -3.1 | 0.072 | 9/21 (NCI-H460, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Penfluridol (drug)]] 5 µM |  | **0.815×** | -3.1 | 0.072 | 10/19 (HS-578T, A-172, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 0.05 µM |  | **0.809×** | -3.1 | 0.072 | 6/19 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.692×** | -3.0 | 0.082 | 5/20 (SW 900, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.7 | 4 | 5 | [[Trametinib (drug)]] 0.5 µM 2.81× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.6) |
| [[HS-578T (line)]] | alt | 1,067 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -16.5) |
| [[hTERT-HPNE (line)]] | wt | 677 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 300 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -13.9) |
| [[A-172 (line)]] | wt | 707 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -14.1) |
| [[HOP62 (line)]] | alt | 81.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +9.3) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.247× (z -10.5) |
| [[SNU-423 (line)]] | alt | 91.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.237× (z -11.2) |
| [[SW 900 (line)]] | alt | 183 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -14.4) |
| [[AN3 CA (line)]] | alt | 158 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -12.6) |
| [[COLO 205 (line)]] | alt | 32.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -13.0) |
| [[SW 1088 (line)]] | alt | 227 | 0 | 2 | — | [[Decitabine (drug)]] 0.5 µM 0.0761× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 330 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.310× (z -9.3) |
| [[A-427 (line)]] | wt | 8.52 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL1A2]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 965 |
| [[ARHGEF6]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[PDGFRB]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 546 |
| [[NID2]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 465 |
| [[CARMN]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[COL3A1]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 970 |
| [[PTGFR]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[COL1A1]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 929 |
| [[TIMP3]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION; STRING 610 |
| [[COL5A1]] | +0.60 | +0.58 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 929 |
| [[SDC2]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[SULF1]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 | STRING 408 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSTO2]] | -0.45 | -0.43 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 4, C 49. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity lowers FBN1's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 9.25× higher at baseline in the lines without NOXA1 | 0.047 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[COL7A1]] | B | COL7A1 activity raises FBN1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.27× lower at baseline in the lines without COL7A1 | 0.097 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[IGFBP6]] | B | IGFBP6 activity raises FBN1's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without IGFBP6 | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers FBN1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ITGA4]] | C | ITGA4 activity raises FBN1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 6.91× lower at baseline in the lines without ITGA4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises FBN1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 6.74× lower at baseline in the lines without COL1A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises FBN1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.44× lower at baseline in the lines without COL5A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises FBN1's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 10.44× lower at baseline in the lines without LINC01411 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises FBN1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 8.93× lower at baseline in the lines without PDGFRB | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises FBN1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 5.50× lower at baseline in the lines without PRRX1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises FBN1's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 4.73× lower at baseline in the lines without DKK3 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises FBN1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 7.90× lower at baseline in the lines without COL1A2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |

### Downstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 15, C 46. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMPD1]] | B | FBN1 activity raises SMPD1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 1.98× lower at baseline in the lines without FBN1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[DAB2]] | B | FBN1 activity raises DAB2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.57× lower at baseline in the lines without FBN1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[MAP1A]] | B | FBN1 activity raises MAP1A's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.74× lower at baseline in the lines without FBN1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[NOXA1]] | B | FBN1 activity lowers NOXA1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 1.94× higher at baseline in the lines without FBN1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[PCDHGC3]] | B | FBN1 activity raises PCDHGC3's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without FBN1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[LOXL2]] | B | FBN1 activity raises LOXL2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.33× lower at baseline in the lines without FBN1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[GXYLT2]] | B | FBN1 activity raises GXYLT2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.84× lower at baseline in the lines without FBN1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[TGFBI]] | B | FBN1 activity raises TGFBI's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.91× lower at baseline in the lines without FBN1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[B3GNT9]] | B | FBN1 activity raises B3GNT9's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without FBN1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[EML1]] | B | FBN1 activity raises EML1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.98× lower at baseline in the lines without FBN1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[DAB2]] | B | FBN1 activity strengthens DAB2's drug response | lines that do not express FBN1 (14) vs lines expressing it (16) | the lines without FBN1 respond 0.54× as strongly (z diff +2.83); strongest at Panobinostat 5 µM: 0.58x vs 0.29x (z diff +5.0) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; target measured in part of the lines; artifact flags |
| [[PLOD2]] | B | FBN1 activity raises PLOD2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.92× lower at baseline in the lines without FBN1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.3, 21.1); signed map (26.7, 44.2). **Vector** length 83.0, 28.5% of its response variance represented; |z| ≥ 3 in 624 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ECM proteoglycans* (reactome, mean cos +0.52 to 9); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.55 to 8); *Fibronectin matrix formation* (reactome, mean cos +0.60 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +12.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | fibrillin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.1 — chr15:48,408,313-48,645,721 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MASS, OCTD, SGS; previously FBN, MFS1, WMS |
| Gene groups (HGNC) | Fibrillin family |
| Hallmark sets | COAGULATION, APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 10 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [P35555](https://www.uniprot.org/uniprotkb/P35555) (Fibrillin-1):

> [Fibrillin-1]: Structural component of the 10-12 nm diameter microfibrils of the extracellular matrix, which conveys both structural and regulatory properties to load-bearing connective tissues. Fibrillin-1-containing microfibrils provide long-term force bearing structural support. In tissues such as the lung, blood vessels and skin, microfibrils form the periphery of the elastic fiber, acting as a scaffold for the deposition of elastin. In addition, microfibrils can occur as …

**Summary**, from NCBI Gene [2200](https://www.ncbi.nlm.nih.gov/gene/2200):

> This gene encodes a member of the fibrillin family of proteins. The encoded preproprotein is proteolytically processed to generate two proteins including the extracellular matrix component fibrillin-1 and the protein hormone asprosin. Fibrillin-1 is an extracellular matrix glycoprotein that serves as a structural component of calcium-binding microfibrils. These microfibrils provide force-bearing structural support in elastic and nonelastic connective tissue throughout the body. Asprosin, …

**Accessions** — [HGNC:3603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3603) · Entrez [2200](https://www.ncbi.nlm.nih.gov/gene/2200) · UniProt [P35555](https://www.uniprot.org/uniprotkb/P35555) · Ensembl [ENSG00000166147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166147)

## Data

Gene col 9246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9246); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9246]; `tensor/DDL_lfc|DDL_z.npy` [9246]; `embed/gene_vectors.npy` [9246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9246 or target_col == 9246). Every well: [[FBN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
