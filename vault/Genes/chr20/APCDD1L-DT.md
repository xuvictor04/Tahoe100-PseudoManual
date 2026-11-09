---
symbol: "APCDD1L-DT"
type: "gene"
col: 13788
ensembl_id: "ENSG00000231290"
name: "APCDD1L divergent transcript"
location: "20q13.32"
module: 13
arm: "+"
pooled_cpm: 32.2
n_lines_expressing: 24
n_dd_up: 9
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 61
direction_downstream: 53
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# APCDD1L-DT

*APCDD1L divergent transcript* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.42× (z +11.0, q 2e-25, up in 19 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.488× (z -9.0, q 1e-16, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1L]] (+0.85, fdr 7e-06, ⚠ same locus), [[LINC01060]] (+0.72, fdr 7e-06), [[LINC00702]] (+0.70, fdr 7e-06), [[COL7A1]] (+0.70, fdr 7e-06); moves opposite to [[CHPT1]] (-0.56, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 61 arrows point to it, the strongest [[NRARP]] → it (grade B ⚠); 53 go from it, the strongest it → [[MIR4435-2HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +11.0 | 2e-25 | 19/22 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.8 | 1e-12 | 1/12 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +7.7 | 2e-12 | 11/22 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +6.7 | 3e-09 | 7/22 (NCI-H1573, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +6.5 | 9e-09 | 11/22 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.1 | 1e-07 | 3/16 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.2 | 0.002 | 2/15 (BT-474, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.002 | 6/21 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.042 | 7/20 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.13 | 3/19 (SW 900, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -9.0 | 1e-16 | 14/22 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -6.6 | 1e-08 | 11/22 (NCI-H23, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.670×** | -5.0 | 9e-05 | 12/21 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.674×** | -5.0 | 1e-04 | 7/22 (RPMI-7951, HOP62, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.701×** | -4.5 | 9e-04 | 13/22 (H4, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.782×** | -4.4 | 0.001 | 11/22 (SNU-423, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.713×** | -4.3 | 0.002 | 12/20 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.751×** | -3.6 | 0.023 | 14/22 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -3.6 | 0.023 | 13/22 (RPMI-7951, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.822×** | -3.5 | 0.026 | 8/22 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.753×** | -3.4 | 0.030 | 12/19 (RPMI-7951, NCI-H23, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.756×** | -3.4 | 0.033 | 11/22 (H4, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.037 | 4/22 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.774×** | -3.2 | 0.055 | 10/22 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.783×** | -3.1 | 0.077 | 11/20 (SK-MEL-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.782×** | -3.0 | 0.100 | 5/22 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.790×** | -3.0 | 0.100 | 9/21 (RPMI-7951, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 616 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -17.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.342× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 14.1 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 10.3× (z +13.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.184× (z -9.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 47.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -11.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[H4 (line)]] | wt | 143 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.261× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.4) |
| [[SNU-423 (line)]] | alt | 139 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.65× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.385× (z -9.9) |
| [[J82 (line)]] | alt | 82.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -10.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.466× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 40.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 41.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 1 | — | [[Tubulin inhibitor 6 (drug)]] 0.5 µM 0.201× (z -13.9) |
| [[A-427 (line)]] | wt | 5.55 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.14 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.33 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.63 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 161 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.77 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1L]] | +0.85 | +0.79 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[LINC01060]] | +0.72 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[LINC00702]] | +0.70 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[COL7A1]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[FRMD4A]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[LINC01435]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SPOCD1]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LINC01411]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[NAV1]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[OR9Q1]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[CSF1R]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[IPO9-AS1]] | +0.65 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[COL5A3]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 6, C 55. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRARP]] | B | NRARP activity lowers APCDD1L-DT's level | lines that do not express NRARP (14) vs lines expressing it (36) | 6.13× higher at baseline in the lines without NRARP | 0.001 | ⚠ within organs, on part of the lines; also absent: PLS1, OCLN, PDE9A |
| [[VEPH1]] | B | VEPH1 activity raises APCDD1L-DT's level | lines that do not express VEPH1 (26) vs lines expressing it (24) | 3.22× lower at baseline in the lines without VEPH1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, PHACTR1, GYPC |
| [[NLRP1]] | B | NLRP1 activity raises APCDD1L-DT's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.89× lower at baseline in the lines without NLRP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[COL7A1]] | B | COL7A1 activity raises APCDD1L-DT's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.51× lower at baseline in the lines without COL7A1 | 0.053 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[COL5A3]] | B | COL5A3 activity raises APCDD1L-DT's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.69× lower at baseline in the lines without COL5A3 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[LINC01605]] | B | LINC01605 activity raises APCDD1L-DT's level | lines that do not express LINC01605 (27) vs lines expressing it (23) | 1.99× lower at baseline in the lines without LINC01605 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC00460, LINC01133, PTPRR |
| [[APCDD1L]] | C | APCDD1L activity raises APCDD1L-DT's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 8.12× lower at baseline in the lines without APCDD1L | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises APCDD1L-DT's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 7.26× lower at baseline in the lines without LINC01411 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises APCDD1L-DT's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 7.27× lower at baseline in the lines without LINC01615 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises APCDD1L-DT's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 5.91× lower at baseline in the lines without PDGFRB | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises APCDD1L-DT's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 5.23× lower at baseline in the lines without CDH13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises APCDD1L-DT's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 4.48× lower at baseline in the lines without HTR1F | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 17, C 36. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR4435-2HG]] | B | APCDD1L-DT activity raises MIR4435-2HG's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.55× lower at baseline in the lines without APCDD1L-DT | 0.017 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[C2orf92]] | B | APCDD1L-DT activity raises C2orf92's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without APCDD1L-DT | 0.024 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[NLRP1]] | B | APCDD1L-DT activity raises NLRP1's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 3.22× lower at baseline in the lines without APCDD1L-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[EVC]] | B | APCDD1L-DT activity raises EVC's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 3.12× lower at baseline in the lines without APCDD1L-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[IQCJ]] | B | APCDD1L-DT activity raises IQCJ's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.02× lower at baseline in the lines without APCDD1L-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[CLEC2D]] | B | APCDD1L-DT activity raises CLEC2D's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without APCDD1L-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[ANAPC1P4]] | B | APCDD1L-DT activity raises ANAPC1P4's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without APCDD1L-DT | 0.040 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[LINC01500]] | B | APCDD1L-DT activity raises LINC01500's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without APCDD1L-DT | 0.041 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[ADAMTS16]] | B | APCDD1L-DT activity raises ADAMTS16's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.62× lower at baseline in the lines without APCDD1L-DT | 0.042 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[FMNL3]] | B | APCDD1L-DT activity raises FMNL3's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.37× lower at baseline in the lines without APCDD1L-DT | 0.049 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[SHANK1]] | B | APCDD1L-DT activity raises SHANK1's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.98× lower at baseline in the lines without APCDD1L-DT | 0.050 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[CAVIN4]] | B | APCDD1L-DT activity raises CAVIN4's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.82× lower at baseline in the lines without APCDD1L-DT | 0.062 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.1, 17.1); signed map (22.2, 47.8). **Vector** length 75.1, 22.9% of its response variance represented; |z| ≥ 3 in 616 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.50 to 9); *Collagen degradation* (reactome, mean cos +0.51 to 8); *Collagen chain trimerization* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.9 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.6 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -5.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | APCDD1L divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.32 — chr20:58,515,379-58,619,888 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously APCDD1L-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27152](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27152) · Entrez [149773](https://www.ncbi.nlm.nih.gov/gene/149773) · Ensembl [ENSG00000231290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231290)

## Data

Gene col 13788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13788); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13788]; `tensor/DDL_lfc|DDL_z.npy` [13788]; `embed/gene_vectors.npy` [13788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13788 or target_col == 13788). Every well: [[APCDD1L-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APCDD1L-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
