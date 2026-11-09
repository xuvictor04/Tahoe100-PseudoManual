---
symbol: "UTP15"
type: "gene"
col: 8934
ensembl_id: "ENSG00000164338"
name: "UTP15 small subunit processome component"
location: "5q13.2"
module: 1
arm: "+"
pooled_cpm: 12.08
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# UTP15

*UTP15 small subunit processome component* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.29× (z +27.0, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.766× (z -5.0, q 3e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIL1]] (+0.79, fdr 7e-06), [[ZNF507]] (+0.79, fdr 7e-06), [[SCO1]] (+0.79, fdr 7e-06); moves opposite to [[PHF1]] (-0.69, fdr 7e-06), [[CBFA2T2]] (-0.66, fdr 1e-05), [[TESK2]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RALGPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.29×** | +27.0 | 0e+00 | 43/45 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.16×** | +18.7 | 0e+00 | 43/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.49×** | +15.8 | 0e+00 | 44/47 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.98×** | +15.1 | 0e+00 | 46/48 (PANC-1, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.56×** | +12.3 | 8e-33 | 41/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.45×** | +11.7 | 8e-30 | 36/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **5.14×** | +11.2 | 2e-27 | 39/45 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.06×** | +9.5 | 2e-19 | 33/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +8.9 | 2e-17 | 34/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.97×** | +8.9 | 3e-17 | 35/48 (LoVo, SW 900, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.97×** | +8.9 | 3e-17 | 33/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +8.2 | 2e-14 | 33/47 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.87×** | +7.9 | 2e-13 | 29/42 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.80×** | +7.7 | 5e-13 | 30/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.73×** | +7.2 | 3e-11 | 29/47 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +6.4 | 6e-09 | 31/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.62×** | +6.0 | 4e-08 | 24/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +6.0 | 7e-08 | 22/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +4.9 | 2e-05 | 18/48 (CFPAC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.003 | 17/48 (NCI-H1573, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.766×** | -5.0 | 3e-04 | 27/48 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.727×** | -4.2 | 0.007 | 18/47 (SHP-77, J82, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -3.5 | 0.076 | 12/47 (NCI-H1792, HCT15, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **0.770×** | -3.5 | 0.076 | 13/47 (C32, NCI-H1573, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.611×** | -3.4 | 0.076 | 13/44 (RKO, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.789× | -3.1 | 0.16 | 8/47 (SW48, CHP-212, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.726× | -3.0 | 0.19 | 12/44 (LoVo, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 17.4 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +15.4) | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +16.0) | — |
| [[A498 (line)]] | wt | 12.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +18.1) | — |
| [[A-172 (line)]] | wt | 9.57 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.08× (z +14.3) | — |
| [[A549 (line)]] | wt | 11.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 31.7 | 0 | 2 | — | [[Macitentan (drug)]] 0.05 µM 0.0510× (z -11.2) |
| [[BT-474 (line)]] | alt | 9.33 | 0 | 2 | — | [[Monocrotaline (drug)]] 0.05 µM 0.107× (z -9.3) |
| [[HOP62 (line)]] | alt | 8.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 7.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.74× (z +12.6) | — |
| [[LoVo (line)]] | wt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 13.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.5 µM 0.109× (z -8.9) |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.104× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 7.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +9.3) | — |
| [[C32 (line)]] | wt | 9.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 5.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 9.31 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0753× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 9.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +11.6) | — |
| [[Hs 766T (line)]] | wt | 6.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 8.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +9.3) | — |
| [[J82 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.5) | — |
| [[KATO III (line)]] | alt | 7.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 9.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 7.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +11.3) | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0867× (z -8.7) |
| [[SW480 (line)]] | alt | 14.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.15× (z +10.5) | — |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIL1]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.79 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[SCO1]] | +0.79 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[MAK16]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 | STRING 586 |
| [[LTV1]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 712 |
| [[QTRT2]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[BYSL]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[UTP20]] | +0.76 | +0.71 / +0.78 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[MTPAP]] | +0.76 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[RRS1]] | +0.75 | +0.82 / +0.71 | both halves | 7e-06 | STRING 642 |
| [[PAK1IP1]] | +0.75 | +0.82 / +0.75 | both halves | 7e-06 | same gene group; STRING 543 |
| [[PFAS]] | +0.74 | +0.70 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF1]] | -0.69 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[CBFA2T2]] | -0.66 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[TESK2]] | -0.65 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[TPT1]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[ABHD3]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[SARAF]] | -0.63 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[NDRG1]] | -0.63 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[F11R]] | -0.63 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[GNB2]] | -0.62 | -0.62 / -0.57 | both halves | 9e-06 | same gene group |
| [[AAMDC]] | -0.62 | -0.48 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | RALGPS2 activity lowers UTP15's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.72× higher at baseline in the lines without RALGPS2 | 0.060 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity lowers UTP15's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.69× higher at baseline in the lines without NDRG1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.865). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.1, -36.6); signed map (1.8, -40.9). **Vector** length 69.3, 13.7% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.59 to 10); *Mitochondrial mRNA modification* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +18.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.4 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | +3.9 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +11.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.9 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.1 | +7.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | UTP15 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:73,565,443-73,583,380 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12787, NET21, FLJ23637 |
| Gene groups (HGNC) | WD repeat domain containing; UTPa subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TED0](https://www.uniprot.org/uniprotkb/Q8TED0) (U3 small nucleolar RNA-associated protein 15 homolog):

> Ribosome biogenesis factor. Involved in nucleolar processing of pre-18S ribosomal RNA. Required for optimal pre-ribosomal RNA transcription by RNA polymerase I. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, …

**Summary**, from NCBI Gene [84135](https://www.ncbi.nlm.nih.gov/gene/84135):

> Enables RNA binding activity. Involved in positive regulation of rRNA processing; positive regulation of transcription by RNA polymerase I; and ribosomal small subunit biogenesis. Located in cytoplasm and fibrillar center. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25758) · Entrez [84135](https://www.ncbi.nlm.nih.gov/gene/84135) · UniProt [Q8TED0](https://www.uniprot.org/uniprotkb/Q8TED0) · Ensembl [ENSG00000164338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164338)

## Data

Gene col 8934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8934); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8934]; `tensor/DDL_lfc|DDL_z.npy` [8934]; `embed/gene_vectors.npy` [8934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8934 or target_col == 8934). Every well: [[UTP15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
