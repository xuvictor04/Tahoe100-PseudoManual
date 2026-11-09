---
symbol: "TCTN1"
type: "gene"
col: 12926
ensembl_id: "ENSG00000204852"
name: "tectonic family member 1"
location: "12q24.11"
module: 64
arm: "+"
pooled_cpm: 10.08
n_lines_expressing: 47
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# TCTN1

*tectonic family member 1* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +10.8, q 1e-24, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.416× (z -10.1, q 2e-21, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATB]] (+0.73, fdr 7e-06), [[USP40]] (+0.70, fdr 8e-06), [[NUDT9]] (+0.68, fdr 7e-06); moves opposite to [[KIAA1958]] (-0.62, fdr 1e-05), [[EXTL3]] (-0.62, fdr 1e-05), [[PDXP]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 2 go from it, the strongest it → [[EXTL3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +10.8 | 1e-24 | 28/43 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +8.8 | 3e-16 | 14/20 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +7.8 | 1e-12 | 28/45 (LoVo, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.9 | 7e-10 | 24/33 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +6.6 | 6e-09 | 16/24 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +6.0 | 2e-07 | 28/45 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.51×** | +4.8 | 1e-04 | 16/45 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 4e-04 | 18/42 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 6e-04 | 20/45 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.4 | 6e-04 | 20/44 (A-427, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.2 | 0.002 | 12/34 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.005 | 11/44 (SW480, SHP-77, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.82×** | +3.6 | 0.012 | 13/38 (A549, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.051 | 9/44 (SW480, NCI-H2030, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.057 | 11/45 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.067 | 7/45 (SW480, SNU-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.416×** | -10.1 | 2e-21 | 34/45 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.485×** | -8.4 | 2e-14 | 32/43 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -7.9 | 7e-13 | 26/40 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.517×** | -7.6 | 4e-12 | 30/44 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.630×** | -5.3 | 1e-05 | 19/45 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.730×** | -5.1 | 3e-05 | 26/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.448×** | -4.8 | 1e-04 | 16/40 (SW480, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.690×** | -4.3 | 0.001 | 17/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.691×** | -4.3 | 0.001 | 16/43 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.002 | 14/43 (A498, NCI-H1792, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.708×** | -4.0 | 0.004 | 14/45 (SNU-1, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.712×** | -3.9 | 0.004 | 11/45 (PANC-1, SW1417, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.539×** | -3.7 | 0.008 | 17/39 (NCI-H23, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.817×** | -3.3 | 0.040 | 18/45 (SNU-1, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.755×** | -3.1 | 0.068 | 12/44 (COLO 205, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.9 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -11.5) |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -9.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 11.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0716× (z -9.6) |
| [[A-427 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 8.24 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0657× (z -9.0) |
| [[J82 (line)]] | alt | 8.25 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 8.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 8.64 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0865× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 8.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 7.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +9.9) | — |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.813 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATB]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[USP40]] | +0.70 | +0.76 / +0.58 | both halves | 8e-06 |  |
| [[NUDT9]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CUL5]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MRPL9]] | +0.67 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PMPCB]] | +0.67 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[MTHFSD]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[FAM204A]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[U2SURP]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZXDA]] | +0.64 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[POLR2M]] | +0.64 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[ANKEF1]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | -0.62 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[EXTL3]] | -0.62 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[PDXP]] | -0.61 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[SRGAP2D]] | -0.61 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[B3GAT3]] | -0.61 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SLC37A3]] | -0.58 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[RELL1]] | -0.57 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[EEF1AKMT4]] | -0.57 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[TMEM184B]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TCTN1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ZNF512B]] | B | ZNF512B activity raises TCTN1's level | lines that do not express ZNF512B (10) vs lines expressing it (40) | 2.05× lower at baseline in the lines without ZNF512B | 0.069 | ⚠ within organs, on part of the lines; also absent: HLTF, FERMT2, DNAAF9; maybe low, not absent |
| [[CCDC102A]] | C | CCDC102A activity raises TCTN1's level | lines that do not express CCDC102A (5) vs lines expressing it (45) | 3.24× lower at baseline in the lines without CCDC102A | 0.013 | ⚠ within organs, on part of the lines; also absent: CYP46A1, TMOD2, DPF1; maybe low, not absent; co-absent with the target |
| [[GDAP1]] | C | GDAP1 activity raises TCTN1's level | lines that do not express GDAP1 (6) vs lines expressing it (44) | 2.34× lower at baseline in the lines without GDAP1 | 0.030 | ⚠ within organs, on part of the lines; also absent: HHAT, PHC1, LINC00888; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EXTL3]] | C | TCTN1 activity lowers EXTL3's level | lines that do not express TCTN1 (3) vs lines expressing it (47) | 2.00× higher at baseline in the lines without TCTN1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, PHC1, DNAJC18; maybe low, not absent; its own permutation p |
| [[SRGAP2]] | C | TCTN1 activity raises SRGAP2's level | lines that do not express TCTN1 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without TCTN1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DPF1, PHC1, DNAJC18; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.6, 4.7); signed map (8.6, -31.9). **Vector** length 78.5, 14.9% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +10.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.4 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +4.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -7.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | tectonic family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:110,614,027-110,663,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21127, TECT1, JBTS13 |
| Gene groups (HGNC) | Tectonic proteins; MKS complex |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2MV58](https://www.uniprot.org/uniprotkb/Q2MV58) (Tectonic-1):

> Component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Regulator of Hedgehog (Hh), required for both activation and inhibition of the Hh pathway in the patterning of the neural tube. During neural tube development, it is required for formation of the most ventral cell types and for full Hh pathway activation. Functions in Hh signal …

**Summary**, from NCBI Gene [79600](https://www.ncbi.nlm.nih.gov/gene/79600):

> This gene encodes a member of a family of secreted and transmembrane proteins. The orthologous gene in mouse functions downstream of smoothened and rab23 to modulate hedgehog signal transduction. This protein is a component of the tectonic-like complex, which forms a barrier between the ciliary axoneme and the basal body. A mutation in this gene was found in a family with Joubert syndrome-13. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:26113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26113) · Entrez [79600](https://www.ncbi.nlm.nih.gov/gene/79600) · UniProt [Q2MV58](https://www.uniprot.org/uniprotkb/Q2MV58) · Ensembl [ENSG00000204852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204852)

## Data

Gene col 12926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12926); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12926]; `tensor/DDL_lfc|DDL_z.npy` [12926]; `embed/gene_vectors.npy` [12926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12926 or target_col == 12926). Every well: [[TCTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
