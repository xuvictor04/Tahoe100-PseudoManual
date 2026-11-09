---
symbol: "C9orf85"
type: "gene"
col: 7906
ensembl_id: "ENSG00000155621"
name: "chromosome 9 open reading frame 85"
location: "9q21.13"
module: 118
arm: "+"
pooled_cpm: 43.66
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# C9orf85

*chromosome 9 open reading frame 85* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.73× (z +15.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.774× (z -5.1, q 2e-04, down in 24 of 47 measured lines) ⚠ toxic. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.233×, RKO 0.331×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.471×, NCI-H460 0.510×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB8OS]] (+0.63, fdr 1e-05), [[ATP6V1E1]] (+0.60, fdr 2e-05), [[PIN4]] (+0.59, fdr 5e-05); moves opposite to [[H2AX]] (-0.54, fdr 5e-05), [[TEDC1]] (-0.53, fdr 2e-04), [[THEM6]] (-0.52, fdr 6e-04).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LYPD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +15.9 | 0e+00 | 42/48 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +15.9 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +15.7 | 0e+00 | 47/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +11.7 | 2e-29 | 45/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +10.9 | 9e-26 | 39/47 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +10.3 | 7e-23 | 43/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +9.3 | 1e-18 | 38/47 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +8.4 | 2e-15 | 33/47 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +8.2 | 2e-14 | 35/48 (HOP62, RKO, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.2 | 2e-14 | 36/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +6.8 | 4e-10 | 38/48 (NCI-H460, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +6.7 | 1e-09 | 22/39 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.6 | 2e-09 | 31/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.22×** | +5.8 | 3e-07 | 21/48 (J82, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +5.4 | 2e-06 | 29/48 (J82, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 8e-06 | 25/47 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 2e-04 | 19/48 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7906.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 9 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (SNU-1 0.233×, RKO 0.331×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.471×, NCI-H460 0.510×; ⚠ cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.774×** | -5.1 | 2e-04 | 24/47 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.801×** | -4.6 | 0.001 | 23/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.825×** | -3.9 | 0.015 | 22/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.819× | -3.4 | 0.11 | 15/48 (PANC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 67.0 | 8 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +16.8) | — |
| [[NCI-H460 (line)]] | wt | 48.7 | 5 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.74× (z +12.8) | [[Digitoxin (drug)]] 0.05 µM 0.419× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 72.7 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 57.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.6) | — |
| [[A-172 (line)]] | wt | 34.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +11.3) | — |
| [[J82 (line)]] | alt | 57.8 | 3 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.20× (z +9.6) | — |
| [[SW480 (line)]] | alt | 53.9 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +12.3) | — |
| [[A498 (line)]] | wt | 57.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 56.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 46.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +14.9) | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.112× (z -11.3) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +10.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.69× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.141× (z -9.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 36.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.471× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.331× (z -8.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 59.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -9.2) ⚠ toxic |
| [[A549 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB8OS]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ATP6V1E1]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[PIN4]] | +0.59 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[GPALPP1]] | +0.59 | +0.67 / +0.39 | both halves | 5e-05 |  |
| [[ZNF529-AS1]] | +0.59 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[VPS13B-DT]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[COPZ1]] | +0.57 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[ALKBH1]] | +0.56 | +0.63 / +0.36 | both halves | 1e-04 |  |
| [[YAE1]] | +0.55 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[SEM1]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MOB4]] | +0.54 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[BMS1P4-1]] | +0.54 | +0.69 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H2AX]] | -0.54 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[TEDC1]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[THEM6]] | -0.52 | -0.50 / -0.22 | both halves | 6e-04 |  |
| [[CBX2]] | -0.52 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[NASP]] | -0.52 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[CELSR2]] | -0.51 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[HYAL2]] | -0.49 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[EIF4A3]] | -0.49 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[LYPD6]] | -0.49 | -0.37 / -0.22 | both halves | 6e-04 |  |
| [[CRY1]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TMEM201]] | -0.47 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[MARCKSL1]] | -0.47 | -0.47 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD6]] | B | LYPD6 activity raises C9orf85's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without LYPD6 | 0.069 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[MTERF1]] | C | MTERF1 activity lowers C9orf85's level | lines that do not express MTERF1 (4) vs lines expressing it (46) | 1.04× higher at baseline in the lines without MTERF1 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with EP300, RNF43, B2M; also absent: TBC1D9, RBMS1, SIX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.402). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-26.9, -10.1); signed map (-2.2, -4.5). **Vector** length 71.3, 14.4% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.0 | +8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.8 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +9.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -0.2 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.9 | +1.4 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | +15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | +11.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.1 | -5.1 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -0.1 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.5 | -1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 9 open reading frame 85 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:71,911,510-71,986,054 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC61599 |
| Matched by | ensembl_id |

UniProt [Q96MD7](https://www.uniprot.org/uniprotkb/Q96MD7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28784) · Entrez [138241](https://www.ncbi.nlm.nih.gov/gene/138241) · UniProt [Q96MD7](https://www.uniprot.org/uniprotkb/Q96MD7) · Ensembl [ENSG00000155621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155621)

## Data

Gene col 7906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7906); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7906]; `tensor/DDL_lfc|DDL_z.npy` [7906]; `embed/gene_vectors.npy` [7906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7906 or target_col == 7906). Every well: [[C9orf85 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C9orf85.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
