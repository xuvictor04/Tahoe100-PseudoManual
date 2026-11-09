---
symbol: "TMEM63C"
type: "gene"
col: 9143
ensembl_id: "ENSG00000165548"
name: "transmembrane protein 63C"
location: "14q24.3"
module: 85
arm: "+"
pooled_cpm: 8.2
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 11
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# TMEM63C

*transmembrane protein 63C* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.84× (z +15.1, q 0e+00, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.609× (z -7.2, q 2e-10, down in 22 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.65, fdr 6e-05), [[SLC29A4]] (+0.65, fdr 4e-05), [[PNKD]] (+0.64, fdr 1e-05); moves opposite to [[PSMD6-AS1]] (-0.61, fdr 5e-05), [[EFCAB2]] (-0.59, fdr 1e-04), [[PSME3IP1]] (-0.59, fdr 3e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MCF2L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9143.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.84×** | +15.1 | 0e+00 | 37/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.50×** | +13.2 | 1e-37 | 32/47 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +12.5 | 2e-33 | 39/47 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.36×** | +12.4 | 2e-33 | 38/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +12.1 | 7e-32 | 35/46 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +9.7 | 2e-20 | 24/35 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +7.7 | 8e-13 | 19/47 (A549, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.9 | 3e-10 | 20/44 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +6.5 | 4e-09 | 21/41 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +6.0 | 1e-07 | 18/44 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 8e-06 | 10/39 (BT-474, HCT15, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.43×** | +5.2 | 9e-06 | 11/28 (Hs 766T, J82, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +4.8 | 5e-05 | 10/44 (NCI-H2347, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.41×** | +4.8 | 7e-05 | 4/15 (HOP62, NCI-H2347, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +4.7 | 9e-05 | 6/32 (A-427, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 5e-04 | 5/36 (SHP-77, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.004 | 12/43 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.004 | 6/36 (SW480, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9143.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -7.2 | 2e-10 | 22/45 (SW 900, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.611×** | -7.2 | 2e-10 | 23/47 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.667×** | -5.8 | 1e-06 | 17/44 (NCI-H23, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.399×** | -5.3 | 2e-05 | 13/44 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.776×** | -5.2 | 2e-05 | 18/43 (NCI-H2030, HOP62, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.724×** | -4.7 | 3e-04 | 17/44 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -4.5 | 5e-04 | 11/41 (SW480, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.736×** | -4.5 | 6e-04 | 10/46 (SW 1271, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.769×** | -3.8 | 0.008 | 18/45 (H4, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.782×** | -3.6 | 0.019 | 14/40 (SW 900, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.797×** | -3.3 | 0.047 | 8/46 (HT-29, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9143. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 7.73 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.48× (z +10.5) | — |
| [[SW480 (line)]] | alt | 13.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.4) | — |
| [[A-172 (line)]] | wt | 8.11 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0618× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 5.59 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.09× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0873× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.101× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.116× (z -10.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 13.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.91× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 4.54 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.92× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 14.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +8.8) | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9143), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.65 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[SLC29A4]] | +0.65 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[PNKD]] | +0.64 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SMARCD3]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[RASAL1]] | +0.62 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[FOXO6]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[RAC3]] | +0.61 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[PRR5]] | +0.61 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[SUSD4]] | +0.61 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[CFD]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[RGS14]] | +0.60 | +0.32 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | -0.61 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[EFCAB2]] | -0.59 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.59 | -0.29 / -0.60 | both halves | 3e-04 |  |
| [[RFX3-DT]] | -0.59 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[EIF4G2]] | -0.57 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[ST7L]] | -0.57 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[UBE3B]] | -0.57 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TUG1]] | -0.56 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | -0.56 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[GEN1]] | -0.55 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[PBLD]] | -0.55 | -0.40 / -0.40 | both halves | 4e-05 |  |
| [[RC3H2]] | -0.55 | -0.39 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCF2L]] | B | MCF2L activity raises TMEM63C's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without MCF2L | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[SBK1]] | B | SBK1 activity raises TMEM63C's level | lines that do not express SBK1 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without SBK1 | 0.031 | ⚠ within organs, on part of the lines; also absent: CASZ1, LAMP3, CAMSAP3 |
| [[SMPDL3B]] | B | SMPDL3B activity raises TMEM63C's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.73× lower at baseline in the lines without SMPDL3B | 0.062 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[SLC29A4]] | B | SLC29A4 activity raises TMEM63C's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.76× lower at baseline in the lines without SLC29A4 | 0.065 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[SNCG]] | B | SNCG activity raises TMEM63C's level | lines that do not express SNCG (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without SNCG | 0.079 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[FGFR4]] | B | FGFR4 activity raises TMEM63C's level | lines that do not express FGFR4 (11) vs lines expressing it (39) | 1.92× lower at baseline in the lines without FGFR4 | 0.094 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, PATJ, LLGL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (8.6, -3.8); signed map (-23.3, 31.3). **Vector** length 60.8, 8.99% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +12.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +6.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +13.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +5.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.3 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 63C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,116,568-77,259,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434P0111, CSC1, hsCSC1; previously C14orf171 |
| Gene groups (HGNC) | TMEM63 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1W3](https://www.uniprot.org/uniprotkb/Q9P1W3) (Osmosensitive cation channel TMEM63C):

> Acts as an osmosensitive cation channel preferentially activated upon hypotonic stress. In contrast to TMEM63B, does not show phospholipid scramblase activity. Enriched in mitochondria-ER contact sites where it may regulate the metabolite flux and organelles' morphologies in response to osmotic changes. In particular may regulate mitochondrial motility and function in motor neuron axons. Required for the functional integrity of the kidney glomerular filtration barrier (By similarity).

**Summary**, from NCBI Gene [57156](https://www.ncbi.nlm.nih.gov/gene/57156):

> Enables calcium-activated cation channel activity. Involved in monoatomic cation transport. Located in lysosomal membrane and plasma membrane. Implicated in hereditary spastic paraplegia 87. Biomarker of focal segmental glomerulosclerosis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23787) · Entrez [57156](https://www.ncbi.nlm.nih.gov/gene/57156) · UniProt [Q9P1W3](https://www.uniprot.org/uniprotkb/Q9P1W3) · Ensembl [ENSG00000165548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165548)

## Data

Gene col 9143: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9143); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9143, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9143]; `tensor/DDL_lfc|DDL_z.npy` [9143]; `embed/gene_vectors.npy` [9143]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9143 or target_col == 9143). Every well: [[TMEM63C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM63C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
