---
symbol: "LNCRNA-IUR"
type: "gene"
col: 14432
ensembl_id: "ENSG00000245552"
name: "lncRNA imatinib upregulated"
location: "11q21"
module: 26
arm: "+"
pooled_cpm: 5.64
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# LNCRNA-IUR

*lncRNA imatinib upregulated* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +16.1, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.572× (z -6.0, q 1e-06, down in 22 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SW1417 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.05 µM in 1 line (J82 0.0605×); [[Captopril (drug)]] 0.5 µM in 1 line (BT-474 0.0594×); [[Asciminib (drug)]] 0.5 µM in 1 line (BT-474 0.0617×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02955]] (+0.75, fdr 1e-05), [[C2orf88]] (+0.73, fdr 7e-06), [[BTG3-AS1]] (+0.66, fdr 2e-05); moves opposite to [[CNEP1R1]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[IL19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +16.1 | 0e+00 | 35/38 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.48×** | +15.3 | 0e+00 | 10/11 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +12.3 | 1e-32 | 19/24 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +9.6 | 1e-19 | 9/15 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +7.1 | 2e-10 | 19/33 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.8 | 7e-07 | 20/44 (NCI-H2347, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.8 | 7e-07 | 13/36 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 10/46 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.016 | 11/37 (HS-578T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.072 | 10/47 (SW48, LoVo, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.072 | 7/46 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.092 | 8/40 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.092 | 11/46 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.094 | 7/46 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14432.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SW1417 0.154×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.05 µM in 1 line (J82 0.0605×); [[Captopril (drug)]] 0.5 µM in 1 line (BT-474 0.0594×); [[Asciminib (drug)]] 0.5 µM in 1 line (BT-474 0.0617×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -6.0 | 1e-06 | 22/44 (LOX-IMVI, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.703×** | -3.8 | 0.047 | 16/46 (RPMI-7951, KATO III, …) | rises with dose | composition shift |
| [[Delamanid (drug)]] 0.05 µM |  | 0.725× | -3.4 | 0.12 | 9/45 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.553× | -3.3 | 0.13 | 11/36 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.753× | -3.0 | 0.28 | 12/42 (RPMI-7951, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 4.69 | 0 | 2 | — | [[Captopril (drug)]] 0.5 µM 0.0594× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 10.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.20× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +8.8) | — |
| [[J82 (line)]] | alt | 2.63 | 0 | 1 | — | [[Belinostat (drug)]] 0.05 µM 0.0605× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 3.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +10.7) | — |
| [[NCI-H2347 (line)]] | alt | 5.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.48× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 4.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02955]] | +0.75 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[C2orf88]] | +0.73 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[BTG3-AS1]] | +0.66 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[LINC01762]] | +0.66 | +0.66 / +0.38 | both halves | 7e-05 |  |
| [[MED28-DT]] | +0.66 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PEBP4]] | +0.66 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SMG1-DT]] | +0.66 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[AXDND1]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[PIPOX]] | +0.65 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[DDX19A-DT]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.65 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PAXBP1-AS1]] | +0.64 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNEP1R1]] | -0.60 | -0.58 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL19]] | B | IL19 activity raises LNCRNA-IUR's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.54× lower at baseline in the lines without IL19 | 0.012 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LNCRNA-IUR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EDIL3-DT]] | B | EDIL3-DT activity raises LNCRNA-IUR's level | lines that do not express EDIL3-DT (25) vs lines expressing it (25) | 1.23× lower at baseline in the lines without EDIL3-DT | 0.017 | ⚠ within organs, on part of the lines; also absent: EDIL3, NALCN, DTNA |
| [[SLC2A9]] | B | SLC2A9 activity raises LNCRNA-IUR's level | lines that do not express SLC2A9 (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without SLC2A9 | 0.047 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises LNCRNA-IUR's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without ZNF341-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[CEMIP2]] | C | CEMIP2 activity raises LNCRNA-IUR's level | lines that do not express CEMIP2 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without CEMIP2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: KIFC3, SMARCA2, PLSCR2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.685). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.3, 19.1); signed map (25.2, -1.1). **Vector** length 50.9, 6.30% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +1.2 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.3 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -6.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | lncRNA imatinib upregulated |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q21 — chr11:95,150,539-95,234,391 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55755) · Entrez [101929295](https://www.ncbi.nlm.nih.gov/gene/101929295) · Ensembl [ENSG00000245552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245552)

## Data

Gene col 14432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14432); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14432]; `tensor/DDL_lfc|DDL_z.npy` [14432]; `embed/gene_vectors.npy` [14432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14432 or target_col == 14432). Every well: [[LNCRNA-IUR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNCRNA-IUR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
