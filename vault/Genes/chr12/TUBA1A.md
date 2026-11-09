---
symbol: "TUBA1A"
type: "gene"
col: 9487
ensembl_id: "ENSG00000167552"
name: "tubulin alpha 1a"
location: "12q13.12"
module: 208
arm: "+"
pooled_cpm: 19.72
n_lines_expressing: 40
n_dd_up: 40
n_dd_down: 9
n_dd_up_clean: 36
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# TUBA1A

*tubulin alpha 1a* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (4 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 5 µM: 2.35× (z +12.6, q 1e-33, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.663× (z -6.0, q 1e-06, down in 22 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBB2A]] (+0.63, fdr 3e-05), [[DYNLT3]] (+0.59, fdr 1e-05), [[KLF7]] (+0.58, fdr 1e-05); moves opposite to [[NAF1]] (-0.54, fdr 3e-05), [[GABPB1-AS1]] (-0.53, fdr 9e-05), [[ECHDC1]] (-0.50, fdr 1e-04).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP1A]] → it (grade B ⚠); 9 go from it, the strongest it → [[OAZ2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 5 µM |  | **2.35×** | +12.6 | 1e-33 | 37/38 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.42×** | +9.2 | 8e-18 | 32/36 (C32, A549, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **2.46×** | +9.0 | 4e-17 | 33/37 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.5 µM |  | **2.06×** | +7.5 | 8e-12 | 36/38 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **2.00×** | +7.2 | 6e-11 | 29/37 (NCI-H2030, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.9 | 4e-07 | 22/38 (SW480, C-33 A, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.61×** | +5.0 | 5e-05 | 21/38 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +5.0 | 5e-05 | 23/38 (C-33 A, PANC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 5e-05 | 21/38 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.7 | 1e-04 | 15/33 (A498, A-172, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **1.60×** | +4.7 | 1e-04 | 22/38 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **2.30×** | +4.5 | 3e-04 | 20/38 (A-427, LOX-IMVI, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Triclosan (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 19/38 (C32, NCI-H460, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.52×** | +4.4 | 5e-04 | 20/38 (BT-474, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +4.3 | 8e-04 | 19/38 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.46×** | +3.9 | 0.003 | 14/38 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.005 | 13/38 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.010 | 15/38 (RPMI-7951, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -6.0 | 1e-06 | 22/38 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.689×** | -5.5 | 1e-05 | 23/38 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.644×** | -4.6 | 1e-03 | 17/38 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.654×** | -4.2 | 0.003 | 21/38 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -3.8 | 0.014 | 19/38 (NCI-H460, A-427, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.698×** | -3.4 | 0.071 | 15/38 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.094 | 14/38 (A498, SW 900, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.733×** | -3.2 | 0.094 | 12/38 (SW 1088, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.557×** | -3.2 | 0.094 | 17/38 (H4, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.746× | -3.0 | 0.14 | 14/38 (J82, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 84.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.7) |
| [[SW480 (line)]] | alt | 14.9 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +10.6) | — |
| [[C32 (line)]] | wt | 23.3 | 3 (1 ⚠) | 0 | [[Docetaxel (drug)]] 5 µM 5.48× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 39.0 | 1 | 2 (1 ⚠) | [[Docetaxel (drug)]] 5 µM 2.50× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.291× (z -9.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.8) |
| [[A498 (line)]] | wt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 20.8 | 1 | 1 (1 ⚠) | [[Docetaxel (drug)]] 5 µM 3.35× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -13.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 28.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 33.6 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0556× (z -16.2) |
| [[A-427 (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0595× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 8.22 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0856× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 30.9 | 1 | 0 | [[Docetaxel (drug)]] 5 µM 3.09× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 35.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -8.8) |
| [[SHP-77 (line)]] | alt | 32.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 21.8 | 1 | 0 | [[Docetaxel (drug)]] 5 µM 2.96× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB2A]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 | pathway: Activation of AMPK downstream of NMDARs; STRING 999 |
| [[DYNLT3]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 | STRING 400 |
| [[KLF7]] | +0.58 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[DLGAP4]] | +0.58 | +0.46 / +0.57 | both halves | 3e-05 | pathway: Neuronal System |
| [[TMOD1]] | +0.58 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[TTLL7]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 | pathway: Carboxyterminal post-translational modifications of tubulin |
| [[PTPRN]] | +0.55 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[YWHAH]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 | pathway: RHO GTPase Effectors; STRING 413 |
| [[RHOB]] | +0.54 | +0.33 / +0.58 | both halves | 1e-04 | pathway: RHO GTPase Effectors |
| [[PNMA1]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MAP1B]] | +0.53 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SKAP2]] | +0.53 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAF1]] | -0.54 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GABPB1-AS1]] | -0.53 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[ECHDC1]] | -0.50 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[QTRT1]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[ANAPC1]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 | pathway: Mitotic Anaphase |
| [[NDUFAF6]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[PDCD6P1]] | -0.48 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[MACROD1]] | -0.48 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[WDR12]] | -0.48 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[ITPKB]] | -0.48 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[SAFB]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[STARD7-AS1]] | -0.47 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1A]] | B | MAP1A activity raises TUBA1A's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 4.00× lower at baseline in the lines without MAP1A | 0.023 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[LGALS1]] | B | LGALS1 activity raises TUBA1A's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 3.58× lower at baseline in the lines without LGALS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[MSX2]] | B | MSX2 activity lowers TUBA1A's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.48× higher at baseline in the lines without MSX2 | 0.029 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[JAZF1]] | B | JAZF1 activity raises TUBA1A's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 4.25× lower at baseline in the lines without JAZF1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |
| [[ZCCHC24]] | B | ZCCHC24 activity raises TUBA1A's level | lines that do not express ZCCHC24 (5) vs lines expressing it (45) | 3.12× lower at baseline in the lines without ZCCHC24 | 0.069 | ⚠ within organs, on part of the lines; also absent: CNTNAP1, KIF17, SLC29A4; maybe low, not absent |
| [[L1CAM]] | B | L1CAM activity raises TUBA1A's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 2.60× lower at baseline in the lines without L1CAM | 0.080 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |
| [[MAP1B]] | C | MAP1B activity raises TUBA1A's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 5.04× lower at baseline in the lines without MAP1B | 0.018 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[TTLL7]] | C | TTLL7 activity raises TUBA1A's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 4.52× lower at baseline in the lines without TTLL7 | 0.043 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAZ2]] | B | TUBA1A activity raises OAZ2's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.26× lower at baseline in the lines without TUBA1A | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[JAZF1]] | B | TUBA1A activity raises JAZF1's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 2.76× lower at baseline in the lines without TUBA1A | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[RASSF2]] | B | TUBA1A activity raises RASSF2's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 2.54× lower at baseline in the lines without TUBA1A | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[ZCCHC24]] | B | TUBA1A activity raises ZCCHC24's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 2.39× lower at baseline in the lines without TUBA1A | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[KIF3C]] | B | TUBA1A activity raises KIF3C's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 3.02× lower at baseline in the lines without TUBA1A | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[NAF1]] | B | TUBA1A activity raises NAF1's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without TUBA1A | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[WDR12]] | B | TUBA1A activity raises WDR12's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.27× lower at baseline in the lines without TUBA1A | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[SAFB]] | B | TUBA1A activity raises SAFB's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 1.14× lower at baseline in the lines without TUBA1A | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10 |
| [[TTLL7]] | C | TUBA1A activity raises TTLL7's level | lines that do not express TUBA1A (10) vs lines expressing it (40) | 5.49× lower at baseline in the lines without TUBA1A | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, GABBR1, CHST10; co-absent with the target |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.3, -1.9); signed map (-8.8, 27.6). **Vector** length 99.9, 24.2% of its response variance represented; |z| ≥ 3 in 1,018 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +5.5 | +9.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.1 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.6 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +3.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.7 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.3 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | tubulin alpha 1a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,184,686-49,189,324 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TUBA3, B-ALPHA-1, FLJ25113 |
| Gene groups (HGNC) | Tubulin alpha family |
| Reactome | 90 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q71U36](https://www.uniprot.org/uniprotkb/Q71U36) (Tubulin alpha-1A chain):

> Tubulin is the major constituent of microtubules, protein filaments consisting of alpha- and beta-tubulin heterodimers (By similarity). Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms (By similarity). Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin (By similarity).

**Summary**, from NCBI Gene [7846](https://www.ncbi.nlm.nih.gov/gene/7846):

> Microtubules of the eukaryotic cytoskeleton perform essential and diverse functions and are composed of a heterodimer of alpha and beta tubulins. The genes encoding these microtubule constituents belong to the tubulin superfamily, which is composed of six distinct families. Genes from the alpha, beta and gamma tubulin families are found in all eukaryotes. The alpha and beta tubulins represent the major components of microtubules, while gamma tubulin plays a critical role in the nucleation of …

**Accessions** — [HGNC:20766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20766) · Entrez [7846](https://www.ncbi.nlm.nih.gov/gene/7846) · UniProt [Q71U36](https://www.uniprot.org/uniprotkb/Q71U36) · Ensembl [ENSG00000167552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167552)

## Data

Gene col 9487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9487); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9487]; `tensor/DDL_lfc|DDL_z.npy` [9487]; `embed/gene_vectors.npy` [9487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9487 or target_col == 9487). Every well: [[TUBA1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBA1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
