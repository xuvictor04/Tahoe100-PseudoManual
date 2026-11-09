---
symbol: "TSPAN6"
type: "gene"
col: 0
ensembl_id: "ENSG00000000003"
name: "tetraspanin 6"
location: "Xq22.1"
module: 29
arm: "+"
pooled_cpm: 8.6
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# TSPAN6

*tetraspanin 6* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.26× (z +16.9, q 0e+00, up in 26 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.51× (z +6.8, q 1e-09, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.632× (z -7.6, q 2e-11, down in 23 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATRAID]] (+0.71, fdr 7e-06), [[SH3BGRL]] (+0.70, fdr 7e-06), [[GSTK1]] (+0.69, fdr 7e-06); moves opposite to [[C19orf25]] (-0.60, fdr 1e-05), [[EIF5B]] (-0.58, fdr 2e-05), [[ZBTB7A]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ARHGDIB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 0.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.26×** | +16.9 | 0e+00 | 26/27 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.27×** | +16.3 | 0e+00 | 17/17 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.19×** | +12.5 | 1e-33 | 21/23 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +6.8 | 1e-09 | 25/44 (KATO III, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.7 | 4e-04 | 13/44 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.6 | 4e-04 | 2/46 (NCI-H23, AN3 CA) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.1 | 0.003 | 13/34 (SW480, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.7 | 0.015 | 14/33 (CFPAC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.7 | 0.015 | 11/34 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.022 | 8/40 (NCI-H1573, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.027 | 7/41 (SW 900, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.037 | 13/45 (HOP62, HEC-1-A, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.47×** | +3.2 | 0.054 | 8/29 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.071 | 5/44 (Hs 766T, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.31×** | +3.0 | 0.095 | 10/35 (CFPAC-1, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 0.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.632×** | -7.6 | 2e-11 | 23/39 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -5.7 | 5e-06 | 19/39 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.625×** | -5.3 | 2e-05 | 25/43 (COLO 205, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.640×** | -5.2 | 2e-05 | 19/44 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.717×** | -3.9 | 0.010 | 13/44 (NCI-H1573, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.739×** | -3.6 | 0.035 | 13/44 (Hs 766T, NCI-H661, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.741×** | -3.5 | 0.035 | 11/44 (KATO III, SNU-1, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | **0.742×** | -3.2 | 0.081 | 9/43 (HS-578T, HCT15, …) | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **0.761×** | -3.2 | 0.081 | 11/38 (NCI-H460, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 0. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.87 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -11.0) |
| [[A498 (line)]] | wt | 6.54 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +9.5) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 8.65 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.64× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.8) |
| [[A549 (line)]] | wt | 8.79 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.41× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 3.79 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0579× (z -9.3) |
| [[HT-29 (line)]] | alt | 6.76 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0685× (z -11.6) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 8.47 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -8.8) |
| [[RKO (line)]] | wt | 6.56 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0977× (z -8.8) |
| [[SNU-423 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 0), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRAID]] | +0.71 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[SH3BGRL]] | +0.70 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[GSTK1]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SCARB2]] | +0.68 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[FAM210B]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[COX11]] | +0.68 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[FUCA2]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[SCCPDH]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PRDX3]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PLBD1]] | +0.64 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.64 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[SCP2]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf25]] | -0.60 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[EIF5B]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ZBTB7A]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.56 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[FBXL18]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[TPT1-AS1]] | -0.55 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PPP1R13L]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[MIDN]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[POLR2J4]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[RAB11FIP3]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[AXIN1]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[BCAT2]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGDIB]] | B | ARHGDIB activity raises TSPAN6's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.42× lower at baseline in the lines without ARHGDIB | 0.091 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.767). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.7, -19.4); signed map (-20.9, -40.0). **Vector** length 64.8, 11.0% of its response variance represented; |z| ≥ 3 in 792 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +16.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +7.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +12.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +2.7 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +3.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | tetraspanin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:100,627,108-100,639,991 (-) |
| Ensembl biotype | protein_coding |
| Also known as | T245, TSPAN-6; previously TM4SF6 |
| Gene groups (HGNC) | Tetraspanin family |
| Matched by | ensembl_id |

UniProt [O43657](https://www.uniprot.org/uniprotkb/O43657) carries no function annotation.

**Summary**, from NCBI Gene [7105](https://www.ncbi.nlm.nih.gov/gene/7105):

> The protein encoded by this gene is a member of the transmembrane 4 superfamily, also known as the tetraspanin family. Most of these members are cell-surface proteins that are characterized by the presence of four hydrophobic domains. The proteins mediate signal transduction events that play a role in the regulation of cell development, activation, growth and motility. The protein encoded by this gene is a cell surface glycoprotein and is highly similar in sequence to the transmembrane 4 …

**Accessions** — [HGNC:11858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11858) · Entrez [7105](https://www.ncbi.nlm.nih.gov/gene/7105) · UniProt [O43657](https://www.uniprot.org/uniprotkb/O43657) · Ensembl [ENSG00000000003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000000003)

## Data

Gene col 0: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 0); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 0, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 0]; `tensor/DDL_lfc|DDL_z.npy` [0]; `embed/gene_vectors.npy` [0]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 0 or target_col == 0). Every well: [[TSPAN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPAN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
