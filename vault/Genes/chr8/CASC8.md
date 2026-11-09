---
symbol: "CASC8"
type: "gene"
col: 14458
ensembl_id: "ENSG00000246228"
name: "cancer susceptibility 8"
location: "8q24.21"
module: 75
arm: "+"
pooled_cpm: 5.09
n_lines_expressing: 30
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# CASC8

*cancer susceptibility 8* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.06× (z +21.0, q 0e+00, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.587× (z -5.7, q 8e-06, down in 17 of 26 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASC19]] (+0.72, fdr 7e-06), [[CASC11]] (+0.67, fdr 7e-06), [[NINJ2]] (+0.60, fdr 3e-05); moves opposite to [[ANKMY2]] (-0.53, fdr 1e-04), [[IFT52]] (-0.52, fdr 2e-04), [[ALAD]] (-0.50, fdr 1e-04).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PPP1R1C]] → it (grade B ⚠); 7 go from it, the strongest it → [[BCL2L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.06×** | +21.0 | 0e+00 | 16/23 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.02×** | +11.7 | 4e-29 | 20/26 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +11.1 | 3e-26 | 6/12 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +10.7 | 9e-25 | 4/8 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +9.6 | 9e-20 | 1/5 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +7.9 | 4e-13 | 8/26 (A498, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +5.8 | 5e-07 | 6/25 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.1 | 3e-05 | 6/26 (SW480, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 4e-04 | 7/25 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.3 | 0.001 | 1/16 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.006 | 0/19 | top dose only | cell-cycle shift (explains ~5% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.8 | 0.006 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.6 | 0.016 | 0/7 | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.025 | 3/23 (HCT15, RKO, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.3 | 0.037 | 1/18 (NCI-H2347) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.071 | 0/21 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.094 | 0/22 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.587×** | -5.7 | 8e-06 | 17/26 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.632×** | -4.7 | 8e-04 | 14/26 (SW1417, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.678×** | -4.2 | 0.006 | 17/26 (SW1417, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.687×** | -3.7 | 0.029 | 6/26 (Hs 766T, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.712×** | -3.4 | 0.068 | 7/26 (Hs 766T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.804×** | -3.3 | 0.085 | 16/25 (HCT15, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.05 µM |  | 0.737× | -3.1 | 0.16 | 1/25 (NCI-H2347) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.744× | -3.0 | 0.17 | 5/26 (SHP-77, A-427, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 51.9 | 0 | 5 | — | [[Cobimetinib (drug)]] 5 µM 0.0462× (z -11.8) |
| [[SW1417 (line)]] | alt | 31.9 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0647× (z -16.3) |
| [[RKO (line)]] | wt | 28.8 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.239× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.165× (z -9.2) |
| [[A498 (line)]] | wt | 1.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.96× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 4.77 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0734× (z -8.9) |
| [[KATO III (line)]] | alt | 5.31 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0928× (z -9.1) |
| [[LoVo (line)]] | wt | 4.32 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0845× (z -10.0) |
| [[A-172 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.976 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC19]] | +0.72 | +0.76 / +0.66 | both halves | 7e-06 | same gene group |
| [[CASC11]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 | same gene group |
| [[NINJ2]] | +0.60 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CCDC26]] | +0.58 | +0.30 / +0.65 | both halves | 2e-04 | same gene group |
| [[ZNF503-AS1]] | +0.57 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[LINC01811]] | +0.56 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[SLC4A10]] | +0.56 | +0.22 / +0.65 | both halves | 6e-04 |  |
| [[SP2-AS1]] | +0.56 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[SLC20A2]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[SLFNL1-AS1]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[B3GALT1-AS1]] | +0.55 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[CFAP92]] | +0.54 | +0.45 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKMY2]] | -0.53 | -0.49 / -0.32 | both halves | 1e-04 |  |
| [[IFT52]] | -0.52 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[ALAD]] | -0.50 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[ACTR10]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[FPGT]] | -0.47 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[NSL1]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[CNEP1R1]] | -0.47 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[PLD2]] | -0.46 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R1C]] | B | PPP1R1C activity strengthens CASC8's drug response | lines that do not express PPP1R1C (6) vs lines expressing it (20) | the lines without PPP1R1C respond 0.54× as strongly (z diff +1.15); strongest at Idarubicin (hydrochloride) 5 µM: 0.82x vs 3.49x (z diff +7.1) | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[SFTA1P]] | B | SFTA1P activity raises CASC8's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 1.45× lower at baseline in the lines without SFTA1P | 0.050 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[HDAC6]] | B | HDAC6 activity raises CASC8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CASC19]] | C | CASC19 activity raises CASC8's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 3.21× lower at baseline in the lines without CASC19 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4; co-absent with the target |
| [[PDE11A]] | C | PDE11A activity lowers CASC8's level | lines that do not express PDE11A (4) vs lines expressing it (46) | 3.94× higher at baseline in the lines without PDE11A | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: XIRP2, ENSG00000214803, ENSG00000228566; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2L1]] | B | CASC8 activity raises BCL2L1's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 2.21× lower at baseline in the lines without CASC8 | 0.047 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent |
| [[C12orf56]] | B | CASC8 activity lowers C12orf56's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 1.44× higher at baseline in the lines without CASC8 | 0.098 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent |
| [[CASC19]] | C | CASC8 activity raises CASC19's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 6.05× lower at baseline in the lines without CASC8 | 0.006 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent; co-absent with the target |
| [[SYK]] | C | CASC8 activity raises SYK's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 4.90× lower at baseline in the lines without CASC8 | 0.028 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent; co-absent with the target |
| [[TNFSF15]] | C | CASC8 activity raises TNFSF15's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 3.41× lower at baseline in the lines without CASC8 | 0.031 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent; co-absent with the target |
| [[LINC02832]] | C | CASC8 activity raises LINC02832's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 2.09× lower at baseline in the lines without CASC8 | 0.095 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent; co-absent with the target |
| [[DMKN]] | C | CASC8 activity raises DMKN's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 2.71× lower at baseline in the lines without CASC8 | 0.096 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.8, 21.3); signed map (28.7, 2.0). **Vector** length 48.3, 9.11% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +21.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -3.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cancer susceptibility 8 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.21 — chr8:127,289,808-127,482,139 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LINC00860, CARLo-1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45129) · Entrez [727677](https://www.ncbi.nlm.nih.gov/gene/727677) · Ensembl [ENSG00000246228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246228)

## Data

Gene col 14458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14458); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14458]; `tensor/DDL_lfc|DDL_z.npy` [14458]; `embed/gene_vectors.npy` [14458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14458 or target_col == 14458). Every well: [[CASC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
