---
symbol: "COL28A1"
type: "gene"
col: 13239
ensembl_id: "ENSG00000215018"
name: "collagen type XXVIII alpha 1 chain"
location: "7p21.3"
module: 68
arm: "+"
pooled_cpm: 3.13
n_lines_expressing: 47
n_dd_up: 41
n_dd_down: 1
n_dd_up_clean: 32
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# COL28A1

*collagen type XXVIII alpha 1 chain* — 7p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 16.9× (z +39.0, q 0e+00, up in 30 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.660× (z -4.1, q 0.026, down in 15 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0950×; ⚠ toxic; transcription drop); [[Dimethyl fumarate (drug)]] 0.05 µM in 1 line (A-172 0.0755×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01933]] (+0.76, fdr 7e-06), [[DNAH12]] (+0.75, fdr 7e-06), [[CHODL]] (+0.74, fdr 7e-06); moves opposite to [[GTPBP3]] (-0.63, fdr 1e-04), [[TAF5L]] (-0.62, fdr 8e-05), [[GFOD2]] (-0.61, fdr 2e-04).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[CNN3-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13239.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **16.9×** | +39.0 | 0e+00 | 30/31 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.97×** | +30.2 | 0e+00 | 31/31 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.89×** | +20.1 | 0e+00 | 27/30 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **6.45×** | +17.5 | 0e+00 | 30/36 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.68×** | +16.9 | 0e+00 | 31/35 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **3.05×** | +15.4 | 0e+00 | 32/40 (A498, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.98×** | +12.9 | 2e-36 | 20/25 (LS 180, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +11.5 | 9e-29 | 24/31 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.09×** | +10.1 | 3e-22 | 19/40 (A498, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +10.0 | 6e-22 | 4/6 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.64×** | +9.4 | 2e-19 | 21/38 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +8.7 | 1e-16 | 3/9 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +8.0 | 7e-14 | 2/13 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.25×** | +7.9 | 1e-13 | 19/40 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +6.8 | 3e-10 | 18/42 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +6.4 | 6e-09 | 21/33 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.89×** | +6.2 | 2e-08 | 11/41 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +5.5 | 9e-07 | 18/39 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13239.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H2030 0.0950×; ⚠ toxic; transcription drop); [[Dimethyl fumarate (drug)]] 0.05 µM in 1 line (A-172 0.0755×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -4.1 | 0.026 | 15/31 (SNU-423, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13239. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.66 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.2× (z +21.7) | — |
| [[A-172 (line)]] | wt | 10.7 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 98.2× (z +23.2) | [[Dimethyl fumarate (drug)]] 0.05 µM 0.0755× (z -8.6) |
| [[SW480 (line)]] | alt | 1.34 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +12.6) | — |
| [[LoVo (line)]] | wt | 1.64 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.5× (z +14.1) | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +16.8) | — |
| [[NCI-H460 (line)]] | wt | 1.58 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 1.26 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.0× (z +13.5) | — |
| [[SK-MEL-2 (line)]] | alt | 5.02 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 50.8× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 9.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 7.14 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 1.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 2.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.3× (z +12.6) | — |
| [[NCI-H2030 (line)]] | alt | 8.11 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +10.7) | [[Digitoxin (drug)]] 5 µM 0.0950× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 4.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +16.6) | — |
| [[AsPC-1 (line)]] | alt | 1.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.9× (z +10.5) | — |
| [[C32 (line)]] | wt | 2.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 3.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +13.7) | — |
| [[J82 (line)]] | alt | 1.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 63.3× (z +13.3) | — |
| [[KATO III (line)]] | alt | 2.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.5× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 3.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 6.26 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +13.8) | — |
| [[A-427 (line)]] | wt | 0.652 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.748 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.987 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13239), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01933]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[CHODL]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[NEB]] | +0.73 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[LINC00240]] | +0.73 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[DNAH3]] | +0.72 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[HSD11B1-AS1]] | +0.72 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.71 | +0.77 / +0.36 | both halves | 1e-04 |  |
| [[LINC01090]] | +0.70 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[KCNAB1]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ANGPT2]] | +0.70 | +0.72 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTPBP3]] | -0.63 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[TAF5L]] | -0.62 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[GFOD2]] | -0.61 | -0.67 / -0.32 | both halves | 2e-04 |  |
| [[EFCAB14]] | -0.61 | -0.64 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COL28A1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC02889]] | B | LINC02889 activity raises COL28A1's level | lines that do not express LINC02889 (12) vs lines expressing it (38) | 1.75× lower at baseline in the lines without LINC02889 | 0.026 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, SAMD5, ENSG00000226640; maybe low, not absent |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises COL28A1's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without MTUS1-DT | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[HLA-V-1]] | B | HLA-V-1 activity raises COL28A1's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.30× lower at baseline in the lines without HLA-V-1 | 0.047 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[LRRN1]] | B | LRRN1 activity raises COL28A1's level | lines that do not express LRRN1 (31) vs lines expressing it (19) | 1.47× lower at baseline in the lines without LRRN1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TACSTD2, PRKCH-AS1, SERPINB3; maybe low, not absent |
| [[KMO]] | B | KMO activity raises COL28A1's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without KMO | 0.080 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNN3-DT]] | C | COL28A1 activity lowers CNN3-DT's level | lines that do not express COL28A1 (3) vs lines expressing it (47) | 2.00× higher at baseline in the lines without COL28A1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC6, KIFC3, MLLT3; maybe low, not absent |
| [[LINC01429]] | C | COL28A1 activity lowers LINC01429's level | lines that do not express COL28A1 (3) vs lines expressing it (47) | 3.54× higher at baseline in the lines without COL28A1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC6, KIFC3, MLLT3; maybe low, not absent; its own permutation p |
| [[SYNPO2]] | C | COL28A1 activity lowers SYNPO2's level | lines that do not express COL28A1 (3) vs lines expressing it (47) | 3.52× higher at baseline in the lines without COL28A1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC6, KIFC3, MLLT3; maybe low, not absent; its own permutation p |
| [[LACTB2]] | C | COL28A1 activity lowers LACTB2's level | lines that do not express COL28A1 (3) vs lines expressing it (47) | 1.63× higher at baseline in the lines without COL28A1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNAJC6, KIFC3, MLLT3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (10.9, 16.7); signed map (25.8, 2.5). **Vector** length 75.2, 13.6% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +39.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.5 | +16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +30.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +20.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +15.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.6 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | +5.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +0.5 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XXVIII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.3 — chr7:7,356,203-7,535,873 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Collagens |
| Reactome | 4 pathways, smallest: Collagen chain trimerization; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2UY09](https://www.uniprot.org/uniprotkb/Q2UY09) (Collagen alpha-1(XXVIII) chain):

> May act as a cell-binding protein.

**Summary**, from NCBI Gene [340267](https://www.ncbi.nlm.nih.gov/gene/340267):

> COL28A1 belongs to a class of collagens containing von Willebrand factor (VWF; MIM 613160) type A (VWFA) domains (Veit et al., 2006 [PubMed 16330543]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:22442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22442) · Entrez [340267](https://www.ncbi.nlm.nih.gov/gene/340267) · UniProt [Q2UY09](https://www.uniprot.org/uniprotkb/Q2UY09) · Ensembl [ENSG00000215018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215018)

## Data

Gene col 13239: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13239); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13239, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13239]; `tensor/DDL_lfc|DDL_z.npy` [13239]; `embed/gene_vectors.npy` [13239]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13239 or target_col == 13239). Every well: [[COL28A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL28A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
