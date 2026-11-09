---
symbol: "HYKK"
type: "gene"
col: 11996
ensembl_id: "ENSG00000188266"
name: "hydroxylysine kinase"
location: "15q25.1"
module: 30
arm: "+"
pooled_cpm: 3.04
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 12
n_dd_up_clean: 21
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# HYKK

*hydroxylysine kinase* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.43× (z +20.1, q 0e+00, up in 31 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.466× (z -8.8, q 6e-16, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OTX1]] (+0.62, fdr 1e-05), [[MPZL1]] (+0.61, fdr 6e-05), [[IER3IP1]] (+0.59, fdr 3e-04); moves opposite to [[USP40]] (-0.58, fdr 2e-04), [[RAD50]] (-0.57, fdr 1e-04), [[RPL7L1]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.43×** | +20.1 | 0e+00 | 31/33 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.04×** | +16.1 | 0e+00 | 40/45 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.77×** | +15.3 | 0e+00 | 38/42 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.64×** | +14.9 | 0e+00 | 34/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +11.0 | 3e-26 | 9/14 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.56×** | +10.8 | 2e-25 | 33/44 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +9.9 | 3e-21 | 15/26 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.21×** | +9.2 | 3e-18 | 22/31 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +7.9 | 2e-13 | 2/3 (A498, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.95×** | +7.4 | 7e-12 | 8/17 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.8 | 7e-10 | 13/31 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +6.7 | 8e-10 | 7/43 (NCI-H2030, KATO III, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.0 | 7e-08 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.5 | 1e-06 | 7/43 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.31×** | +5.1 | 2e-05 | 8/39 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.5 | 2e-04 | 7/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 6e-04 | 6/39 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +4.2 | 7e-04 | 4/43 (PANC-1, SW1417, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.007 | 3/41 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.010 | 2/26 (LS 180, LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.466×** | -8.8 | 6e-16 | 25/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.615×** | -5.6 | 6e-06 | 17/44 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.629×** | -5.4 | 1e-05 | 19/41 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.414×** | -5.3 | 1e-05 | 11/36 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.647×** | -5.0 | 5e-05 | 15/43 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.651×** | -5.0 | 6e-05 | 14/40 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -4.8 | 2e-04 | 16/42 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.670×** | -4.6 | 3e-04 | 12/33 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.696×** | -4.0 | 0.003 | 14/41 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.749×** | -3.2 | 0.083 | 7/42 (SW48, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.754×** | -3.2 | 0.083 | 8/40 (AN3 CA, HT-29, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.763×** | -3.1 | 0.083 | 8/39 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.22 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 4.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +9.5) | [[Cobimetinib (drug)]] 0.05 µM 0.0631× (z -11.5) |
| [[HT-29 (line)]] | alt | 3.30 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0681× (z -8.8) |
| [[LoVo (line)]] | wt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 5.94 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0454× (z -19.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 2.17 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0797× (z -9.4) |
| [[SW480 (line)]] | alt | 3.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +9.6) | — |
| [[A-172 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTX1]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MPZL1]] | +0.61 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[IER3IP1]] | +0.59 | +0.27 / +0.60 | both halves | 3e-04 |  |
| [[MIIP]] | +0.59 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TMEM139-AS1]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[UBTD1]] | +0.57 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[LMX1B]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ZNF250]] | +0.57 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[SEC61A2]] | +0.57 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[XKR8]] | +0.57 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[IFI27L1]] | +0.57 | +0.29 / +0.57 | both halves | 2e-04 |  |
| [[DENND10]] | +0.56 | +0.35 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP40]] | -0.58 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[RAD50]] | -0.57 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[RPL7L1]] | -0.56 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[SLC35A4]] | -0.56 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[R3HDM2]] | -0.55 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[RASEF]] | -0.53 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[ERCC6L2]] | -0.52 | -0.21 / -0.55 | both halves | 7e-04 |  |
| [[CRADD]] | -0.52 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[EDN1]] | -0.51 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[HNRNPH2]] | -0.51 | -0.29 / -0.48 | both halves | 3e-04 |  |
| [[ZNF260]] | -0.50 | -0.21 / -0.47 | both halves | 6e-04 |  |
| [[PUDP]] | -0.50 | -0.32 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HYKK's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYNGR1]] | B | SYNGR1 activity raises HYKK's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.13× lower at baseline in the lines without SYNGR1 | 0.051 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[LMX1B]] | B | LMX1B activity raises HYKK's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.23× lower at baseline in the lines without LMX1B | 0.070 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[EDN1]] | B | EDN1 activity raises HYKK's level | lines that do not express EDN1 (27) vs lines expressing it (23) | 1.25× lower at baseline in the lines without EDN1 | 0.084 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.4, 2.5); signed map (-41.1, -2.9). **Vector** length 44.6, 4.97% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +20.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +11.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +5.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.9 | +0.9 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +0.8 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.7 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.5 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | -0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | hydroxylysine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,507,564-78,537,372 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC123688; previously AGPHD1 |
| Gene groups (HGNC) | Small molecule kinases |
| Reactome | 2 pathways, smallest: Lysine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [A2RU49](https://www.uniprot.org/uniprotkb/A2RU49) (Hydroxylysine kinase):

> Catalyzes the GTP-dependent phosphorylation of 5-hydroxy-L-lysine.

**Summary**, from NCBI Gene [123688](https://www.ncbi.nlm.nih.gov/gene/123688):

> Enables hydroxylysine kinase activity. Predicted to be involved in obsolete lysine catabolic process. Predicted to be located in mitochondrial matrix. Implicated in chronic obstructive pulmonary disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34403) · Entrez [123688](https://www.ncbi.nlm.nih.gov/gene/123688) · UniProt [A2RU49](https://www.uniprot.org/uniprotkb/A2RU49) · Ensembl [ENSG00000188266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188266)

## Data

Gene col 11996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11996); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11996]; `tensor/DDL_lfc|DDL_z.npy` [11996]; `embed/gene_vectors.npy` [11996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11996 or target_col == 11996). Every well: [[HYKK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYKK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
