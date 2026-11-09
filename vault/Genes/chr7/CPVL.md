---
symbol: "CPVL"
type: "gene"
col: 2715
ensembl_id: "ENSG00000106066"
name: "carboxypeptidase vitellogenic like"
location: "7p14.3"
module: 29
arm: "+"
pooled_cpm: 10.95
n_lines_expressing: 29
n_dd_up: 25
n_dd_down: 9
n_dd_up_clean: 20
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CPVL

*carboxypeptidase vitellogenic like* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.46× (z +14.6, q 1e-45, up in 15 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +11.9, q 2e-30, up in 15 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.572× (z -6.3, q 2e-07, down in 16 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASAH1]] (+0.59, fdr 1e-05), [[CTSH]] (+0.57, fdr 1e-05), [[PPP1R3B-DT]] (+0.57, fdr 3e-05); moves opposite to [[DLGAP4]] (-0.46, fdr 5e-05), [[CCM2]] (-0.45, fdr 1e-04), [[RNF34]] (-0.45, fdr 8e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[UGT8]] → it (grade B ⚠); 5 go from it, the strongest it → [[DNASE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +14.6 | 1e-45 | 15/18 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +14.2 | 5e-43 | 10/11 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +11.9 | 2e-30 | 15/27 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +11.3 | 3e-27 | 22/27 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.81×** | +11.3 | 3e-27 | 15/16 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +7.7 | 1e-12 | 17/26 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +5.9 | 4e-07 | 15/26 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.6 | 2e-06 | 9/26 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +5.6 | 2e-06 | 8/24 (CFPAC-1, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +5.3 | 6e-06 | 14/26 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.3 | 6e-06 | 7/27 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.2 | 1e-05 | 5/26 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 5e-04 | 12/26 (KATO III, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 5e-04 | 16/26 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.41×** | +4.3 | 8e-04 | 14/27 (HEC-1-A, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.016 | 7/26 (H4, HEC-1-A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.018 | 7/27 (AsPC-1, RKO, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.035 | 4/26 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.043 | 6/26 (LOX-IMVI, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.572×** | -6.3 | 2e-07 | 16/26 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.601×** | -6.0 | 6e-07 | 18/26 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.715×** | -5.6 | 5e-06 | 17/26 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -4.7 | 4e-04 | 18/26 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.768×** | -4.4 | 0.001 | 13/26 (HCT15, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.714×** | -3.9 | 0.007 | 11/26 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.729×** | -3.7 | 0.017 | 10/26 (C32, Panc 03.27, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.747×** | -3.4 | 0.041 | 11/26 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.041 | 13/26 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -17.8) |
| [[C32 (line)]] | wt | 19.5 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0659× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0723× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 122 | 2 | 2 (2 ⚠) | [[Cepharanthine (drug)]] 5 µM 1.78× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.452× (z -9.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -9.2) |
| [[KATO III (line)]] | alt | 18.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0505× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 31.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -11.5) |
| [[SW1417 (line)]] | alt | 6.22 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0942× (z -9.8) |
| [[A-172 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASAH1]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CTSH]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PPP1R3B-DT]] | +0.57 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[GSTK1]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[CFI]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[MAP2K6]] | +0.51 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[PPT1]] | +0.50 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[MACROD2]] | +0.50 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[C10orf90]] | +0.50 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[NTRK2]] | +0.50 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[TSPAN6]] | +0.49 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[SH3BGRL]] | +0.49 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP4]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[CCM2]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RNF34]] | -0.45 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[GPSM1]] | -0.45 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[ZNF696]] | -0.44 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[CLCF1]] | -0.43 | -0.40 / -0.46 | both halves | 4e-05 |  |
| [[C11orf91]] | -0.43 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ATP6V0A2]] | -0.43 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[KCTD5]] | -0.43 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[ELOVL1]] | -0.43 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[SETX]] | -0.42 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[PREB]] | -0.42 | -0.41 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT8]] | B | UGT8 activity raises CPVL's level | lines that do not express UGT8 (21) vs lines expressing it (29) | 1.35× lower at baseline in the lines without UGT8 | 0.083 | ⚠ within organs, on part of the lines; also absent: CCSER1, JPH1, ABO |
| [[NTRK2]] | C | NTRK2 activity raises CPVL's level | lines that do not express NTRK2 (28) vs lines expressing it (22) | 1.66× lower at baseline in the lines without NTRK2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANKRD20A9P, ONECUT3, LINC00408; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DNASE2]] | B | CPVL activity lowers DNASE2's level | lines that do not express CPVL (21) vs lines expressing it (29) | 1.32× higher at baseline in the lines without CPVL | 0.036 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1 |
| [[CRTAP]] | B | CPVL activity lowers CRTAP's level | lines that do not express CPVL (21) vs lines expressing it (29) | 1.32× higher at baseline in the lines without CPVL | 0.075 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1 |
| [[UGT8]] | B | CPVL activity raises UGT8's level | lines that do not express CPVL (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without CPVL | 0.089 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1 |
| [[SELENOP]] | B | CPVL activity raises SELENOP's level | lines that do not express CPVL (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without CPVL | 0.095 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1 |
| [[NTRK2]] | C | CPVL activity raises NTRK2's level | lines that do not express CPVL (21) vs lines expressing it (29) | 1.90× lower at baseline in the lines without CPVL | 0.098 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (31.6, 57.2); signed map (60.2, -4.9). **Vector** length 60.9, 13.8% of its response variance represented; |z| ≥ 3 in 639 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +14.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.9 | +7.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | carboxypeptidase vitellogenic like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:28,995,235-29,195,451 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3G5](https://www.uniprot.org/uniprotkb/Q9H3G5) (Probable serine carboxypeptidase CPVL):

> May be involved in the digestion of phagocytosed particles in the lysosome, participation in an inflammatory protease cascade, and trimming of peptides for antigen presentation.

**Summary**, from NCBI Gene [54504](https://www.ncbi.nlm.nih.gov/gene/54504):

> The protein encoded by this gene is a carboxypeptidase and bears strong sequence similarity to serine carboxypeptidases. Carboxypeptidases are a large class of proteases that act to cleave a single amino acid from the carboxy termini of proteins or peptides. The exact function of this protein, however, has not been determined. [provided by RefSeq, Jan 2017]

**Accessions** — [HGNC:14399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14399) · Entrez [54504](https://www.ncbi.nlm.nih.gov/gene/54504) · UniProt [Q9H3G5](https://www.uniprot.org/uniprotkb/Q9H3G5) · Ensembl [ENSG00000106066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106066)

## Data

Gene col 2715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2715); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2715]; `tensor/DDL_lfc|DDL_z.npy` [2715]; `embed/gene_vectors.npy` [2715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2715 or target_col == 2715). Every well: [[CPVL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPVL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
