---
symbol: "NCR3LG1"
type: "gene"
col: 11987
ensembl_id: "ENSG00000188211"
name: "natural killer cell cytotoxicity receptor 3 ligand 1"
location: "11p15.1"
module: 3
arm: "-"
pooled_cpm: 12.04
n_lines_expressing: 43
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 30
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# NCR3LG1

*natural killer cell cytotoxicity receptor 3 ligand 1* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.52× (z +26.1, q 0e+00, up in 31 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.185×, SW480 0.319×); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (SW48 0.0544×); [[Menadione (drug)]] 0.05 µM in 1 line (SW48 0.0608×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF121]] (+0.68, fdr 8e-06), [[COA7]] (+0.66, fdr 7e-06), [[POGLUT1]] (+0.66, fdr 2e-05); moves opposite to [[PIN1]] (-0.68, fdr 1e-05), [[COX6A1]] (-0.68, fdr 1e-05), [[CBFA2T2]] (-0.68, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC38A1]] → it (grade C ⚠); 4 go from it, the strongest it → [[ECHDC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11987.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.52×** | +26.1 | 0e+00 | 31/38 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.01×** | +16.3 | 0e+00 | 30/40 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.13×** | +13.9 | 7e-42 | 32/39 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +12.5 | 1e-33 | 19/25 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.0 | 6e-26 | 15/19 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +10.1 | 4e-22 | 19/31 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +9.8 | 1e-20 | 22/38 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **2.15×** | +9.3 | 8e-19 | 32/41 (J82, A498, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +8.8 | 6e-17 | 24/40 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.03×** | +8.7 | 3e-16 | 30/41 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +7.5 | 3e-12 | 26/40 (SNU-423, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.4 | 6e-12 | 18/34 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +7.3 | 1e-11 | 24/41 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +7.1 | 7e-11 | 20/41 (SW1417, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +6.6 | 1e-09 | 20/32 (hTERT-HPNE, J82, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +6.6 | 2e-09 | 20/41 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +6.4 | 5e-09 | 21/40 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +5.1 | 9e-06 | 16/40 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +4.8 | 6e-05 | 19/41 (NCI-H460, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.3 | 5e-04 | 14/41 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.003 | 12/41 (LoVo, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (SHP-77 0.185×, SW480 0.319×); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (SW48 0.0544×); [[Menadione (drug)]] 0.05 µM in 1 line (SW48 0.0608×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.98 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.1× (z +20.8) | — |
| [[SW48 (line)]] | wt | 32.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.5) | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0544× (z -13.5) |
| [[A498 (line)]] | wt | 17.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +16.9) | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +14.7) | [[Ligustrazine (drug)]] 0.05 µM 0.0677× (z -9.6) |
| [[J82 (line)]] | alt | 16.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +19.9) | — |
| [[LoVo (line)]] | wt | 25.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.78× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 6.11 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +15.1) | — |
| [[A-427 (line)]] | wt | 32.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.5) |
| [[BT-474 (line)]] | alt | 7.99 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +12.3) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.109× (z -8.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 5.03 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 7.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +17.5) | — |
| [[RPMI-7951 (line)]] | alt | 9.27 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.37× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -10.8) |
| [[SNU-423 (line)]] | alt | 5.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.0× (z +16.7) | — |
| [[AsPC-1 (line)]] | alt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +15.3) | — |
| [[COLO 205 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 8.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 35.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.567× (z -8.8) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 3.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 8.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 6.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.82× (z +10.1) | — |
| [[SW480 (line)]] | alt | 21.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -8.5) |
| [[A-172 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF121]] | +0.68 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[COA7]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[POGLUT1]] | +0.66 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[SNHG26]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[UTP20]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ABCE1]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[KICS2]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SLC16A9]] | +0.63 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[GPATCH4]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD18A]] | +0.62 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[PRRC2B]] | +0.62 | +0.48 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIN1]] | -0.68 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.68 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.68 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.67 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.66 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[RANBP10]] | -0.66 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[GBF1]] | -0.65 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MACO1]] | -0.64 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.64 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[TSC2]] | -0.64 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[MTM1]] | -0.63 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[SPSB3]] | -0.63 | -0.53 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC38A1]] | C | SLC38A1 activity raises NCR3LG1's level | lines that do not express SLC38A1 (3) vs lines expressing it (47) | 2.68× lower at baseline in the lines without SLC38A1 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ALPK3, TRIB3, SAMHD1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ECHDC1]] | B | NCR3LG1 activity raises ECHDC1's level | lines that do not express NCR3LG1 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without NCR3LG1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000260196; maybe low, not absent |
| [[ZNF121]] | B | NCR3LG1 activity raises ZNF121's level | lines that do not express NCR3LG1 (7) vs lines expressing it (43) | 1.52× lower at baseline in the lines without NCR3LG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000260196; maybe low, not absent |
| [[ZNF195]] | B | NCR3LG1 activity raises ZNF195's level | lines that do not express NCR3LG1 (7) vs lines expressing it (43) | 1.69× lower at baseline in the lines without NCR3LG1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000260196; maybe low, not absent |
| [[MAK16]] | B | NCR3LG1 activity raises MAK16's level | lines that do not express NCR3LG1 (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without NCR3LG1 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000260196; maybe low, not absent |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.677). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (2.5, -16.3); signed map (23.0, -34.6). **Vector** length 95.2, 20.8% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +7.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +10.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.2 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | natural killer cell cytotoxicity receptor 3 ligand 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:17,351,800-17,377,341 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686O24166, B7-H6 |
| Gene groups (HGNC) | Receptor ligands; C1-set domain containing; B7 family |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68D85](https://www.uniprot.org/uniprotkb/Q68D85) (Natural cytotoxicity triggering receptor 3 ligand 1):

> Triggers NCR3-dependent natural killer cell activation.

**Summary**, from NCBI Gene [374383](https://www.ncbi.nlm.nih.gov/gene/374383):

> B7H6 belongs to the B7 family (see MIM 605402) and is selectively expressed on tumor cells. Interaction of B7H6 with NKp30 (NCR3; MIM 611550) results in natural killer (NK) cell activation and cytotoxicity (Brandt et al., 2009 [PubMed 19528259]).[supplied by OMIM, Jan 2011]

**Accessions** — [HGNC:42400](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42400) · Entrez [374383](https://www.ncbi.nlm.nih.gov/gene/374383) · UniProt [Q68D85](https://www.uniprot.org/uniprotkb/Q68D85) · Ensembl [ENSG00000188211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188211)

## Data

Gene col 11987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11987); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11987]; `tensor/DDL_lfc|DDL_z.npy` [11987]; `embed/gene_vectors.npy` [11987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11987 or target_col == 11987). Every well: [[NCR3LG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCR3LG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
