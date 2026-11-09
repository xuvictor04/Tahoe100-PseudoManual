---
symbol: "LAMA2"
type: "gene"
col: 12239
ensembl_id: "ENSG00000196569"
name: "laminin subunit alpha 2"
location: "6q22.33"
module: 150
arm: "+"
pooled_cpm: 10.47
n_lines_expressing: 41
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# LAMA2

*laminin subunit alpha 2* — 6q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.44× (z +30.1, q 0e+00, up in 26 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.153×, SK-MEL-2 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW48 0.0641×, LoVo 0.233×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0896×); [[Proglumide (drug)]] 0.5 µM in 1 line (LS 180 0.0586×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.156×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD7B]] (+0.71, fdr 1e-05), [[GRIA4]] (+0.68, fdr 9e-06), [[MYO16]] (+0.68, fdr 2e-05); moves opposite to [[WRAP73]] (-0.60, fdr 8e-04, ⚠ one half only (not replicated)), [[RAB40B]] (-0.58, fdr 1e-04), [[SERAC1]] (-0.58, fdr 6e-04), [[MIGA2]] (-0.56, fdr 4e-04).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PGBD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.44×** | +30.1 | 0e+00 | 26/35 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.46×** | +25.1 | 0e+00 | 27/35 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.36×** | +16.0 | 0e+00 | 10/19 (CFPAC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.95×** | +15.5 | 0e+00 | 24/37 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.93×** | +15.4 | 0e+00 | 27/34 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +15.2 | 0e+00 | 17/25 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.59×** | +13.1 | 4e-37 | 28/36 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +12.8 | 2e-35 | 24/39 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +10.1 | 3e-22 | 7/13 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +9.4 | 3e-19 | 17/39 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.87×** | +9.0 | 2e-17 | 18/36 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +7.4 | 5e-12 | 15/35 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.3 | 1e-11 | 14/35 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.8 | 2e-07 | 16/38 (NCI-H23, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +5.5 | 1e-06 | 10/36 (SW480, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 4e-04 | 12/37 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.006 | 0/36 | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.009 | 5/33 (MIA PaCa-2, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (LoVo 0.153×, SK-MEL-2 0.126×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (SW48 0.0641×, LoVo 0.233×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0896×); [[Proglumide (drug)]] 0.5 µM in 1 line (LS 180 0.0586×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.156×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Salicylic acid (drug)]] 5 µM |  | 0.851× | -3.3 | 0.57 | 5/39 (J82, CHP-212, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.811× | -3.0 | 0.71 | 13/36 (SHP-77, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 8.35 | 9 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 15.4× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.90 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +12.9) | — |
| [[NCI-H460 (line)]] | wt | 2.96 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +14.8) | — |
| [[NCI-H2030 (line)]] | alt | 4.17 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +11.7) | — |
| [[HOP62 (line)]] | alt | 4.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +11.6) | — |
| [[LoVo (line)]] | wt | 54.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 5.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 3.26 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +11.2) | [[Proglumide (drug)]] 0.5 µM 0.0586× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 15.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +11.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0896× (z -12.5) |
| [[SW48 (line)]] | wt | 60.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0641× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +11.0) | — |
| [[C32 (line)]] | wt | 4.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +9.2) | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 7.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +10.9) | — |
| [[J82 (line)]] | alt | 3.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.00× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 4.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +12.6) | — |
| [[SW480 (line)]] | alt | 3.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.87× (z +12.9) | — |
| [[A-427 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD7B]] | +0.71 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[GRIA4]] | +0.68 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[MYO16]] | +0.68 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[CFLAR-AS1]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.66 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[LINC02268]] | +0.64 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[ANKRD31]] | +0.64 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[LRRC4C]] | +0.62 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[IPCEF1]] | +0.61 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[COL28A1]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 | pathway: Extracellular matrix organization |
| [[PCNX4-DT]] | +0.61 | +0.64 / +0.25 | both halves | 4e-04 |  |
| [[CFAP54]] | +0.60 | +0.56 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.60 | -0.52 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RAB40B]] | -0.58 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[SERAC1]] | -0.58 | -0.51 / -0.21 | both halves | 6e-04 |  |
| [[MIGA2]] | -0.56 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[MTMR12]] | -0.56 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[CABLES2]] | -0.56 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[FN3KRP]] | -0.56 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[GNA12]] | -0.56 | -0.61 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[SDHAP1]] | -0.56 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.56 | -0.39 / -0.24 | both halves | 4e-04 |  |
| [[RNF41]] | -0.55 | -0.45 / -0.23 | both halves | 5e-04 |  |
| [[SDHAP2]] | -0.55 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.55 | -0.51 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LAMA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANGPT1]] | B | ANGPT1 activity raises LAMA2's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without ANGPT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[FAP]] | B | FAP activity raises LAMA2's level | lines that do not express FAP (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without FAP | 0.090 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGBD4]] | B | LAMA2 activity lowers PGBD4's level | lines that do not express LAMA2 (9) vs lines expressing it (41) | 1.13× higher at baseline in the lines without LAMA2 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC00243, DCBLD2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.0, 26.8); signed map (30.1, 12.1). **Vector** length 78.2, 15.2% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +30.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.6 | +15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +25.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.3 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.0 | +16.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +5.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -0.7 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.33 — chr6:128,883,138-129,516,566 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LAMM |
| Gene groups (HGNC) | Laminin subunits |
| Hallmark sets | MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 20 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P24043](https://www.uniprot.org/uniprotkb/P24043) (Laminin subunit alpha-2):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components.

**Summary**, from NCBI Gene [3908](https://www.ncbi.nlm.nih.gov/gene/3908):

> Laminin, an extracellular protein, is a major component of the basement membrane. It is thought to mediate the attachment, migration, and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components. It is composed of three subunits, alpha, beta, and gamma, which are bound to each other by disulfide bonds into a cross-shaped molecule. This gene encodes the alpha 2 chain, which constitutes one of the subunits of laminin 2 (merosin) and …

**Accessions** — [HGNC:6482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6482) · Entrez [3908](https://www.ncbi.nlm.nih.gov/gene/3908) · UniProt [P24043](https://www.uniprot.org/uniprotkb/P24043) · Ensembl [ENSG00000196569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196569)

## Data

Gene col 12239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12239); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12239]; `tensor/DDL_lfc|DDL_z.npy` [12239]; `embed/gene_vectors.npy` [12239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12239 or target_col == 12239). Every well: [[LAMA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
