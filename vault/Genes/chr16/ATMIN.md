---
symbol: "ATMIN"
type: "gene"
col: 9312
ensembl_id: "ENSG00000166454"
name: "ATM interactor"
location: "16q23.2"
module: 7
arm: "+"
pooled_cpm: 24.31
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ATMIN

*ATM interactor* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +10.6, q 2e-23, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.893× (z -6.3, q 1e-07, down in 9 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.595× (z -4.7, q 9e-04, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.186×, LS 180 0.309×, NCI-H1573 0.371×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[AZD2858 (drug)]] 0.5 µM in 2 lines (HS-578T 0.0877×, C-33 A 0.0951×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS4A]] (+0.62, fdr 1e-05), [[C17orf80]] (+0.62, fdr 9e-06), [[ZBTB39]] (+0.62, fdr 7e-06); moves opposite to [[PTMA]] (-0.60, fdr 3e-05), [[PTMAP2]] (-0.53, fdr 1e-04, ⚠ PTMAP2 in the vector space only through flagged drug-doses), [[PTMAP5]] (-0.52, fdr 1e-04), [[VEGFB]] (-0.50, fdr 9e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PGAP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +10.6 | 2e-23 | 37/47 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +9.3 | 6e-18 | 39/44 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +8.1 | 1e-13 | 29/48 (J82, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.9 | 9e-10 | 29/48 (A498, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +6.2 | 7e-08 | 29/48 (SW480, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 1e-07 | 25/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +6.1 | 1e-07 | 24/44 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +5.7 | 9e-07 | 23/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +5.4 | 3e-06 | 28/48 (A-172, H4, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +5.3 | 6e-06 | 23/47 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.36×** | +5.3 | 6e-06 | 20/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 1e-05 | 22/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.8 | 7e-05 | 23/47 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +4.5 | 3e-04 | 18/48 (A498, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.001 | 18/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.001 | 14/47 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 15/47 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.001 | 16/47 (AsPC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9312.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.186×, LS 180 0.309×, NCI-H1573 0.371×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[AZD2858 (drug)]] 0.5 µM in 2 lines (HS-578T 0.0877×, C-33 A 0.0951×; ⚠ toxic); [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.117×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -6.3 | 1e-07 | 9/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.595×** | -4.7 | 9e-04 | 18/48 (NCI-H1792, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.9 | 0.021 | 19/46 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 28.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 30.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.13× (z +9.4) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 28.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.113× (z -8.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0877× (z -10.2) ⚠ toxic |
| [[HT-29 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.66× (z +8.5) ⚠ toxic | — |
| [[J82 (line)]] | alt | 20.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.19× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS4A]] | +0.62 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[C17orf80]] | +0.62 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[ZBTB39]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 | same gene group |
| [[TOR1A]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ACTR8]] | +0.60 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZNF468]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZNF845]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 | same gene group |
| [[ZNF746]] | +0.58 | +0.49 / +0.51 | both halves | 1e-05 | same gene group |
| [[FBXO30]] | +0.58 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[RNF6]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[C7orf25]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[AP5B1]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTMA]] | -0.60 | -0.66 / -0.46 | both halves | 3e-05 |  |
| [[PTMAP2]] ⚠ | -0.53 | -0.61 / -0.36 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PTMAP5]] | -0.52 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[VEGFB]] | -0.50 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[CHEK2]] | -0.48 | -0.50 / -0.36 | both halves | 1e-04 | STRING 846 |
| [[EIF2AK3]] | -0.48 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[SETD5]] | -0.48 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[IGFBP2]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[EFHC1]] | -0.47 | -0.52 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGAP4]] | B | PGAP4 activity lowers ATMIN's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.25× higher at baseline in the lines without PGAP4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-33.1, 13.8); signed map (3.1, -31.9). **Vector** length 81.2, 15.8% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.1 | +9.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.1 | +6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +1.1 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -4.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ATM interactor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:81,035,842-81,047,350 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ASCIZ, KIAA0431, ZNF822 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [O43313](https://www.uniprot.org/uniprotkb/O43313) (ATM interactor):

> Transcription factor. Plays a crucial role in cell survival and RAD51 foci formation in response to methylating DNA damage. Involved in regulating the activity of ATM in the absence of DNA damage. May play a role in stabilizing ATM. Binds to the DYNLL1 promoter and activates its transcription.

**Summary**, from NCBI Gene [23300](https://www.ncbi.nlm.nih.gov/gene/23300):

> Enables dynein complex binding activity. Involved in positive regulation of DNA-templated transcription. Located in nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29034) · Entrez [23300](https://www.ncbi.nlm.nih.gov/gene/23300) · UniProt [O43313](https://www.uniprot.org/uniprotkb/O43313) · Ensembl [ENSG00000166454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166454)

## Data

Gene col 9312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9312); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9312]; `tensor/DDL_lfc|DDL_z.npy` [9312]; `embed/gene_vectors.npy` [9312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9312 or target_col == 9312). Every well: [[ATMIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATMIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
