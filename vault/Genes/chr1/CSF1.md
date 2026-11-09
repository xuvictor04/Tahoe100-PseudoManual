---
symbol: "CSF1"
type: "gene"
col: 11527
ensembl_id: "ENSG00000184371"
name: "colony stimulating factor 1"
location: "1p13.3"
module: 14
arm: "+"
pooled_cpm: 44.29
n_lines_expressing: 29
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 14
direction_downstream: 11
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CSF1

*colony stimulating factor 1* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 12.3× (z +38.8, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.485× (z -7.9, q 1e-12, down in 18 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP2]] (+0.77, fdr 7e-06), [[DENND2B]] (+0.76, fdr 7e-06), [[VCAM1]] (+0.75, fdr 7e-06); moves opposite to [[DIP2A]] (-0.54, fdr 2e-05), [[WDR37]] (-0.53, fdr 1e-05), [[ZCCHC17]] (-0.52, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LINC02605]] → it (grade B ⚠); 11 go from it, the strongest it → [[CFL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11527.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **12.3×** | +38.8 | 0e+00 | 26/26 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **10.6×** | +24.8 | 0e+00 | 26/27 (SNU-423, J82, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.77×** | +22.4 | 0e+00 | 25/26 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.33×** | +16.0 | 0e+00 | 22/27 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +12.9 | 4e-36 | 23/26 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **9.20×** | +12.7 | 6e-35 | 26/27 (SNU-1, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.05×** | +12.2 | 2e-32 | 24/27 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.2 | 2e-18 | 11/27 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +9.0 | 2e-17 | 20/24 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.26×** | +8.9 | 2e-17 | 16/26 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +7.2 | 3e-11 | 14/27 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.79×** | +6.4 | 8e-09 | 16/27 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.69×** | +5.7 | 6e-07 | 21/24 (HEC-1-A, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.0 | 2e-05 | 13/27 (A498, HS-578T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +4.4 | 4e-04 | 10/27 (Hs 766T, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.003 | 9/27 (A-172, HOP62, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.009 | 10/27 (MIA PaCa-2, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.009 | 11/27 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11527.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.485×** | -7.9 | 1e-12 | 18/27 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -6.6 | 9e-09 | 16/27 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -6.5 | 1e-08 | 14/27 (MIA PaCa-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.677×** | -4.3 | 0.003 | 15/26 (SW 1088, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.739× | -3.3 | 0.10 | 9/27 (H4, NCI-H661, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.577× | -3.2 | 0.15 | 12/26 (SW 1088, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 0.806× | -3.0 | 0.20 | 4/27 (J82, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11527. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 47.4 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +18.4) | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -14.3) |
| [[SNU-1 (line)]] | wt | 167 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.77× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.0639× (z -19.3) |
| [[A-172 (line)]] | wt | 64.9 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.88× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 168 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +16.1) | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +22.8) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +16.3) | — |
| [[PANC-1 (line)]] | alt | 40.4 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +21.3) | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -9.6) |
| [[SW48 (line)]] | wt | 18.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.7× (z +16.6) | — |
| [[SNU-423 (line)]] | alt | 42.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +23.6) | — |
| [[A549 (line)]] | wt | 21.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.8× (z +23.0) | — |
| [[HEC-1-A (line)]] | alt | 14.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.9× (z +26.1) | — |
| [[Hs 766T (line)]] | wt | 43.6 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +16.4) | [[Panobinostat (drug)]] 5 µM 0.241× (z -8.5) |
| [[J82 (line)]] | alt | 41.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.8× (z +24.5) | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.7× (z +25.2) | — |
| [[HepG2_C3A (line)]] | wt | 20.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 55.0× (z +21.5) | — |
| [[HOP62 (line)]] | alt | 21.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.5× (z +21.3) | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.8× (z +21.4) | — |
| [[SK-MEL-2 (line)]] | alt | 19.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +16.2) | — |
| [[RPMI-7951 (line)]] | alt | 46.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +13.2) | — |
| [[A498 (line)]] | wt | 553 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.288× (z -9.0) |
| [[H4 (line)]] | wt | 32.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +12.7) | — |
| [[RKO (line)]] | wt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +15.6) | — |
| [[SW 1088 (line)]] | alt | 94.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +8.8) | — |
| [[A-427 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.08 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11527), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP2]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DENND2B]] | +0.76 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[VCAM1]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 | STRING 542 |
| [[STAT5A]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 458 |
| [[SLC2A6]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CX3CL1]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 605 |
| [[NFKBIA]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 519 |
| [[LINC02605]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[ANKRD33B]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[BCL3]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[DRAM1]] | +0.65 | +0.68 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CXCL2]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 711 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[WDR37]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 6, C 8. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02605]] | B | LINC02605 activity raises CSF1's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 2.75× lower at baseline in the lines without LINC02605 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517 |
| [[HDAC6]] | B | HDAC6 activity raises CSF1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers CSF1's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RBMS3]] | B | RBMS3 activity raises CSF1's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 2.96× lower at baseline in the lines without RBMS3 | 0.048 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472 |
| [[SLC2A6]] | B | SLC2A6 activity raises CSF1's level | lines that do not express SLC2A6 (6) vs lines expressing it (44) | 3.03× lower at baseline in the lines without SLC2A6 | 0.057 | ⚠ within organs, on part of the lines; also absent: GFOD1, SOAT1, RGS9; maybe low, not absent |
| [[CFH]] | B | CFH activity raises CSF1's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.44× lower at baseline in the lines without CFH | 0.096 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[TNFAIP6]] | C | TNFAIP6 activity raises CSF1's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 3.10× lower at baseline in the lines without TNFAIP6 | 0.025 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[ANKRD33B]] | C | ANKRD33B activity raises CSF1's level | lines that do not express ANKRD33B (15) vs lines expressing it (35) | 2.62× lower at baseline in the lines without ANKRD33B | 0.037 | ⚠ within organs, on part of the lines; also absent: JCAD, FAT4, ARHGAP22; co-absent with the target |
| [[SRGN]] | C | SRGN activity raises CSF1's level | lines that do not express SRGN (30) vs lines expressing it (20) | 3.10× lower at baseline in the lines without SRGN | 0.041 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[CNTNAP1]] | C | CNTNAP1 activity raises CSF1's level | lines that do not express CNTNAP1 (4) vs lines expressing it (46) | 3.71× lower at baseline in the lines without CNTNAP1 | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZCCHC24, KIF17, SLC29A4 |
| [[RRAD]] | C | RRAD activity raises CSF1's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.36× lower at baseline in the lines without RRAD | 0.068 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |
| [[CFL2]] | C | CFL2 activity raises CSF1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 3.38× lower at baseline in the lines without CFL2 | 0.075 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | B | CSF1 activity raises CFL2's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.12× lower at baseline in the lines without CSF1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[LINC02605]] | B | CSF1 activity raises LINC02605's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.14× lower at baseline in the lines without CSF1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[RBM43]] | B | CSF1 activity raises RBM43's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.87× lower at baseline in the lines without CSF1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[SLC2A6]] | B | CSF1 activity raises SLC2A6's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without CSF1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[NFKB1]] | B | CSF1 activity raises NFKB1's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without CSF1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[NFKBIA]] | B | CSF1 activity raises NFKBIA's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without CSF1 | 0.074 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[EBI3]] | B | CSF1 activity raises EBI3's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without CSF1 | 0.077 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[TIFA]] | B | CSF1 activity raises TIFA's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 1.26× lower at baseline in the lines without CSF1 | 0.095 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[ANKRD33B]] | C | CSF1 activity raises ANKRD33B's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 3.89× lower at baseline in the lines without CSF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1; co-absent with the target |
| [[TNFAIP6]] | C | CSF1 activity raises TNFAIP6's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.46× lower at baseline in the lines without CSF1 | 0.041 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1; co-absent with the target |
| [[SLFN12]] | C | CSF1 activity raises SLFN12's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without CSF1 | 0.072 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 4.9); signed map (44.0, 7.4). **Vector** length 100, 29.9% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.56 to 12); *Chemokine receptors bind chemokines* (reactome, mean cos +0.52 to 8); *interferon gamma response* (hallmark, mean cos +0.53 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +24.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +22.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +38.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -6.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -7.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | colony stimulating factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,910,242-109,930,992 (+) |
| Ensembl biotype | protein_coding |
| Also known as | M-CSF, MCSF, MGC31930 |
| Gene groups (HGNC) | Colony stimulating factors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_ALPHA_RESPONSE, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 10 pathways, smallest: Other interleukin signaling; Developmental Cell Lineages; Interleukin-10 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P09603](https://www.uniprot.org/uniprotkb/P09603) (Macrophage colony-stimulating factor 1):

> Cytokine that plays an essential role in the regulation of survival, proliferation and differentiation of hematopoietic precursor cells, especially mononuclear phagocytes, such as macrophages and monocytes. Promotes the release of pro-inflammatory chemokines, and thereby plays an important role in innate immunity and in inflammatory processes. Plays an important role in the regulation of osteoclast proliferation and differentiation, the regulation of bone resorption, and is required for normal …

**Summary**, from NCBI Gene [1435](https://www.ncbi.nlm.nih.gov/gene/1435):

> The protein encoded by this gene is a cytokine that controls the production, differentiation, and function of macrophages. The active form of the protein is found extracellularly as a disulfide-linked homodimer, and is thought to be produced by proteolytic cleavage of membrane-bound precursors. The encoded protein may be involved in development of the placenta. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:2432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2432) · Entrez [1435](https://www.ncbi.nlm.nih.gov/gene/1435) · UniProt [P09603](https://www.uniprot.org/uniprotkb/P09603) · Ensembl [ENSG00000184371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184371)

## Data

Gene col 11527: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11527); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11527, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11527]; `tensor/DDL_lfc|DDL_z.npy` [11527]; `embed/gene_vectors.npy` [11527]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11527 or target_col == 11527). Every well: [[CSF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
