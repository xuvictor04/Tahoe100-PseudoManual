---
symbol: "USP48"
type: "gene"
col: 1636
ensembl_id: "ENSG00000090686"
name: "ubiquitin specific peptidase 48"
location: "1p36.12"
module: 57
arm: "+"
pooled_cpm: 152.0
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# USP48

*ubiquitin specific peptidase 48* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.27× (z +5.8, q 5e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.668× (z -9.6, q 4e-19, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL3]] (+0.72, fdr 1e-05), [[NKTR]] (+0.71, fdr 7e-06), [[TTC3]] (+0.71, fdr 7e-06); moves opposite to [[ZNF562]] (-0.65, fdr 8e-06), [[GABPB1]] (-0.63, fdr 2e-05), [[E2F3]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CCDC71L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +5.8 | 5e-06 | 30/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.007 | 23/48 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.033 | 24/47 (NCI-H1573, RKO, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.7 | 0.034 | 8/48 (C32, NCI-H23, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.070 | 22/49 (SK-MEL-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.074 | 14/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.092 | 20/49 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | 1.29× | +3.2 | 0.11 | 18/49 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.13 | 19/48 (PANC-1, C-33 A, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -9.6 | 4e-19 | 38/48 (NCI-H460, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -7.5 | 1e-11 | 36/47 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.732×** | -7.4 | 2e-11 | 36/48 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.749×** | -6.6 | 5e-09 | 28/48 (HOP62, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.828×** | -6.3 | 3e-08 | 22/49 (AsPC-1, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.775×** | -5.6 | 2e-06 | 26/45 (C-33 A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.822×** | -4.7 | 3e-04 | 23/48 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.841× | -4.1 | 0.003 | 21/48 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.843× | -4.0 | 0.003 | 20/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.844× | -3.9 | 0.006 | 18/48 (LoVo, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | 0.856× | -3.5 | 0.021 | 21/44 (SNU-1, CHP-212, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.904× | -3.4 | 0.033 | 11/48 (PANC-1, HS-578T, …) | top dose only | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.876× | -3.1 | 0.077 | 9/49 (LS 180, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 104 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.439× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.413× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 114 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.481× (z -12.4) |
| [[HOP62 (line)]] | alt | 171 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.426× (z -12.2) |
| [[SW 900 (line)]] | alt | 130 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.424× (z -9.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.465× (z -9.1) |
| [[A549 (line)]] | wt | 109 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.408× (z -10.0) |
| [[C-33 A (line)]] | alt | 245 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.92× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -11.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 194 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.430× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.454× (z -10.6) |
| [[Hs 766T (line)]] | wt | 224 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.433× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 112 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.524× (z -8.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 138 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.447× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 207 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -12.9) |
| [[A-427 (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.477× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 109 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.526× (z -9.6) |
| [[AN3 CA (line)]] | alt | 163 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.265× (z -10.9) |
| [[BT-474 (line)]] | alt | 94.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[H4 (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 112 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -11.9) |
| [[J82 (line)]] | alt | 170 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.609× (z -8.7) |
| [[KATO III (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.489× (z -10.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.482× (z -10.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 122 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.420× (z -10.4) |
| [[PANC-1 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 227 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.492× (z -10.2) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SNU-1 (line)]] | wt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.233× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change |
| [[SNU-423 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.497× (z -9.4) ⚠ toxic |
| [[SW48 (line)]] | wt | 173 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 155 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.602× (z -8.5) |
| [[COLO 205 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 187 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 182 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 226 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 150 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 197 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 149 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL3]] | +0.72 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[NKTR]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[TTC3]] | +0.71 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 | pathway: Deubiquitination |
| [[GMCL1]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[CAT]] | +0.68 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[UBAC1]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 | STRING 625 |
| [[SKIC3]] | +0.67 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CBX1]] | +0.67 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[RPA1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PAPSS1]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[HACE1]] | +0.66 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF562]] | -0.65 | -0.57 / -0.62 | both halves | 8e-06 |  |
| [[GABPB1]] | -0.63 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[E2F3]] | -0.62 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.62 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[NIP7]] | -0.60 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.59 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[ZNF629]] | -0.58 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SLC9A8]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TP53RK]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[NFE2L2]] | -0.58 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[EMG1]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[FBXO30]] | -0.57 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC71L]] | B | CCDC71L activity lowers USP48's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 1.18× higher at baseline in the lines without CCDC71L | 0.099 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (2.2, -10.6); signed map (-36.9, -11.6). **Vector** length 123, 36.3% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.8 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | +5.3 | -3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.3 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +2.6 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.7 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.2 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -4.9 | -6.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 48 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:21,678,298-21,783,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23277, FLJ11328, FLJ20103, FLJ23054, MGC14879; previously USP31 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UV5](https://www.uniprot.org/uniprotkb/Q86UV5) (Ubiquitin carboxyl-terminal hydrolase 48):

> Deubiquitinase that recognizes and hydrolyzes the peptide bond at the C-terminal Gly of ubiquitin. Involved in the processing of polyubiquitin precursors as well as that of ubiquitinated proteins. Plays a role in the regulation of NF-kappa-B activation by TNF receptor superfamily via its interactions with RELA and TRAF2. May also play a regulatory role at postsynaptic sites. Plays an important role in cell cycle progression by deubiquitinating Aurora B/AURKB and thereby extending its stability. …

**Summary**, from NCBI Gene [84196](https://www.ncbi.nlm.nih.gov/gene/84196):

> This gene encodes a protein containing domains that associate it with the peptidase family C19, also known as family 2 of ubiquitin carboxyl-terminal hydrolases. Family members function as deubiquitinating enzymes, recognizing and hydrolyzing the peptide bond at the C-terminal glycine of ubiquitin. Enzymes in peptidase family C19 are involved in the processing of poly-ubiquitin precursors as well as that of ubiquitinated proteins. Alternate transcriptional splice variants, encoding different …

**Accessions** — [HGNC:18533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18533) · Entrez [84196](https://www.ncbi.nlm.nih.gov/gene/84196) · UniProt [Q86UV5](https://www.uniprot.org/uniprotkb/Q86UV5) · Ensembl [ENSG00000090686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090686)

## Data

Gene col 1636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1636); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1636]; `tensor/DDL_lfc|DDL_z.npy` [1636]; `embed/gene_vectors.npy` [1636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1636 or target_col == 1636). Every well: [[USP48 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP48.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
