---
symbol: "DNAH6"
type: "gene"
col: 3674
ensembl_id: "ENSG00000115423"
name: "dynein axonemal heavy chain 6"
location: "2p11.2"
module: 27
arm: "+"
pooled_cpm: 6.75
n_lines_expressing: 46
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 26
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# DNAH6

*dynein axonemal heavy chain 6* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.30× (z +13.4, q 6e-38, up in 41 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.511× (z -5.7, q 7e-06, down in 19 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS6]] (+0.65, fdr 1e-05), [[KSR2]] (+0.61, fdr 7e-06), [[C12orf50]] (+0.61, fdr 1e-05); moves opposite to [[GPR89A]] (-0.55, fdr 3e-05), [[ZNF595]] (-0.54, fdr 3e-05), [[DCUN1D2]] (-0.53, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CD70]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FOXP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.30×** | +13.4 | 6e-38 | 41/43 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +12.0 | 7e-31 | 23/36 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.60×** | +11.5 | 4e-28 | 27/37 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.40×** | +10.4 | 3e-23 | 38/42 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.43×** | +9.9 | 6e-21 | 38/43 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.11×** | +9.0 | 2e-17 | 29/43 (NCI-H460, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.82×** | +8.8 | 1e-16 | 14/25 (HOP62, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.56×** | +7.7 | 1e-12 | 7/8 (HEC-1-A, HT-29, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.43×** | +7.3 | 3e-11 | 24/39 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +6.9 | 3e-10 | 18/36 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.89×** | +6.9 | 3e-10 | 30/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.40×** | +6.9 | 3e-10 | 5/10 (SK-MEL-2, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.11×** | +6.3 | 1e-08 | 22/41 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.3 | 1e-08 | 15/44 (NCI-H460, A549, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **3.73×** | +5.9 | 2e-07 | 20/40 (LoVo, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +5.8 | 2e-07 | 25/40 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.81×** | +4.9 | 4e-05 | 16/39 (SW480, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.002 | 18/42 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3674.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.511×** | -5.7 | 7e-06 | 19/42 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.706×** | -4.2 | 0.008 | 16/42 (KATO III, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.631×** | -3.7 | 0.046 | 15/39 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.663×** | -3.5 | 0.066 | 16/43 (SHP-77, HEC-1-A, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.697× | -3.1 | 0.24 | 6/42 (hTERT-HPNE, KATO III, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.702× | -3.0 | 0.25 | 11/43 (J82, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.66 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 34.2 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0474× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0833× (z -13.4) |
| [[A-172 (line)]] | wt | 5.05 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.8× (z +14.8) | — |
| [[NCI-H460 (line)]] | wt | 3.10 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 7.65× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0792× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.133× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 52.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +14.9) | — |
| [[A498 (line)]] | wt | 2.52 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 24.7× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0744× (z -9.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 3.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 7.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0818× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 3.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 2.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.5× (z +10.1) | — |
| [[A-427 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS6]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[KSR2]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[C12orf50]] | +0.61 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[TMEM232]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[NCALD]] | +0.60 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[LINC01933]] | +0.60 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[LINC00992]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ANOS2P]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[DNAH7]] | +0.58 | +0.67 / +0.54 | both halves | 1e-05 | same gene group; STRING 583 |
| [[MIR4500HG]] | +0.57 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[FOXP1]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SLCO2B1]] | +0.56 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89A]] | -0.55 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ZNF595]] | -0.54 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[DCUN1D2]] | -0.53 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[ZNF549]] | -0.52 | -0.61 / -0.29 | both halves | 2e-04 |  |
| [[GPR89B]] | -0.52 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[ZCCHC17]] | -0.50 | -0.56 / -0.37 | both halves | 9e-05 |  |
| [[DENND10]] | -0.49 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ZBTB49]] | -0.49 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[SS18L1]] | -0.49 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[MFSD8]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZNF767P-1]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CDK5RAP1]] | -0.48 | -0.54 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD70]] | B | CD70 activity raises DNAH6's level | lines that do not express CD70 (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without CD70 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, MEG8, MEG3 |
| [[TOP2A]] | B | TOP2A activity lowers DNAH6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLCO2B1]] | B | SLCO2B1 activity raises DNAH6's level | lines that do not express SLCO2B1 (21) vs lines expressing it (29) | 1.46× lower at baseline in the lines without SLCO2B1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000253227, ENSG00000254261, PDE1C; maybe low, not absent |
| [[RNF183]] | B | RNF183 activity raises DNAH6's level | lines that do not express RNF183 (36) vs lines expressing it (14) | 1.94× lower at baseline in the lines without RNF183 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, LINC02964, VIL1 |
| [[LINC00992]] | B | LINC00992 activity raises DNAH6's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without LINC00992 | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXP1]] | C | DNAH6 activity raises FOXP1's level | lines that do not express DNAH6 (4) vs lines expressing it (46) | 3.32× lower at baseline in the lines without DNAH6 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IQCM, LINC02932, LINC00907; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.499). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.3, 39.8); signed map (55.6, 17.0). **Vector** length 73.9, 14.2% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +5.4 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.5 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.5 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +4.9 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -1.7 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.4 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:84,516,455-84,819,589 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dnahc6, HL-2, FLJ37357; previously DNHL1 |
| Gene groups (HGNC) | Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0G6](https://www.uniprot.org/uniprotkb/Q9C0G6) (Dynein axonemal heavy chain 6):

> Force generating protein of respiratory cilia. Produces force towards the minus ends of microtubules. Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP (By similarity).

**Summary**, from NCBI Gene [1768](https://www.ncbi.nlm.nih.gov/gene/1768):

> This gene belongs to the dynein family, whose members encode large proteins that are constituents of the microtubule-associated motor protein complex. This complex is composed of dynein heavy, intermediate and light chains, which can be axonemal or cytoplasmic. This protein is an axonemal dynein heavy chain. It is involved in producing force for ciliary beating by using energy from ATP hydrolysis. Mutations in this gene may cause primary ciliary dyskinesia (PCD) as well as heterotaxy. [provided …

**Accessions** — [HGNC:2951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2951) · Entrez [1768](https://www.ncbi.nlm.nih.gov/gene/1768) · UniProt [Q9C0G6](https://www.uniprot.org/uniprotkb/Q9C0G6) · Ensembl [ENSG00000115423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115423)

## Data

Gene col 3674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3674); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3674]; `tensor/DDL_lfc|DDL_z.npy` [3674]; `embed/gene_vectors.npy` [3674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3674 or target_col == 3674). Every well: [[DNAH6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
