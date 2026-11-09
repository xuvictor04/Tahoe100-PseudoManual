---
symbol: "ZNF710-AS1"
type: "gene"
col: 15182
ensembl_id: "ENSG00000259291"
name: "ZNF710 antisense RNA 1"
location: "15q26.1"
module: 40
arm: "+"
pooled_cpm: 5.39
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ZNF710-AS1

*ZNF710 antisense RNA 1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.16× (z +11.3, q 4e-27, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.366× (z -14.8, q 0e+00, down in 29 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IDH2]] (+0.77, fdr 7e-06, ⚠ same locus), [[KDELR1]] (+0.70, fdr 8e-06), [[MED26]] (+0.69, fdr 1e-05), [[SRP54-AS1]] (+0.69, fdr 1e-05); moves opposite to [[COA7]] (-0.69, fdr 1e-05), [[RTL6]] (-0.65, fdr 1e-05), [[ZNF480]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[TRIM16L-1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +11.3 | 4e-27 | 29/39 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +8.6 | 2e-15 | 3/9 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.2 | 8e-08 | 11/27 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +5.3 | 1e-05 | 14/35 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.005 | 14/37 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.076 | 13/45 (A-172, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.36× | +3.2 | 0.11 | 3/29 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.34× | +3.0 | 0.17 | 9/46 (HOP62, BT-474, …) | all doses, flat | cell-cycle shift (explains ~8% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15182.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.366×** | -14.8 | 0e+00 | 29/37 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.285×** | -12.6 | 8e-34 | 33/40 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.318×** | -11.9 | 2e-30 | 31/37 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.423×** | -8.9 | 5e-17 | 29/44 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.425×** | -8.9 | 6e-17 | 30/46 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.475×** | -7.7 | 9e-13 | 24/42 (SHP-77, KATO III, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.476×** | -7.7 | 9e-13 | 26/43 (HepG2/C3A, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.562×** | -6.0 | 2e-07 | 20/45 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -5.7 | 8e-07 | 22/43 (hTERT-HPNE, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.593×** | -5.4 | 3e-06 | 21/35 (J82, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.600×** | -5.3 | 6e-06 | 18/45 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.614×** | -5.1 | 2e-05 | 18/42 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.629×** | -4.6 | 2e-04 | 16/41 (J82, C-33 A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.428×** | -4.6 | 2e-04 | 13/35 (KATO III, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.636×** | -4.5 | 2e-04 | 16/31 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.694×** | -3.8 | 0.005 | 12/47 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.712×** | -3.5 | 0.014 | 18/43 (HepG2/C3A, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -3.4 | 0.023 | 11/40 (HOP62, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 9.37 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -16.7) |
| [[A-172 (line)]] | wt | 8.82 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -21.7) |
| [[LoVo (line)]] | wt | 7.11 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0778× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 8.11 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -11.6) |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -11.6) |
| [[SW480 (line)]] | alt | 6.48 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0792× (z -13.2) |
| [[HT-29 (line)]] | alt | 11.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -12.7) |
| [[J82 (line)]] | alt | 5.08 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -9.4) |
| [[KATO III (line)]] | alt | 5.32 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0524× (z -12.0) |
| [[LS 180 (line)]] | wt | 9.29 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.6) |
| [[PANC-1 (line)]] | alt | 7.07 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -17.0) |
| [[A498 (line)]] | wt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.6) | — |
| [[A549 (line)]] | wt | 5.52 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0600× (z -10.7) |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 2.79 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0285× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 4.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 3.92 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0733× (z -8.7) |
| [[A-427 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDH2]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.8 kb, same strand: neighbours can correlate without regulation) |
| [[KDELR1]] | +0.70 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[MED26]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 | same gene group |
| [[TBC1D22A-DT]] | +0.67 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[APAF1]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TMEM50B]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[DNAJC4]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DPM1]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[GMCL1]] | +0.61 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[GOLT1B]] | +0.60 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[IFI27L1]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA7]] | -0.69 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[RTL6]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ZNF480]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[ATXN7L1]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.61 | -0.36 / -0.70 | both halves | 9e-05 |  |
| [[MRPL47]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CIAO1]] | -0.60 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.60 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.60 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[COMMD10]] | -0.60 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ZNF518B]] | -0.59 | -0.43 / -0.65 | both halves | 3e-05 |  |
| [[ASF1A]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF710-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CREB3L1]] | B | CREB3L1 activity raises ZNF710-AS1's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without CREB3L1 | 0.032 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |
| [[IDH2]] | C | IDH2's natural level strengthens ZNF710-AS1's drug response | IDH2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.57; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM16L-1]] | C | ZNF710-AS1's natural level strengthens TRIM16L-1's drug response | ZNF710-AS1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.29; direction not clear | 0.038 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ZXDB]] | C | ZNF710-AS1's natural level strengthens ZXDB's drug response | ZNF710-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.26; direction not clear | 0.041 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.667). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (5.3, -18.8); signed map (-42.3, 14.2). **Vector** length 63.7, 9.72% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.2 | +0.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -12.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -7.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ZNF710 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.1 — chr15:90,074,512-90,082,207 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000558334 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53141) · Entrez [109729181](https://www.ncbi.nlm.nih.gov/gene/109729181) · Ensembl [ENSG00000259291](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259291)

## Data

Gene col 15182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15182); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15182]; `tensor/DDL_lfc|DDL_z.npy` [15182]; `embed/gene_vectors.npy` [15182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15182 or target_col == 15182). Every well: [[ZNF710-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF710-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
