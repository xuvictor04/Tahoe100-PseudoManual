---
symbol: "IMPDH1"
type: "gene"
col: 2748
ensembl_id: "ENSG00000106348"
name: "inosine monophosphate dehydrogenase 1"
location: "7q32.1"
module: 77
arm: "+"
pooled_cpm: 18.22
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# IMPDH1

*inosine monophosphate dehydrogenase 1* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.37× (z +5.6, q 1e-05, up in 21 of 42 measured lines) ⚠ transcription drop. The strongest without an alert is [[Budesonide (drug)]] 0.5 µM: 1.25× (z +3.9, q 0.013, up in 8 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.332× (z -27.8, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC6]] (+0.74, fdr 7e-06), [[ZDHHC8]] (+0.73, fdr 7e-06), [[LPCAT1]] (+0.73, fdr 1e-05); moves opposite to [[BAZ2B]] (-0.78, fdr 7e-06), [[RIPK2-DT]] (-0.69, fdr 2e-05), [[C11orf58]] (-0.66, fdr 4e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[JAG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.37×** | +5.6 | 1e-05 | 21/42 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +4.9 | 2e-04 | 11/30 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.013 | 8/46 (J82, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.24×** | +3.9 | 0.013 | 9/46 (SK-MEL-2, A498, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.026 | 10/46 (PANC-1, C-33 A, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.6 | 0.033 | 8/33 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.22×** | +3.5 | 0.035 | 11/38 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.071 | 8/46 (A498, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.332×** | -27.8 | 0e+00 | 43/44 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.443×** | -13.9 | 1e-41 | 39/46 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -13.4 | 1e-38 | 32/43 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -11.4 | 8e-28 | 32/43 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -9.4 | 6e-19 | 32/46 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.695×** | -9.1 | 6e-18 | 30/46 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -6.7 | 2e-09 | 23/44 (SK-MEL-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.714×** | -6.0 | 1e-07 | 20/44 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -6.0 | 1e-07 | 22/46 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.529×** | -5.9 | 2e-07 | 24/46 (LoVo, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.797×** | -5.7 | 6e-07 | 21/46 (Panc 03.27, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -5.7 | 6e-07 | 22/46 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.738×** | -5.4 | 3e-06 | 21/46 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.710×** | -5.3 | 5e-06 | 18/45 (H4, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.744×** | -5.3 | 6e-06 | 22/46 (SW48, Hs 766T, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.796×** | -4.0 | 0.002 | 14/46 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.019 | 2/45 (HT-29, C32) | top dose only | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | 0.878× | -3.2 | 0.033 | 6/46 (A498, SNU-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -13.4) |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -19.5) |
| [[HS-578T (line)]] | alt | 31.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -15.7) |
| [[J82 (line)]] | alt | 22.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0785× (z -27.1) |
| [[LoVo (line)]] | wt | 23.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -21.2) |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -13.9) |
| [[PANC-1 (line)]] | alt | 16.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.6) |
| [[RKO (line)]] | wt | 37.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -20.1) |
| [[SW48 (line)]] | wt | 44.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.3) |
| [[A498 (line)]] | wt | 35.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.1) |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.4) |
| [[Hs 766T (line)]] | wt | 24.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -14.9) |
| [[LS 180 (line)]] | wt | 16.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 9.74 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.264× (z -12.5) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.2) |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.0) |
| [[A549 (line)]] | wt | 17.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -12.5) |
| [[C32 (line)]] | wt | 42.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.5) |
| [[H4 (line)]] | wt | 18.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0531× (z -11.9) |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~4% of this change |
| [[HEC-1-A (line)]] | alt | 8.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.6) |
| [[HT-29 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.7) |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -9.3) |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0654× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 21.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -9.7) |
| [[SW480 (line)]] | alt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.1) |
| [[A-427 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC6]] | +0.74 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.73 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[LPCAT1]] | +0.73 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[ANKRD27]] | +0.73 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[EPHB4]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[RNF216P1]] | +0.70 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[ST6GALNAC4]] | +0.70 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.69 | +0.64 / +0.51 | both halves | 1e-05 | STRING 461 |
| [[WASF3]] | +0.69 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ATP7B]] | +0.69 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[WDR5]] | +0.67 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[GTPBP3]] | +0.67 | +0.67 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.78 | -0.80 / -0.60 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | -0.69 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.66 | -0.70 / -0.42 | both halves | 4e-05 |  |
| [[CASC9]] | -0.66 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[CREBBP]] | -0.66 | -0.64 / -0.38 | both halves | 6e-05 |  |
| [[PATL2]] | -0.65 | -0.68 / -0.40 | both halves | 5e-05 |  |
| [[MED13]] | -0.63 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[RBM23]] | -0.61 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[BRAF]] | -0.61 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ATRX]] | -0.61 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.60 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[LPXN]] | -0.60 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAG2]] | B | JAG2 activity raises IMPDH1's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without JAG2 | 0.016 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises IMPDH1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GJA3]] | B | GJA3 activity raises IMPDH1's level | lines that do not express GJA3 (17) vs lines expressing it (33) | 1.25× lower at baseline in the lines without GJA3 | 0.034 | ⚠ within organs, on part of the lines; also absent: GBX1 |
| [[STARD9]] | B | STARD9 activity raises IMPDH1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without STARD9 | 0.048 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[PMP22]] | B | PMP22 activity raises IMPDH1's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.57× lower at baseline in the lines without PMP22 | 0.063 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[ANKRD13B]] | C | ANKRD13B activity raises IMPDH1's level | lines that do not express ANKRD13B (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without ANKRD13B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CAMKK1]] | C | CAMKK1 activity raises IMPDH1's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without CAMKK1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.6, 0.4); signed map (-41.5, -4.6). **Vector** length 89.1, 18.8% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.7 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.5 | -4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -13.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -27.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -13.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | inosine monophosphate dehydrogenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,392,277-128,409,986 (-) |
| Ensembl biotype | protein_coding |
| Also known as | sWSS2608, LCA11; previously RP10 |
| Gene groups (HGNC) | Inosine monophosphate dehydrogenase family |
| Reactome | 10 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Azathioprine ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P20839](https://www.uniprot.org/uniprotkb/P20839) (Inosine-5'-monophosphate dehydrogenase 1):

> Catalyzes the conversion of inosine 5'-phosphate (IMP) to xanthosine 5'-phosphate (XMP), the first committed and rate-limiting step in the de novo synthesis of guanine nucleotides, and therefore plays an important role in the regulation of cell growth. Could also have a single-stranded nucleic acid-binding activity and could play a role in RNA and/or DNA metabolism. It may also have a role in the development of malignancy and the growth progression of some tumors.

**Summary**, from NCBI Gene [3614](https://www.ncbi.nlm.nih.gov/gene/3614):

> The protein encoded by this gene acts as a homotetramer to regulate cell growth. The encoded protein is an enzyme that catalyzes the synthesis of xanthine monophosphate (XMP) from inosine-5'-monophosphate (IMP). This is the rate-limiting step in the de novo synthesis of guanine nucleotides. Defects in this gene are a cause of retinitis pigmentosa type 10 (RP10). Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:6052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6052) · Entrez [3614](https://www.ncbi.nlm.nih.gov/gene/3614) · UniProt [P20839](https://www.uniprot.org/uniprotkb/P20839) · Ensembl [ENSG00000106348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106348)

## Data

Gene col 2748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2748); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2748]; `tensor/DDL_lfc|DDL_z.npy` [2748]; `embed/gene_vectors.npy` [2748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2748 or target_col == 2748). Every well: [[IMPDH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IMPDH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
