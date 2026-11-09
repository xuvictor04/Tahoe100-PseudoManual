---
symbol: "ZC3HAV1L"
type: "gene"
col: 7128
ensembl_id: "ENSG00000146858"
name: "ZC3HAV1 like"
location: "7q34"
module: 18
arm: "+"
pooled_cpm: 11.37
n_lines_expressing: 45
n_dd_up: 0
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 19
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ZC3HAV1L

*ZC3HAV1 like* — 7q34

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.216× (z -14.4, q 3e-44, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIPC]] (+0.68, fdr 7e-06), [[TMEM64]] (+0.66, fdr 1e-05), [[RFT1]] (+0.66, fdr 7e-06); moves opposite to [[GBF1]] (-0.64, fdr 5e-05), [[POLD4]] (-0.63, fdr 3e-05), [[PMM1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUXAP8]] → it (grade B ⚠); 19 go from it, the strongest it → cells under [[Methylthiouracil (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Roxadustat (drug)]] 5 µM |  | 1.49× | +3.6 | 0.14 | 14/43 (AN3 CA, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.48× | +3.4 | 0.14 | 13/42 (SW48, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.3 | 0.14 | 3/43 (NCI-H23, SHP-77, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.42× | +3.3 | 0.14 | 15/43 (A-427, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.216×** | -14.4 | 3e-44 | 42/43 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.286×** | -14.3 | 5e-44 | 39/42 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.266×** | -12.4 | 3e-33 | 40/43 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.301×** | -11.3 | 2e-27 | 38/43 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.354×** | -9.4 | 7e-19 | 35/42 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -6.3 | 2e-08 | 31/41 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.581×** | -4.9 | 8e-05 | 23/40 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.595×** | -4.9 | 8e-05 | 26/43 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.599×** | -4.8 | 9e-05 | 24/43 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.606×** | -4.5 | 3e-04 | 22/41 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.619×** | -4.5 | 3e-04 | 19/41 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.614×** | -4.3 | 7e-04 | 23/43 (HCT15, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.637×** | -4.2 | 1e-03 | 22/42 (SNU-1, NCI-H460, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -4.0 | 0.003 | 21/43 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.657×** | -3.8 | 0.006 | 22/42 (A-427, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.674×** | -3.7 | 0.008 | 20/43 (Panc 03.27, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.738×** | -3.2 | 0.039 | 14/43 (LOX-IMVI, SHP-77, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.606×** | -3.0 | 0.076 | 15/41 (C-33 A, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 20.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -12.3) |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0880× (z -15.0) |
| [[SW480 (line)]] | alt | 20.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0575× (z -18.7) |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 3 | — | [[Vilanterol (drug)]] 0.5 µM 0.0702× (z -12.1) |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 28.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.158× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.173× (z -10.3) |
| [[RKO (line)]] | wt | 9.30 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0565× (z -10.1) |
| [[A549 (line)]] | wt | 9.60 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 8.52 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.139× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.196× (z -9.3) |
| [[LoVo (line)]] | wt | 12.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.141× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 5.81 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0617× (z -15.2) |
| [[SNU-1 (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0531× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.155× (z -10.0) |
| [[SW1417 (line)]] | alt | 7.44 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.115× (z -9.1) |
| [[A-427 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HOP62 (line)]] | alt | 8.92 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -8.8) |
| [[KATO III (line)]] | alt | 7.53 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 8.27 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0337× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0503× (z -9.6) |
| [[SW48 (line)]] | wt | 16.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0884× (z -9.2) |
| [[A-172 (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIPC]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[TMEM64]] | +0.66 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RFT1]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[NAE1]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[RAB11FIP2]] | +0.66 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[FAM136A]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ALG10B]] | +0.65 | +0.38 / +0.67 | both halves | 6e-05 |  |
| [[NUP210]] | +0.64 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[VMA21]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[HDDC2]] | +0.62 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[UBE2G2]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TUBGCP4]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBF1]] | -0.64 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[POLD4]] | -0.63 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[PMM1]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.61 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[SELENOK]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[PPARA]] | -0.59 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[MTHFR]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[COQ10B]] | -0.58 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MED19]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.57 | -0.32 / -0.54 | both halves | 1e-04 |  |
| [[TRAPPC2B]] | -0.57 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.57 | -0.39 / -0.54 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF324]] | -0.56 | -0.61 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity raises ZC3HAV1L's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without DUXAP8 | 0.082 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 0, C 19. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Methylthiouracil (drug)]] 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Methylthiouracil 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.30× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.35× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Belinostat (drug)]] 5 µM | C | ZC3HAV1L activity raises the cells' numbers under Belinostat 5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.70× the cells of the other lines | 0.032 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Artemether (drug)]] 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Artemether 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.36× the cells of the other lines | 0.032 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Allopurinol (drug)]] 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Allopurinol 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.32× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Cabozantinib (S-malate) (drug)]] 5 µM | C | ZC3HAV1L activity raises the cells' numbers under Cabozantinib (S-malate) 5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.79× the cells of the other lines | 0.037 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Pemetrexed (drug)]] 5 µM | C | ZC3HAV1L activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.75× the cells of the other lines | 0.048 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Vortioxetine (drug)]] 5 µM | C | ZC3HAV1L activity raises the cells' numbers under Vortioxetine 5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.76× the cells of the other lines | 0.048 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Daptomycin (drug)]] 0.5 µM | C | ZC3HAV1L activity raises the cells' numbers under Daptomycin 0.5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.67× the cells of the other lines | 0.057 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2; cell counts less trustworthy |
| cells under [[Ferulic acid (drug)]] 0.5 µM | C | ZC3HAV1L activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.69× the cells of the other lines | 0.057 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Fulvestrant (drug)]] 5 µM | C | ZC3HAV1L activity lowers the cells' numbers under Fulvestrant 5 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.26× the cells of the other lines | 0.071 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 5 µM | C | ZC3HAV1L activity raises the cells' numbers under Bisoprolol (hemifumarate) 5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.79× the cells of the other lines | 0.075 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-24.4, -29.4); signed map (-13.4, -41.0). **Vector** length 74.3, 14.6% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | -0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -14.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -9.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.0 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.9 | -14.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -0.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ZC3HAV1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:139,025,706-139,036,042 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14289; previously C7orf39 |
| Matched by | ensembl_id |

UniProt [Q96H79](https://www.uniprot.org/uniprotkb/Q96H79) carries no function annotation.

**Summary**, from NCBI Gene [92092](https://www.ncbi.nlm.nih.gov/gene/92092):

> Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22423) · Entrez [92092](https://www.ncbi.nlm.nih.gov/gene/92092) · UniProt [Q96H79](https://www.uniprot.org/uniprotkb/Q96H79) · Ensembl [ENSG00000146858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146858)

## Data

Gene col 7128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7128); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7128]; `tensor/DDL_lfc|DDL_z.npy` [7128]; `embed/gene_vectors.npy` [7128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7128 or target_col == 7128). Every well: [[ZC3HAV1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZC3HAV1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
