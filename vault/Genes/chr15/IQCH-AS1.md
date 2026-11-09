---
symbol: "IQCH-AS1"
type: "gene"
col: 15224
ensembl_id: "ENSG00000259673"
name: "IQCH antisense RNA 1"
location: "15q23"
module: 10
arm: "+"
pooled_cpm: 12.43
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 11
n_dd_up_clean: 22
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# IQCH-AS1

*IQCH antisense RNA 1* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +14.3, q 2e-43, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.614× (z -5.7, q 9e-06, down in 23 of 47 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.655× (z -4.9, q 2e-04, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WARS2-AS1]] (+0.82, fdr 2e-05), [[LEKR1]] (+0.77, fdr 1e-05), [[UFL1-AS1]] (+0.76, fdr 4e-05); moves opposite to [[YIF1B]] (-0.72, fdr 4e-04), [[UBA6]] (-0.68, fdr 1e-04), [[ABCB9]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC00886]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +14.3 | 2e-43 | 39/45 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +13.3 | 5e-38 | 29/45 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.8 | 3e-16 | 19/20 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +8.6 | 9e-16 | 30/34 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +7.0 | 3e-10 | 31/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +6.7 | 1e-09 | 15/27 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +5.8 | 4e-07 | 22/44 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.5 | 3e-06 | 18/46 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.39×** | +5.4 | 4e-06 | 22/47 (NCI-H1573, SW1417, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.55×** | +5.1 | 2e-05 | 17/46 (LoVo, C-33 A, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.48×** | +4.6 | 2e-04 | 21/46 (NCI-H2030, CFPAC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.62×** | +4.4 | 4e-04 | 15/45 (KATO III, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.4 | 5e-04 | 20/44 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +4.4 | 5e-04 | 17/45 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.002 | 15/47 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 15/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.006 | 12/47 (SW48, NCI-H2030, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.012 | 9/47 (SW1417, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.012 | 11/43 (hTERT-HPNE, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.614×** | -5.7 | 9e-06 | 23/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.654×** | -4.9 | 2e-04 | 21/46 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.655×** | -4.9 | 2e-04 | 22/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.490×** | -4.3 | 0.002 | 17/41 (BT-474, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.696×** | -4.2 | 0.003 | 21/47 (LoVo, SNU-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.642×** | -4.1 | 0.004 | 19/46 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.653×** | -3.9 | 0.008 | 18/47 (NCI-H1573, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.714×** | -3.7 | 0.017 | 16/43 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.023 | 15/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -3.4 | 0.035 | 18/46 (KATO III, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.703×** | -3.2 | 0.064 | 15/47 (LoVo, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 0.769× | -3.0 | 0.11 | 19/47 (LoVo, HEC-1-A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 38.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HCT15 (line)]] | alt | 17.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +10.0) | [[Saquinavir (drug)]] 0.5 µM 0.101× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 5.22 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +11.8) | — |
| [[A498 (line)]] | wt | 7.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.8) | — |
| [[A549 (line)]] | wt | 8.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0831× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[HEC-1-A (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 4.43 | 0 | 1 | — | [[Adenine (drug)]] 0.5 µM 0.0603× (z -9.5) |
| [[J82 (line)]] | alt | 5.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +10.5) | — |
| [[LoVo (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.262× (z -10.0) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1792 (line)]] | alt | 9.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[PANC-1 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +9.2) | — |
| [[SNU-1 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.127× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 5.99 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0714× (z -9.7) |
| [[SW48 (line)]] | wt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +10.8) | — |
| [[A-172 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 18 of them with an alert (⚠; 18 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | +0.82 | +0.83 / +0.47 | both halves | 2e-05 | same gene group |
| [[LEKR1]] | +0.77 | +0.83 / +0.50 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | +0.76 | +0.80 / +0.41 | both halves | 4e-05 | same gene group |
| [[PCNX4-DT]] | +0.76 | +0.78 / +0.43 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.75 | +0.76 / +0.37 | both halves | 9e-05 | same gene group |
| [[PPP3CB-AS1]] | +0.74 | +0.70 / +0.37 | both halves | 7e-05 | same gene group |
| [[GALNT7-DT]] | +0.74 | +0.75 / +0.31 | both halves | 2e-04 |  |
| [[OXA1L-DT]] | +0.73 | +0.77 / +0.34 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | +0.72 | +0.76 / +0.26 | both halves | 4e-04 | same gene group |
| [[INO80D]] | +0.72 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[RFX3-DT]] | +0.72 | +0.76 / +0.27 | both halves | 3e-04 |  |
| [[PLBD1-AS1]] | +0.72 | +0.68 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIF1B]] | -0.72 | -0.69 / -0.24 | both halves | 4e-04 |  |
| [[UBA6]] | -0.68 | -0.77 / -0.33 | both halves | 1e-04 |  |
| [[ABCB9]] | -0.67 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[CLTCL1]] | -0.66 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[CIB1]] | -0.65 | -0.70 / -0.34 | both halves | 1e-04 |  |
| [[MPG]] | -0.65 | -0.72 / -0.31 | both halves | 2e-04 |  |
| [[SLC27A1]] | -0.65 | -0.62 / -0.20 | both halves | 7e-04 |  |
| [[SH3PXD2B]] | -0.65 | -0.62 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00886]] | B | LINC00886 activity raises IQCH-AS1's level | lines that do not express LINC00886 (16) vs lines expressing it (34) | 1.44× lower at baseline in the lines without LINC00886 | 0.012 | ⚠ within organs, on part of the lines; also absent: RASEF; maybe low, not absent |
| [[TMOD1]] | B | TMOD1 activity strengthens IQCH-AS1's drug response | lines that do not express TMOD1 (14) vs lines expressing it (34) | the lines without TMOD1 respond 0.87× as strongly (z diff +0.37); strongest at Homoharringtonine 5 µM: 1.41x vs 2.33x (z diff +2.6) | 0.012 | ⚠ within organs, on part of the lines; also absent: TGFB1I1, ABLIM3, ENSG00000285744; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MPP2]] | B | MPP2 activity strengthens IQCH-AS1's drug response | lines that do not express MPP2 (7) vs lines expressing it (41) | the lines without MPP2 respond 0.76× as strongly (z diff +0.71); strongest at Homoharringtonine 5 µM: 0.95x vs 2.31x (z diff +5.5) | 0.020 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT; target measured in part of the lines; both ways; artifact flags |
| [[ACTR3C]] | B | ACTR3C activity raises IQCH-AS1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without ACTR3C | 0.033 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[MARVELD2]] | B | MARVELD2 activity raises IQCH-AS1's level | lines that do not express MARVELD2 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without MARVELD2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CHMP4C, ARHGEF5, LLGL2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers IQCH-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GOLGA2P5-1]] | B | GOLGA2P5-1 activity raises IQCH-AS1's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without GOLGA2P5-1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[DENND2D]] | B | DENND2D activity raises IQCH-AS1's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without DENND2D | 0.054 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[GRHL2]] | B | GRHL2 activity raises IQCH-AS1's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without GRHL2 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[ANKRD18A]] | B | ANKRD18A activity raises IQCH-AS1's level | lines that do not express ANKRD18A (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without ANKRD18A | 0.076 | ⚠ within organs, on part of the lines; also absent: LRRC61, SLC27A2, CHMP4C |
| [[STARD9]] | B | STARD9 activity strengthens IQCH-AS1's drug response | lines that do not express STARD9 (8) vs lines expressing it (40) | the lines without STARD9 respond 0.77× as strongly (z diff +0.75); strongest at Homoharringtonine 5 µM: 1.04x vs 2.32x (z diff +4.8) | 0.078 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.800). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.8, 14.7); signed map (27.8, -11.7). **Vector** length 95.1, 21.5% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +4.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.3 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.0 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | -4.1 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | IQCH antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q23 — chr15:67,290,636-67,521,844 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44104) · Entrez [100506686](https://www.ncbi.nlm.nih.gov/gene/100506686) · Ensembl [ENSG00000259673](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259673)

## Data

Gene col 15224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15224); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15224]; `tensor/DDL_lfc|DDL_z.npy` [15224]; `embed/gene_vectors.npy` [15224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15224 or target_col == 15224). Every well: [[IQCH-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCH-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
