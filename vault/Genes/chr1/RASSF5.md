---
symbol: "RASSF5"
type: "gene"
col: 15482
ensembl_id: "ENSG00000266094"
name: "Ras association domain family member 5"
location: "1q32.1"
module: 14
arm: "+"
pooled_cpm: 15.09
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RASSF5

*Ras association domain family member 5* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.28× (z +24.5, q 0e+00, up in 32 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.540× (z -9.0, q 2e-16, down in 24 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.634× (z -6.6, q 9e-09, down in 17 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADORA2A]] (+0.65, fdr 7e-06), [[IKBKE]] (+0.61, fdr 1e-05, ⚠ same locus), [[TNFAIP2]] (+0.60, fdr 7e-06), [[EBI3]] (+0.60, fdr 7e-06); moves opposite to [[THAP4]] (-0.49, fdr 1e-04), [[ZFP28]] (-0.47, fdr 1e-04), [[CWF19L1]] (-0.47, fdr 8e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[RRAD]] → it (grade B ⚠); 11 go from it, the strongest it → [[TJP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.28×** | +24.5 | 0e+00 | 32/37 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.51×** | +17.6 | 0e+00 | 30/41 (J82, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +15.1 | 0e+00 | 35/41 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.32×** | +12.2 | 4e-32 | 29/43 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +10.8 | 5e-25 | 27/41 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +10.5 | 1e-23 | 26/41 (Panc 03.27, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +9.9 | 3e-21 | 26/39 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +7.4 | 8e-12 | 20/37 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +6.8 | 5e-10 | 23/42 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.49×** | +5.4 | 3e-06 | 12/40 (HOP62, COLO 205, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.40×** | +4.7 | 2e-04 | 12/36 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 17/41 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.8 | 0.005 | 15/35 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.029 | 5/43 (HOP62, HEC-1-A, …) | top dose only |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.080 | 6/41 (COLO 205, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15482.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.540×** | -9.0 | 2e-16 | 24/32 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.634×** | -6.6 | 9e-09 | 17/39 (A498, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.684×** | -5.5 | 6e-06 | 14/41 (SW 900, COLO 205, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.490×** | -5.4 | 6e-06 | 14/35 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.689×** | -5.4 | 6e-06 | 11/41 (KATO III, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -5.0 | 5e-05 | 16/41 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.763×** | -3.9 | 0.007 | 13/40 (HEC-1-A, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.797×** | -3.3 | 0.068 | 5/43 (AN3 CA, A498, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.070 | 11/43 (A498, LoVo, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.807× | -3.0 | 0.15 | 11/39 (Hs 766T, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 36.5 | 4 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 11.0× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.214× (z -11.3) |
| [[HS-578T (line)]] | alt | 10.9 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.41× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 47.6 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW480 (line)]] | alt | 21.3 | 0 | 6 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -11.0) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.323× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 13.8 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 8.54× (z +10.0) | — |
| [[A549 (line)]] | wt | 13.1 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 18.5× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 74.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.55× (z +8.8) ⚠ cell-cycle shift, explains ~17% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0291× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +18.3) | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.2) | [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 21.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +10.3) | — |
| [[J82 (line)]] | alt | 13.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 17.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 6.38× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.41 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 42.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 8.76 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 14.6× (z +9.6) | — |
| [[A-172 (line)]] | wt | 8.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +10.9) | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0844× (z -9.4) |
| [[HOP62 (line)]] | alt | 9.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +17.7) | — |
| [[LS 180 (line)]] | wt | 22.2 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.65× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 14.9× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 9.05 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0662× (z -11.5) |
| [[A-427 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADORA2A]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[IKBKE]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 | STRING 414; ⚠ same locus (10.6 kb, same strand: neighbours can correlate without regulation) |
| [[TNFAIP2]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[EBI3]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CCL2]] | +0.58 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[IFNGR2]] | +0.57 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[CD83]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[NKX3-1]] | +0.56 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[IRF1]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CSF1]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PTGER4]] | +0.54 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ZC3H12A]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[MIR3142HG]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP4]] | -0.49 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[ZFP28]] | -0.47 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[CWF19L1]] | -0.47 | -0.37 / -0.49 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAD]] | B | RRAD activity raises RASSF5's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without RRAD | 0.008 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[CX3CL1]] | B | CX3CL1 activity raises RASSF5's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.86× lower at baseline in the lines without CX3CL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[NOD2]] | B | NOD2 activity raises RASSF5's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.83× lower at baseline in the lines without NOD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[STAT5A]] | B | STAT5A activity raises RASSF5's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without STAT5A | 0.025 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[SLC43A3]] | B | SLC43A3 activity raises RASSF5's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without SLC43A3 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[ANO9]] | B | ANO9 activity raises RASSF5's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without ANO9 | 0.029 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[TSPAN2]] | B | TSPAN2 activity raises RASSF5's level | lines that do not express TSPAN2 (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without TSPAN2 | 0.032 | ⚠ within organs, on part of the lines; also absent: SAA1, STK32A, IFI44L |
| [[TNFRSF9]] | B | TNFRSF9 activity raises RASSF5's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 1.76× lower at baseline in the lines without TNFRSF9 | 0.039 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[ITGA1]] | B | ITGA1 activity raises RASSF5's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.86× lower at baseline in the lines without ITGA1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[TJP2]] | B | TJP2 activity raises RASSF5's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.04× lower at baseline in the lines without TJP2 | 0.073 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[MAML2]] | B | MAML2 activity raises RASSF5's level | lines that do not express MAML2 (8) vs lines expressing it (42) | 2.19× lower at baseline in the lines without MAML2 | 0.082 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[ITGA1]] | B | ITGA1 activity strengthens RASSF5's drug response | lines that do not express ITGA1 (14) vs lines expressing it (29) | the lines without ITGA1 respond 0.33× as strongly (z diff +2.33); strongest at Panobinostat 0.5 µM: 0.95x vs 2.45x (z diff +3.7) | 0.085 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973; target measured in part of the lines; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP2]] | B | RASSF5 activity raises TJP2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 4.07× lower at baseline in the lines without RASSF5 | 0.050 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[FHDC1]] | B | RASSF5 activity raises FHDC1's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 2.23× lower at baseline in the lines without RASSF5 | 0.050 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[BAMBI]] | B | RASSF5 activity raises BAMBI's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 3.71× lower at baseline in the lines without RASSF5 | 0.058 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[NFATC2]] | B | RASSF5 activity raises NFATC2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 3.61× lower at baseline in the lines without RASSF5 | 0.069 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[NOD2]] | B | RASSF5 activity raises NOD2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 2.54× lower at baseline in the lines without RASSF5 | 0.072 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| cells under [[Omeprazole (drug)]] 5 µM | B | RASSF5 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express RASSF5 (5) vs lines expressing it (43) | the lines without RASSF5: 1.13× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| cells under [[Docetaxel (drug)]] 5 µM | B | RASSF5 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express RASSF5 (5) vs lines expressing it (43) | the lines without RASSF5: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[CCL2]] | B | RASSF5 activity lowers CCL2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 2.18× higher at baseline in the lines without RASSF5 | 0.084 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| cells under [[Docetaxel (drug)]] 0.5 µM | B | RASSF5 activity raises the cells' numbers under Docetaxel 0.5 µM (protects the cells) | lines that do not express RASSF5 (5) vs lines expressing it (43) | the lines without RASSF5: 0.82× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[MAML2]] | B | RASSF5 activity raises MAML2's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 3.45× lower at baseline in the lines without RASSF5 | 0.098 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent |
| [[IKBKE]] | C | RASSF5 activity raises IKBKE's level | lines that do not express RASSF5 (5) vs lines expressing it (45) | 3.47× lower at baseline in the lines without RASSF5 | 0.007 | ⚠ within organs, on part of the lines; also absent: NAT1, WWC3, ZMIZ1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 4.6); signed map (43.8, 8.1). **Vector** length 94.0, 20.2% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +15.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +9.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +17.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +24.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.5 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.2 | -6.6 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | Ras association domain family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,507,531-206,589,448 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Maxp1, NORE1, RAPL |
| Gene groups (HGNC) | Ras association domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWW0](https://www.uniprot.org/uniprotkb/Q8WWW0) (Ras association domain-containing protein 5):

> Potential tumor suppressor. Seems to be involved in lymphocyte adhesion by linking RAP1A activation upon T-cell receptor or chemokine stimulation to integrin activation. Isoform 2 stimulates lymphocyte polarization and the patch-like distribution of ITGAL/LFA-1, resulting in an enhanced adhesion to ICAM1. Together with RAP1A may participate in regulation of microtubule growth. The association of isoform 2 with activated RAP1A is required for directional movement of endothelial cells during …

**Summary**, from NCBI Gene [83593](https://www.ncbi.nlm.nih.gov/gene/83593):

> This gene is a member of the Ras association domain family. It functions as a tumor suppressor, and is inactivated in a variety of cancers. The encoded protein localizes to centrosomes and microtubules, and associates with the GTP-activated forms of Ras, Rap1, and several other Ras-like small GTPases. The protein regulates lymphocyte adhesion and suppresses cell growth in response to activated Rap1 or Ras. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:17609](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17609) · Entrez [83593](https://www.ncbi.nlm.nih.gov/gene/83593) · UniProt [Q8WWW0](https://www.uniprot.org/uniprotkb/Q8WWW0) · Ensembl [ENSG00000266094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266094)

## Data

Gene col 15482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15482); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15482]; `tensor/DDL_lfc|DDL_z.npy` [15482]; `embed/gene_vectors.npy` [15482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15482 or target_col == 15482). Every well: [[RASSF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
