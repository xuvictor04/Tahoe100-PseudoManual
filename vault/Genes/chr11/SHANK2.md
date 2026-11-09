---
symbol: "SHANK2"
type: "gene"
col: 8482
ensembl_id: "ENSG00000162105"
name: "SH3 and multiple ankyrin repeat domains 2"
location: "11q13.3-q13.4"
module: 193
arm: "+"
pooled_cpm: 132.47
n_lines_expressing: 35
n_dd_up: 3
n_dd_down: 51
n_dd_up_clean: 2
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# SHANK2

*SH3 and multiple ankyrin repeat domains 2* — 11q13.3-q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.31× (z +4.6, q 0.003, up in 17 of 33 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Demeclocycline (drug)]] 5 µM: 1.20× (z +4.3, q 0.005, up in 16 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.300× (z -19.9, q 0e+00, down in 32 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD4]] (+0.68, fdr 7e-06), [[CCND1]] (+0.62, fdr 7e-06), [[MAMLD1]] (+0.61, fdr 1e-05); moves opposite to [[IGFBP5]] (-0.46, fdr 5e-05), [[BPNT1]] (-0.44, fdr 9e-05), [[C1R]] (-0.44, fdr 8e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PHLDA2]] → it (grade B ⚠); 4 go from it, the strongest it → [[ACTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.31×** | +4.6 | 0.003 | 17/33 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.20× | +4.3 | 0.005 | 16/33 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Dabrafenib (drug)]] 5 µM |  | **1.61×** | +4.2 | 0.005 | 18/34 (HOP62, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.1 | 0.005 | 13/34 (SW 900, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.080 | 14/32 (HT-29, Hs 766T, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.45× | +3.2 | 0.12 | 16/33 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.22× | +3.1 | 0.16 | 15/33 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.18 | 12/34 (RKO, A-427, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.300×** | -19.9 | 0e+00 | 32/33 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -19.7 | 0e+00 | 27/33 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.351×** | -16.6 | 0e+00 | 30/32 (NCI-H1573, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.368×** | -16.5 | 0e+00 | 30/33 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.374×** | -16.2 | 0e+00 | 30/33 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.417×** | -13.9 | 9e-42 | 27/33 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.602×** | -11.8 | 3e-30 | 27/34 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.541×** | -9.8 | 5e-21 | 28/33 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.557×** | -9.3 | 1e-18 | 23/29 (A-427, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.692×** | -8.6 | 6e-16 | 22/33 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.600×** | -8.4 | 2e-15 | 24/33 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.605×** | -8.3 | 6e-15 | 27/33 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.616×** | -8.0 | 6e-14 | 28/34 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.626×** | -7.1 | 4e-11 | 23/30 (J82, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.664×** | -6.7 | 6e-10 | 25/33 (NCI-H23, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.672×** | -6.5 | 2e-09 | 22/33 (Panc 03.27, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -6.4 | 4e-09 | 20/33 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.662×** | -6.4 | 5e-09 | 23/33 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.735×** | -6.2 | 1e-08 | 17/33 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 178 | 0 | 29 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -25.9) |
| [[HOP62 (line)]] | alt | 123 | 0 | 27 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.4) |
| [[NCI-H23 (line)]] | alt | 340 | 0 | 17 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0837× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 766 | 0 | 16 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0769× (z -21.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.8) |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -19.5) |
| [[A549 (line)]] | wt | 341 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -26.6) |
| [[Panc 03.27 (line)]] | alt | 229 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -16.9) |
| [[LoVo (line)]] | wt | 72.8 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -18.9) |
| [[HEC-1-A (line)]] | alt | 225 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 477 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -25.1) |
| [[SW1417 (line)]] | alt | 226 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -16.7) |
| [[RKO (line)]] | wt | 78.1 | 0 | 8 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.100× (z -20.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.199× (z -14.4) |
| [[KATO III (line)]] | alt | 147 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 60.4 | 0 | 7 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0937× (z -17.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.204× (z -12.0) |
| [[SNU-423 (line)]] | alt | 86.9 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.235× (z -12.9) |
| [[PANC-1 (line)]] | alt | 76.0 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -13.2) |
| [[SW48 (line)]] | wt | 99.4 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.4) |
| [[SW480 (line)]] | alt | 80.5 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.301× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.8) |
| [[J82 (line)]] | alt | 74.3 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0902× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.343× (z -9.1) |
| [[HT-29 (line)]] | alt | 95.6 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.219× (z -13.6) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.501× (z -9.1) |
| [[COLO 205 (line)]] | alt | 70.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -17.0) |
| [[HepG2_C3A (line)]] | wt | 198 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -14.3) |
| [[BT-474 (line)]] | alt | 458 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -10.5) |
| [[HCT15 (line)]] | alt | 92.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 53.5 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.371× (z -14.1) |
| [[SW 900 (line)]] | alt | 61.0 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -13.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.408× (z -8.8) |
| [[A-427 (line)]] | wt | 89.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[A498 (line)]] | wt | 78.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -8.9) |
| [[Hs 766T (line)]] | wt | 48.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -9.1) |
| [[LS 180 (line)]] | wt | 45.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.9) |
| [[A-172 (line)]] | wt | 30.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 22.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD4]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CCND1]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[MAMLD1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 | same gene group |
| [[NR2E3]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[ELK3]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SRGAP1]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 | same gene group |
| [[HMGA2]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CDH4]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[KIFC3]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[C16orf74]] | +0.55 | +0.60 / +0.50 | both halves | 1e-05 | same gene group |
| [[LTBP2]] | +0.54 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGFBP5]] | -0.46 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[BPNT1]] | -0.44 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[C1R]] | -0.44 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[MTCP1]] | -0.44 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[SULF1]] | -0.43 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[FPGT]] | -0.42 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDA2]] | B | PHLDA2 activity raises SHANK2's level | lines that do not express PHLDA2 (7) vs lines expressing it (43) | 4.07× lower at baseline in the lines without PHLDA2 | 0.052 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[SLC35F3]] | B | SLC35F3 activity raises SHANK2's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.67× lower at baseline in the lines without SLC35F3 | 0.073 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[MGLL]] | B | MGLL activity raises SHANK2's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.35× lower at baseline in the lines without MGLL | 0.086 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[GPR39]] | C | GPR39 activity raises SHANK2's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 4.44× lower at baseline in the lines without GPR39 | 0.020 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3; co-absent with the target |
| [[CDCP1]] | C | CDCP1 activity raises SHANK2's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 4.09× lower at baseline in the lines without CDCP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C; co-absent with the target |
| [[EPHA2]] | C | EPHA2 activity raises SHANK2's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 4.42× lower at baseline in the lines without EPHA2 | 0.066 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTN1]] | B | SHANK2 activity raises ACTN1's level | lines that do not express SHANK2 (15) vs lines expressing it (35) | 1.15× lower at baseline in the lines without SHANK2 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EPS8L2 |
| [[ARHGEF28]] | B | SHANK2 activity raises ARHGEF28's level | lines that do not express SHANK2 (15) vs lines expressing it (35) | 2.64× lower at baseline in the lines without SHANK2 | 0.079 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EPS8L2 |
| [[EPHA2]] | C | SHANK2 activity raises EPHA2's level | lines that do not express SHANK2 (15) vs lines expressing it (35) | 3.53× lower at baseline in the lines without SHANK2 | 0.055 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EPS8L2; co-absent with the target |
| [[CDCP1]] | C | SHANK2 activity raises CDCP1's level | lines that do not express SHANK2 (15) vs lines expressing it (35) | 4.39× lower at baseline in the lines without SHANK2 | 0.089 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EPS8L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.2, 8.6); signed map (9.1, 43.8). **Vector** length 111, 34.6% of its response variance represented; |z| ≥ 3 in 1,490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | -0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.0 | +4.6 |
|  | [[vincristine (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.6 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.2 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -16.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -6.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.8 | -8.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and multiple ankyrin repeat domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.3-q13.4 — chr11:70,467,854-71,252,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTTNBP1, ProSAP1, SHANK, SPANK-3; previously CORTBP1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing; PDZ domain containing; MicroRNA protein coding host genes; SH3 domain containing |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPX8](https://www.uniprot.org/uniprotkb/Q9UPX8) (SH3 and multiple ankyrin repeat domains protein 2):

> Seems to be an adapter protein in the postsynaptic density (PSD) of excitatory synapses that interconnects receptors of the postsynaptic membrane including NMDA-type and metabotropic glutamate receptors, and the actin-based cytoskeleton. May play a role in the structural and functional organization of the dendritic spine and synaptic junction.

**Summary**, from NCBI Gene [22941](https://www.ncbi.nlm.nih.gov/gene/22941):

> This gene encodes a protein that is a member of the Shank family of synaptic proteins that may function as molecular scaffolds in the postsynaptic density of excitatory synapses. Shank proteins contain multiple domains for protein-protein interaction, including ankyrin repeats, and an SH3 domain. This particular family member contains a PDZ domain, a consensus sequence for cortactin SH3 domain-binding peptides and a sterile alpha motif. The alternative splicing demonstrated in Shank genes has …

**Accessions** — [HGNC:14295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14295) · Entrez [22941](https://www.ncbi.nlm.nih.gov/gene/22941) · UniProt [Q9UPX8](https://www.uniprot.org/uniprotkb/Q9UPX8) · Ensembl [ENSG00000162105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162105)

## Data

Gene col 8482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8482); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8482]; `tensor/DDL_lfc|DDL_z.npy` [8482]; `embed/gene_vectors.npy` [8482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8482 or target_col == 8482). Every well: [[SHANK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHANK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
