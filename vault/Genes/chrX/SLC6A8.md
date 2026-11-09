---
symbol: "SLC6A8"
type: "gene"
col: 5135
ensembl_id: "ENSG00000130821"
name: "solute carrier family 6 member 8"
location: "Xq28"
module: 1
arm: "-"
pooled_cpm: 29.95
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SLC6A8

*solute carrier family 6 member 8* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +7.1, q 5e-10, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.373× (z -6.5, q 3e-08, down in 32 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2A]] (+0.57, fdr 1e-05), [[SH3D21]] (+0.55, fdr 1e-05), [[NLGN2]] (+0.53, fdr 1e-05); moves opposite to [[CCDC66]] (-0.56, fdr 1e-05), [[COA1]] (-0.56, fdr 2e-05), [[RAD51D]] (-0.52, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CREB3L1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.1 | 5e-10 | 25/42 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.8 | 2e-09 | 27/42 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.9 | 6e-07 | 23/43 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.2 | 3e-05 | 23/41 (H4, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.2 | 3e-05 | 25/43 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +4.9 | 8e-05 | 23/43 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.8 | 1e-04 | 3/44 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.001 | 19/43 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +4.1 | 0.003 | 18/43 (A498, AsPC-1, …) | rises with dose | low cells (technical?); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.38×** | +4.0 | 0.004 | 18/44 (HepG2/C3A, HS-578T, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.009 | 18/41 (SK-MEL-2, A-172, …) | two highest doses | low cells (technical?); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.018 | 17/43 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.024 | 10/44 (C32, SW1417, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.3 | 0.031 | 13/43 (PANC-1, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.031 | 12/42 (SK-MEL-2, A-172, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.031 | 14/40 (hTERT-HPNE, KATO III, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.62×** | +3.2 | 0.053 | 12/42 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.373×** | -6.5 | 3e-08 | 32/43 (SNU-423, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -5.0 | 1e-04 | 21/42 (KATO III, HS-578T, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.671×** | -4.9 | 2e-04 | 20/43 (Hs 766T, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.795×** | -4.2 | 0.004 | 19/43 (HepG2/C3A, AN3 CA, …) | two highest doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -4.1 | 0.004 | 19/41 (Hs 766T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.755×** | -3.6 | 0.029 | 22/43 (SW 1088, HepG2/C3A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.050 | 15/42 (LOX-IMVI, HS-578T, …) | top dose only | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.788× | -3.1 | 0.15 | 11/43 (NCI-H2030, KATO III, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.8 | 9 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.87× (z +15.3) | — |
| [[Hs 766T (line)]] | wt | 82.4 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0618× (z -18.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.104× (z -14.7) |
| [[HepG2_C3A (line)]] | wt | 79.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -16.3) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.228× (z -10.3) |
| [[LS 180 (line)]] | wt | 52.8 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.123× (z -12.2) |
| [[A498 (line)]] | wt | 20.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +15.7) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 52.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -10.2) |
| [[J82 (line)]] | alt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0422× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 73.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.6) |
| [[PANC-1 (line)]] | alt | 26.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.6) | — |
| [[SW480 (line)]] | alt | 12.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.0) | — |
| [[A549 (line)]] | wt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +11.3) | — |
| [[AN3 CA (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -16.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[AsPC-1 (line)]] | alt | 71.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +10.4) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[COLO 205 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.122× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[HOP62 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -8.6) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0446× (z -15.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 27.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +9.3) | — |
| [[A-172 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2A]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SH3D21]] | +0.55 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[NLGN2]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ATG9A]] | +0.53 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[KIAA1191]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[TNFSF9]] | +0.52 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[PFKL]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TPI1]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[VEGFA]] | +0.51 | +0.58 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CREB3L1]] | +0.51 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CSRP2]] | +0.50 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[SMPD3]] | +0.50 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC66]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[COA1]] | -0.56 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[RAD51D]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[JPX]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[COG2]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[ZNF839]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[ALKBH8]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[WDR7]] | -0.50 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[IRAK1BP1]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[BRIX1]] | -0.50 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[RPRD1A]] | -0.49 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[ORC5]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CREB3L1]] | B | CREB3L1 activity weakens SLC6A8's drug response | lines that do not express CREB3L1 (23) vs lines expressing it (21) | the lines without CREB3L1 respond 1.13× as strongly (z diff -0.21); strongest at Idarubicin (hydrochloride) 5 µM: 1.92x vs 1.14x (z diff -3.9) | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers SLC6A8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.392). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.0, -47.8); signed map (-34.0, 29.8). **Vector** length 107, 25.4% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +6.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.0 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.8 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +5.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.2 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,687,926-153,696,588 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRTR, CT1, CRT, CRT-1, CRT1 |
| Gene groups (HGNC) | Solute carrier family 6 |
| Hallmark sets | MYOGENESIS, UV_RESPONSE_UP, HEME_METABOLISM, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Creatine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P48029](https://www.uniprot.org/uniprotkb/P48029) (Sodium- and chloride-dependent creatine transporter 1):

> Creatine:sodium symporter which mediates the uptake of creatine. Plays an important role in supplying creatine to the brain via the blood-brain barrier (By similarity).

**Summary**, from NCBI Gene [6535](https://www.ncbi.nlm.nih.gov/gene/6535):

> The protein encoded by this gene is a plasma membrane protein whose function is to transport creatine into and out of cells. Defects in this gene can result in X-linked creatine deficiency syndrome. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:11055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11055) · Entrez [6535](https://www.ncbi.nlm.nih.gov/gene/6535) · UniProt [P48029](https://www.uniprot.org/uniprotkb/P48029) · Ensembl [ENSG00000130821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130821)

## Data

Gene col 5135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5135); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5135]; `tensor/DDL_lfc|DDL_z.npy` [5135]; `embed/gene_vectors.npy` [5135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5135 or target_col == 5135). Every well: [[SLC6A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
