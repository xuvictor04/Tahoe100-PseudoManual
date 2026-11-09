---
symbol: "USP2-AS1"
type: "gene"
col: 14424
ensembl_id: "ENSG00000245248"
name: "USP2 antisense RNA 1"
location: "11q23.3"
module: 18
arm: "+"
pooled_cpm: 14.35
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# USP2-AS1

*USP2 antisense RNA 1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.21× (z +21.1, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[NG25 (drug)]] 5 µM: 0.584× (z -4.1, q 0.022, down in 15 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (PANC-1 0.211×, C-33 A 0.0850×, A-427 0.227×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.212×, MIA PaCa-2 0.177×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.121×, PANC-1 0.255×; ⚠ cell-cycle shift, explains ~32% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAF4B]] (+0.66, fdr 7e-06), [[MIR17HG]] (+0.61, fdr 8e-06), [[GART]] (+0.61, fdr 1e-05); moves opposite to [[MOB4]] (-0.52, fdr 3e-05), [[SUCLG1]] (-0.49, fdr 1e-04), [[NFU1]] (-0.48, fdr 7e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.21×** | +21.1 | 0e+00 | 42/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +19.3 | 0e+00 | 32/44 (NCI-H1792, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.07×** | +16.5 | 0e+00 | 37/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.95×** | +15.9 | 0e+00 | 35/46 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +12.0 | 4e-31 | 10/17 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +8.9 | 4e-17 | 22/45 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +8.6 | 8e-16 | 21/37 (KATO III, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +7.8 | 6e-13 | 26/47 (HT-29, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +7.7 | 1e-12 | 13/25 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.2 | 3e-08 | 21/44 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +5.5 | 2e-06 | 17/47 (SW1417, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.3 | 5e-06 | 16/44 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.38×** | +4.7 | 1e-04 | 17/45 (A549, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 3e-04 | 16/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 3e-04 | 16/45 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.002 | 7/45 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.002 | 16/45 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.004 | 10/47 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.005 | 15/46 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14424.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (PANC-1 0.211×, C-33 A 0.0850×, A-427 0.227×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.212×, MIA PaCa-2 0.177×); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.121×, PANC-1 0.255×; ⚠ cell-cycle shift, explains ~32% of this change); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.584×** | -4.1 | 0.022 | 15/40 (HT-29, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.784× | -3.5 | 0.11 | 11/46 (NCI-H2030, RKO, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.796× | -3.3 | 0.16 | 4/46 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.799× | -3.1 | 0.25 | 9/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.25 | 12/46 (SW 900, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 55.9 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.5) |
| [[MIA PaCa-2 (line)]] | alt | 34.6 | 0 | 5 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.460× (z -17.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.177× (z -15.6) |
| [[KATO III (line)]] | alt | 12.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 13.7× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 58.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -17.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.7) |
| [[SW480 (line)]] | alt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.15× (z +11.4) | — |
| [[A-172 (line)]] | wt | 6.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +8.9) | — |
| [[A-427 (line)]] | wt | 21.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -9.3) |
| [[HS-578T (line)]] | alt | 12.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.78× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 6.51 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 6.40 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +10.1) | — |
| [[A549 (line)]] | wt | 10.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.82× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0850× (z -11.6) |
| [[H4 (line)]] | wt | 13.0 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0727× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 17.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 5.76 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.15× (z +9.6) | — |
| [[LoVo (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 4.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.01× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.0× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 6.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.98× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 9.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.5) | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0701× (z -9.8) |
| [[A498 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF4B]] | +0.66 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MIR17HG]] | +0.61 | +0.57 / +0.63 | both halves | 8e-06 |  |
| [[GART]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MACROD1]] | +0.60 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TXLNG]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[PUS7]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MDN1]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[LYRM4]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ZP3]] | +0.57 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[CMSS1]] | +0.57 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SEH1L]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PRMT3]] | +0.56 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB4]] | -0.52 | -0.60 / -0.43 | both halves | 3e-05 |  |
| [[SUCLG1]] | -0.49 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[NFU1]] | -0.48 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[SECISBP2L]] | -0.48 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[BPNT1]] | -0.47 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[ZHX1]] | -0.46 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[SUPT20H]] | -0.46 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[DCAF5]] | -0.45 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[ASB8]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[EXOC5]] | -0.45 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[ATP6V1A]] | -0.44 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[ILK]] | -0.44 | -0.54 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers USP2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WT1-AS]] | B | WT1-AS activity raises USP2-AS1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.50× lower at baseline in the lines without WT1-AS | 0.074 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.8, -42.7); signed map (-0.5, -55.7). **Vector** length 92.9, 20.0% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +19.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +4.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +21.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.5 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +7.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +1.8 | +2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.5 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[NG25 (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | USP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q23.3 — chr11:119,356,467-119,659,284 (+) |
| Ensembl biotype | lncRNA |
| Also known as | THY1-AS1, gLINC |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100499227](https://www.ncbi.nlm.nih.gov/gene/100499227):

> Predicted to enable U4 snRNA binding activity. Predicted to be involved in formation of quadruple SL/U4/U5/U6 snRNP and spliceosomal tri-snRNP complex assembly. Predicted to be part of U4/U6 x U5 tri-snRNP complex and U6 snRNP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:48673](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48673) · Entrez [100499227](https://www.ncbi.nlm.nih.gov/gene/100499227) · Ensembl [ENSG00000245248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245248)

## Data

Gene col 14424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14424); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14424]; `tensor/DDL_lfc|DDL_z.npy` [14424]; `embed/gene_vectors.npy` [14424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14424 or target_col == 14424). Every well: [[USP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
