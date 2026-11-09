---
symbol: "PMS2P3"
type: "gene"
col: 4850
ensembl_id: "ENSG00000127957"
name: "PMS1 homolog 2, mismatch repair system component pseudogene 3"
location: "7q11.23"
module: 168
arm: "+"
pooled_cpm: 4.07
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# PMS2P3

*PMS1 homolog 2, mismatch repair system component pseudogene 3* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.52× (z +8.5, q 8e-15, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.604× (z -3.9, q 0.025, down in 15 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Furosemide (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0632×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SW1417 0.0482×); [[Pyridoxine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0697×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P3-1]] (+0.89, fdr 7e-06, ⚠ same locus), [[ALG9]] (+0.75, fdr 7e-06), [[SNRPA1]] (+0.72, fdr 7e-06), [[TRIT1]] (+0.71, fdr 7e-06); moves opposite to [[SKIL]] (-0.64, fdr 1e-05), [[CUX1]] (-0.64, fdr 1e-05), [[ERCC6L2]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C21orf91]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SRP54-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.52×** | +8.5 | 8e-15 | 35/41 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.0 | 7e-10 | 23/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **4.98×** | +6.8 | 2e-09 | 27/37 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +6.3 | 4e-08 | 25/46 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.80×** | +4.8 | 2e-04 | 18/46 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.80×** | +4.7 | 2e-04 | 19/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.79×** | +4.7 | 2e-04 | 16/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.003 | 8/38 (Hs 766T, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.61×** | +3.8 | 0.008 | 14/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.008 | 11/43 (SK-MEL-2, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.008 | 15/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.40×** | +3.7 | 0.010 | 2/10 (MIA PaCa-2, LoVo) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +3.6 | 0.017 | 8/43 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.3 | 0.037 | 6/30 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.056 | 3/46 (A498, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.092 | 11/45 (RPMI-7951, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4850.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Furosemide (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0632×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (SW1417 0.0482×); [[Pyridoxine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0697×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.604×** | -3.9 | 0.025 | 15/44 (C-33 A, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.620×** | -3.9 | 0.025 | 14/25 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Thymol (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.025 | 15/46 (SHP-77, A549, …) | top dose only | position effect removed |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.671× | -3.2 | 0.17 | 9/46 (C32, HEC-1-A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.681× | -3.1 | 0.18 | 9/47 (KATO III, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.684× | -3.1 | 0.18 | 8/46 (AsPC-1, NCI-H1573, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.685× | -3.1 | 0.18 | 15/46 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 5.09 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0632× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.05 µM 0.0697× (z -9.0) |
| [[SW1417 (line)]] | alt | 4.38 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0482× (z -10.2) |
| [[A-172 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | +0.89 | +0.85 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ALG9]] | +0.75 | +0.80 / +0.67 | both halves | 7e-06 |  |
| [[SNRPA1]] | +0.72 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.71 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[ATPAF2]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MMS19]] | +0.71 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[FOXJ3]] | +0.67 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[SNX1]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NDUFAF7]] | +0.66 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[NAPB]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIL]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[CUX1]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.64 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[MED1]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[PTPRK]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SON]] | -0.60 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[PNRC2]] | -0.60 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H11A]] | -0.59 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[RASEF]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[EPC2]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C21orf91]] | B | C21orf91 activity lowers PMS2P3's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 1.33× higher at baseline in the lines without C21orf91 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRP54-AS1]] | C | PMS2P3's natural level strengthens SRP54-AS1's drug response | PMS2P3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.26; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.839). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-3.9, -13.2); signed map (-34.0, -9.6). **Vector** length 47.4, 5.67% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.7 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +6.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -2.9 |
|  | [[Thymol (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.3 | -3.1 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | PMS1 homolog 2, mismatch repair system component pseudogene 3 |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:75,510,931-75,516,235 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | PMS5, PMSR3; previously PMS2L9, PMS2L3 |
| Matched by | ensembl_id |

UniProt [Q13401](https://www.uniprot.org/uniprotkb/Q13401) carries no function annotation.

**Summary**, from NCBI Gene [5387](https://www.ncbi.nlm.nih.gov/gene/5387):

> Predicted to enable ATP hydrolysis activity and ATP-dependent DNA damage sensor activity. Predicted to be involved in mismatch repair and regulation of DNA-templated transcription. Predicted to be part of mismatch repair complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9128](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9128) · Entrez [5387](https://www.ncbi.nlm.nih.gov/gene/5387) · UniProt [Q13401](https://www.uniprot.org/uniprotkb/Q13401) · Ensembl [ENSG00000127957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127957)

## Data

Gene col 4850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4850); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4850]; `tensor/DDL_lfc|DDL_z.npy` [4850]; `embed/gene_vectors.npy` [4850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4850 or target_col == 4850). Every well: [[PMS2P3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMS2P3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
