---
symbol: "RDH5"
type: "gene"
col: 5703
ensembl_id: "ENSG00000135437"
name: "retinol dehydrogenase 5"
location: "12q13.2"
module: 26
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# RDH5

*retinol dehydrogenase 5* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.44× (z +12.6, q 1e-33, up in 22 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.05 µM in 1 line (PANC-1 0.0679×); [[Omeprazole (drug)]] 0.5 µM in 1 line (SW1417 0.0908×).
> Its strongest partners by |cos| (69 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 31 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL19-AS1]] (+0.60, fdr 4e-04), [[TRAF3IP2-AS1]] (+0.59, fdr 5e-04), [[EFCAB5]] (+0.58, fdr 5e-05); moves opposite to [[TAMM41]] (-0.56, fdr 1e-04), [[GTF2H2C]] (-0.54, fdr 2e-04), [[ELP1]] (-0.54, fdr 9e-04, ⚠ not reproduced), [[STUB1]] (-0.54, fdr 3e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +12.6 | 1e-33 | 22/28 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +11.0 | 9e-26 | 1/1 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +9.8 | 3e-20 | 1/2 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +8.5 | 4e-15 | 1/10 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +6.3 | 3e-08 | 7/20 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.1 | 1e-07 | 7/41 (SW480, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.7 | 9e-07 | 1/10 (NCI-H460) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +5.1 | 2e-05 | 5/45 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.36×** | +4.3 | 9e-04 | 4/40 (SW480, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.001 | 12/43 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 6/29 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.015 | 5/38 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.6 | 0.015 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.052 | 2/43 (HT-29, A549) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.060 | 3/44 (NCI-H460, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.060 | 3/47 (SW1417, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.073 | 9/30 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.079 | 2/19 (NCI-H1573, LoVo) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.082 | 6/28 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Alpelisib (drug)]] 5 µM |  | **1.77×** | +3.0 | 0.084 | 0/17 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5703.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.05 µM in 1 line (PANC-1 0.0679×); [[Omeprazole (drug)]] 0.5 µM in 1 line (SW1417 0.0908×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.783× | -3.5 | 0.15 | 6/40 (HS-578T, A-427, …) | top dose only | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.710× | -3.5 | 0.15 | 7/32 (A498, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.45 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.05 µM 0.0679× (z -8.8) |
| [[SW1417 (line)]] | alt | 4.53 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0908× (z -8.5) |
| [[A-172 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.600 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.888 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.755 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL19-AS1]] | +0.60 | +0.58 / +0.25 | both halves | 4e-04 |  |
| [[TRAF3IP2-AS1]] | +0.59 | +0.49 / +0.23 | both halves | 5e-04 |  |
| [[EFCAB5]] | +0.58 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[AHI1-DT]] | +0.57 | +0.62 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[ALG1L9P]] | +0.57 | +0.59 / +0.30 | both halves | 2e-04 |  |
| [[CD96]] | +0.57 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[PNISR-AS1]] | +0.56 | +0.64 / +0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[NINJ2]] | +0.56 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[LINC01762]] | +0.56 | +0.59 / +0.26 | both halves | 4e-04 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.55 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[CDKN2B-AS1]] | +0.55 | +0.57 / +0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[TTC32]] | +0.54 | +0.52 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[MED28-DT]] | +0.54 | +0.47 / +0.37 | both halves | 8e-05 |  |
| [[RBM15-AS1]] | +0.54 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[INTS6-AS1]] | +0.53 | +0.50 / +0.33 | both halves | 1e-04 |  |
| [[GSTZ1]] | +0.53 | +0.41 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAMM41]] | -0.56 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[GTF2H2C]] | -0.54 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[ELP1]] | -0.54 | -0.49 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[STUB1]] | -0.54 | -0.35 / -0.28 | both halves | 3e-04 |  |
| [[MRPS34]] | -0.54 | -0.57 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[NDUFB10]] | -0.53 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[UTP6]] | -0.52 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[THYN1]] | -0.51 | -0.36 / -0.24 | both halves | 4e-04 |  |
| [[MIA3]] | -0.50 | -0.31 / -0.26 | both halves | 4e-04 |  |
| [[FAM98A]] | -0.50 | -0.50 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[PAPSS1]] | -0.50 | -0.46 / -0.09 | ⚠ not reproduced | 0.003 |  |
| [[GTF2H2]] | -0.50 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[CCDC112]] | -0.49 | -0.28 / -0.23 | both halves | 5e-04 |  |
| [[NARS2]] | -0.49 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[ZNHIT6]] | -0.48 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[MPHOSPH10]] | -0.48 | -0.40 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RDH5's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[OPRD1]] | B | OPRD1 activity raises RDH5's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.29× lower at baseline in the lines without OPRD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (10.1, 20.0); signed map (26.4, -4.6). **Vector** length 35.2, 3.49% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -0.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | retinol dehydrogenase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:55,720,367-55,724,705 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSD17B9, SDR9C5; previously RDH1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 9 pathways, smallest: Diseases associated with visual transduction; Diseases of the neuronal system; Retinoid cycle disease events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92781](https://www.uniprot.org/uniprotkb/Q92781) (Retinol dehydrogenase 5):

> Catalyzes the oxidation of cis-isomers of retinol, including 11-cis-, 9-cis-, and 13-cis-retinol in an NAD-dependent manner. Has no activity towards all-trans retinal (By similarity). Plays a significant role in 11-cis retinol oxidation in the retinal pigment epithelium cells (RPE). Also recognizes steroids (androsterone, androstanediol) as its substrates.

**Summary**, from NCBI Gene [5959](https://www.ncbi.nlm.nih.gov/gene/5959):

> This gene encodes an enzyme belonging to the short-chain dehydrogenases/reductases (SDR) family. This retinol dehydrogenase functions to catalyze the final step in the biosynthesis of 11-cis retinaldehyde, which is the universal chromophore of visual pigments. Mutations in this gene cause autosomal recessive fundus albipunctatus, a rare form of night blindness that is characterized by a delay in the regeneration of cone and rod photopigments. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:9940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9940) · Entrez [5959](https://www.ncbi.nlm.nih.gov/gene/5959) · UniProt [Q92781](https://www.uniprot.org/uniprotkb/Q92781) · Ensembl [ENSG00000135437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135437)

## Data

Gene col 5703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5703); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5703]; `tensor/DDL_lfc|DDL_z.npy` [5703]; `embed/gene_vectors.npy` [5703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5703 or target_col == 5703). Every well: [[RDH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
