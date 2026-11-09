---
symbol: "WDR91"
type: "gene"
col: 2681
ensembl_id: "ENSG00000105875"
name: "WD repeat domain 91"
location: "7q33"
module: 46
arm: "+"
pooled_cpm: 10.65
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# WDR91

*WD repeat domain 91* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +16.4, q 0e+00, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.775× (z -4.4, q 0.005, down in 16 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XRCC1]] (+0.55, fdr 1e-05), [[FOXJ2]] (+0.55, fdr 3e-05), [[TAPT1]] (+0.54, fdr 1e-05); moves opposite to [[MRPS28]] (-0.53, fdr 3e-05), [[UBE3D]] (-0.48, fdr 1e-04), [[CCT4]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2681.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +16.4 | 0e+00 | 38/43 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +12.2 | 2e-31 | 34/44 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.46×** | +11.1 | 2e-26 | 40/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +10.4 | 4e-23 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +9.3 | 1e-18 | 38/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.9 | 2e-13 | 33/43 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +7.2 | 5e-11 | 25/45 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +6.0 | 2e-07 | 23/47 (C32, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.10×** | +4.8 | 1e-04 | 17/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.5 | 3e-04 | 13/44 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.9 | 0.005 | 11/44 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.006 | 6/48 (LS 180, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.32×** | +3.4 | 0.027 | 5/47 (SW1417, CFPAC-1, …) | two highest doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +3.3 | 0.036 | 4/47 (RPMI-7951, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2681.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -4.4 | 0.005 | 16/48 (A498, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.722×** | -3.9 | 0.023 | 11/47 (A498, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.732×** | -3.8 | 0.023 | 11/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.762× | -3.4 | 0.11 | 14/46 (A498, HOP62, …) | all doses, flat |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.830× | -3.3 | 0.11 | 7/48 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.770× | -3.2 | 0.11 | 10/45 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 0.833× | -3.2 | 0.11 | 16/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.768× | -3.1 | 0.12 | 10/48 (HepG2/C3A, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.82 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +12.5) | — |
| [[SW480 (line)]] | alt | 9.19 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.86 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.110× (z -8.5) |
| [[A498 (line)]] | wt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -9.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 6.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +8.6) | — |
| [[HEC-1-A (line)]] | alt | 9.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -11.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 3.68 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0926× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 4.54 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0674× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 9.73 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[NCI-H2030 (line)]] | alt | 9.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 5.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 7.95 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0716× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 9.56 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0989× (z -9.4) |
| [[A-427 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC1]] | +0.55 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[FOXJ2]] | +0.55 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[TAPT1]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SYNJ1]] | +0.51 | +0.30 / +0.63 | both halves | 2e-04 |  |
| [[TGFB3]] | +0.50 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[CFAP418]] | +0.50 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[GORASP1]] | +0.48 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TYK2]] | +0.47 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CDKN2C]] | +0.47 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[SIX5]] | +0.47 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[ARHGEF40]] | +0.47 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[CCDC159]] | +0.46 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS28]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[UBE3D]] | -0.48 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[CCT4]] | -0.46 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[DFFA]] | -0.45 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[EXOC6B]] | -0.44 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[VTI1A]] | -0.43 | -0.44 / -0.47 | both halves | 3e-05 | same gene group |
| [[GARNL3]] | -0.42 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[C7orf50]] | -0.42 | -0.20 / -0.45 | ⚠ not reproduced | 8e-04 | same gene group |
| [[RAPSN]] | -0.42 | -0.26 / -0.48 | both halves | 3e-04 |  |
| [[RRP7BP-1]] | -0.42 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[BTBD9]] | -0.42 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[ERC1]] | -0.42 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[EDA]] | -0.40 | -0.44 / -0.23 | both halves | 5e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WDR91's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.368). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (17.8, -23.8); signed map (24.1, -18.8). **Vector** length 53.9, 7.10% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +3.8 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +16.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +0.1 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.0 | +0.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.0 | +1.1 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +1.0 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.5 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.8 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -2.3 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | +0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 91 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:135,183,839-135,211,555 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC049, SORF-1 |
| Gene groups (HGNC) | WD repeat domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: CDC42 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [A4D1P6](https://www.uniprot.org/uniprotkb/A4D1P6) (WD repeat-containing protein 91):

> Functions as a negative regulator of the PI3 kinase/PI3K activity associated with endosomal membranes via BECN1, a core subunit of the PI3K complex. By modifying the phosphatidylinositol 3-phosphate/PtdInsP3 content of endosomal membranes may regulate endosome fusion, recycling, sorting and early to late endosome transport. It is for instance, required for the delivery of cargos like BST2/tetherin from early to late endosome and thereby participates indirectly to their degradation by the …

**Summary**, from NCBI Gene [29062](https://www.ncbi.nlm.nih.gov/gene/29062):

> Enables phosphatidylinositol 3-kinase inhibitor activity. Involved in early endosome to late endosome transport and regulation of protein catabolic process. Located in cytosol; early endosome membrane; and late endosome membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24997) · Entrez [29062](https://www.ncbi.nlm.nih.gov/gene/29062) · UniProt [A4D1P6](https://www.uniprot.org/uniprotkb/A4D1P6) · Ensembl [ENSG00000105875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105875)

## Data

Gene col 2681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2681); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2681]; `tensor/DDL_lfc|DDL_z.npy` [2681]; `embed/gene_vectors.npy` [2681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2681 or target_col == 2681). Every well: [[WDR91 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR91.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
