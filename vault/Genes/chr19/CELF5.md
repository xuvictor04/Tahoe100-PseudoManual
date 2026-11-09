---
symbol: "CELF5"
type: "gene"
col: 8416
ensembl_id: "ENSG00000161082"
name: "CUGBP Elav-like family member 5"
location: "19p13.3"
module: 100
arm: "+"
pooled_cpm: 2.61
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# CELF5

*CUGBP Elav-like family member 5* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.64× (z +21.6, q 0e+00, up in 26 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.628× (z -4.7, q 0.002, down in 16 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LHX4]] (+0.77, fdr 7e-06), [[ITGA7]] (+0.75, fdr 1e-05), [[GSG1L]] (+0.73, fdr 7e-06).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SRRM3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.64×** | +21.6 | 0e+00 | 26/28 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **7.11×** | +19.6 | 0e+00 | 42/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.58×** | +17.1 | 0e+00 | 39/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.29×** | +16.8 | 0e+00 | 41/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **4.67×** | +15.4 | 0e+00 | 24/34 (SW480, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +13.1 | 2e-37 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.65×** | +12.9 | 3e-36 | 38/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.31×** | +11.9 | 5e-31 | 37/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +11.4 | 4e-28 | 16/32 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +10.4 | 1e-23 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +9.6 | 4e-20 | 23/33 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +9.3 | 9e-19 | 6/11 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.8 | 4e-07 | 7/22 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +5.5 | 2e-06 | 8/22 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +5.3 | 4e-06 | 5/26 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.2 | 9e-06 | 4/44 (NCI-H460, A-172, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.57×** | +4.9 | 3e-05 | 7/35 (NCI-H2030, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.37×** | +3.2 | 0.047 | 2/19 (C-33 A, HEC-1-A) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -4.7 | 0.002 | 16/39 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.662×** | -4.1 | 0.010 | 13/44 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.674×** | -3.9 | 0.015 | 9/33 (HEC-1-A, LoVo, …) | two highest doses |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.708×** | -3.4 | 0.079 | 1/44 (hTERT-HPNE) | inconsistent across doses |  |
| [[Neratinib (drug)]] 0.5 µM |  | 0.722× | -3.3 | 0.13 | 5/42 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.734× | -3.1 | 0.19 | 9/20 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.23 | 2 | 0 | [[Auranofin (drug)]] 5 µM 14.4× (z +9.7) | — |
| [[A498 (line)]] | wt | 3.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +9.6) | — |
| [[A549 (line)]] | wt | 3.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0426× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 1.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 3.44 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.162× (z -8.5) |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 1 | — | [[Lonafarnib (drug)]] 0.5 µM 0.132× (z -26.0) |
| [[A-172 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.838 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.898 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.770 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LHX4]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[ITGA7]] | +0.75 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[GSG1L]] | +0.73 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[CAMK2B]] | +0.73 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[MYO1F]] | +0.72 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[RYR1]] | +0.71 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.71 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.70 | +0.58 / +0.77 | both halves | 8e-06 | same gene group; STRING 405 |
| [[SYN1]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[CDH23]] | +0.69 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[SPTBN4]] | +0.66 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[EFHD1]] | +0.66 | +0.63 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | SRRM3 activity raises CELF5's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without SRRM3 | 0.031 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[LINC00595]] | B | LINC00595 activity raises CELF5's level | lines that do not express LINC00595 (9) vs lines expressing it (41) | 1.69× lower at baseline in the lines without LINC00595 | 0.039 | ⚠ within organs, on part of the lines; also absent: SUSD4, EBF4, SLC17A7; maybe low, not absent |
| [[KCNK13]] | B | KCNK13 activity raises CELF5's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without KCNK13 | 0.044 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[EPHA1-AS1]] | B | EPHA1-AS1 activity lowers CELF5's level | lines that do not express EPHA1-AS1 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without EPHA1-AS1 | 0.056 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[MAP3K9-DT]] | B | MAP3K9-DT activity raises CELF5's level | lines that do not express MAP3K9-DT (17) vs lines expressing it (33) | 1.49× lower at baseline in the lines without MAP3K9-DT | 0.065 | ⚠ within organs, on part of the lines; also absent: KIAA0319, STXBP2, SMPDL3B; maybe low, not absent |
| [[JPH3]] | B | JPH3 activity raises CELF5's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 1.62× lower at baseline in the lines without JPH3 | 0.067 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent |
| [[TMEM145]] | B | TMEM145 activity raises CELF5's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without TMEM145 | 0.069 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[CACNA1B]] | B | CACNA1B activity raises CELF5's level | lines that do not express CACNA1B (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without CACNA1B | 0.071 | ⚠ within organs, on part of the lines; also absent: DGCR5, PPP1R14C; maybe low, not absent |
| [[DPYSL5]] | B | DPYSL5 activity raises CELF5's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.65× lower at baseline in the lines without DPYSL5 | 0.074 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[DISP3]] | B | DISP3 activity raises CELF5's level | lines that do not express DISP3 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without DISP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02609, DPF1, ARHGEF26 |
| [[NKAIN1]] | C | NKAIN1 activity raises CELF5's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without NKAIN1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.7, 34.7); signed map (26.8, 19.7). **Vector** length 51.0, 6.76% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +9.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +1.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CUGBP Elav-like family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,224,661-3,297,076 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BRUNOL5 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6W0](https://www.uniprot.org/uniprotkb/Q8N6W0) (CUGBP Elav-like family member 5):

> RNA-binding protein implicated in the regulation of pre-mRNA alternative splicing. Mediates exon inclusion and/or exclusion in pre-mRNA that are subject to tissue-specific and developmentally regulated alternative splicing. Specifically activates exon 5 inclusion of cardiac isoforms of TNNT2 during heart remodeling at the juvenile to adult transition. Binds to muscle-specific splicing enhancer (MSE) intronic sites flanking the alternative exon 5 of TNNT2 pre-mRNA.

**Summary**, from NCBI Gene [60680](https://www.ncbi.nlm.nih.gov/gene/60680):

> This gene encodes a member of the the CELF/BRUNOL protein family, which contain two N-terminal RNA recognition motif (RRM) domains, one C-terminal RRM domain, and a divergent segment of 160-230 aa between the second and third RRM domains. Members of this protein family regulate pre-mRNA alternative splicing and may also be involved in mRNA editing and translation. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:14058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14058) · Entrez [60680](https://www.ncbi.nlm.nih.gov/gene/60680) · UniProt [Q8N6W0](https://www.uniprot.org/uniprotkb/Q8N6W0) · Ensembl [ENSG00000161082](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161082)

## Data

Gene col 8416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8416); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8416]; `tensor/DDL_lfc|DDL_z.npy` [8416]; `embed/gene_vectors.npy` [8416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8416 or target_col == 8416). Every well: [[CELF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
