---
symbol: "CCDC113"
type: "gene"
col: 2303
ensembl_id: "ENSG00000103021"
name: "cilia and flagella associated protein 263"
location: "16q21"
module: 28
arm: "+"
pooled_cpm: 9.79
n_lines_expressing: 47
n_dd_up: 22
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CCDC113

*cilia and flagella associated protein 263* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +15.9, q 0e+00, up in 31 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.537× (z -8.5, q 1e-14, down in 27 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.547× (z -8.3, q 4e-14, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEX1]] (+0.74, fdr 7e-06), [[MKS1]] (+0.71, fdr 7e-06), [[RNF214]] (+0.68, fdr 1e-05); moves opposite to [[C9orf153]] (-0.61, fdr 3e-05), [[SNHG30]] (-0.60, fdr 1e-05), [[HIGD2A]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BSN]] → it (grade B ⚠); 9 go from it, the strongest it → [[HSD17B10]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +15.9 | 0e+00 | 31/42 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.82×** | +14.2 | 3e-43 | 40/44 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +13.4 | 2e-38 | 22/29 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.60×** | +13.1 | 6e-37 | 39/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +11.9 | 2e-30 | 14/16 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +9.8 | 7e-21 | 30/43 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.02×** | +9.7 | 4e-20 | 34/44 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +9.4 | 2e-19 | 15/21 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +7.8 | 3e-13 | 23/42 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +6.1 | 7e-08 | 20/43 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +6.0 | 1e-07 | 17/44 (A-172, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.52×** | +5.7 | 6e-07 | 18/44 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +5.5 | 1e-06 | 13/45 (NCI-H1573, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.48×** | +5.2 | 1e-05 | 13/32 (MIA PaCa-2, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +4.9 | 3e-05 | 11/45 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +4.9 | 3e-05 | 18/40 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.008 | 6/45 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.009 | 3/43 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.038 | 9/44 (A-172, J82, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2303.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.537×** | -8.5 | 1e-14 | 27/40 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.547×** | -8.3 | 4e-14 | 25/44 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -6.9 | 8e-10 | 25/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -6.6 | 5e-09 | 25/44 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -6.3 | 3e-08 | 21/38 (A-427, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.648×** | -5.9 | 3e-07 | 22/43 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -5.3 | 7e-06 | 17/44 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -4.7 | 2e-04 | 17/41 (SW1417, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.524×** | -4.6 | 2e-04 | 13/39 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.793×** | -4.5 | 4e-04 | 17/45 (NCI-H661, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -4.1 | 0.002 | 8/45 (H4, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -4.1 | 0.002 | 18/43 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.823×** | -3.8 | 0.007 | 14/45 (KATO III, HCT15, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.775×** | -3.3 | 0.042 | 14/42 (KATO III, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.764×** | -3.3 | 0.042 | 9/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.788×** | -3.1 | 0.070 | 13/44 (SW480, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.1 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +10.2) | [[Digitoxin (drug)]] 0.5 µM 0.280× (z -9.4) |
| [[PANC-1 (line)]] | alt | 10.6 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +8.6) | [[Bortezomib (drug)]] 5 µM 0.0672× (z -11.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -11.0) |
| [[A-427 (line)]] | wt | 27.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -17.4) |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0801× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -8.5) |
| [[LoVo (line)]] | wt | 9.62 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +10.1) | [[PH-797804 (drug)]] 5 µM 0.0387× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 18.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.276× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -10.2) |
| [[A498 (line)]] | wt | 15.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -13.4) |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.150× (z -8.8) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEX1]] | +0.74 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[MKS1]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[RNF214]] | +0.68 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[YTHDC2]] | +0.67 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[FAR2P1]] | +0.65 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[ZNF512B]] | +0.65 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[POLI]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.65 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[RTL6]] | +0.64 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.64 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[MDM1]] | +0.64 | +0.66 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C9orf153]] | -0.61 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SNHG30]] | -0.60 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[HIGD2A]] | -0.55 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.55 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.54 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[CD81]] | -0.53 | -0.60 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BSN]] | B | BSN activity raises CCDC113's level | lines that do not express BSN (17) vs lines expressing it (33) | 1.66× lower at baseline in the lines without BSN | 0.023 | ⚠ within organs, on part of the lines; also absent: HRK, SPTB, CACNA2D2; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD17B10]] | C | CCDC113 activity raises HSD17B10's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 2.12× lower at baseline in the lines without CCDC113 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1; its own permutation p |
| [[TYW5]] | C | CCDC113 activity raises TYW5's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.36× lower at baseline in the lines without CCDC113 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1; its own permutation p |
| [[FAHD2CP]] | C | CCDC113 activity raises FAHD2CP's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without CCDC113 | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |
| [[MIF4GD]] | C | CCDC113 activity raises MIF4GD's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.84× lower at baseline in the lines without CCDC113 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |
| [[RNF214]] | C | CCDC113 activity raises RNF214's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.34× lower at baseline in the lines without CCDC113 | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |
| [[PEX1]] | C | CCDC113 activity raises PEX1's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without CCDC113 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |
| [[ZNF512B]] | C | CCDC113 activity raises ZNF512B's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 2.40× lower at baseline in the lines without CCDC113 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1; its own permutation p |
| [[BPHL]] | C | CCDC113 activity raises BPHL's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.71× lower at baseline in the lines without CCDC113 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |
| [[TTC26]] | C | CCDC113 activity raises TTC26's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 2.23× lower at baseline in the lines without CCDC113 | 0.0997 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.4, 2.7); signed map (0.8, -34.5). **Vector** length 74.9, 13.5% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +15.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +13.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +3.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.0 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 263 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,231,157-58,283,836 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC065, DKFZp434N1418; previously CCDC113 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0I3](https://www.uniprot.org/uniprotkb/Q9H0I3) (Cilia- and flagella-associated protein 263):

> Component of centriolar satellites contributing to primary cilium formation. In complex with CFAP263, acts as a regulator of ciliary beating that connects radial spoke 3 (RS3) to the inner dynein arm (IDA) and the nexin-dynein regulatory complex (N-DRC). The complex is positioned parallel to N-DRC and forms a connection between the arch at the base of RS3, the IDA tail and N-DRC (By similarity).

**Summary**, from NCBI Gene [29070](https://www.ncbi.nlm.nih.gov/gene/29070):

> Involved in cilium assembly. Located in centriolar satellite and ciliary basal body. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25002) · Entrez [29070](https://www.ncbi.nlm.nih.gov/gene/29070) · UniProt [Q9H0I3](https://www.uniprot.org/uniprotkb/Q9H0I3) · Ensembl [ENSG00000103021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103021)

## Data

Gene col 2303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2303); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2303]; `tensor/DDL_lfc|DDL_z.npy` [2303]; `embed/gene_vectors.npy` [2303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2303 or target_col == 2303). Every well: [[CCDC113 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC113.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
