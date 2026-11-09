---
symbol: "SLAMF7"
type: "gene"
col: 374
ensembl_id: "ENSG00000026751"
name: "SLAM family member 7"
location: "1q23.3"
module: 125
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 16
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 10
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# SLAMF7

*SLAM family member 7* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.18× (z +10.4, q 1e-22, up in 9 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Citalopram (hydrobromide) (drug)]] 0.05 µM: 0.450× (z -4.1, q 0.023, down in 9 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HS-578T 0.0431×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (HS-578T 0.0620×); [[Budesonide (drug)]] 5 µM in 1 line (HS-578T 0.0860×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ROR1-AS1]] (+0.77, fdr 7e-06), [[ANKRD30B]] (+0.74, fdr 7e-06), [[ENTHD1]] (+0.71, fdr 7e-06); moves opposite to [[PACSIN2]] (-0.57, fdr 3e-05), [[DAAM2]] (-0.56, fdr 1e-05), [[ITGA10]] (-0.55, fdr 1e-04).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CD274]] → it (grade B ⚠); 10 go from it, the strongest it → [[CPD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.18×** | +10.4 | 1e-22 | 9/12 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.14×** | +10.3 | 1e-22 | 4/5 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.18×** | +8.4 | 6e-15 | 3/6 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.88×** | +8.4 | 6e-15 | 3/5 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.14×** | +7.3 | 4e-11 | 7/9 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.48×** | +6.6 | 5e-09 | 8/13 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +6.3 | 2e-08 | 8/14 (CFPAC-1, J82, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +5.4 | 4e-06 | 2/6 (SK-MEL-2, SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +5.4 | 4e-06 | 4/7 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.06×** | +5.1 | 2e-05 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.66×** | +5.0 | 3e-05 | 3/9 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +4.7 | 1e-04 | 2/7 (SW 900, hTERT-HPNE) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.33×** | +4.3 | 6e-04 | 6/10 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.32×** | +4.3 | 7e-04 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.27×** | +4.2 | 1e-03 | 6/9 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.04×** | +4.1 | 0.002 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.16×** | +3.9 | 0.003 | 0/7 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.005 | 1/10 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.008 | 5/12 (A549, A-172, …) | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.96×** | +3.4 | 0.015 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +3.2 | 0.033 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.86×** | +3.2 | 0.034 | 4/12 (SW 900, SK-MEL-2, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 374.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HS-578T 0.0431×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (HS-578T 0.0620×); [[Budesonide (drug)]] 5 µM in 1 line (HS-578T 0.0860×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **0.450×** | -4.1 | 0.023 | 9/14 (HS-578T, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.526× | -3.3 | 0.27 | 7/13 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 18.7 | 0 | 6 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0431× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 16.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +8.9) | — |
| [[A-172 (line)]] | wt | 4.32 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.1× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 3.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.12× (z +8.6) | — |
| [[A-427 (line)]] | wt | 0.143 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.910 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.611 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.575 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.168 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.900 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.157 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.680 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.122 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.164 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.126 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.140 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.141 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROR1-AS1]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ANKRD30B]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ENTHD1]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[LINC02154]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NGF]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SHISAL1]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[PSG4]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 | same gene group |
| [[IGFN1]] | +0.68 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[C12orf50]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TNFRSF9]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 | same gene group; STRING 510 |
| [[HDAC9]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PSG9]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACSIN2]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[DAAM2]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ITGA10]] | -0.55 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[TBC1D8]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SRPX]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[COPS8]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[FN1]] | -0.53 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[CPD]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ZMYND8]] | -0.51 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[UGP2]] | -0.51 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ATP1A1]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 2, C 11. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD274]] | B | CD274 activity raises SLAMF7's level | lines that do not express CD274 (18) vs lines expressing it (32) | 2.04× lower at baseline in the lines without CD274 | 0.060 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[ANKRD20A5P]] | B | ANKRD20A5P activity raises SLAMF7's level | lines that do not express ANKRD20A5P (16) vs lines expressing it (34) | 1.60× lower at baseline in the lines without ANKRD20A5P | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000283294, SH3RF2 |
| [[NAALADL2-AS2]] | C | NAALADL2-AS2 activity raises SLAMF7's level | lines that do not express NAALADL2-AS2 (36) vs lines expressing it (14) | 3.57× lower at baseline in the lines without NAALADL2-AS2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RNF17, ENSG00000287598, SSX1; co-absent with the target |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises SLAMF7's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without ROR1-AS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |
| [[NGF]] | C | NGF activity raises SLAMF7's level | lines that do not express NGF (31) vs lines expressing it (19) | 2.69× lower at baseline in the lines without NGF | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, AMPH, FYB1; co-absent with the target |
| [[CD5L]] | C | CD5L activity raises SLAMF7's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.14× lower at baseline in the lines without CD5L | 0.034 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent; co-absent with the target |
| [[CCN3]] | C | CCN3 activity raises SLAMF7's level | lines that do not express CCN3 (20) vs lines expressing it (30) | 1.94× lower at baseline in the lines without CCN3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SNAI2, FAR2, ENSG00000228033; co-absent with the target |
| [[FN1]] | C | FN1 activity raises SLAMF7's level | lines that do not express FN1 (29) vs lines expressing it (21) | 2.52× lower at baseline in the lines without FN1 | 0.063 | ⚠ within organs, on part of the lines; also absent: PLPP4, ENSG00000234261, IL7R; co-absent with the target |
| [[CSF2]] | C | CSF2 activity raises SLAMF7's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without CSF2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2; co-absent with the target |
| [[PSG4]] | C | PSG4 activity raises SLAMF7's level | lines that do not express PSG4 (40) vs lines expressing it (10) | 2.52× lower at baseline in the lines without PSG4 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PSG9, LINC01242, PSG5; co-absent with the target |
| [[DAAM2]] | C | DAAM2 activity raises SLAMF7's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without DAAM2 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |
| [[GBP5]] | C | GBP5 activity raises SLAMF7's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.17× lower at baseline in the lines without GBP5 | 0.092 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPD]] | B | SLAMF7 activity raises CPD's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 1.31× lower at baseline in the lines without SLAMF7 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[RPLP0P2]] | B | SLAMF7 activity raises RPLP0P2's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without SLAMF7 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[PACSIN2]] | B | SLAMF7 activity raises PACSIN2's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 1.33× lower at baseline in the lines without SLAMF7 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[C12orf50]] | B | SLAMF7 activity raises C12orf50's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without SLAMF7 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[GSDME]] | B | SLAMF7 activity raises GSDME's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.39× lower at baseline in the lines without SLAMF7 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17 |
| [[LYPD1]] | C | SLAMF7 activity raises LYPD1's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.10× lower at baseline in the lines without SLAMF7 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |
| [[ENTHD1]] | C | SLAMF7 activity raises ENTHD1's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.82× lower at baseline in the lines without SLAMF7 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |
| [[DAAM2]] | C | SLAMF7 activity raises DAAM2's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.21× lower at baseline in the lines without SLAMF7 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |
| [[NAALADL2-AS2]] | C | SLAMF7 activity raises NAALADL2-AS2's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without SLAMF7 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |
| [[LINC00973]] | C | SLAMF7 activity raises LINC00973's level | lines that do not express SLAMF7 (34) vs lines expressing it (16) | 2.11× lower at baseline in the lines without SLAMF7 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG4, AMPH, RNF17; co-absent with the target |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, 21.9); signed map (38.5, 23.0). **Vector** length 40.0, 11.9% of its response variance represented; |z| ≥ 3 in 358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +1.1 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.5 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SLAM family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:160,739,057-160,754,821 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRACC, 19A, CS1, CD319 |
| Gene groups (HGNC) | CD molecules; V-set domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ25](https://www.uniprot.org/uniprotkb/Q9NQ25) (SLAM family member 7):

> Self-ligand receptor of the signaling lymphocytic activation molecule (SLAM) family. SLAM receptors triggered by homo- or heterotypic cell-cell interactions are modulating the activation and differentiation of a wide variety of immune cells and thus are involved in the regulation and interconnection of both innate and adaptive immune response. Activities are controlled by presence or absence of small cytoplasmic adapter proteins, SH2D1A/SAP and/or SH2D1B/EAT-2. Isoform 1 mediates NK cell …

**Summary**, from NCBI Gene [57823](https://www.ncbi.nlm.nih.gov/gene/57823):

> Enables identical protein binding activity. Predicted to be involved in T cell activation and immune response. Predicted to act upstream of or within regulation of natural killer cell activation. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21394) · Entrez [57823](https://www.ncbi.nlm.nih.gov/gene/57823) · UniProt [Q9NQ25](https://www.uniprot.org/uniprotkb/Q9NQ25) · Ensembl [ENSG00000026751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026751)

## Data

Gene col 374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 374); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 374]; `tensor/DDL_lfc|DDL_z.npy` [374]; `embed/gene_vectors.npy` [374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 374 or target_col == 374). Every well: [[SLAMF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLAMF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
