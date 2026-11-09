---
symbol: "APBB1"
type: "gene"
col: 9281
ensembl_id: "ENSG00000166313"
name: "amyloid beta precursor protein binding family B member 1"
location: "11p15.4"
module: 61
arm: "+"
pooled_cpm: 5.86
n_lines_expressing: 39
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# APBB1

*amyloid beta precursor protein binding family B member 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.04× (z +8.7, q 1e-15, up in 22 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.535× (z -7.4, q 1e-10, down in 21 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTX3]] (+0.60, fdr 3e-05), [[KIF5A]] (+0.59, fdr 1e-05), [[ADAP2]] (+0.58, fdr 1e-05); moves opposite to [[HDAC4]] (-0.54, fdr 1e-05), [[URB1]] (-0.49, fdr 5e-05), [[TRAPPC9]] (-0.49, fdr 6e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CCDC136]] → it (grade B ⚠); 7 go from it, the strongest it → [[ZNF555]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +8.7 | 1e-15 | 22/35 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +8.2 | 6e-14 | 13/33 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +7.0 | 4e-10 | 14/37 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +6.8 | 2e-09 | 16/33 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +6.4 | 2e-08 | 11/36 (HOP62, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.70×** | +4.6 | 4e-04 | 8/31 (A-427, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 0.001 | 7/36 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +4.0 | 0.004 | 6/32 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.004 | 5/36 (PANC-1, SW480, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.9 | 0.005 | 5/34 (RPMI-7951, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.006 | 7/24 (HOP62, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.7 | 0.011 | 4/9 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.050 | 5/34 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.2 | 0.050 | 6/22 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.056 | 0/35 | rises with dose | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.064 | 4/35 (A549, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -7.4 | 1e-10 | 21/33 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.641×** | -5.4 | 1e-05 | 14/34 (SNU-423, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.621×** | -5.3 | 2e-05 | 14/36 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.656×** | -5.2 | 3e-05 | 15/36 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.727×** | -3.9 | 0.011 | 10/34 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.743×** | -3.5 | 0.044 | 9/27 (A549, NCI-H1792, …) | top dose only |  |
| [[Clotrimazole (drug)]] 5 µM |  | **0.823×** | -3.4 | 0.063 | 9/37 (A-172, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.776× | -3.1 | 0.14 | 5/36 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.780× | -3.0 | 0.15 | 6/36 (A549, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.8) |
| [[A-427 (line)]] | wt | 19.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 21.4 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0766× (z -8.7) |
| [[LoVo (line)]] | wt | 1.75 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +11.6) | — |
| [[A498 (line)]] | wt | 3.82 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 9.56 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0644× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[Hs 766T (line)]] | wt | 6.03 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0933× (z -8.5) ⚠ cell-cycle shift, explains ~61% of this change |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.758 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTX3]] | +0.60 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[KIF5A]] | +0.59 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[ADAP2]] | +0.58 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ZFP37]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PAPLN]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[UBE2Q2P1]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[CAMSAP3]] | +0.55 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SRSF12]] | +0.54 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[CHRNA7]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[TBKBP1]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[RNFT1]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[BTG3]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC4]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[URB1]] | -0.49 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[TRAPPC9]] | -0.49 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[PIGN]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ATR]] | -0.46 | -0.35 / -0.50 | both halves | 1e-04 | pathway: DNA Double-Strand Break Repair |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC136]] | B | CCDC136 activity raises APBB1's level | lines that do not express CCDC136 (10) vs lines expressing it (40) | 2.93× lower at baseline in the lines without CCDC136 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, RECK, ENSG00000267405; maybe low, not absent |
| [[REEP2]] | B | REEP2 activity raises APBB1's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 2.41× lower at baseline in the lines without REEP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[CD72]] | C | CD72 activity raises APBB1's level | lines that do not express CD72 (3) vs lines expressing it (47) | 2.04× lower at baseline in the lines without CD72 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TCF7, DUSP19, MIR4435-2HG; maybe low, not absent; its own permutation p |
| [[DNAJC18]] | C | DNAJC18 activity raises APBB1's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 3.05× lower at baseline in the lines without DNAJC18 | 0.091 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF555]] | B | APBB1 activity raises ZNF555's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without APBB1 | 0.022 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[CCDC136]] | B | APBB1 activity raises CCDC136's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without APBB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[FAM161A]] | B | APBB1 activity raises FAM161A's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 2.28× lower at baseline in the lines without APBB1 | 0.043 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[PGBD1]] | B | APBB1 activity raises PGBD1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without APBB1 | 0.062 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[YAE1]] | B | APBB1 activity raises YAE1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without APBB1 | 0.074 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[FEZ1]] | B | APBB1 activity raises FEZ1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without APBB1 | 0.091 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[CYP2U1]] | B | APBB1 activity raises CYP2U1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without APBB1 | 0.096 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.388). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, 35.9); signed map (24.8, 20.4). **Vector** length 57.4, 9.68% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +4.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -2.4 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -5.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding family B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:6,395,125-6,419,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Fe65; previously RIR |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 4 pathways, smallest: Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks; DNA Double Strand Break Response; DNA Double-Strand Break Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [O00213](https://www.uniprot.org/uniprotkb/O00213) (Amyloid beta precursor protein binding family B member 1):

> Transcription coregulator that can have both coactivator and corepressor functions. Adapter protein that forms a transcriptionally active complex with the gamma-secretase-derived amyloid precursor protein (APP) intracellular domain. Plays a central role in the response to DNA damage by translocating to the nucleus and inducing apoptosis. May act by specifically recognizing and binding histone H2AX phosphorylated on 'Tyr-142' (H2AXY142ph) at double-strand breaks (DSBs), recruiting other …

**Summary**, from NCBI Gene [322](https://www.ncbi.nlm.nih.gov/gene/322):

> The protein encoded by this gene is a member of the Fe65 protein family. It is an adaptor protein localized in the nucleus. It interacts with the Alzheimer's disease amyloid precursor protein (APP), transcription factor CP2/LSF/LBP1 and the low-density lipoprotein receptor-related protein. APP functions as a cytosolic anchoring site that can prevent the gene product's nuclear translocation. This encoded protein could play an important role in the pathogenesis of Alzheimer's disease. It is …

**Accessions** — [HGNC:581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:581) · Entrez [322](https://www.ncbi.nlm.nih.gov/gene/322) · UniProt [O00213](https://www.uniprot.org/uniprotkb/O00213) · Ensembl [ENSG00000166313](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166313)

## Data

Gene col 9281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9281); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9281]; `tensor/DDL_lfc|DDL_z.npy` [9281]; `embed/gene_vectors.npy` [9281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9281 or target_col == 9281). Every well: [[APBB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APBB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
