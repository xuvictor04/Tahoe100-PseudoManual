---
symbol: "CFAP54"
type: "gene"
col: 12027
ensembl_id: "ENSG00000188596"
name: "cilia and flagella associated protein 54"
location: "12q23.1"
module: 26
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 44
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CFAP54

*cilia and flagella associated protein 54* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.84× (z +19.3, q 0e+00, up in 28 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Uridine (drug)]] 5 µM in 1 line (NCI-H661 0.230×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.194×); [[Tofacitinib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0523×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.75, fdr 1e-05), [[ARHGAP15]] (+0.74, fdr 7e-06), [[SYNPO2]] (+0.74, fdr 7e-06); moves opposite to [[MAST3]] (-0.64, fdr 7e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PITX1-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12027.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.84×** | +19.3 | 0e+00 | 28/34 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +15.6 | 0e+00 | 28/34 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.31×** | +12.0 | 9e-31 | 27/40 (HOP62, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.57×** | +11.9 | 1e-30 | 5/10 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +11.1 | 1e-26 | 10/15 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +10.6 | 3e-24 | 23/30 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +9.8 | 1e-20 | 4/6 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.53×** | +9.4 | 4e-19 | 25/36 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +7.0 | 2e-10 | 19/34 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +6.9 | 2e-10 | 18/32 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.88×** | +6.4 | 8e-09 | 13/35 (SW480, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +6.4 | 8e-09 | 15/36 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +4.5 | 3e-04 | 9/35 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.004 | 8/39 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.9 | 0.004 | 1/7 (A-172) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.009 | 10/38 (NCI-H460, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.011 | 6/39 (SW480, Hs 766T, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.023 | 6/35 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.061 | 5/40 (RKO, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12027.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Uridine (drug)]] 5 µM in 1 line (NCI-H661 0.230×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.194×); [[Tofacitinib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0523×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.798× | -3.2 | 0.51 | 9/38 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.806× | -3.1 | 0.51 | 6/35 (Hs 766T, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12027. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +16.4) | — |
| [[Hs 766T (line)]] | wt | 6.93 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +8.8) | [[Tofacitinib (drug)]] 0.5 µM 0.0523× (z -10.4) |
| [[RKO (line)]] | wt | 38.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -10.8) |
| [[A-427 (line)]] | wt | 32.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0428× (z -8.9) |
| [[A549 (line)]] | wt | 3.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.60× (z +8.5) | — |
| [[LoVo (line)]] | wt | 1.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 2.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +11.3) | — |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 1 | — | [[Uridine (drug)]] 5 µM 0.230× (z -219.5) |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12027), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.75 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP15]] | +0.74 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SYNPO2]] | +0.74 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.73 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.71 / +0.43 | both halves | 4e-05 |  |
| [[MYO16]] | +0.73 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[NQO1-DT]] | +0.72 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[SP140]] | +0.72 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.71 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[EYS]] | +0.71 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[GRM8]] | +0.71 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CIBAR1-DT]] | +0.71 | +0.64 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.64 | -0.63 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CFAP54's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CACNA2D1]] | B | CACNA2D1 activity raises CFAP54's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 1.85× lower at baseline in the lines without CACNA2D1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169 |
| [[CUBN]] | B | CUBN activity raises CFAP54's level | lines that do not express CUBN (21) vs lines expressing it (29) | 1.81× lower at baseline in the lines without CUBN | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC02813, ENSG00000263655, LINC01535; maybe low, not absent |
| [[LINC01592]] | B | LINC01592 activity raises CFAP54's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without LINC01592 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent |
| [[LINC01010]] | B | LINC01010 activity raises CFAP54's level | lines that do not express LINC01010 (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without LINC01010 | 0.090 | ⚠ within organs, on part of the lines; also absent: TRIML2, PHACTR1, LINC01776 |
| [[LINC02608]] | C | LINC02608 activity lowers CFAP54's level | lines that do not express LINC02608 (4) vs lines expressing it (46) | 3.02× higher at baseline in the lines without LINC02608 | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GNA14; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PITX1-AS1]] | B | CFAP54 activity lowers PITX1-AS1's level | lines that do not express CFAP54 (6) vs lines expressing it (44) | 2.03× higher at baseline in the lines without CFAP54 | 0.060 | ⚠ within organs, on part of the lines; also absent: LRP12, TMOD2, TBC1D19; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (25.2, 24.5); signed map (37.5, 14.3). **Vector** length 61.6, 10.1% of its response variance represented; |z| ≥ 3 in 891 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +19.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +15.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +12.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 54 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:96,489,571-96,875,555 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31514, FLJ44112; previously C12orf63, C12orf55 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N23](https://www.uniprot.org/uniprotkb/Q96N23) (Cilia- and flagella-associated protein 54):

> Required for assembly and function of cilia and flagella.

**Summary**, from NCBI Gene [144535](https://www.ncbi.nlm.nih.gov/gene/144535):

> Involved in sperm flagellum assembly. Predicted to be located in axoneme. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26456) · Entrez [144535](https://www.ncbi.nlm.nih.gov/gene/144535) · UniProt [Q96N23](https://www.uniprot.org/uniprotkb/Q96N23) · Ensembl [ENSG00000188596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188596)

## Data

Gene col 12027: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12027); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12027, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12027]; `tensor/DDL_lfc|DDL_z.npy` [12027]; `embed/gene_vectors.npy` [12027]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12027 or target_col == 12027). Every well: [[CFAP54 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP54.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
